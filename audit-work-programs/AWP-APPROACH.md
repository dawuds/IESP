# AWP Architecture and Approach

**Last updated:** 2026-03-31

## Principle: AWPs Are Anchored to Appendixes

Audit Work Programs (AWPs) are structured around the BNM RMiT Appendix that defines the controls to be assessed, not around engagement types or audit phases. This ensures the AWP scope directly mirrors the regulatory requirement.

### Logic Chain

```
BNM requires negative attestation (Appendix 7 Part C)
  -> IESP must perform a controls assessment to form that opinion
    -> Controls to assess are defined by the relevant Appendix
      -> Cloud: Appendix 10 (Part A + Part B)
      -> Emerging Tech: Appendix 9 (5 areas)
      -> All engagements: Appendix 7 Part D (minimum controls)
    -> The AWP walks through every control in that Appendix
      -> Each test step: objective, procedure, evidence, pass/fail
  -> Findings feed into Part A report and Part C attestation opinion
```

### Negative Attestation (Part C)

The IESP's deliverable is a negative assurance opinion under Appendix 7 Part C:

> "Nothing has come to our attention that causes us to believe the controls are not operating effectively..."

The AWP is the tool that generates sufficient appropriate evidence to support (or qualify) that opinion. Three opinion types:
- **Type A (Clean):** No material exceptions identified
- **Type B (With Exceptions):** Material exceptions identified but not pervasive
- **Type C (Adverse):** Pervasive control failures

### AWP Workbooks (Excel — 12-Column Working Papers)

The primary AWP deliverables are Excel workbooks in the DAC-style 12-column format (modelled on the sc-gtrm-dac `DAC-Cybersecurity-Custody-WorkProgram.xlsx`). Each workbook is a complete working paper — the auditor fills in columns 7-12 as they execute.

| # | Workbook | Anchored To | Sheets | Test Steps |
|---|----------|------------|--------|-----------|
| 1 | `IESP-Cloud-WorkProgram.xlsx` | Appendix 10 (Part A + Part B) | Methodology + App 10 Part A + App 10 Part B + Part D | 54 |
| 2 | `IESP-EmergingTech-WorkProgram.xlsx` | Appendix 9 (5 areas) | Methodology + Appendix 9 + Part D | 44 |
| 3 | `IESP-DigitalServices-WorkProgram.xlsx` | RMiT 16.4/16.5 | Methodology + Digital Services + Part D | 49 |
| 4 | `IESP-DCRA-WorkProgram.xlsx` | RMiT clauses 10.24–10.28 | Methodology + DCRA + Part D | 49 |
| 5 | `IESP-NRA-WorkProgram.xlsx` | RMiT clauses 10.36–10.43 | Methodology + NRA + Part D | 49 |

**12-Column Format:**

| Col | Column Name | Pre-populated? | Purpose |
|-----|------------|----------------|---------|
| A | Ref | Yes | Unique test reference (e.g., CLD-01, PD-07) |
| B | Control | Yes | Control domain name |
| C | Sub-Procedure | Yes | Specific control aspect being tested |
| D | Assessment Procedures | Yes | Numbered, prescriptive test steps |
| E | Expected Evidence | Yes | Documents/artifacts to request |
| F | Method | Yes | Inspection / Inquiry / Observation / Confirmation / Re-performance |
| G | Procedures Performed | **Auditor fills** | What the auditor actually did |
| H | Evidence Obtained | **Auditor fills** | What was actually provided |
| I | Evidence Ref | **Auditor fills** | Working paper cross-reference |
| J | Observation / Findings | **Auditor fills** | What was found |
| K | Conclusion | **Auditor fills** | Compliant / Partially Compliant / Non-Compliant / N/A |
| L | Recommendations | **Auditor fills** | Remediation advice |

**Methodology & Approach Sheet** (common to all workbooks):
- Engagement details (entity, type, date, assessor, reference)
- Scope of assessment
- Engagement mode guidance (design adequacy vs. operating effectiveness)
- Assessment methods (Inspection, Inquiry, Observation, Confirmation, Re-performance)
- Conclusion scale definitions
- Evidence hierarchy (6 ranks)
- Limitations and sign-off

