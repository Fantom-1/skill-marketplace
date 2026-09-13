import sys
import os

from bot_detection import is_blocked_response
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5'
}


def check_extraction(url, html):
    findings = []
    soup = BeautifulSoup(html, 'html.parser')
    
    # 1. Semantic Tagging
    article = soup.find('article')
    main = soup.find('main')
    
    if not article and not main:
        findings.append({
            "id": "EXTRACT-001",
            "skill_source": "content-extraction-audit",
            "category": "engagement",
            "title": "Missing Semantic Content Tags",
            "severity": "medium",
            "confidence": "high",
            "evidence": "Neither <article> nor <main> tags were found in the HTML.",
            "suggested_action": {
                "summary": "Wrap core content in <main> or <article>",
                "detail": "LLM scrapers rely on semantic tags to strip out navigational boilerplate and footers. Add these to improve content parsing accuracy.",
                "priority": "medium",
                "effort": "low"
            }
        })
        
    # 2. Interstitial / Cookie Wall Detection
    interstitials = soup.find_all('div', attrs={'id': lambda val: val and any(x in val.lower() for x in ['cookie', 'modal', 'popup', 'overlay', 'consent'])})
    if interstitials:
        findings.append({
            "id": "EXTRACT-002",
            "skill_source": "content-extraction-audit",
            "category": "engagement",
            "title": "Potential Interstitial / Overlay Detected",
            "severity": "low",
            "confidence": "medium",
            "evidence": "Found <div> elements with IDs indicating cookie banners or overlays.",
            "suggested_action": {
                "summary": "Ensure overlays don't block headless crawlers",
                "detail": "If a cookie wall requires interaction to view the page text, AI bots may fail to extract the content.",
                "priority": "low",
                "effort": "medium"
            }
        })
        
    return findings

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL provided"}))
        return
        
    url = sys.argv[1]
    
    try:
        resp = requests.get(url, headers=HEADERS, timeout=10, verify=False)
        
        content_type = resp.headers.get('content-type', '').lower()
        if 'text/html' not in content_type and 'text/plain' not in content_type:
            print(json.dumps({"error": "Target URL is not an HTML page (e.g. JSON API or binary file). Audit not applicable."}))
            return
            
        if is_blocked_response(resp):
            print(json.dumps({"findings": []}))
            return
            
        findings = check_extraction(url, resp.text)
        print(json.dumps({"findings": findings}, indent=2))
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        print(json.dumps({"findings": []}))

if __name__ == "__main__":
    main()
