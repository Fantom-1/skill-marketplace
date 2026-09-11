import sys
import json
import requests
import re
from bs4 import BeautifulSoup

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
    viewport = soup.find('meta', attrs={'name': 'viewport'})
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
    # Remove script and style tags to count visible words
    for script in soup(["script", "style", "noscript"]):
        script.extract()
    text = soup.get_text(separator=' ')
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
    cta_words = ['buy', 'purchase', 'subscribe', 'contact', 'sign up', 'register', 'get started', 'book', 'shop', 'learn more']
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
        headers = {'User-Agent': 'Mozilla/5.0'}
        resp = requests.get(url, headers=headers, timeout=15)
        html = resp.text
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
