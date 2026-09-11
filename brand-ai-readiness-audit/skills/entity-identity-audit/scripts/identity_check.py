import sys
import json
import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url

def check_identity(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    base_url = get_base_url(html, url)
    
    try:
        data = extruct.extract(html, base_url=base_url, syntaxes=['json-ld'])
        json_ld = data.get('json-ld', [])
    except:
        json_ld = []

    has_org_schema = False
    same_as_links = []
    schema_desc = ""
    
    for item in json_ld:
        if isinstance(item, dict):
            type_val = item.get('@type', '')
            if type_val == 'Organization' or type_val == 'LocalBusiness':
                has_org_schema = True
                if 'sameAs' in item:
                    val = item['sameAs']
                    if isinstance(val, list):
                        same_as_links.extend(val)
                    else:
                        same_as_links.append(val)
                if 'description' in item:
                    schema_desc = item['description']
                    
    if not has_org_schema:
        findings.append({
            "id": "IDENT-001",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "Missing Organization/LocalBusiness Schema",
            "severity": "high",
            "evidence": "No JSON-LD block of type 'Organization' or 'LocalBusiness' was found.",
            "suggested_action": {
                "summary": "Add Organization Schema",
                "detail": "Implement Organization schema to explicitly define your brand identity to search engines.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    if has_org_schema and not same_as_links:
        findings.append({
            "id": "IDENT-002",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "No sameAs links in Organization schema",
            "severity": "high",
            "evidence": "Organization schema was found, but it lacks the 'sameAs' property pointing to social or knowledge graph profiles.",
            "suggested_action": {
                "summary": "Add sameAs links to establish identity",
                "detail": "Include links to Wikipedia, LinkedIn, Twitter, etc., to disambiguate the brand name from generic terms.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    # Consistency check
    meta_desc = soup.find('meta', attrs={'name': 'description'})
    meta_desc_val = meta_desc.get('content', '') if meta_desc else ""
    
    og_desc = soup.find('meta', property='og:description')
    og_desc_val = og_desc.get('content', '') if og_desc else ""
    
    descriptions = [d for d in [schema_desc, meta_desc_val, og_desc_val] if d]
    if len(set(descriptions)) > 1:
         findings.append({
            "id": "IDENT-003",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "Inconsistent brand descriptions",
            "severity": "medium",
            "evidence": f"Found diverging descriptions across meta tag, OG tag, and JSON-LD: {list(set(descriptions))[:2]}...",
            "suggested_action": {
                "summary": "Harmonize core brand description",
                "detail": "Ensure that the primary description is consistent across meta, OG, and JSON-LD to avoid confusing AI systems.",
                "priority": "medium",
                "effort": "low"
            }
        })
        
    # About page check
    links = soup.find_all('a', href=True)
    has_about = False
    for link in links:
        href = link['href'].lower()
        if 'about' in href or 'who-we-are' in href:
            has_about = True
            break
            
    if not has_about:
        findings.append({
            "id": "IDENT-004",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "Missing explicit 'About' page link",
            "severity": "medium",
            "evidence": "Scanned all on-page links; no link containing 'about' or 'who-we-are' was found.",
            "suggested_action": {
                "summary": "Add a clear About page link to navigation",
                "detail": "A dedicated About page helps establish brand identity and authority.",
                "priority": "medium",
                "effort": "low"
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
        all_findings.extend(check_identity(url, html))
    except Exception as e:
        all_findings.append({
            "id": "IDENT-ERR",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "Failed to fetch page for identity audit",
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
