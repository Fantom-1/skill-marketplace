import sys
import json
import requests
import urllib.robotparser
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
import time

def check_robots_txt(url):
    parsed = urlparse(url)
    base_url = f"{parsed.scheme}://{parsed.netloc}"
    robots_url = f"{base_url}/robots.txt"
    
    findings = []
    
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    
    try:
        rp.read()
    except Exception as e:
        return findings

    bots_to_check = ['GPTBot', 'Google-Extended', 'CCBot', 'anthropic-ai', 'ChatGPT-User']
    blocked_bots = []
    
    for bot in bots_to_check:
        if not rp.can_fetch(bot, url):
            blocked_bots.append(bot)
            
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
    robots_meta = soup.find('meta', attrs={'name': 'robots'})
    if robots_meta and 'noindex' in robots_meta.get('content', '').lower():
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
    canonical = soup.find('link', rel='canonical')
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
        soup.find(id='root'), soup.find(id='app'), 
        soup.find('script', id='__NEXT_DATA__'), soup.find('noscript')
    ]
    # Check if body is mostly empty (indicative of SPA)
    body = soup.body
    if body and len(body.get_text(strip=True)) < 100 and any(js_markers):
        findings.append({
            "id": "CRAWL-006",
            "skill_source": "crawl-render-audit",
            "category": "discoverability",
            "title": "Heavy JS-rendering dependency detected",
            "severity": "high",
            "evidence": "Raw HTML contains very little text (< 100 words) and contains SPA markers (e.g. empty #root or #app divs, __NEXT_DATA__).",
            "suggested_action": {
                "summary": "Implement server-side rendering (SSR) or pre-rendering",
                "detail": "Ensure that the core content is present in the raw HTML payload sent to crawlers. Use SSR, SSG, or dynamic rendering.",
                "priority": "high",
                "effort": "high"
            }
        })
        
    # 7. Iframes
    iframes = soup.find_all('iframe')
    if len(iframes) > 2:
        findings.append({
            "id": "CRAWL-007",
            "skill_source": "crawl-render-audit",
            "category": "engagement",
            "title": "Content potentially locked in iframes",
            "severity": "medium",
            "evidence": f"Found {len(iframes)} <iframe> tags. Search engines and AI often do not index iframe content well.",
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
        resp = requests.get(sitemap_url, timeout=10)
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
            # Check lastmod
            stale = False
            namespaces = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
            for url_elem in root.findall('sm:url', namespaces):
                lastmod = url_elem.find('sm:lastmod', namespaces)
                if lastmod is not None:
                    try:
                        date_str = lastmod.text[:10]
                        mod_date = datetime.strptime(date_str, "%Y-%m-%d")
                        delta = datetime.now() - mod_date
                        if delta.days > 180:
                            stale = True
                            break
                    except:
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
        except ET.ParseError:
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
            
    except Exception as e:
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
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    try:
        resp = requests.get(url, headers=headers, timeout=15)
        html = resp.text
        if resp.status_code != 200 or "<title>Just a moment...</title>" in html or "cloudflare" in html.lower() or "captcha" in html.lower():
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
            return all_findings
        size = len(resp.content)
        
        # HTML Signals
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
