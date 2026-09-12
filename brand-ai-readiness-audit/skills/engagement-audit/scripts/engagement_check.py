import sys
import json
import re
import requests
from bs4 import BeautifulSoup

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

def check_engagement(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Navigation
    navs = soup.find_all('nav')
    if not navs:
        findings.append({
            "id": "ENGAGE-001",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Missing semantic <nav> element",
            "severity": "high",
            "evidence": "Did not find any <nav> HTML elements on the page.",
            "suggested_action": {
                "summary": "Use semantic HTML5 <nav> tags",
                "detail": "Wrap your main navigation menus in <nav> tags to provide clear structure for both users (screen readers) and bots.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    # 2. Viewport (Mobile)
    viewport = soup.find('meta', attrs={'name': re.compile(r'^viewport$', re.I)})
    if not viewport:
        findings.append({
            "id": "ENGAGE-002",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Missing mobile viewport meta tag",
            "severity": "high",
            "evidence": "No <meta name=\"viewport\"> tag found.",
            "suggested_action": {
                "summary": "Add viewport meta tag for responsive design",
                "detail": "Add <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    # 3. Heading Hierarchy
    h1s = soup.find_all('h1')
    if not h1s:
        findings.append({
            "id": "ENGAGE-003",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Missing H1 tag",
            "severity": "medium",
            "evidence": "No <h1> tag was found on the page.",
            "suggested_action": {
                "summary": "Add a single, clear H1 tag",
                "detail": "Ensure the page has one main heading that describes the content.",
                "priority": "medium",
                "effort": "low"
            }
        })
    elif len(h1s) > 1:
        findings.append({
            "id": "ENGAGE-004",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Multiple H1 tags",
            "severity": "low",
            "evidence": f"Found {len(h1s)} <h1> tags.",
            "suggested_action": {
                "summary": "Use only one H1 tag per page",
                "detail": "For best structural clarity, restrict H1 to the page's primary title and use H2/H3 for subsections.",
                "priority": "low",
                "effort": "low"
            }
        })
        
    # 4. Thin content
    soup_copy = BeautifulSoup(html, 'html.parser')
    for script in soup_copy(["script", "style", "noscript", "svg"]):
        script.extract()
    text = soup_copy.get_text(separator=' ')
    words = text.split()
    if len(words) < 100:
        findings.append({
            "id": "ENGAGE-005",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Thin content",
            "severity": "medium",
            "evidence": f"Page contains only ~{len(words)} visible words.",
            "suggested_action": {
                "summary": "Increase content depth",
                "detail": "Pages with very little content often fail to satisfy user intent and cause high bounce rates.",
                "priority": "medium",
                "effort": "medium"
            }
        })
        
    # 5. Clear CTAs
    links_and_buttons = soup.find_all(['a', 'button'])
    cta_words = ['buy', 'purchase', 'subscribe', 'contact', 'sign up', 'register', 'get started', 'book', 'shop', 'learn more', 'apply', 'donate', 'join', 'explore']
    has_cta = False
    
    for el in links_and_buttons:
        el_text = el.get_text().strip().lower()
        if any(w in el_text for w in cta_words):
            has_cta = True
            break
            
    if not has_cta:
        findings.append({
            "id": "ENGAGE-006",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "No obvious Call to Action (CTA)",
            "severity": "medium",
            "evidence": "Did not detect standard CTA verbs (buy, sign up, contact, etc.) in buttons or links.",
            "suggested_action": {
                "summary": "Add clear CTAs",
                "detail": "Guide visitors to the next step to improve engagement and retention.",
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
        all_findings.extend(check_engagement(url, html))
    except Exception as e:
        all_findings.append({
            "id": "ENGAGE-ERR",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Failed to fetch page for engagement audit",
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

