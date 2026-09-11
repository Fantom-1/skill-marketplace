# Adobe University Hackathon 2026 — Round 3
# Brand AI-Readiness Audit: Agent Skill Marketplace — Execution Plan

---

## Executive Summary

**Objective:** Build a multi-skill Agent Skill Marketplace that audits any website for AI discoverability and on-site engagement issues, producing a structured JSON report with evidence-backed findings and prioritized fix recommendations.

**Submission Format:** A zip (≤ 50 MB) containing `marketplace.json` + skill folders in agentskills.io format.

**Runtime Constraint:** < 5 minutes per website on a standard machine.

---

## Phase 0 — Research & Experimentation (Field Research)
**Duration:** ~2 days | **Milestone:** Signal Catalogue Complete

### 0.1 Understand the Problem Space
- **Task:** Study the Round 2 appendix concepts (A–F) and map them to concrete, testable signals.
- **Proof:** The appendix defines 6 failure modes. Each must map to ≥1 automated check.

| Appendix Concept | Domain | Concrete Signals to Test |
|---|---|---|
| A. Search visibility basics | Discoverability | `robots.txt` blocks, `noindex` meta, sitemap missing/broken, canonical issues |
| B. How assistants use sources | Discoverability | No structured data (JSON-LD/schema.org), missing OpenGraph, no clear factual statements in plain text |
| C. How machines read a page | Discoverability + Engagement | JS-rendered content invisible to crawlers, facts locked in images/video/PDFs, iframe-embedded content |
| D. Agreement across the web | Discoverability | Entity ambiguity (common name, no disambiguator), inconsistent NAP/brand info across sources, no Wikipedia/Wikidata presence |
| E. Personalization & prior context | Engagement | No personalization hooks, no contextual landing pages, no conversation-continuity signals |
| F. Why machines drop email content | Engagement (by analogy) | Key content buried in non-text (images, carousels), low signal-to-noise ratio, no clear headline/summary |

### 0.2 Field Research — Cited vs. Uncited Websites
- **Task:** Manually test 15–20 websites across categories (e-commerce, SaaS, local business, media, D2C brands) against ChatGPT, Perplexity, and Google AI Overviews.
- **Method:**
  1. Ask AI assistants about the brand → record whether cited, how accurately, and what sources used.
  2. Crawl the same sites with `curl`/`fetch` (no JS) vs. browser → diff what's visible.
  3. Check `robots.txt`, sitemaps, structured data, meta tags.
  4. Cross-reference brand facts on 3rd-party sites (Wikipedia, Crunchbase, social profiles).
- **Deliverable:** A **Signal Catalogue** spreadsheet mapping each observation to a repeatable, automatable check.
- **Checkpoint:** ✅ ≥ 20 distinct, repeatable signals identified with evidence from ≥ 3 real websites each.

### 0.3 Prioritize Signals by Impact & Generalizability
- **Task:** Rank signals by: (a) how often they appear in the wild, (b) severity of impact on AI discoverability/engagement, (c) feasibility of automated detection.
- **Deliverable:** Prioritized signal list grouped by skill domain (crawlability, structured-data, freshness, engagement, entity-identity).
- **Checkpoint:** ✅ Every signal has a severity tier (critical / high / medium) and a detection method defined.

---

## Phase 1 — Architecture & Design
**Duration:** ~1 day | **Milestone:** Marketplace Architecture Locked

### 1.1 Skill Decomposition Design

**Decision: 6 skills (5 specialist + 1 orchestrator)**

**Proof for this decomposition:**
- The rubric explicitly rewards "genuine separation of concerns" in marketplace composition.
- Each skill maps to a distinct failure-mode domain from the appendix, ensuring no overlap and clean composition.
- The orchestrator pattern lets us test/iterate each skill independently.

