# Zappos - Prompt 3: Structured Data & Machine Readability
**Agent:** GEMINI
**Site:** https://www.zappos.com
**Captured:** 2026-09-08T18:52:50.931582

---

Zappos HTML-source audit

Only these Zappos URLs were inspected:

https://www.zappos.com/
https://www.zappos.com/robots.txt

No external website was used.

(a) JSON-LD / schema.org structured data

Result: NOT FOUND on site / not verifiable in the accessible HTML source.

The accessible HTML representation of https://www.zappos.com/ exposes the page body and product data, but does not expose the <head> or an accessible JSON-LD block.

I could not directly verify:

<script type="application/ld+json">

or:

schema.org

Therefore:

Structured data	Finding
JSON-LD	NOT FOUND / NOT VERIFIABLE
schema.org	NOT FOUND / NOT VERIFIABLE
Organization	NOT FOUND / NOT VERIFIABLE
Product	NOT FOUND / NOT VERIFIABLE
WebSite	NOT FOUND / NOT VERIFIABLE
Raw HTML evidence

The accessible source instead exposes ordinary product information directly:

“Brand Name”
“Steve Madden”
“Product Name”
“Banks”
“Gender”
“Men's”
“Price”
“$79.99”

This confirms product information is present in the accessible HTML, but does not establish schema.org markup.

(b) OpenGraph meta tags

Result: NOT FOUND / NOT VERIFIABLE in the accessible HTML source.

The accessible HTML does not expose the page's <head> sufficiently to directly verify tags such as:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>
<meta property="og:type" ...>

Therefore the exact OpenGraph values are:

og:title — NOT FOUND / NOT VERIFIABLE
og:description — NOT FOUND / NOT VERIFIABLE
og:image — NOT FOUND / NOT VERIFIABLE
og:url — NOT FOUND / NOT VERIFIABLE
og:type — NOT FOUND / NOT VERIFIABLE

I am not treating this as proof that Zappos has no OpenGraph tags; the accessible source simply does not expose enough of the <head> to verify them.

(c) Is the main content available in raw HTML?

YES.

A substantial amount of the homepage content is directly available in the fetched HTML.

Navigation

The source contains:

“Women”
“Men”
“Kids”
“Brands”
“Sneakers”
“Sports”
“Back to School”
“Sale”
“Help & Support”

Homepage content

It directly contains:

“# Zappos Homepage”

“First Day Essentials From the backpack they carry with pride to the water bottle that never leaves their side.”

“The Fall Sports Shop A winning lineup for a season full of two-a-days, meets & matches.”

“Desk to Dinner Versatile Steve Madden styles...”

Product information

The HTML also directly contains individual product names, genders, prices, ratings and stock information. For example:

“Brand Name Steve Madden”

“Product Name Banks”

“Gender Men's”

“Price $79.99”

There are many further products with equivalent fields throughout the HTML.

Determination

Main content: available directly in raw/fetched HTML.

JavaScript may be used for interactive functionality, but the evidence available here shows that the principal textual navigation, promotional content and product data are already present in the HTML.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL: https://www.zappos.com/robots.txt

The file is directly accessible and begins:

“# Global robots.txt updated 2026-06-03”

“User-agent: *”

It then specifies restrictions including:

“Disallow: /bin/”

“Disallow: /logout”

“Disallow: /register”

“Disallow: /account”

“Disallow: /cart$”

“Disallow: /marty/account”

“Disallow: /multiview/”

“Disallow: /my-orders”

“Disallow: /item-details”

“Disallow: /my-returns”

“Disallow: /return-item”

It also contains:

“Noindex: /a/the-style-room/filters/”

“Noindex: /search?term=*”

“Disallow: /search?term=*”

AI-specific crawler rules

The retrieved file contains a generic rule:

User-agent: *

I found no separate AI-specific User-agent entry in the retrieved robots.txt, such as:

User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: PerplexityBot

The actual retrieved robots file instead applies its listed restrictions to:

“User-agent: *”

Therefore, based strictly on this file, there is no explicitly named AI-crawler block found. The generic restrictions apply to all user agents for the specified paths.

Meta tags

AI-specific meta crawler directives: NOT FOUND / NOT VERIFIABLE.

The accessible HTML does not expose enough of the <head> to verify a robots meta tag or an AI-specific crawler directive.

Final findings
Question	Site-only finding
JSON-LD / schema.org	NOT FOUND / NOT VERIFIABLE in accessible HTML
Structured-data types	NOT FOUND / NOT VERIFIABLE
OpenGraph tags	NOT FOUND / NOT VERIFIABLE
Main content in HTML	YES
Product data in HTML	YES
robots.txt available	YES
AI-specific User-agent rule	NOT FOUND
Generic crawler restrictions	YES — specified paths are disallowed/noindexed
AI-specific meta directives	NOT FOUND / NOT VERIFIABLE