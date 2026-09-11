# Notion - Prompt 3: Structured Data & Machine Readability
**Agent:** PERPLEXITY
**Site:** https://www.notion.so
**Captured:** 2026-09-08T17:16:20.106735

---

(a) JSON-LD / schema.org structured data

NOT FOUND on site — not verifiable from the accessible HTML source.

The HTML document returned for:

https://www.notion.so/

contains substantial page content, but the accessible HTML extraction does not expose any raw:

<script type="application/ld+json">

or:

schema.org

evidence.

Therefore, I cannot verify any JSON-LD/schema.org types from the accessible source.

Raw HTML evidence available: the extracted document begins with navigation and page content such as:

“Product”

“Notion AI”

“Agents”

“AI Meeting Notes”

and:

“Where teams and agents Think together.”

Result: JSON-LD/schema.org type = NOT FOUND on site / not exposed in accessible HTML evidence.

(b) OpenGraph meta tags

NOT FOUND on site — not exposed in the accessible HTML source.

I could not verify any raw tags such as:

<meta property="og:title" ...>
<meta property="og:description" ...>
<meta property="og:image" ...>
<meta property="og:url" ...>
<meta property="og:type" ...>

The accessible HTML extraction contains the page's rendered textual content, but does not expose the <head> metadata needed to list exact OpenGraph values.

Therefore:

OpenGraph field	Evidence
og:title	NOT FOUND on site
og:description	NOT FOUND on site
og:image	NOT FOUND on site
og:url	NOT FOUND on site
og:type	NOT FOUND on site

I will not infer their values from the visible page content.

(c) Is the main content in raw HTML or does it require JavaScript?
Main content is available in the fetched HTML.

The accessible HTML extraction contains substantial textual content directly, including:

“Where teams and agents Think together.”

“Capture context, find answers, and automate tasks with AI built for your team.”

“Keep work moving 24/7.”

“Custom Agents Automate repetitive work for your team.”

“Enterprise Search”

“One search for everything.”

“AI Meeting Notes”

“Perfect notes, every time.”

“Docs”

“Simple and powerful.”

“Knowledge Base”

“One source of truth for teams and agents.”

“Projects”

“Less tracking. More progress.”

The HTML extraction also contains product navigation, links, company information, and footer content, including:

“© 2026 Notion Labs, Inc.”

Result: The main textual content is present in the fetched HTML. The evidence does not establish that JavaScript rendering is required to obtain this main content.

Important URL behavior

The requested URL:

https://www.notion.so/

was returned by the fetch as:

“Redirected to URL: https://www.notion.com/”

I have not used the redirected site's separate pages as evidence for the answers above; the content analyzed is the document returned from the requested URL.

(d) Does robots.txt or meta tags block AI crawlers?
robots.txt

No blanket AI-crawler block is present in the generic rule.

Raw evidence from:

https://www.notion.so/robots.txt

is:

User-agent: *
Allow: /
Disallow: /invite/
Disallow: /*/invite/
Disallow: /templates/search?query=*
Disallow: /*/templates/search?query=*
Disallow: /experiment/*
Disallow: /*/experiment/*
Disallow: /lp/webinars/
Disallow: /lp/webinars/*
Disallow: /_vercel/insights/view
Disallow: /embed/*
Disallow: /*/embed/*

The file specifically blocks these named crawlers:

User-agent: BLEXBot
Disallow: /

User-agent: AhrefsBot
Disallow: /

User-agent: Amazonbot
Disallow: /

User-agent: SemrushBot
Disallow: /

User-agent: dotbot
Disallow: /

Raw finding: There is no user-agent explicitly named GPTBot, ChatGPT-User, ClaudeBot, Google-Extended, PerplexityBot, or another crawler explicitly identified as an AI crawler in the accessible robots.txt.

However, the named Amazonbot is blocked:

User-agent: Amazonbot

Disallow: /

I will not classify additional named crawlers as AI crawlers without evidence from the specified site.

HTML meta-tag blocking

NOT FOUND on site.

The accessible HTML extraction does not expose a raw:

<meta name="robots" ...>

or equivalent crawler-blocking meta tag, so no such HTML-level AI crawler restriction can be verified.

Final raw findings
Check	Finding
JSON-LD	NOT FOUND on site / not exposed in accessible HTML
Schema.org	NOT FOUND on site / not exposed in accessible HTML
OpenGraph	NOT FOUND on site / not exposed in accessible HTML
Main content	Present in fetched HTML
JavaScript required for main text	Not indicated by the accessible evidence
Generic robots rule	User-agent: * → Allow: /
Explicitly blocked named crawlers	BLEXBot, AhrefsBot, Amazonbot, SemrushBot, dotbot
Explicit AI crawler names	NOT FOUND on site
HTML robots meta tag	NOT FOUND on site / not exposed in accessible HTML