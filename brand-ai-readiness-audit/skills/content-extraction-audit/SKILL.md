---
name: content-extraction-audit
description: Audits a website for LLM readability, checking for semantic layout tags, boilerplate ratios, and accessibility of core textual content to basic scraping bots.
allowed-tools:
  - web_fetch
  - bash
license: MIT
---
# Content Extraction Audit

## When to use
Use to determine if an AI assistant (using basic headless browsing or HTTP fetching) can easily extract the primary informational content of a page without hallucinating on excessive boilerplate or hitting interstitial blockades.

## Inputs
- `url` (string): The website URL to audit.

## Procedure
1. Run `scripts/extraction_check.py` on the input URL.
2. Evaluate usage of semantic HTML5 grouping tags (`<article>`, `<main>`, `<section>`).
3. Check the text-to-HTML ratio and warn if boilerplate (nav/footer) heavily outweighs core content.
4. Detect interstitial pop-ups (cookie walls, paywall overlays) that might obscure content.

## Output
A JSON sub-report containing extraction findings (`EXTRACT-001` through `EXTRACT-003`) formatted according to the report schema.
