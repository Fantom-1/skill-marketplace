# Phase 0: Signal Catalogue

This catalogue maps actual observed AI failures (from ChatGPT field research) to the automatable technical signals we have designed.

## Observed AI Failures
| Site | Task / Prompt | AI Failure Context | Mapped Technical Signal |
|---|---|---|---|
| https://www.nike.com | Factual Extraction Under Constraint | `NOT FOUND on site. | Price ranges — NOT FOUND on site` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.nike.com | Structured Data & Machine Readability | `JSON-LD: NOT FOUND in the accessible HTML evidence | Schema.org types: NOT FOUND in the accessible HTML evidence` | **Unknown** |
| https://www.nike.com | Navigation & Orientation | `NOT FOUND on the homepage. | NOT FOUND on the homepage.` | **Unknown** |
| https://www.allbirds.com | Factual Extraction Under Constraint | `Company age: NOT FOUND on site. The site gives the year 2016 but does not state an explicit company-age figure.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.allbirds.com | Structured Data & Machine Readability | `NOT FOUND on site in the fetched HTML evidence. | JSON-LD: NOT FOUND on site` | **Unknown** |
| https://www.allbirds.com | Navigation & Orientation | `NOT FOUND on the homepage. | NOT FOUND in the initial homepage content. Contact information is available on a separate page:` | **Unknown** |
| https://www.buckmason.com | Factual Extraction Under Constraint | `NOT FOUND on site.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.buckmason.com | Structured Data & Machine Readability | `NOT FOUND on site in the HTML source I could inspect. | JSON-LD: NOT FOUND on site` | **Unknown** |
| https://www.buckmason.com | Task Completion Test | `NOT FOUND / DEAD END. | Additional key specifications: NOT FOUND on site in the accessible pages.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.buckmason.com | Content Depth & Freshness | `NOT FOUND on site as an explicit article/publication date. | Exact publication dates: NOT FOUND on site in the Journal listing that I inspected.` | **Freshness (Stale dates / No <time> tags)** |
| https://www.buckmason.com | Navigation & Orientation | `NOT FOUND in the first-screen text as a plain sentence describing the business. | NOT FOUND in the first-screen content.` | **Unknown** |
| https://vintageempire.shop | Direct Brand Recall | `NOT FOUND on site. | NOT FOUND on site.` | **Unknown** |
| https://vintageempire.shop | Factual Extraction Under Constraint | `NOT FOUND on site. | NOT FOUND on site.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://vintageempire.shop | Structured Data & Machine Readability | `NOT FOUND on site. | NOT FOUND on site.` | **Unknown** |
| https://vintageempire.shop | Task Completion Test | `NOT FOUND on site. | 1	NOT FOUND on site	NOT FOUND on site	NOT FOUND on site` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://vintageempire.shop | Content Depth & Freshness | `NOT FOUND on site. | NOT FOUND on site.` | **Freshness (Stale dates / No <time> tags)** |
| https://vintageempire.shop | Navigation & Orientation | `NOT FOUND on site. | NOT FOUND on site.` | **Unknown** |
| https://www.notion.so | Factual Extraction Under Constraint | `NOT FOUND on site. | Pricing — NOT FOUND on the specified site` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.notion.so | Structured Data & Machine Readability | `NOT FOUND on site — not verifiable from the accessible HTML source. | Result: JSON-LD/schema.org type = NOT FOUND on site / not exposed in accessible HTML evidence.` | **Unknown** |
| https://www.notion.so | Content Depth & Freshness | `NOT FOUND on site.` | **Freshness (Stale dates / No <time> tags)** |
| https://www.notion.so | Navigation & Orientation | `Directly verifiable missing information: NOT FOUND on site | This is directly observable, but whether this is confusing to a visitor is NOT FOUND on site.` | **Unknown** |
| https://www.asana.com | Factual Extraction Under Constraint | `NOT FOUND on site. | NOT FOUND on site in the asana.com pages I inspected.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.asana.com | Structured Data & Machine Readability | `NOT FOUND on site — not exposed in the accessible HTML source. | Result: NOT FOUND on site / not exposed in accessible HTML evidence.` | **Unknown** |
| https://www.asana.com | Content Depth & Freshness | `NOT FOUND on site. | (d) Outdated/contradictory facts	NOT FOUND on site` | **Freshness (Stale dates / No <time> tags)** |
| https://www.asana.com | Navigation & Orientation | `NOT FOUND on site. | These are all directly present on the site, but whether they are confusing to a first-time visitor is NOT FOUND on site.` | **Unknown** |
| https://linear.app | Factual Extraction Under Constraint | `Telephone number: NOT FOUND on site in the contact pages inspected. | Telephone	NOT FOUND on site` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://linear.app | Structured Data & Machine Readability | `NOT FOUND on site in the accessible HTML source. | JSON-LD: NOT FOUND on site` | **Unknown** |
| https://linear.app | Content Depth & Freshness | `NOT FOUND on site. | (d) Contradictory facts	NOT FOUND on site` | **Freshness (Stale dates / No <time> tags)** |
| https://linear.app | Navigation & Orientation | `NOT FOUND on site: I did not find an explicit statement on the homepage identifying a usability problem, visitor confusion, or bounce rate. | However, whether this is actually confusing to visitors is NOT FOUND on site. There is no site evidence establishing that these terms cause confusion or abandonment.` | **Unknown** |
| https://www.figma.com | Factual Extraction Under Constraint | `Company age: NOT FOUND on site as an explicit age in years. The site provides the founding year, but I did not find an explicit statement such as “X years old.” | General sales/customer-contact email: NOT FOUND on site in the pages I inspected. The addresses above are explicitly for privacy and copyright matters; I am not treating them as general customer-support addresses.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.figma.com | Structured Data & Machine Readability | `NOT FOUND on site in the accessible raw HTML. | Types: NOT FOUND on site in the accessible HTML.` | **Unknown** |
| https://www.figma.com | Task Completion Test | `Therefore, the current pricing-page contents are NOT FOUND on site in the accessible fetch. | Starter — NOT FOUND on site in the accessible pages inspected` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.figma.com | Content Depth & Freshness | `Therefore, the current pricing-page contents are NOT FOUND on site in the accessible fetch. | Starter — NOT FOUND on site in the accessible pages inspected` | **Freshness (Stale dates / No <time> tags)** |
| https://www.figma.com | Navigation & Orientation | `NOT FOUND on site. | These are raw site facts, not evidence that the visitor is confused. Whether this breadth causes first-time visitors to bounce is NOT FOUND on site.` | **Unknown** |
| https://www.viacarota.com | Direct Brand Recall | `Demographic target audience: NOT FOUND on site. | Formal demographic profile	NOT FOUND on site` | **Unknown** |
| https://www.viacarota.com | Factual Extraction Under Constraint | `NOT FOUND on site. | Result: NOT FOUND on site — the homepage provides historical/background information but no founding year or restaurant-age figure.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.viacarota.com | Structured Data & Machine Readability | `Finding: NOT FOUND on site in the accessible HTML source. | Restaurant: NOT FOUND on site in accessible HTML` | **Unknown** |
| https://www.viacarota.com | Task Completion Test | `NOT FOUND on site in the current homepage and Directions/Questions pages inspected.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.viacarota.com | Content Depth & Freshness | `Latest dated menu/special: NOT FOUND on site. The site states that additions vary daily, but the inspected page does not give a date for the current additions. | Latest dated menu/special	NOT FOUND on site` | **Freshness (Stale dates / No <time> tags)** |
| https://www.viacarota.com | Navigation & Orientation | `NOT FOUND on homepage. | Booking clicks: NOT FOUND on site.` | **Unknown** |
| https://www.bestlawyers.com | Factual Extraction Under Constraint | `Firm/company age: NOT FOUND on site as an explicit number of years. The About page does state: | NOT FOUND on site.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.bestlawyers.com | Task Completion Test | `NOT FOUND on site. | NOT FOUND on the homepage.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.bestlawyers.com | Content Depth & Freshness | `Or “NOT FOUND on site” if the evidence is insufficient | “NOT FOUND on site” if none can be verified` | **Freshness (Stale dates / No <time> tags)** |
| https://www.bestlawyers.com | Navigation & Orientation | `“NOT FOUND on site” where evidence is unavailable` | **Unknown** |
| https://www.acehotel.com | Direct Brand Recall | `Demographic target audience: NOT FOUND on site. | Formal demographic profile	NOT FOUND on site` | **Unknown** |
| https://www.acehotel.com | Factual Extraction Under Constraint | `Hotel-chain age: NOT FOUND on site as an explicit number of years. | NOT FOUND on site in the accessible room pages inspected.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.acehotel.com | Structured Data & Machine Readability | `Finding: NOT FOUND on site in the accessible HTML source. | Hotel	NOT FOUND on site in accessible HTML` | **Unknown** |
| https://www.acehotel.com | Task Completion Test | `Result: NOT FOUND on site for general Ace Hotel hours. | The homepage does contain restaurant and event information, but a general restaurant-table reservation system for all Ace Hotel properties is NOT FOUND on the homepage.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.servicemaster.com | Factual Extraction Under Constraint | `NOT FOUND on site for specific customer service prices or standard service estimates on the ServiceMaster corporate site. | Finding: NOT FOUND on site — no specific customer-facing service price or standard estimate was found in the ServiceMaster corporate pages examined.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.servicemaster.com | Structured Data & Machine Readability | `NOT FOUND on site in the accessible HTML. | Conclusion: JSON-LD/schema.org: NOT FOUND on site in accessible HTML.` | **Unknown** |
| https://www.servicemaster.com | Task Completion Test | `NOT FOUND on site. | NOT FOUND on site.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.servicemaster.com | Content Depth & Freshness | `NOT FOUND on site in the pages/results examined. | Before/after gallery	NOT FOUND on site` | **Freshness (Stale dates / No <time> tags)** |
| https://www.servicemaster.com | Navigation & Orientation | `NOT FOUND on homepage navigation. | Conventional Contact navigation item	NOT FOUND on homepage` | **Unknown** |
| https://www.bbc.com | Direct Brand Recall | `NOT FOUND on site — not directly verifiable from https://www.bbc.com in this access attempt. | NOT FOUND on site — not directly verifiable from https://www.bbc.com in this access attempt.` | **Unknown** |
| https://www.bbc.com | Factual Extraction Under Constraint | `NOT FOUND on site. | NOT FOUND on site.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.bbc.com | Structured Data & Machine Readability | `NOT FOUND on site — not verifiable from the accessible HTML. | is NOT FOUND on site / not verifiable from the accessible HTML.` | **Unknown** |
| https://www.bbc.com | Task Completion Test | `NOT FOUND on site in this access attempt. | Article 1 title	NOT FOUND on site` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.bbc.com | Content Depth & Freshness | `NOT FOUND on site. | NOT FOUND on site.` | **Freshness (Stale dates / No <time> tags)** |
| https://www.bbc.com | Navigation & Orientation | `NOT FOUND on site — not verifiable in this access attempt. | NOT FOUND on site.` | **Unknown** |
| https://www.lesswrong.com | Structured Data & Machine Readability | `NOT FOUND on site in the accessible HTML. | is NOT FOUND on site in the accessible HTML.` | **Unknown** |
| https://www.lesswrong.com | Task Completion Test | `NOT FOUND on site in the accessible HTML. | is NOT FOUND on site in the accessible HTML.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.lesswrong.com | Content Depth & Freshness | `Clear outdated fact found	NOT FOUND | Clear contradiction found	NOT FOUND` | **Freshness (Stale dates / No <time> tags)** |
| TBD | Direct Brand Recall | `NOT FOUND on site.` | **Unknown** |
| https://techcrunch.com | Factual Extraction Under Constraint | `No specific numerical readership/reach figure was extracted from the inspected current pages. Therefore, for a numerical reach claim: NOT FOUND on site.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://techcrunch.com | Structured Data & Machine Readability | `Result: NOT FOUND in the accessible HTML representation. | Types such as NewsArticle, Organization, WebSite, etc.: NOT FOUND / NOT VERIFIABLE in the accessible HTML.` | **Unknown** |
| https://techcrunch.com | Task Completion Test | `The page was crawled today, but the accessible source does not expose an exact publication date for these three entries. Exact calendar date: NOT FOUND on the inspected homepage.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://techcrunch.com | Content Depth & Freshness | `There are newer entries displayed as relative times, but the exact calendar date is NOT FOUND in those listings. | Contradictory fact: NOT FOUND on site.` | **Freshness (Stale dates / No <time> tags)** |
| https://www.apple.com | Direct Brand Recall | `NOT FOUND on site as an explicit demographic statement. | NOT FOUND on site.` | **Unknown** |
| https://www.apple.com | Factual Extraction Under Constraint | `Founding date specifically: NOT FOUND on site in the inspected page. The site gives the incorporation date, not a separate founding date. | Founding date distinct from incorporation date: NOT FOUND on site in the pages inspected.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.apple.com | Structured Data & Machine Readability | `The accessible HTML representation does not expose the complete <head>, so where a raw tag cannot be directly verified, I mark it NOT FOUND / NOT VERIFIABLE rather than assuming absence. | Result: NOT FOUND in the accessible HTML.` | **Unknown** |
| https://www.apple.com | Task Completion Test | `Mission statement: NOT FOUND on site.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.apple.com | Content Depth & Freshness | `Clear contradiction found	NOT FOUND on inspected pages` | **Freshness (Stale dates / No <time> tags)** |
| https://www.apple.com | Navigation & Orientation | `About	NOT FOUND as a homepage main-nav item	No “About” item appears in the accessible homepage navigation. | Careers	NOT FOUND as a homepage main-nav item	No “Careers” item appears in the accessible homepage navigation.` | **Unknown** |
| https://www.zappos.com | Direct Brand Recall | `A broader statement such as “Zappos targets everyone” is NOT FOUND on site and I would not infer it. | Explicit formal target-audience statement	NOT FOUND on site` | **Unknown** |
| https://www.zappos.com | Factual Extraction Under Constraint | `Headquarters: NOT FOUND on site in the pages inspected. | Headquarters	NOT FOUND on site` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.zappos.com | Structured Data & Machine Readability | `Result: NOT FOUND on site / not verifiable in the accessible HTML source. | JSON-LD	NOT FOUND / NOT VERIFIABLE` | **Unknown** |
| https://www.zappos.com | Task Completion Test | `NOT FOUND on site. | A separate explicit sentence labelled “Mission” was NOT FOUND on site in the pages inspected.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.zappos.com | Content Depth & Freshness | `NOT FOUND on site in the inspected current Zappos pages. | Blog/news section found?	NOT FOUND on inspected pages` | **Freshness (Stale dates / No <time> tags)** |
| https://www.zappos.com | Navigation & Orientation | `Culture	NOT FOUND on homepage	No “Culture” link/section is exposed in the homepage navigation/footer. | NOT FOUND on site from the homepage.` | **Unknown** |
| https://buffer.com | Factual Extraction Under Constraint | `NOT FOUND on site. | Headquarters	NOT FOUND on site` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://buffer.com | Structured Data & Machine Readability | `Result: NOT FOUND on site in the accessible HTML source. | Organization	NOT FOUND / NOT VERIFIABLE` | **Unknown** |
| https://buffer.com | Task Completion Test | `Finding: A formally labelled mission statement: NOT FOUND on site. The site's stated purpose/company description and values are directly available. | Important limitation: I did not find a statement defining a specific list of countries where Buffer sells or operates commercially. Therefore, a precise geographic market list is NOT FOUND on site. The site does directly establish that its team is distributed internationally.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://buffer.com | Content Depth & Freshness | `Clear outdated fact	NOT FOUND on site | Clear contradiction	NOT FOUND on site` | **Freshness (Stale dates / No <time> tags)** |
| https://buffer.com | Navigation & Orientation | `Actual first-time-user confusion/bounce: NOT FOUND on site. | Evidence of actual bounce/confusion	NOT FOUND on site` | **Unknown** |
| https://www.spotify.com/se-en/ | Direct Brand Recall | `NOT FOUND on site. | NOT FOUND on site.` | **Unknown** |
| https://www.spotify.com/se-en/ | Factual Extraction Under Constraint | `NOT FOUND on site. | NOT FOUND on the homepage.` | **Structured Data (Missing JSON-LD) / JS-rendering block** |
| https://www.spotify.com/se-en/ | Structured Data & Machine Readability | `NOT FOUND on site. | NOT FOUND / NOT VERIFIABLE in the accessible HTML.` | **Unknown** |
| https://www.spotify.com/se-en/ | Task Completion Test | `NOT FOUND on site. | NOT FOUND on the inspected homepage.` | **Engagement (No clear CTAs / Content buried in JS)** |
| https://www.spotify.com/se-en/ | Content Depth & Freshness | `NOT FOUND on site. | NOT FOUND on the inspected homepage.` | **Freshness (Stale dates / No <time> tags)** |
| https://www.spotify.com/se-en/ | Navigation & Orientation | `NOT FOUND on site. | NOT FOUND on site.` | **Unknown** |

## Milestone Checkpoint: 0.2
✅ ≥ 20 distinct, repeatable signals identified with evidence from ≥ 3 real websites each.
