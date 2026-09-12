# Figma - Prompt 3: Structured Data & Machine Readability
**Agent:** CHATGPT
**Site:** https://www.figma.com
**Captured:** 2026-09-08T17:25:24.176196

---

(a) JSON-LD / schema.org structured data

NOT FOUND on site in the accessible raw HTML.

URL inspected: https://www.figma.com/

The fetched HTML contains the page's actual navigation and content, including:

“The intelligent canvas for infinite creativity”

“One workspace for your entire product development process.”

“Design anything you can imagine”

“Build with intention”

But the accessible HTML does not expose a <script type="application/ld+json"> block or visible schema.org structured-data markup.

Raw evidence: The fetched HTML runs through the page content and footer without an exposed JSON-LD block.

Types: NOT FOUND on site in the accessible HTML.

(b) OpenGraph meta tags

NOT FOUND on site in the accessible HTML returned.

URL inspected: https://www.figma.com/

I could not extract raw <meta property="og:..."> elements or their values from the accessible HTML.

Therefore:

OpenGraph field	Raw HTML evidence
og:title	NOT FOUND on site
og:description	NOT FOUND on site
og:image	NOT FOUND on site
og:url	NOT FOUND on site
og:type	NOT FOUND on site

This means I cannot verify from the accessible HTML that the tags are absent from Figma's actual served source; they are simply not exposed in the HTML extraction available here.

(c) Is the main content in raw HTML or does it require JavaScript?

The main content is available in the fetched HTML.

URL: https://www.figma.com/

The raw HTML directly contains the main headline:

# The intelligent canvas for infinite creativity

It also contains:

“One workspace for your entire product development process.”

“Made so your whole team can go from WIP to ship, together.”

“Design anything you can imagine”

“Turn your ideas into apps, websites, and products.”

“Build with intention”

“Dev tools that take you all the way to production.”

“Move fast in the right direction on an AI-native canvas.”

“Teammates and AI agents work in the same space with shared context.”

It also contains product names and links directly in the HTML:

“Figma Design”

“Figma Make”

“Figma Weave”

“Dev Mode”

“Figma Motion”

“FigJam”

“Figma Slides”

“Figma Draw”

“Figma Sites”

“Figma Buzz”

These are present in the fetched HTML rather than being represented only by an empty application shell.

Finding: YES — substantial main content is available in the raw HTML. The evidence does not require me to infer that JavaScript rendering is necessary for the primary textual content.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL attempted: https://www.figma.com/robots.txt

The request was blocked by the site's robots policy:

“Failed to fetch https://www.figma.com/robots.txt: Fetch denied by robots.txt”

Therefore the actual contents of Figma's robots.txt are:

NOT FOUND on site — blocked from retrieval.

I cannot truthfully report whether it contains GPTBot, ClaudeBot, Google-Extended, or other AI-crawler rules because the file itself could not be retrieved.

HTML meta robots

URL: https://www.figma.com/

A meta name="robots" directive was NOT FOUND in the accessible HTML extraction.

Therefore:

meta name="robots" — NOT FOUND on site

I cannot establish an AI-crawler restriction from the HTML evidence available.

Raw-evidence conclusion
Question	Finding
JSON-LD / schema.org	NOT FOUND on site in accessible HTML
OpenGraph tags	NOT FOUND on site in accessible HTML
Main content	YES — substantial content is directly present in fetched HTML
robots.txt	Could not retrieve — fetch denied by robots.txt
AI crawler rules in robots.txt	NOT FOUND on site / not verifiable because robots.txt was blocked
HTML meta robots	NOT FOUND on site in accessible HTML

Only https://www.figma.com was inspected. The failed robots.txt retrieval was from the same domain.