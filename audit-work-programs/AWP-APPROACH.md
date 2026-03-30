# AWP Architecture and Approach

**Last updated:** 2026-03-31

## Principle: AWPs Are Anchored to Control Sources

Audit Work Programs (AWPs) are structured around the BNM RMiT Appendix or clause that defines the **controls** to be assessed, not around engagement types or audit phases.

**Important distinction — Appendix 7 is the reporting and IESP framework, not a control source:**

| Appendix 7 Part | What It Is | Controls? |
|-----------------|-----------|-----------|
| Part A | Report format (6-section output template) | No |
| Part B | CISO/board confirmation letter (9-point attestation) | No |
| Part C | Requirements on the IESP (independence, competence, scope, methodology, reporting, QA) | No — governs the IESP |
| Part D | Minimum controls to be assessed | **Yes** — the only part that defines controls |

**Controls come from:**
- Appendix 10 — cloud controls (Part A: 7 governance areas, Part B: 14 design/control areas)
- Appendix 9 — emerging technology controls (5 assessment areas)
- Clauses 10.24–10.28 — DC resilience controls
- Clauses 10.36–10.43 — network resilience controls
- Appendix 7 Part D — minimum controls baseline (applied to all engagements)

### Logic Chain

```
BNM requires negative attestation (IESP complies with Appendix 7 Part C)
  -> IESP performs a controls assessment to form that opinion
    -> Controls to assess are defined by the relevant source:
      -> Cloud: Appendix 10 (Part A + Part B)
      -> Emerging Tech: Appendix 9 (5 areas)
      -> DCRA: Clauses 10.24–10.28
      -> NRA: Clauses 10.36–10.43
      -> All engagements: Appendix 7 Part D (minimum controls)
    -> The AWP walks through every control in that source
      -> Each test step: ref, level, control, procedure, evidence, method
  -> Report follows Appendix 7 Part A format
  -> IESP attests under Part C; FI signs Part B (for pre-impl)
```

### Overlap: Cloud + Emerging Technology

When a cloud deployment involves emerging technology (e.g., AI/ML on cloud, cloud-native AI services like AWS Bedrock or Azure OpenAI), **both** Appendix 10 and Appendix 9 apply:
- Appendix 10 governs the **cloud infrastructure** controls
- Appendix 9 governs the **emerging technology** controls
- Both AWP workbooks must be used in conjunction
- Part D applies to both

### Negative Attestation (Part C)

The IESP's deliverable is a negative assurance opinion. The IESP must comply with Appendix 7 Part C requirements (independence, competence, scope, methodology, reporting, QA):

> "Nothing has come to our attention that causes us to believe the controls are not operating effectively..."

The AWP is the tool that generates sufficient appropriate evidence to support (or qualify) that opinion. Three opinion types:
- **Type A (Clean):** No material exceptions identified
- **Type B (With Exceptions):** Material exceptions identified but not pervasive
- **Type C (Adverse):** Pervasive control failures

### AWP Workbooks (Excel — 13-Column Working Papers)

The primary AWP deliverables are Excel workbooks in a 13-column format (evolved from the DAC-style template in sc-gtrm-dac). Each workbook is a complete working paper — the auditor fills in columns 8-13 as they execute.

| # | Workbook | Anchored To | Test Steps |
|---|----------|------------|-----------|
| 1 | `IESP-Cloud-WorkProgram.xlsx` | Appendix 10 (Part A + Part B) | 56 |
| 2 | `IESP-EmergingTech-WorkProgram.xlsx` | Appendix 9 (5 areas) | 47 |
| 3 | `IESP-DigitalServices-WorkProgram.xlsx` | RMiT 16.4/16.5 | 49 |
| 4 | `IESP-DCRA-WorkProgram.xlsx` | RMiT clauses 10.24–10.28 | 49 |
| 5 | `IESP-NRA-WorkProgram.xlsx` | RMiT clauses 10.36–10.43 | 49 |

**13-Column Format:**

| Col | Column Name | Pre-populated? | Purpose |
|-----|------------|----------------|---------|
| A | Ref | Yes | Unique test reference (e.g., CLD-01, PD-07) |
| B | Level | Yes | Assessment level: ORG / PLATFORM / WORKLOAD |
| C | Control | Yes | Control domain name |
| D | Sub-Procedure | Yes | Specific control aspect being tested |
| E | Assessment Procedures | Yes | Numbered, prescriptive test steps |
| F | Expected Evidence | Yes | Documents/artifacts to request |
| G | Method | Yes | Inspection / Inquiry / Observation / Confirmation / Re-performance |
| H | Procedures Performed | **Auditor fills** | What the auditor actually did |
| I | Evidence Obtained | **Auditor fills** | What was actually provided |
| J | Evidence Ref | **Auditor fills** | Working paper cross-reference |
| K | Observation / Findings | **Auditor fills** | What was found |
| L | Conclusion | **Auditor fills** | Compliant / Partially Compliant / Non-Compliant / N/A |
| M | Recommendations | **Auditor fills** | Remediation advice |

### Assessment Levels

Controls operate at different levels. The Level column (B) tells the auditor how to scope each test step:

| Level | Meaning | How to Use |
|-------|---------|-----------|
| **ORG** | Organisation / Enterprise | Assessed ONCE per engagement. Policies, governance, frameworks. |
| **PLATFORM** | Platform / CSP | Assessed PER PLATFORM in scope. If FI uses AWS + Azure, repeat for each. |
| **WORKLOAD** | System / Application | Assessed PER CRITICAL SYSTEM using sampling from the scoping sheet. |

### Standard Sheets (8 per workbook)

| # | Sheet | Purpose |
|---|-------|---------|
| 1 | **Methodology & Approach** | Engagement details, scope, mode, methods, conclusion scale, evidence hierarchy, limitations, sign-off |
| 2 | **Scoping** | Assessment level definitions, platforms/CSPs in scope, critical systems in scope, sampling approach |
| 3 | **Planning** | 14-step engagement planning checklist (trigger confirmation through scoping memo) |
| 4-5 | **Domain Assessment(s)** | Pre-populated test steps anchored to the relevant Appendix |
| 6 | **Appendix 7 Part D** | 29 minimum control test steps (universal baseline, embedded in every workbook) |
| 7 | **Reporting & Attestation** | 16-step reporting checklist (findings consolidation through Part C opinion formation) |
| 8 | **Part C Self-Assessment** | 6-requirement IESP self-assessment against Appendix 7 Part C |

**Generation:** Workbooks are generated via `python3 generate-awp-workbooks.py` from the repo root. The script contains all test step content and can be updated to regenerate.

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
