import sys
import os
import json
import subprocess
import time
from urllib.parse import urlparse

def slugify(url):
    return urlparse(url).netloc.replace("www.", "").replace(".", "_")

def run_pipeline(agent_name):
    # Load corpus
    with open("data/test_corpus.json", "r", encoding="utf-8") as f:
        corpus = json.load(f)
        
    if agent_name not in corpus:
        print(f"Error: Agent {agent_name} not found in test_corpus.json")
        sys.exit(1)
        
    sites = corpus[agent_name]
    log_dir = os.path.join("logs", agent_name)
    os.makedirs(log_dir, exist_ok=True)
    
    print(f"[{agent_name}] Starting automated run pipeline on {len(sites)} sites...")
    
    summary = {
        "agent": agent_name,
        "total_time": 0,
        "sites": [],
        "crashes": 0,
        "anomalies_detected": []
    }
    
    orchestrator = "brand-ai-readiness-audit/skills/audit-orchestrator/scripts/merge_report.py"
    
    for site in sites:
        print(f"  Auditing {site}...")
        start_time = time.time()
        
        slug = slugify(site)
        output_file = os.path.join(log_dir, f"{slug}.json")
        
        try:
            result = subprocess.run(
                [sys.executable, orchestrator, site],
                capture_output=True,
                text=True,
                timeout=300
            )
            
            duration = time.time() - start_time
            summary["total_time"] += duration
            
            if result.returncode != 0:
                print(f"    [CRASH] {site} stderr: {result.stderr.strip()[:100]}...")
                summary["crashes"] += 1
                continue
                
            try:
                report = json.loads(result.stdout)
                
                # Save JSON
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(report, f, indent=2)
                    
                finding_summary = report.get("summary", {})
                
                # Auto-Diagnostics (Heuristics)
                # If a site is highly optimized (Apple/Microsoft) but gets > 5 critical/high, flag it as a potential False Positive.
                if "apple" in site or "microsoft" in site or "github" in site:
                    if finding_summary.get("high", 0) + finding_summary.get("critical", 0) > 3:
                        summary["anomalies_detected"].append(f"Potential False Positives on {site}: Found {finding_summary.get('high')} High findings on an optimized site.")
                
                # If blocked, ensure it fired the -BLOCKED flag
                is_blocked = any("BLOCKED" in f.get("id", "") for f in report.get("findings", []))
                if is_blocked:
                    print(f"    [BLOCKED] Detected bot mitigation for {site}")
                
                summary["sites"].append({
                    "url": site,
                    "time": duration,
                    "critical": finding_summary.get("critical", 0),
                    "high": finding_summary.get("high", 0),
                    "medium": finding_summary.get("medium", 0),
                    "blocked": is_blocked
                })
                print(f"    [OK] {duration:.2f}s | C:{finding_summary.get('critical',0)} H:{finding_summary.get('high',0)}")
                
            except json.JSONDecodeError:
                print("    [ERROR] JSON Decode failed. Raw Output:\n", result.stdout[:200])
                summary["crashes"] += 1
                
        except subprocess.TimeoutExpired:
            print(f"    [TIMEOUT] {site}")
            summary["crashes"] += 1
            
    # Write Analysis Report
    report_path = os.path.join(log_dir, "analysis_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"# Pipeline Run Analysis: {agent_name}\n\n")
        f.write(f"**Total Run Time:** {summary['total_time']:.2f}s\n")
        f.write(f"**Crashes / Timeouts:** {summary['crashes']}\n\n")
        
        f.write("## Site Breakdown\n")
        f.write("| Site | Time (s) | Critical | High | Medium | Bot Blocked? |\n")
        f.write("|---|---|---|---|---|---|\n")
        for s in summary["sites"]:
            f.write(f"| {s['url']} | {s['time']:.2f} | {s['critical']} | {s['high']} | {s['medium']} | {s['blocked']} |\n")
            
        f.write("\n## Automated Diagnostic Feedback\n")
        if summary["anomalies_detected"]:
            for a in summary["anomalies_detected"]:
                f.write(f"- ⚠️ **WARNING:** {a}\n")
            f.write("\n**Skill Improvement Suggestion:** The thresholds for these High/Critical findings may be too aggressive. Review the JSON logs for these sites and adjust the severity in `engagement_check.py` or `crawl_check.py`.\n")
        elif summary["crashes"] == 0:
            f.write("- ✅ **SUCCESS:** No crashes and no massive false-positive anomalies detected. The skills appear stable for this cohort.\n")
        else:
            f.write("- ⚠️ **WARNING:** Crashes detected. You must review stderr and add try/except blocks to the failing Python scripts.\n")

    print(f"[{agent_name}] Pipeline finished. Diagnostics written to {report_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_pipeline.py <agent_name>")
        sys.exit(1)
    run_pipeline(sys.argv[1])
