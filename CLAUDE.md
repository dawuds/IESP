# IESP — BNM RMiT IESP Audit Work Programs

## What This Is
Structured knowledge base and audit work programs for BNM RMiT Internet and Electronic Services Provision (IESP) assessments. SPA explorer with JSON data and markdown audit procedures.

## Architecture
- **SPA**: `index.html` + `app.js` + `style.css` (vanilla JS, no build step)
- **Schema**: GRC Portfolio v2.0 Standardized Schema

## Key Data Files
- `controls/control-domains.json`, `control-mapping.json` — Control structure
- `decision-tree/decision-tree.json` — IESP classification decision logic
- `audit-work-programs/` — 6 AWPs: cloud, DCRA, digital-services, NRA, AI/emerging-tech, Appendix 7 Part D
- `requirements/` — Regulatory requirement breakdowns
- `artifacts/inventory.json`, `clause-map.json`

## Conventions
- Kebab-case slugs for all IDs
- AWP files are markdown with structured audit steps

## Important
- IESP classification (Appendix 7) determines assessment scope — misclassification affects entire audit
- Decision tree logic must match current BNM RMiT Appendix 7 requirements

## Related Repos
- `RMIT/` — Parent RMiT framework
- `cybercompliance/reference/nacsa/` — Regulatory source documents
