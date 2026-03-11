> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative. This does not constitute legal, regulatory, or professional advice. Always refer to the official BNM Policy Document and engage qualified professionals.

---

# Worked Example: Bank Perdana Berhad — Cloud Pre-Implementation IESP Review (17.1)

## Scenario Summary

| Field | Detail |
|-------|--------|
| **Financial Institution** | Bank Perdana Berhad (fictitious) |
| **FI Profile** | Mid-sized Malaysian commercial bank, ~RM50B total assets, ~2,400 staff |
| **IESP Firm** | CyberAssure Advisory Sdn Bhd (fictitious) |
| **Engagement Reference** | CA/IESP/2026/BPB-001 |
| **Engagement Type** | Cloud Pre-Implementation Technology Risk Assessment |
| **RMIT Trigger** | Paragraph 17.1 — first-time migration of critical systems to public cloud |
| **System Under Review** | Temenos T24/Transact R23 core banking system |
| **Target Environment** | AWS ap-southeast-1 (Singapore), DR in ap-southeast-3 (Jakarta) |
| **Key Services** | EC2, RDS Aurora PostgreSQL, S3, EKS, CloudFront, Direct Connect |
| **Higher-Risk Factors** | Customer data processing in cloud; cross-border data flow to Singapore |
| **Engagement Period** | 6 January – 14 March 2026 (10 weeks) |
| **Total Fee** | RM300,000 (excl. SST) |

---

## Table of Contents

This worked example comprises **14 files** (00–13), each representing a key artefact in the IESP engagement lifecycle:

| # | File | Description |
|---|------|-------------|
| 00 | [00-README.md](./00-README.md) | This file — scenario overview and navigation guide |
| 01 | [01-engagement-letter.md](./01-engagement-letter.md) | Formal engagement letter between IESP and FI |
| 02 | [02-scoping-document.md](./02-scoping-document.md) | Detailed scoping document with systems, clauses, and timeline |
| 03 | [03-document-request-list.md](./03-document-request-list.md) | Information and evidence request list issued to FI |
| 04 | [04-audit-work-programme.md](./04-audit-work-programme.md) | Detailed test procedures mapped to RMIT controls |
| 05 | [05-interview-schedule.md](./05-interview-schedule.md) | Interview plan with FI personnel and stakeholders |
| 06 | [06-evidence-tracker.md](./06-evidence-tracker.md) | Evidence collection log and status tracker |
| 07 | [07-working-papers.md](./07-working-papers.md) | Sample working papers with test results |
| 08 | [08-findings-register.md](./08-findings-register.md) | Consolidated findings with risk ratings and recommendations |
| 09 | [09-risk-assessment-report.md](./09-risk-assessment-report.md) | Final report in Appendix 7 Part A format |
| 10 | [10-confirmation-letter.md](./10-confirmation-letter.md) | Confirmation letter to BNM (Appendix 7 Part B) |
| 11 | [11-board-deliberation-pack.md](./11-board-deliberation-pack.md) | Board deliberation pack for BRTC |
| 12 | [12-appendix-7-part-d-attestation.md](./12-appendix-7-part-d-attestation.md) | Part D negative attestation |
| 13 | [13-remediation-tracker.md](./13-remediation-tracker.md) | Post-report remediation tracker |

---

## Engagement Lifecycle

The files map to the following phases of the IESP engagement:

```
Phase 1: ENGAGEMENT SETUP (Week 1–2)
├── 01-engagement-letter.md        Formalise terms, scope, fees
├── 02-scoping-document.md         Define boundaries, map RMIT clauses
└── 03-document-request-list.md    Request evidence from FI

Phase 2: FIELDWORK PREPARATION (Week 2–3)
├── 04-audit-work-programme.md     Design test procedures
└── 05-interview-schedule.md       Plan stakeholder interviews

Phase 3: FIELDWORK EXECUTION (Week 3–7)
├── 06-evidence-tracker.md         Track evidence receipt and gaps
└── 07-working-papers.md           Document test execution and results

Phase 4: REPORTING (Week 7–9)
├── 08-findings-register.md                Consolidate and rate findings
├── 09-risk-assessment-report.md           Draft and finalise Part A report
└── 12-appendix-7-part-d-attestation.md    Part D negative attestation

Phase 5: FINALISATION (Week 9–10)
├── 10-confirmation-letter.md              FI confirmation to BNM (Part B)
├── 11-board-deliberation-pack.md          Board deliberation pack for BRTC
└── 13-remediation-tracker.md              Post-report remediation tracking
```

---

## How to Use This Example

1. **Read sequentially** — The files are numbered in the order they would typically be produced during a real engagement. Start with this README, then proceed through 01 to 13.

2. **Cross-reference with templates** — Each example file is based on a corresponding template in `/templates/`. Compare the filled-in example against the blank template to understand what information is required.

3. **Understand the "why"** — Each file includes commentary explaining why certain decisions were made (e.g., why specific RMIT clauses apply, why certain items are out of scope).

4. **Adapt to your context** — This example covers a cloud migration scenario. The structure and approach are transferable to other IESP engagement types (DCRA, NRA, AI assessments) with appropriate modifications.

5. **Remember the disclaimers** — This is an educational illustration. Real engagements require professional judgement, current regulatory knowledge, and adaptation to the specific FI's circumstances.
