# Website Audit Testing Matrix — Complete Prompt Set

**120 Test Cases Across 20 Sites** — 6 Rigorous Probes Per Site

---

## Testing Framework Overview

### Anti-Cheating Constraints (Embedded in All Prompts)
- **"Visit ONLY [exact URL]"** — restricts to target domain
- **"Cite the specific page URL and quote the exact text"** — forces proof of on-site visit
- **"If you cannot find X, state 'NOT FOUND on site'"** — captures gaps instead of hallucinations
- **"Do not use external sources, prior knowledge, or other websites"** — blocks cross-contamination

### Probe Groups
- **Group A (Prompts 1–3):** Discoverability — Can the AI find & cite this site?
- **Group B (Prompts 4–6):** Engagement — Can the AI help users navigate and act?

---

# CATEGORY 1: E-COMMERCE / D2C

## Site 1: Nike.com
**Category:** Major Brand  
**URL:** https://www.nike.com  
**Audit Focus:** Brand recognition, product citations, image-heavy content

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.nike.com. Based solely on what you can read and extract from this site, describe what Nike does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.nike.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details (price ranges for key categories)
(c) Contact information
(d) Key differentiators they claim

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.nike.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find and compare their two cheapest products in footwear. List price, name, and key specs.

Using ONLY https://www.nike.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.nike.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.nike.com only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 2: Allbirds.com
**Category:** Mid-Size D2C  
**URL:** https://www.allbirds.com  
**Audit Focus:** Product variants, review aggregation, sustainability claims

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.allbirds.com. Based solely on what you can read and extract from this site, describe what Allbirds does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.allbirds.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details (price ranges for key product lines)
(c) Contact information
(d) Key differentiators they claim (sustainability, materials, etc.)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.allbirds.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (product, organization, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find and compare their two cheapest products in shoes. List price, name, and key specs (material, color options).

Using ONLY https://www.allbirds.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.allbirds.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.allbirds.com only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 3: Buck Mason
**Category:** Small/Niche Store  
**URL:** https://www.buckmason.com  
**Audit Focus:** Small inventory, brand voice, limited schema

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.buckmason.com. Based solely on what you can read and extract from this site, describe what Buck Mason does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.buckmason.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details
(c) Contact information
(d) Key differentiators they claim

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.buckmason.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find and compare their two cheapest products in apparel. List price, name, and key specs.

Using ONLY https://www.buckmason.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.buckmason.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.buckmason.com only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 4: Vintage Empire (Poorly Optimized)
**Category:** Poorly Optimized E-commerce  
**URL:** https://vintageempire.shop (or similar niche reseller)  
**Audit Focus:** Missing alt text, thin descriptions, broken schema

### Prompt 1 — Direct Brand Recall
Visit ONLY https://vintageempire.shop. Based solely on what you can read and extract from this site, describe what Vintage Empire does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://vintageempire.shop and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details
(c) Contact information
(d) Key differentiators they claim

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://vintageempire.shop and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find and compare their two cheapest products available. List price, name, and key specs.

Using ONLY https://vintageempire.shop, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://vintageempire.shop. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://vintageempire.shop only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

# CATEGORY 2: SAAS / TECH

## Site 5: Notion.so
**Category:** Major / Well-Cited  
**URL:** https://www.notion.so  
**Audit Focus:** Comparison pages, integration citations, use-case clarity

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.notion.so. Based solely on what you can read and extract from this site, describe what Notion does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.notion.so and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details
(c) Contact information
(d) Key differentiators they claim

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.notion.so and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their pricing page, list all plan tiers, and tell me what the free plan includes.

Using ONLY https://www.notion.so, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.notion.so. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.notion.so only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 6: Asana.com
**Category:** Mid-Tier  
**URL:** https://www.asana.com  
**Audit Focus:** Feature depth, comparison surface, pricing transparency

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.asana.com. Based solely on what you can read and extract from this site, describe what Asana does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.asana.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details
(c) Contact information
(d) Key differentiators they claim

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.asana.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their pricing page, list all plan tiers, and tell me what the free plan includes.

Using ONLY https://www.asana.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.asana.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.asana.com only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 7: Linear.app
**Category:** Obscure / New  
**URL:** https://linear.app  
**Audit Focus:** Niche audience, minimal content, technical positioning

### Prompt 1 — Direct Brand Recall
Visit ONLY https://linear.app. Based solely on what you can read and extract from this site, describe what Linear does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://linear.app and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details
(c) Contact information
(d) Key differentiators they claim

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://linear.app and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their pricing page, list all plan tiers, and tell me what the free plan includes.

Using ONLY https://linear.app, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://linear.app. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://linear.app only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 8: Figma.com
**Category:** JS-Heavy SPA  
**URL:** https://www.figma.com  
**Audit Focus:** Dynamic content, client-side rendering, SEO challenges

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.figma.com. Based solely on what you can read and extract from this site, describe what Figma does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.figma.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing or product details
(c) Contact information
(d) Key differentiators they claim

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.figma.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their pricing page, list all plan tiers, and tell me what the free plan includes.

Using ONLY https://www.figma.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.figma.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or updates? What's the latest?
(c) Is the content substantive (detailed text) or thin (mostly images, slogans, or boilerplate)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.figma.com only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (pricing/product/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

# CATEGORY 3: LOCAL BUSINESS / SERVICES

## Site 9: Via Carota (NYC) / Nobu
**Category:** Restaurant  
**URL:** https://www.viacarota.com or https://www.nobumatsuhisa.com  
**Audit Focus:** NAP consistency, reservation CTAs, location schema

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.viacarota.com [or Nobu URL]. Based solely on what you can read and extract from this site, describe what this restaurant does, what services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.viacarota.com and extract the following factual data points from the site only:
(a) Founding year or restaurant age
(b) Pricing information (avg price range)
(c) Contact information (phone, address, email)
(d) Key differentiators they claim (cuisine style, chef, ambiance)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.viacarota.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (LocalBusiness, Restaurant, Event, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their hours, location, and how to book an appointment or reserve a table.

Using ONLY https://www.viacarota.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.viacarota.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there updates, menus, or specials? What's the latest?
(c) Is the content substantive (detailed descriptions, menus) or thin (mostly images)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.viacarota.com only, describe:
(a) Can you understand what this restaurant does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (booking/reservation/contact)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 10: Law Firm / Medical Clinic
**Category:** Legal / Healthcare  
**URL:** Example: Individual law firm site or https://www.bestlawyers.com  
**Audit Focus:** Credentials, testimonials, practice area clarity, license verification

### Prompt 1 — Direct Brand Recall
Visit ONLY [specific law firm/clinic URL]. Based solely on what you can read and extract from this site, describe what this firm does, what services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to [specific law firm/clinic URL] and extract the following factual data points from the site only:
(a) Founding year or firm age
(b) Pricing information (consultation fees, retainers, hourly rates)
(c) Contact information (phone, address, email)
(d) Key differentiators they claim (practice areas, attorney credentials, licenses)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch [specific law firm/clinic URL] and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (LocalBusiness, Organization, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their hours, location, and how to book an appointment or reserve a table.

Using ONLY [specific law firm/clinic URL], help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY [specific law firm/clinic URL]. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there updates, news, or case studies? What's the latest?
(c) Is the content substantive (detailed descriptions, credentials) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of [specific law firm/clinic URL] only, describe:
(a) Can you understand what this firm does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (contact/appointment)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 11: Ace Hotel
**Category:** Hotel / Accommodation  
**URL:** https://www.acehotel.com  
**Audit Focus:** Room photos, location data, booking integration, reviews

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.acehotel.com. Based solely on what you can read and extract from this site, describe what Ace Hotel does, what services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.acehotel.com and extract the following factual data points from the site only:
(a) Founding year or hotel chain age
(b) Pricing information (price ranges for room types)
(c) Contact information (phone, address, email)
(d) Key differentiators they claim (design, locations, amenities)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.acehotel.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (Hotel, LocalBusiness, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their hours, location, and how to book an appointment or reserve a table.

Using ONLY https://www.acehotel.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.acehotel.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there updates, special offers, or events? What's the latest?
(c) Is the content substantive (detailed descriptions, amenities) or thin (mostly images)?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.acehotel.com only, describe:
(a) Can you understand what this hotel does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (booking)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 12: ServiceMaster (Trades/Contractor)
**Category:** Trades / Contractor  
**URL:** https://www.servicemaster.com or local contractor site  
**Audit Focus:** Service area coverage, licensing, before/after content

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.servicemaster.com. Based solely on what you can read and extract from this site, describe what ServiceMaster does, what services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.servicemaster.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Pricing information or service estimates
(c) Contact information (phone, address, service areas)
(d) Key differentiators they claim (certifications, licenses, guarantees)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.servicemaster.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (LocalBusiness, Service, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their hours, location, and how to book an appointment or reserve a table.

Using ONLY https://www.servicemaster.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.servicemaster.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there case studies, before/after galleries, or updates? What's the latest?
(c) Is the content substantive (detailed descriptions, testimonials) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.servicemaster.com only, describe:
(a) Can you understand what this company does within the first screen of content? Quote what tells you.
(b) How many clicks to reach the most important conversion page (contact/booking)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

# CATEGORY 4: MEDIA / CONTENT / BLOG

## Site 13: BBC.com
**Category:** Major News / Media Outlet  
**URL:** https://www.bbc.com  
**Audit Focus:** Recency, byline authority, topic clustering, archive depth

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.bbc.com. Based solely on what you can read and extract from this site, describe what BBC does, what content they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.bbc.com and extract the following factual data points from the site only:
(a) Founding year or organization age
(b) Content categories or sections offered
(c) Contact information (editorial, feedback)
(d) Key differentiators they claim (editorial standards, reach, coverage)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.bbc.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (NewsArticle, Organization, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find the 3 most recent articles. Give me the title, date, and a one-line summary of each.

Using ONLY https://www.bbc.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.bbc.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there updates or breaking news? What's the latest?
(c) Is the content substantive (detailed reporting) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.bbc.com only, describe:
(a) Can you understand what BBC does within the first screen of content? Quote what tells you.
(b) How many clicks to reach important sections (news, features, topics)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper into topics?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 14: LessWrong.com
**Category:** Niche Blog  
**URL:** https://www.lesswrong.com  
**Audit Focus:** Niche audience, author credibility, citation patterns

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.lesswrong.com. Based solely on what you can read and extract from this site, describe what LessWrong does, what content they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.lesswrong.com and extract the following factual data points from the site only:
(a) Founding year or site age
(b) Content focus or topics covered
(c) Contact information or site governance
(d) Key differentiators they claim (community, epistemic standards)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.lesswrong.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find the 3 most recent articles. Give me the title, date, and a one-line summary of each.

Using ONLY https://www.lesswrong.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.lesswrong.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there new posts or updates? What's the latest?
(c) Is the content substantive (detailed analysis, citations) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.lesswrong.com only, describe:
(a) Can you understand what LessWrong does within the first screen of content? Quote what tells you.
(b) How many clicks to reach different content sections or topics?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper into topics?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 15: Outdated / Stale Site
**Category:** Outdated / Stale Content  
**URL:** Example: Older WordPress installation or static site (2010-2015 era)  
**Audit Focus:** Missing freshness signals, broken links, outdated claims

### Prompt 1 — Direct Brand Recall
Visit ONLY [outdated site URL]. Based solely on what you can read and extract from this site, describe what this site does, what content they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to [outdated site URL] and extract the following factual data points from the site only:
(a) Founding year or site age
(b) Content focus or topics
(c) Contact information
(d) Key claims they make

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch [outdated site URL] and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types?
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find the 3 most recent articles. Give me the title, date, and a one-line summary of each.

Using ONLY [outdated site URL], help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY [outdated site URL]. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there updates or recent content? What's the latest?
(c) Is the content substantive or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of [outdated site URL] only, describe:
(a) Can you understand what this site does within the first screen of content? Quote what tells you.
(b) How many clicks to reach different sections?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing, broken, or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 16: TechCrunch
**Category:** Content-Heavy Magazine  
**URL:** https://techcrunch.com  
**Audit Focus:** Volume of content, author attribution, topic depth

### Prompt 1 — Direct Brand Recall
Visit ONLY https://techcrunch.com. Based solely on what you can read and extract from this site, describe what TechCrunch does, what content they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://techcrunch.com and extract the following factual data points from the site only:
(a) Founding year or publication age
(b) Content categories or sections offered
(c) Contact information (editorial, submissions)
(d) Key differentiators they claim (coverage, expertise, reach)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://techcrunch.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (NewsArticle, Organization, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find the 3 most recent articles. Give me the title, date, and a one-line summary of each.

Using ONLY https://techcrunch.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://techcrunch.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there multiple updates per day? What's the latest?
(c) Is the content substantive (detailed reporting, analysis) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://techcrunch.com only, describe:
(a) Can you understand what TechCrunch does within the first screen of content? Quote what tells you.
(b) How many clicks to reach different categories or topics?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper into topics or stories?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

# CATEGORY 5: BRAND / CORPORATE

## Site 17: Apple.com
**Category:** Fortune 500  
**URL:** https://www.apple.com  
**Audit Focus:** Brand consistency, corporate messaging, investor relations links

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.apple.com. Based solely on what you can read and extract from this site, describe what Apple does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.apple.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Product lines or services offered
(c) Contact information or headquarters
(d) Key corporate claims or values

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.apple.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (Organization, Product, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their leadership team, mission statement, and what markets they operate in.

Using ONLY https://www.apple.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.apple.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there news, announcements, or updates? What's the latest?
(c) Is the content substantive (detailed descriptions, corporate info) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.apple.com only, describe:
(a) Can you understand what Apple does within the first screen of content? Quote what tells you.
(b) How many clicks to reach important sections (products, about, careers)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper into products or corporate sections?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 18: Zappos.com
**Category:** Mid-Size Company  
**URL:** https://www.zappos.com  
**Audit Focus:** Company culture, mission clarity, employee spotlights

### Prompt 1 — Direct Brand Recall
Visit ONLY https://www.zappos.com. Based solely on what you can read and extract from this site, describe what Zappos does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://www.zappos.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Product lines or services offered
(c) Contact information or headquarters
(d) Key corporate claims or values (culture, mission)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://www.zappos.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (Organization, Product, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their leadership team, mission statement, and what markets they operate in.

Using ONLY https://www.zappos.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://www.zappos.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, news, or culture updates? What's the latest?
(c) Is the content substantive (detailed descriptions, culture stories) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://www.zappos.com only, describe:
(a) Can you understand what Zappos does within the first screen of content? Quote what tells you.
(b) How many clicks to reach important sections (about, careers, culture)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper into company information?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 19: Buffer.com
**Category:** Startup with Common-Word Name  
**URL:** https://buffer.com  
**Audit Focus:** Disambiguation challenges, brand positioning, resource hub

### Prompt 1 — Direct Brand Recall
Visit ONLY https://buffer.com. Based solely on what you can read and extract from this site, describe what Buffer does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources.

### Prompt 2 — Factual Extraction Under Constraint
Go to https://buffer.com and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Product lines or services offered
(c) Contact information or headquarters
(d) Key differentiators they claim (positioning, approach)

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch https://buffer.com and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (Organization, SoftwareApplication, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Is the main content available in the raw HTML or does it require JavaScript rendering?
(d) Does robots.txt or meta tags block any AI crawlers?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their leadership team, mission statement, and what markets they operate in.

Using ONLY https://buffer.com, help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY https://buffer.com. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there blog posts, updates, or resources? What's the latest?
(c) Is the content substantive (detailed guides, case studies) or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of https://buffer.com only, describe:
(a) Can you understand what Buffer does within the first screen of content? Quote what tells you.
(b) How many clicks to reach important sections (product, about, resources)?
(c) Is there clear navigation? List the main nav items.
(d) Are there internal links guiding you deeper into company information or resources?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Site 20: Non-English Site (Spotify Nordic / Alibaba)
**Category:** Non-English Site  
**URL:** https://www.spotify.se (Swedish) or https://www.alibaba.com (Chinese)  
**Audit Focus:** Language detection, localization, regional NAP, hreflang tags

### Prompt 1 — Direct Brand Recall
Visit ONLY [non-English site URL]. Based solely on what you can read and extract from this site, describe what this brand does, what products/services they offer, and who their target audience is. Cite the specific pages and text passages you extracted this information from. Do not use any external sources or translation tools.

### Prompt 2 — Factual Extraction Under Constraint
Go to [non-English site URL] and extract the following factual data points from the site only:
(a) Founding year or company age
(b) Product lines or services offered
(c) Regional contact information (address, phone for this locale)
(d) Key local claims or positioning

For each fact, quote the exact text and the page URL where you found it. If you cannot find a data point, state 'NOT FOUND on site' and explain what made it unfindable.

### Prompt 3 — Structured Data & Machine Readability
Fetch [non-English site URL] and analyze only its HTML source. Report:
(a) Does it have JSON-LD or schema.org structured data? What types? (Organization, LocalBusiness, etc.)
(b) Are there OpenGraph meta tags? List them.
(c) Are there hreflang tags indicating other language versions?
(d) Does robots.txt or meta tags block any AI crawlers?
(e) What language is the HTML declared as?

Provide the raw evidence for each answer.

### Prompt 4 — Task Completion Test (Category-Specific)
**Task:** Find their leadership team, mission statement, and what markets they operate in.

Using ONLY [non-English site URL], help me complete this task. Walk through the exact pages you visited and what you found on each. If you hit a dead end, describe what blocked you. Do not leave this website.

### Prompt 5 — Content Depth & Freshness
Visit ONLY [non-English site URL]. Assess the content freshness and depth:
(a) What is the most recent date you can find on any page? Where?
(b) Are there updates, news, or regional content? What's the latest?
(c) Is the content substantive or thin?
(d) Can you find any facts that appear outdated or contradictory? Quote your evidence from the site only.

### Prompt 6 — Navigation & Orientation
Starting from the homepage of [non-English site URL] only, describe:
(a) Can you understand what this brand does within the first screen of content? Quote what tells you (in the original language).
(b) How many clicks to reach important sections (about, careers, regional contact)?
(c) Is there clear navigation? List the main nav items (in the original language).
(d) Are there internal links guiding you deeper?
(e) Is there anything confusing or missing that would make a first-time visitor bounce? Evidence from the site only.

---

## Summary Table: All 20 Sites × 6 Prompts

| # | Category | Site | URL | Probe 1 | Probe 2 | Probe 3 | Probe 4 Task | Probe 5 | Probe 6 |
|---|----------|------|-----|---------|---------|---------|--------------|---------|---------|
| 1 | E-com | Nike | nike.com | Brand Recall | Factual Extract | Structured Data | Compare cheapest shoes | Freshness | Navigation |
| 2 | E-com | Allbirds | allbirds.com | Brand Recall | Factual Extract | Structured Data | Compare cheapest shoes | Freshness | Navigation |
| 3 | E-com | Buck Mason | buckmason.com | Brand Recall | Factual Extract | Structured Data | Compare cheapest apparel | Freshness | Navigation |
| 4 | E-com | Vintage Empire | vintageempire.shop | Brand Recall | Factual Extract | Structured Data | Compare cheapest products | Freshness | Navigation |
| 5 | SaaS | Notion | notion.so | Brand Recall | Factual Extract | Structured Data | List pricing tiers & free plan | Freshness | Navigation |
| 6 | SaaS | Asana | asana.com | Brand Recall | Factual Extract | Structured Data | List pricing tiers & free plan | Freshness | Navigation |
| 7 | SaaS | Linear | linear.app | Brand Recall | Factual Extract | Structured Data | List pricing tiers & free plan | Freshness | Navigation |
| 8 | SaaS | Figma | figma.com | Brand Recall | Factual Extract | Structured Data | List pricing tiers & free plan | Freshness | Navigation |
| 9 | Local | Via Carota | viacarota.com | Brand Recall | Factual Extract | Structured Data | Find hours, location, booking | Freshness | Navigation |
| 10 | Local | Law Firm | [firm URL] | Brand Recall | Factual Extract | Structured Data | Find hours, location, booking | Freshness | Navigation |
| 11 | Local | Ace Hotel | acehotel.com | Brand Recall | Factual Extract | Structured Data | Find hours, location, booking | Freshness | Navigation |
| 12 | Local | ServiceMaster | servicemaster.com | Brand Recall | Factual Extract | Structured Data | Find hours, location, booking | Freshness | Navigation |
| 13 | Media | BBC | bbc.com | Brand Recall | Factual Extract | Structured Data | 3 most recent articles | Freshness | Navigation |
| 14 | Media | LessWrong | lesswrong.com | Brand Recall | Factual Extract | Structured Data | 3 most recent articles | Freshness | Navigation |
| 15 | Media | Outdated Site | [URL] | Brand Recall | Factual Extract | Structured Data | 3 most recent articles | Freshness | Navigation |
| 16 | Media | TechCrunch | techcrunch.com | Brand Recall | Factual Extract | Structured Data | 3 most recent articles | Freshness | Navigation |
| 17 | Brand | Apple | apple.com | Brand Recall | Factual Extract | Structured Data | Leadership, mission, markets | Freshness | Navigation |
| 18 | Brand | Zappos | zappos.com | Brand Recall | Factual Extract | Structured Data | Leadership, mission, markets | Freshness | Navigation |
| 19 | Brand | Buffer | buffer.com | Brand Recall | Factual Extract | Structured Data | Leadership, mission, markets | Freshness | Navigation |
| 20 | Brand | Non-English | spotify.se | Brand Recall | Factual Extract | Structured Data | Leadership, mission, markets | Freshness | Navigation |

---

## Running the Test Suite

**Execution Strategy:**
1. **Batch by category** — Test all 4 sites in one category before moving to the next
2. **Parallel probes** — Run all 6 probes per site in sequence (don't skip any)
3. **Log responses** — Capture AI output verbatim; flag hallucinations vs. genuine findings
4. **Score on:**
   - Discoverability: Did it find the site? (Probes 1–3)
   - Engagement: Can it help users navigate? (Probes 4–6)
   - Citation accuracy: Quotes + URLs or just general statements?
   - Freshness detection: Does it catch stale content?
   - Language handling: Can it work in non-English contexts? (Site 20)

**Expected Failure Modes:**
- JS-heavy sites (Figma, Spotify SPA) → Content unavailable in raw HTML
- Small/niche stores → Missing schema, thin content
- Outdated sites → Hallucinations about currency
- Non-English sites → Language detection failures, translation leakage
- Common-word domains (Buffer) → Confusion or cross-contamination

---
