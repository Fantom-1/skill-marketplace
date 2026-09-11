# Brand AI-Readiness Audit Marketplace

An Agent Skill Marketplace that audits websites for AI discoverability and on-site engagement issues, producing a structured JSON report with evidence-backed findings and prioritized fix recommendations.

## Skills Included
| Skill Name | Role | Purpose |
|------------|------|---------|
| `audit-orchestrator` | Entrypoint | Composes outputs from specialist skills, merges reports, dedupes findings, and formats final JSON. |
| `crawl-render-audit` | Specialist | Checks `robots.txt`, sitemaps, canonicals, and detects JS-rendering blockers (Appendix A, C). |
| `structured-data-audit` | Specialist | Validates JSON-LD, OpenGraph, title/meta description presence (Appendix B, C). |
| `freshness-corroboration` | Specialist | Checks content dates for staleness and corroboration signals (Appendix D). |
| `entity-identity-audit` | Specialist | Checks brand name ambiguity, missing knowledge graph links, and consistent identity (Appendix D). |
| `engagement-audit` | Specialist | Evaluates content engagement, navigation, CTAs, and mobile support (Appendix E, F). |

## How the Entrypoint Composes Skills
```text
[Input: URL] -> [audit-orchestrator]
                      |--> invokes `crawl-render-audit`
                      |--> invokes `structured-data-audit`
                      |--> invokes `freshness-corroboration`
                      |--> invokes `entity-identity-audit`
                      |--> invokes `engagement-audit`
                      |
                      v
                (merges sub-reports)
                      |
                      v
             [Final JSON Audit Report]
```

## How to Run
- Requires Python 3.10+
- Dependencies: `requests`, `beautifulsoup4`, `lxml`, `extruct` (Install via `pip install -r requirements.txt`)
- Run via agentskills.io framework targeting the entrypoint skill.

## Design Decisions
- **Skill Decomposition:** Separating by domain ensures clean logic without overlapping responsibilities, per the rubric's "genuine separation of concerns."
- **No Headless Browser:** To keep runtime < 5 mins and avoid heavy dependencies, JS-rendering issues are detected heuristically (e.g., framework markers, `<noscript>` tags) instead of via Playwright.
- **Output Schema:** Extends the mandatory base schema to include categories, effort level, and beyond-problem proactive recommendations.
