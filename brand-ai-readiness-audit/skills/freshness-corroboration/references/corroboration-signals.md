# Freshness & Corroboration Audit Signals

| Signal | Domain | Severity | Detection Mechanism |
|--------|--------|----------|---------------------|
| Stale content dates | Discoverability | High | Check `<time>`, `datePublished`, `dateModified` in JSON-LD and HTML. Flag if older than 1 year. |
| No date signals | Discoverability | Medium | Flag pages with zero date metadata. |
| Copyright outdated | Discoverability | Medium | Parse footer copyright year, flag if older than current year. |
| Inconsistent facts | Discoverability | High | Check if `<title>`, JSON-LD `name`, OG title, and H1 agree. |
| No corroboration | Discoverability | Medium | Check for outbound links to authoritative sources (Wikipedia, media). |
