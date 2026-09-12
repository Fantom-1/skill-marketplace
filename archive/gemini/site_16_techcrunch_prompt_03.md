# TechCrunch - Prompt 3: Structured Data & Machine Readability
**Agent:** GEMINI
**Site:** https://techcrunch.com
**Captured:** 2026-09-08T18:46:30.090917

---

TechCrunch HTML-source audit

Target inspected only: https://techcrunch.com/

(a) JSON-LD / schema.org structured data

Result: NOT FOUND in the accessible HTML representation.

I could not verify an exposed:

<script type="application/ld+json">

block or a schema.org structured-data declaration in the HTML source made available for inspection.

Raw evidence: The accessible HTML begins exposing page content directly, e.g.:

Latest
Startups
Venture
Apple
Security
AI
Apps
Disrupt 2026
Events
Podcasts
Newsletters

and article/content elements beginning with:

### Sila lands $1.4B Pentagon loan as militaries demand more batteries
Tim De Chant
5 hours ago

Types such as NewsArticle, Organization, WebSite, etc.: NOT FOUND / NOT VERIFIABLE in the accessible HTML.

(b) OpenGraph meta tags

Result: NOT FOUND in the accessible HTML representation.

I could not directly inspect the <head> section containing raw <meta> elements, so exact values for:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>
<meta property="og:type" ...>

are NOT FOUND / NOT VERIFIABLE from the HTML representation available to me.

I therefore cannot truthfully claim that particular og:* tags are present or absent.

Important distinction: this means not verifiable from the accessible HTML, not that the tags definitively do not exist on TechCrunch.

(c) Is the main content in raw HTML or does it require JavaScript?

Result: Main textual content is available in the accessible HTML.

The fetched HTML directly contains substantial page content, including headlines, authors, timestamps, categories, navigation and article descriptions.

Raw evidence
## Latest News

Aptoide becomes the first rival app store to return to Google Play in the US
Sarah Perez
1 hour ago

Another example:

## AI

Meta’s new Glimmer AI model offers a hint at Zuckerberg’s personal intelligence vision
Rebecca Bellan
4 hours ago

And:

## Startups

Discovered Materials is playing AI whack-a-mole to hunt cooler chips
Tim Fernholz
8 hours ago

Therefore, the principal textual homepage content does not require JavaScript rendering to be present in the fetched HTML.

This does not establish that every interactive feature on the site works without JavaScript.

(d) robots.txt / meta tags blocking AI crawlers
robots.txt

URL inspected: https://techcrunch.com/robots.txt

Result: NOT FOUND / NOT VERIFIABLE.

The direct retrieval returned:

Internal Error

Therefore I cannot extract or quote any User-agent, Disallow, Allow, GPTBot, OAI-SearchBot, ChatGPT-User, or other crawler directive from TechCrunch's robots.txt.

HTML meta robots

Result: NOT FOUND / NOT VERIFIABLE.

The accessible HTML representation does not expose the <head> sufficiently to verify an exact:

<meta name="robots" ...>

or an AI-specific meta directive.

Therefore:

Check	Result
robots.txt content	NOT FOUND / NOT VERIFIABLE
meta name="robots"	NOT FOUND / NOT VERIFIABLE
AI-specific meta directives	NOT FOUND / NOT VERIFIABLE
Evidence of an AI-crawler block	NOT VERIFIABLE
Final source-only determination
JSON-LD/schema.org: NOT FOUND / NOT VERIFIABLE in accessible HTML.
OpenGraph: NOT FOUND / NOT VERIFIABLE because the accessible representation does not expose the raw <head>.
Main content: YES — substantial textual content is directly present in the fetched HTML.
AI crawler blocking: NOT VERIFIABLE because robots.txt could not be retrieved and the relevant HTML meta tags were not exposed.

I have not used another website to fill any of these gaps.