# Distributed Agent Pipeline - Execution Instructions

Welcome to the skill-marketplace testing framework. You have been assigned one of three branches (`agent1`, `agent2`, or `agent3`). Your goal is to run the automated pipeline, review the diagnostics, and improve the underlying codebase until false positives reach zero and crashes are eliminated.

## 1. Setup Your Environment
First, ensure you are on your designated branch and install the dependencies.
```bash
# Check out your branch (replace agent1 with your assigned name)
git checkout agent1

# Install requirements
pip install -r requirements.txt
```

## 2. Run the Evaluation Pipeline
You do **not** need to manually run the orchestrator on individual sites. A robust pipeline script has been created for you.

```bash
# Run the pipeline for your specific agent
python scripts/run_pipeline.py agent1
```

### What happens under the hood?
1. The script reads `test_corpus.json` from the root directory. This JSON file contains an array of exactly 70 highly diverse, *failure-prone* test sites assigned to you. These are deliberately gritty (e.g., pure Web3 SPAs, ancient raw HTML academic pages, tiny local businesses with embedded iFrames, foreign e-commerce, and heavily Cloudflare-protected domains). Expect crashes, timeouts, and weird HTML.
2. The pipeline sequentially executes the `audit-orchestrator` (`merge_report.py`) against your assigned sites.
3. It captures the raw JSON outputs and saves them in the `logs/agent1/` directory (e.g., `logs/agent1/www_apple_com.json`).
4. It automatically analyzes the results for crashes, bot-blocking failures, and false-positive anomalies (e.g., flagging if Apple.com throws too many critical errors).

## 3. Analyze and Fix
Once the pipeline finishes, it will generate an analysis report:
`logs/agent1/analysis_report.md`

1. **Read the Analysis Report:** This is your primary diagnostic tool. Look for crashes, timeouts, or the automated warnings indicating your severity thresholds might be too aggressive.
2. **Review the JSON:** If a site failed or threw an anomaly, open its specific JSON file in the `logs/` directory to see exactly which `id` (e.g., `CRAWL-003` or `ENGAGE-005`) triggered the issue.
3. **Patch the Skills:** Navigate to the `brand-ai-readiness-audit/skills/` directory and modify the underlying Python scripts (`crawl_check.py`, `engagement_check.py`, etc.) to fix the bugs or adjust the heuristic thresholds. 
   - *Example: If `engagement_check.py` is flagging "Thin content" on a site that you know is an SPA, you need to update `engagement_check.py` to be smarter about JS-rendered text.*

## 4. Iterate and Commit
1. Re-run the pipeline to ensure your fixes worked and didn't cause regressions on your other sites.
2. Once your pipeline runs cleanly with zero crashes and zero flagged anomalies, commit your code and logs.
```bash
git add .
git commit -m "agent1: Fixed SPA engagement bug and tuned schema threshold"
git push
```

---

# 🚀 Iteration 2: Heuristics & False Positives

**Your specific assignment for Iteration 2 focuses exclusively on `identity_check.py` and `engagement_check.py`.**

1. **Pull the latest `main`:** The `main` branch now contains robust, crash-proof anti-bot/parsing logic. Ensure your branch has this code.
   ```bash
   git pull origin main
   ```
2. **Re-run the Pipeline:** Execute `python scripts/run_pipeline.py agent1` to run against your gritty corpus.
3. **Hunt False Positives / False Negatives:** Now that the script doesn't crash, look at the logical outputs in your logs. 
   - Is `engagement_check.py` flagging modern SPAs (like Uniswap) as having "Thin Content" just because it can't render JS?
   - Is `identity_check.py` failing to extract phone numbers or social links from local businesses?
4. **Tune the Heuristics:** Open `engagement_check.py` and `identity_check.py` and improve their logic. Adjust word-count thresholds, add specific edge cases for SPAs, or refine regexes for local businesses.
5. **Push:** Commit your tuning adjustments and push them back!
