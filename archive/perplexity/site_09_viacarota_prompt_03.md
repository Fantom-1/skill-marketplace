# Via Carota - Prompt 3: Structured Data & Machine Readability
**Agent:** PERPLEXITY
**Site:** https://www.viacarota.com
**Captured:** 2026-09-08T18:27:56.150846

---

(a) JSON-LD / schema.org structured data

URL inspected:
https://www.viacarota.com/

Finding: NOT FOUND on site in the accessible HTML source.

I could not extract a:

<script type="application/ld+json">

block or visible schema.org structured-data markup from the fetched HTML.

The raw page content instead contains ordinary page text such as:

“Via Carota is the West Village osteria of celebrated downtown chefs Rita Sodi and Jody Williams.”

“VIA CAROTA MENU”

“51 Grove Street, New York City”

Structured-data type
Restaurant: NOT FOUND on site in accessible HTML
LocalBusiness: NOT FOUND on site in accessible HTML
Event: NOT FOUND on site in accessible HTML
Other JSON-LD/schema.org types: NOT FOUND on site in accessible HTML

I am reporting what was exposed in the fetched HTML; this does not establish that the live server has no structured data outside the accessible extraction.

(b) OpenGraph meta tags

Finding: NOT FOUND on site in the accessible HTML extraction.

I could not extract raw tags such as:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>

Therefore:

Meta tag	Exact value
og:title	NOT FOUND on site
og:description	NOT FOUND on site
og:image	NOT FOUND on site
og:url	NOT FOUND on site
og:type	NOT FOUND on site

The accessible HTML does contain the actual page content, including:

“Your neighborhood place for a leisurely lunch with a friend, family dinners or a late-night amaro.”

and:

“Via Carota is the West Village osteria of celebrated downtown chefs Rita Sodi and Jody Williams.”

(c) Is the main content available in raw HTML?

Yes.

URL:
https://www.viacarota.com/

The fetched HTML directly contains the restaurant's substantive content.

Raw evidence

At the beginning of the returned HTML:

“Your neighborhood place for a leisurely lunch with a friend, family dinners or a late-night amaro.”

The main restaurant description is also directly present:

“Via Carota is the West Village osteria of celebrated downtown chefs Rita Sodi and Jody Williams. Renowned for its simple, seasonal menu, Via Carota serves Italian food reminiscent of home in a spirit of relaxed care and warmth.”

The page also contains:

“VIA CAROTA MENU”

and:

“A plain-text version of the Via Carota menu is available here.”

Further down:

“Our aim is simple: to honor markets and farms from one season to the next, nurture our chefs, and pursue that elegant balance in cooking between authenticity and spontaneity.”

The address is also directly present:

“51 Grove Street, New York City”

and the contact email:

“Please email us at ciao@viacarota.com”

Finding: The main textual content is directly available in the fetched HTML. The accessible evidence does not indicate that JavaScript rendering is required to obtain this main content.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL attempted:
https://www.viacarota.com/robots.txt

Result: NOT FOUND / not retrievable.

The fetch returned:

“URL https://www.viacarota.com/robots.txt is not safe to open (non-retryable error)”

Therefore I could not inspect the actual robots.txt contents.

AI crawler rules

Because the file could not be retrieved:

GPTBot: NOT FOUND on site / not verifiable
ChatGPT-User: NOT FOUND on site / not verifiable
ClaudeBot: NOT FOUND on site / not verifiable
Google-Extended: NOT FOUND on site / not verifiable
Other AI crawler directives: NOT FOUND on site / not verifiable

I will not infer their presence or absence.

HTML meta robots

A meta name="robots" directive was NOT FOUND in the accessible HTML extraction.

Therefore:

<meta name="robots" ...>

NOT FOUND on site in the accessible HTML.

No AI-crawler-specific HTML directive could be verified.

Raw evidence summary
Question	Finding
JSON-LD	NOT FOUND on site in accessible HTML
schema.org type	NOT FOUND on site in accessible HTML
OpenGraph tags	NOT FOUND on site in accessible HTML
Main content in raw HTML	YES
JavaScript required for main textual content?	No evidence of that; main content is directly present in fetched HTML
robots.txt	Could not retrieve
AI crawler rules	NOT FOUND on site / not verifiable because robots.txt could not be retrieved
HTML meta robots	NOT FOUND on site

Only https://www.viacarota.com was inspected.