```
brand-ai-readiness-audit/          ← marketplace root (zipped)
├── marketplace.json                ← manifest with entrypoint
├── README.md                       ← describes each skill + composition
└── skills/
    ├── audit-orchestrator/         ← ENTRYPOINT: composes all skills, emits final report
    │   ├── SKILL.md
    │   ├── scripts/
    │   │   └── merge_report.py     ← merges sub-reports into final JSON schema
    │   └── references/
    │       └── report-schema.json  ← the required output schema
    │
    ├── crawl-render-audit/         ← Appendix A + C: can crawlers reach & read the page?
    │   ├── SKILL.md
    │   ├── scripts/
    │   │   └── crawl_check.py      ← robots.txt parser, sitemap validator, JS-render diff
    │   └── references/
    │       └── crawl-signals.md    ← checklist of signals
    │
    ├── structured-data-audit/      ← Appendix B + C: is content machine-extractable?
    │   ├── SKILL.md
    │   ├── scripts/
    │   │   └── schema_check.py     ← JSON-LD/microdata/RDFa validator, OpenGraph checker
    │   └── references/
    │       └── schema-signals.md
    │
    ├── freshness-corroboration/    ← Appendix D: are facts consistent, corroborated, unambiguous?
    │   ├── SKILL.md
    │   ├── scripts/
    │   │   └── freshness_check.py  ← date staleness, cross-source consistency, entity disambiguation
    │   └── references/
    │       └── corroboration-signals.md
    │
    ├── engagement-audit/           ← Appendix E + F: does the site retain visitors?
    │   ├── SKILL.md
    │   ├── scripts/
    │   │   └── engagement_check.py ← content accessibility, navigation clarity, CTA presence, signal-to-noise
    │   └── references/
    │       └── engagement-signals.md
    │
    └── entity-identity-audit/      ← Appendix D (identity): is the brand distinguishable?
        ├── SKILL.md
        ├── scripts/
        │   └── identity_check.py   ← brand name ambiguity, consistent descriptions, knowledge-graph presence
        └── references/
            └── identity-signals.md
```

### 1.2 Technology Choices

| Component | Technology | Proof / Justification |
|---|---|---|
| **Skill format** | agentskills.io SKILL.md + YAML frontmatter | Required by contest rules. Validated via `skills-ref validate`. |
| **Scripts language** | Python 3.10+ | Universally available, rich ecosystem for web scraping/parsing (`requests`, `beautifulsoup4`, `lxml`). Contest says "portable" — Python is the safest bet. |
| **HTML parsing** | `beautifulsoup4` + `lxml` | Industry standard for HTML parsing. Handles malformed HTML gracefully. Zero external service dependency. |
| **HTTP fetching** | `requests` (sync) | Simple, reliable, no async complexity. Respects `robots.txt` via `robotparser` stdlib. |
| **Structured data extraction** | `extruct` library | Extracts JSON-LD, Microdata, RDFa, OpenGraph, Dublin Core in one pass. Well-maintained, MIT licensed. |
| **Sitemap parsing** | `advertools` or custom XML parser | Parse XML sitemaps, check lastmod dates, validate URLs. |
| **robots.txt parsing** | `urllib.robotparser` (stdlib) | Built into Python, no external dependency. |
| **JS-render detection** | Heuristic diff (raw HTML vs. meta-content signals) | Compare content in raw HTML (`noscript` tags, empty containers, JS framework markers like `__NEXT_DATA__`, `id="app"`, `<div id="root"></div>`) to detect JS-dependent rendering. No headless browser needed — keeps runtime < 5 min. |
| **Report merging** | Python `json` module | Merge sub-reports into the required schema. No external dependency. |
| **Manifest format** | `marketplace.json` | Required by contest convention. |
| **Validation** | `skills-ref validate` (npm/pip) | Contest-recommended. Run on each skill folder before submission. |

**Why no headless browser (Playwright/Puppeteer)?**
- Adds ~200MB+ dependency, risks exceeding 50MB zip limit.
- Slows runtime significantly (spin-up per page).
- The heuristic approach (detecting JS framework markers, empty `<div>` shells, `noscript` fallbacks) is sufficient to *detect* that content is JS-rendered without actually rendering it — the skill's job is to *report the problem*, not render the page.

