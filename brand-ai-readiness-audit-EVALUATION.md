# Evaluation Report: `brand-ai-readiness-audit` Marketplace
**Round 3 — Adobe University Hackathon 2026**

## Methodology

The sandbox this evaluation ran in has no general internet egress (only pypi/npm/github-class domains are reachable), so the marketplace's scripts cannot be pointed at arbitrary live URLs here. To still produce a real functional benchmark rather than a pure code read-through, I:

1. Installed the exact dependencies in `requirements.txt` (plus `w3lib`, an undeclared transitive dependency every script imports directly).
2. Built a **10-site synthetic corpus** — each site is a faithful reconstruction of a common real-world markup archetype (SSR Next.js app, bare CSR React shell, WordPress local-business page, Shopify-style PDP, Cloudflare-fronted storefront, a real WAF challenge page, etc.), each with **hand-labeled ground truth** for what a correct auditor should (and should not) flag.
3. Ran the **actual, unmodified** check scripts (`crawl_check.py`, `schema_check.py`, `freshness_check.py`, `identity_check.py`, `engagement_check.py`, `extraction_check.py`) against each fixture, intercepting only the network layer (`requests.get`) so real HTTP calls never leave the sandbox but the scripts' own parsing/decision logic runs untouched.
4. Separately exercised `merge_report.py` (the orchestrator) with canned sub-reports to test dedup, severity summary, proactive-recommendation logic, and conformance to the marketplace's own `report-schema.json`.

This is not a substitute for live-web generalization testing, but it is a legitimate, reproducible way to stress-test the actual decision logic, and it surfaced several concrete, high-confidence bugs (not stylistic nitpicks) detailed below.

---

## Corpus & Results

| Fixture | Archetype | Result |
|---|---|---|
| `good_01_saas_marketing` | Clean, fully-optimized SaaS site | ✅ Zero findings — correct |
| `bad_robots_blocked_ai` | robots.txt disallows GPTBot/anthropic-ai/CCBot | ✅ CRAWL-001 fired correctly |
| `spa_bare_react_no_ssr` | Empty `#root` CSR shell, no SSR | ✅ Caught almost everything (9/10 expected signals); only missed a "placeholder title" case |
| `spa_ssr_ok_nextjs` | Next.js framework markers *but* full SSR content | ⚠️ Correctly avoided the CSR false-positive, but wrongly reported "no CTA" despite a working CTA button |
| `stale_local_business` | 14-year-stale copyright, no date metadata | ✅ All staleness signals caught correctly |
| `waf_block_real` | Genuine Cloudflare bot-challenge page (403 + Ray ID) | ✅ Correctly identified as blocked |
| `cf_badge_false_positive_trap` | Normal storefront, footer merely *mentions* "Cloudflare" as a trust badge | ❌ **Entire audit misfires** — falsely reports the whole site as bot-blocked and skips every other check |
| `ecommerce_good_pdp` | Product page, complete `Product` schema, alt text, dates | ❌ Misses the real CTA ("Add to cart"), flags a false "contradictory description," and conflates Product schema with brand-identity schema |
| `ambiguous_entity_no_disambiguation` | Single-word brand name ("Mercury"), zero `sameAs`/Wikidata grounding | ⚠️ Flags generic "no schema," but never surfaces the actual *name-collision* risk, and silently skips the external-corroboration check because the page is short |
| `cookie_wall_and_iframes` | Cookie banner + 3 ad iframes + untitled YouTube embed | ✅ All signals caught correctly |

**Bottom line:** on unambiguous, textbook failure cases (blocked robots.txt, bare CSR shells, egregious staleness, cookie walls/iframe abuse), detection is strong and the suggested fixes are correct and specific. The problems cluster in edge cases and in the more "editorial" checks (identity/consistency), which is exactly where hackathon judges are likely to probe, since they explicitly test **unseen** sites.

---

## Findings, by severity

### 🔴 Critical — will misfire on real, common sites

