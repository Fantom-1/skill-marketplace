# Structured Data Audit Signals

| Signal | Domain | Severity | Detection Mechanism |
|--------|--------|----------|---------------------|
| No JSON-LD / Microdata | Discoverability | High / Medium (SPA) | Extract with `extruct` (`json-ld`, `microdata`). Flag if 0 elements exist. |
| Invalid/Missing Schema | Discoverability | Medium | Validates `name` or `headline` on targeted schema (Organization, Product, LocalBusiness, Article, Person). |
| Missing OpenGraph | Discoverability | Medium | Check `<meta property="og:title">`, `og:description`, `og:image`. |
| Missing Title/Desc | Discoverability | High / Medium (SPA) | Check `<title>` and `<meta name="description">`. |
| Text vs Image facts | Engagement | Medium | High ratio (>50% AND >=3) of `<img>` without `alt` tags. |

**Note**: All schema findings may include a `confidence: "low"` field if an SPA framework or interstitial shell is detected, as static scraping may miss JS-rendered schema.
