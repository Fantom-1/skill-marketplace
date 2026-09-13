import sys
import os

# Add shared directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from shared.bot_detection import is_blocked_response
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


def is_spa_shell(html, soup):
    text = soup.body.get_text(separator=' ', strip=True) if soup.body else ""
    words = len(text.split())
    markers = bool(re.search(r'id=["\'](?:root|app|__next)["\']|__NEXT_DATA__|window\.__INITIAL_STATE__', html))
    return words < 100 or (words < 300 and markers)

def check_freshness(url, html, headers_dict):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    try:
        base_url = get_base_url(html, url)
    except Exception:
        base_url = url
    
    spa_detected = is_spa_shell(html, soup)
    confidence = "low" if spa_detected else "high"
    spa_note = "[SPA/interstitial shell detected] " if spa_detected else ""

    # 1. & 2. Date signals
    try:
        data = extruct.extract(html, base_url=base_url, syntaxes=['json-ld', 'microdata'])
        json_ld = data.get('json-ld', []) if isinstance(data, dict) else []
    except Exception:
        json_ld = []

    dates_found = []
    
    for item in json_ld:
        if isinstance(item, dict):
            if 'datePublished' in item and item['datePublished']:
                dates_found.append(str(item['datePublished']))
            if 'dateModified' in item and item['dateModified']:
                dates_found.append(str(item['dateModified']))

    for time_tag in soup.find_all('time'):
        dt = time_tag.get('datetime')
        if dt:
            dates_found.append(str(dt))
            
    is_stale = False
    stale_date = ""
    stale_years_diff = 0
    current_year = datetime.now().year

    if not dates_found:
        # Fallback to copyright years or last-modified
        full_text = soup.get_text(separator=' ', strip=True)
        years = [int(y) for y in re.findall(r'\b(19\d{2}|20\d{2})\b', full_text)]
        last_mod = headers_dict.get('Last-Modified')
        if last_mod:
            try:
                lm_year = datetime.strptime(last_mod, "%a, %d %b %Y %H:%M:%S %Z").year
                years.append(lm_year)
            except:
                pass
        
        if years:
            max_year = max(years)
            if max_year <= current_year:
                if (current_year - max_year) > 3:
                    is_stale = True
                    stale_date = str(max_year)
                    stale_years_diff = current_year - max_year
        
        findings.append({
            "id": "FRESH-001",
            "skill_source": "freshness-corroboration",
            "category": "discoverability",
            "title": "No explicit date metadata found",
            "severity": "high" if not is_stale else "medium", # Escalate if total absence of dates and not caught by stale
            "confidence": confidence,
            "evidence": spa_note + "No <time> tags or JSON-LD date properties were found.",
            "suggested_action": {
                "summary": "Add publication and modification dates",
                "detail": "Use standard schema.org datePublished/dateModified and HTML5 <time> elements.",
                "priority": "high",
                "effort": "low"
            }
        })
    else:
        for d in dates_found:
            try:
                clean_d = d.strip().replace('Z', '+00:00')
                date_obj = datetime.fromisoformat(clean_d)
                now = datetime.now(timezone.utc) if date_obj.tzinfo else datetime.now()
                diff_years = (now - date_obj).days / 365.25
                if diff_years > 1:
                    is_stale = True
                    stale_date = d
                    stale_years_diff = diff_years
                    break
            except Exception:
                m = re.search(r'(\d{4})-(\d{2})-(\d{2})', str(d))
                if m:
                    try:
                        date_obj = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)))
                        diff_years = (datetime.now() - date_obj).days / 365.25
                        if diff_years > 1:
                            is_stale = True
                            stale_date = d
                            stale_years_diff = diff_years
                            break
                    except Exception:
                        pass
                
    if is_stale:
        severity = "critical" if stale_years_diff > 10 else "high"
        findings.append({
            "id": "FRESH-002",
            "skill_source": "freshness-corroboration",
            "category": "discoverability",
            "title": f"Content appears highly stale (>{int(stale_years_diff)} years old)",
            "severity": severity,
            "confidence": confidence,
            "evidence": spa_note + f"Found date '{stale_date}' which is significantly outdated.",
            "suggested_action": {
                "summary": "Update content and refresh dates",
                "detail": "AI systems prefer fresh content. Review and update the page.",
                "priority": severity,
                "effort": "medium"
            }
        })

    # 3. Copyright year outdated
    full_text_for_copyright = soup.get_text(separator=' ', strip=True)
    # Try range first
    copyright_match = re.search(r'(?:Copyright|©)\s*(\d{4})\s*[-–—]\s*(\d{4})', full_text_for_copyright, re.IGNORECASE)
    year = None
    if copyright_match:
        year = int(copyright_match.group(2))
    else:
        copyright_match = re.search(r'(?:Copyright|©).*?([12][0-9]{3})', full_text_for_copyright, re.IGNORECASE)
        if copyright_match:
            year = int(copyright_match.group(1))

    if year and year < current_year:
        diff = current_year - year
        if diff >= 2: # Only flag if >= 2 years old
            severity = "critical" if diff > 10 else "high" if diff > 5 else "medium"
            findings.append({
                "id": "FRESH-003",
                "skill_source": "freshness-corroboration",
                "category": "discoverability",
                "title": "Outdated copyright year",
                "severity": severity,
                "confidence": confidence,
                "evidence": spa_note + f"Found copyright year {year}, but current year is {current_year}.",
                "suggested_action": {
                    "summary": "Update copyright year",
                    "detail": "A stale copyright year is a strong negative freshness signal to automated systems.",
                    "priority": severity,
                    "effort": "low"
                }
            })

    # 4. Inconsistent facts (Title vs H1)
    title = soup.title.get_text(strip=True) if soup.title else ""
    h1 = soup.find('h1')
    h1_text = h1.get_text(strip=True) if h1 else ""
    
    if title and h1_text:
        h1_words_list = re.findall(r'\w+', h1_text.lower())
        if len(h1_words_list) > 5: # Only flag if H1 is substantial, skip short slogans
            title_words = set(re.findall(r'\w+', title.lower().replace('.com', '').replace('.org', '').replace('.net', '').replace('.edu', '')))
            h1_words = set(h1_words_list)
            
            stop_words = {'the', 'a', 'an', 'and', 'or', 'of', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'is', 'home', 'page', 'official', 'site', 'welcome', 'inc', 'llc', 'corporation', 'company', 'brand'}
            
            title_meaningful = title_words - stop_words
            h1_meaningful = h1_words - stop_words
            
            if title_meaningful and h1_meaningful and len(title_meaningful.intersection(h1_meaningful)) == 0:
                findings.append({
                    "id": "FRESH-004",
                    "skill_source": "freshness-corroboration",
                    "category": "discoverability",
                    "title": "Stylistically Divergent H1 and Title",
                    "severity": "low",
                    "confidence": "low",
                    "evidence": spa_note + f"Title ('{title}') and H1 ('{h1_text}') have zero overlap in words. This is often an intentional styling choice, but extreme divergence can dilute entity signals.",
                    "suggested_action": {
                        "summary": "Ensure Title and H1 are topically aligned",
                        "detail": "While it is normal for SEO titles to differ from marketing H1 taglines, ensure they still target the same core semantic topic.",
                        "priority": "low",
                        "effort": "low"
                    }
                })
            
    # 5. Corroboration (Outbound links)
    if not spa_detected:
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
                "severity": "low", # Downgraded severity for commercial sites
                "confidence": confidence,
                "evidence": spa_note + "Found 0 external outbound links.",
                "suggested_action": {
                    "summary": "Add citations or links to trusted sources",
                    "detail": "Linking to authoritative external sources helps ground the entity in the wider knowledge graph.",
                    "priority": "low",
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
        
        content_type = resp.headers.get('content-type', '').lower()
        if 'text/html' not in content_type and 'text/plain' not in content_type:
            print(json.dumps({"error": "Target URL is not an HTML page (e.g. JSON API or binary file). Audit not applicable."}))
            return
            
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
        
        all_findings.extend(check_freshness(url, html, resp.headers))
        
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
