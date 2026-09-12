# Iteration 1 Analysis & Merge

**Date:** 2026-09-12
**Status:** Completed

## Analytical Findings
After distributing the 210 highly gritty, failure-prone websites across the three agent branches, the agents reported massive failures on the initial pipeline.
1. **Bot Mitigation Failures:** The default `python-requests` User-Agent was instantly blocked by Cloudflare, resulting in 403s and 429s, breaking the HTML parsers.
2. **Encoding Failures:** `run_pipeline.py` crashed when saving JSON reports for foreign-language sites (e.g., Yahoo Japan) because Windows default encoding is not UTF-8.
3. **HTML Parsing Crashes:** Ancient academic pages and poorly built local sites used capitalized HTML tags (e.g., `<META NAME="Description">`) which caused our strict `BeautifulSoup` queries to fail and crash.

## Architectural Decisions & Fixes Merged
1. **Robust Bot Detection:** We selected Agent 2's implementation of `is_blocked_response()`. It uses regex and string matching to detect Cloudflare `cf-chl-bypass`, Captchas, and HTTP `403`/`429`. This was merged into all 5 specialist scripts.
2. **Resilient Parsing:** We merged Agent 2's case-insensitive Regex searches for `title` and `og:description` into `schema_check.py`, and added `try/except` blocks around `extruct.extract` to prevent crashes on invalid raw HTML.
3. **UTF-8 Support:** We updated the `run_pipeline.py` file handlers to explicitly enforce `encoding="utf-8"`.
4. **Chrome Headers:** We applied a standard Chrome User-Agent and `verify=False` to bypass basic bot traps and broken SSL certs on local business sites.

## Conclusion
The `main` branch is now highly resilient against broken DOMs and basic WAF rules. We are ready to proceed to Iteration 2 to refine the heuristic thresholds.
