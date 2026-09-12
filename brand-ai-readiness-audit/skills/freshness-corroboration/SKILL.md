---
name: freshness-corroboration
description: Audits a website for stale content dates and lacks of external corroboration signals.
license: MIT
version: 1.1.0
author: Antigravity
---
# Freshness & Corroboration Audit
## When to use
Use to determine if a brand's facts are up-to-date and adequately corroborated by external authoritative sources.
## Inputs
- `url` (string): The website URL to audit.
## Procedure
1. Run `scripts/freshness_check.py` on the input URL.
2. Parse HTML `<time>` and schema `datePublished`/`dateModified` tags.
3. Fallback: Parse 4-digit years from page text, HTTP Last-Modified headers, and footer copyright dates.
4. Flag dates older than 1 year as stale, scaling severity up to critical for >10 years.
5. Check for outbound links corroborating stated facts (except on SPAs).
6. Verify Title vs H1 alignment (skipping standard domain names and taglines).
## Limitations
- Operates on static HTML. If SPA shells are detected, corroboration checks are suppressed or downgraded to low confidence.
## Finding IDs
- **FRESH-001**: No explicit date metadata found
- **FRESH-002**: Content appears highly stale (>X years old)
- **FRESH-003**: Outdated copyright year
- **FRESH-004**: Inconsistent on-page facts (Title vs H1)
- **FRESH-005**: No external corroborating links
## Output
A JSON sub-report containing discoverability findings related to freshness and corroboration.
