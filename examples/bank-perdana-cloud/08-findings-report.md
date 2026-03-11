> **WARNING: AI-GENERATED EXAMPLE -- FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative.

---

**CONFIDENTIAL**

# IESP Findings Report

# Independent Assessment of Cloud Services
# Bank Perdana Berhad -- Temenos T24/Transact R23 Migration to AWS

---

**Report Reference:** CA/IESP/BPB-CLOUD/2026-001-FR

**Financial Institution:** Bank Perdana Berhad ("BPB")

**Cloud Service Provider:** Amazon Web Services (AWS)

**IESP:** CyberAssure Advisory Sdn Bhd

**Engagement Type:** Cloud Services Assessment (RMIT Appendix 10)

**Assessment Period:** 20 January 2026 to 21 February 2026

**Report Date:** 28 February 2026

**Report Status:** Final

---

## Table of Contents

1. Executive Summary
2. Scope and Methodology
3. Summary of Findings
4. Detailed Findings
5. Negative Attestation Statement
6. Appendices

---

## 1. Executive Summary

### 1.1 Background

Bank Perdana Berhad ("BPB") engaged CyberAssure Advisory Sdn Bhd ("CyberAssure") to perform an independent assessment of BPB's migration of its core banking system, Temenos T24/Transact Release 23 ("T24"), to Amazon Web Services ("AWS") in accordance with the Risk Management in Technology (RMIT) Policy Document (November 2025).

BPB commenced its cloud migration programme in Q2 2025, with the T24 production workload going live on AWS ap-southeast-1 (Singapore) region in October 2025. The deployment utilises a combination of Amazon EC2, Amazon RDS (Oracle), Amazon ECS (Fargate), Amazon S3, and supporting services. Disaster recovery is planned for ap-southeast-3 (Jakarta) region.

This assessment was required by Bank Negara Malaysia (BNM) as a condition of BPB's adoption of cloud services for critical systems, pursuant to RMIT paragraphs 10.51 through 10.55 and Appendix 10.

### 1.2 Objective

The objective of this assessment was to:

1. Evaluate the effectiveness of BPB's technology risk management controls for the T24 cloud deployment against the requirements of RMIT Appendix 10 (Cloud Services);
2. Assess BPB's cloud governance, security posture, operational resilience, and exit readiness;
3. Provide a negative attestation on the design and operating effectiveness of cloud-related controls; and
4. Identify findings and recommendations for remediation.

### 1.3 Overall Assessment

**Overall Rating: Partially Effective**

BPB has established a reasonable cloud governance framework and deployed foundational security controls for its T24 migration to AWS. The cloud strategy has Board endorsement, CSP due diligence was thorough, and contractual arrangements broadly address RMIT requirements. However, the assessment identified three High-rated findings relating to identity and access management, cloud audit logging, and exit strategy readiness that require prompt remediation before the control environment can be considered fully effective. Until these are addressed, BPB's cloud deployment carries elevated risk of unauthorised access, incomplete threat detection, and inability to execute a timely exit if required.

**Recommendation: Recommend with Conditions** -- The three High findings (F-001, F-002, F-003) must be remediated within the agreed timelines and verified by CyberAssure before the control environment can be attested as effective without exceptions.

### 1.4 Key Highlights

| Metric | Value |
|--------|-------|
| Total findings | 11 |
| Critical findings | 0 |
| High findings | 3 |
| Medium findings | 5 |
| Low findings | 3 |
| Observations | 0 |
| Control areas assessed | 16 |
| Control areas rated Effective | 8 |
| Control areas rated Partially Effective | 7 |
| Control areas rated Ineffective | 1 |

### 1.5 Key Themes

1. **Identity and Access Governance Gaps:** Overly permissive IAM policies, stale service accounts, and root account misuse indicate that cloud IAM governance has not kept pace with the speed of deployment (F-001).
2. **Incomplete Observability and Detection:** Cloud audit logging is not comprehensive, SIEM integration is partial, and GuardDuty coverage is incomplete, reducing the ability to detect and respond to cloud-specific threats (F-002).
3. **Exit Strategy Immaturity:** The cloud exit strategy remains high-level without actionable procedures, cost estimates, or testing, creating a dependency risk on AWS (F-003).
4. **Operational Readiness Gaps:** Several operational controls -- CSPM, drift detection, DR testing, cloud IR playbooks, and KMS rotation -- are either not deployed or not fully operationalised (F-004 through F-008).
5. **Emerging Capability Maturity:** Container security, DDoS response, and cloud skills training show early-stage maturity that will benefit from structured uplift (F-009 through F-011).

---

## 2. Scope and Methodology

### 2.1 Scope

This assessment covered the following:

**Systems/Infrastructure:**
- Temenos T24/Transact Release 23 deployed on AWS ap-southeast-1 (Singapore)
- AWS accounts: BPB-PROD-001 (Production), BPB-UAT-001 (UAT), BPB-DR-001 (DR -- ap-southeast-3)
- AWS services: EC2, RDS (Oracle), ECS (Fargate), S3, CloudFront, ALB, Route 53, KMS, IAM, CloudTrail, GuardDuty, Security Hub, WAF, Shield Advanced, AWS Backup, Secrets Manager, ACM, VPC, Transit Gateway
- Supporting infrastructure: GitLab CI/CD, Terraform IaC, SIEM (Splunk Cloud)

**RMIT Requirements:**
- RMIT (November 2025) paragraphs 10.51 to 10.55 (Cloud Services)
- RMIT Appendix 10, Part A (Applicability and Scope)
- RMIT Appendix 10, Part B (Control Areas 1-14)
- RMIT Appendix 10, Part D (Minimum Controls)

**Assessment Period:** 20 January 2026 to 21 February 2026

**Fieldwork Period:** 20 January 2026 to 21 February 2026

**Exclusions:**
- Application-level security testing of Temenos T24 software (covered under separate application security assessment)
- BPB's on-premises data centre controls (subject to separate DCRA engagement)
- Non-T24 workloads on AWS (out of scope per engagement letter)

### 2.2 Methodology

The assessment was conducted using the following approach:

1. **Document Review:** Review of 90+ evidence items across 16 control categories mapped to RMIT Appendix 10 (see Appendix A for full evidence list)
2. **Interviews:** 14 interviews conducted with key personnel from BPB (IT, Risk, Compliance, Operations) and AWS (Solutions Architect, TAM)
3. **Walkthroughs:** Process walkthroughs of cloud change management, incident response, backup and recovery, and IAM provisioning/deprovisioning
4. **Technical Review:** Review of AWS IAM policies, security group configurations, CloudTrail settings, KMS key configurations, VPC architecture, and ECS task definitions via console exports and configuration extracts
5. **Automated Scanning:** CIS AWS Foundations Benchmark v3.0 scan via AWS Security Hub (enabled during fieldwork for assessment purposes)
6. **Sample Testing:** Sample-based testing of change tickets (28 changes, Oct-Dec 2025), access review records (Q4 2025), backup restoration (Dec 2025 test), and incident records (Jul 2025 -- Jan 2026)

**Assessment Work Programmes (AWPs) Used:**
- AWP-CLOUD-01: Cloud Governance, Risk, and Compliance (Categories 1-6, 10, 12)
- AWP-CLOUD-02: Cloud Security, Architecture, and Operations (Categories 7-9, 11, 13-16)

### 2.3 Assessment Standards

The assessment was conducted against:
- RMIT (November 2025) -- Appendix 10, Parts A, B, and D
- CIS Amazon Web Services Foundations Benchmark v3.0
- AWS Well-Architected Framework -- Security Pillar (supplementary reference)
- CSA Cloud Controls Matrix v4.0 (supplementary reference)

### 2.4 Risk Rating Definitions

| Rating | Definition |
|--------|-----------|
| **Critical** | Immediate threat to the confidentiality, integrity, or availability of critical systems or data. Regulatory non-compliance with material impact. Requires immediate remediation. |
| **High** | Significant control weakness that could result in material impact to the FI. Requires remediation within 30 days. |
| **Medium** | Moderate control weakness with potential for adverse impact. Requires remediation within 90 days. |
| **Low** | Minor control improvement opportunity with limited risk exposure. Requires remediation within 180 days. |
| **Observation** | Best practice recommendation for management consideration. No immediate risk. |