**Why no external APIs (Google Search API, etc.)?**
- Contest says "self-contained — no external service needed to resolve it."
- All checks must work from the website's own content + standard HTTP fetches.

### 1.3 Output Schema Design

```json
{
  "site": "<domain>",
  "audited_at": "<ISO 8601 timestamp>",
  "summary": {
    "total_findings": "<int>",
    "critical": "<int>",
    "high": "<int>",
    "medium": "<int>",
    "low": "<int>"
  },
  "findings": [
    {
      "id": "F-001",
      "skill_source": "<which skill produced this>",
      "category": "discoverability | engagement",
      "title": "<concise problem title>",
      "severity": "critical | high | medium | low",
      "evidence": "<specific, quantitative evidence from the site>",
      "suggested_action": {
        "summary": "<what to do>",
        "detail": "<how to do it, with code snippets or config examples where applicable>",
        "priority": "critical | high | medium | low",
        "effort": "low | medium | high"
      }
    }
  ],
  "proactive_recommendations": [
    {
      "id": "R-001",
      "title": "<improvement title>",
      "rationale": "<why this helps even though no defect was found>",
      "suggested_action": "<what to do>"
    }
  ]
}
```

**Proof:** Extends the minimum required schema from the handout (site, audited_at, summary, findings with id/title/severity/evidence/suggested_action) while adding `skill_source`, `category`, `detail`, `effort`, and a `proactive_recommendations` section — all of which the rubric rewards ("beyond-problem suggestions", "actionable report a non-expert could act on").

### Checkpoint: ✅ Architecture document reviewed, skill boundaries validated against all 6 appendix concepts, no overlap.

---

## Phase 2 — Development
**Duration:** ~3 days | **Milestone:** All Skills Implemented & Individually Tested

### 2.1 Scaffold the Marketplace Structure
- Create all directories and empty `SKILL.md` files with valid YAML frontmatter.
- Write `marketplace.json` manifest.
- Validate with `skills-ref validate` on each skill folder.
- **Checkpoint:** ✅ `skills-ref validate` passes on all 6 skill folders.

### 2.2 Develop Individual Skills (Parallel Tracks)

#### Track A: `crawl-render-audit` (Appendix A + C)
**Checks implemented:**
| # | Check | Detection Method | Severity if Failed |
|---|---|---|---|
| 1 | `robots.txt` blocks AI crawlers | Parse robots.txt, check for Disallow rules targeting GPTBot, Google-Extended, CCBot, anthropic-ai, etc. | Critical |
| 2 | `noindex` / `nofollow` meta tags | Parse `<meta name="robots">` on sampled pages | Critical |
| 3 | Missing/broken XML sitemap | Fetch `/sitemap.xml`, validate XML structure, check for HTTP errors | High |
| 4 | Stale sitemap `lastmod` dates | Parse sitemap `lastmod`, flag if > 6 months old | Medium |
| 5 | Canonical URL issues | Check `<link rel="canonical">` presence and correctness | High |
| 6 | JS-rendering dependency | Detect empty `<div id="root">`, `__NEXT_DATA__`, framework markers, `<noscript>` tags | High |
| 7 | Content locked in iframes | Detect `<iframe>` containing substantive content | Medium |
| 8 | Slow page (large HTML payload) | Measure response size, flag if > 5MB raw HTML | Medium |

**Checkpoint:** ✅ Skill runs on 5 test sites, produces valid sub-report JSON, zero false positives on known-good sites.

