# IESP Evidence Folder Structure

Standard folder structure for organising audit evidence during BNM RMiT IESP engagements. Created by `create-evidence-structure.sh`.

## Folder Reference

### 00-Engagement-Admin

Administrative documents that establish the engagement.

| Subfolder | Contents |
|-----------|----------|
| `engagement-letter/` | Signed engagement letter, scope amendments, fee proposals |
| `independence-declaration/` | Independence and conflict-of-interest declarations for each team member |
| `team-qualifications/` | CVs, certifications (CISA, CISSP, ISO 27001 LA), and competency evidence |

### 01-Planning

Pre-fieldwork planning artefacts.

| Subfolder | Contents |
|-----------|----------|
| `prior-reports/` | Previous IESP reports, internal audit reports, BNM examination findings |
| `scoping-memo/` | Engagement scoping memo defining systems, timeframe, and assessment boundaries |
| `document-request-list/` | Initial and follow-up document request lists sent to the financial institution |

### 02-Scoping

Evidence that supports scoping decisions.

| Subfolder | Contents |
|-----------|----------|
| `platform-inventory/` | Inventory of platforms, cloud tenants, and infrastructure in scope |
| `critical-systems-inventory/` | Critical systems classification and dependency mapping |
| `sampling-methodology/` | Sampling approach, sample sizes, and selection rationale |

### 03-Evidence-Governance

Governance evidence aligned to **Appendix 10 Part A** (governance domains) and **Appendix 9 Domain 1-3** (strategy, governance, risk).

| Subfolder | Contents | AWP Cross-Ref |
|-----------|----------|---------------|
| `strategy/` | Technology strategy, cloud strategy, digital transformation roadmap | GOV-01 to GOV-03 |
| `policies/` | IT policies, security policies, acceptable use, data classification | GOV-04 to GOV-08 |
| `risk-assessment/` | IT risk register, risk assessment methodology, risk appetite statements | GOV-09 to GOV-12 |
| `roles-responsibilities/` | RACI matrices, org charts, job descriptions for key IT/security roles | GOV-13 to GOV-15 |
| `competency/` | Training records, awareness programmes, skills gap assessments | GOV-16 to GOV-18 |
| `compliance-mapping/` | Regulatory compliance mapping (RMiT, BNM guidelines, PDPA, etc.) | GOV-19 to GOV-21 |
| `oversight/` | Board/committee minutes, management oversight reports, KRI dashboards | GOV-22 to GOV-25 |

### 04-Evidence-Controls

Technical controls evidence aligned to **Appendix 10 Part B** (technology controls) and **Appendix 9 Domain 4-5**.

| Subfolder | Contents | AWP Cross-Ref |
|-----------|----------|---------------|
| `architecture/` | Architecture diagrams, design documents, technology standards | CLD-01 to CLD-05 |
| `identity-access-management/` | IAM policies, access reviews, privileged access management, MFA configs | CLD-06 to CLD-12 |
| `data-protection/` | Encryption standards, DLP configs, data classification, key management | CLD-13 to CLD-18 |
| `network-security/` | Firewall rules, network diagrams, segmentation evidence, WAF configs | CLD-19 to CLD-24 |
| `compute-security/` | Hardening standards, patching evidence, container security, image scanning | CLD-25 to CLD-30 |
| `storage-security/` | Storage encryption, backup configs, retention policies | CLD-31 to CLD-34 |
| `logging-monitoring/` | SIEM configs, log retention, alerting rules, SOC procedures | CLD-35 to CLD-40 |
| `vulnerability-management/` | Vulnerability scans, penetration test reports, remediation tracking | CLD-41 to CLD-46 |
| `change-management/` | Change management policy, CAB records, deployment evidence | CLD-47 to CLD-50 |
| `incident-response/` | IR plan, IR drill reports, incident logs, escalation matrices | CLD-51 to CLD-55 |
| `business-continuity/` | BCP/DR plans, RTO/RPO documentation, DR test results | CLD-56 to CLD-60 |
| `vendor-management/` | Vendor risk assessments, SLAs, contract reviews, fourth-party inventory | CLD-61 to CLD-65 |
| `exit-strategy/` | Exit/transition plans, data portability evidence, escrow arrangements | CLD-66 to CLD-68 |
| `regulatory-compliance/` | Regulatory correspondence, compliance attestations, audit certifications | CLD-69 to CLD-72 |

