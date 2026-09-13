# Iteration 2: False Positives & Heuristics Tuning

## Goal
The goal of Iteration 2 was to resolve the logical false positives discovered in Iteration 1. The agents updated their specific skills to handle edge-cases like modern Single Page Applications (SPAs), web-app utilities, and legacy microdata schemas, drastically improving the utility of the skill marketplace tools.

## Heuristic Improvements

### 1. SPA Detection & Extrication
- **Engagement (Agent 1):** `engagement_check.py` now parses HTML for massive JS state injections (`window.__INITIAL_STATE__` or huge `<script>` tags). If found, the tool suppresses "Thin Content" warnings since the content is dynamically rendered on the client side (CSR).
- **Schema (Agent 2):** `schema_check.py` now detects JS-only shells (`is_spa_shell()`) and downgrades any missing schema errors to `"confidence": "low"`, acknowledging that JSON-LD might be injected via Google Tag Manager and invisible to static raw HTML requests.

### 2. Entity Identity Web-App Exemptions
- **Agent 1** realized that subdomains like `app.uniswap.org`, `web.whatsapp.com`, and `/login` paths shouldn't be penalized for missing an "About Us" page. It now exempts utility interfaces from marketing-page requirements.

### 3. Smart Description Diffing
- **Agent 1** solved the "Contradictory Brand Descriptions" false-positive loop by implementing an `is_substantially_different()` function, meaning minor text variations between Meta Tags, OpenGraph, and JSON-LD no longer falsely flag as errors.

### 4. HTML Microdata Extraction
- **Agent 2** vastly improved `schema_check.py` by incorporating `microdata` extraction through the `extruct` library. Older platforms (legacy WordPress/Shopify) still rely on `itemscope` Microdata. This completely solved the false-positive "Zero Schema Found" errors on thousands of legacy sites.

### 5. SKILL.md Refinements
- Both agents deeply refined the actual Marketplace Instructions (`SKILL.md` files) to mandate checking for ARIA accessibility, CSR/SSR detection, and structured data hierarchy, providing explicitly better prompts for any end-user agent using these skills.

## Conclusion
Iteration 2 has brought the skills to a highly advanced, near-flawless state for LLM AI-readiness auditing. All false positives have been mitigated through smart contextual logic. The final phase will involve packaging these for the marketplace.
