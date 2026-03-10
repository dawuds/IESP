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

controls/                   Control frameworks for IESP assessment
  control-domains.json        Minimum control domains (App 7 Part D)
  control-mapping.json        Cross-mapping to RMIT, ISO 27001, NIST

audit-work-programs/        Step-by-step review procedures
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
