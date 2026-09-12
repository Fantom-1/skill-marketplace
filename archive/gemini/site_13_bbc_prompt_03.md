# BBC - Prompt 3: Structured Data & Machine Readability
**Agent:** GEMINI
**Site:** https://www.bbc.com
**Captured:** 2026-09-08T18:39:37.069363

---

(a) JSON-LD / schema.org structured data

NOT FOUND on site — not verifiable from the accessible HTML.

URL attempted: https://www.bbc.com/

The HTML could not be fetched. Therefore I could not inspect the document for:

<script type="application/ld+json">

or schema.org markup.

Consequently, the presence of types such as:

NewsArticle
Organization
WebSite
NewsMediaOrganization

is NOT FOUND on site / not verifiable from the accessible HTML.

Raw retrieval evidence:

“Failed to fetch https://www.bbc.com/: (robots.txt) Fetch denied by robots.txt (OAI-SearchBot)”

(b) OpenGraph meta tags

NOT FOUND on site — not verifiable from the accessible HTML.

I could not retrieve the HTML <head>, so I could not verify values for:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>
<meta property="og:type" ...>

I therefore cannot truthfully state that these tags are absent; they are simply not inspectable in the retrieved HTML.

Raw evidence: the homepage fetch was blocked before HTML was returned.

(c) Main content: raw HTML vs JavaScript

NOT FOUND on site — not verifiable.

No HTML document was returned, so I could not determine whether BBC's main content is:

directly present in the server-delivered HTML, or
populated/rendered through JavaScript.

The only directly verifiable retrieval result is:

“Failed to fetch https://www.bbc.com/: (robots.txt) Fetch denied by robots.txt (OAI-SearchBot)”

Therefore, no claim about the rendering architecture can be made from the accessible source.

(d) robots.txt / meta tags blocking AI crawlers
robots.txt

The robots.txt contents are NOT FOUND on site because they could not be retrieved.

URL attempted: https://www.bbc.com/robots.txt

Raw retrieval result:

“Failed to fetch https://www.bbc.com/robots.txt: (robots.txt) Fetch denied by robots.txt (OAI-SearchBot)”

Therefore I cannot extract or quote the actual User-agent, Disallow, or Allow directives from BBC's robots.txt.

However, the retrieval system explicitly reports that its access to BBC was “Fetch denied by robots.txt (OAI-SearchBot)”.

HTML meta robots

NOT FOUND on site — not verifiable.

Because the HTML itself was not returned, I could not inspect for:

<meta name="robots" content="...">

or crawler-specific meta directives.

Final HTML-source findings
Check	Result
JSON-LD	NOT FOUND / not verifiable
schema.org types	NOT FOUND / not verifiable
OpenGraph tags	NOT FOUND / not verifiable
Main content in raw HTML	NOT FOUND / not verifiable
JavaScript rendering requirement	NOT FOUND / not verifiable
robots.txt contents	NOT FOUND — fetch blocked
Meta robots	NOT FOUND / not verifiable
AI-crawler blocking evidence	Yes: retrieval explicitly reports “Fetch denied by robots.txt (OAI-SearchBot)”

No external website was accessed or used.