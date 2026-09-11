# Buffer - Prompt 3: Structured Data & Machine Readability
**Agent:** CHATGPT
**Site:** https://buffer.com
**Captured:** 2026-09-08T18:55:57.932383

---

Buffer — HTML-source audit

Only these URLs were inspected:

https://buffer.com/
https://buffer.com/robots.txt

No external website was used.

(a) JSON-LD / schema.org structured data

Result: NOT FOUND on site in the accessible HTML source.

I could not verify an exposed JSON-LD block or schema.org declaration in the HTML representation of https://buffer.com/.

The accessible source begins directly with page content such as:

Features
CreateBuild your own library of content ideas
PublishPlan and schedule your content across social media platforms
InsightsNewUnderstand your performance and what to post next
CommunityEasily engage with your community
CollaborateWork together seamlessly, from planning to publishing

and:

## Your social media workspace

Connected to every platform and tool you use.

Exact structured-data types:

Type	Finding
Organization	NOT FOUND / NOT VERIFIABLE
SoftwareApplication	NOT FOUND / NOT VERIFIABLE
WebSite	NOT FOUND / NOT VERIFIABLE
Product	NOT FOUND / NOT VERIFIABLE
JSON-LD	NOT FOUND / NOT VERIFIABLE
schema.org	NOT FOUND / NOT VERIFIABLE

I will not infer structured data from the visible content.

(b) OpenGraph meta tags

Result: NOT FOUND / NOT VERIFIABLE in the accessible HTML source.

The accessible representation does not expose the complete <head> containing the raw <meta> elements. Therefore I cannot directly verify exact values for:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>
<meta property="og:type" ...>
Exact values
OpenGraph tag	Finding
og:title	NOT FOUND / NOT VERIFIABLE
og:description	NOT FOUND / NOT VERIFIABLE
og:image	NOT FOUND / NOT VERIFIABLE
og:url	NOT FOUND / NOT VERIFIABLE
og:type	NOT FOUND / NOT VERIFIABLE

This means the tags cannot be verified from the accessible HTML representation; it does not establish that Buffer definitively has no OpenGraph tags.

(c) Is the main content available in raw HTML?

YES.

Substantial homepage content is directly present in the fetched HTML.

Raw evidence — main description
## Your social media workspace

Connected to every platform and tool you use.

Raw evidence — product features
### Publish

Schedule your content to the most popular platforms including Facebook, Instagram, TikTok, LinkedIn, Threads, Bluesky, YouTube Shorts, Pinterest, Google Business, Mastodon and X.
### Create

Whether you’re flying solo or working with a team, Buffer has all the features to help you create, organize, and repurpose your content for any channel. There’s also an AI Assistant if you need it.
### Community

Engage with your audience across all your channels at 10x speed. Buffer will help you triage and respond to comments from one simple dashboard.
### Insights

Whether it’s basic analytics or in-depth reporting, Buffer will help you learn what works and how to improve.

Raw evidence — corporate information

The HTML also directly contains:

## About us

We are an open company

Since 2013, we’ve shared Buffer’s finances, team salaries, and other key metrics openly.

It exposes current metrics directly:

MAU Monthly active users
239,753

Total customers Total customers
79,318

Teammates Across 15 countries
73

ARR Annual recurring revenue
$25.9M

Determination: The main textual content is available in the fetched HTML. The evidence does not require JavaScript rendering to expose these portions of the page.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

URL: https://buffer.com/robots.txt

The file is directly accessible.

Raw contents:

User-agent: *
Disallow: /add
Disallow: /ajax
Disallow: /button
Disallow: /docs-custom-code.js
Disallow: /docs-footer
Disallow: /free-trial
Disallow: /pricing-calculator

There is also a specific crawler rule:

User-agent: bitlybot
Disallow: /

AI-specific crawler rules

I found no explicitly named AI crawler in the retrieved robots.txt.

Specifically, there are no entries shown for:

GPTBot
OAI-SearchBot
ChatGPT-User
ClaudeBot
PerplexityBot
Google-Extended

The generic rule is:

User-agent: *

with restrictions only on the listed paths.

Finding: No AI-specific crawler block was found in the retrieved robots.txt.

Meta crawler directives

NOT FOUND / NOT VERIFIABLE.

The accessible HTML does not expose enough of the <head> to verify a raw:

<meta name="robots" ...>

or an AI-specific crawler meta directive.

Final findings
Audit item	Result
JSON-LD	NOT FOUND / NOT VERIFIABLE
schema.org	NOT FOUND / NOT VERIFIABLE
Organization / SoftwareApplication / Product types	NOT FOUND / NOT VERIFIABLE
OpenGraph tags	NOT FOUND / NOT VERIFIABLE
Main content in raw HTML	YES
robots.txt accessible	YES
Generic crawler restrictions	YES — specific paths
AI-specific crawler rule	NOT FOUND
AI-specific meta directive	NOT FOUND / NOT VERIFIABLE