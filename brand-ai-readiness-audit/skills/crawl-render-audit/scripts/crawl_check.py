import sys
import os

# Add shared directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from shared.bot_detection import is_blocked_response
import json
import re
import requests
import urllib.robotparser
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.9',
}


def check_robots_txt(url):
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = f"{base_url}/robots.txt"
    
    findings = []
    rp = urllib.robotparser.RobotFileParser()
    
    try:
        resp = requests.get(robots_url, headers=HEADERS, timeout=10, verify=False)
        if resp.status_code == 200:
            rp.parse(resp.text.splitlines())
        elif resp.status_code in (401, 403):
            findings.append({
                "id": "CRAWL-WAF",
                "skill_source": "crawl-render-audit",
                "category": "discoverability",
                "title": "WAF blocks robots.txt access",
                "severity": "critical",
                "evidence": f"robots.txt is protected or inaccessible due to WAF/security firewall (status {resp.status_code}).",
                "suggested_action": {
                    "summary": "Whitelist crawler IP in WAF",
                    "detail": "Configure WAF/security settings to whitelist crawler IP and allow access to robots.txt.",
                    "priority": "critical",
                    "effort": "low"
                }
            })
            return findings
        else:
            return findings
    except Exception:
        return findings

    bots_to_check = ['GPTBot', 'Google-Extended', 'CCBot', 'anthropic-ai', 'ChatGPT-User']
    blocked_bots = []
    
    for bot in bots_to_check:
        try:
            if not rp.can_fetch(bot, url):
                blocked_bots.append(bot)
        except Exception:
            pass
            
    if blocked_bots:
        findings.append({
            "id": "CRAWL-001",
            "skill_source": "crawl-render-audit",
            "category": "discoverability",
            "title": "robots.txt blocks AI crawlers",
            "severity": "critical",
            "evidence": f"The following AI bots are disallowed in robots.txt: {', '.join(blocked_bots)}",
            "suggested_action": {
                "summary": "Remove AI crawler blocks from robots.txt",
                "detail": "Allow AI bots to crawl the site to ensure inclusion in AI overviews and answers. Remove 'Disallow: /' for these User-agents.",
                "priority": "critical",
                "effort": "low"
            }
        })
        
    return findings

def check_html_signals(url, html, response_size):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    
    # 2. noindex
    robots_meta = soup.find('meta', attrs={'name': re.compile(r'^robots$', re.I)})
    if robots_meta and 'noindex' in (robots_meta.get('content') or '').lower():
        findings.append({
            "id": "CRAWL-002",
            "skill_source": "crawl-render-audit",
            "category": "discoverability",
            "title": "Page contains noindex meta tag",
            "severity": "critical",
            "evidence": f"Found: <meta name=\"robots\" content=\"{robots_meta.get('content')}\">",
            "suggested_action": {
                "summary": "Remove noindex tag",
                "detail": "If this page should be discoverable, remove the 'noindex' directive from the meta robots tag.",
                "priority": "critical",
                "effort": "low"
            }
        })
        
    # 5. Canonical URL issues
    canonical = soup.find('link', rel=lambda val: val and 'canonical' in val)
    if not canonical or not canonical.get('href'):
        findings.append({
            "id": "CRAWL-005",
            "skill_source": "crawl-render-audit",
            "category": "discoverability",
            "title": "Missing canonical URL",
            "severity": "high",
            "evidence": "No <link rel=\"canonical\"> tag found in the HTML <head>.",
            "suggested_action": {
                "summary": "Add a canonical URL tag",
                "detail": "Add a <link rel=\"canonical\" href=\"...\"> tag to prevent duplicate content issues.",
                "priority": "high",
                "effort": "low"
            }
        })
        
    # 6. JS-rendering dependency
    js_markers = [
        soup.find(id='root'), soup.find(id='app'), soup.find(id='__next'),
        soup.find('script', id='__NEXT_DATA__'), soup.find('noscript')
    ]
    body = soup.body
    if body:
        body_words = len(body.get_text(strip=True).split())
        if body_words < 100 and any(js_markers):
            findings.append({
                "id": "CRAWL-006",
                "skill_source": "crawl-render-audit",
                "category": "discoverability",
                "title": "Heavy JS-rendering dependency detected",
                "severity": "high",
                "evidence": f"Raw HTML contains very little text ({body_words} words) and contains SPA markers (e.g. empty #root or #app divs, __NEXT_DATA__).",
                "suggested_action": {
                    "summary": "Implement server-side rendering (SSR) or pre-rendering",
                    "detail": "Ensure that the core content is present in the raw HTML payload sent to crawlers. Use SSR, SSG, or dynamic rendering.",
                    "priority": "high",
                    "effort": "high"
                }
            })
        
    # 7. Iframes
    iframes = soup.find_all('iframe')
    content_iframes = []
    for iframe in iframes:
        src = (iframe.get('src') or '').lower()
        width = iframe.get('width', '')
        height = iframe.get('height', '')
        style = (iframe.get('style') or '').lower()
        if 'googletagmanager' in src or width in ('0', '1') or height in ('0', '1') or 'display:none' in style or 'visibility:hidden' in style:
            continue
        content_iframes.append(iframe)

    if len(content_iframes) > 2:
        findings.append({
            "id": "CRAWL-007",
            "skill_source": "crawl-render-audit",
            "category": "engagement",
            "title": "Content potentially locked in iframes",
            "severity": "medium",
            "evidence": f"Found {len(content_iframes)} <iframe> tags. Search engines and AI often do not index iframe content well.",
            "suggested_action": {
                "summary": "Avoid using iframes for core content",
                "detail": "Embed core content directly into the DOM instead of relying on iframes.",
                "priority": "medium",
                "effort": "medium"
            }
        })
        
    # 8. Payload size
    if response_size > 5 * 1024 * 1024:
        findings.append({
            "id": "CRAWL-008",
            "skill_source": "crawl-render-audit",
            "category": "engagement",
            "title": "Very large HTML payload",
            "severity": "medium",
            "evidence": f"Raw HTML payload is {response_size / (1024*1024):.2f} MB, which exceeds 5MB.",
            "suggested_action": {
                "summary": "Reduce HTML document size",
                "detail": "Remove inline base64 images, excessive inline CSS/JS, or bloated DOM structures.",
                "priority": "medium",
                "effort": "medium"
            }
        })

    return findings

