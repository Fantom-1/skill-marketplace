---
name: crawl-render-audit
description: Audits a website for crawlability issues (robots.txt blocks, noindex, broken sitemaps) and heavy JS-render dependencies that block basic AI extraction.
license: MIT
---
# Crawl & Render Audit
## When to use
Use to determine if a website can be successfully reached and read by automated crawlers without executing JavaScript.
## Inputs
- `url` (string): The website URL to crawl.
## Procedure
1. Run `scripts/crawl_check.py` on the input URL.
2. Check `robots.txt` for disallow rules targeting AI bots.
3. Check for `<meta name="robots" content="noindex">`.
4. Validate XML sitemap presence and health.
5. Detect JS-heavy rendering (empty root divs, framework markers).
## Output
A JSON sub-report containing discoverability findings related to crawling and rendering.