**Part D** is embedded as a sheet in every workbook — the auditor gets one file per engagement.

**Generation:** Workbooks are generated via `python3 generate-awp-workbooks.py` from the repo root for reproducibility. The script contains all test step content and can be updated to regenerate workbooks.

### Legacy Markdown AWPs

The original markdown AWPs remain in `audit-work-programs/awp-*.md` as reference material:

| # | File | Status |
|---|------|--------|
| 1 | `awp-cloud.md` | Superseded by `IESP-Cloud-WorkProgram.xlsx` |
| 2 | `awp-ai-emerging-tech.md` | Superseded by `IESP-EmergingTech-WorkProgram.xlsx` |
| 3 | `awp-appendix-7-part-d.md` | Superseded — Part D embedded in all workbooks |
| 4 | `awp-dcra.md` | Superseded by `IESP-DCRA-WorkProgram.xlsx` |
| 5 | `awp-nra.md` | Superseded by `IESP-NRA-WorkProgram.xlsx` |
| 6 | `awp-digital-services.md` | Superseded by `IESP-DigitalServices-WorkProgram.xlsx` |

### Engagement Mode: Pre-Implementation vs. Attestation

The same AWP serves both engagement modes. Each test step includes guidance for both:

**Design Adequacy (Pre-Implementation — 17.1):**
- Assessing proposed/planned controls before go-live
- Evidence is primarily documentary: architecture designs, policies, vendor assessments, staging test results
- Question: "Is this control designed to meet the requirement?"

**Operating Effectiveness (Independent Attestation):**
- Assessing controls that are live and operational
- Evidence is observation, sampling, re-performance, system-generated logs
- Question: "Did this control operate effectively during the assessment period?"
- Requires defined sampling methodology and assessment period

### Evidence Hierarchy

When gathering evidence for the attestation, prefer higher-ranked evidence:

| Rank | Evidence Type | Description |
|------|-------------|-------------|
| 1 | Direct observation | IESP directly observes control in operation |
| 2 | Independent confirmation | Third-party evidence (SOC 2, CSP certifications) |
| 3 | System-generated | Logs, configurations without manual intervention |
| 4 | Re-performance | IESP re-performs control procedure |
| 5 | Documentary | Policies, procedures, meeting minutes |
| 6 | Inquiry | Verbal representations from FI personnel |

### AWP Test Step Design Principles

Every test step must be prescriptive enough for a junior auditor to execute without senior interpretation:

1. **Ref** — Unique identifier (e.g., CLD-01, AI-03, PD-07)
2. **Control / Sub-Procedure** — What domain and specific aspect is being tested
3. **Assessment Procedures** — Numbered, specific actions the auditor performs (not vague guidance)
4. **Expected Evidence** — Concrete documents/artifacts to request from the FI
5. **Method** — How the evidence is gathered (Inspection, Inquiry, Observation, Confirmation, Re-performance)
6. **Conclusion** — Compliant / Partially Compliant / Non-Compliant / N/A (standardised scale)

### Engagement-to-AWP Mapping

| Engagement | Trigger | Mode | AWPs Required |
|-----------|---------|------|---------------|
| Cloud Pre-Implementation | 17.1 | Design adequacy | Appendix 10 AWP + Part D AWP |
| Cloud Independent Attestation | Appendix 7 | Operating effectiveness | Appendix 10 AWP + Part D AWP |
| Emerging Tech Pre-Implementation | 17.1 | Design adequacy | Appendix 9 AWP + Part D AWP |
| Emerging Tech Independent Attestation | Appendix 7 | Operating effectiveness | Appendix 9 AWP + Part D AWP |
| DCRA | 14.1 | Operating effectiveness | DCRA AWP + Part D AWP |
| NRA | 14.2 | Operating effectiveness | NRA AWP + Part D AWP |
| Digital Services Pre-Launch | 16.4/16.5 | Design adequacy | Digital Services AWP (Part D embedded) |
| BNM Directed | 17.4/1.4 | As directed | Scoped per BNM direction |