### 2.5 Limitations

- The assessment was based on evidence provided by BPB and AWS during the fieldwork period. CyberAssure did not perform independent penetration testing or vulnerability scanning of the T24 application or underlying infrastructure.
- AWS console access was provided in read-only mode. Configuration evidence was obtained via exports and screenshots prepared by BPB's Cloud Engineering team.
- The DR account (BPB-DR-001) in ap-southeast-3 was reviewed based on documentation and configuration exports; a physical or logical inspection of the Jakarta region was not performed.
- Management responses were provided by BPB management and have not been independently verified by CyberAssure.

---

## 3. Summary of Findings

### 3.1 Findings by Severity

```
Critical  0
High      3 ██████████████████
Medium    5 ██████████████████████████████
Low       3 ██████████████████
```

### 3.2 Findings Summary Table

| Finding ID | Title | Risk Rating | RMIT Reference | Control Area | Status |
|-----------|-------|-------------|----------------|-------------|--------|
| F-001 | Overly Permissive IAM Policies and Root Account Usage | High | App 10 Part B Area 2 / Part D Item 1(a) | Access Controls | New |
| F-002 | Incomplete Cloud Audit Logging and SIEM Integration | High | App 10 Part B Area 7 / Part D Item 1(e) | Logging and SIEM | New |
| F-003 | Untested and Incomplete Cloud Exit Strategy | High | App 10 Part B Area 13 | Exit Strategy | New |
| F-004 | Cloud Security Posture Management Not Deployed | Medium | App 10 Part B Area 4 / Part D Item 1(b) | Architecture and Security | New |
| F-005 | IaC Drift Detection Not Implemented | Medium | App 10 Part B Area 5 | IaC and Automation | New |
| F-006 | Cloud DR Not Tested End-to-End | Medium | App 10 Part B Area 8 / Part D Item 1(d) | Backup and Recovery | New |
| F-007 | Cloud Incident Response Playbook Incomplete | Medium | App 10 Part B Area 10 / Part D Item 1(f) | Incident Response | New |
| F-008 | KMS Key Rotation Not Automated | Medium | App 10 Part B Area 9 | Cryptographic Key Mgmt | New |
| F-009 | Cloud Skills Training Plan Incomplete | Low | App 10 Part B Area 1 | Strategy and Governance | New |
| F-010 | Container Image Scanning Not Gating CI/CD Pipeline | Low | App 10 Part B Area 6 | Container Security | New |
| F-011 | DDoS Response Playbook Not Tested | Low | App 10 Part B Area 10 | Incident Response | New |

### 3.3 Findings by Control Area

| # | Control Area | RMIT Reference | Critical | High | Medium | Low | Total | Overall Rating |
|---|-------------|----------------|----------|------|--------|-----|-------|---------------|
| 1 | Cloud Strategy and Governance | App 10 Part B Area 1 | 0 | 0 | 0 | 1 | 1 | Partially Effective |
| 2 | Cloud Usage Policy | App 10 Part B Area 2 | 0 | 0 | 0 | 0 | 0 | Effective |
| 3 | Due Diligence and CSP Selection | App 10 Part B Area 3 | 0 | 0 | 0 | 0 | 0 | Effective |
| 4 | CSP Certifications and Assurance | App 10 Part B Area 3 | 0 | 0 | 0 | 0 | 0 | Effective |
| 5 | Contracts and SLAs | App 10 Part B Area 11 | 0 | 0 | 0 | 0 | 0 | Effective |
| 6 | Cloud Monitoring and Operations | App 10 Part B Area 7 | 0 | 0 | 0 | 0 | 0 | Effective |
| 7 | Cloud Architecture and Security | App 10 Part B Area 4 | 0 | 0 | 1 | 0 | 1 | Partially Effective |
| 8 | IaC and Automation | App 10 Part B Area 5 | 0 | 0 | 1 | 0 | 1 | Partially Effective |
| 9 | Container Security | App 10 Part B Area 6 | 0 | 0 | 0 | 1 | 1 | Partially Effective |
| 10 | Change Management | App 10 Part B Area 5 | 0 | 0 | 0 | 0 | 0 | Effective |
| 11 | Backup, Recovery, and Resilience | App 10 Part B Area 8 | 0 | 0 | 1 | 0 | 1 | Partially Effective |
| 12 | Exit Strategy and Portability | App 10 Part B Area 13 | 0 | 1 | 0 | 0 | 1 | Ineffective |
| 13 | Cryptographic Key Management | App 10 Part B Area 9 | 0 | 0 | 1 | 0 | 1 | Partially Effective |
| 14 | Access Controls (Cloud) | App 10 Part B Area 2 | 0 | 1 | 0 | 0 | 1 | Partially Effective |
| 15 | Cloud Logging and SIEM | App 10 Part B Area 7 | 0 | 1 | 0 | 0 | 1 | Effective* |
| 16 | Cloud Incident Response | App 10 Part B Area 10 | 0 | 0 | 1 | 1 | 2 | Effective* |
| | **Total** | | **0** | **3** | **5** | **3** | **11** | |

*Note: Control areas 15 and 16 are rated Effective overall with specific gaps identified; the finding reflects a specific deficiency within an otherwise adequate control framework.

---

## 4. Detailed Findings

---

### Finding F-001: Overly Permissive IAM Policies and Root Account Usage

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-001 |
| **Risk Rating** | High |
| **Control Area** | Access Controls (Cloud) |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 2 (Access Controls); Part D, Item 1(a) (Identity and access management) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 14.1 -- 14.6 |
| **Status** | New |

**Description:**

The assessment identified deficiencies in BPB's cloud IAM governance that collectively create an elevated risk of unauthorised access and privilege escalation within the AWS production environment. RMIT Appendix 10 requires the FI to implement effective identity and access management controls, including the principle of least privilege, for all cloud services.

**RMIT Requirement:**

Appendix 10, Part D, Item 1(a): "The FI must implement effective identity and access management controls, including multi-factor authentication, role-based access control, and the principle of least privilege for all cloud service accounts and users."

**Condition Observed:**

1. **Overly permissive IAM policies:** Review of the IAM Policy Export (E-086) identified four (4) IAM policies attached to production roles that use wildcard (`*`) actions on resource ARNs. Specifically:
   - `BPB-T24-DeployRole` grants `ec2:*` on all EC2 resources in the production account;
   - `BPB-T24-DataOpsRole` grants `s3:*` on all S3 buckets including the audit log bucket;
   - `BPB-T24-MonitorRole` grants `cloudwatch:*` and `logs:*` across all log groups;
   - `BPB-T24-BackupRole` grants `rds:*` on all RDS instances including the ability to modify and delete.

2. **Stale service accounts with excessive privileges:** Two (2) service accounts (`svc-t24-migration` and `svc-t24-legacy-sync`) retain `AdministratorAccess` managed policy. These accounts were created during the migration phase (Apr 2025) and have not had their credentials rotated in nine (9) months. The accounts remain active despite the migration being completed in October 2025.

3. **Root account usage for non-emergency tasks:** CloudTrail logs (E-093) revealed three (3) instances of root account usage for non-emergency administrative tasks between November 2025 and January 2026:
   - 12 Nov 2025: Root used to modify S3 bucket policy;
   - 3 Dec 2025: Root used to create an IAM user;
   - 8 Jan 2026: Root used to update a KMS key policy.
   None of these actions were documented as break-glass events in the incident log.

**Root Cause:**

The rapid pace of the cloud build-out and migration (Apr -- Oct 2025) prioritised functional delivery over IAM governance maturity. IAM policies were created with broad permissions during development and not refined to least-privilege before production go-live. Post-migration hygiene -- including service account decommissioning and credential rotation -- was not formally tracked. Root account usage lacks a defined break-glass procedure with compensating controls.

**Risk/Impact:**

