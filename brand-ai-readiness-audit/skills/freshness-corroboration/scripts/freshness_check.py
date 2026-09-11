import sys
import json
import re
import requests
from bs4 import BeautifulSoup
import extruct
from w3lib.html import get_base_url
from datetime import datetime
from urllib.parse import urlparse

def check_freshness(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    base_url = get_base_url(html, url)
    
    # 1. & 2. Date signals
    try:
        data = extruct.extract(html, base_url=base_url, syntaxes=['json-ld'])
        json_ld = data.get('json-ld', [])
    except:
        json_ld = []

    dates_found = []
    
    # Search JSON-LD
    for item in json_ld:
        if isinstance(item, dict):
            if 'datePublished' in item: dates_found.append(item['datePublished'])
            if 'dateModified' in item: dates_found.append(item['dateModified'])

    # Search HTML <time> tags
    for time_tag in soup.find_all('time'):
        if time_tag.get('datetime'):
            dates_found.append(time_tag.get('datetime'))
            
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
        current_year = datetime.now().year
        for d in dates_found:
            try:
                date_obj = datetime.fromisoformat(d.replace('Z', '+00:00'))
                if (datetime.now().astimezone() - date_obj).days > 365:
                    is_stale = True
                    stale_date = d
                    break
            except:
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
    footer_text = ""
    footer = soup.find('footer')
    if footer:
        footer_text = footer.get_text()
    else:
        # Fallback to body text
        footer_text = soup.body.get_text()[-1000:] if soup.body else ""
        
    copyright_match = re.search(r'(?:Copyright|©).*?([12][0-9]{3})', footer_text, re.IGNORECASE)
    if copyright_match:
        year = int(copyright_match.group(1))
        if year < datetime.now().year:
            findings.append({
                "id": "FRESH-003",
                "skill_source": "freshness-corroboration",
                "category": "discoverability",
                "title": "Outdated copyright year",
                "severity": "medium",
                "evidence": f"Found copyright year {year}, but current year is {datetime.now().year}.",
                "suggested_action": {
                    "summary": "Update copyright year",
                    "detail": "A stale copyright year is a strong negative freshness signal to automated systems.",
                    "priority": "medium",
                    "effort": "low"
                }
            })

    # 4. Inconsistent facts (Title vs H1)
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    h1 = soup.find('h1')
    h1_text = h1.get_text(strip=True) if h1 else ""
    
    if title and h1_text:
        # Just a very basic heuristic: if they share no words
        title_words = set(title.lower().split())
        h1_words = set(h1_text.lower().split())
        if len(title_words.intersection(h1_words)) == 0:
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
    external_links = [l['href'] for l in links if l['href'].startswith('http') and urlparse(l['href']).netloc != urlparse(url).netloc]
    
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
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=15)
        html = resp.text
        
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
