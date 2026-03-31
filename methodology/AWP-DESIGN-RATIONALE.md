# AWP Design Rationale

**Last updated:** 2026-04-01
**Applicable to:** All GRC portfolio AWP workbooks (IESP, GTRM-DAC, and future repos)

---

## 1. Design Principles

### 1.1 The AWP Is Both Work Program AND Working Paper

Most firms maintain separate documents: a work program (what to test) and working papers (what was tested). Our AWPs combine both into a single Excel workbook. The first 7-8 columns are pre-populated (the work program), the remaining 6 columns are filled by the auditor during execution (the working paper).

**Why:** Reduces duplication, ensures every test step is documented, and the completed workbook IS the evidence of work performed. A junior auditor opens one file and works through it.

### 1.2 AWPs Are Anchored to Regulatory Sources, Not Engagement Types

Each AWP mirrors the structure of the regulatory appendix or clause that defines the controls. The AWP is not organised by "audit phases" or "risk domains" — it walks through the regulation section by section.

**Why:** Direct traceability to the regulatory requirement. The regulator (BNM, SC, etc.) can see exactly which requirement was tested and what was found. If the regulation is restructured, the AWP restructure follows naturally.

### 1.3 Domain-Level Conclusions, Sub-Item Observations

The auditor gives ONE conclusion per control domain (e.g., "Cloud Risk Management" or "Access Control"). Individual regulatory sub-items are tested separately and observations are recorded, but they roll up into the domain conclusion.

**Why:** This matches how audit opinions are formed — you assess a control area holistically, not as disconnected checkboxes. A control domain might have 7 sub-items where 6 are compliant and 1 has a minor gap — the domain conclusion is "Partially Compliant" with the specific gap noted. This is how Big 4 firms structure SOC 2 and ISAE 3402 testing.

### 1.4 Prescriptive for Junior Auditors

Every test step must be executable by a junior auditor without requiring senior interpretation. Test steps are numbered, specific, and tell the auditor exactly what to do, what to ask for, and what passes or fails.

**Why:** The value of the AWP is that it encodes the senior auditor's judgement into a repeatable procedure. If the junior needs to ask "what does this mean?" for every step, the AWP has failed.

---

## 2. Column Structure (14 Columns)

### 2.1 Why 14 Columns

| Col | Name | Purpose | Justification |
|-----|------|---------|--------------|
| A | **BNM Ref** | Regulatory source reference | Traceability — every row maps to a specific regulatory sub-item. Blank = best practice addition. Most firms do this in a separate mapping sheet; inline is more efficient. |
| B | **Ref** | AWP test reference | Unique ID for cross-referencing to evidence folders, findings, and the report |
| C | **Level** | ORG / PLATFORM / WORKLOAD | Tells the auditor whether to assess once, per platform, or per system. Unique to our approach — eliminates scoping confusion. |
| D | **Control Domain** | Control area name | Groups sub-items under the assessable unit |
| E | **Sub-Procedure** | Specific aspect being tested | What this particular row is checking |
| F | **Assessment Procedures** | Numbered test steps | The "how" — what the auditor actually does |
| G | **Expected Evidence** | Documents/artifacts to request | The "what" — saves the auditor from guessing what to ask for |
| H | **Method** | Inspection / Inquiry / Observation / Confirmation / Re-performance | Standardised assessment method taxonomy |
| I | **Procedures Performed** | What the auditor actually did | Auditor fills — documents the work performed |
| J | **Evidence Obtained** | What was actually provided | Auditor fills — documents what the FI delivered |
| K | **Evidence Ref** | Working paper cross-reference | Auditor fills — links to the evidence folder structure |
| L | **Observations** | What was found | Auditor fills — factual observations per sub-item |
| M | **Conclusion** | Compliant / Partially / Non-Compliant / N/A | Auditor fills — **domain rows only** |
| N | **Recommendations** | Remediation advice | Auditor fills — **domain rows only** |

### 2.2 Industry Comparison

| Framework/Standard | Typical Columns | Notes |
|-------------------|----------------|-------|
| ISACA IT Audit | 4-6 | Control objective, test, evidence, result |
| Big 4 SOC 2/ISAE 3402 | 6-8 | Control, ToD, ToOE, result, exceptions |
| ISA 315/PCAOB | 5-7 | Assertion, control, procedure, evidence, conclusion |
| SC GTRM DAC (our v1) | 12 | Original format without Level or BNM Ref |
| Our current standard | 14 | Combined work program + working paper + traceability |

Our 14-column format is on the higher end because it combines three things that are typically separate documents: (1) the regulatory requirements mapping, (2) the audit work program, and (3) the working paper template. This is more efficient — one file per engagement instead of three.

---

## 3. Row Structure

### 3.1 Two Row Types

**Domain Row** (conclusion level):
- Bold font, green fill (E2EFDA)
- Conclusion (M) and Recommendations (N) cells highlighted yellow
- Ref format: `CLD-01`, `PD-05`, `NRA-03` (no dots)
- Represents one assessable control domain
- Auditor gives ONE conclusion here after reviewing all sub-items

**Sub-Item Row** (observation level):
- Normal font, no special fill
- Ref format: `CLD-01.1`, `PD-05.3`, `NRA-03.2` (with dots)
- Represents one specific regulatory sub-requirement or best practice test
- Auditor records observations but NOT conclusions
- BNM Ref column traces to exact source (e.g., `App10-A1(b)`, `App7-D2(e)(viii)`)

### 3.2 Best Practice Identification

Sub-item rows with a **blank BNM Ref** are best practice additions — the IESP's professional value-add beyond the literal regulatory text. This is important because:
- The FI can see what's regulatory vs. advisory
- The regulator can see that the IESP went beyond minimum requirements
- If challenged, the IESP can justify the scope by separating mandatory from recommended