- **Unauthorised access:** Overly permissive policies increase the blast radius if any IAM credential is compromised, potentially allowing an attacker to access, modify, or delete critical T24 data and infrastructure.
- **Privilege escalation:** Service accounts with AdministratorAccess could be exploited to escalate privileges, create new users, or exfiltrate data.
- **Regulatory non-compliance:** Non-adherence to the principle of least privilege and uncontrolled root account usage contravenes RMIT Appendix 10 requirements and may attract regulatory scrutiny.
- **Audit trail integrity:** The `BPB-T24-DataOpsRole` policy with `s3:*` on all buckets includes the audit log bucket, creating the risk that an insider or compromised account could tamper with audit logs.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | AWS IAM Policy Export -- BPB-PROD-001 | E-086 | 22 Jan 2026 |
| 2 | Cloud Privileged Access Inventory and Controls Register | E-087 | 22 Jan 2026 |
| 3 | AWS Service Account Inventory | E-090 | 22 Jan 2026 |
| 4 | CloudTrail Configuration Export -- All Accounts | E-093 | 30 Jan 2026 |
| 5 | BPB Cloud IAM Policy | E-085 | Oct 2025 |

**Recommendation:**

1. **Immediate (within 14 days):** Revoke `AdministratorAccess` from `svc-t24-migration` and `svc-t24-legacy-sync` service accounts. If accounts are no longer required, disable and schedule for deletion. If still required, assign least-privilege policies scoped to specific resources and actions.
2. **Short-term (within 30 days):** Refine the four identified IAM policies to replace wildcard actions with specific, required actions. Use IAM Access Analyzer's policy generation feature to create least-privilege policies based on actual CloudTrail access patterns from the past 90 days.
3. **Short-term (within 30 days):** Implement a root account break-glass procedure that requires: (a) documented justification, (b) dual-approval, (c) real-time SIEM alert on any root account activity, and (d) post-use review. Store root credentials in a physical safe with tamper-evident seals.
4. **Ongoing:** Deploy AWS IAM Access Analyzer on all accounts to continuously identify unused permissions and external access. Integrate findings into quarterly access reviews.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | (1) Revoke AdministratorAccess from stale service accounts immediately. (2) Engage IAM Access Analyzer to generate least-privilege policies for the four identified roles. (3) Develop and implement root break-glass procedure. (4) Deploy IAM Access Analyzer across all accounts. |
| **Responsible Person** | Encik Ahmad Razif bin Mohd Yusof, Head of Cloud Engineering |
| **Target Completion Date** | 28 February 2026 |
| **Status** | In Progress |

---

### Finding F-002: Incomplete Cloud Audit Logging and SIEM Integration

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-002 |
| **Risk Rating** | High |
| **Control Area** | Cloud Logging and SIEM |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 7 (Security Monitoring); Part D, Item 1(e) (Security monitoring and log management) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 15.1 -- 15.5 |
| **Status** | New |

**Description:**

BPB's cloud audit logging and SIEM integration are not comprehensive, creating gaps in threat detection and forensic investigation capability. RMIT Appendix 10 requires the FI to implement comprehensive logging, monitoring, and security event management for all cloud services.

**RMIT Requirement:**

Appendix 10, Part D, Item 1(e): "The FI must implement comprehensive security monitoring, logging, and security event management for all cloud services, including integration with the FI's security operations centre."

**Condition Observed:**

1. **CloudTrail limited to management events only:** Review of the CloudTrail configuration (E-093) confirmed that only management events are enabled across all three AWS accounts. S3 data-level events (GetObject, PutObject, DeleteObject) are not logged. This means that access to T24 data stored in S3 -- including customer financial records and Temenos data extracts -- is not audited at the object level.

2. **GuardDuty not enabled on DR account:** Amazon GuardDuty is enabled and active on the production account (BPB-PROD-001) and UAT account (BPB-UAT-001) but is not enabled on the DR account (BPB-DR-001) in ap-southeast-3 (E-050). This creates a monitoring blind spot in the DR environment.

3. **VPC Flow Logs not integrated with SIEM:** VPC Flow Logs are enabled and stored in CloudWatch Logs but are not forwarded to the Splunk Cloud SIEM (E-095). Network-layer anomalies (e.g., unusual traffic patterns, data exfiltration attempts) are therefore not correlated with other security events.

4. **Incomplete SIEM integration:** Of the 12 AWS services generating security-relevant logs, only 8 are integrated with Splunk Cloud. The following 4 services are not sending logs to SIEM:
   - AWS WAF logs (web application attack detection);
   - Amazon ECR image scan events (container vulnerability alerts);
   - AWS Config change notifications (configuration drift alerts);
   - AWS KMS key usage events (encryption key access monitoring).

**Root Cause:**

The SIEM integration was implemented in phases aligned with the migration timeline. Phase 1 (completed Oct 2025) covered core services (CloudTrail, GuardDuty, RDS, IAM). Phase 2 (WAF, VPC Flow Logs, Config, KMS, ECR) was planned for Q1 2026 but has not yet commenced. S3 data events were excluded due to cost concerns without a formal risk-acceptance decision. The DR account was stood up later (Dec 2025) and GuardDuty enablement was overlooked during provisioning.

**Risk/Impact:**

- **Undetected data access:** Without S3 data-level logging, unauthorised access to customer financial data stored in S3 would not be detected or auditable, compromising forensic investigation capability and regulatory reporting.
- **DR environment blind spot:** The absence of GuardDuty on the DR account means that if the DR environment is compromised (e.g., via a supply chain attack or misconfigured access), there is no automated threat detection.
- **Incomplete threat correlation:** Without VPC Flow Logs and WAF logs in SIEM, the SOC cannot correlate network-layer and application-layer attacks with identity and data-access events, reducing detection efficacy for multi-stage attacks.
- **Regulatory non-compliance:** Incomplete logging contravenes the RMIT requirement for comprehensive security monitoring of cloud services.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | CloudTrail Configuration Export -- All Accounts | E-093 | 30 Jan 2026 |
| 2 | SIEM Integration Architecture -- Cloud Log Sources | E-095 | Dec 2025 |
| 3 | GuardDuty and Security Hub Configuration Export | E-050 | 24 Jan 2026 |
| 4 | CloudWatch Log Retention and S3 Lifecycle Policy Export | E-094 | 30 Jan 2026 |

**Recommendation:**

1. **Immediate (within 14 days):** Enable Amazon GuardDuty on the DR account (BPB-DR-001) and configure centralised findings aggregation to the production account.
2. **Short-term (within 30 days):** Enable S3 data-level events in CloudTrail for all production S3 buckets containing T24 data. Apply event selectors to focus on critical buckets to manage cost.
3. **Short-term (within 30 days):** Complete Phase 2 SIEM integration: forward VPC Flow Logs, WAF logs, Config change notifications, KMS key usage events, and ECR scan events to Splunk Cloud.
4. **Short-term (within 30 days):** Develop and deploy SIEM correlation rules for the newly integrated log sources, including rules for: S3 data exfiltration patterns, WAF attack escalation, and KMS key misuse.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | (1) Enable GuardDuty on DR account immediately. (2) Enable S3 data events for critical buckets. (3) Accelerate Phase 2 SIEM integration to complete by 15 Feb 2026. (4) Develop corresponding SIEM rules. |
| **Responsible Person** | Puan Nurul Huda binti Ismail, Head of Security Operations |
| **Target Completion Date** | 15 February 2026 |
| **Status** | In Progress |

---

### Finding F-003: Untested and Incomplete Cloud Exit Strategy

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-003 |
| **Risk Rating** | High |
| **Control Area** | Exit Strategy and Portability |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 13 (Exit Strategy and Data Portability) |
| **AWP Reference** | AWP-CLOUD-01, Test Procedure 12.1 -- 12.5 |
| **Status** | New |

**Description:**

BPB's cloud exit strategy for the T24/AWS deployment is high-level and has never been tested, creating a material risk that BPB cannot execute a timely and orderly exit from AWS if required. RMIT Appendix 10 requires the FI to maintain a viable, tested exit strategy for cloud services supporting critical systems.

**RMIT Requirement:**

Appendix 10, Part B, Area 13: "The FI must develop, maintain, and periodically test a viable exit strategy for critical cloud services, including data retrieval procedures, alternative hosting arrangements, timeline and resource estimates, and contractual provisions for exit assistance."

