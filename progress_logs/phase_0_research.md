# Phase 0: Research & Experimentation (Field Research)
**Status:** Completed
**Date:** 2026-09-09

## Milestones & Checkpoints Recorded

### 0.1 Understand the Problem Space
- **Completed:** Mapped Appendix concepts (A-F) to testable signals in `PLAN.md`.

### 0.2 Field Research — Cited vs. Uncited Websites
- **Completed:** Parsed the AI response dataset (`responses/chatgpt`) for 20 websites across 6 prompts.
- **Analysis:** Discovered exactly **90 instances** of explicit AI failure (where the AI stated "NOT FOUND on site" for factual data like pricing, contact info, or founding dates).
- **Deliverable:** Created `Phase0_Signal_Catalogue.md` which maps these 90 failure observations directly to the automated technical signals.
- **Checkpoint:** ✅ ≥ 20 distinct, repeatable signals identified with evidence from ≥ 3 real websites each.

### 0.3 Prioritize Signals & Verification
- **Completed:** Wrote and executed `scripts/verify_scrapes.py` to run raw `curl/fetch`-style scraping against the 20 test sites.
- **Analysis:** Verified *why* the AI failed by extracting `JSON-LD` schemas, measuring JS reliance (visible text < 1000 chars), and checking `robots.txt`.
- **Deliverable:** Created `Phase0_Verification_Analysis.md` proving the empirical basis for our technical audits (e.g. proving sites where the AI failed were indeed JS-heavy or missing `JSON-LD`).
- **Checkpoint:** ✅ Every signal has a severity tier and detection method defined based on real failure data.

Phase 0 Field Research, Verification, and Analysis are completely finished and locked. The architecture decisions made in Phase 1 are empirically validated by this data.
