# BNM RMiT — Independent External Service Provider (IESP) Toolkit

**Practitioner's toolkit for conducting Independent External Service Provider reviews under the BNM Risk Management in Technology (RMiT) Policy Document, November 2025 edition.**

> **Disclaimer**: This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document and seek professional counsel for compliance decisions.

## What is an IESP Review?

Under BNM RMiT, financial institutions are required to appoint **technically competent external service providers** to conduct independent assessments of their technology infrastructure, cloud services, and emerging technology deployments. These reviews provide assurance that controls are adequate and operating effectively.

## Five Core Engagement Types

| # | Engagement Type | Trigger Clause | Frequency | Scope |
|---|----------------|----------------|-----------|-------|
| 1 | **DCRA** — Data Centre Resilience Assessment | 14.1 | Every 3 years or material change | Paragraphs 10.24–10.28 |
| 2 | **NRA** — Network Resilience Assessment | 14.2 | Every 3 years or material change | Paragraphs 10.36–10.43 |
| 3 | **Cloud Pre-Implementation Review** | 17.1(c) | First-time cloud for critical systems | Appendix 10 |
| 4 | **Emerging Tech Pre-Implementation Review** | 17.1(c) | First-time AI/ML for critical systems | Appendix 9 |
| 5 | **Digital Services Enhancement Assurance** | 16.4, 16.5 | Non-simplified digital service changes | Appendix 7 Part D |

Plus: **Subsequent Cloud/Emerging Tech Notification** (17.2) and **BNM Discretionary Direction** (17.4, 1.4).

## Repository Structure

```
decision-tree/              Decision logic for when IESP is required
  when-iesp-required.md       Flowchart and engagement type guide
  decision-tree.json          Machine-readable decision tree

requirements/               Regulatory requirements by engagement type
  regulatory-requirements.md  All RMIT clauses triggering IESP
  appendix-7-assessment.md    Appendix 7 IESP assessment framework (Parts A–D)
  dcra-requirements.md        DCRA (14.1) requirements
  nra-requirements.md         NRA (14.2) requirements
  cloud-pre-implementation.md Cloud review (17.1) requirements
  emerging-tech-review.md     Emerging tech (17.1, App 9) requirements

scope/                      Scope definition guides
  scoping-methodology.md      How to define IESP scope
  cloud-services.md           Cloud scope (IaaS/PaaS/SaaS, App 10)
  ai-emerging-tech.md         AI/ML scope (App 9)
  data-centre.md              DCRA scope (10.24–10.28)
  network-infrastructure.md   NRA scope (10.36–10.43)
  digital-services.md         Digital services scope (16.4/16.5)

controls/                   Control frameworks for IESP assessment
  control-domains.json        Minimum control domains (App 7 Part D)
  control-mapping.json        Cross-mapping to RMIT, ISO 27001, NIST

audit-work-programs/        Step-by-step review procedures
  awp-appendix-7-part-d.md    Appendix 7 Part D minimum controls AWP (universal)
  awp-dcra.md                 DCRA work program (~30 test steps)
  awp-nra.md                  NRA work program (~30 test steps)
  awp-cloud.md                Cloud IESP work program (~50 test steps)
  awp-ai-emerging-tech.md     AI/Emerging tech work program (~20 test steps)
  awp-digital-services.md     Digital services work program (~25 test steps)

templates/                  Engagement and reporting templates
  engagement-letter.md        IESP engagement letter
  scoping-document.md         Scope definition template
  risk-assessment-report.md   App 7 Part A format
  confirmation-letter.md      App 7 Part B format
  findings-report.md          IESP findings report
  management-representation.md  Management rep letter
  board-deliberation-pack.md  Board presentation pack

evidence/                   Evidence collection guides
  evidence-requirements.md    Evidence overview by engagement type
  evidence-checklist-dcra.md  DCRA evidence checklist
  evidence-checklist-nra.md   NRA evidence checklist
  evidence-checklist-cloud.md Cloud IESP evidence checklist
  evidence-checklist-ai.md    AI/emerging tech evidence checklist
  evidence-checklist-digital.md  Digital services evidence checklist

examples/                   Worked examples with fictitious data
  bank-perdana-cloud/         Full cloud IESP engagement (14 files, kick-off to board resolution)

artifacts/                  Structured data
  clause-map.json             IESP ↔ RMIT clause bidirectional map
  inventory.json              All artifacts inventory

source/                     Reference materials
  pd-rmit-nov25.pdf           Original BNM policy document
```

## The Compliance Chain

```
BNM RMiT Clause → IESP Engagement Type → Scope Definition → Audit Work Program → Evidence Collection → Findings Report → Board Deliberation
```