**Condition Observed:**

1. **Exit strategy is high-level and incomplete:** The Cloud Exit Strategy document (E-074, v1.0, Nov 2025) exists but is limited to a high-level narrative. It identifies AWS as the CSP and Temenos T24 as the workload but does not include:
   - A step-by-step data retrieval procedure with responsible parties and sequencing;
   - An estimated timeline for complete data extraction and application migration;
   - A cost estimate for executing the exit (infrastructure, personnel, licensing, migration tooling);
   - Criteria and triggers for initiating exit (beyond regulatory directive).

2. **Data portability plan in draft:** The T24 Data Portability Assessment (E-075) remains in draft (v0.5, Dec 2025). Database export procedures for Oracle on RDS have not been finalised, and the format and integrity verification steps for extracted data are undefined.

3. **No data retrieval and deletion procedures at exit:** BPB has not developed formal procedures for retrieving all data from AWS and confirming secure deletion/destruction of data upon contract termination (E-076 -- Gap).

4. **Exit strategy never tested:** The exit strategy has never been tested, even at a tabletop level (E-078 -- Gap). BPB has no empirical understanding of the time, cost, or complexity of executing an exit.

5. **Contractual gap -- exit assistance period:** Review of the Enterprise Agreement Schedule 7 (E-034) revealed that while termination provisions exist, the exit assistance period (the duration during which AWS would continue to provide services while BPB transitions away) is not explicitly defined with a minimum duration.

**Root Cause:**

Cloud exit planning was deprioritised relative to migration delivery. The cloud team's focus during 2025 was on building and stabilising the T24 environment on AWS. Exit strategy development was allocated to a single resource on a part-time basis, resulting in a document that has not progressed beyond initial drafting. There is no defined owner or governance cadence for exit strategy maintenance and testing.

**Risk/Impact:**

- **Vendor lock-in:** Without a tested, actionable exit strategy, BPB is effectively locked into AWS for its critical core banking workload. If AWS experiences a material service failure, changes its pricing materially, or is subject to regulatory restrictions, BPB may be unable to migrate in a controlled and timely manner.
- **Regulatory non-compliance:** BNM may view the absence of a tested exit strategy as a material gap in cloud risk management, potentially resulting in supervisory action or restrictions on cloud usage.
- **Data loss risk:** Without defined data retrieval and deletion procedures, BPB risks incomplete data extraction or residual data remaining on AWS infrastructure after exit.
- **Unplanned costs:** The absence of cost estimates means BPB has not budgeted or provisioned for exit, which could result in significant unplanned expenditure if exit is required at short notice.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | BPB Cloud Exit Strategy -- T24/AWS | E-074 | Nov 2025 |
| 2 | T24 Data Portability Assessment (Draft) | E-075 | Dec 2025 |
| 3 | Data Retrieval and Deletion Procedures -- Not Developed | E-076 | N/A |
| 4 | Exit Strategy Testing Records -- Never Tested | E-078 | N/A |
| 5 | Enterprise Agreement -- Schedule 7 (Termination and Exit) | E-034 | 15 Sep 2025 |

**Recommendation:**

1. **Short-term (within 60 days):** Complete the exit strategy document to include: (a) step-by-step data retrieval procedures for all data stores (RDS Oracle, S3, Secrets Manager, CloudWatch Logs); (b) estimated timeline (target: full exit within 6 months of trigger); (c) cost estimate including infrastructure, personnel, licensing, and tooling; (d) defined exit triggers beyond regulatory directive (e.g., material SLA breach, CSP insolvency, unacceptable pricing change).
2. **Short-term (within 60 days):** Finalise the data portability assessment (v1.0) with validated Oracle database export procedures, data format specifications, and integrity verification steps.
3. **Short-term (within 60 days):** Develop formal data retrieval and secure deletion procedures for contract termination, aligned with PDPA requirements.
4. **Medium-term (within 90 days):** Negotiate an addendum to the Enterprise Agreement to define a minimum exit assistance period (recommended: 12 months from termination notice).
5. **Medium-term (within 120 days):** Conduct a tabletop exercise of the exit strategy with all relevant stakeholders (Cloud Engineering, T24 Application, DBA, Risk, Legal, Finance) to validate the plan and identify gaps.
6. **Ongoing:** Assign a named owner for the exit strategy and schedule annual reviews and testing.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | (1) Complete exit strategy v2.0 with all required components. (2) Finalise data portability assessment. (3) Develop data retrieval and deletion procedures. (4) Negotiate exit assistance addendum with AWS. (5) Conduct tabletop exercise by Q2 2026. |
| **Responsible Person** | Encik Mohd Faizal bin Abdullah, CTO |
| **Target Completion Date** | 30 April 2026 |
| **Status** | Not Started |

---

### Finding F-004: Cloud Security Posture Management Not Deployed

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-004 |
| **Risk Rating** | Medium |
| **Control Area** | Cloud Architecture and Security |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 4 (Cloud Security Controls); Part D, Item 1(b) (Security configuration management) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 7.5 -- 7.7 |
| **Status** | New |

**Description:**

BPB has not deployed a Cloud Security Posture Management (CSPM) tool to continuously assess the security configuration of its AWS environment against established benchmarks.

**RMIT Requirement:**

Appendix 10, Part D, Item 1(b): "The FI must implement security configuration management controls to ensure cloud resources are configured in accordance with approved security baselines and industry benchmarks."

**Condition Observed:**

- AWS Security Hub is enabled on the production account but CIS AWS Foundations Benchmark compliance checks are not activated. Security Hub is currently used only as a findings aggregator for GuardDuty.
- No CSPM tool (e.g., Wiz, Prisma Cloud, Prowler) is deployed to provide continuous assessment of cloud security posture against CIS benchmarks, AWS Well-Architected security best practices, or BPB's own security baselines.
- During fieldwork, CyberAssure enabled CIS AWS Foundations Benchmark v3.0 checks in Security Hub for assessment purposes. The scan identified 23 failed checks across the production account, including findings related to S3 public access block settings, EBS volume encryption defaults, and IAM password policy configuration.

**Root Cause:**

CSPM deployment was included in the Phase 2 security roadmap (Q1 2026) but has not been initiated. The cloud team has been focused on operational stabilisation post go-live. A CSPM tool selection process was started in December 2025 but is not yet concluded.

**Risk/Impact:**

- **Configuration drift:** Without continuous posture assessment, security misconfigurations may go undetected, increasing the attack surface.
- **Compliance gaps:** The 23 failed CIS benchmark checks identified during fieldwork indicate that the current environment has configuration gaps that would not be detected without a CSPM tool.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | GuardDuty and Security Hub Configuration Export | E-050 | 24 Jan 2026 |
| 2 | CIS AWS Benchmark Scan Results (fieldwork scan) | Fieldwork workpaper | 24 Jan 2026 |

**Recommendation:**

1. Activate CIS AWS Foundations Benchmark and AWS Foundational Security Best Practices standards in Security Hub immediately as an interim measure.
2. Complete CSPM tool selection and deploy (e.g., Wiz, Prisma Cloud, or Prowler for open-source) by end of Q2 2026.
3. Establish a process for triaging and remediating CSPM findings with defined SLAs by severity.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | (1) Activate CIS benchmark checks in Security Hub immediately. (2) Complete CSPM tool evaluation and deploy Wiz by Q2 2026. (3) Establish remediation SLAs. |
| **Responsible Person** | Encik Ahmad Razif bin Mohd Yusof, Head of Cloud Engineering |
| **Target Completion Date** | 30 June 2026 |
| **Status** | Not Started |

---

### Finding F-005: IaC Drift Detection Not Implemented

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-005 |
| **Risk Rating** | Medium |
| **Control Area** | IaC and Automation |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 5 (Change Management and Configuration Control) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 8.5 |
| **Status** | New |

**Description:**

BPB uses Terraform as its Infrastructure as Code (IaC) tool for provisioning AWS resources but has not implemented drift detection to identify when cloud resources deviate from their Terraform-defined state.

**RMIT Requirement:**

