import sys
import json
import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

IDENTITY_TYPES = {
    'organization', 'localbusiness', 'corporation', 'educationalorganization',
    'ngo', 'governmentorganization', 'newsmediaorganization', 'performinggroup',
    'sportsorganization', 'financialservice', 'medicalorganization', 'automotivebusiness',
    'foodestablishment', 'store', 'onlinebusiness', 'techarticle', 'brand',
    'website', 'project', 'person', 'service', 'product'
}

SOCIAL_DOMAINS = [
    'twitter.com', 'x.com', 'linkedin.com', 'github.com', 'wikipedia.org',
    'wikidata.org', 'facebook.com', 'instagram.com', 'youtube.com', 'medium.com',
    'discord.gg', 'discord.com', 't.me', 'telegram.me'
]

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

def extract_all_schema_items(data):
    """Recursively extracts all dict items from extruct output across json-ld, microdata, rdfa."""
    items = []
    if not isinstance(data, dict):
        return items

    def _traverse(obj):
        if isinstance(obj, dict):
            # Check for @graph or nested items
            if "@graph" in obj and isinstance(obj["@graph"], list):
                for sub in obj["@graph"]:
                    _traverse(sub)
            items.append(obj)
            for k, v in obj.items():
                if k != "@graph":
                    _traverse(v)
        elif isinstance(obj, list):
            for elem in obj:
                _traverse(elem)

    for syntax in ['json-ld', 'microdata', 'rdfa']:
        syntax_data = data.get(syntax, [])
        _traverse(syntax_data)

    return items

def get_item_types(item):
    """Extracts a set of lowercased type names from a schema item dict."""
    types = set()
    if not isinstance(item, dict):
        return types
    
    raw_type = item.get('@type') or item.get('type') or item.get('@category')
    if not raw_type:
        return types

    if isinstance(raw_type, list):
        raw_types = raw_type
    else:
        raw_types = [raw_type]

    for t in raw_types:
        if isinstance(t, str):
            clean_t = t.split('/')[-1].split('#')[-1].strip().lower()
            if clean_t:
                types.add(clean_t)
    return types

def extract_same_as(item):
    """Extracts sameAs URLs from a schema item."""
    urls = []
    if not isinstance(item, dict):
        return urls
    val = item.get('sameAs') or item.get('same_as')
    if isinstance(val, list):
        for v in val:
            if isinstance(v, str) and v.strip():
                urls.append(v.strip())
            elif isinstance(v, dict) and ('@id' in v or 'url' in v):
                u = v.get('@id') or v.get('url')
                if u:
                    urls.append(str(u).strip())
    elif isinstance(val, str) and val.strip():
        urls.append(val.strip())
    elif isinstance(val, dict):
        u = val.get('@id') or val.get('url')
        if u:
            urls.append(str(u).strip())
    return urls

def tokenize(text):
    return set(re.findall(r'\w+', text.lower()))

def is_substantially_different(d1, d2):
    """Returns True only if two descriptions have contradictory/unrelated content."""
    s1, s2 = d1.strip().lower(), d2.strip().lower()
    if not s1 or not s2 or s1 == s2:
        return False
    if s1 in s2 or s2 in s1:
        return False
    
    t1, t2 = tokenize(s1), tokenize(s2)
    if min(len(t1), len(t2)) < 5:
        return False
        
    jaccard = len(t1 & t2) / float(len(t1 | t2)) if (t1 | t2) else 1.0
    return jaccard < 0.20

