> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative.

---

# Board Deliberation Pack

## IESP Assessment Results — Cloud Core Banking Migration

---

**Confidential — Board/Committee Use Only**

**Financial Institution:** Bank Perdana Berhad

**Board Committee:** Board Risk and Technology Committee (BRTC)

**Meeting Date:** 10 March 2026

**Agenda Item:** 5.2 — IESP Assessment Results: T24 Cloud Migration

**Prepared by:** Puan Faridah binti Hassan, Chief Information Security Officer

**Date Prepared:** 8 March 2026

---

## 1. Executive Summary

### 1.1 Purpose

This paper presents the results of the Independent External Service Provider (IESP) assessment of Bank Perdana Berhad's migration of its core banking system (Temenos T24/Transact R23) to Amazon Web Services (AWS) public cloud for the BRTC's deliberation, in accordance with paragraph 8.3 of the RMIT (November 2025).

### 1.2 Regulatory Basis

Under paragraph 8.3 of the RMIT, the Board and senior management are required to deliberate on the findings and recommendations of IESP assessments. As the BRTC is the designated Board-level committee responsible for technology risk oversight, the Committee is requested to review the assessment results, approve the remediation plan, and determine the conditions under which the Bank may proceed with the production go-live.

### 1.3 IESP Details

| Attribute | Detail |
|-----------|--------|
| ESP Name | CyberAssure Advisory Sdn Bhd |
| Engagement Lead | Puan Siti Nabilah binti Mohd Yusof (CISA, CCSP, CISSP) |
| Engagement Type | Cloud Pre-Implementation Technology Risk Assessment (Paragraph 17.1) |
| Assessment Period | 6 January to 7 March 2026 |
| Report Date | 7 March 2026 |
| Report Reference | CA/IESP/2026/BPB-001/RAR |

### 1.4 Overall Assessment Result

**Overall Rating: Partially Effective**

**IESP Recommendation: Recommend with Conditions**

The IESP has determined that the Bank's technology risk management controls for the cloud migration are partially effective. The majority of the 21 assessed areas are effective, but three areas — identity and access management, security operations/audit logging, and technology exit strategy — require significant improvement. The IESP recommends proceeding with the migration subject to remediation of three High-rated findings before the May 2026 go-live date.

---

## 2. Assessment Results

### 2.1 Scope of Assessment

The assessment covered:

- **System:** Temenos T24/Transact R23 on AWS (EC2, RDS Aurora, EKS, S3, CloudFront, Direct Connect)
- **RMIT Requirements:** Paragraph 17.1, Appendix 7 Part D, Appendix 10 (all 21 areas)
- **Period:** 6 January to 7 March 2026
- **Evidence:** 87 documents reviewed, 22 interviews conducted, technical testing performed

### 2.2 Assessment Results by Control Area

| # | Control Area | Rating | Findings |
|---|-------------|--------|----------|
| 1 | Technology Risk Governance | Effective | — |
| 2 | Technology Risk Management Framework | Effective | — |
| 3 | Technology Operations Management | Effective | F-005 (M) |
| 4 | Technology Project Management | Effective | — |
| 5 | Security Operations | **Partially Effective** | F-002 (H), F-007 (M) |
| 6 | Identity and Access Management | **Partially Effective** | F-001 (H) |
| 7 | Cryptographic Controls | Effective | F-008 (L) |
| 8 | Network Security | Effective | — |
| 9 | Application Security | Effective | F-010 (L) |
| 10 | Data Security and Privacy | Effective | — |
| 11 | Technology Audit Logging | **Partially Effective** | F-002 (H) |
| 12 | Vulnerability Management | Effective | F-004 (M) |
| 13 | Patch Management | Effective | — |
| 14 | Change Management | Effective | F-005 (M) |
| 15 | Capacity Management | Effective | — |
| 16 | Incident Management | **Partially Effective** | F-007 (M) |
| 17 | Business Continuity Management | Effective | F-006 (M) |
| 18 | Cloud Service Provider Management | Effective | — |
| 19 | Technology Outsourcing | Effective | — |
| 20 | Technology Exit Strategy | **Partially Effective** | F-003 (H) |
| 21 | Emerging Technology Risk | Effective | F-011 (L) |

### 2.3 Comparison with Prior Assessment

This is the first IESP assessment for BPB's cloud infrastructure. No prior assessment baseline exists for comparison. A follow-up assessment is recommended for Q1 2027 to verify remediation effectiveness and assess the matured operational environment.

---

## 3. Key Findings and Risk Ratings

### 3.1 Summary of Findings

| Severity | Count | Percentage |
|----------|-------|-----------|
| Critical | 0 | 0% |
| High | 3 | 27% |
| Medium | 5 | 46% |
| Low | 3 | 27% |
| **Total** | **11** | **100%** |