### 05-Evidence-PartD

Evidence for **Appendix 7 Part D** minimum controls. Applies to all IESP engagement types.

| Subfolder | Part D Ref | Contents |
|-----------|-----------|----------|
| `1a-access-control/` | 1(a) | Logical access controls, password policies, access provisioning/deprovisioning |
| `1b-physical-security/` | 1(b) | Physical access logs, CCTV, visitor management, environmental controls |
| `1c-operations-security/` | 1(c) | Operational procedures, capacity management, system acceptance testing |
| `1d-communications-security/` | 1(d) | Network security, email security, data transfer controls |
| `1e-incident-management/` | 1(e) | Incident management procedures, incident logs, escalation records |
| `1f-business-continuity/` | 1(f) | BCP documentation, DR test results, recovery procedures |
| `2a-customer-authentication/` | 2(a) | Customer authentication mechanisms for online financial transactions |
| `2b-transaction-authentication/` | 2(b) | Transaction signing, OTP, biometrics for financial transactions |
| `2c-segregation-of-duties/` | 2(c) | SoD matrices, conflicting-role analysis, compensating controls |
| `2d-data-integrity/` | 2(d) | Data integrity checks, reconciliation evidence, validation controls |
| `2e-mobile-device-risks/` | 2(e) | Mobile device management, app security testing, mobile risk assessment |

### 06-Evidence-DCRA

**DCRA engagements only** (Clause 14.1). Remove this folder for non-DCRA engagements.

| Subfolder | Contents |
|-----------|----------|
| `resilience-objectives/` | Resilience objectives, RTO/RPO targets, availability SLAs |
| `redundancy/` | Redundancy architecture, failover configs, N+1 evidence |
| `physical-security/` | DC physical security, environmental controls, fire suppression |
| `dc-operations/` | DC operational procedures, capacity planning, maintenance records |
| `segregation/` | Logical and physical segregation within the data centre |

### 07-Evidence-NRA

**NRA engagements only** (Clause 14.2). Remove this folder for non-NRA engagements.

| Subfolder | Contents |
|-----------|----------|
| `network-design/` | Network architecture documents, topology diagrams |
| `network-resilience/` | Redundancy configs, failover testing, path diversity evidence |
| `network-monitoring/` | Network monitoring tools, dashboards, alerting configs |
| `network-security/` | Firewall rules, IDS/IPS configs, network access controls |
| `network-blueprint/` | Network blueprint and standards documentation |
| `network-logging/` | Network device logs, NetFlow/sFlow, log retention evidence |
| `network-segmentation/` | VLAN configs, micro-segmentation, zone architecture |

### 08-Working-Papers

Internal working papers produced during the engagement.

| Subfolder | Contents |
|-----------|----------|
| `awp-workbooks/` | Completed AWP workbooks (Excel) with test results populated |
| `sampling-records/` | Sample selections, random number generation records, population data |
| `interview-notes/` | Stakeholder interview notes (dated, attributed) |
| `screenshots/` | Screenshot evidence captured during walkthroughs and demonstrations |

### 09-Findings

Findings lifecycle from draft through to final.

| Subfolder | Contents |
|-----------|----------|
| `draft-findings/` | Draft finding write-ups for review before issuing to management |
| `management-responses/` | Management responses, remediation plans, agreed timelines |
| `final-findings/` | Final findings after incorporating management responses |

### 10-Report

Report drafts and final deliverable.

| Subfolder | Contents |
|-----------|----------|
| `draft-report/` | Draft IESP report for internal review |
| `review-comments/` | Review comments from engagement manager and quality reviewer |
| `final-report/` | Final signed IESP report for submission to the financial institution and BNM |

### 11-Sign-Off

Engagement close-out and attestation.

| Subfolder | Contents |
|-----------|----------|
| `management-sign-off/` | Engagement manager and partner sign-off records |
| `board-presentation/` | Board/committee presentation pack summarising findings |
| `part-c-attestation/` | Appendix 7 Part C confirmation letter (9-point attestation) |

---

## Evidence Naming Convention

All evidence files should follow this pattern:

```
[ControlRef]-[Description].[ext]
```