def check_sitemap(url):
    findings = []
    parsed = urlparse(url)
    sitemap_url = f"{parsed.scheme}://{parsed.netloc}/sitemap.xml"
    
    try:
        resp = requests.get(sitemap_url, headers=HEADERS, timeout=10, verify=False)
        if resp.status_code != 200:
            findings.append({
                "id": "CRAWL-003",
                "skill_source": "crawl-render-audit",
                "category": "discoverability",
                "title": "Missing or broken XML sitemap",
                "severity": "high",
                "evidence": f"Attempted to fetch {sitemap_url} but got status {resp.status_code}.",
                "suggested_action": {
                    "summary": "Publish a valid XML sitemap",
                    "detail": "Create a sitemap.xml at the domain root and list it in robots.txt.",
                    "priority": "high",
                    "effort": "low"
                }
            })
            return findings
            
        try:
            root = ET.fromstring(resp.content)
            stale = False
            for elem in root.iter():
                if elem.tag.endswith('lastmod') and elem.text:
                    try:
                        date_str = elem.text.strip()[:10]
                        mod_date = datetime.strptime(date_str, "%Y-%m-%d")
                        delta = datetime.now() - mod_date
                        if delta.days > 180:
                            stale = True
                            break
                    except Exception:
                        pass
            
            if stale:
                findings.append({
                    "id": "CRAWL-004",
                    "skill_source": "crawl-render-audit",
                    "category": "discoverability",
                    "title": "Stale sitemap lastmod dates",
                    "severity": "medium",
                    "evidence": "Found <lastmod> dates in sitemap.xml that are older than 6 months.",
                    "suggested_action": {
                        "summary": "Update sitemap lastmod dates",
                        "detail": "Ensure your CMS automatically updates <lastmod> when content changes.",
                        "priority": "medium",
                        "effort": "low"
                    }
                })
        except Exception:
            findings.append({
                "id": "CRAWL-003",
                "skill_source": "crawl-render-audit",
                "category": "discoverability",
                "title": "Invalid XML sitemap",
                "severity": "high",
                "evidence": f"Sitemap at {sitemap_url} could not be parsed as valid XML.",
                "suggested_action": {
                    "summary": "Fix sitemap XML syntax",
                    "detail": "Validate your sitemap against the standard XML schema.",
                    "priority": "high",
                    "effort": "low"
                }
            })
            
    except Exception:
        pass
        
    return findings

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL provided"}))
        sys.exit(1)
        
    url = sys.argv[1]
    if not url.startswith('http'):
        url = 'https://' + url
        
    all_findings = []
    
    # 1. Robots.txt
    all_findings.extend(check_robots_txt(url))
    
    # Fetch page
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
            
        size = len(resp.content)
        all_findings.extend(check_html_signals(url, html, size))
        
    except Exception as e:
        all_findings.append({
            "id": "CRAWL-ERR",
            "skill_source": "crawl-render-audit",
            "category": "discoverability",
            "title": "Failed to fetch homepage",
            "severity": "critical",
            "evidence": str(e),
            "suggested_action": {
                "summary": "Ensure server is reachable",
                "detail": "The audit could not reach the server. Check DNS and server status.",
                "priority": "critical",
                "effort": "medium"
            }
        })
        
    # Sitemap
    all_findings.extend(check_sitemap(url))
    
    # Output Sub-report
    print(json.dumps({"findings": all_findings}, indent=2))

if __name__ == "__main__":
    main()

