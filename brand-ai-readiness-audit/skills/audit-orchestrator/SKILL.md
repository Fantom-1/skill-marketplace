---
name: audit-orchestrator
description: Entrypoint skill that orchestrates the execution of 5 specialist audit skills (crawl, schema, freshness, identity, engagement) and merges their findings into a final prioritized audit report.
license: MIT
---
# Brand AI-Readiness Audit Orchestrator
## When to use
Use when auditing a brand's website to generate a complete AI-readiness and engagement report.
## Inputs
- `url` (string): The website URL or domain to audit.
## Procedure
1. Execute `crawl-render-audit` on the target URL.
2. Execute `structured-data-audit` on the target URL.
3. Execute `freshness-corroboration` on the target URL.
4. Execute `entity-identity-audit` on the target URL.
5. Execute `engagement-audit` on the target URL.
6. Pass all generated sub-reports to `scripts/merge_report.py`.
7. Output the finalized JSON report.
## Output
A JSON report matching the schema defined in `references/report-schema.json`.
