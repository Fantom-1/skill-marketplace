# Entity Identity Audit Signals

| Signal | Domain | Severity | Detection Mechanism |
|--------|--------|----------|---------------------|
| Missing `Organization` schema | Discoverability | High | Check JSON-LD for `@type: Organization` or `@type: LocalBusiness`. |
| No `sameAs` links | Discoverability | High | Check JSON-LD `Organization` for `sameAs` pointing to Wikipedia, social profiles. |
| Inconsistent description | Discoverability | Medium | Compare `<meta description>`, JSON-LD description, and OG description. |
| No About page | Discoverability | Medium | Check for `/about` links in navigation or footer. |
