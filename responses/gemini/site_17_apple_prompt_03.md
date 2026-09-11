# Apple - Prompt 3: Structured Data & Machine Readability
**Agent:** GEMINI
**Site:** https://www.apple.com
**Captured:** 2026-09-08T18:50:10.208952

---

Apple HTML-source audit

Only the following Apple URLs were inspected:

https://www.apple.com/
https://www.apple.com/robots.txt

The accessible HTML representation does not expose the complete <head>, so where a raw tag cannot be directly verified, I mark it NOT FOUND / NOT VERIFIABLE rather than assuming absence.

(a) JSON-LD / schema.org structured data

Result: NOT FOUND in the accessible HTML.

I searched the accessible HTML for:

<script type="application/ld+json">

and:

schema.org

No matching text was returned.

Raw evidence

Search for application/ld+json:

“No matching text found for "application/ld+json"”

Search for schema.org:

“No matching text found for "schema.org"”

Types such as Organization, Product, WebSite, etc.: NOT FOUND / NOT VERIFIABLE in the accessible HTML.

(b) OpenGraph meta tags

Result: NOT FOUND / NOT VERIFIABLE in the accessible HTML.

I searched for:

<meta property="og:title" ...>

The accessible HTML returned no og:title match.

Raw evidence

“No matching text found for "og:title"”

I therefore cannot provide exact values for:

og:title
og:description
og:image
og:url
og:type

because the accessible representation does not expose them.

Important: this does not establish that Apple has no OpenGraph tags. It establishes only that they are not directly verifiable in the accessible HTML source provided for inspection.

(c) Is the main content in raw HTML?

YES — substantial main content is directly available in the fetched HTML.

The Apple homepage source exposes navigation, headings, product descriptions, promotional text and links without requiring me to infer them from rendered screenshots.

Raw evidence
Store
Mac
iPad
iPhone
Watch
Vision
AirPods
TV & Home
Entertainment
Accessories
Support

Then:

## iPhone

Meet the latest iPhone lineup.

And:

## MacBook Air

Now supercharged by M5.

And:

### MacBook Pro

Now with M5, M5 Pro, and M5 Max.

And:

## iPad Pro

Advanced AI performance and game-changing capabilities.

The source also contains:

## Endless entertainment.

followed by Apple TV, Apple Music, Apple Fitness and App Store content.

Determination

Main textual content: available in raw HTML.

This does not establish that every interactive component is implemented without JavaScript; only that substantial page content is already present in the fetched HTML.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL: https://www.apple.com/robots.txt

The file is directly accessible and contains these rules:

# robots.txt for https://www.apple.com/

User-agent: *
Disallow: /*shop/browse/overlay/*
Disallow: /*shop/iphone/payments/overlay/*
Disallow: /cn/*/aow/*
Disallow: /tmall*
Allow: /ac/globalnav/2.0/*/images/ac-globalnav/globalnav/search/*

There are also crawler-specific rules:

User-agent: Baiduspider
Disallow: /*
Allow: /cn/*
Allow: /cn-edu/*
Allow: /cn-k12/*
User-agent: HaoSouSpider
Disallow: /*
Allow: /cn/*
Allow: /cn-edu/*
Allow: /cn-k12/*
User-agent: Sogou web spider
Disallow: /*
Allow: /cn/*
Allow: /cn-k12/*
User-agent: Sogou inst spider
Disallow: /*
Allow: /cn/*
Allow: /cn-k12/*

AI-specific crawlers

In the retrieved robots.txt, I found no named entries for:

GPTBot
OAI-SearchBot
ChatGPT-User
ClaudeBot
PerplexityBot
Google-Extended

The relevant generic rule is:

User-agent: *
Disallow: /*shop/browse/overlay/*
Disallow: /*shop/iphone/payments/overlay/*
Disallow: /cn/*/aow/*
Disallow: /tmall*

Therefore, from the site's actual robots.txt: I found no AI-specific crawler block. The generic User-agent: * rules shown above block only the listed URL patterns, not the entire site.

Meta tags

AI-specific meta crawler directives: NOT FOUND / NOT VERIFIABLE.

The accessible HTML does not expose the complete <head>, and searches for crawler-related robots content in the accessible body/source representation produced no match.

Final findings
Check	Finding
JSON-LD	NOT FOUND in accessible HTML
schema.org	NOT FOUND in accessible HTML
Structured-data types	NOT FOUND / NOT VERIFIABLE
OpenGraph	NOT FOUND / NOT VERIFIABLE
Main content	YES — substantial content directly in HTML
robots.txt	Accessible
AI-specific robots.txt rules	None found
Generic robots.txt restrictions	Yes, limited URL patterns
AI-specific meta directives	NOT FOUND / NOT VERIFIABLE