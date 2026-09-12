# Asana - Prompt 3: Structured Data & Machine Readability
**Agent:** GEMINI
**Site:** https://www.asana.com
**Captured:** 2026-09-08T17:18:48.017417

---

(a) JSON-LD / schema.org structured data

NOT FOUND on site — not exposed in the accessible HTML source.

URL: https://www.asana.com/

The fetched HTML contains substantial body content, but the accessible source does not expose a raw block such as:

<script type="application/ld+json">

or a visible:

schema.org

Therefore, I cannot verify any JSON-LD or schema.org type from the accessible HTML.

Result: NOT FOUND on site / not exposed in accessible HTML evidence.

(b) OpenGraph meta tags

NOT FOUND on site — not exposed in the accessible HTML source.

The fetched HTML does not expose the <head> metadata needed to verify exact values for tags such as:

<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
<meta property="og:url" content="...">
<meta property="og:type" content="...">

Therefore:

Tag	Result
og:title	NOT FOUND on site
og:description	NOT FOUND on site
og:image	NOT FOUND on site
og:url	NOT FOUND on site
og:type	NOT FOUND on site

I will not infer these values from the visible page title or body text.

(c) Is the main content available in raw HTML?

Yes — substantial main content is available directly in the fetched HTML.

URL: https://www.asana.com/

Raw extracted HTML evidence includes:

“# The OS for human-agent teams”

“Supercharge your teams to get things done”

“Try Asana for free. No credit card required.”

The HTML also directly contains:

“Asana Work Graph®”

“A neural network of everything your company is doing, every person, task, project, goal, and dependency connected, so humans and agents always know who is doing what, by when, and toward which goal.”

and:

“Pre-built AI agents that work alongside your team inside real workflows, with shared memory, governance, and context from the Work Graph, so they are ready to go on day one.”

The page also contains product names, descriptions, navigation, buttons, and footer content directly in the fetched HTML.

Result: The main textual content is present in the raw/fetched HTML. The available evidence does not show that JavaScript rendering is required to obtain this main content.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

NOT VERIFIABLE from the requested site with the available direct fetch.

I attempted:

URL: https://www.asana.com/robots.txt

The fetch returned:

“URL https://www.asana.com/robots.txt is not safe to open (non-retryable error)”

Therefore, I cannot truthfully report the contents of Asana's robots.txt or claim that particular AI crawlers are blocked.

Result: NOT FOUND / NOT VERIFIABLE on site.

HTML meta crawler directives

NOT FOUND on site.

The accessible HTML extraction does not expose a raw tag such as:

<meta name="robots" content="...">

or another crawler-specific meta directive.

Therefore, I cannot verify an HTML-level AI crawler block.

Important distinction

The Asana homepage HTML itself contains:

“AI Teammates”

“AI Studio”

“Asana Dash”

“MCP and AI Connectors”

and extensive AI-related content.

That is not evidence of crawler permissions, so I am not using it to infer anything about robots restrictions.

Final findings
Check	Verified result
JSON-LD	NOT FOUND on site / not exposed in accessible HTML
schema.org	NOT FOUND on site / not exposed in accessible HTML
OpenGraph tags	NOT FOUND on site / not exposed in accessible HTML
Main content in raw HTML	YES
JavaScript required for main content	No evidence of this in fetched HTML
robots.txt AI-crawler rules	NOT VERIFIABLE
HTML AI-crawler meta tags	NOT FOUND on site / not exposed

Only https://www.asana.com was used for the site-content analysis.