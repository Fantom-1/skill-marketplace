---
name: entity-identity-audit
description: Audits a website for brand ambiguity, entity identity clarity, structured graph schema grounding, and social profile corroboration.
license: MIT
---
# Entity Identity Audit

## When to use
Use when evaluating whether a website clearly grounds its brand identity for LLM crawlers, search engines, and Knowledge Graph entities to avoid hallucinations and entity ambiguity.

## Inputs
- `url` (string): The website URL or domain to audit.

## Procedure
1. Run `scripts/identity_check.py` on the input URL.
2. Recursively flatten JSON-LD, Microdata, and RDFa graphs to inspect `Organization`, `Brand`, `LocalBusiness`, `Corporation`, `WebSite`, and related identity schemas.
3. Extract `sameAs` identity profile links from structured data nodes and corroborate against on-page HTML social links (Twitter/X, LinkedIn, GitHub, Wikipedia, Wikidata).
4. Perform fuzzy semantic comparison across `<meta description>`, OpenGraph, and structured schema descriptions to detect true brand message contradictions while ignoring non-material wording variations.
5. Inspect navigation links for explicit "About", "Company", "Docs", or "Team" pages, applying web-application context filters for app dashboards and login gates.

## Output
A JSON sub-report containing discoverability findings (`IDENT-001` through `IDENT-004`) formatted according to the report schema.

