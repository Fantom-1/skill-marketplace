import sys
import json
import subprocess
import os
import re
from datetime import datetime, timezone
from urllib.parse import urlparse

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def run_skill_script(script_path, url):
    try:
        result = subprocess.run(
            [sys.executable, script_path, url],
            capture_output=True,
            text=True,
            timeout=180
        )
        if result.returncode == 0:
            try:
                data = json.loads(result.stdout)
                return data.get("findings", [])
            except Exception as jde:
                print(f"JSON decode error running {script_path}: {jde}. Stdout: {result.stdout[:200]}", file=sys.stderr)
                return []
        else:
            print(f"Error running {script_path}: {result.stderr}", file=sys.stderr)
            return []
    except Exception as e:
        print(f"Exception running {script_path}: {e}", file=sys.stderr)
        return []

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL provided"}))
        sys.exit(1)
        
    url = sys.argv[1]
    if not url.startswith('http'):
        url = 'https://' + url
        
    domain = urlparse(url).netloc
    
    # Locate all scripts relative to orchestrator
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    scripts = [
        os.path.join(base_dir, "crawl-render-audit", "scripts", "crawl_check.py"),
        os.path.join(base_dir, "structured-data-audit", "scripts", "schema_check.py"),
        os.path.join(base_dir, "freshness-corroboration", "scripts", "freshness_check.py"),
        os.path.join(base_dir, "entity-identity-audit", "scripts", "identity_check.py"),
        os.path.join(base_dir, "engagement-audit", "scripts", "engagement_check.py")
    ]
    
    all_findings = []
    valid_scripts = [s for s in scripts if os.path.exists(s)]
    
    from concurrent.futures import ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=len(valid_scripts)) as executor:
        results = executor.map(lambda s: run_skill_script(s, url), valid_scripts)
        for findings in results:
            all_findings.extend(findings)
            
    # Deduplicate findings based on ID and Title
    unique_findings = []
    seen_ids = set()
    seen_titles = set()
    
    for f in all_findings:
        fid = f.get('id')
        title = f.get('title')
        if fid and fid in seen_ids:
            continue
        if title and title in seen_titles:
            continue
        if fid:
            seen_ids.add(fid)
        if title:
            seen_titles.add(title)
        unique_findings.append(f)
            
    # Sort by severity
    unique_findings.sort(key=lambda x: SEVERITY_ORDER.get(x.get('severity', 'low'), 99))
    
    # Calculate summary
    summary = {
        "total_findings": len(unique_findings),
        "critical": 0,
        "high": 0,
        "medium": 0,
        "low": 0
    }
    
    for f in unique_findings:
        sev = f.get('severity')
        if sev in summary:
            summary[sev] += 1
            
    # Add proactive recommendations dynamically based on findings
    proactive = []
    
    # Check if primary identity/schema is missing (R-001 only triggers on SCHEMA-001 or IDENT-001)
    has_identity_issue = any(f.get('id') in ("SCHEMA-001", "IDENT-001") for f in unique_findings)
    if has_identity_issue:
        proactive.append({
            "id": "R-001",
            "title": "Establish a consistent Knowledge Graph presence",
            "rationale": "Even if structured data is valid, explicitly linking to a maintained Wikipedia or Wikidata entity acts as an anchor for AI to ground facts about the brand.",
            "suggested_action": "Claim your Wikidata item, ensure Wikipedia is accurate, and link to them using JSON-LD sameAs."
        })
        
    # Check if explicit CRAWL-001 block exists (R-002 only triggers on explicit CRAWL-001 disallows)
    has_crawl_issue = any(f.get('id') == "CRAWL-001" for f in unique_findings)
    if has_crawl_issue:
        proactive.append({
            "id": "R-002",
            "title": "Publish an AI Policy / Terms of Service",
            "rationale": "If you block some AI bots in robots.txt to protect IP, explicitly state what is allowed in a `/ai-policy` page. This ensures bots that respect advanced directives handle your content correctly.",
            "suggested_action": "Add an AI Terms page and use <meta name=\"robots\" content=\"noai\"> if needed, rather than blanket disallows."
        })

    # Check for question/answer content lacking FAQPage schema (R-003)
    findings_text = " ".join(
        f"{f.get('title', '')} {f.get('evidence', '')} {json.dumps(f.get('suggested_action', {}))}"
        for f in unique_findings
    )
    has_question_content = bool(re.search(r'\b(how|what|why)\b', findings_text, re.IGNORECASE))
    has_faq_schema = "faq" in findings_text.lower() or "faqpage" in findings_text.lower()
    
    if has_question_content and not has_faq_schema:
        proactive.append({
            "id": "R-003",
            "title": "Implement FAQPage Structured Data",
            "rationale": "Content answering common user questions ('how', 'what', 'why') benefits from JSON-LD FAQPage schema to enable direct Q&A snippet extraction by AI engines.",
            "suggested_action": "Mark up key Q&A sections with FAQPage schema using Question and Answer elements."
        })

    # Check if FRESH-002 (Stale dates) is triggered (R-004)
    has_stale_dates = any(f.get('id') == "FRESH-002" for f in unique_findings)
    if has_stale_dates:
        proactive.append({
            "id": "R-004",
            "title": "Establish a Content Refresh Cadence",
            "rationale": "Outdated content dates signal low freshness to AI crawlers, reducing confidence in answers generated from your pages.",
            "suggested_action": "Establish a periodic content review process to refresh outdated facts and update dateModified metadata."
        })
    
    report = {
        "site": domain,
        "audited_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "summary": summary,
        "findings": unique_findings,
        "proactive_recommendations": proactive
    }
    
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()

