# IESP — BNM RMiT IESP Audit Work Programs

**Last updated:** 2026-03-31

## What This Is
Structured knowledge base and audit work programs for BNM RMiT Independent External Service Provider (IESP) assessments. SPA explorer with JSON data and markdown audit procedures. **Tier 1 Focus Area** in the GRC portfolio.

## Portfolio Role
One of 5 Tier 1 focus areas. Practitioner-focused toolkit for conducting IESP assessments under BNM RMiT Appendix 7. Content is currently markdown-heavy — JSON-ification of engagements and evidence checklists is a priority.

## Quick Start
Open `index.html` in a browser. Run `node validate.js` to check data integrity. See `engagements.json` for structured engagement type data.

## Architecture
- **SPA**: `index.html` + `app.js` + `style.css` (vanilla JS, no build step)
- **Schema**: GRC Portfolio v2.0 Standardized Schema

## Key Data Files
- `engagements.json` — 7 structured IESP engagement types with clauses, scope, deliverables
- `audit-integration.json` — AWP-to-engagement linkage and audit workflow integration
- `controls/control-domains.json`, `control-mapping.json` — Control structure
- `decision-tree/decision-tree.json` — IESP classification decision logic
- `audit-work-programs/` — 6 AWPs: cloud, DCRA, digital-services, NRA, AI/emerging-tech, Appendix 7 Part D
- `requirements/` — Regulatory requirement breakdowns
- `artifacts/inventory.json`, `clause-map.json`

## AWP Architecture
AWPs are anchored to BNM RMiT Appendixes, not engagement types. The logic chain:

1. BNM requires negative attestation (Appendix 7 Part C)
2. To form that attestation, the IESP performs a controls assessment
3. The controls assessed are defined by the relevant Appendix
4. The AWP walks through every control in that Appendix

**AWP set (6 total):**
| AWP | Anchored To | Used By |
|-----|------------|---------|
| Appendix 10 AWP | Appendix 10 (Part A: 7 governance, Part B: 14 controls) | Cloud pre-impl + attestation |
| Appendix 9 AWP | Appendix 9 (5 assessment areas) | Emerging tech pre-impl + attestation |
| Appendix 7 Part D AWP | Part D items 1(a-f) + 2(a-e) | ALL engagements (universal baseline) |
| DCRA AWP | Clauses 10.24–10.28 | DCRA engagements |
| NRA AWP | Clauses 10.36–10.43 | NRA engagements |
| Digital Services AWP | 16.4/16.5 + Part D | Digital services pre-launch |

**Engagement mode** (pre-impl vs. attestation) is guidance within each AWP, not a separate document:
- **Design adequacy** (pre-impl): Assess whether proposed controls meet the requirement
- **Operating effectiveness** (attestation): Sample and verify controls operated as designed

AWPs must be prescriptive enough for a junior auditor to execute without senior interpretation.

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
