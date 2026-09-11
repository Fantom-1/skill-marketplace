import sys
import json
import subprocess
import os
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
            return json.loads(result.stdout).get("findings", [])
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
    
    for script in scripts:
        if os.path.exists(script):
            findings = run_skill_script(script, url)
            all_findings.extend(findings)
            
    # Deduplicate findings based on ID (though they should be unique) and Title
    unique_findings = []
    seen_titles = set()
    
    for f in all_findings:
        title = f.get('title')
        if title not in seen_titles:
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
    
    # Check if identity/schema was missing
    has_identity_issue = any("IDENT-" in f.get('id', '') or "SCHEMA-" in f.get('id', '') for f in unique_findings)
    if has_identity_issue:
        proactive.append({
            "id": "R-001",
            "title": "Establish a consistent Knowledge Graph presence",
            "rationale": "Even if structured data is valid, explicitly linking to a maintained Wikipedia or Wikidata entity acts as an anchor for AI to ground facts about the brand.",
            "suggested_action": "Claim your Wikidata item, ensure Wikipedia is accurate, and link to them using JSON-LD sameAs."
        })
        
    # Check if crawl issues exist
    has_crawl_issue = any("CRAWL-" in f.get('id', '') for f in unique_findings)
    if has_crawl_issue:
        proactive.append({
            "id": "R-002",
            "title": "Publish an AI Policy / Terms of Service",
            "rationale": "If you block some AI bots in robots.txt to protect IP, explicitly state what is allowed in a `/ai-policy` page. This ensures bots that respect advanced directives handle your content correctly.",
            "suggested_action": "Add an AI Terms page and use <meta name=\"robots\" content=\"noai\"> if needed, rather than blanket disallows."
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