**1. The bot-block detector triggers on the word "Cloudflare" anywhere in the page, not on evidence of an actual block.**
`bot_detection.py` (duplicated verbatim into all six skill folders) does:
```python
block_markers = ['cloudflare', 'ray id', 'access denied', ...]
if any(marker in text for marker in block_markers): return True
```
Roughly a third of the web sits behind Cloudflare, and it's extremely common for sites to say so in a footer trust badge ("Protected by Cloudflare"), a privacy policy, or a status page. In our test, an entirely ordinary, well-formed storefront that just mentions Cloudflare in a sentence got **misclassified as "Site Blocked Bot Access (200)"** — and because every check script returns immediately after this classification, **all six specialist checks silently skip that page**, producing a report that says nothing except a false "critical: blocked" verdict. This is the single highest-impact bug: it produces confidently wrong output on a large, common class of real sites, which the rubric explicitly penalizes ("without false positives").
*Fix:* only treat this as a block when the *status code* is 403/429/503 **and** the page body is short/templated (a real challenge page), not on keyword presence in an otherwise normal, content-rich page.

**2. The audit hammers the target site with 6+ concurrent, duplicated requests per run — which can cause the bug above to trigger for real.**
`merge_report.py` runs all six scripts concurrently via `ThreadPoolExecutor`, and each script independently re-fetches the homepage, and several also independently re-fetch `robots.txt`/`sitemap.xml`. A single "audit" burst-fetches the same handful of URLs 6–10 times in a few seconds with an identical User-Agent. Basic rate limiters (very common on small/mid business sites) will return 429s to some of those requests — which `is_blocked_response()` interprets as "the site blocks AI bots," a false positive *caused by the auditor's own architecture*, not by the site.
*Fix:* fetch each unique URL once, cache the response, and pass it to all specialist checks.

### 🟠 High — systematic detection gaps

**3. CTA detection misses extremely common real CTA phrasing.**
`CTA_KEYWORDS` is a flat keyword list matched by substring. It has no entry for **"quote"**, **"cart"**, **"get a"**, **"add to"**, etc. In our tests, both **"Add to cart"** (the single most common e-commerce CTA in existence) and **"Get my free quote"** were reported as "No obvious Call to Action" — a false negative on two of the most standard, unambiguous CTA patterns on the web. This will generate wrong, embarrassing findings on a large fraction of real commerce and lead-gen sites.

**4. Paraphrase is confused with contradiction.**
`entity-identity-audit`'s "contradictory brand descriptions" check (IDENT-003) uses raw token-Jaccard overlap with a 0.20 threshold. Two genuinely consistent, differently-worded marketing sentences about the same product ("weighs 2.8lbs... lifetime warranty" vs. "2.8lb ultralight... with lifetime warranty") scored **0.167 Jaccard** and were flagged as a **contradiction** — even though every fact stated is identical. Since meta descriptions and OG descriptions are *routinely* hand-written differently for SEO vs. social-share purposes, this check will false-positive constantly on normal sites, which is exactly the kind of well-formed-but-differently-phrased content the rubric asks the judges to watch for.

**5. The "proactive FAQPage schema" recommendation is dead code.**
In `merge_report.py`:
```python
findings_text = " ".join(f"{f.get('title','')} {f.get('evidence','')} ..." for f in unique_findings)
has_question_content = bool(re.search(r'\b(how|what|why)\b', findings_text, re.IGNORECASE))
```
This scans the **audit's own generated finding text** for "how/what/why" — not the *website's actual page content*. Since none of the fixed finding titles/evidence strings in this codebase ever contain those words, this proactive recommendation **never fires, on any site**, in our full 10-site corpus. It's clearly meant to detect Q&A-style page content and instead checks nothing meaningful. This is worth flagging because "proactive, beyond-defect recommendations" is an explicit rubric line item, and one of the four proactive rules is non-functional.

**6. SPA-shell detection is duplicated four times with inconsistent thresholds, and misfires on short-but-real pages.**
`crawl_check.py`, `schema_check.py`, `freshness_check.py`, and `engagement_check.py` each reimplement their own "is this an SPA?" heuristic independently (word-count cutoffs of 100/150/300, combined differently with framework-marker checks). Because the threshold is **pure body word count with no requirement that framework markers actually be present**, a short — but perfectly normal, server-rendered — marketing homepage (our "ambiguous brand" fixture, ~40 words of real text) got classified as an "SPA shell," which **silently suppressed the external-corroboration check** for that page. A genuinely important signal (the site has zero outbound links to third parties) was dropped not because of any actual JS-rendering issue, but because the page was short. This also means the four skills can disagree with each other about whether the *same* page is an SPA, since the thresholds and logic aren't shared.

