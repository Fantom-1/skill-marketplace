# Nike - Prompt 3: Structured Data & Machine Readability
**Agent:** GEMINI
**Site:** https://www.nike.com
**Captured:** 2026-09-08T19:05:05.757719

---

(a) Does it have JSON-LD or schema.org structured data? What types?
Finding: NOT FOUND on site via the accessible HTML payload for [https://www.nike.com](https://www.nike.com).

Raw Evidence / Explanation: A direct inspection of the homepage markup reveals no script tags containing application/ld+json or inline itemscope/itemtype microdata attributes in the retrievable DOM. Any structured data schemas on Nike.com (such as Organization or WebSite) are not exposed in the server-delivered static HTML blocks retrieved for this URL.

(b) Are there OpenGraph meta tags? List them.
Finding: NOT FOUND on site in the accessible page output for [https://www.nike.com](https://www.nike.com).

Raw Evidence / Explanation: No <meta property="og:..."> tags (e.g., og:title, og:description, og:image, og:url) are present or visible in the accessible HTML document body/head returned during extraction. The primary page metadata extracted consists of the standard HTML title:

"Nike. Just Do It. Nike.com"

(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
Finding: Available in the raw HTML (Server-Side Rendered / Pre-rendered).

Raw Evidence: The full text hierarchy, navigation trees, campaign headings, product taxonomy, and legal notices are delivered directly as accessible text inside the DOM without requiring client-side JS hydration to be parsed. Exact extracted passages include:

Navigation links and categories:

"Men", "Women", "Kids", "Jordan", "NikeSKIMS", "Sport"

Promotional copy and product headers:

"SHOW THEM WHERE YOU STAND. Division lines, drawn. The 2026 Rivalries Collection is touching down."
"The Wait is Over. After two decades, the Air Jordan \"Tour Yellow\" returns."
"HARD IN THE PAINT. Gear up for NYC's biggest tennis showdown in the hoops-inspired Slam City Collection."
"PEGASUS PLUS 2. Power tempo training for race day. A stacked ZoomX foam midsole and exposed Air Zoom unit deliver 18% more energy return."

Footer copyright and links:

"© 2026 Nike, Inc. All Rights Reserved"
"Guides", "Nike Air", "Nike Air Force 1", "Nike Air Max"

(d) Does robots.txt or meta tags block any AI crawlers?
Finding for meta tags: NOT FOUND on site. There are no visible robots or googlebot meta tags (such as <meta name="robots" content="noindex, nofollow">) blocking crawlers on [https://www.nike.com](https://www.nike.com).

Finding for robots.txt ([https://www.nike.com/robots.txt](https://www.nike.com/robots.txt)): YES, AI crawlers are explicitly blocked.

Raw Evidence: Attempting to retrieve [https://www.nike.com/robots.txt](https://www.nike.com/robots.txt) returned an opt-out status:

URL_FETCH_STATUS_GOOGLE_EXTENDED_OPT_OUT

This status confirms that Nike's server directives via robots.txt block the Google-Extended user-agent (and related autonomous AI crawlers/data collectors) from crawling and indexing the domain.