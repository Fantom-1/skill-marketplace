# Engagement Audit Signals

| Signal | Domain | Severity | Detection Mechanism |
|--------|--------|----------|---------------------|
| No `<nav>` element | Engagement | High | Check for standard HTML5 navigation tags. |
| Missing viewport meta | Engagement | High | Check for `<meta name="viewport">` for mobile friendliness. |
| Poor heading hierarchy | Engagement | Medium | Check for H1 presence and logical H1 -> H2 structure. |
| Thin content | Engagement | Medium | Measure total word count of body text; flag if < 100. |
| No clear CTAs | Engagement | Medium | Detect buttons/links containing action verbs (Buy, Sign up, Contact, Learn). |
