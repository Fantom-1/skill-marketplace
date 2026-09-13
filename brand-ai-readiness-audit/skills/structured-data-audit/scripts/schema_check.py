import sys
import json
import re
import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

def is_blocked_response(resp):
    if resp.status_code in (403, 429):
        return True
    html = resp.text or ""
    html_lower = html.lower()
    if "<title>just a moment...</title>" in html_lower or "<title>attention required! | cloudflare</title>" in html_lower:
        return True
    if "cf-chl-bypass" in html or "cf-browser-verification" in html or "challenge-platform" in html or "_cf_chl_opt" in html:
        return True
    if resp.status_code != 200 and ("cloudflare" in html_lower or "captcha" in html_lower or "access denied" in html_lower):
        return True
    return False

def is_spa_shell(html, soup):
    text = soup.body.get_text(separator=' ', strip=True) if soup.body else ""
    words = len(text.split())
    markers = bool(re.search(r'id=["\'](?:root|app|__next)["\']|__NEXT_DATA__|window\.__INITIAL_STATE__', html))
    return words < 100 or (words < 300 and markers)

def check_structured_data(url, html, spa_detected):
    findings = []
    try:
        base_url = get_base_url(html, url)
    except Exception:
        base_url = url
    
    confidence = "low" if spa_detected else "high"
    spa_note = "[SPA/interstitial shell detected - JS rendering required] " if spa_detected else ""
    base_severity = "medium" if spa_detected else "high"

    # Extract metadata
    try:
        data = extruct.extract(html, base_url=base_url, syntaxes=['json-ld', 'microdata'])
        json_ld = data.get('json-ld', []) if isinstance(data, dict) else []
        microdata = data.get('microdata', []) if isinstance(data, dict) else []
        combined_data = json_ld + microdata
    except Exception:
        combined_data = []
        
    if not combined_data:
        findings.append({
            "id": "SCHEMA-001",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "No JSON-LD structured data found",
            "severity": base_severity,
            "confidence": confidence,
            "evidence": spa_note + "extruct parser found 0 JSON-LD or microdata objects on the page.",
            "suggested_action": {
                "summary": "Implement schema.org JSON-LD",
                "detail": "Add standard schema.org types like Organization, WebSite, or Product to help AI assistants understand your entities.",
                "priority": base_severity,
                "effort": "medium"
            }
        })
    else:
        missing_names = []
        target_types = {'Organization', 'Product', 'LocalBusiness', 'Article', 'Person'}
        
        for item in combined_data:
            if isinstance(item, dict):
                item_type = item.get('@type', 'Unknown')
                # handle lists in type
                if isinstance(item_type, list):
                    has_target = any(t in target_types for t in item_type)
                    t_str = str(item_type)
                else:
                    has_target = item_type in target_types
                    t_str = item_type

                if has_target:
                    name = item.get('name')
                    if not name and 'properties' in item:
                        name = item['properties'].get('name')
                        
                    headline = item.get('headline')
                    if not headline and 'properties' in item:
                        headline = item['properties'].get('headline')
                        
                    if not name and not headline:
                        missing_names.append(t_str)

        if missing_names:
            findings.append({
                "id": "SCHEMA-002",
                "skill_source": "structured-data-audit",
                "category": "discoverability",
                "title": "Missing required properties in Structured Data",
                "severity": "medium",
                "confidence": confidence,
                "evidence": spa_note + f"Found these types missing a 'name' or 'headline' property: {', '.join(missing_names)}",
                "suggested_action": {
                    "summary": "Ensure all schema blocks have a name",
                    "detail": "Provide a descriptive name property for all schema.org entities.",
                    "priority": "medium",
                    "effort": "low"
                }
            })

    return findings

def check_meta_tags(url, html, spa_detected):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    confidence = "low" if spa_detected else "high"
    spa_note = "[SPA/interstitial shell detected] " if spa_detected else ""
    base_severity = "medium" if spa_detected else "high"
    
    # Title & Meta Description
    title_text = soup.title.get_text(strip=True) if soup.title else ""
    desc = soup.find('meta', attrs={'name': re.compile(r'^description$', re.I)})
    desc_content = (desc.get('content') or '').strip() if desc else ""
    
    if not title_text or len(title_text) < 5:
        findings.append({
            "id": "SCHEMA-003",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "Missing or very short <title>",
            "severity": base_severity,
            "confidence": confidence,
            "evidence": spa_note + f"Title tag found: {title_text if title_text else 'None'}",
            "suggested_action": {
                "summary": "Add a descriptive <title> tag",
                "detail": "Include a meaningful, brand-inclusive title.",
                "priority": base_severity,
                "effort": "low"
            }
        })
        
    if not desc_content or len(desc_content) < 10:
        findings.append({
            "id": "SCHEMA-004",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "Missing <meta description>",
            "severity": base_severity,
            "confidence": confidence,
            "evidence": spa_note + "No meta description found, or it's too short.",
            "suggested_action": {
                "summary": "Add a descriptive meta description",
                "detail": "Provide a 150-160 character summary of the page.",
                "priority": base_severity,
                "effort": "low"
            }
        })
        
    # OpenGraph
    og_title = soup.find('meta', property=re.compile(r'^og:title$', re.I))
    og_desc = soup.find('meta', property=re.compile(r'^og:description$', re.I))
    
    if not og_title or not og_desc:
        findings.append({
            "id": "SCHEMA-005",
            "skill_source": "structured-data-audit",
            "category": "discoverability",
            "title": "Missing OpenGraph tags",
            "severity": "medium",
            "confidence": confidence,
            "evidence": spa_note + f"og:title present: {bool(og_title)}, og:description present: {bool(og_desc)}",
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
    if images and len(images_no_alt) >= 3 and (len(images_no_alt) / len(images)) > 0.5:
        findings.append({
            "id": "SCHEMA-006",
            "skill_source": "structured-data-audit",
            "category": "engagement",
            "title": "Facts locked in images (Missing alt text)",
            "severity": "medium",
            "confidence": confidence,
            "evidence": spa_note + f"{len(images_no_alt)} out of {len(images)} images are missing alt text.",
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
        resp = requests.get(url, headers=HEADERS, timeout=15, verify=False)
        html = resp.text
        if is_blocked_response(resp):
            all_findings.append({
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
            print(json.dumps({"findings": all_findings}, indent=2))
            return
        
        soup = BeautifulSoup(html, 'html.parser')
        spa_detected = is_spa_shell(html, soup)
        
        all_findings.extend(check_structured_data(url, html, spa_detected))
        all_findings.extend(check_meta_tags(url, html, spa_detected))
        
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
