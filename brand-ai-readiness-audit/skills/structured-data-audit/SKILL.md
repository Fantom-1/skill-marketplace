---
name: structured-data-audit
description: Audits a website for missing or malformed structured data (JSON-LD and microdata), OpenGraph tags, and evaluates plain-text factual clarity vs non-text media lock-in.
allowed-tools: [web_fetch, bash]
license: MIT
version: 1.1.0
author: Antigravity
---
# Structured Data Audit
## When to use
Use to verify if a website properly exposes machine-readable facts and metadata to AI systems.
## Inputs
- `url` (string): The website URL to audit.
## Procedure
1. Run `scripts/schema_check.py` on the input URL.
2. Extract all JSON-LD and microdata using `extruct`.
3. Check for essential OpenGraph tags.
4. Check for presence of `<title>` and `<meta description>`.
5. Identify images lacking `alt` attributes.
## Limitations
- This audit relies on static HTML extraction (no headless browser). When SPA shell markers are detected, findings are downgraded to medium confidence, as rendering may provide the missing metadata at runtime.
## Finding IDs
- **SCHEMA-001**: No JSON-LD structured data found
- **SCHEMA-002**: Missing required properties in Structured Data
- **SCHEMA-003**: Missing or very short `<title>`
- **SCHEMA-004**: Missing `<meta description>`
- **SCHEMA-005**: Missing OpenGraph tags
- **SCHEMA-006**: Facts locked in images (Missing alt text)
## Output
A JSON sub-report containing discoverability findings related to structured data and machine readability.