Appendix 10, Part B, Area 5 requires the FI to maintain effective change management and configuration control for cloud services, including mechanisms to detect and remediate unauthorised or unplanned changes.

**Condition Observed:**

- Terraform is used to provision and manage AWS infrastructure via GitLab CI/CD. However, no drift detection mechanism is in place (E-055 -- Gap).
- Review of AWS Config change records (E-066) identified three (3) manual console changes made directly to production resources between October and December 2025, bypassing the Terraform/GitLab CI/CD pipeline:
  - 15 Oct 2025: Security group rule added manually via AWS Console;
  - 22 Nov 2025: RDS parameter group modified via AWS Console;
  - 9 Dec 2025: S3 bucket policy updated via AWS Console.
- These changes were not reflected in the Terraform state file, creating drift between the intended (IaC-defined) and actual configuration.

**Root Cause:**

Drift detection was considered a "Phase 2" capability and was not implemented during the initial migration. Console access for production is restricted but not fully prevented for senior cloud engineers, enabling ad-hoc changes.

**Risk/Impact:**

- **Configuration integrity:** Drift between IaC-defined and actual configurations creates uncertainty about the true state of the environment and may introduce security misconfigurations.
- **Audit trail gaps:** Changes made outside the IaC pipeline bypass peer review and approval workflows, weakening the change management control.
- **Recovery risk:** In a disaster recovery scenario, restoring from Terraform code would not reflect the manually applied changes, potentially causing service disruptions.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | Drift Detection -- Not Deployed | E-055 | N/A |
| 2 | AWS Config Change Timeline Export (Oct-Dec 2025) | E-066 | 27 Jan 2026 |
| 3 | Terraform Module Repository (GitLab) | E-051 | Jan 2026 |

**Recommendation:**

1. Implement Terraform Cloud or Terraform Enterprise with drift detection enabled to automatically compare actual AWS resource states against Terraform state files.
2. Configure alerts for detected drift and integrate with the incident management workflow.
3. Restrict AWS Console write access for production accounts to break-glass only, enforcing all changes through the IaC pipeline.
4. Reconcile the three identified drift instances and update the Terraform state and code to reflect the actual intended configuration.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | (1) Implement Terraform Cloud with drift detection. (2) Reconcile existing drift. (3) Restrict console write access to break-glass. |
| **Responsible Person** | Encik Ahmad Razif bin Mohd Yusof, Head of Cloud Engineering |
| **Target Completion Date** | 31 March 2026 |
| **Status** | Not Started |

---

### Finding F-006: Cloud DR Not Tested End-to-End

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-006 |
| **Risk Rating** | Medium |
| **Control Area** | Backup, Recovery, and Resilience |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 8 (Business Continuity and Disaster Recovery); Part D, Item 1(d) (Resilience and recovery) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 11.4 -- 11.6 |
| **Status** | New |

**Description:**

BPB's cloud DR architecture for the T24 workload has been designed but a full end-to-end failover test has not been conducted. The stated RTO of 4 hours and RPO of 1 hour have not been validated.

**RMIT Requirement:**

Appendix 10, Part D, Item 1(d): "The FI must test its cloud disaster recovery and business continuity arrangements at least annually, including full failover testing for critical systems, to validate recovery time and recovery point objectives."

**Condition Observed:**

- DR architecture is documented (E-070) with a target of ap-southeast-3 (Jakarta) as the DR region. The design includes cross-region RDS read replica, S3 cross-region replication, and ECS Fargate service definitions for the DR region.
- Only a partial component test was conducted in November 2025 (E-071): an RDS failover to the read replica was tested in isolation. The test confirmed database switchover in 38 minutes but did not test application-tier failover, DNS cutover, or end-user access.
- The stated RTO of 4 hours and RPO of 1 hour have not been validated through a full end-to-end test including: application failover, load balancer and DNS switchover, data consistency verification, and user acceptance testing in the DR environment.
- No failback procedure or test has been conducted.

**Root Cause:**

The DR region was provisioned in December 2025, and the cloud team planned a full DR test for February 2026. However, the test has been deferred due to competing priorities (production stability monitoring and this IESP assessment). There is no formal DR test schedule integrated into the annual testing calendar.

**Risk/Impact:**

- **Unvalidated RTO/RPO:** Without end-to-end testing, BPB cannot confirm that it can recover T24 within the 4-hour RTO, potentially resulting in prolonged core banking outage.
- **Failover failure risk:** Untested DR procedures may contain errors or dependencies that only surface during an actual disaster, when the consequences are most severe.
- **Regulatory expectation:** BNM expects annual DR testing for critical systems; the absence of a full test represents a gap in resilience assurance.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | T24 Cloud DR Architecture and Failover Procedures | E-070 | Dec 2025 |
| 2 | DR Test Report -- Partial Component Test (Nov 2025) | E-071 | Nov 2025 |
| 3 | Multi-AZ Deployment Configuration Evidence | E-072 | 28 Jan 2026 |

**Recommendation:**

1. Conduct a full end-to-end DR failover test by Q1 2026, including: application-tier failover to ap-southeast-3, DNS cutover via Route 53, data consistency verification, and user acceptance testing.
2. Document actual RTO and RPO achieved during the test and compare against targets.
3. Test the failback procedure from DR to primary region.
4. Integrate cloud DR testing into the annual BCP/DR test calendar with at least one full test per year.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | Full end-to-end DR failover test planned for late February 2026. Will include application failover, DNS cutover, data verification, and UAT. Failback test to follow. Annual schedule to be established. |
| **Responsible Person** | Encik Ahmad Razif bin Mohd Yusof, Head of Cloud Engineering |
| **Target Completion Date** | 28 February 2026 |
| **Status** | In Progress (test scheduled for 25-26 Feb 2026) |

---

### Finding F-007: Cloud Incident Response Playbook Incomplete

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-007 |
| **Risk Rating** | Medium |
| **Control Area** | Cloud Incident Response |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 10 (Incident Management); Part D, Item 1(f) (Cloud-specific incident response) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 16.1 -- 16.3 |
| **Status** | New |

**Description:**

BPB has a general cloud incident response plan (CIRP) but has not developed cloud-specific response playbooks for key threat scenarios that are unique to the AWS environment.

**RMIT Requirement:**

Appendix 10, Part D, Item 1(f): "The FI must develop cloud-specific incident response procedures, including playbooks for common cloud security incidents, integrated with the FI's overall incident management framework."

**Condition Observed:**

- The Cloud Incident Response Plan (E-098, v1.0, Nov 2025) provides a general framework for cloud incident handling, including severity classification, escalation matrix, and BNM notification criteria.
- However, the following cloud-specific playbooks have not been developed:
  - **AWS account compromise playbook:** Steps for containment, investigation, and recovery when an AWS account or IAM credentials are suspected compromised;
  - **Access key compromise playbook:** Procedures for rotating compromised access keys, assessing blast radius, and identifying affected resources;
  - **S3 data exposure playbook:** Steps for responding to accidental or malicious public exposure of S3 buckets containing sensitive data;
  - **Cryptographic key compromise playbook:** Procedures for responding to suspected KMS key compromise, including re-encryption of affected data.
- The incident classification matrix does not include cloud-specific indicators of compromise (IoCs) such as GuardDuty finding types, unusual API call patterns, or cross-region activity.

**Root Cause:**

The CIRP was developed based on BPB's existing on-premises incident response plan with cloud-specific modifications limited to escalation contacts and AWS Support integration. The team lacked experience with cloud-native threat scenarios to develop specific playbooks. Playbook development was planned for Q1 2026 but has not commenced.

**Risk/Impact:**

- **Delayed response:** Without predefined playbooks, incident responders must improvise during cloud-specific incidents, increasing mean time to contain (MTTC) and mean time to recover (MTTR).
- **Inconsistent handling:** Ad-hoc responses may miss critical containment steps (e.g., not revoking all sessions for a compromised IAM user, not checking for persistence mechanisms).
- **Evidence preservation:** Without defined forensic procedures for cloud incidents, critical evidence (e.g., CloudTrail logs, VPC Flow Logs, memory dumps) may not be preserved correctly.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | BPB Cloud Incident Response Plan (CIRP) | E-098 | Nov 2025 |
| 2 | Cloud Incident Classification and Escalation Matrix | E-099 | Nov 2025 |