#### Track B: `structured-data-audit` (Appendix B + C)
**Checks implemented:**
| # | Check | Detection Method | Severity if Failed |
|---|---|---|---|
| 1 | No JSON-LD structured data | Use `extruct` to extract, flag if zero JSON-LD blocks | High |
| 2 | Invalid/incomplete schema.org markup | Validate extracted JSON-LD against schema.org types, check required properties | High |
| 3 | Missing OpenGraph tags | Check for `og:title`, `og:description`, `og:image`, `og:url` | Medium |
| 4 | Missing Twitter Card tags | Check for `twitter:card`, `twitter:title`, `twitter:description` | Medium |
| 5 | No `<title>` or empty `<meta description>` | Parse `<head>` section | High |
| 6 | Facts locked in images (no alt text) | Count `<img>` without `alt` attributes, flag high ratio | Medium |
| 7 | No clear factual statements in plain text | Analyze text density vs. boilerplate ratio | Medium |

**Checkpoint:** ✅ Correctly identifies missing structured data on 5 test sites with evidence.

#### Track C: `freshness-corroboration` (Appendix D — facts)
**Checks implemented:**
| # | Check | Detection Method | Severity if Failed |
|---|---|---|---|
| 1 | Stale content dates | Check `<time>`, `datePublished`, `dateModified` in JSON-LD and HTML | High |
| 2 | No date signals at all | Flag pages with zero date metadata | Medium |
| 3 | Copyright year outdated | Parse footer copyright, flag if > 1 year old | Medium |
| 4 | Inconsistent facts on-page | Check if `<title>`, JSON-LD `name`, OG title, and H1 agree | High |
| 5 | No corroboration signals | Check for links to authoritative external sources, citations | Medium |

**Checkpoint:** ✅ Detects stale/inconsistent content on test sites.

#### Track D: `entity-identity-audit` (Appendix D — identity)
**Checks implemented:**
| # | Check | Detection Method | Severity if Failed |
|---|---|---|---|
| 1 | Brand name ambiguity | Check if brand name is a common word/phrase, presence of `sameAs` links in JSON-LD | High |
| 2 | No `sameAs` / knowledge graph links | Check JSON-LD `Organization`/`WebSite` for `sameAs` pointing to Wikipedia, LinkedIn, social profiles | High |
| 3 | Inconsistent brand description | Compare `<meta description>`, JSON-LD `description`, OG description — flag divergence | Medium |
| 4 | Missing `Organization` schema | Check for JSON-LD `@type: Organization` with `name`, `url`, `logo` | High |
| 5 | No about page or clear identity statement | Check for `/about` page, "About" link in navigation | Medium |

**Checkpoint:** ✅ Flags identity issues on ambiguous-brand test sites.

#### Track E: `engagement-audit` (Appendix E + F)
**Checks implemented:**
| # | Check | Detection Method | Severity if Failed |
|---|---|---|---|
| 1 | No clear navigation / orientation | Check for `<nav>`, breadcrumbs, internal link structure | High |
| 2 | No clear CTAs on landing pages | Detect CTA patterns (buttons, links with action words) on main pages | Medium |
| 3 | High bounce risk: thin content | Measure text word count on key pages, flag if < 100 words | Medium |
| 4 | Content buried in carousels/accordions | Detect carousel/accordion patterns with hidden content | Medium |
| 5 | No mobile viewport meta | Check for `<meta name="viewport">` | High |
| 6 | Excessive ads/popups signals | Detect ad-related scripts, popup patterns | Medium |
| 7 | No contextual internal linking | Check for in-content links to related pages | Medium |
| 8 | Poor heading hierarchy | Validate H1 → H2 → H3 structure, flag skips or missing H1 | Medium |

**Checkpoint:** ✅ Correctly flags engagement issues on poor-UX sites.

#### Track F: `audit-orchestrator` (Entrypoint)
**Responsibilities:**
1. Receive input URL/domain from the agent.
2. Invoke each specialist skill in sequence (or describe composition order).
3. Collect sub-reports from each skill.
4. Merge into the final report JSON using `merge_report.py`.
5. De-duplicate overlapping findings.
6. Sort findings by severity (critical → low).
7. Append proactive recommendations.
8. Emit the final structured audit report.

**Checkpoint:** ✅ Orchestrator composes 5 sub-reports into a valid, de-duplicated final report.