### 3.2 High Findings — Requiring BRTC Attention

#### Finding F-001: Excessive IAM Permissions and Stale Service Accounts — High

| Attribute | Detail |
|-----------|--------|
| **RMIT Reference** | Appendix 7 Part D Item 1(a); Appendix 10 Area 6 |
| **Description** | Four of twelve IAM roles assigned to the T24 application layer have broader permissions than required. Specifically, some roles have unrestricted access to all S3 buckets rather than only the T24 data bucket. Additionally, three service accounts from the proof-of-concept phase (July 2025) remain active with administrative permissions despite having no activity for over 90 days. |
| **Risk/Impact** | In a cloud environment, excessive permissions can be exploited rapidly — a compromised application role with unrestricted S3 access could lead to unauthorised access to customer data across all storage buckets. Stale privileged accounts are a common attack vector in cloud breaches. The Bank's exposure is heightened given that customer financial data is stored in the affected S3 buckets. |
| **Management Response** | IAM Access Analyzer deployed. Two of four policies rescoped. Stale accounts disabled. Full remediation by 15 April 2026. |
| **Proposed Timeline** | 15 April 2026 (before go-live) |

#### Finding F-002: Insufficient Audit Logging Configuration — High

| Attribute | Detail |
|-----------|--------|
| **RMIT Reference** | Appendix 7 Part D Item 1(e); Appendix 10 Areas 5, 11 |
| **Description** | The Bank's cloud audit logging has three gaps: (i) CloudTrail captures management events but not S3 data-access events, meaning the Bank cannot track who accessed or downloaded customer data stored in S3; (ii) Amazon GuardDuty — the primary cloud threat detection service — is not enabled in the disaster recovery region, leaving the Bank without threat detection capability during a DR failover; and (iii) SIEM integration is 75% complete, with EKS audit logs and Lambda function logs not yet ingested. |
| **Risk/Impact** | Without S3 data-event logging, a data exfiltration incident may go undetected or be uninvestigable. The absence of GuardDuty in the DR region means that during a disaster recovery scenario — when the Bank is already under stress — it would have no automated threat detection. These gaps directly affect the Bank's ability to meet BNM's expectations for security monitoring under paragraph 11.3 of the RMIT. |
| **Management Response** | S3 data events enabled 6 Mar 2026. GuardDuty DR region enablement scheduled 12 Mar 2026. SIEM integration target: 31 Mar 2026. |
| **Proposed Timeline** | 31 March 2026 (before go-live) |

#### Finding F-003: Untested Cloud Exit Strategy — High

| Attribute | Detail |
|-----------|--------|
| **RMIT Reference** | Appendix 10 Area 20 |
| **Description** | The Bank has documented a cloud exit strategy that outlines scenarios for migrating away from AWS, but the strategy has not been tested. There is no validated procedure for extracting all data from AWS, no cost estimate for an exit, and no confirmed timeline for how long an exit would take. For a Tier 1 critical system with customer data hosted in a foreign jurisdiction (Singapore), this represents a significant gap in the Bank's ability to demonstrate control over its technology destiny. |
| **Risk/Impact** | Without a tested exit strategy, the Bank may face vendor lock-in risk. In a scenario where the AWS relationship must be terminated — whether due to regulatory directive, contractual dispute, or service degradation — the Bank may be unable to execute a timely and orderly migration. The absence of a cost estimate also means the Board cannot make an informed assessment of the total cost of the cloud strategy. |
| **Management Response** | Exit strategy test to be conducted post go-live. Target: April 2026. Will include data extraction test, portability validation, cost modelling, and timeline estimation. |
| **Proposed Timeline** | 30 April 2026 |

### 3.3 Medium and Low Findings Summary

| # | Finding ID | Title | Rating | RMIT Area | Management Response | Target Date |
|---|-----------|-------|--------|-----------|-------------------|-------------|
| 1 | F-004 | CSPM tool not deployed | Medium | App 10 Area 12 | Agreed — Wiz evaluation in progress | Apr 2026 |
| 2 | F-005 | IaC drift detection not automated | Medium | App 10 Area 14 | Agreed — Terraform Cloud trial started | Apr 2026 |
| 3 | F-006 | DR test initially exceeded RTO | Medium | App 10 Area 17 | Agreed — remediation test passed 28 Feb | Completed |
| 4 | F-007 | Incomplete cloud incident playbooks | Medium | App 10 Area 16 | Agreed — 2/3 playbooks in draft | Mar 2026 |
| 5 | F-009 | Cloud skills gap in CoE | Medium | App 10 Area 15 | Agreed — training plan approved | Dec 2026 |
| 6 | F-008 | Manual key rotation | Low | App 10 Area 7 | Agreed — auto-rotation enabled 25 Feb | Completed |
| 7 | F-010 | Container image scanning gap | Low | App 10 Area 9 | Agreed — Trivy evaluation in progress | Q2 2026 |
| 8 | F-011 | Cloud cost optimisation review pending | Low | App 10 Area 21 | Agreed — planned post go-live | Q2 2026 |

