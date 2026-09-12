# Linear - Prompt 3: Structured Data & Machine Readability
**Agent:** CHATGPT
**Site:** https://linear.app
**Captured:** 2026-09-08T17:22:27.408930

---

(a) JSON-LD / schema.org structured data

NOT FOUND on site in the accessible HTML source.

URL: https://linear.app/

The fetched HTML contains substantial page content, but the accessible source does not expose a raw:

<script type="application/ld+json">

block or a schema.org reference.

Therefore:

JSON-LD: NOT FOUND on site
schema.org structured data: NOT FOUND on site
Structured-data types: NOT FOUND on site

I will not infer structured data from the visible page content.

(b) OpenGraph meta tags

NOT FOUND on site in the accessible HTML source.

The accessible HTML extraction does not expose the <head> metadata or raw tags such as:

<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
<meta property="og:url" content="...">
<meta property="og:type" content="...">

Therefore:

OpenGraph tag	Finding
og:title	NOT FOUND on site
og:description	NOT FOUND on site
og:image	NOT FOUND on site
og:url	NOT FOUND on site
og:type	NOT FOUND on site

Raw accessible HTML does contain the page title/content, including:

“The product development system for teams and agents”

but this is not evidence of an og:title value.

(c) Is the main content available in raw HTML?

Yes.

The fetched HTML contains the main page content directly.

URL: https://linear.app/

Raw evidence includes:

“The product development system for teams and agents”

“Purpose-built for planning and building products. Designed for the AI era.”

“A new species of product tool. Purpose-built for modern teams with AI workflows at its core, Linear sets a new standard for planning and building products.”

“Designed for workflows shared by humans and agents. From drafting PRDs to pushing PRs.”

The HTML also contains extensive product sections:

“Make product operations self-driving”

“Define the product direction”

“Move work forward across teams and agents”

“Review PRs and agent output”

“Understand progress at scale”

The changelog is also directly present:

“Coding sessions on mobile” — “Jul 30, 2026”

“Agent-assisted text editing” — “Jul 22, 2026”

“Loops” — “Jul 16, 2026”

Finding: The main textual content is available in the fetched HTML. The evidence does not establish that JavaScript rendering is required to obtain this content.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL: https://linear.app/robots.txt

The site's raw robots.txt contains:

User-Agent: *
Disallow: /api/
Disallow: /cdn-cgi/
Allow: /api/og/

Sitemap: https://linear.app/sitemap.xml

There is no explicitly named AI crawler in this file.

The generic rule is:

“User-Agent: *”

followed by:

“Disallow: /api/”

“Disallow: /cdn-cgi/”

and:

“Allow: /api/og/”

Therefore, the accessible robots.txt does not explicitly block a named AI crawler such as GPTBot, ClaudeBot, or Google-Extended.

However, the generic Disallow rules apply to all user agents, including AI crawlers, for those specific paths.

HTML meta crawler directives

NOT FOUND on site in the accessible HTML source.

The fetched homepage HTML does not expose a raw:

<meta name="robots" content="...">

or AI-crawler-specific meta directive.

Therefore, I cannot verify an HTML-level crawler block.

Final findings
Check	Result
JSON-LD	NOT FOUND on site
schema.org	NOT FOUND on site
OpenGraph tags	NOT FOUND on site in accessible HTML
Main content in raw HTML	YES
JavaScript required for main content	No evidence of this
Named AI crawlers in robots.txt	NOT FOUND on site
Generic robots rules	/api/ and /cdn-cgi/ disallowed; /api/og/ allowed
HTML robots meta tag	NOT FOUND on site in accessible HTML

Only linear.app was used for the site analysis.