# Nike - Prompt 3: Structured Data & Machine Readability
**Agent:** PERPLEXITY
**Site:** https://www.nike.com
**Captured:** 2026-09-08T19:10:24.142793

---

(a) JSON-LD / schema.org structured data
NOT FOUND in the accessible extraction.

Requested URL: https://www.nike.com/

The accessible extracted content begins with:

“Pure pace. Zero mercy. Blow past defenders in the Vapor Pro 'CeeDee Lamb,' engineered with an ultra-light plate for raw speed.”

No raw HTML source, <script type="application/ld+json">, schema.org, @context, or @type values were returned by the available page extraction.

Why unfindable: the returned representation exposes extracted page text, not the document’s raw <head> / <script> HTML. Therefore, no JSON-LD or schema.org type can be verified from the directly extracted source representation.

(b) OpenGraph meta tags
NOT FOUND in the accessible extraction.

Requested URL: https://www.nike.com/

The page title returned was:

“Nike. Just Do It”

No raw <meta> elements were returned, including no strings matching:

xml
<meta property="og:...">
or:

xml
<meta name="og:...">
Why unfindable: the accessible result contains extracted visible text and a title, but no raw HTML <head> markup. Accordingly, no OpenGraph tag names or exact content attribute values can be listed without guessing.

(c) Raw HTML content versus JavaScript rendering
NOT FOUND as a definitive raw-HTML determination.

Requested URL: https://www.nike.com/

Visible content was returned, including:

“Pure pace. Zero mercy. Blow past defenders in the Vapor Pro 'CeeDee Lamb,' engineered with an ultra-light plate for raw speed.”

“Classic silhouettes and cutting-edge innovation to build your game from the ground up.”

The fetched /launch URL produced references to site resources rather than launch-page content:

“The webpage at https://www.nike.com/static/uxf/guest-session-html/index.html might be temporarily down or it may have moved permanently to a new web address.”

“The webpage at https://www.nike.com/149e9513-01fa-4fb0-aad4-566afd725d1b/2d206a39-8ed7-437e-a3be-862e0f06eea3/fp?x-kpsdk-v=j-1.2.728 might be temporarily down or it may have moved permanently to a new web address.”

Why unfindable: no literal HTML source was returned, so it is not possible to verify whether the homepage’s visible content was present in the initial server response or added after JavaScript execution. The extracted text alone does not establish either condition.

(d) AI-crawler blocking in robots.txt or meta tags
robots.txt
No AI-crawler-specific user-agent block was found in the extracted robots.txt.

URL: https://www.nike.com/robots.txt

Exact opening text:

text
# www.nike.com robots.txt -- just crawl it.


Exact general crawler block:

text
User-agent: *

Disallow: */member/inbox
Disallow: */member/settings
Disallow: */p/
Disallow: */checkout/
Disallow: /*.swf$
Disallow: /*.pdf$
Disallow: /pdf/
Disallow: /ar/help/
Disallow: /br/help/
Disallow: /hk/help/
Disallow: /uy/help/
Disallow: /xf/help/
Disallow: /xl/help/
Disallow: /xm/help/
Disallow: /fragments/recommendations-carousel
Disallow: /kr/en$
Disallow: /kr/en/
Disallow: */w/*-*z*z*z*z*z


The crawler-specific user-agent names returned were:

text
User-agent: Baiduspider
User-agent: HaoSouSpider
User-agent: Sogou web spider
User-agent: Sogou inst spider
User-agent: Sogou spider2


Each of those named blocks includes:

text
Disallow: /


Exact finding: In the extracted robots.txt, the strings GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, PerplexityBot, Google-Extended, CCBot, and Bytespider were NOT FOUND. The file’s wildcard rule does disallow the specific paths quoted above for User-agent: *.

Meta robots / AI meta tags
NOT FOUND in the accessible extraction.

URL checked: https://www.nike.com/

No raw meta-tag HTML was supplied in the extraction; therefore, none of the following could be verified:

xml
<meta name="robots" ...>
<meta name="googlebot" ...>
<meta name="noai" ...>
<meta name="noimageai" ...>
Why unfindable: the available source representation contains no raw <meta> markup.