### 3.4 Key Themes

The IESP assessment identified the following key themes across the findings:

1. **Cloud security maturity gap:** While the Bank has invested significantly in cloud security architecture, operational security processes (IAM governance, logging completeness, incident playbooks) have not yet matured to match the sophistication of the technical controls. This is typical for organisations undertaking their first major cloud migration.

2. **Pre-production vs. production readiness:** Several gaps (stale PoC accounts, incomplete SIEM integration, missing CSPM) reflect the transition from a project/build phase to an operational/run phase. These need to be closed before go-live.

3. **Exit strategy as strategic assurance:** The untested exit strategy is not a day-to-day operational risk but is a strategic risk that the Board should monitor. It provides assurance that the Bank retains control over its technology platform choices.

---

## 4. Remediation Plan and Timeline

### 4.1 Remediation Plan Summary

| # | Finding | Rating | Remediation Action | Owner | Start Date | Target Date | Status |
|---|---------|--------|--------------------|-------|-----------|-------------|--------|
| 1 | F-001 | High | Rescope IAM policies to least privilege; remove stale accounts; implement quarterly review | Encik Wong Kar Wai, IAM Lead | 3 Mar 2026 | 15 Apr 2026 | In Progress |
| 2 | F-002 | High | Enable S3 data events; enable GuardDuty in DR; complete SIEM integration | Puan Lee Mei Ling, SOC Manager | 6 Mar 2026 | 31 Mar 2026 | In Progress |
| 3 | F-003 | High | Conduct exit strategy test; prepare cost estimate; validate data portability | Encik Raj Kumar, Head of Cloud Engineering | 1 Apr 2026 | 30 Apr 2026 | Not Started |
| 4 | F-004 | Medium | Deploy Wiz CSPM for continuous cloud posture monitoring | Encik Raj Kumar, Head of Cloud Engineering | 15 Mar 2026 | 30 Apr 2026 | Not Started |
| 5 | F-005 | Medium | Implement Terraform Cloud with automated drift detection | Encik David Lim, DevOps Lead | 1 Mar 2026 | 30 Apr 2026 | In Progress |
| 6 | F-006 | Medium | Conduct additional DR test; implement automated DR orchestration | Encik Mohd Faisal, Head of BCM | 28 Feb 2026 | 25 Mar 2026 | Completed |
| 7 | F-007 | Medium | Complete and test 3 cloud incident playbooks | Puan Lee Mei Ling, SOC Manager | 1 Mar 2026 | 20 Mar 2026 | In Progress |
| 8 | F-008 | Low | Enable KMS automatic key rotation | Encik Tan Chee Keong, DBA Lead | 25 Feb 2026 | 25 Feb 2026 | Completed |
| 9 | F-009 | Medium | Execute CoE training plan (AWS certifications) | Encik Raj Kumar, Head of Cloud Engineering | 1 Mar 2026 | 31 Dec 2026 | In Progress |
| 10 | F-010 | Low | Integrate Trivy container image scanning into CI/CD pipeline | Encik David Lim, DevOps Lead | 1 Apr 2026 | 30 Jun 2026 | Not Started |
| 11 | F-011 | Low | Conduct cloud cost optimisation review; deploy AWS Cost Anomaly Detection | Encik Raj Kumar, Head of Cloud Engineering | 1 May 2026 | 30 Jun 2026 | Not Started |

### 4.2 Resource Requirements

| Resource Type | Description | Estimated Cost (RM) | Funding Source |
|--------------|-------------|---------------------|---------------|
| Technology — CSPM | Wiz platform licence (annual) | 480,000 | IT Security Budget FY2026 |
| Technology — IaC | Terraform Cloud Team licence (annual) | 85,000 | Cloud Operations Budget FY2026 |
| Technology — Container Security | Trivy Enterprise licence (annual) | 60,000 | IT Security Budget FY2026 |
| Professional Services | IESP follow-up assessment (Q1 2027) | 150,000 | IT Audit Budget FY2027 |
| Training | AWS certification programme (8 staff) | 120,000 | HR Training Budget FY2026 |
| Professional Services | Exit strategy test (consulting support) | 180,000 | Cloud Migration Programme |
| Internal Resources | Staff effort for remediation (estimated 4 FTE-months) | 125,000 | Absorbed within existing headcount |
| **Total** | | **1,200,000** | |

### 4.3 Dependencies and Risks to Remediation