**Recommendation:**

1. Develop cloud-specific incident response playbooks for: (a) AWS account compromise, (b) IAM access key compromise, (c) S3 data exposure, and (d) KMS key compromise.
2. Include cloud-specific IoCs in the incident classification matrix, mapped to GuardDuty finding types and CloudTrail anomaly patterns.
3. Conduct tabletop exercises for each playbook within 30 days of development.
4. Integrate playbooks with the SIEM alert rules to enable semi-automated initial response steps.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | Develop four cloud-specific playbooks and update the incident classification matrix with cloud IoCs. Conduct tabletop exercises for each. |
| **Responsible Person** | Puan Nurul Huda binti Ismail, Head of Security Operations |
| **Target Completion Date** | 28 February 2026 |
| **Status** | Not Started |

---

### Finding F-008: KMS Key Rotation Not Automated

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-008 |
| **Risk Rating** | Medium |
| **Control Area** | Cryptographic Key Management |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 9 (Cryptographic Controls) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 13.3 -- 13.5 |
| **Status** | New |

**Description:**

BPB uses AWS KMS customer-managed keys (CMKs) for encrypting RDS databases and S3 buckets but has not enabled automatic key rotation, and there is no defined key rotation policy.

**RMIT Requirement:**

Appendix 10, Part B, Area 9 requires the FI to implement effective cryptographic key management controls, including defined key lifecycles and rotation procedures.

**Condition Observed:**

- Five (5) customer-managed KMS keys are in use for encrypting production data: two for RDS (Oracle tablespace encryption), two for S3 (bucket-level SSE-KMS), and one for EBS volumes.
- AWS KMS automatic annual rotation is not enabled for any of the five CMKs (E-081).
- The keys were created during the migration phase (Jun -- Aug 2025) and have not been rotated since creation -- approximately 7 to 9 months.
- The BPB KMS Key Management Procedures document (E-081) references key rotation as a requirement but does not define a rotation schedule, procedure, or responsible party.

**Root Cause:**

Key rotation was not configured during initial key creation. The key management procedure was developed as a policy document without operational implementation details. The cloud team was unaware that AWS KMS automatic rotation must be explicitly enabled for each CMK.

**Risk/Impact:**

- **Cryptographic risk:** Extended use of the same key material without rotation increases the risk exposure if key material is compromised, as all data encrypted since key creation would be at risk.
- **Compliance gap:** Industry best practice and CIS AWS Benchmark require annual (or more frequent) key rotation for CMKs.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | BPB KMS Key Management Procedures | E-081 | Nov 2025 |
| 2 | KMS and S3/RDS Encryption Configuration Export | E-082 | 29 Jan 2026 |
| 3 | KMS Key Policy Export -- BPB CMKs | E-083 | 29 Jan 2026 |

**Recommendation:**

1. Enable AWS KMS automatic annual rotation for all five customer-managed keys immediately. (Note: AWS KMS automatic rotation creates new key material annually while retaining old material for decryption -- no re-encryption is required.)
2. Update the KMS Key Management Procedures to include: rotation schedule (annual minimum), rotation verification process, and responsible party.
3. Configure a CloudWatch alarm to detect CMKs that do not have automatic rotation enabled (using AWS Config rule `cmk-backing-key-rotation-enabled`).

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | Enable automatic annual rotation on all CMKs. Update procedures. Deploy Config rule for monitoring. |
| **Responsible Person** | Encik Ahmad Razif bin Mohd Yusof, Head of Cloud Engineering |
| **Target Completion Date** | 28 February 2026 |
| **Status** | Not Started |

---

### Finding F-009: Cloud Skills Training Plan Incomplete

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-009 |
| **Risk Rating** | Low |
| **Control Area** | Cloud Strategy and Governance |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 1 (Cloud Governance and Skills) |
| **AWP Reference** | AWP-CLOUD-01, Test Procedure 1.4 |
| **Status** | New |

**Description:**

BPB's cloud team does not have a formalised training and certification plan, and the current level of AWS certification across the team is limited.

**RMIT Requirement:**

Appendix 10, Part B, Area 1 requires the FI to ensure that personnel responsible for managing cloud services possess adequate skills and knowledge, supported by a structured training programme.

**Condition Observed:**

- The cloud engineering team comprises eight (8) members responsible for managing the T24 AWS environment.
- Only three (3) of eight team members hold current AWS certifications:
  - 1x AWS Solutions Architect -- Professional;
  - 1x AWS Solutions Architect -- Associate;
  - 1x AWS SysOps Administrator -- Associate.
- Five team members have no cloud-specific certifications and have undergone only vendor-provided introductory training.
- There is no formal cloud skills training plan with: target certifications per role, training budget allocation, completion timelines, or skills gap analysis.

**Root Cause:**

The cloud team was assembled rapidly during the migration programme, drawing on existing IT infrastructure staff. Training was ad-hoc and driven by individual initiative rather than a structured programme. A training plan was discussed at the Cloud Steering Committee in November 2025 but was not formalised or funded.

**Risk/Impact:**

- **Operational risk:** Insufficient cloud expertise increases the risk of misconfigurations, inefficient operations, and slower incident response.
- **Key-person dependency:** Advanced cloud knowledge is concentrated in 2-3 individuals, creating key-person risk.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | Cloud Steering Committee Minutes -- Nov 2025 | E-006 | Nov 2025 |
| 2 | Cloud Governance RACI | E-004 | Sep 2025 |

**Recommendation:**

1. Develop a formal cloud skills training plan that maps required certifications to each role in the cloud team.
2. Allocate training budget and set certification targets (e.g., all team members to hold at least AWS Associate-level certification within 6 months).
3. Prioritise security-focused training (AWS Security Specialty) for at least two team members.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | Develop formal training plan with role-based certification targets and dedicated budget. Submit for CTO approval by end of Q1 2026. |
| **Responsible Person** | Encik Ahmad Razif bin Mohd Yusof, Head of Cloud Engineering |
| **Target Completion Date** | 31 March 2026 |
| **Status** | Not Started |

---

### Finding F-010: Container Image Scanning Not Gating CI/CD Pipeline

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-010 |
| **Risk Rating** | Low |
| **Control Area** | Container Security |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 6 (Container and Serverless Security) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 9.2 -- 9.4 |
| **Status** | New |

**Description:**

BPB has enabled basic image scanning in Amazon ECR but scan results are not integrated as a quality gate in the CI/CD pipeline, allowing container images with known HIGH-severity vulnerabilities to be deployed to production.

**RMIT Requirement:**

Appendix 10, Part B, Area 6 requires the FI to implement container security controls including vulnerability scanning and prevention of deploying containers with known critical vulnerabilities.

**Condition Observed:**

- Amazon ECR basic scanning (Clair-based) is enabled and scans images on push (E-057).
- However, scan results are not configured as a blocking gate in the GitLab CI/CD pipeline. The pipeline proceeds to deployment regardless of scan findings.
- Review of ECR scan results for the 12 most recently pushed T24 container images revealed: 2 images with HIGH-severity vulnerabilities (CVE-2025-XXXX in a base OS package) and 5 images with MEDIUM-severity vulnerabilities.
- The two HIGH-severity images were deployed to the production ECS cluster without remediation or risk acceptance.

**Root Cause:**

ECR basic scanning was enabled as a visibility measure but was not integrated into the CI/CD pipeline as a gate. The pipeline configuration (E-054) includes a scan stage that runs Checkov for IaC but does not include a container image vulnerability assessment step.

**Risk/Impact:**

- **Vulnerable containers in production:** Known HIGH-severity vulnerabilities in production containers could be exploited by an attacker who gains network access to the ECS environment.
- **Supply chain risk:** Without gating, compromised or vulnerable base images could propagate undetected into production.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | ECR Image Scan Results -- T24 Container Images | E-057 | 25 Jan 2026 |
| 2 | GitLab CI/CD Pipeline Configuration | E-054 | Jan 2026 |
| 3 | Container Security Standard | E-056 | Nov 2025 |

