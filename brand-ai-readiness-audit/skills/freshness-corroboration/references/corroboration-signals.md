# Freshness & Corroboration Audit Signals

| Signal | Domain | Severity | Detection Mechanism |
|--------|--------|----------|---------------------|
| Stale content dates | Discoverability | High / Critical | Check `<time>`, `datePublished`/`dateModified`. Fallback to Last-Modified or 4-digit years. >1 year (High), >10 years (Critical). |
| No date signals | Discoverability | High / Medium | Flag pages with zero date metadata (escalates to High if no dates exist and stale logic isn't triggered). |
| Copyright outdated | Discoverability | Medium / High / Critical | Parse copyright range (e.g., 2010-2026), check highest year. >= 2 years old (Medium), > 5 years (High), > 10 years (Critical). |
| Inconsistent facts | Discoverability | Low | Check if `<title>` and `<h1>` have zero word overlap (ignoring brand stop words and domain extensions). |
| No corroboration | Discoverability | Low | Check for outbound links. Suppressed on SPA shells. Commercial sites graded leniently. |

**Note**: Corroboration and date findings may include a `confidence: "low"` field if an SPA shell is detected, as content is likely populated via JS.
