# Spotify SE - Prompt 3: Structured Data & Machine Readability
**Agent:** CHATGPT
**Site:** https://www.spotify.com/se-en/
**Captured:** 2026-09-08T19:01:02.192443

---

Non-English Site HTML-source audit

The category specification supplied two possible URLs. I inspected only those supplied domains:

https://www.spotify.se
https://www.alibaba.com

No external websites were used.

(a) JSON-LD / schema.org structured data
https://www.spotify.se

NOT FOUND on site.

The homepage could not be fetched:

“Failed to fetch https://www.spotify.se/: Cache miss”

Therefore JSON-LD or schema.org types cannot be verified.

https://www.alibaba.com

NOT FOUND / NOT VERIFIABLE in the accessible HTML.

The accessible HTML contains extensive inline localization/application data, including:

"localData":{"bucket":"exp","topResourcePic":"...","lang":"en_US"}

and:

"verifiedFeatures":["5K+ industries covered","Factory-direct pricing","Sample & customization available"]

but I did not find an exposed:

<script type="application/ld+json">

or a directly exposed schema.org declaration in the accessible HTML.

Types such as Organization, LocalBusiness, Product, etc.: NOT FOUND / NOT VERIFIABLE.

(b) OpenGraph meta tags
https://www.spotify.se

NOT FOUND / NOT VERIFIABLE.

The page fetch failed with:

“Failed to fetch https://www.spotify.se/: Cache miss”

Therefore the <head> and OpenGraph tags could not be inspected.

https://www.alibaba.com

NOT FOUND / NOT VERIFIABLE.

The accessible source does not expose the complete <head> sufficiently to verify exact:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>
<meta property="og:type" ...>

No exact og:* values can therefore be reported without guessing.

(c) Hreflang tags
https://www.spotify.se

NOT FOUND / NOT VERIFIABLE.

The page could not be fetched, so <link rel="alternate" hreflang="..."> tags cannot be inspected.

https://www.alibaba.com

NOT FOUND / NOT VERIFIABLE in the accessible HTML.

I did not find an exposed:

<link rel="alternate" hreflang="..." href="...">

declaration in the accessible HTML.

The page does contain localization controls and language-related data, including:

“Select your preferred language and currency.”

“You can update the settings at any time.”

and:

"lang":"en_US"

These are not hreflang tags.

(d) AI crawler blocking
https://www.spotify.se

NOT FOUND / NOT VERIFIABLE.

The homepage could not be fetched, and:

https://www.spotify.se/robots.txt

could not be retrieved because the URL was not available as an accessible source.

Therefore no robots.txt or meta crawler directive can be verified.

https://www.alibaba.com

robots.txt: NOT FOUND / NOT VERIFIABLE.

The direct attempt to retrieve:

https://www.alibaba.com/robots.txt

returned an internal retrieval error, so I cannot quote its contents.

HTML meta directives: NOT FOUND / NOT VERIFIABLE.

The accessible homepage source does not expose enough of the <head> to verify:

<meta name="robots" ...>

or AI-specific crawler directives.

Therefore I cannot establish from the accessible source whether Alibaba.com blocks or permits specific AI crawlers.

(e) What language is the HTML declared as?
https://www.spotify.se

NOT FOUND / NOT VERIFIABLE.

The homepage could not be fetched.

https://www.alibaba.com

The accessible page contains the raw application/localization value:

"lang":"en_US"

The visible homepage text is also English:

“Meet Your AI Sourcing Agent”

“Your all-in-one sourcing agent. Research smarter, design faster, source better, and communicate easier.”

“What are you looking for?”

Finding: The accessible Alibaba.com page is configured with the locale value en_US. I did not find evidence in the accessible source establishing a Chinese HTML lang declaration.

Final findings
Audit	Spotify.se	Alibaba.com
JSON-LD/schema.org	NOT FOUND / NOT VERIFIABLE	NOT FOUND / NOT VERIFIABLE
Structured-data types	NOT FOUND / NOT VERIFIABLE	NOT FOUND / NOT VERIFIABLE
OpenGraph tags	NOT FOUND / NOT VERIFIABLE	NOT FOUND / NOT VERIFIABLE
hreflang tags	NOT FOUND / NOT VERIFIABLE	NOT FOUND / NOT VERIFIABLE
AI crawler blocking	NOT VERIFIABLE	NOT VERIFIABLE
HTML language	NOT VERIFIABLE	"lang":"en_US" found
Fetch status	Cache miss	HTML accessible

Important: For Spotify.se, the inability to verify these elements is caused by the page-fetch failure. For Alibaba.com, the findings are limited to what is exposed in the accessible HTML; I did not infer hidden <head> metadata.