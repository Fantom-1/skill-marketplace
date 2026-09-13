---
name: engagement-audit
description: Audits a website for AI-agent engagement factors, structural navigation accessibility, heading hierarchy, Client-Side Rendering reliance, and conversion actions.
allowed-tools:
  - web_fetch
  - bash
license: MIT
---
# Engagement Audit

## When to use
Use to determine if human visitors and AI agents referred to a website can navigate structure cleanly, extract core text without JavaScript rendering failures, and execute primary Call to Action (CTA) tasks.

## Inputs
- `url` (string): The website URL or domain to audit.

## Procedure
1. Run `scripts/engagement_check.py` on the input URL.
2. Evaluate navigation accessibility using HTML5 `<nav>` elements, ARIA `role="navigation"`, or structured header menu containers.
3. Validate heading hierarchy (`H1` and ARIA heading roles), allowing sectioned `H1` tags inside HTML5 `<section>` or `<article>` wrappers.
4. Detect Single Page Applications (SPAs) relying on Client-Side Rendering (CSR) that hide main content from basic LLM crawlers, recommending Server-Side Rendering (SSR) or SSG prerendering.
5. Search interactive elements (`a`, `button`, `input`, `[role="button"]`) across text content, `value`, `aria-label`, and `title` attributes for clear Call to Action (CTA) actions.

## Output
A JSON sub-report containing engagement findings (`ENGAGE-001` through `ENGAGE-006`) formatted according to the report schema.

