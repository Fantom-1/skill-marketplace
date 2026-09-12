---
name: audit-orchestrator
description: Master entrypoint skill orchestrating 5 specialist audit skills (crawl-render, structured-data, freshness, entity-identity, engagement) to output a merged, prioritized Brand AI-Readiness Audit report.
license: MIT
---
# Brand AI-Readiness Audit Orchestrator

## When to use
Use when auditing any website or domain to evaluate LLM crawler discoverability, entity grounding, structural navigation, engagement readiness, and bot accessibility.

## Inputs
- `url` (string): Target website URL or domain.

## Procedure
1. Concurrently execute specialist audit sub-skills:
   - `crawl-render-audit` (`crawl_check.py`)
   - `structured-data-audit` (`schema_check.py`)
   - `freshness-corroboration` (`freshness_check.py`)
   - `entity-identity-audit` (`identity_check.py`)
   - `engagement-audit` (`engagement_check.py`)
2. Pass sub-reports to `scripts/merge_report.py` for deduplication, severity sorting, and proactive strategic recommendation generation.
3. Validate output against `references/report-schema.json`.

## Output
A unified JSON report conforming to `references/report-schema.json`.

