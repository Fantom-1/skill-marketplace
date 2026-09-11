# Crawl & Render Audit Signals

This checklist defines the concrete signals checked by the `crawl-render-audit` skill.

| Signal | Domain | Severity | Detection Mechanism |
|--------|--------|----------|---------------------|
| `robots.txt` AI blocks | Discoverability | Critical | Parse `robots.txt` and check if user-agents like `GPTBot`, `Google-Extended`, or `CCBot` are disallowed. |
| `noindex` meta tags | Discoverability | Critical | Parse HTML for `<meta name="robots" content="noindex">`. |
| Missing XML sitemap | Discoverability | High | Attempt to fetch `/sitemap.xml`; check for HTTP 200 and valid XML structure. |
| Stale sitemap `lastmod` | Discoverability | Medium | Parse sitemap XML; flag if `lastmod` date is older than 6 months. |
| Canonical URL issues | Discoverability | High | Check for `<link rel="canonical">`; ensure it points to a valid, absolute URL. |
| JS-rendering dependency | Engagement/Discoverability | High | Detect empty `<div id="root">`, `<div id="app">`, `__NEXT_DATA__`, or `<noscript>` fallbacks in the raw HTML. |
| Content in iframes | Engagement/Discoverability | Medium | Count `<iframe>` tags in the body that might hide main content. |
| Slow page payload | Engagement | Medium | Measure raw HTML response size; flag if > 5MB. |
