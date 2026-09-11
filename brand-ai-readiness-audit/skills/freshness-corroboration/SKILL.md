---
name: freshness-corroboration
description: Audits a website for stale content dates and lacks of external corroboration signals.
license: MIT
---
# Freshness & Corroboration Audit
## When to use
Use to determine if a brand's facts are up-to-date and adequately corroborated by external authoritative sources.
## Inputs
- `url` (string): The website URL to audit.
## Procedure
1. Run `scripts/freshness_check.py` on the input URL.
2. Parse HTML `<time>` and schema `datePublished`/`dateModified` tags.
3. Flag dates older than 12 months as stale.
4. Check copyright year in the footer.
5. Check for outbound links corroborating stated facts.
## Output
A JSON sub-report containing discoverability findings related to freshness and corroboration.