This toolkit follows the **GRC Portfolio v2.0 Standardized Schema** from the [RMIT repo](https://github.com/dawuds/RMIT) where possible, enabling cross-referencing between the two repositories.

## Appendix 7 — The IESP Reporting Framework

BNM prescribes a structured reporting framework in Appendix 7:

| Part | Title | Purpose |
|------|-------|---------|
| **Part A** | Risk Assessment Report | 6-section report: FI details, ESP details, application details, tech risk assessment, quality assurance, authorised signatory |
| **Part B** | Format of Confirmation | 9-point attestation by CISO / board chair / senior management confirming readiness |
| **Part C** | Requirements on External Party Assurance | 6 requirements the independent ESP must follow |
| **Part D** | Minimum Controls to be Assessed | Access control, physical security, operations security, communication security, incident management, BCP, online transactions, mobile security |

## Understanding the IESP Conclusion — Effectiveness, Not Compliance

This is one of the most important distinctions for IESP practitioners to understand. **The IESP does not opine on compliance.** The IESP opines on **effectiveness of controls**.

### What BNM Actually Requires

The Appendix 7 Part A report has three conclusion components, each serving a different purpose:

| Component | Where | What the IESP States |
|-----------|-------|---------------------|
| **Technology Risk Assessment** | Section 4 | Assurance on the **effectiveness** of technology risk control and mitigation in meeting Part D expectations |
| **Negative Attestation** | Part C point 5 | Whether **exceptions** were noted against the prescribed risk areas |
| **Overall Recommendation** | Section 5 | The IESP's recommendation on whether to proceed |

### 1. Effectiveness — Not Compliance

BNM's exact wording (Appendix 7, Section 4):

> *"Technology risk assessment shall provide assurance on the **effectiveness** of technology risk control and mitigation performed by the financial institution in meeting expectations outlined in Part D of this Appendix and paragraph 17.1 (for cloud services and emerging technology)."*

**Why this matters:** "Compliance" asks *"does the FI follow the rules?"* — that is the FI's own responsibility and BNM's supervisory role. "Effectiveness" asks *"do the FI's controls actually work to mitigate technology risk?"* — that is what the IESP assesses.

| Rating | Meaning | When to Use |
|--------|---------|-------------|
| **Effective** | Controls are adequately designed and operating effectively to mitigate technology risk in the assessed areas | All Part D control areas meet expectations; no material exceptions |
| **Partially Effective** | Controls are in place but have gaps that reduce their ability to mitigate technology risk | Some Part D areas meet expectations, others have material gaps; exceptions noted |
| **Ineffective** | Controls are absent, poorly designed, or not operating in a manner that mitigates technology risk | Fundamental control failures across multiple Part D areas; significant exceptions |

**Example — Effective:**
> *"Based on our assessment, the technology risk controls implemented by [FI] for cloud identity and access management are effective in meeting the expectations outlined in Appendix 7 Part D Item 1(a). Access controls are adequately designed with least-privilege enforcement, multi-factor authentication, and regular access reviews."*

**Example — Partially Effective:**
> *"Based on our assessment, the technology risk controls implemented by [FI] for cloud identity and access management are partially effective. While multi-factor authentication is enforced for interactive access, we noted overly permissive IAM policies for 4 service accounts and root account usage for non-emergency purposes (Finding F-001). These gaps reduce the effectiveness of access controls in mitigating unauthorised access risk."*

**Example — Ineffective:**
> *"Based on our assessment, the technology risk controls for cloud identity and access management are ineffective. No centralised IAM governance exists, privileged access is not managed through a PAM solution, access reviews have not been conducted, and multiple accounts have unrestricted administrative privileges without MFA."*

### 2. Negative Attestation — What It Means

BNM's exact wording (Part C point 5):

> *"The Risk Assessment Report shall confirm there is no exception noted based on the prescribed risk areas (Negative attestation)."*

A **negative attestation** is a specific form of professional assurance. Instead of the IESP positively stating *"the controls are adequate"*, the IESP states *"nothing has come to our attention that indicates the controls do not meet expectations"* — or identifies specific exceptions where they do.

There are three possible outcomes:

#### Option A — Clean (No Exceptions)

> *"Based on our assessment of the technology risk controls implemented by [FI] against the prescribed risk areas in Appendix 7 Part D and paragraph 17.1, nothing has come to our attention that causes us to believe that the controls are not effective in meeting the expectations outlined therein. No exceptions were noted."*

**When to use:** All Part D control areas assessed as Effective. No material findings. This is the ideal outcome but relatively uncommon for first-time engagements.

#### Option B — With Exceptions

> *"Based on our assessment of the technology risk controls implemented by [FI] against the prescribed risk areas in Appendix 7 Part D and paragraph 17.1, nothing has come to our attention that causes us to believe that the controls are not effective, except for the following areas where exceptions were noted:*
>
> *1. Part D Item 1(a) — Access Control: Overly permissive IAM policies and root account usage gaps (Finding F-001, rated High)*
> *2. Part D Item 1(e) — Incident Management: Incomplete cloud audit logging and SIEM integration (Finding F-002, rated High)*
> *3. Appendix 10 Part B Area 13 — Exit Strategy: Untested and incomplete cloud exit strategy (Finding F-003, rated High)*
>
> *These exceptions should be remediated prior to production deployment. Subject to satisfactory remediation of the above, the overall control environment is expected to meet Part D expectations."*

**When to use:** Most Part D areas are Effective but material exceptions exist. This is the most common real-world outcome — the FI has done reasonable work but gaps remain.

#### Option C — Adverse

> *"Based on our assessment, we are unable to confirm that the technology risk controls implemented by [FI] meet the expectations outlined in Appendix 7 Part D and paragraph 17.1. Material exceptions were noted across multiple prescribed risk areas, including [list areas]. In our assessment, the control environment is not effective in mitigating technology risk in its current state. We recommend that the FI defer the planned deployment until the identified control gaps are remediated and independently re-assessed."*

**When to use:** Fundamental control failures across multiple areas. The IESP cannot support the FI proceeding. This is rare but must be issued when warranted — the IESP's professional obligation overrides commercial considerations.

### 3. Overall Recommendation (Section 5)

This is the IESP's recommendation to the FI's board and to BNM. It is separate from the negative attestation and provides actionable guidance:

| Recommendation | Meaning | Typical Scenario |
|---------------|---------|-----------------|
| **Recommend** | Proceed with deployment/launch | Option A attestation; no material findings |
| **Recommend with Conditions** | Proceed, but specific conditions must be met before/after go-live | Option B attestation; high findings that are remediable within a reasonable timeframe |
| **Do Not Recommend** | Do not proceed until fundamental gaps are addressed | Option C attestation; control environment is not ready |

**Example — Recommend with Conditions:**
> *"We recommend that Bank Perdana Berhad proceed with the cloud migration of Temenos T24 to AWS, subject to the following conditions:*
> *1. Remediate Finding F-001 (IAM governance gaps) prior to production go-live*
> *2. Complete SIEM integration for all cloud log sources per Finding F-002 prior to production go-live*
> *3. Enhance and test the cloud exit strategy per Finding F-003 within 90 days of production go-live"*

### How These Three Components Work Together

```
Section 4: Technology Risk Assessment
  → Per-area effectiveness ratings for each Part D control area
  → Identifies WHERE controls are effective / partially effective / ineffective

Part C.5: Negative Attestation
  → Formal attestation statement with or without exceptions
  → Identifies WHAT exceptions exist against prescribed risk areas

Section 5: Overall Recommendation
  → Actionable recommendation (Recommend / Recommend with Conditions / Do Not Recommend)
  → Identifies WHAT SHOULD HAPPEN next — conditions, timelines, actions
```

The board and BNM read all three together. A "Partially Effective" assessment with "Option B — Exceptions Noted" and "Recommend with Conditions" gives a complete picture: controls mostly work, specific gaps exist, and here's what must be done.

### Common Mistakes to Avoid

| Mistake | Why It's Wrong | Correct Approach |
|---------|---------------|-----------------|
| Concluding "Compliant" or "Non-compliant" | The IESP assesses effectiveness, not compliance. Compliance is BNM's determination | Use "Effective / Partially Effective / Ineffective" |
| Issuing a clean attestation despite material findings | Undermines the integrity of the negative attestation and the IESP's independence | If material findings exist, use Option B or C |
| Using "Pass/Fail" as the overall conclusion | Oversimplifies the assessment; BNM expects nuanced assurance | Rate effectiveness per control area; use negative attestation with specific exceptions |
| Conflating the negative attestation with the recommendation | These serve different purposes — one is a statement of fact, the other is professional advice | Keep them separate: attestation states what was found; recommendation states what should happen |
| Rating everything "Effective" to satisfy the FI | Professional obligation requires honest assessment; BNM reviews these reports | Rate based on evidence; document the basis for each rating |

### For a Worked Example

See [examples/bank-perdana-cloud/](examples/bank-perdana-cloud/) for a complete end-to-end example showing how effectiveness ratings, negative attestation, and the overall recommendation are applied in practice across all engagement documents.

---

## How to Use This Toolkit

### For engagement planning:
1. Start with the [Decision Tree](decision-tree/when-iesp-required.md) to confirm IESP is required
2. Review the relevant [Requirements](requirements/) document
3. Define scope using the [Scope Guide](scope/scoping-methodology.md) and engagement-specific scope document
4. Issue the [Engagement Letter](templates/engagement-letter.md)

### For executing the review:
5. Follow the relevant [Audit Work Program](audit-work-programs/) step-by-step
6. Collect evidence per the [Evidence Checklist](evidence/)
7. Document findings in the [Findings Report](templates/findings-report.md)

### For reporting:
8. Complete the [Risk Assessment Report](templates/risk-assessment-report.md) (App 7 Part A)
9. Obtain the [Confirmation Letter](templates/confirmation-letter.md) (App 7 Part B)
10. Prepare the [Board Deliberation Pack](templates/board-deliberation-pack.md)

## Related Repository

- **[RMIT Compliance Database](https://github.com/dawuds/RMIT)** — Full 121-clause structured extraction of BNM RMiT with controls, evidence, and 365 document templates

## Technical Details

- **Source Document:** BNM/RH/PD 028-98, issued 28 November 2025
- **Applicable to:** Licensed banks, investment banks, Islamic banks, insurers, takaful operators, prescribed DFIs, e-money issuers, payment system operators, merchant acquirers, IRIs
- **Schema Version:** GRC Portfolio v2.0 (compatible with RMIT repo)

## License

CC-BY-4.0