**Recommendation:**

1. Integrate a container image scanning tool (e.g., Trivy, Grype, or Amazon ECR enhanced scanning with Amazon Inspector) into the GitLab CI/CD pipeline as a blocking gate.
2. Define vulnerability thresholds: block deployment for CRITICAL and HIGH; warn for MEDIUM.
3. Remediate the two existing HIGH-severity vulnerabilities in production images by rebuilding with patched base images.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | Integrate Trivy into GitLab CI/CD pipeline as a blocking gate. Rebuild affected images with patched base. Enable ECR enhanced scanning via Amazon Inspector. |
| **Responsible Person** | Encik Ahmad Razif bin Mohd Yusof, Head of Cloud Engineering |
| **Target Completion Date** | 31 March 2026 |
| **Status** | Not Started |

---

### Finding F-011: DDoS Response Playbook Not Tested

| Attribute | Detail |
|-----------|--------|
| **Finding ID** | F-011 |
| **Risk Rating** | Low |
| **Control Area** | Cloud Incident Response |
| **RMIT Clause Reference** | Appendix 10, Part B, Area 10 (Incident Management) |
| **AWP Reference** | AWP-CLOUD-02, Test Procedure 16.5 |
| **Status** | New |

**Description:**

BPB has AWS Shield Advanced enabled and a DDoS response playbook documented but has never conducted a tabletop exercise or simulation to validate the playbook.

**RMIT Requirement:**

Appendix 10, Part B, Area 10 requires the FI to periodically test incident response procedures, including playbooks for common cloud-specific threats.

**Condition Observed:**

- AWS Shield Advanced is enabled on CloudFront distributions and Application Load Balancers (E-049). The Shield Response Team (SRT) engagement is configured.
- A DDoS response playbook is documented within the CIRP (E-098) and covers: detection via Shield Advanced metrics, escalation to AWS SRT, traffic scrubbing activation, and communication procedures.
- However, no tabletop exercise, simulation, or live drill has been conducted to validate the playbook (E-102 -- Gap).
- BPB's SOC team has not practised coordinating with the AWS Shield Response Team in a simulated scenario.

**Root Cause:**

The DDoS playbook was developed in November 2025 as part of the CIRP. A tabletop exercise was tentatively planned for Q1 2026 but has not been scheduled. The SOC team has limited experience with AWS Shield Advanced and the SRT engagement process.

**Risk/Impact:**

- **Response delays:** Without testing, the SOC team may be unfamiliar with Shield Advanced dashboards, SRT engagement procedures, and Route 53 health check failover during an actual DDoS event.
- **Communication gaps:** Untested communication procedures may result in delayed or incomplete notifications to BNM, customers, and internal stakeholders during a DDoS attack.

**Evidence:**

| # | Evidence Item | Reference | Date |
|---|--------------|-----------|------|
| 1 | AWS WAF and Shield Advanced Configuration Export | E-049 | 23 Jan 2026 |
| 2 | BPB Cloud Incident Response Plan (CIRP) | E-098 | Nov 2025 |
| 3 | DDoS Response Playbook -- Tabletop Exercise (Not Conducted) | E-102 | N/A |

**Recommendation:**

1. Schedule and conduct a tabletop exercise for the DDoS response playbook by Q2 2026, involving the SOC team, Cloud Engineering, and the AWS Shield Response Team.
2. Include realistic scenarios (e.g., volumetric attack on CloudFront, application-layer attack on ALB) and test the full communication chain.
3. Document lessons learned and update the playbook based on exercise findings.

**Management Response:**

| Attribute | Detail |
|-----------|--------|
| **Response** | Agree |
| **Remediation Action** | Schedule DDoS tabletop exercise with AWS SRT for Q2 2026. Update playbook based on lessons learned. |
| **Responsible Person** | Puan Nurul Huda binti Ismail, Head of Security Operations |
| **Target Completion Date** | 30 June 2026 |
| **Status** | Not Started |

---

## 5. Negative Attestation Statement

*Per RMIT Appendix 7, Part C, Item 5 (as applicable to cloud assessments under Appendix 10):*

Based on the work performed and the evidence obtained during the assessment period of 20 January 2026 to 21 February 2026, and subject to the scope, methodology, and limitations described in Section 2 of this report:

**Option B -- Attestation with exceptions:**

Nothing has come to our attention that causes us to believe that the technology risk management controls of Bank Perdana Berhad within the scope of this assessment are not, in all material respects, designed and operating effectively as at 21 February 2026, in accordance with the requirements of the Risk Management in Technology Policy Document (November 2025), Appendix 10 (Cloud Services), except for the following matters:

1. **Finding F-001 (High):** Overly permissive IAM policies with wildcard actions, stale service accounts retaining AdministratorAccess for 9 months, and root account usage for non-emergency tasks, resulting in elevated risk of unauthorised access and privilege escalation in the production AWS environment.

2. **Finding F-002 (High):** Incomplete cloud audit logging (S3 data events not enabled), GuardDuty not enabled on the DR account, VPC Flow Logs not integrated with SIEM, and 4 of 12 cloud services not forwarding logs to SIEM, resulting in gaps in threat detection and forensic investigation capability.

3. **Finding F-003 (High):** Cloud exit strategy remains high-level without data retrieval procedures, timeline, or cost estimates; has never been tested; and the contractual exit assistance period is not explicitly defined, creating material vendor dependency risk.

These matters are described in detail in Section 4 of this report.

We recommend that Bank Perdana Berhad remediate the three High-rated findings within the agreed timelines and that CyberAssure Advisory be engaged to verify remediation before the control environment can be attested as effective without exceptions.

---

| | |
|---|---|
| **Name** | Puan Siti Aminah binti Hassan |
| **Designation** | Partner, Technology Risk Advisory |
| **Professional Qualifications** | CISA, CISSP, CCSP, PMP |
| **Organisation** | CyberAssure Advisory Sdn Bhd |
| **Signature** | _________________________________ |
| **Date** | 28 February 2026 |

---

## Appendix A: Evidence List

| # | Evidence ID | Description | Source | Date Obtained | Classification |
|---|-----------|-------------|--------|--------------|---------------|
| 1 | E-001 | BPB Cloud Strategy v2.0 | FI | 20 Jan 2026 | Confidential |
| 2 | E-002 | Board Resolution -- Cloud Strategy Adoption | FI | 20 Jan 2026 | Confidential |
| 3 | E-003 | BPB Cloud Governance Framework | FI | 20 Jan 2026 | Confidential |
| 4 | E-004 | Cloud RACI Matrix -- T24 Migration Programme | FI | 20 Jan 2026 | Internal |
| 5 | E-005 | Cloud Steering Committee ToR | FI | 20 Jan 2026 | Internal |
| 6 | E-006 | Cloud Steering Committee Minutes (3 samples) | FI | 22 Jan 2026 | Confidential |
| 7 | E-007 | Technology Risk Appetite Statement (Cloud Addendum) | FI | 20 Jan 2026 | Confidential |
| 8 | E-020 | AWS SOC 2 Type II Report (Apr 2024 -- Mar 2025) | CSP | 21 Jan 2026 | Confidential |
| 9 | E-021 | AWS ISO 27001:2022 Certificate and SoA | CSP | 21 Jan 2026 | Public |
| 10 | E-028 | BPB-AWS Enterprise Agreement | FI/CSP | 22 Jan 2026 | Confidential |
| 11 | E-034 | Enterprise Agreement -- Schedule 7 (Termination) | FI/CSP | 22 Jan 2026 | Confidential |
| 12 | E-044 | T24 Cloud Logical Architecture -- AWS | FI | 23 Jan 2026 | Confidential |
| 13 | E-050 | GuardDuty and Security Hub Configuration Export | FI | 24 Jan 2026 | Confidential |
| 14 | E-051 | Terraform Module Repository (GitLab) | FI | 27 Jan 2026 | Confidential |
| 15 | E-055 | Drift Detection -- Not Deployed (Gap) | FI | 27 Jan 2026 | Internal |
| 16 | E-066 | AWS Config Change Timeline Export | FI | 27 Jan 2026 | Confidential |
| 17 | E-070 | T24 Cloud DR Architecture and Failover Procedures | FI | 28 Jan 2026 | Confidential |
| 18 | E-074 | BPB Cloud Exit Strategy -- T24/AWS | FI | 28 Jan 2026 | Confidential |
| 19 | E-081 | BPB KMS Key Management Procedures | FI | 29 Jan 2026 | Internal |
| 20 | E-086 | AWS IAM Policy Export -- BPB-PROD-001 | FI | 22 Jan 2026 | Confidential |
| 21 | E-093 | CloudTrail Configuration Export -- All Accounts | FI | 30 Jan 2026 | Confidential |
| 22 | E-095 | SIEM Integration Architecture -- Cloud Log Sources | FI | 30 Jan 2026 | Confidential |
| 23 | E-098 | BPB Cloud Incident Response Plan (CIRP) | FI | 30 Jan 2026 | Confidential |

