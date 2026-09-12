import sys
import json
import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}

CTA_KEYWORDS = {
    'buy', 'purchase', 'subscribe', 'contact', 'sign up', 'signup', 'register',
    'get started', 'book', 'shop', 'learn more', 'learn', 'apply', 'donate',
    'join', 'explore', 'login', 'log in', 'sign in', 'connect', 'download',
    'start', 'try', 'open', 'view', 'see', 'find', 'go', 'search', 'send',
    'submit', 'claim', 'swap', 'trade', 'mint', 'stake', 'access', 'check',
    'request', 'demo', 'play', 'listen', 'watch', 'install', 'launch',
    'enter', 'discover', 'get in touch'
}

FRAMEWORK_MARKERS = [
    'id="root"', 'id="app"', 'id="mount"', 'id="__next"', '__next_data__',
    'window.__initial_state__', 'react', 'vue', 'angular', 'svelte', 'gatsby'
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

def check_engagement(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    parsed_url = urlparse(url)
    domain_lower = parsed_url.netloc.lower()
    path_lower = parsed_url.path.lower()
    
    is_web_app_or_login = (
        domain_lower.startswith('app.') or
        domain_lower.startswith('web.') or
        domain_lower.startswith('messages.') or
        '/login' in path_lower or
        '/flow/login' in path_lower or
        '/trade/' in path_lower
    )

    # 1. Navigation
    has_nav = False
    if soup.find('nav'):
        has_nav = True
    elif soup.find(attrs={'role': 'navigation'}):
        has_nav = True
    else:
        # Check header or container elements with nav/menu classes/ids
        nav_containers = soup.find_all(['header', 'div', 'aside', 'ul'], attrs={
            'id': re.compile(r'nav|navbar|navigation|menu', re.I)
        })
        if not nav_containers:
            nav_containers = soup.find_all(['header', 'div', 'aside', 'ul'], attrs={
                'class': re.compile(r'nav|navbar|navigation|menu', re.I)
            })
        for container in nav_containers:
            if len(container.find_all('a')) >= 2:
                has_nav = True
                break

    if not has_nav:
        findings.append({
            "id": "ENGAGE-001",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Missing semantic navigation structure",
            "severity": "medium",
            "evidence": "Did not find <nav> elements, role='navigation', or header menu containers with links.",
            "suggested_action": {
                "summary": "Use semantic HTML5 <nav> or ARIA navigation roles",
                "detail": "Wrap main navigation menus in <nav> tags or role='navigation' to provide clear structure for AI crawlers.",
                "priority": "medium",
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
            "severity": "low",
            "evidence": "No <meta name=\"viewport\"> tag found.",
            "suggested_action": {
                "summary": "Add viewport meta tag for responsive design",
                "detail": "Add <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">.",
                "priority": "low",
                "effort": "low"
            }
        })
        
    # 3. Heading Hierarchy
    h1s = soup.find_all('h1')
    aria_h1s = soup.find_all(attrs={'role': 'heading', 'aria-level': '1'})
    all_main_headings = h1s + aria_h1s

    if not all_main_headings:
        findings.append({
            "id": "ENGAGE-003",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "Missing H1 heading",
            "severity": "medium",
            "evidence": "No <h1> tag or role='heading' (aria-level=1) was found on the page.",
            "suggested_action": {
                "summary": "Add a single, clear H1 heading",
                "detail": "Ensure the page has one main H1 heading that describes the primary content for AI summarization.",
                "priority": "medium",
                "effort": "low"
            }
        })
    elif len(all_main_headings) > 1:
        # Check if H1s are sectioned (inside distinct <section>, <article>, <aside>, <nav>, <header>)
        unsectioned_h1s = []
        section_parents = set()
        has_duplicate_in_same_section = False

        for h in all_main_headings:
            parent_section = h.find_parent(['section', 'article', 'aside', 'nav', 'header'])
            if parent_section:
                if parent_section in section_parents:
                    has_duplicate_in_same_section = True
                section_parents.add(parent_section)
            else:
                unsectioned_h1s.append(h)

        if has_duplicate_in_same_section or len(unsectioned_h1s) > 1:
            findings.append({
                "id": "ENGAGE-004",
                "skill_source": "engagement-audit",
                "category": "engagement",
                "title": "Multiple unsectioned H1 tags",
                "severity": "low",
                "evidence": f"Found {len(all_main_headings)} main headings without separate HTML5 sectioning elements.",
                "suggested_action": {
                    "summary": "Scope H1 tags within sectioning elements or restrict to single top-level H1",
                    "detail": "Encapsulate secondary H1 tags inside <section> or <article> elements, or use H2/H3 for subsections.",
                    "priority": "low",
                    "effort": "low"
                }
            })
        
    # 4. Thin Content & Single Page Application (SPA) diagnosis
    soup_copy = BeautifulSoup(html, 'html.parser')
    for tag in soup_copy(["script", "style", "noscript", "svg"]):
        tag.extract()
    text = soup_copy.get_text(separator=' ')
    words = text.split()
    
    html_lower = html.lower()
    is_spa = any(marker in html_lower for marker in FRAMEWORK_MARKERS) or (len(soup.find_all('script')) > 3 and len(words) < 150)
    
    if len(words) < 100:
        if is_spa and not is_web_app_or_login:
            findings.append({
                "id": "ENGAGE-005",
                "skill_source": "engagement-audit",
                "category": "engagement",
                "title": "Client-Side Rendered (CSR) SPA content hidden from basic AI crawlers",
                "severity": "high",
                "evidence": f"Raw HTML contains only ~{len(words)} visible words because content relies on client-side JavaScript rendering.",
                "suggested_action": {
                    "summary": "Implement Server-Side Rendering (SSR) or Prerendering",
                    "detail": "Use SSR (e.g. Next.js, Nuxt) or prerendering services so non-JS AI crawlers can read full page content.",
                    "priority": "high",
                    "effort": "high"
                }
            })
        elif not is_web_app_or_login:
            findings.append({
                "id": "ENGAGE-005",
                "skill_source": "engagement-audit",
                "category": "engagement",
                "title": "Thin content",
                "severity": "medium",
                "evidence": f"Page contains only ~{len(words)} visible words.",
                "suggested_action": {
                    "summary": "Increase content depth",
                    "detail": "Pages with very little content fail to provide adequate context for AI indexing and recommendation.",
                    "priority": "medium",
                    "effort": "medium"
                }
            })
        
    # 5. Clear CTAs
    actionable_elements = soup.find_all(['a', 'button', 'input'])
    actionable_elements.extend(soup.find_all(attrs={'role': 'button'}))
    
    has_cta = False
    for el in actionable_elements:
        el_text = el.get_text(strip=True).lower()
        val_attr = (el.get('value') or '').strip().lower()
        aria_attr = (el.get('aria-label') or '').strip().lower()
        title_attr = (el.get('title') or '').strip().lower()
        
        combined_cta_text = f"{el_text} {val_attr} {aria_attr} {title_attr}"
        if any(w in combined_cta_text for w in CTA_KEYWORDS):
            has_cta = True
            break
            
    if not has_cta:
        findings.append({
            "id": "ENGAGE-006",
            "skill_source": "engagement-audit",
            "category": "engagement",
            "title": "No obvious Call to Action (CTA)",
            "severity": "medium",
            "evidence": "Did not detect standard CTA actions (buy, sign up, contact, learn, try, search, connect) in interactive elements.",
            "suggested_action": {
                "summary": "Add clear CTAs",
                "detail": "Guide visitors and AI agents to primary conversion or engagement actions.",
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


