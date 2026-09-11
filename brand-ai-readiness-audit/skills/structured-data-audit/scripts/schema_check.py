import sys
import json
import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url

def check_structured_data(url, html):
    findings = []
    base_url = get_base_url(html, url)
    
    # Extract metadata
    try:
        data = extruct.extract(html, base_url=base_url, syntaxes=['json-ld'])
        json_ld = data.get('json-ld', [])
    except Exception as e:
        json_ld = []
        
    if not json_ld:
        findings.append({
            "id": "SCHEMA-001",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "No JSON-LD structured data found",
            "severity": "high",
            "evidence": "extruct parser found 0 JSON-LD objects on the page.",
            "suggested_action": {
                "summary": "Implement schema.org JSON-LD",
                "detail": "Add standard schema.org types like Organization, WebSite, or Product to help AI assistants understand your entities.",
                "priority": "high",
                "effort": "medium"
            }
        })
    else:
        # Check if there are some basic issues with the schema
        missing_names = []
        for item in json_ld:
            if isinstance(item, dict) and '@type' in item:
                if 'name' not in item and 'headline' not in item:
                    missing_names.append(item['@type'])
        if missing_names:
            findings.append({
                "id": "SCHEMA-002",
                "skill_source": "structured-data-audit",
                "category": "discoverability",
                "title": "Missing required properties in JSON-LD",
                "severity": "medium",
                "evidence": f"Found these types missing a 'name' or 'headline' property: {', '.join(missing_names)}",
                "suggested_action": {
                    "summary": "Ensure all schema blocks have a name",
                    "detail": "Provide a descriptive name property for all schema.org entities.",
                    "priority": "medium",
                    "effort": "low"
                }
            })

    return findings

def check_meta_tags(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    
    # Title & Meta Description
    title = soup.title
    desc = soup.find('meta', attrs={'name': 'description'})
    
    if not title or not title.string or len(title.string.strip()) < 5:
        findings.append({
            "id": "SCHEMA-003",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "Missing or very short <title>",
            "severity": "high",
            "evidence": f"Title tag found: {title.string if title else 'None'}",
            "suggested_action": {
                "summary": "Add a descriptive <title> tag",
                "detail": "Include a meaningful, brand-inclusive title.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    if not desc or not desc.get('content') or len(desc.get('content').strip()) < 10:
        findings.append({
            "id": "SCHEMA-004",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "Missing <meta description>",
            "severity": "high",
            "evidence": "No meta description found, or it's too short.",
            "suggested_action": {
                "summary": "Add a descriptive meta description",
                "detail": "Provide a 150-160 character summary of the page.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    # OpenGraph
    og_title = soup.find('meta', property='og:title')
    og_desc = soup.find('meta', property='og:description')
    
    if not og_title or not og_desc:
        findings.append({
            "id": "SCHEMA-005",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "Missing OpenGraph tags",
            "severity": "medium",
            "evidence": f"og:title present: {bool(og_title)}, og:description present: {bool(og_desc)}",
            "suggested_action": {
                "summary": "Implement OpenGraph tags",
                "detail": "Add standard OpenGraph tags (og:title, og:description, og:image) for better snippet rendering across platforms and assistants.",
                "priority": "medium",
                "effort": "low"
            }
        })

    # Images missing alt text
    images = soup.find_all('img')
    images_no_alt = [img for img in images if not img.get('alt')]
    if images and (len(images_no_alt) / len(images)) > 0.5:
        findings.append({
            "id": "SCHEMA-006",
            "skill_source": "structured-data-audit",
            "category": "engagement",
            "title": "Facts locked in images (Missing alt text)",
            "severity": "medium",
            "evidence": f"{len(images_no_alt)} out of {len(images)} images are missing alt text.",
            "suggested_action": {
                "summary": "Add descriptive alt attributes",
                "detail": "If images contain facts or text, ensure they have alt tags so AI can extract the data.",
                "priority": "medium",
                "effort": "medium"
            }
        })

    return findings

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL provided"}))
        sys.exit(1)
        
    url = sys.argv[1]
    if not url.startswith('http'):
        url = 'https://' + url
        
    all_findings = []
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=15)
        html = resp.text
        if resp.status_code != 200 or "<title>Just a moment...</title>" in html or "cloudflare" in html.lower() or "captcha" in html.lower():
            findings.append({
                "id": "SKILLS-BLOCKED",
                "skill_source": "skills",
                "category": "discoverability",
                "title": f"Site Blocked Bot Access ({resp.status_code})",
                "severity": "critical",
                "evidence": f"Status: {resp.status_code}. Content indicates bot challenge or block.",
                "suggested_action": {
                    "summary": "Allow AI crawlers",
                    "detail": "Configure WAF/Cloudflare to whitelist known AI crawlers.",
                    "priority": "critical",
                    "effort": "low"
                }
            })
            return findings
        
        all_findings.extend(check_structured_data(url, html))
        all_findings.extend(check_meta_tags(url, html))
        
    except Exception as e:
        all_findings.append({
            "id": "SCHEMA-ERR",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "Failed to fetch page for schema audit",
            "severity": "critical",
            "evidence": str(e),
            "suggested_action": {
                "summary": "Ensure page is reachable",
                "detail": "Could not fetch the HTML.",
                "priority": "critical",
                "effort": "medium"
            }
        })
        
    print(json.dumps({"findings": all_findings}, indent=2))

if __name__ == "__main__":
    main()
