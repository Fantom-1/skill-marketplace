# LessWrong - Prompt 3: Structured Data & Machine Readability
**Agent:** PERPLEXITY
**Site:** https://www.lesswrong.com
**Captured:** 2026-09-08T18:41:43.404734

---

HTML-source audit — LessWrong

Target URL: https://www.lesswrong.com/

I inspected only the LessWrong domain. The accessible HTML exposes substantial rendered page text, but the retrieval does not expose the document <head> as raw HTML, so metadata conclusions below are limited to what is directly verifiable.

(a) JSON-LD / schema.org structured data

NOT FOUND on site in the accessible HTML.

I could not verify an exposed:

<script type="application/ld+json">

block or schema.org markup in the accessible HTML representation.

Therefore, the presence of structured-data types such as:

NewsArticle
Article
Organization
WebSite
DiscussionForumPosting

is NOT FOUND on site in the accessible HTML.

Raw evidence

The retrieved page exposes page content beginning with:

“LessWrong”

“This website requires javascript to properly function. Consider activating javascript to get access to all site functionality.”

and then navigation/content such as:

“Home”
“All Posts”
“Concepts”
“Library”

but no JSON-LD block is exposed in the retrieved HTML representation.

Important: This means not found in accessible HTML, not a claim that no structured data exists in every response/rendering layer.

(b) OpenGraph meta tags

NOT FOUND on site in the accessible HTML.

I could not inspect an exposed <head> containing tags such as:

<meta property="og:title" content="...">
<meta property="og:description" content="...">
<meta property="og:image" content="...">
<meta property="og:url" content="...">
<meta property="og:type" content="...">

No exact OpenGraph values can therefore be reported.

The accessible HTML begins with page content rather than exposing the document's complete <head>:

“LessWrong”

“This website requires javascript to properly function. Consider activating javascript to get access to all site functionality.”

Conclusion: OpenGraph tags are NOT FOUND in the accessible HTML.

(c) Is the main content available in raw HTML?

YES — substantial main content is directly accessible.

The homepage HTML contains navigation:

“Home”
“All Posts”
“Concepts”
“Library”
“Best of LessWrong”
“Sequence Highlights”
“Rationality: A-Z”
“The Codex”
“HPMOR”
“Community Events”

It also contains actual post content, including:

“Search versus design”

“How is it that we solve engineering problems? What is the nature of the design process that humans follow when building an air conditioner or computer program?”

and current discussion content such as:

“LLMs are (still) mostly powered by imitative learning, not RL”

with:

“7d”

The page also contains current-looking post timestamps such as:

“20h”

“5h”

“4h”

JavaScript evidence

The page explicitly states:

“This website requires javascript to properly function. Consider activating javascript to get access to all site functionality.”

Therefore:

Primary textual content: available in the accessible HTML.
Full site functionality: explicitly requires JavaScript according to the site's own text.

Conclusion: The main textual content does not require JavaScript merely to be exposed in the retrieved HTML, although the site explicitly says JavaScript is required for proper/full functionality.

(d) robots.txt / meta tags and AI crawlers
robots.txt

NOT FOUND / NOT VERIFIABLE.

I attempted:

URL: https://www.lesswrong.com/robots.txt

The retrieval system returned:

“URL https://www.lesswrong.com/robots.txt is not safe to open (non-retryable error)”

Therefore I cannot extract the actual User-agent, Allow, or Disallow directives from LessWrong's robots.txt.

I will not infer AI-crawler permissions from that failed retrieval.

HTML meta robots

NOT FOUND on site in the accessible HTML.

I could not verify an exposed:

<meta name="robots" content="...">

or an AI-specific meta directive.

No exact GPTBot, ChatGPT-User, or other AI-crawler meta directive was exposed in the accessible HTML.

Final findings
Check	Site-only result
JSON-LD	NOT FOUND in accessible HTML
schema.org types	NOT FOUND in accessible HTML
OpenGraph tags	NOT FOUND in accessible HTML
Main textual content in HTML	YES
JavaScript required for full functionality	YES — explicitly stated by site
robots.txt contents	NOT FOUND / NOT VERIFIABLE
HTML meta[name="robots"]	NOT FOUND in accessible HTML
AI-specific meta directives	NOT FOUND in accessible HTML

Raw site evidence: https://www.lesswrong.com/ explicitly says:

“This website requires javascript to properly function.”

while simultaneously exposing substantial navigation, posts, comments, timestamps, and other textual content in the retrieved HTML.