*Note: This is a representative subset. Full evidence list (103 items) is maintained in the Evidence Tracker (separate document CA/IESP/BPB-CLOUD/2026-001-ET).*

---

## Appendix B: People Interviewed

| # | Name | Title | Organisation | Date | Topics Covered |
|---|------|-------|-------------|------|---------------|
| 1 | Encik Mohd Faizal bin Abdullah | Chief Technology Officer | BPB | 20 Jan 2026 | Cloud strategy, governance, risk appetite, overall programme |
| 2 | Encik Ahmad Razif bin Mohd Yusof | Head of Cloud Engineering | BPB | 21 Jan 2026 | Cloud architecture, IaC, deployment model, DR design |
| 3 | Puan Nurul Huda binti Ismail | Head of Security Operations | BPB | 22 Jan 2026 | Cloud security monitoring, SIEM integration, IR procedures |
| 4 | Encik Tan Wei Ming | Senior Cloud Engineer | BPB | 23 Jan 2026 | IAM configuration, Terraform pipelines, drift issues |
| 5 | Puan Nor Azlina binti Kamaruddin | Head of IT Risk Management | BPB | 24 Jan 2026 | Cloud risk assessment, RMIT compliance mapping, exit strategy |
| 6 | Encik Rajesh Kumar a/l Subramaniam | Temenos T24 Application Lead | BPB | 27 Jan 2026 | T24 application architecture, data flows, DR considerations |
| 7 | Puan Farah Diba binti Mohd Noor | Head of IT Compliance | BPB | 28 Jan 2026 | Regulatory requirements, BNM notifications, contract review |
| 8 | Encik Muhammad Hafiz bin Osman | Database Administrator (Cloud) | BPB | 29 Jan 2026 | RDS Oracle configuration, backup/recovery, KMS key management |
| 9 | Puan Lim Mei Ling | IT Internal Audit Manager | BPB | 30 Jan 2026 | Prior audit findings, cloud control testing, access reviews |
| 10 | Encik Amir Hamzah bin Yusoff | Head of IT Operations | BPB | 3 Feb 2026 | Change management, monitoring, SLA tracking, incident management |
| 11 | Cik Siti Nurhaliza binti Ahmad | DevSecOps Engineer | BPB | 5 Feb 2026 | CI/CD pipeline, container security, ECR scanning, GitLab config |
| 12 | Encik Lee Chong Wei | Network and Security Engineer | BPB | 7 Feb 2026 | VPC architecture, security groups, WAF, Shield Advanced config |
| 13 | Mr James Thornton | AWS Solutions Architect (BPB Account) | AWS | 10 Feb 2026 | AWS architecture review, shared responsibility, service configurations |
| 14 | Ms Priya Menon | AWS Technical Account Manager (BPB) | AWS | 10 Feb 2026 | Enterprise support, SLA performance, incident notifications, SRT |

---

## Appendix C: Documents Reviewed

| # | Document Title | Author/Owner | Version / Date | Relevance |
|---|---------------|-------------|-------------|-----------|
| 1 | BPB Cloud Strategy v2.0 | CTO Office | v2.0, Oct 2025 | Cloud governance and strategic direction |
| 2 | BPB Cloud Governance Framework | IT Risk Management | v1.1, Nov 2025 | Governance structure and accountability |
| 3 | BPB Cloud Adoption Policy | IT Risk Management | v1.2, Nov 2025 | Cloud usage controls and approval workflow |
| 4 | BPB Cloud Security Architecture Document | Cloud Engineering | v1.1, Nov 2025 | Security controls design and defence-in-depth |
| 5 | BPB-AWS Enterprise Agreement | Legal / AWS | 15 Sep 2025 | Contractual obligations and RMIT compliance |
| 6 | AWS SOC 2 Type II Report (Apr 2024 -- Mar 2025) | AWS / Ernst & Young | Mar 2025 | CSP assurance and CUEC identification |
| 7 | BPB Cloud Exit Strategy -- T24/AWS | Cloud Engineering | v1.0, Nov 2025 | Exit readiness assessment |
| 8 | T24 Cloud DR Architecture and Failover Procedures | Cloud Engineering | v1.0, Dec 2025 | DR design and resilience |
| 9 | BPB Cloud Incident Response Plan (CIRP) | Security Operations | v1.0, Nov 2025 | Incident handling and cloud-specific response |
| 10 | BPB KMS Key Management Procedures | Cloud Engineering | v1.0, Nov 2025 | Cryptographic key lifecycle |
| 11 | BPB Cloud IAM Policy | IT Risk Management | v1.0, Oct 2025 | Access control governance |
| 12 | BPB Container Security Standard | Cloud Engineering | v1.0, Nov 2025 | Container security controls |
| 13 | CIS Amazon Web Services Foundations Benchmark v3.0 | CIS | v3.0 | Security configuration benchmark |
| 14 | RMIT Policy Document (November 2025) | BNM | Nov 2025 | Regulatory requirements |
| 15 | RMIT Appendix 10 -- Cloud Services | BNM | Nov 2025 | Cloud-specific regulatory requirements |

---

## Appendix D: Abbreviations

| Abbreviation | Definition |
|-------------|-----------|
| ALB | Application Load Balancer |
| AWS | Amazon Web Services |
| BNM | Bank Negara Malaysia |
| BPB | Bank Perdana Berhad |
| CAB | Change Advisory Board |
| CIRP | Cloud Incident Response Plan |
| CMK | Customer-Managed Key |
| CSP | Cloud Service Provider |
| CSPM | Cloud Security Posture Management |
| CUEC | Complementary User Entity Control |
| DR | Disaster Recovery |
| EBS | Elastic Block Store |
| ECR | Elastic Container Registry |
| ECS | Elastic Container Service |
| IAM | Identity and Access Management |
| IaC | Infrastructure as Code |
| IESP | Independent External Service Provider |
| IoC | Indicator of Compromise |
| KMS | Key Management Service |
| NACL | Network Access Control List |
| PDPA | Personal Data Protection Act |
| RDS | Relational Database Service |
| RMIT | Risk Management in Technology |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SIEM | Security Information and Event Management |
| SOC | Security Operations Centre |
| SRT | Shield Response Team |
| VPC | Virtual Private Cloud |
| WAF | Web Application Firewall |

---

## Appendix E: Report Distribution List

| # | Name | Title | Organisation | Copy # |
|---|------|-------|-------------|--------|
| 1 | Tan Sri Dato' Haji Razaleigh bin Hamzah | Chairman, Board of Directors | BPB | 1 |
| 2 | Datuk Dr. Wan Ahmad bin Wan Ibrahim | Group CEO | BPB | 2 |
| 3 | Encik Mohd Faizal bin Abdullah | Chief Technology Officer | BPB | 3 |
| 4 | Puan Nor Azlina binti Kamaruddin | Head of IT Risk Management | BPB | 4 |
| 5 | Puan Farah Diba binti Mohd Noor | Head of IT Compliance | BPB | 5 |
| 6 | Puan Lim Mei Ling | IT Internal Audit Manager | BPB | 6 |
| 7 | BNM -- Department of IT Risk Supervision | (Regulatory copy) | BNM | 7 |

---

*End of Findings Report*