### Control reference prefixes

| Prefix | Domain | Example |
|--------|--------|---------|
| `GOV-##` | Governance (03-Evidence-Governance) | `GOV-04-information-security-policy.pdf` |
| `CLD-##` | Cloud/Technology Controls (04-Evidence-Controls) | `CLD-12-IAM-policy-review.pdf` |
| `PD-##` | Part D minimum controls (05-Evidence-PartD) | `PD-1a-access-control-matrix.xlsx` |
| `DCRA-##` | DCRA controls (06-Evidence-DCRA) | `DCRA-02-redundancy-architecture.pdf` |
| `NRA-##` | NRA controls (07-Evidence-NRA) | `NRA-05-network-blueprint-2026.pdf` |

### General rules

- Use **kebab-case** for filenames (lowercase, hyphens, no spaces)
- Include the **date** for time-sensitive evidence: `CLD-41-vuln-scan-2026-03-15.pdf`
- Prefix screenshots with **SS-**: `SS-CLD-35-siem-dashboard.png`
- Interview notes use **INT-**: `INT-2026-03-20-CISO-interview.docx`
- Sampling records use **SAM-**: `SAM-CLD-06-access-review-sample.xlsx`

### Version control

For documents with multiple versions, append a version suffix:

```
CLD-12-IAM-policy-review-v1.pdf
CLD-12-IAM-policy-review-v2-final.pdf
```

---

## Engagement Type Applicability

Not all folders are used for every engagement type. The table below shows which evidence sections apply.

| Folder | Cloud Pre-Impl | DCRA | NRA | Digital Services | Emerging Tech | Subsequent | BNM Directed |
|--------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 00-Engagement-Admin | Y | Y | Y | Y | Y | Y | Y |
| 01-Planning | Y | Y | Y | Y | Y | Y | Y |
| 02-Scoping | Y | Y | Y | Y | Y | Y | Y |
| 03-Evidence-Governance | Y | Y | Y | Y | Y | Y | Y |
| 04-Evidence-Controls | Y | - | - | Y | Y | Y | Y |
| 05-Evidence-PartD | Y | Y | Y | Y | Y | Y | Y |
| 06-Evidence-DCRA | - | **Y** | - | - | - | - | * |
| 07-Evidence-NRA | - | - | **Y** | - | - | - | * |
| 08-Working-Papers | Y | Y | Y | Y | Y | Y | Y |
| 09-Findings | Y | Y | Y | Y | Y | Y | Y |
| 10-Report | Y | Y | Y | Y | Y | Y | Y |
| 11-Sign-Off | Y | Y | Y | Y | Y | Y | Y |

**Y** = Required | **-** = Not applicable (remove folder) | **\*** = As directed by BNM

> **Tip:** The script creates all folders. After confirming the engagement type, delete any folders marked "-" above to keep the evidence pack clean.

---

## AWP Workbook Cross-Reference

Each AWP workbook (in `08-Working-Papers/awp-workbooks/`) has an **Evidence Ref** column (Column J) that maps test steps to evidence files. When populating the workbook:

1. Place the evidence file in the correct folder per this structure
2. In Column J of the AWP workbook, enter the **relative path** from the engagement root, e.g.:
   - `04-Evidence-Controls/identity-access-management/CLD-12-IAM-policy-review.pdf`
   - `05-Evidence-PartD/1a-access-control/PD-1a-access-control-matrix.xlsx`
3. If a single piece of evidence supports multiple test steps, reference the same path in each row
4. If no evidence is available for a test step, enter `N/A - [reason]` in Column J

### AWP to folder mapping

| AWP Workbook | Primary Evidence Folders |
|--------------|------------------------|
| `awp-cloud-pre-implementation.xlsx` | 03-Evidence-Governance, 04-Evidence-Controls |
| `awp-dcra.xlsx` | 03-Evidence-Governance, 06-Evidence-DCRA |
| `awp-nra.xlsx` | 03-Evidence-Governance, 07-Evidence-NRA |
| `awp-digital-services.xlsx` | 03-Evidence-Governance, 04-Evidence-Controls |
| `awp-emerging-tech.xlsx` | 03-Evidence-Governance, 04-Evidence-Controls |
| `awp-appendix7-partd.xlsx` | 05-Evidence-PartD |