| # | Dependency/Risk | Impact | Mitigation |
|---|----------------|--------|-----------|
| 1 | Wiz procurement timeline | Delays to F-004 remediation | Begin procurement immediately; AWS Security Hub as interim measure |
| 2 | SIEM vendor capacity for log integration | Delays to F-002 SIEM component | Escalated with vendor; dedicated resource assigned |
| 3 | Staff availability for exit strategy test | F-003 timeline at risk if CoE diverted to go-live preparation | Dedicated 2-person team assigned; ring-fenced from go-live activities |

### 4.4 Monitoring and Reporting

- Remediation progress will be reported to the BRTC on a monthly basis until all High findings are closed.
- Management will provide a status update at the next BRTC meeting on 14 April 2026.
- Internal Audit will perform an independent verification of the three High finding remediations before sign-off.
- A follow-up IESP assessment is planned for Q1 2027 to provide assurance on the matured operational environment.

---

## 5. Recommendation for Board Action

### 5.1 Management Recommendation

Management recommends that the BRTC:

1. **Note** the results of the IESP assessment conducted by CyberAssure Advisory Sdn Bhd, including the overall rating of "Partially Effective" and the recommendation of "Recommend with Conditions."

2. **Approve** the migration to production, subject to the following conditions:
   - All three High-rated findings (F-001, F-002, F-003) must be remediated and verified by the IESP or Internal Audit before the May 2026 go-live date.
   - Evidence of remediation must be presented to the BRTC before production deployment is authorised.

3. **Approve** the remediation plan and timeline as set out in Section 4, including the estimated budget of RM1.2 million.

4. **Direct** management to:
   - Implement all remediation actions within the agreed timelines
   - Report remediation progress to the BRTC on a monthly basis
   - Ensure no production go-live occurs until the three conditions are verified as met
   - Engage CyberAssure Advisory for a follow-up IESP assessment in Q1 2027

5. **Approve** the submission of the Confirmation Letter (Appendix 7 Part B) to Bank Negara Malaysia, to be signed by the BRTC Chairman and CTO.

### 5.2 Conditions Imposed by the IESP

The IESP's recommendation of "Recommend with Conditions" requires that the following conditions be met:

| # | Condition | Required Completion | Status |
|---|-----------|-------------------|--------|
| 1 | Remediate all excessive IAM permissions and implement automated stale account lifecycle management (F-001) | 30 April 2026 | In Progress |
| 2 | Enable comprehensive audit logging including S3 data events, GuardDuty in DR region, and complete SIEM integration (F-002) | 30 April 2026 | In Progress |
| 3 | Conduct a full exit strategy test including data extraction, portability validation, and cost estimation (F-003) | 30 April 2026 | Not Started |

---

## 6. Supporting Documents

The following documents are available for the Committee's reference:

| # | Document | Reference | Classification |
|---|----------|-----------|---------------|
| 1 | IESP Risk Assessment Report (Appendix 7 Part A) | CA/IESP/2026/BPB-001/RAR | Confidential |
| 2 | IESP Part D Attestation | CA/IESP/2026/BPB-001/PDA | Confidential |
| 3 | IESP Detailed Findings Register | CA/IESP/2026/BPB-001/FR | Confidential |
| 4 | Confirmation Letter — Draft (Appendix 7 Part B) | BPB/BRTC/2026/CL-001 | Confidential |
| 5 | Remediation Plan (detailed) | BPB/IT/2026/RP-001 | Confidential |
| 6 | Remediation Tracker (as at 10 March 2026) | BPB/IT/2026/RT-001 | Confidential |

---

## 7. Board Committee Resolution

**Resolution:**

The Board Risk and Technology Committee, having reviewed and deliberated on the IESP assessment results for the migration of the core banking system (Temenos T24/Transact R23) to Amazon Web Services:

- [x] Notes the IESP assessment results, including the overall rating of "Partially Effective" and the recommendation of "Recommend with Conditions"
- [x] Approves the migration to production, subject to remediation and verification of all three High-rated findings (F-001, F-002, F-003) before the May 2026 go-live date
- [x] Approves the remediation plan, timeline, and estimated budget of RM1.2 million
- [x] Directs management to report remediation progress to the BRTC monthly and to ensure no production go-live occurs until conditions are verified
- [x] Approves the submission of the Confirmation Letter (Appendix 7 Part B) to Bank Negara Malaysia
- [x] Requires a follow-up IESP assessment in Q1 2027

**Conditions/Directions:**

Production go-live is conditional upon written confirmation from the CISO and Internal Audit that all three High-rated findings have been remediated. The BRTC will convene a special session if required to review remediation evidence before go-live authorisation.

| | |
|---|---|
| **Committee Chairman** | Tan Sri Dato' Mohamad Ibrahim bin Abdul Rahman |
| **Signature** | *[Signed]* |
| **Date** | 10 March 2026 |

---

**Minutes Reference:** BRTC/2026/M03-5.2
