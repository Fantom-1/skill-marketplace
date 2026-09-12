import sys
import json
import re
import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url
from datetime import datetime, timezone
from urllib.parse import urlparse

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

def check_freshness(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    try:
        base_url = get_base_url(html, url)
    except Exception:
        base_url = url
    
    # 1. & 2. Date signals
    try:
        data = extruct.extract(html, base_url=base_url, syntaxes=['json-ld'])
        json_ld = data.get('json-ld', []) if isinstance(data, dict) else []
    except Exception:
        json_ld = []

    dates_found = []
    
    # Search JSON-LD
    for item in json_ld:
        if isinstance(item, dict):
            if 'datePublished' in item and item['datePublished']:
                dates_found.append(str(item['datePublished']))
            if 'dateModified' in item and item['dateModified']:
                dates_found.append(str(item['dateModified']))

    # Search HTML <time> tags
    for time_tag in soup.find_all('time'):
        dt = time_tag.get('datetime')
        if dt:
            dates_found.append(str(dt))
            
    if not dates_found:
        findings.append({
            "id": "FRESH-001",
            "skill_source": "freshness-corroboration",
            "category": "discoverability",
            "title": "No date signals found",
            "severity": "medium",
            "evidence": "No <time> tags or JSON-LD date properties were found.",
            "suggested_action": {
                "summary": "Add publication and modification dates",
                "detail": "Use standard schema.org datePublished/dateModified and HTML5 <time> elements so AI knows the freshness of the content.",
                "priority": "medium",
                "effort": "low"
            }
        })
    else:
        # Check staleness
        is_stale = False
        stale_date = ""
        for d in dates_found:
            try:
                clean_d = d.strip().replace('Z', '+00:00')
                date_obj = datetime.fromisoformat(clean_d)
                now = datetime.now(timezone.utc) if date_obj.tzinfo else datetime.now()
                if (now - date_obj).days > 365:
                    is_stale = True
                    stale_date = d
                    break
            except Exception:
                m = re.search(r'(\d{4})-(\d{2})-(\d{2})', str(d))
                if m:
                    try:
                        date_obj = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                        if (datetime.now() - date_obj).days > 365:
                            is_stale = True
                            stale_date = d
                            break
                    except Exception:
                        pass
                
        if is_stale:
            findings.append({
                "id": "FRESH-002",
                "skill_source": "freshness-corroboration",
                "category": "discoverability",
                "title": "Content appears stale (>1 year old)",
                "severity": "high",
                "evidence": f"Found date '{stale_date}' which is more than a year old.",
                "suggested_action": {
                    "summary": "Update content and refresh dateModified",
                    "detail": "AI systems prefer fresh content. Review and update the page, then update the schema dateModified.",
                    "priority": "high",
                    "effort": "medium"
                }
            })

    # 3. Copyright year outdated
    footer = soup.find('footer')
    if footer:
        footer_text = footer.get_text()
    else:
        footer_text = soup.body.get_text()[-1000:] if soup.body else ""
        
    copyright_match = re.search(r'(?:Copyright|©).*?([12][0-9]{3})', footer_text, re.IGNORECASE)
    if copyright_match:
        try:
            year = int(copyright_match.group(1))
            current_year = datetime.now().year
            if year < current_year:
                findings.append({
                    "id": "FRESH-003",
                    "skill_source": "freshness-corroboration",
                    "category": "discoverability",
                    "title": "Outdated copyright year",
                    "severity": "medium",
                    "evidence": f"Found copyright year {year}, but current year is {current_year}.",
                    "suggested_action": {
                        "summary": "Update copyright year",
                        "detail": "A stale copyright year is a strong negative freshness signal to automated systems.",
                        "priority": "medium",
                        "effort": "low"
                    }
                })
        except Exception:
            pass

    # 4. Inconsistent facts (Title vs H1)
    title = soup.title.get_text(strip=True) if soup.title else ""
    h1 = soup.find('h1')
    h1_text = h1.get_text(strip=True) if h1 else ""
    
    if title and h1_text:
        title_words = set(re.findall(r'\w+', title.lower()))
        h1_words = set(re.findall(r'\w+', h1_text.lower()))
        stop_words = {'the', 'a', 'an', 'and', 'or', 'of', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'is', 'home', 'page', 'official', 'site', 'welcome'}
        title_meaningful = title_words - stop_words
        h1_meaningful = h1_words - stop_words
        if title_meaningful and h1_meaningful and len(title_meaningful.intersection(h1_meaningful)) == 0:
            findings.append({
                "id": "FRESH-004",
                "skill_source": "freshness-corroboration",
                "category": "discoverability",
                "title": "Inconsistent on-page facts (Title vs H1)",
                "severity": "high",
                "evidence": f"Title ('{title}') and H1 ('{h1_text}') have zero overlap in words, indicating potential confusion.",
                "suggested_action": {
                    "summary": "Align Title and H1 tags",
                    "detail": "Ensure your primary H1 heading and page <title> are topically consistent to give strong entity signals.",
                    "priority": "high",
                    "effort": "low"
                }
            })
            
    # 5. Corroboration (Outbound links)
    links = soup.find_all('a', href=True)
    current_netloc = urlparse(url).netloc.lower()
    external_links = []
    for l in links:
        href = l.get('href', '')
        if href.startswith('http'):
            try:
                target_netloc = urlparse(href).netloc.lower()
                if target_netloc and target_netloc != current_netloc:
                    external_links.append(href)
            except Exception:
                pass
    
    if len(external_links) == 0:
        findings.append({
            "id": "FRESH-005",
            "skill_source": "freshness-corroboration",
            "category": "discoverability",
            "title": "No external corroborating links",
            "severity": "medium",
            "evidence": "Found 0 external outbound links.",
            "suggested_action": {
                "summary": "Add citations or links to trusted sources",
                "detail": "Linking to authoritative external sources (like partners, media coverage, Wikipedia) helps ground the entity in the wider knowledge graph.",
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
        
        all_findings.extend(check_freshness(url, html))
        
    except Exception as e:
        all_findings.append({
            "id": "FRESH-ERR",
            "skill_source": "freshness-corroboration",
            "category": "discoverability",
            "title": "Failed to fetch page for freshness audit",
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

