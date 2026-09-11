# Structured Data Audit Signals

| Signal | Domain | Severity | Detection Mechanism |
|--------|--------|----------|---------------------|
| No JSON-LD | Discoverability | High | Extract with `extruct`. Flag if 0 JSON-LD elements exist. |
| Invalid/Missing Schema | Discoverability | High | Basic validation of JSON-LD properties (e.g., Organization requires name, url). |
| Missing OpenGraph | Discoverability | Medium | Check `<meta property="og:title">`, `og:description`, `og:image`. |
| Missing Title/Desc | Discoverability | High | Check `<title>` and `<meta name="description">`. |
| Text vs Image facts | Engagement | Medium | High ratio of `<img>` without `alt` tags. |
| Low Text Density | Engagement | Medium | Very few plain-text paragraphs compared to the raw HTML size. |
