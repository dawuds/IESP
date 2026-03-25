# IESP — BNM RMiT IESP Audit Work Programs

**Last updated:** 2026-03-25

## What This Is
Structured knowledge base and audit work programs for BNM RMiT Independent External Service Provider (IESP) assessments. SPA explorer with JSON data and markdown audit procedures. **Tier 1 Focus Area** in the GRC portfolio.

## Portfolio Role
One of 5 Tier 1 focus areas. Practitioner-focused toolkit for conducting IESP assessments under BNM RMiT Appendix 7. Content is currently markdown-heavy — JSON-ification of engagements and evidence checklists is a priority.

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

## Validation
```bash
node validate.js
```

## Related Repos
- [RMIT](https://github.com/dawuds/RMIT) — Parent RMiT framework (121 clauses)
- [nacsa](https://github.com/dawuds/nacsa) — NACSA Act 854; IESP engagements may interact with NCII obligations (Tier 1)
- [pdpa-my](https://github.com/dawuds/pdpa-my) — PDPA data protection overlaps with IESP assessment scope (Tier 1)
- [AI-Governance](https://github.com/dawuds/AI-Governance) — AI/emerging tech is an IESP engagement type (Tier 1)
- [sc-gtrm](https://github.com/dawuds/sc-gtrm) — Parallel assessment framework for capital markets (Tier 1)
- [Tech-Audit](https://github.com/dawuds/Tech-Audit) — Audit methodology; IESP domain planned (Tier 2)
- [grc](https://github.com/dawuds/grc) — Portfolio hub
