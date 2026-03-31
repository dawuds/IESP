# IESP — BNM RMiT IESP Audit Work Programs

**Last updated:** 2026-03-31

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
- `engagements.json` — 7 structured IESP engagement types with clauses, scope, deliverables
- `audit-integration.json` — AWP-to-engagement linkage and audit workflow integration
- `controls/control-domains.json`, `control-mapping.json` — Control structure
- `decision-tree/decision-tree.json` — IESP classification decision logic
- `requirements/` — Regulatory requirement breakdowns
- `artifacts/inventory.json`, `clause-map.json`

## AWP Workbooks (in Tech-Audit/IESP/)
The 5 Excel AWP workbooks have been moved to Tech-Audit/IESP/ (private repo):

| Workbook | Anchored To | Test Steps |
|----------|------------|-----------|
| `IESP-Cloud-WorkProgram.xlsx` | Appendix 10 (Part A + B) | 56 |
| `IESP-EmergingTech-WorkProgram.xlsx` | Appendix 9 | 47 |
| `IESP-DigitalServices-WorkProgram.xlsx` | 16.4/16.5 | 49 |
| `IESP-DCRA-WorkProgram.xlsx` | 10.24–10.28 | 49 |
| `IESP-NRA-WorkProgram.xlsx` | 10.36–10.43 | 49 |

**Standard sheets per workbook (9):** Methodology & Approach, Scoping, Planning, Domain Assessment(s), Appendix 7 Part D, Reporting & Attestation, Part C Self-Assessment, Scoring Dashboard.

**13-column format:** Ref, Level (ORG/PLATFORM/WORKLOAD), Control, Sub-Procedure, Assessment Procedures, Expected Evidence, Method (pre-populated) + Procedures Performed, Evidence Obtained, Evidence Ref, Observations, Conclusion, Recommendations (auditor fills).

**Assessment levels:** ORG (assessed once), PLATFORM (per CSP/platform in scope), WORKLOAD (per critical system, sample-based).

Markdown AWPs in `audit-work-programs/awp-*.md` retained in this repo as reference.

## AWP Architecture
AWPs are anchored to BNM RMiT control sources (Appendixes and clauses), not engagement types. Appendix 7 is the **reporting and IESP framework**, not a control source — only Part D defines controls.

**Control sources:**
| Source | Controls | Used By |
|--------|---------|---------|
| Appendix 10 | Cloud governance (7 areas) + design/controls (14 areas) | Cloud pre-impl + attestation |
| Appendix 9 | Emerging tech (5 assessment areas) | Emerging tech pre-impl + attestation |
| Appendix 7 Part D | Minimum controls: items 1(a-f) + 2(a-e) | ALL engagements (universal baseline) |
| Clauses 10.24–10.28 | DC resilience controls | DCRA engagements |
| Clauses 10.36–10.43 | Network resilience controls | NRA engagements |

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
- AWP workbooks (Excel, 13-column format) are in Tech-Audit/IESP/; markdown AWPs retained in this repo as reference
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
