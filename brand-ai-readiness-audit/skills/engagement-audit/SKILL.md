---
name: engagement-audit
description: Audits a website for on-site engagement factors, including clear navigation, CTAs, content depth, and mobile-friendliness.
license: MIT
---
# Engagement Audit
## When to use
Use to determine if visitors to a website (including those referred by AI) will have a good experience and stay on the site.
## Inputs
- `url` (string): The website URL to audit.
## Procedure
1. Run `scripts/engagement_check.py` on the input URL.
2. Check for clear `<nav>` and internal link structures.
3. Check for obvious Call to Action (CTA) buttons.
4. Check for mobile `<meta name="viewport">`.
5. Flag thin content (pages with very low word counts) or content buried in carousels.
## Output
A JSON sub-report containing engagement findings related to user retention and accessibility.