### 2.3 Write SKILL.md Instructions
For each skill, write lean but complete SKILL.md with:
- `## When to use` — one-liner matching the skill's scope.
- `## Inputs` — URL/domain.
- `## Procedure` — numbered, deterministic steps (the rubric says "deterministic").
- `## Output` — sub-report schema (for specialist skills) or final report schema (for orchestrator).
- Tool declarations in `allowed-tools`.

**Checkpoint:** ✅ Every SKILL.md is < 500 lines, has all 4 required sections, passes `skills-ref validate`.

---

## Phase 3 — Compilation & Integration Testing
**Duration:** ~1.5 days | **Milestone:** End-to-End Audit Working on Unseen Sites

### 3.1 Integration Test — Full Pipeline
- Run the complete marketplace on **5 unseen websites** (sites never used during development):
  - 1 well-optimized site (expecting few findings)
  - 1 JS-heavy SPA (expecting crawl/render issues)
  - 1 small local business (expecting structured data gaps)
  - 1 media/content site (expecting freshness issues)
  - 1 e-commerce site (expecting engagement + structured data issues)
- **Validation criteria:**
  - Report JSON matches required schema.
  - No false positives on the well-optimized site (≤ 2 medium findings).
  - ≥ 3 high/critical findings on the poorly-optimized sites.
  - Runtime < 5 minutes per site.
  - All evidence fields contain specific, verifiable data (URLs, counts, code snippets).

**Checkpoint:** ✅ 5/5 test sites produce valid, accurate reports. Zero schema violations.

### 3.2 Generalization Stress Test
- Run on **3 additional edge-case sites:**
  - A site entirely in a non-English language.
  - A single-page application (SPA) with hash routing.
  - A site with aggressive `robots.txt` blocking.
- Verify graceful handling (meaningful findings or "unable to audit — blocked by robots.txt" with evidence).

**Checkpoint:** ✅ No crashes. Graceful degradation. Meaningful output in all cases.

### 3.3 Validation Pass
- Run `skills-ref validate` on every skill folder.
- Validate `marketplace.json` structure (exactly one `entrypoint: true`).
- Verify all `name` fields match directory names (lowercase, hyphens only).
- Check zip size < 50 MB (no model weights, no node_modules, no venv).

**Checkpoint:** ✅ All validations pass. Zero errors.

---

## Phase 4 — Deliverables & Packaging
**Duration:** ~0.5 days | **Milestone:** Submission-Ready Zip

### 4.1 Write README.md
Contents:
1. **Overview** — what the marketplace does, in 2-3 sentences.
2. **Skill Inventory** — table of all skills with name, purpose, and key checks.
3. **How the Entrypoint Composes Skills** — data flow diagram (text-based).
4. **How to Run** — prerequisites (Python 3.10+, pip packages), invocation instructions.
5. **Output Schema** — reference to the report schema.
6. **Design Decisions** — brief justification for skill decomposition, tech choices, and signal selection.

### 4.2 Final marketplace.json

```json
{
  "name": "brand-ai-readiness-audit",
  "version": "1.0.0",
  "skills": [
    { "id": "audit-orchestrator", "path": "skills/audit-orchestrator", "entrypoint": true },
    { "id": "crawl-render-audit", "path": "skills/crawl-render-audit" },
    { "id": "structured-data-audit", "path": "skills/structured-data-audit" },
    { "id": "freshness-corroboration", "path": "skills/freshness-corroboration" },
    { "id": "entity-identity-audit", "path": "skills/entity-identity-audit" },
    { "id": "engagement-audit", "path": "skills/engagement-audit" }
  ]
}
```

### 4.3 Package & Verify
- Create zip: `brand-ai-readiness-audit.zip`
- Verify contents: `marketplace.json` at root, all 6 skill folders present.
- Verify size < 50 MB.
- Unzip in a clean directory and run one final end-to-end test.