**7. Only the single homepage is ever audited — never a real crawl.**
The contest's own sample evidence string ("Crawled 12 product pages; 0/12 contain schema.org markup") implies checks should sample multiple pages of a site. Every script in this marketplace takes one `url` argument and audits exactly that one page. For a real brand (whose product/article pages are usually where structured-data and freshness problems actually live, per Appendix D), a homepage-only audit will systematically under- or over-state the brand's real AI-readiness. This is a meaningful scope gap relative to what "discoverability" auditing usually requires in practice.

### 🟡 Medium — conceptual gaps vs. the Round-2 reasoning

**8. Entity ambiguity (Appendix D's "mistaken identity" problem) isn't actually assessed — only its remedy is.**
`entity-identity-audit` checks whether `sameAs`/social links *exist*, but never estimates whether a brand's name is actually ambiguous in the first place (e.g., a single dictionary word, or a name that collides with a well-known entity). In our "Mercury" fixture — a textbook case of the exact problem Appendix D describes — the tool produced the same generic "no Organization schema found" finding it would give *any* site missing schema, with no elevated priority or distinct framing for the specific name-collision risk. The remedy (add `sameAs`) is right, but the diagnosis never distinguishes "you're missing schema" from "you're missing schema *and* your name is dangerously generic," which is the more actionable and differentiating insight the appendix is actually pointing at.

**9. `freshness-corroboration`'s "corroboration" check doesn't check the wider web — only the target page's own outbound links.**
Appendix D's core idea is: *does the wider web independently agree with the brand's own claims?* The implemented check (FRESH-005) instead counts the site's own outbound `<a href>` links to any external domain. A page can pass this check by linking to a payment processor or a font CDN, and can fail it despite being extensively covered/cited elsewhere on the web, because that corroboration signal is never looked up. This check answers a different (and much weaker) question than the one Appendix D poses; a genuine corroboration check would need to search the web for independent mentions of the brand/claim, which the current design doesn't attempt.

**10. `structured-data-audit`'s "boilerplate ratio" isn't implemented, despite being documented.**
`SKILL.md` for `content-extraction-audit` states step 3 is "Check the text-to-HTML ratio and warn if boilerplate... heavily outweighs core content," and lists `EXTRACT-003` as a finding ID — but `extraction_check.py` only implements two checks (`EXTRACT-001`, `EXTRACT-002`); no boilerplate-ratio logic or `EXTRACT-003` exists anywhere in the code. The skill's documentation overstates what it does.

**11. The orchestrator's declared self-validation step doesn't exist.**
`audit-orchestrator/SKILL.md` states step 3 is "Validate output against `references/report-schema.json`," but `merge_report.py` contains no schema validation code (no `jsonschema` import, no `validate()` call — confirmed by grep). Worse, if it *were* run, it would fail: `report-schema.json` marks `is_spa_degraded` as a required top-level field, which `merge_report.py` never emits, and marks `confidence` as required on every finding, but `crawl_check.py`, `identity_check.py`, and `engagement_check.py` never set it. (Note: this does **not** violate the contest's own minimum schema in the PDF, which only requires `id/title/severity/evidence/suggested_action` — but it is a self-inconsistency between what the marketplace documents and what it does, and an unverified claim.)

### 🟢 Minor — packaging hygiene

- `__pycache__/*.pyc` files for both CPython 3.12 and 3.13 are committed inside the zip in every skill folder — should be gitignored/excluded from the submission.
- `requirements.txt` doesn't pin `w3lib`, which every script imports directly (`from w3lib.html import get_base_url`); it currently works only because `extruct` happens to pull it in transitively.
- `bot_detection.py`, the `HEADERS` dict, and the "SKILLS-BLOCKED" finding block are copy-pasted verbatim into all six skill folders rather than centralized — each `agentskills.io` skill folder does need to be independently self-contained, so *some* duplication is structurally required by the format, but six independently-maintained copies of the same block increases the chance they drift (as the SPA-detection heuristic already has, see #6).
- `merge_report.py`'s dedup logic drops a finding if its exact `title` string has already been seen from an earlier skill — brittle if two unrelated checks ever produce the same generic wording; ID-based dedup alone would be safer.
- All specialist skills declare `allowed-tools: [web_fetch, bash]`, but the actual scripts call Python's `requests` library directly rather than going through a `web_fetch` tool — meaning the marketplace's real-world portability depends entirely on the executing agent's shell having outbound network access. In agent sandboxes with restricted egress (not uncommon), every script would fail with "Failed to fetch page" and the audit would report nothing but critical fetch errors.

---

## Scoring against the official Round 3 rubric

| Criterion | Assessment |
|---|---|
| **Detection accuracy** | Solid on unambiguous cases (robots.txt blocks, bare CSR shells, severe staleness, cookie walls). Undermined by a critical false-positive class (#1/#2) and two systematic false-negative classes (#3 CTA keywords, #4 paraphrase-as-contradiction) that will recur on ordinary, unseen sites. **Good, not excellent.** |
| **Suggested-action quality** | Fixes that do fire are correct, specific, and mechanism-sound (SSR/pre-rendering, sameAs, JSON-LD types, WAF whitelisting), with useful effort/priority tagging beyond the schema floor. Weakened by one non-functional proactive rule (#5) and generic proactive suggestions that don't differentiate by brand risk (#8). **Good.** |
| **Output design** | Clear, structured, evidence + severity + prioritized action per finding; exceeds the contest's minimum schema with `confidence`, `category`, `effort`. Undercut by the schema self-inconsistency (#11) and by the false-block short-circuit (#1) that can produce a nearly-empty, misleading report for a fine site. **Good.** |
| **Skill-format & engineering hygiene** | All 7 `SKILL.md` files have valid frontmatter and match the agentskills.io shape; manifest is well-formed with exactly one entrypoint. Docs overstate implemented behavior in two places (#10, #11); packaging includes dev artifacts (`__pycache__`); undeclared dependency (`w3lib`). **Adequate, needs cleanup.** |
| **Marketplace composition** | Six specialists is a real decomposition by concern, not padding, and the orchestrator does genuinely merge/dedupe/prioritize rather than just concatenating. Docked for duplicated-and-*inconsistent* SPA-detection logic across four skills (#6) and copy-pasted glue code that isn't factored into a shared reference. **Good.** |
| **Generalization** | This is where the corpus testing matters most: several bugs (#1 Cloudflare keyword, #3 CTA list gaps, #4 Jaccard contradiction check, #6 SPA word-count threshold) are exactly the kind of brittle heuristics that look fine on the sites the authors tested against but misfire predictably on unseen, ordinary sites. **This is the area most at risk given the contest's explicit unseen-site evaluation.** |

---

## Priority fix list (highest leverage first)

1. **Fix the Cloudflare/bot-block false positive** (#1) — this is the one bug most likely to produce a badly wrong report on a normal, popular site during judging.
2. **Fetch each URL once and share the response** across the six specialist checks (#2) — removes the self-inflicted rate-limit risk and cuts runtime/bandwidth.
3. **Expand and generalize CTA detection** (#3) — move from a static substring list toward a small pattern set covering `get (a|my) ...`, `add to ...`, `book a ...`, `request a ...`, etc.
4. **Fix or remove the paraphrase-as-contradiction check** (#4) — either raise the bar substantially (require actual factual conflict, e.g. differing numbers/entities), or drop the Jaccard heuristic in favor of checking for explicit numeric/date/name mismatches only.
5. **Fix the FAQPage proactive-recommendation bug** (#5) — scan the actual page text/headings for question-style content, not the audit's own generated findings.
6. **Unify the SPA-detection heuristic into one shared, marker-gated check** (#6) — require an actual framework marker *and* low word count together, not word count alone, and share the function rather than reimplementing it four times.
7. **Extend to a small multi-page crawl** (#7) — even 3–5 pages (homepage + one or two linked content/product pages) would substantially improve real-world validity versus a homepage-only audit.
8. **Add an explicit name-ambiguity signal** (#8) — e.g., flag when the brand name is a common dictionary word/short generic term with no `sameAs` grounding, and raise its priority above a generic "add schema" finding.
9. **Reframe corroboration as inbound/third-party, not outbound** (#9) — the current check answers a different question than Appendix D asks.
10. Clean up packaging (#pycache, pin `w3lib`, either implement or remove the documented-but-missing checks/validation, fold the schema-consistency gap).