def check_identity(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    try:
        base_url = get_base_url(html, url)
    except Exception:
        base_url = url
    
    try:
        extruct_data = extruct.extract(html, base_url=base_url, syntaxes=['json-ld', 'microdata', 'rdfa'])
    except Exception:
        extruct_data = {}

    all_items = extract_all_schema_items(extruct_data)
    
    has_org_schema = False
    same_as_links = []
    schema_desc = ""
    
    for item in all_items:
        types = get_item_types(item)
        if types & IDENTITY_TYPES:
            has_org_schema = True
            links = extract_same_as(item)
            if links:
                same_as_links.extend(links)
            if not schema_desc and 'description' in item and isinstance(item['description'], str):
                schema_desc = item['description'].strip()
                
    # Also check HTML for social / identity profile links
    html_links = soup.find_all(['a', 'link'], href=True)
    social_html_links = []
    for l in html_links:
        href = (l.get('href') or '').lower()
        if any(domain in href for domain in SOCIAL_DOMAINS):
            social_html_links.append(href)

    if not has_org_schema:
        findings.append({
            "id": "IDENT-001",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "Missing Organization/Brand Schema",
            "severity": "high",
            "evidence": "No structured data (JSON-LD, Microdata, RDFa) block of type Organization, Brand, LocalBusiness, or WebSite was found.",
            "suggested_action": {
                "summary": "Add Organization or Brand Schema",
                "detail": "Implement Organization schema to explicitly define your brand identity to AI search engine crawlers.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    if has_org_schema and not same_as_links:
        if social_html_links:
            findings.append({
                "id": "IDENT-002",
                "skill_source": "entity-identity-audit",
                "category": "discoverability",
                "title": "No sameAs links in Organization schema",
                "severity": "medium",
                "evidence": "Organization schema was found with social links present in HTML, but schema lacks the 'sameAs' property pointing to those profiles.",
                "suggested_action": {
                    "summary": "Add sameAs links to schema",
                    "detail": "Include links to Wikipedia, LinkedIn, Twitter, GitHub, etc., in your JSON-LD sameAs array to disambiguate the brand name.",
                    "priority": "medium",
                    "effort": "low"
                }
            })
        else:
            findings.append({
                "id": "IDENT-002",
                "skill_source": "entity-identity-audit",
                "category": "discoverability",
                "title": "No sameAs links or identity profiles found",
                "severity": "high",
                "evidence": "Organization schema was found, but it lacks 'sameAs' links and no external social profile links were detected in HTML.",
                "suggested_action": {
                    "summary": "Add sameAs links to establish identity",
                    "detail": "Include links to Wikipedia, LinkedIn, Twitter, etc., to disambiguate the brand name from generic terms.",
                    "priority": "high",
                    "effort": "low"
                }
            })
        
    # Consistency check
    meta_desc = soup.find('meta', attrs={'name': re.compile(r'^description$', re.I)})
    meta_desc_val = (meta_desc.get('content') or '').strip() if meta_desc else ""
    
    og_desc = soup.find('meta', property=re.compile(r'^og:description$', re.I))
    og_desc_val = (og_desc.get('content') or '').strip() if og_desc else ""
    
    descriptions = [("Schema", schema_desc), ("Meta", meta_desc_val), ("OpenGraph", og_desc_val)]
    active_descs = [(label, val) for label, val in descriptions if val]
    
    found_inconsistency = False
    for i in range(len(active_descs)):
        for j in range(i + 1, len(active_descs)):
            l1, d1 = active_descs[i]
            l2, d2 = active_descs[j]
            if is_substantially_different(d1, d2):
                found_inconsistency = True
                evidence_text = f"Found contradictory descriptions between {l1} ('{d1[:60]}...') and {l2} ('{d2[:60]}...')."
                break
        if found_inconsistency:
            break

    if found_inconsistency:
        findings.append({
            "id": "IDENT-003",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "Contradictory brand descriptions",
            "severity": "medium",
            "evidence": evidence_text,
            "suggested_action": {
                "summary": "Harmonize core brand description",
                "detail": "Ensure that primary brand messaging is consistent across meta, OG, and JSON-LD to avoid confusing AI systems.",
                "priority": "medium",
                "effort": "low"
            }
        })
        
    # About page check
    parsed_url = urlparse(url)
    domain_lower = parsed_url.netloc.lower()
    path_lower = parsed_url.path.lower()
    
    # Web applications or app interfaces (e.g. app.uniswap.org, web.whatsapp.com, app.slack.com) don't require marketing About links
    is_web_app = (
        domain_lower.startswith('app.') or
        domain_lower.startswith('web.') or
        domain_lower.startswith('messages.') or
        domain_lower.startswith('forum.') or
        domain_lower.startswith('forums.') or
        '/trade/' in path_lower or
        '/browse' in path_lower or
        '/login' in path_lower or
        '/flow/login' in path_lower
    )

    has_about = False
    about_keywords = ['about', 'who-we-are', 'our-story', 'company', 'team', 'mission', 'overview', 'info', 'faq', 'docs', 'documentation', 'story', 'learn']
    
    for link in html_links:
        href = (link.get('href') or '').lower()
        text = link.get_text(strip=True).lower()
        aria = (link.get('aria-label') or '').lower()
        title_attr = (link.get('title') or '').lower()
        
        combined_text = f"{href} {text} {aria} {title_attr}"
        if any(kw in combined_text for kw in about_keywords):
            has_about = True
            break
            
    if not has_about and not is_web_app:
        findings.append({
            "id": "IDENT-004",
            "skill_source": "entity-identity-audit",
            "category": "discoverability",
            "title": "Missing explicit 'About' or 'Company' page link",
            "severity": "medium",
            "evidence": "Scanned all on-page navigation links; no link pointing to 'About', 'Company', 'Team', or 'Docs' was found.",
            "suggested_action": {
                "summary": "Add a clear About/Company link to navigation",
                "detail": "A dedicated About or Company page helps establish brand identity and authority for AI models.",
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


