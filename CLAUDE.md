# IESP — BNM RMiT IESP Audit Work Programs

**Last updated:** 2026-04-01

## What This Is
Structured knowledge base and audit work programs for BNM RMiT Independent External Service Provider (IESP) assessments. SPA explorer with JSON data and markdown audit procedures. **Tier 1 Focus Area** in the GRC portfolio.

## Portfolio Role
One of 5 Tier 1 focus areas. Practitioner-focused toolkit for conducting IESP assessments under BNM RMiT. Includes markdown audit procedures and structured JSON data. Excel AWP workbooks, Word report template, and evidence folder structure are in Tech-Audit/IESP/ (private repo).

## Quick Start
Open `index.html` in a browser. Run `node validate.js` to check data integrity. See `engagements.json` for structured engagement type data.

## Architecture
- **SPA**: `index.html` + `app.js` + `style.css` (vanilla JS, no build step)
- **Schema**: GRC Portfolio v2.0 Standardized Schema

## Key Data Files
- `methodology/IESP-METHODOLOGY.md` — End-to-end IESP assessment methodology (start here)
- `methodology/AWP-DESIGN-RATIONALE.md` — AWP design decisions, column justification, replication guide
- `engagements.json` — 7 structured IESP engagement types with clauses, scope, deliverables
- `audit-integration.json` — AWP-to-engagement linkage and audit workflow integration
- `controls/control-domains.json`, `control-mapping.json` — Control structure
- `decision-tree/decision-tree.json` — IESP classification decision logic
- `requirements/` — Regulatory requirement breakdowns
- `artifacts/inventory.json`, `clause-map.json`

## AWP Workbooks
| Workbook | Anchored To | Domains | Sub-Items |
|----------|------------|---------|-----------|
| `IESP-Cloud-WorkProgram.xlsx` | Appendix 10 (Part A + B) | 32 | 148 |
| `IESP-EmergingTech-WorkProgram.xlsx` | Appendix 9 | 18 | 66 |
| `IESP-DigitalServices-WorkProgram.xlsx` | 16.4/16.5 | 16 | 64 |
| `IESP-DCRA-WorkProgram.xlsx` | 10.24–10.28 | 16 | 63 |
| `IESP-NRA-WorkProgram.xlsx` | 10.36–10.43 | 19 | 64 |

**Standard sheets per workbook (9):** Methodology & Approach, Scoping, Planning, Domain Assessment(s), Appendix 7 Part D, Reporting & Attestation, Part C Self-Assessment, Scoring Dashboard.

**14-column format:** BNM Ref, Ref, Level (ORG/PLATFORM/WORKLOAD), Control, Sub-Procedure, Assessment Procedures, Expected Evidence, Method (pre-populated) + Procedures Performed, Evidence Obtained, Evidence Ref, Observations, Conclusion, Recommendations (auditor fills).

**Domain-level conclusions:** Auditor gives ONE conclusion per control domain (not per sub-item). Sub-items are individual BNM requirements that feed observations into the domain conclusion. Best practice additions have blank BNM Ref — clearly separated from regulatory requirements.

**Assessment levels:** ORG (assessed once), PLATFORM (per CSP/platform in scope), WORKLOAD (per critical system, sample-based).

Regenerate with `python3 generate-awp-workbooks.py`. Legacy markdown AWPs in `awp-*.md` retained as reference.

## AWP Architecture
AWPs are anchored to BNM RMiT control sources (Appendixes and clauses), not engagement types. Appendix 7 is the **reporting and IESP framework**, not a control source — only Part D defines controls.

**Control sources (57 unique domains, 11 shared via Part D):**
| Source | Domains | Sub-Items | Used By |
|--------|---------|-----------|---------|
| Appendix 10 Part A | 7 governance | 30 | Cloud |
| Appendix 10 Part B | 14 design/controls | 74 | Cloud |
| Appendix 9 (BNM) | 2 | 9 | Emerging tech |
| Appendix 9 (best practice) | 5 | 13 | Emerging tech |
| Clauses 10.24–10.28 | 5 | 19 | DCRA |
| Clauses 10.36–10.43 | 8 | 20 | NRA |
| Digital services | 5 | 20 | Digital services |
| Appendix 7 Part D | 11 | 44 | ALL engagements |

**Appendix 7 (reporting framework, not controls):**
- Part A — Report format (6-section output template)
- Part B — CISO/board confirmation letter (9-point attestation, for pre-impl)
- Part C — Requirements on the IESP (independence, competence, scope, methodology, reporting, QA)
- Part D — Minimum controls (the only part that defines controls)

**Engagement mode** (pre-impl vs. attestation) is guidance within each AWP, not a separate document:
- **Design adequacy** (pre-impl): Assess whether proposed controls meet the requirement
- **Operating effectiveness** (attestation): Sample and verify controls operated as designed

**Cloud + Emerging Tech overlap:** When cloud involves emerging tech (AI/ML on cloud), both Appendix 10 and Appendix 9 workbooks must be used.

AWPs must be prescriptive enough for a junior auditor to execute without senior interpretation.

## Report Template and Evidence (in Tech-Audit/IESP/)
- `IESP-Report-Template.docx` — Appendix 7 Part A format with Part C attestation (Type A/B/C)
- `evidence-folder-structure.md` — Evidence folder documentation
- `create-evidence-structure.sh` — Generates 66-folder evidence structure per engagement
- `AWP-APPROACH.md` — AWP design approach documentation

## Conventions
- Kebab-case slugs for all IDs
- AWP workbooks use 14-column format with BNM Ref traceability and domain-level conclusions
- Conclusion scale: Compliant / Partially Compliant / Non-Compliant / N/A
- Evidence hierarchy: Direct observation > Independent confirmation > System-generated > Re-performance > Documentary > Inquiry
- Assessment levels: ORG (once per engagement) > PLATFORM (per CSP) > WORKLOAD (per critical system)

## Important
- IESP classification determines assessment scope — misclassification affects entire audit
- Decision tree logic must match current BNM RMiT requirements
- Appendix 7 is the reporting/IESP framework, not a control source (except Part D)

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
- [Tech-Audit/IESP](https://github.com/dawuds/Tech-Audit) — IESP audit toolkit (5 Excel workbooks, report template, evidence structure, AWP approach) (Tier 2)
- [grc](https://github.com/dawuds/grc) — Portfolio hub
