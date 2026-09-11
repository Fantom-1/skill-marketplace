---
name: entity-identity-audit
description: Audits a website for brand ambiguity, consistency of identity, and presence of knowledge graph links.
license: MIT
---
# Entity Identity Audit
## When to use
Use to verify if a brand clearly identifies itself and links to external identity graphs (Wikipedia, LinkedIn) to avoid mistaken identity.
## Inputs
- `url` (string): The website URL to audit.
## Procedure
1. Run `scripts/identity_check.py` on the input URL.
2. Check JSON-LD `Organization` schema for `sameAs` links.
3. Compare the brand description across `<meta description>`, JSON-LD, and OpenGraph to check for consistency.
4. Check for the presence of an "About" page.
## Output
A JSON sub-report containing discoverability findings related to entity identity and ambiguity.
