# IESP Toolkit — Learnings & Architecture Notes

## Architecture Decisions

- **Content-heavy SPA**: Unlike other GRC repos (45-50 controls as JSON), IESP is primarily markdown-based (47 .md files) with 5 JSON data files. The app.js renders markdown content references rather than structured control data.
- **Decision tree as JSON**: The engagement type decision tree is machine-readable (decision-tree.json) enabling interactive branching UI without hardcoding logic in app.js.
- **Engagement-centric navigation**: 7 tabs organized by practitioner workflow (Decision Tree → Engagements → Controls → Work Programs → Templates → Evidence) rather than the typical framework-centric layout.
- **Cross-reference to RMIT**: control-mapping.json maps IESP domains to RMIT clause numbers, ISO 27001:2022 controls, and NIST CSF 2.0 functions. This enables bidirectional lookup between the RMIT repo and IESP toolkit.

## Data Quality

- **Source document**: BNM/RH/PD 028-98, issued 28 November 2025 (RMiT Policy Document).
- **Appendix 7 Part D**: 7 core control domains (1a-1f + 2) directly from the official document. 3 additional domains (Cloud/Emerging Tech/Third-Party) from Appendices 8, 9, 10.
- **Worked example**: Bank Perdana Berhad is entirely fictitious. All engagement documents use realistic but fabricated data for educational purposes.
- **ISO 27001 mappings**: Use 2022 edition (A.5/A.7/A.8 numbering scheme).
- **NIST CSF mappings**: Use CSF 2.0 function/category IDs (GV, PR, RS, RC prefixes).

## Technical Notes

- **ES5-compatible JavaScript**: Uses var, function declarations for maximum browser compatibility. No build step required.
- **Hash routing**: #overview, #decision-tree, #engagements, #controls, #work-programs, #templates, #evidence.
- **Caching**: Map-based cache for JSON fetches prevents redundant network requests.
- **Dark mode**: localStorage persistence with prefers-color-scheme fallback.

## Distinction from RMIT Repo

The RMIT repo is a comprehensive clause-by-clause extraction of the full BNM RMiT document (121 clauses). The IESP toolkit focuses on the **practitioner workflow** for conducting independent reviews — when to engage, how to scope, what to test, and how to report. They are complementary: RMIT provides the "what" (requirements), IESP provides the "how" (methodology).