**Checkpoint:** ✅ Zip created, verified, and final test passes.

---

## Milestone Summary

| Phase | Milestone | Checkpoint Criteria | Target |
|---|---|---|---|
| **Phase 0** | Signal Catalogue Complete | ≥ 20 signals mapped, each with evidence from ≥ 3 sites | Day 2 |
| **Phase 1** | Architecture Locked | 6 skills designed, no overlap, schema defined | Day 3 |
| **Phase 2** | Skills Implemented | All 6 skills pass individual tests, SKILL.md validated | Day 6 |
| **Phase 3** | Integration Complete | 5 unseen sites produce valid reports, < 5 min each | Day 7.5 |
| **Phase 4** | Submission Ready | Zip < 50 MB, all validations pass, README complete | Day 8 |

---

## Risk Register

| Risk | Impact | Mitigation |
|---|---|---|
| JS-render detection without headless browser is inaccurate | Medium | Use multiple heuristics (framework markers, noscript tags, empty containers, script analysis). Flag as "likely JS-dependent" not "confirmed". |
| `robots.txt` blocks our own crawling during audit | High | Respect it — report "site blocks AI crawlers" as a Critical finding. This IS the finding. |
| False positives on well-built sites | High (rubric penalizes) | Conservative severity assignment. Require ≥ 2 evidence signals before flagging. Test extensively on known-good sites. |
| Zip exceeds 50 MB | Medium | No binary dependencies, no model weights, no large assets. Scripts only. |
| Runtime exceeds 5 minutes | Medium | Limit crawl depth to homepage + 5 internal pages. Parallelize checks where possible. Set HTTP timeouts. |
| Single skill does everything (no real decomposition) | High (rubric penalizes) | Architecture enforces separation — each skill has its own SKILL.md, scripts/, references/. Orchestrator only merges. |

---

## Rubric Alignment Matrix

| Rubric Criterion | How Our Plan Addresses It |
|---|---|
| **Detection accuracy** | Phase 0 field research ensures signals are evidence-backed. Phase 3 tests on unseen sites for generalization. Conservative flagging reduces false positives. |
| **Suggested-action quality** | Each finding includes `detail` (how to fix with code examples) + `priority` + `effort`. Proactive recommendations section for beyond-problem suggestions. |
| **Output design** | Extended JSON schema with categories, skill_source, effort estimates. Non-expert readable. |
| **Skill-format & engineering hygiene** | Every skill validated with `skills-ref validate`. Deterministic procedures. `allowed-tools` declared. `robots.txt` respected. |
| **Marketplace composition** | 6 skills with genuine separation of concerns (each maps to distinct appendix concepts). Orchestrator handles only merging/dedup. No padding. |
| **Generalization** | No hardcoded site patterns. All checks use generic signals (HTML structure, meta tags, schema.org). Phase 3 stress tests on diverse unseen sites. |

---

## Technology Stack Summary

```
┌─────────────────────────────────────────────┐
│           Agent Skill Marketplace            │
│         (agentskills.io format)              │
├─────────────────────────────────────────────┤
│  marketplace.json  │  README.md              │
├────────────────────┴────────────────────────┤
│                  Skills (6)                  │
│  ┌─────────────┐  ┌──────────────────────┐  │
│  │ Orchestrator │  │ 5 Specialist Skills  │  │
│  │ (entrypoint) │←─│ crawl-render         │  │
│  │              │←─│ structured-data      │  │
│  │  merge &     │←─│ freshness            │  │
│  │  compose     │←─│ entity-identity      │  │
│  │              │←─│ engagement           │  │
│  └─────────────┘  └──────────────────────┘  │
├─────────────────────────────────────────────┤
│              Scripts (Python)                │
│  requests · beautifulsoup4 · lxml · extruct │
│  urllib.robotparser (stdlib) · json (stdlib) │
├─────────────────────────────────────────────┤
│              References (.md)                │
│  Signal checklists · Report schema           │
└─────────────────────────────────────────────┘
```
