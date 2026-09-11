import subprocess
import sys
import json
import time

SITES_TO_TEST = [
    "https://www.apple.com",       # Well-optimized, massive brand
    "https://www.nike.com",        # E-commerce, heavily interactive
    "https://techcrunch.com",      # Media, content-heavy, high freshness
    "https://www.allbirds.com",    # D2C E-commerce
    "https://www.lesswrong.com"    # Community blog, mostly text
]

def run_test():
    print("Starting Batch Evaluation...\n" + "-"*50)
    
    total_time = 0
    results_summary = []
    
    for site in SITES_TO_TEST:
        print(f"Auditing: {site} ...")
        
        start_time = time.time()
        
        try:
            # Run the orchestrator
            result = subprocess.run(
                [sys.executable, "brand-ai-readiness-audit/skills/audit-orchestrator/scripts/merge_report.py", site],
                capture_output=True,
                text=True,
                timeout=300 # 5 minute timeout rule
            )
            
            end_time = time.time()
            duration = end_time - start_time
            total_time += duration
            
            if result.returncode != 0:
                print(f"  [ERROR] Script crashed! Stderr: {result.stderr.strip()}")
                continue
                
            try:
                report = json.loads(result.stdout)
                summary = report.get('summary', {})
                print(f"  [SUCCESS] Completed in {duration:.2f}s")
                print(f"  Findings -> Critical: {summary.get('critical', 0)} | High: {summary.get('high', 0)} | Medium: {summary.get('medium', 0)} | Low: {summary.get('low', 0)}")
                
                results_summary.append({
                    "site": site,
                    "duration": duration,
                    "findings": summary
                })
                
            except json.JSONDecodeError:
                print(f"  [ERROR] Failed to parse JSON output. Output was:\n{result.stdout[:200]}...")
                
        except subprocess.TimeoutExpired:
            print(f"  [TIMEOUT] Site {site} took longer than 5 minutes to audit!")
        except Exception as e:
            print(f"  [EXCEPTION] {e}")
            
        print("-" * 50)
        
    print("\n=== EVALUATION COMPLETE ===")
    print(f"Total time for {len(SITES_TO_TEST)} sites: {total_time:.2f}s")
    print("Average time per site: {:.2f}s".format(total_time / len(SITES_TO_TEST) if SITES_TO_TEST else 0))

if __name__ == "__main__":
    run_test()