---

## 4. Assessment Levels

| Level | Meaning | When to Use | Example |
|-------|---------|-------------|---------|
| **ORG** | Organisation / Enterprise | Assessed ONCE per engagement | Cloud strategy, incident management policy, BCP framework |
| **PLATFORM** | Platform / CSP / DC | Assessed PER PLATFORM in scope | IAM config per CSP, network architecture per DC, encryption per platform |
| **WORKLOAD** | System / Application | Assessed PER CRITICAL SYSTEM (sample-based) | Backup config per workload, DR arrangement per system, data residency per dataset |

**Why this matters:** Without assessment levels, a junior auditor doesn't know whether to test "IAM" once or per CSP. If the FI uses AWS and Azure, IAM must be tested separately for each — the controls are configured differently. ORG-level controls (like the cloud policy) are assessed once regardless.

---

## 5. Standard Sheets (9 per workbook)

| # | Sheet | Purpose | Rationale |
|---|-------|---------|-----------|
| 1 | **Methodology & Approach** | Engagement details, scope, mode, methods, conclusion scale, evidence hierarchy, sampling methodology, limitations, sign-off | Professional standards require methodology documentation |
| 2 | **Scoping** | Platforms in scope, critical systems, sampling approach, assessment level definitions | Scoping is the foundation — wrong scope = wrong conclusions |
| 3 | **Planning** | 14-step planning checklist | Ensures no engagement setup steps are missed |
| 4-5 | **Domain Assessment(s)** | Pre-populated test steps with context rows and BNM Ref traceability | The core assessment — anchored to the regulatory appendix/clauses |
| 6 | **Appendix 7 Part D** | 11 domains, 44 sub-items (universal minimum controls) | Embedded in every workbook so the auditor has one complete file |
| 7 | **Reporting & Attestation** | 16-step reporting checklist including Part C opinion formation | Ensures the report process is complete and the attestation is properly formed |
| 8 | **Part C Self-Assessment** | 6-requirement IESP compliance check | The IESP must self-assess against Part C before issuing the report |
| 9 | **Scoring Dashboard** | Live COUNTIF formulas: domain compliance counts, overall %, Part C opinion indicator, level breakdown | Automated aggregation — the auditor doesn't manually count conclusions |

---

## 6. Supporting Deliverables

### 6.1 Context Rows

Italic merged rows under each section header providing:
- **Why** — regulatory intent
- **What good looks like** — expected state
- **Key risk if absent** — what's at stake

**Why:** Gives the auditor the "so what" before diving into test steps. Without context, the auditor tests mechanically without understanding purpose.

### 6.2 Sampling Methodology (in Methodology sheet)

- Population-based sample sizes (5 tiers from 1-5 to 100+)
- Time-based evidence coverage (board reports = 4 quarters, operational = 3-6 months, etc.)
- Control risk tiers (Critical / Standard / Conditional)

**Why:** Defensible sampling basis. Without documented methodology, a reviewer can challenge "why 10 samples and not 20?"

### 6.3 Scoring Dashboard

- COUNTIF formulas counting Compliant / Partially / Non-Compliant / N/A per sheet
- Overall compliance percentage
- Part C opinion indicator (Type A/B/C) via nested IF formula
- Breakdown by assessment level (ORG/PLATFORM/WORKLOAD)

**Why:** Automated aggregation reduces manual effort and errors. The Part C opinion formula gives the auditor an indicative opinion type based on the data.

### 6.4 Report Template (Word)

Appendix 7 Part A format with:
- Finding template (condition/criteria/cause/effect/recommendation/management response)
- Part C attestation statements (Type A/B/C)
- Part D minimum controls summary

### 6.5 Evidence Folder Structure

66-folder structure generated per engagement via shell script. Folders map to AWP sections and the Evidence Ref column (K).

---

## 7. Evolution History

| Version | Date | Key Changes |
|---------|------|-------------|
| v1 | 2026-03-26 | 12-column format from DAC template. Flat test steps, no levels, no BNM Ref. |
| v2 | 2026-03-31 | 13 columns — added Level (ORG/PLATFORM/WORKLOAD). Added Scoping, Planning, Reporting, Part C sheets. Filled Cloud and Emerging Tech gaps. |
| v3 | 2026-03-31 | Added context rows (why/what good looks like/key risk). Sampling methodology in Methodology sheet. Cloud + Emerging Tech overlap guidance. |
| v4 | 2026-04-01 | 14 columns — added BNM Ref. Domain-level conclusions with sub-item rows. Each BNM sub-item gets its own row. Best practice clearly separated (blank BNM Ref). Scoring counts domain conclusions only. |

---

## 8. Replicating This Pattern to Other GRC Repos

When building AWPs for other frameworks (SC GTRM, NACSA, PDPA, etc.), apply the same pattern:

1. **Identify the control source** — which regulation/guideline/appendix defines the controls?
2. **Map every sub-item** — each regulatory sub-point gets its own row with source reference
3. **Group into domains** — one conclusion per logical control area
4. **Assign levels** — which controls are entity-wide vs. per-system?
5. **Add best practice** — mark with blank source ref so it's clearly separated
6. **Use the 14-column format** — consistent across all GRC repos
7. **Include all 9 standard sheets** — methodology, scoping, planning, assessment, Part D equivalent, reporting, self-assessment, scoring
8. **Write context rows** — why each domain matters
9. **Define sampling** — population-based and time-based tables

The generator script (`generate-awp-workbooks.py`) can be adapted for any framework by changing the section data while keeping the workbook structure and styling functions.
