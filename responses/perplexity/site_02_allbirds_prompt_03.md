# Allbirds - Prompt 3: Structured Data & Machine Readability
**Agent:** PERPLEXITY
**Site:** https://www.allbirds.com
**Captured:** 2026-09-08T17:08:27.653199

---

(a) JSON-LD / Schema.org structured data

NOT FOUND on site in the fetched HTML evidence.

URL: https://www.allbirds.com/

The fetched page exposes the HTML content, but no raw:

<script type="application/ld+json">
...
</script>

block or explicit schema.org markup was exposed in the HTML returned for inspection.

Therefore:

JSON-LD: NOT FOUND on site
Schema.org structured-data types: NOT FOUND on site
Product/Organization schema types: NOT FOUND on site

Raw HTML evidence from the page instead includes ordinary page content such as:

<h1>Wildly Comfortable. Super Natural.</h1>

and product names:

Women's Canvas Cruiser Slip On
Women's Cruiser Slip On
Women's Runner NZ Slip On
Men's Runner NZ Slip On
Men's Cruiser

https://www.allbirds.com/

(b) OpenGraph meta tags

NOT FOUND on site in the fetched HTML evidence.

The fetched HTML does not expose raw <meta property="og:..."> values.

Therefore the following cannot be reported without inventing data:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>

URL: https://www.allbirds.com/

(c) Is the main content available in raw HTML?

YES.

The fetched HTML contains substantial visible content without requiring JavaScript rendering.

URL: https://www.allbirds.com/

Raw extracted evidence:

Wildly Comfortable. Super Natural.
New Arrivals
Women's Canvas Cruiser Slip On
Women's Cruiser Slip On
Women's Runner NZ Slip On
Women's Canvas Cruiser
Women's Tree Runner NZ
Men's Runner NZ Slip On
Men's Cruiser

It also contains detailed descriptive text:

Lightweight, bouncy, and wildly comfortable, Allbirds shoes make any outing feel effortless. Slip in, lace up, or slide them on and enjoy the comfy support.

and:

DESIGNED FOR EVERYDAY WEAR
Easy-to-wear styles made for daily routines, weekend plans, travel, and everything in between.

and:

Materials From The Earth
We replace petroleum-based synthetics with natural alternatives wherever we can. Like using wool, tree fiber, and sugarcane.

https://www.allbirds.com/

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL: https://www.allbirds.com/robots.txt

The general rule is:

User-agent: *
Disallow: /a/downloads/-/*
Disallow: /admin
Disallow: /cart
Disallow: /orders
Disallow: /checkouts/
Disallow: /checkout
...

There is no Disallow: / under User-agent: *.

There is, however, a complete block for a specifically named crawler:

User-agent: Nutch
Disallow: /

The fetched robots.txt contains no user-agent entry explicitly identifying an AI crawler. Therefore:

AI-crawler blocking in robots.txt: NOT FOUND on site.

Meta tags

AI-blocking meta tag: NOT FOUND on site in the fetched HTML evidence.

No exposed raw HTML evidence showed a tag such as:

<meta name="robots" content="noai">

or:

<meta name="robots" content="noimageai">

Therefore I cannot establish a meta-tag-based AI block from the fetched HTML.

Raw findings
Item	Result
JSON-LD	NOT FOUND on site
Schema.org types	NOT FOUND on site
OpenGraph tags	NOT FOUND on site
Main content in raw HTML	YES
User-agent: * blocks entire site	NO
Explicit AI crawler in robots.txt	NOT FOUND on site
Nutch blocked	YES — Disallow: /
AI-blocking meta tag	NOT FOUND on site