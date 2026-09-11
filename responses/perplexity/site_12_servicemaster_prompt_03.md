# ServiceMaster - Prompt 3: Structured Data & Machine Readability
**Agent:** PERPLEXITY
**Site:** https://www.servicemaster.com
**Captured:** 2026-09-08T18:37:04.208662

---

HTML-source audit — ServiceMaster

Target URL: https://www.servicemaster.com/

I analyzed only the HTML/content exposed for the specified ServiceMaster domain. I did not use external sites as sources.

(a) JSON-LD / schema.org structured data
Finding

NOT FOUND on site in the accessible HTML.

I did not find an exposed:

<script type="application/ld+json">

block or visible schema.org structured-data markup in the accessible HTML.

I therefore cannot verify any schema types such as:

LocalBusiness
Organization
Service
WebSite
Corporation

as being present in the accessible HTML.

Raw HTML evidence

The accessible page exposes ordinary page content such as:

ServiceMaster Brands

Be There When You Need Us™

ServiceMaster Brands has been a leader in needs-based services businesses for nearly a century.

Founded in 1929...

but no exposed JSON-LD/schema.org block accompanies that content.

Conclusion: JSON-LD/schema.org: NOT FOUND on site in accessible HTML.

(b) OpenGraph meta tags
Finding

NOT FOUND on site in the accessible HTML extraction.

I could not verify exposed values for:

og:title
og:description
og:image
og:url
og:type
og:site_name
Raw evidence

The accessible HTML extraction begins with page content and links:

ServiceMaster Brands

Be There When You Need Us™

Our Brands

and continues directly into the site's content.

No <meta property="og:..."> elements were exposed in the accessible HTML.

Conclusion: OpenGraph tags: NOT FOUND on site in accessible HTML.

This does not establish that such tags are absent from every server response or rendering layer; only that they were not exposed in the accessible HTML I could inspect.

(c) Is the main content in raw HTML or does it require JavaScript?
Finding

The main content is available directly in the accessible HTML.

The page exposes substantial content without requiring client-side rendering to read the primary text.

Raw evidence

The accessible HTML contains:

# Be There When You Need Us™

## Our Brands

ServiceMaster Brands has been a leader in needs-based services businesses for nearly a century.

Founded in 1929, the company is home to over 3,200 franchisees across 4,600+ locations serving over 1,000,000 homes and businesses each year.

It also exposes the brand names:

ServiceMaster Restore®

ServiceMaster Recovery Management®

ServiceMaster Clean®

Merry Maids®

TWO MEN AND A TRUCK®

TWO MEN AND A JUNK TRUCK®

and contact information:

1-888-We-Serve®

One Glenlake Parkway NE, Suite 1400 Atlanta, GA 30328

3400 Belle Chase Way Lansing, MI 48911

414 W Frontier Ln Olathe, KS 66061

All of this is exposed in the fetched HTML representation.

There is also a service input:

How can we serve you today?

ServiceMaster is a family of brands with a wide variety of services.

[Input: Enter service]

Go ‣

The presence of this interactive element does not prevent the surrounding primary content from being available in the HTML.

Conclusion: Main content: available in raw/accessibly fetched HTML; JavaScript rendering is not required to obtain the primary textual content.

(d) robots.txt / meta tags blocking AI crawlers
robots.txt

NOT FOUND / NOT VERIFIABLE.

I attempted to access the exact site URL:

https://www.servicemaster.com/robots.txt

The fetch did not return the contents of robots.txt; it returned an access/safety error instead. Therefore I cannot truthfully report any User-agent, Disallow, Allow, or AI-crawler-specific directives from that file.

Raw fetch result:

URL https://www.servicemaster.com/robots.txt is not safe to open (non-retryable error)

Therefore:

AI-crawler rules in robots.txt: NOT FOUND / NOT VERIFIABLE.

HTML meta robots

NOT FOUND on site in the accessible HTML.

I did not find an exposed:

<meta name="robots" content="...">

or an equivalent AI-crawler-specific meta directive in the accessible HTML.

I therefore cannot verify a restriction specifically targeting:

GPTBot
ChatGPT-User
other AI crawlers

from HTML meta tags.

Important additional site evidence

The ServiceMaster Terms of Use contain a broad restriction on automated access:

URL: https://www.servicemaster.com/terms-of-use/

Exact text:

“You may not use any ‘deep-link’, ‘page-scrape’, ‘robot’, ‘spider’ or other automatic device, program, algorithm or methodology, or any similar or equivalent manual process, to access, acquire, copy or monitor any portion of this website or any of its content...”

This is not an HTML meta tag or robots.txt directive, and it does not specifically name AI crawlers. It is nevertheless an explicit site-level contractual restriction on automated access.

Final findings
Check	Result
JSON-LD	NOT FOUND on site in accessible HTML
schema.org types	NOT FOUND on site in accessible HTML
OpenGraph tags	NOT FOUND on site in accessible HTML
Main content in raw HTML	YES
JS required for primary text?	NO — primary content is directly exposed
robots.txt contents	NOT FOUND / NOT VERIFIABLE
HTML meta[name="robots"]	NOT FOUND on site
AI-specific crawler meta directives	NOT FOUND on site
Explicit automated-access restriction elsewhere on site	YES — Terms of Use explicitly mention “robot”, “spider”, “page-scrape”, etc.