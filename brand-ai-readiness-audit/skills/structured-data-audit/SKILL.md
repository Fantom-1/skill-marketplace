---
name: structured-data-audit
description: Audits a website for missing or malformed structured data (JSON-LD), OpenGraph tags, and evaluates plain-text factual clarity vs non-text media lock-in.
license: MIT
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
## Output
A JSON sub-report containing discoverability findings related to structured data and machine readability.
