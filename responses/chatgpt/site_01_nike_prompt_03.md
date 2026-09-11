# Nike - Prompt 3: Structured Data & Machine Readability
**Agent:** CHATGPT
**Site:** https://www.nike.com
**Captured:** 2026-09-08T17:06:00.668011

---

(a) JSON-LD / Schema.org structured data

NOT CONFIRMED from the available raw HTML source.

URL fetched:
https://www.nike.com/

The fetched HTML exposes the page content, but the available source does not expose any raw:

<script type="application/ld+json">
...
</script>

or an explicit schema.org declaration.

Therefore:

JSON-LD: NOT FOUND in the accessible HTML evidence
Schema.org types: NOT FOUND in the accessible HTML evidence

I will not infer structured-data types from the rendered content.

(b) OpenGraph meta tags

NOT FOUND in the accessible HTML evidence.

The requested OpenGraph evidence would be tags such as:

<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
<meta property="og:url" content="...">

Those <head> tags are not exposed by the fetched HTML representation, so I cannot provide their values without inventing evidence.

URL:
https://www.nike.com/

(c) Is the main content available in raw HTML?

YES — substantial page content is present in the fetched HTML.

URL:
https://www.nike.com/

Raw extracted HTML/page-source evidence includes:

SHOW THEM
WHERE YOU STAND.
Division lines, drawn. The 2026 Rivalries Collection is touching down.
The Wait is Over
After two decades, the Air Jordan "Tour Yellow" returns.
PEGASUS
PLUS 2
Power tempo training for race day.
A stacked ZoomX foam midsole and exposed Air Zoom unit deliver 18% more energy return.
Engineered mesh helps keep the upper lightweight and breathable.
An updated Waffle design with a diagonal pattern and sharp edges improve traction and ground feel.

The HTML also contains navigation/product content such as:

Shoes
All Shoes
Jordan Shoes
Running Shoes
Basketball Shoes
Tennis Shoes
Training Shoes
Custom Shoes
Sale Shoes
Soccer Cleats

This demonstrates that substantial main content is available in the fetched HTML rather than requiring JavaScript rendering before any meaningful content is present.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL:
https://www.nike.com/robots.txt

For all unspecified crawlers, Nike has:

User-agent: *

followed by:

Disallow: */member/inbox
Disallow: */member/settings
Disallow: */p/
Disallow: */checkout/
Disallow: /*.swf$
Disallow: /*.pdf$
Disallow: /pdf/

There is no:

Disallow: /

under User-agent: *.

Nike does explicitly block several named crawlers. For example:

User-agent: Baiduspider
...
Disallow: /
User-agent: HaoSouSpider
...
Disallow: /
User-agent: Sogou web spider
...
Disallow: /

It also contains:

User-agent: Sogou inst spider
...
Disallow: /

and:

User-agent: Sogou spider2
...
Disallow: /

AI-crawler-specific blocking: NOT FOUND in the fetched robots.txt. I found no named AI-crawler User-agent entry in the returned robots.txt.

Meta-tag blocking

NOT FOUND / NOT VERIFIABLE from the available HTML source.

The fetched HTML representation does not expose the <head> meta tags needed to verify a tag such as:

<meta name="robots" content="noai, noimageai">

Therefore I cannot claim that Nike uses—or does not use—an AI-blocking meta tag.

Bottom line
Question	Finding
JSON-LD	NOT FOUND in accessible HTML evidence
Schema.org types	NOT FOUND in accessible HTML evidence
OpenGraph	NOT FOUND in accessible HTML evidence
Main content in HTML	YES — substantial content is present
Generic crawler blocked?	No blanket block
Named crawlers blocked?	Yes — Baiduspider, HaoSouSpider, Sogou variants
AI-specific robots.txt block	NOT FOUND
AI-specific meta block	NOT VERIFIABLE from available HTML source