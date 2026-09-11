import sys
import os
import json
import requests
from bs4 import BeautifulSoup
import extruct
from urllib.parse import urlparse

# List of the 20 sites from our field research
SITES = [
    "https://www.nike.com",
    "https://www.allbirds.com",
    "https://www.buckmason.com",
    "https://vintageempire.shop",
    "https://www.notion.so",
    "https://www.asana.com",
    "https://linear.app",
    "https://www.figma.com",
    "https://www.viacarota.com",
    "https://www.bestlawyers.com",
    "https://www.acehotel.com",
    "https://www.servicemaster.com",
    "https://www.bbc.com",
    "https://www.lesswrong.com",
    "https://techcrunch.com",
    "https://www.apple.com",
    "https://www.zappos.com",
    "https://buffer.com",
    "https://www.spotify.com/se-en/"
]

def analyze_site(url):
    results = {}
    try:
        response = requests.get(url, timeout=10, headers={'User-Agent': 'Mozilla/5.0'})
        results['status'] = response.status_code
        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, 'lxml')
            
            # Check JSON-LD
            data = extruct.extract(html, syntaxes=['json-ld'])
            results['has_json_ld'] = bool(data.get('json-ld', []))
            
            # Check JS reliance (is content empty without JS?)
            visible_text = soup.get_text(strip=True)
            results['is_js_reliant'] = len(visible_text) < 1000
            
            # Check robots
            robots_url = f"{urlparse(url).scheme}://{urlparse(url).netloc}/robots.txt"
            rob_resp = requests.get(robots_url, timeout=5)
            results['has_robots'] = rob_resp.status_code == 200
            
    except Exception as e:
        results['error'] = str(e)
        
    return results

def main():
    print("Starting Verification and Analysis of target sites...")
    
    with open("Phase0_Verification_Analysis.md", "w", encoding='utf-8') as f:
        f.write("# Phase 0 Verification & Analysis\n\n")
        f.write("This document contains the raw technical verification of the sites analyzed in the AI field research. We run 'curl/fetch' equivalent scraping to verify *why* the AI failed.\n\n")
        f.write("| Site | Status | Has JSON-LD? | Heavily JS Reliant? | Has robots.txt? |\n")
        f.write("|---|---|---|---|---|\n")
        
        for site in SITES:
            print(f"Analyzing {site}...")
            res = analyze_site(site)
            status = res.get('status', res.get('error', 'N/A'))
            has_schema = res.get('has_json_ld', 'Error')
            js_reliant = res.get('is_js_reliant', 'Error')
            has_robots = res.get('has_robots', 'Error')
            
            f.write(f"| {site} | {status} | {has_schema} | {js_reliant} | {has_robots} |\n")
            
    print("Verification complete. Results written to Phase0_Verification_Analysis.md")

if __name__ == "__main__":
    main()
