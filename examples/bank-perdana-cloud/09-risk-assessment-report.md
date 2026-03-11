> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative.

---

# Risk Assessment Report

## BNM RMIT Appendix 7 Part A

---

**Confidential**

**Report Reference:** CA/IESP/2026/BPB-001/RAR

**Date of Report:** 7 March 2026

**Assessment Period:** 6 January 2026 to 7 March 2026

---

## Section 1: Financial Institution

| Field | Details |
|-------|---------|
| **Name of financial institution** | Bank Perdana Berhad |
| **Company registration number** | 199301012345 |
| **Address of financial institution** | Level 30, Menara Perdana, 50 Jalan Sultan Ismail, 50250 Kuala Lumpur |
| **Type of application** | Cloud service — New |
| **Description** | Migration of core banking system (Temenos T24/Transact R23) from on-premises to Amazon Web Services (AWS) public cloud infrastructure |
| **Contact person** | Encik Ahmad Razali |
| **Designation** | Chief Technology Officer |
| **Telephone number** | +603-2188-5500 |
| **Email address** | ahmad.razali@bankperdana.com.my |

---

## Section 2: External Service Provider

| Field | Details |
|-------|---------|
| **Name of external service provider** | CyberAssure Advisory Sdn Bhd |
| **Company registration number (SSM)** | 201501023456 |
| **Address of external service provider** | Level 18, Menara Cyber, 88 Jalan Bangsar, 59200 Kuala Lumpur |
| **Engagement period** | 6 January 2026 to 14 March 2026 |
| **Contact person** | Puan Siti Nabilah binti Mohd Yusof |
| **Designation** | Director, Technology Risk Advisory |
| **Telephone number** | +603-2201-8800 |
| **Email address** | siti.nabilah@cyberassure.com.my |
| **Professional qualifications** | CISA, CCSP, CISSP |

**Engagement Team:**

| Name | Role | Qualifications |
|------|------|----------------|
| Puan Siti Nabilah binti Mohd Yusof | Engagement Lead | CISA, CCSP, CISSP |
| Encik Lim Wei Keat | Quality Assurance Partner | CISA, CRISC, CISM |
| Encik Hafiz bin Abdullah | Senior Consultant | CCSP, AWS Solutions Architect Professional |
| Puan Priya Devi a/p Ramasamy | Consultant | CISA, AWS Security Specialty |
| Encik Daniel Tan Wei Ming | Consultant | OSCP, CCSP |

---

## Section 3: Detail of Application

### 3.1 Business Case

Bank Perdana Berhad ("BPB" or "the Bank") is undertaking a strategic migration of its core banking system from an aging on-premises infrastructure to Amazon Web Services (AWS) public cloud. The initiative is a cornerstone of the Bank's Digital Transformation Strategy 2024–2028, approved by the Board of Directors in October 2024.

The existing Temenos T24 deployment, hosted in the Bank's Cyberjaya data centre, is approaching end-of-supportable-life on current hardware. The infrastructure is increasingly unable to support the performance and scalability demands of the Bank's growing digital banking channels, which now account for 68% of all transactions. Batch processing windows have expanded from 3 hours to 5.5 hours over the past 18 months, creating operational risk during nightly settlement cycles.

The cloud migration aims to: (i) modernise the core banking infrastructure to enable horizontal scalability and reduce batch processing times to under 2 hours; (ii) strengthen the Bank's digital banking capabilities by leveraging cloud-native services for API-based integrations; (iii) reduce operational risk by eliminating single points of failure inherent in the current architecture; and (iv) achieve long-term cost optimisation through a shift from capital expenditure to operational expenditure. The total approved budget for the migration programme is RM45 million, inclusive of licensing, infrastructure, professional services, and the first two years of cloud operating costs. The system is classified as Critical (Tier 1) under the Bank's IT Criticality Framework, as it processes all customer accounts, deposits, loans, and treasury transactions.

### 3.2 Technology Description

The target architecture deploys Temenos T24/Transact R23 (the latest long-term support release) on AWS infrastructure in the ap-southeast-1 (Singapore) region, with disaster recovery in ap-southeast-3 (Jakarta).

**Compute and Application Layer:** The T24 application tier runs on Amazon EC2 instances (r6i.4xlarge) within an Auto Scaling Group, deployed across three Availability Zones in ap-southeast-1. Container workloads for T24 microservices and API gateway components are orchestrated via Amazon Elastic Kubernetes Service (EKS) version 1.28. The Design Studio and reporting modules are deployed as separate EKS workloads to isolate resource contention.

**Database Layer:** The core banking database is hosted on Amazon RDS Aurora PostgreSQL (version 15.4), configured in a Multi-AZ cluster with one writer and two reader instances. Aurora Global Database provides asynchronous replication to the DR region with a typical replication lag of under 1 second.

**Storage and Content Delivery:** Amazon S3 stores document imaging, regulatory reports, and archival data with S3 Object Lock for WORM compliance. Amazon CloudFront provides content delivery for the internet banking portal with AWS WAF integration.

**Network Connectivity:** AWS Direct Connect (2 x 10 Gbps circuits from two separate carriers) provides dedicated private connectivity from the Bank's Cyberjaya operations centre to the AWS Singapore region. All inter-VPC traffic traverses AWS Transit Gateway. VPN backup is configured over the public internet with IPSec encryption.

**Security Services:** AWS Key Management Service (KMS) with customer-managed keys (CMK) for encryption at rest across all data stores. AWS Shield Advanced for DDoS protection. Amazon GuardDuty for threat detection. AWS CloudTrail and VPC Flow Logs for audit logging. AWS WAF with managed rule sets and custom rules for the internet banking application.

**Disaster Recovery:** Cross-region DR to ap-southeast-3 (Jakarta) using Aurora Global Database, S3 Cross-Region Replication, and pre-provisioned EKS infrastructure with Velero backup. Target RTO of 4 hours and RPO of 1 hour.

### 3.3 Scope of Assessment

This assessment was performed in accordance with the scoping document (reference CA/IESP/2026/BPB-001/SD, dated 10 January 2026) and covers:

- **Systems assessed:** Temenos T24/Transact R23 on AWS, including all supporting AWS services (EC2, RDS Aurora, EKS, S3, CloudFront, Direct Connect, KMS, IAM, CloudTrail, GuardDuty, WAF, Shield Advanced)
- **RMIT requirements covered:** Paragraph 17.1 (pre-implementation prerequisites), Appendix 7 Part D minimum controls, Appendix 10 (all 21 technology risk areas), and relevant provisions of paragraphs 10–16
- **Period of assessment:** 6 January to 7 March 2026
- **Assessment type:** Pre-implementation technology risk assessment for first-time migration of critical system to public cloud

**Exclusions:** End-user devices and branch network infrastructure; third-party integrations beyond the AWS boundary (e.g., RENTAS, PayNet); business process controls within T24 application logic; financial audit of the migration programme budget.

---

## Section 4: Technology Risk Assessment

### 4.1 Assessment Objective

This section provides assurance on the effectiveness of technology risk management controls for the migration of BPB's core banking system to AWS, assessed against the minimum controls specified in Appendix 7 Part D, the requirements of paragraph 17.1, and the 21 technology risk areas set out in Appendix 10 of the RMIT (November 2025).

### 4.2 Assessment Methodology

The assessment was performed using CyberAssure Advisory's proprietary RMIT Assessment Methodology (RAM v4.2), which is aligned with ISACA IT Audit and Assurance Standards and ISO 27001:2022 audit practices. The methodology comprises:

- **Inspection:** Review of 87 documents, policies, configurations, and artefacts provided by BPB and AWS
- **Interview:** 22 interviews conducted with BPB personnel, AWS representatives, and the Temenos implementation partner across all relevant functions
- **Observation:** Direct observation of operational processes including change management, incident handling, and access provisioning workflows
- **Re-performance:** Re-performance of selected controls including access reviews, backup restoration, and DR failover
- **Technical testing:** Automated scanning using CyberAssure's cloud security assessment toolkit (Prowler v3, ScoutSuite, and custom AWS Config rule evaluation), supplemented by manual configuration review

Sampling was performed using risk-based judgemental sampling for document reviews and a minimum sample size of 25 items or 10% (whichever is greater) for transactional controls.

### 4.3 Summary of Assessment Results

**Overall Assessment: Partially Effective**

The Bank has established a generally sound technology risk management framework for the cloud migration, with effective controls in the majority of assessed areas. However, three areas require significant improvement before go-live, and five areas have moderate gaps that should be addressed within defined timelines.

**Assessment Results by Appendix 10 Area:**

| # | Appendix 10 Area | Rating | Findings | Key Observations |
|---|------------------|--------|----------|------------------|
| 1 | Technology Risk Governance | Effective | — | Cloud governance framework established; BRTC oversight adequate |
| 2 | Technology Risk Management Framework | Effective | — | Risk register maintained; cloud-specific risks identified |
| 3 | Technology Operations Management | Effective | F-005 (M) | Operations runbooks in place; IaC drift detection needs improvement |
| 4 | Technology Project Management | Effective | — | Migration programme well-managed with stage gates |
| 5 | Security Operations | Partially Effective | F-002 (H), F-007 (M) | CloudTrail gaps in DR region; incident playbooks incomplete |
| 6 | Identity and Access Management | Partially Effective | F-001 (H) | Excessive IAM permissions; stale service accounts detected |
| 7 | Cryptographic Controls | Effective | F-008 (L) | KMS CMK in use; key rotation was manual (now automated) |
| 8 | Network Security | Effective | — | Direct Connect resilient; security groups well-configured |
| 9 | Application Security | Effective | F-010 (L) | SAST/DAST in CI/CD pipeline; container image scanning gap |
| 10 | Data Security and Privacy | Effective | — | Encryption at rest and in transit; DLP controls in place |
| 11 | Technology Audit Logging | Partially Effective | F-002 (H) | CloudTrail management events only; S3 data events not enabled |
| 12 | Vulnerability Management | Effective | F-004 (M) | Regular scanning; CSPM tool not yet deployed |
| 13 | Patch Management | Effective | — | Automated patching via Systems Manager; EKS node rotation |
| 14 | Change Management | Effective | F-005 (M) | CAB process in place; Terraform state drift detection gap |
| 15 | Capacity Management | Effective | — | Auto Scaling configured; capacity modelling completed |
| 16 | Incident Management | Partially Effective | F-007 (M) | Framework exists; cloud-specific playbooks incomplete |
| 17 | Business Continuity Management | Effective | F-006 (M) | BCP/DRP in place; DR test initially missed RTO target |
| 18 | Cloud Service Provider Management | Effective | — | AWS Enterprise Support; quarterly business reviews |
| 19 | Technology Outsourcing | Effective | — | Contractual controls adequate; exit provisions reviewed |
| 20 | Technology Exit Strategy | Partially Effective | F-003 (H) | Exit strategy documented but not tested; no cost estimate |
| 21 | Emerging Technology Risk | Effective | F-011 (L) | AI/ML risk framework in place; cloud cost optimisation review pending |

**Assessment Results by Part D Minimum Controls:**

| Part D Control | Rating | Findings |
|----------------|--------|----------|
| 1(a) Access Control | Partially Effective | F-001 |
| 1(b) Physical Security | Effective | — (reliance on AWS SOC 2 Type II) |
| 1(c) Operations Security | Effective | — |
| 1(d) Communications Security | Effective | — |
| 1(e) Incident Management | Partially Effective | F-002, F-007 |
| 1(f) Business Continuity Management | Effective | F-006 |
| 2(a) Customer Authentication | Effective | — |
| 2(b) Transaction Authorisation | Effective | — |
| 2(c) Segregation of Duties & Access Control | Effective | — |
| 2(d) Data Integrity | Effective | — |
| 2(e) Mobile Device Security | Effective | — |

**Assessment Against Paragraph 17.1 Prerequisites:**

| # | Prerequisite | Assessment | Finding |
|---|-------------|-----------|---------|
| 1 | Adequate security measures | Partially Met | F-001, F-002 — IAM and logging gaps to be remediated before go-live |
| 2 | Customer support services | Met | 24/7 call centre; digital support channels operational |
| 3 | Performance monitoring established | Met | CloudWatch + Datadog APM; 99.95% availability SLA |
| 4 | Contingency and business resumption plans | Met | BCP/DRP in place; DR test completed 28 Feb 2026 |
| 5 | Adequate resources | Partially Met | F-009 (M) — Cloud CoE staffing adequate but training gap |
| 6 | Constant review of systems and procedures | Partially Met | F-003 — Exit strategy requires periodic testing |

**Findings Summary:**

| Severity | Count | Description |
|----------|-------|-------------|
| Critical | 0 | — |
| High | 3 | IAM excessive permissions (F-001); audit logging gaps (F-002); untested exit strategy (F-003) |
| Medium | 5 | CSPM not deployed (F-004); IaC drift detection (F-005); DR RTO gap (F-006); incomplete playbooks (F-007); cloud skills gap (F-009) |
| Low | 3 | Manual key rotation (F-008); container image scanning (F-010); cost optimisation review (F-011) |
| **Total** | **11** | |

### 4.4 Detailed Assessment Against Part D Minimum Controls

---

#### Control Area: 1(a) Access Control

**RMIT Reference:** Appendix 7 Part D, Item 1(a); Appendix 10 Area 6

**Control Objective:** Ensure that access to the cloud environment and core banking system is restricted to authorised users with appropriate levels of privilege, and that access is reviewed periodically.

**Assessment Procedures Performed:**

1. Reviewed AWS IAM policies, roles, and permission boundaries for the BPB AWS Organisation
2. Analysed IAM Access Analyzer findings and evaluated policy scope against least-privilege principles
3. Reviewed service account inventory and last-activity dates
4. Tested access provisioning and de-provisioning workflows (sample of 30 requests)
5. Reviewed MFA enforcement across all IAM users and federated access via AWS SSO

**Evidence Reviewed:**

- AWS IAM Policy documents and CloudFormation templates (E-023 to E-031)
- IAM Access Analyzer output report dated 15 Feb 2026 (E-032)
- Access provisioning SOP (E-033)
- Active Directory federation configuration (E-034)
- MFA enforcement audit report (E-035)

**Findings:**

**F-001 (High): Excessive IAM Permissions and Stale Service Accounts.** Testing identified that 4 of 12 IAM roles assigned to the T24 application tier have broader permissions than required by the principle of least privilege. Specifically, the `T24-AppServer-Role` includes `s3:*` permissions across all buckets rather than scoped to the T24 data bucket. Additionally, 3 service accounts created during the proof-of-concept phase (Jul 2025) have not been used in over 90 days and retain administrative-level permissions. IAM Access Analyzer had flagged these issues but remediation had not been actioned.

**Assessment Result:** Partially Effective

**Risk Rating:** High

**Recommendation:**

1. Scope all IAM roles to least-privilege permissions using IAM Access Analyzer policy generation based on CloudTrail activity logs
2. Remove or disable all stale service accounts (>90 days inactive) and implement automated lifecycle management
3. Implement a quarterly IAM access review with documented evidence of review and remediation
4. Enforce permission boundaries on all application roles to prevent privilege escalation

**Management Response:**

Management agrees. IAM Access Analyzer deployment completed 3 Mar 2026. Two of four policies have been rescoped. Stale accounts were disabled on 5 Mar 2026. Remaining policy remediation and quarterly review process to be implemented by 15 Apr 2026.

---

#### Control Area: 1(b) Physical Security

**RMIT Reference:** Appendix 7 Part D, Item 1(b); Appendix 10 Area 8

**Control Objective:** Ensure that adequate physical security controls protect the infrastructure hosting the core banking system.

**Assessment Procedures Performed:**

1. Reviewed AWS SOC 2 Type II report (period: 1 Oct 2024 – 30 Sep 2025) for physical security controls
2. Reviewed AWS ISO 27001:2022 certificate for ap-southeast-1 region
3. Assessed BPB's Direct Connect termination points (Cyberjaya data centre) physical security controls
4. Reviewed complementary user entity controls (CUECs) documentation

**Evidence Reviewed:**

- AWS SOC 2 Type II report (E-041)
- AWS ISO 27001:2022 certificate (E-042)
- Cyberjaya data centre physical security assessment report (E-043)
- CUECs mapping document (E-044)

**Findings:**

No findings. AWS physical security controls are independently attested through SOC 2 Type II and ISO 27001 certifications. BPB's Direct Connect termination points in the Cyberjaya data centre have adequate physical security controls including biometric access, CCTV, and environmental monitoring.

**Assessment Result:** Effective

**Risk Rating:** N/A

---

#### Control Area: 1(c) Operations Security

**RMIT Reference:** Appendix 7 Part D, Item 1(c); Appendix 10 Areas 3, 12, 13, 14

**Control Objective:** Ensure that operational procedures for the cloud environment are documented, followed, and subject to change management controls.

**Assessment Procedures Performed:**

1. Reviewed cloud operations runbooks and standard operating procedures
2. Assessed change management process including CAB minutes (sample of 15 changes)
3. Reviewed vulnerability management programme and scanning results
4. Assessed patch management procedures and compliance rates
5. Reviewed infrastructure-as-code (Terraform) management practices

**Evidence Reviewed:**

- Cloud Operations Runbook v2.1 (E-050)
- Change Advisory Board minutes, Jan–Feb 2026 (E-051 to E-054)
- Vulnerability scan reports from Qualys and Prowler (E-055 to E-058)
- AWS Systems Manager Patch Manager compliance dashboard (E-059)
- Terraform repository and state management configuration (E-060)

**Findings:**

Two medium findings relate to this area:

- **F-004 (Medium):** Cloud Security Posture Management (CSPM) tool not yet deployed. While Prowler and ScoutSuite are used for periodic assessments, continuous posture monitoring is not in place.
- **F-005 (Medium):** Terraform state drift detection is not automated. Manual drift reconciliation is performed monthly but configuration drift between Terraform state and actual AWS resources could go undetected between reviews.

**Assessment Result:** Effective (with observations)

**Risk Rating:** Medium

**Recommendation:**

1. Deploy a CSPM tool (e.g., Wiz, Prisma Cloud, or AWS Security Hub with Config Rules) for continuous monitoring
2. Implement automated Terraform drift detection using Terraform Cloud or equivalent, with alerts on detected drift

**Management Response:**

Management agrees. CSPM tool evaluation (Wiz shortlisted) to be completed by Apr 2026. Terraform Cloud trial initiated 1 Mar 2026.

---

#### Control Area: 1(d) Communications Security

**RMIT Reference:** Appendix 7 Part D, Item 1(d); Appendix 10 Area 8

**Control Objective:** Ensure that network communications are secured and monitored.

**Assessment Procedures Performed:**

1. Reviewed network architecture including VPC design, security groups, and NACLs
2. Assessed Direct Connect configuration and redundancy
3. Reviewed TLS configuration for all external-facing endpoints
4. Tested VPN backup connectivity and failover

**Evidence Reviewed:**

- Network architecture diagram v3.2 (E-061)
- Security group and NACL rule matrices (E-062)
- Direct Connect monitoring dashboard and failover test results (E-063)
- TLS configuration audit report (E-064)
- VPN configuration and test results (E-065)

**Findings:**

No findings. Network security controls are well-designed with defence-in-depth. TLS 1.3 is enforced on all external endpoints. Direct Connect redundancy with automatic VPN failover is operational. Security groups follow least-privilege principles with no overly permissive rules identified.

**Assessment Result:** Effective

**Risk Rating:** N/A

---

#### Control Area: 1(e) Incident Management

**RMIT Reference:** Appendix 7 Part D, Item 1(e); Appendix 10 Areas 5, 11, 16

**Control Objective:** Ensure that security incidents are detected, reported, and responded to in a timely manner.

**Assessment Procedures Performed:**

1. Reviewed incident management policy and procedures
2. Assessed SIEM/SOC capabilities for cloud workloads
3. Reviewed Amazon GuardDuty configuration and alert handling
4. Reviewed AWS CloudTrail configuration across all accounts and regions
5. Tested incident response through tabletop exercise review
6. Reviewed cloud-specific incident playbooks

**Evidence Reviewed:**

- Incident Management Policy v5.0 (E-070)
- SOC operations procedures for cloud workloads (E-071)
- GuardDuty configuration and findings dashboard (E-072)
- CloudTrail configuration audit across all accounts (E-073)
- Incident response tabletop exercise report, Dec 2025 (E-074)
- Cloud incident playbooks — draft (E-075)

**Findings:**

Two findings relate to this area:

- **F-002 (High): Insufficient Audit Logging Configuration.** CloudTrail is configured for management events only; S3 data-event logging is not enabled for the T24 data bucket, creating a gap in the ability to detect unauthorised data access. Additionally, GuardDuty is not enabled in the DR region (ap-southeast-3), which means threat detection would be unavailable during a DR failover. The centralised SIEM integration for CloudTrail and VPC Flow Logs is approximately 75% complete, with the remaining log sources (Lambda, EKS audit logs) not yet ingested.
- **F-007 (Medium): Incomplete Cloud-Specific Incident Response Playbooks.** The Bank maintains a comprehensive incident management framework for on-premises systems. However, cloud-specific playbooks are still in development — only 1 of 3 required playbooks (account compromise) has been finalised. The remaining playbooks for data exfiltration and service disruption scenarios are in draft.

**Assessment Result:** Partially Effective

**Risk Rating:** High (F-002), Medium (F-007)

**Recommendation:**

1. Enable CloudTrail S3 data-event logging for all buckets containing customer or financial data
2. Enable GuardDuty in the DR region (ap-southeast-3) immediately
3. Complete SIEM integration for all cloud log sources before go-live
4. Finalise all three cloud incident playbooks and conduct a tabletop exercise before go-live

**Management Response:**

Management agrees with urgency. S3 data events enabled 6 Mar 2026. GuardDuty DR enablement scheduled for 12 Mar 2026. SIEM integration target: 31 Mar 2026. Playbooks target: 20 Mar 2026.

---

#### Control Area: 1(f) Business Continuity Management

**RMIT Reference:** Appendix 7 Part D, Item 1(f); Appendix 10 Area 17

**Control Objective:** Ensure that business continuity and disaster recovery plans are in place and tested for the cloud-hosted core banking system.

**Assessment Procedures Performed:**

1. Reviewed BCP and DRP for cloud-hosted core banking system
2. Assessed DR architecture (cross-region replication, infrastructure pre-provisioning)
3. Reviewed DR test plan and observed DR test execution on 28 Feb 2026
4. Verified RTO/RPO achievement

**Evidence Reviewed:**

- Business Continuity Plan — Core Banking Cloud v1.0, Jan 2026 (E-080)
- Disaster Recovery Plan — AWS Cloud v1.0, Jan 2026 (E-081)
- DR test plan (E-082)
- DR test execution evidence and results, 28 Feb 2026 (E-083)

**Findings:**

- **F-006 (Medium): DR Test Initially Exceeded RTO Target.** The first DR test on 15 Feb 2026 achieved an RTO of 5.2 hours against the target of 4 hours, primarily due to Aurora Global Database failover taking longer than expected (47 minutes vs. planned 15 minutes). The Bank conducted a remediation DR test on 28 Feb 2026, which achieved an RTO of 3.5 hours after optimising the Aurora failover process and pre-warming EKS nodes. While the remediation test met the RTO target, only one successful test has been completed.

**Assessment Result:** Effective (with observations)

**Risk Rating:** Medium

**Recommendation:**

1. Conduct at least one additional DR test before go-live to confirm repeatability
2. Implement automated DR failover orchestration to reduce manual intervention
3. Schedule semi-annual DR tests post go-live

**Management Response:**

Management agrees. Additional DR test scheduled for 25 Mar 2026. Automated DR orchestration using AWS Step Functions to be implemented by Q2 2026.

---

#### Control Area: 2(a) Customer Authentication

**RMIT Reference:** Appendix 7 Part D, Item 2(a)

**Control Objective:** Ensure robust customer authentication mechanisms are in place for the cloud-hosted core banking system and its digital channels.

**Assessment Procedures Performed:**

1. Reviewed authentication architecture for internet and mobile banking
2. Assessed multi-factor authentication implementation
3. Reviewed password policy and session management controls
4. Tested authentication controls against OWASP guidelines

**Evidence Reviewed:**

- Authentication architecture document (E-090)
- MFA implementation specification (E-091)
- Penetration test report — authentication module, Jan 2026 (E-092)

**Findings:**

No findings. Customer authentication controls are robust, with risk-based adaptive MFA, device fingerprinting, and session timeout controls aligned with RMIT requirements and industry best practices.

**Assessment Result:** Effective

**Risk Rating:** N/A

---

#### Control Area: 2(b) Transaction Authorisation

**RMIT Reference:** Appendix 7 Part D, Item 2(b)

**Control Objective:** Ensure that transaction authorisation controls prevent unauthorised transactions.

**Assessment Procedures Performed:**

1. Reviewed transaction authorisation workflows within T24
2. Assessed maker-checker controls for high-value transactions
3. Reviewed transaction signing mechanisms
4. Tested transaction limits and threshold alerts

**Evidence Reviewed:**

- T24 transaction authorisation matrix (E-095)
- Maker-checker configuration evidence (E-096)
- Transaction monitoring rules (E-097)

**Findings:**

No findings. Transaction authorisation controls are appropriately configured with maker-checker enforcement, transaction signing for high-risk operations, and real-time monitoring with threshold-based alerts.

**Assessment Result:** Effective

**Risk Rating:** N/A

---

#### Control Area: 2(c) Segregation of Duties and Access Control

**RMIT Reference:** Appendix 7 Part D, Item 2(c)

**Control Objective:** Ensure appropriate segregation of duties across development, operations, and security functions.

**Assessment Procedures Performed:**

1. Reviewed organisational structure and role definitions for cloud operations
2. Assessed AWS account structure and OU-level separation
3. Tested SoD enforcement in CI/CD pipeline (developer vs. deployer roles)
4. Reviewed T24 user role matrix for SoD conflicts

**Evidence Reviewed:**

- AWS Organisations structure and OU design (E-100)
- CI/CD pipeline role configuration (E-101)
- T24 role-based access control matrix (E-102)
- SoD conflict analysis report (E-103)

**Findings:**

No findings. The Bank has implemented a well-structured AWS Organisation with separate accounts for production, staging, development, security, and logging. The CI/CD pipeline enforces separation between code commit, review, and deployment roles. No SoD conflicts were identified in the T24 user role matrix.

**Assessment Result:** Effective

**Risk Rating:** N/A

---

#### Control Area: 2(d) Data Integrity

**RMIT Reference:** Appendix 7 Part D, Item 2(d)

**Control Objective:** Ensure the integrity of data processed and stored in the cloud environment.

**Assessment Procedures Performed:**

1. Reviewed data integrity controls in the T24 database layer
2. Assessed Aurora PostgreSQL integrity features (checksums, WAL verification)
3. Reviewed data migration integrity validation plan
4. Tested backup integrity verification procedures

**Evidence Reviewed:**

- Data migration plan and integrity validation framework (E-106)
- Aurora configuration for data integrity (E-107)
- Backup verification test results (E-108)

**Findings:**

No findings. Data integrity controls are comprehensive, with database-level checksums, WAL-based consistency verification, and a robust data migration validation plan that includes row-count reconciliation, hash-based verification, and parallel-run comparison.

**Assessment Result:** Effective

**Risk Rating:** N/A

---

#### Control Area: 2(e) Mobile Device Security

**RMIT Reference:** Appendix 7 Part D, Item 2(e)

**Control Objective:** Ensure that mobile banking channels accessing the cloud-hosted core banking system are adequately secured.

**Assessment Procedures Performed:**

1. Reviewed mobile banking application security architecture
2. Assessed mobile device management (MDM) for staff devices accessing cloud management consoles
3. Reviewed mobile application penetration test results

**Evidence Reviewed:**

- Mobile banking security architecture (E-110)
- MDM policy and configuration (E-111)
- Mobile application penetration test report, Dec 2025 (E-112)

**Findings:**

No findings. Mobile banking security controls include certificate pinning, runtime application self-protection (RASP), jailbreak/root detection, and secure local storage. Staff access to AWS management consoles from mobile devices requires MDM enrolment and MFA.

**Assessment Result:** Effective

**Risk Rating:** N/A

---

### 4.5 Additional Findings

The following findings, while not directly mapped to a single Part D control, were identified during the assessment of Appendix 10 areas:

#### F-004 (Medium): Cloud Security Posture Management Tool Not Deployed

- **Appendix 10 Area:** 12 — Vulnerability Management
- **Description:** The Bank has not deployed a continuous Cloud Security Posture Management (CSPM) tool. Misconfiguration detection relies on periodic Prowler and ScoutSuite scans (monthly), leaving a window for configuration drift to go undetected.
- **Recommendation:** Deploy a CSPM tool for continuous monitoring before go-live.
- **Management Response:** Wiz evaluation in progress. Target deployment: April 2026.

#### F-005 (Medium): Infrastructure-as-Code Drift Detection Not Automated

- **Appendix 10 Area:** 14 — Change Management
- **Description:** Terraform state drift detection is performed manually on a monthly basis. Automated drift detection is not configured, meaning out-of-band changes to AWS resources may not be detected promptly.
- **Recommendation:** Implement Terraform Cloud or equivalent with automated drift detection and alerting.
- **Management Response:** Terraform Cloud trial started 1 Mar 2026. Target: April 2026.

#### F-008 (Low): Manual Cryptographic Key Rotation

- **Appendix 10 Area:** 7 — Cryptographic Controls
- **Description:** At the time of initial testing, KMS CMK rotation was performed manually. While keys were rotated within the required 365-day cycle, manual processes introduce risk of missed rotations.
- **Recommendation:** Enable automatic key rotation for all KMS CMKs.
- **Management Response:** Auto-rotation enabled 25 Feb 2026. Finding considered remediated.

#### F-009 (Medium): Cloud Skills Gap in Operations Team

- **Appendix 10 Area:** 15 — Capacity Management / Resources
- **Description:** Of the 8-person Cloud Centre of Excellence (CoE), only 3 members hold AWS professional-level certifications. The remaining 5 members are at associate level or uncertified, which may be insufficient for managing a Tier 1 critical system on AWS.
- **Recommendation:** Implement a structured training plan to ensure all CoE members achieve at minimum AWS Solutions Architect Associate and Security Specialty certifications within 12 months.
- **Management Response:** Training plan approved. Target: all certifications by Dec 2026.

#### F-010 (Low): Container Image Scanning Gap

- **Appendix 10 Area:** 9 — Application Security
- **Description:** While the CI/CD pipeline includes SAST and DAST scanning, container image vulnerability scanning is not integrated into the build pipeline. Images are scanned ad hoc using Amazon ECR native scanning, but this is not enforced as a pipeline gate.
- **Recommendation:** Integrate container image scanning (e.g., Trivy, Snyk Container) as a mandatory pipeline gate.
- **Management Response:** Trivy evaluation in progress. Target: Q2 2026.

#### F-011 (Low): Cloud Cost Optimisation Review Pending

- **Appendix 10 Area:** 21 — Emerging Technology Risk
- **Description:** A formal cloud cost optimisation review has not been conducted. While the migration budget has been approved, the Bank has not established cost anomaly detection or reserved instance planning to manage ongoing cloud operating costs.
- **Recommendation:** Conduct a cloud cost optimisation review and implement AWS Cost Anomaly Detection and budgeting alerts.
- **Management Response:** Planned for Q2 2026 post go-live.

### 4.6 Consideration of Prior Assessments

This is the first IESP assessment for BPB's cloud infrastructure. There are no prior assessment findings to evaluate. The Bank's most recent internal audit of IT general controls (September 2025) was reviewed and no open findings are directly relevant to the cloud migration scope.

---

## Section 5: Quality Assurance

### 5.1 Overall Recommendation

Based on the assessment performed, the ESP provides the following overall recommendation:

- [ ] **Recommend** — The technology risk management controls assessed are effective and the FI may proceed.

- [x] **Recommend with Conditions** — The technology risk management controls assessed are partially effective. The FI may proceed subject to the remediation of the conditions listed below prior to the planned go-live date (May 2026).

- [ ] **Do not recommend** — The technology risk management controls assessed are ineffective.

### 5.2 Conditions

The following three conditions, corresponding to the three High-rated findings, must be remediated prior to the planned go-live date:

| # | Condition | Finding | Priority | Required Completion Date |
|---|-----------|---------|----------|------------------------|
| 1 | Remediate all excessive IAM permissions and implement automated stale account lifecycle management | F-001 | High | 30 April 2026 |
| 2 | Enable comprehensive audit logging (S3 data events, GuardDuty in DR region, complete SIEM integration) | F-002 | High | 30 April 2026 |
| 3 | Conduct a full exit strategy test including data extraction, portability validation, and cost estimation | F-003 | High | 30 April 2026 |

Evidence of remediation for all three conditions must be provided to CyberAssure Advisory for verification before the Bank proceeds to production go-live.

### 5.3 Key Considerations for the Board / Senior Management

The following matters are highlighted for the Board Risk and Technology Committee's attention, in accordance with paragraph 8.3 of the RMIT:

1. **IAM hygiene is fundamental to cloud security.** Excessive permissions in a cloud environment can be exploited rapidly and at scale. The Board should ensure that the remediation of F-001 is treated as a pre-go-live blocker and that ongoing IAM governance is embedded into operational processes.

2. **Audit logging completeness is a regulatory imperative.** Incomplete logging in the DR region means that during a disaster recovery event, the Bank would have reduced ability to detect and investigate security incidents. This directly impacts the Bank's ability to meet BNM's expectations for security monitoring in paragraph 11.3 of the RMIT.

3. **Cloud exit strategy readiness.** While the Bank has documented an exit strategy, it has not been tested. Given that this is a Tier 1 critical system, the Board should satisfy itself that the Bank can extract its data and migrate to an alternative platform if required. This is particularly important given the cross-border nature of the deployment (data hosted in Singapore).

4. **Cross-border data considerations.** Customer data will be processed and stored in AWS Singapore (ap-southeast-1) and Jakarta (ap-southeast-3). The Board should confirm that all necessary regulatory approvals for cross-border data processing have been obtained and that data sovereignty controls are in place.

5. **Cloud operational maturity.** This is the Bank's first critical system on public cloud. The Cloud CoE is relatively new and the skills gap identified in F-009 should be addressed proactively. The Board should monitor the training programme progress.

### 5.4 Negative Attestation

**Option B — Attestation with Exceptions:**

Based on the work performed and the evidence obtained during the period 6 January to 7 March 2026, nothing has come to our attention that causes us to believe that the technology risk management controls within the scope of this assessment are not, in all material respects, designed and operating effectively, **except for the following matters:**

1. **F-001 (High):** Excessive IAM permissions and stale service accounts in the AWS environment, indicating gaps in access control governance.
2. **F-002 (High):** Insufficient audit logging configuration, including the absence of S3 data-event logging and GuardDuty in the disaster recovery region.
3. **F-003 (High):** The cloud exit strategy has not been tested, and no cost estimate for exit has been prepared.

These exceptions are reflected in the three conditions set out in Section 5.2 above.

### 5.5 Limitations and Caveats

1. This assessment is based on the information, documentation, and access provided by Bank Perdana Berhad during the assessment period of 6 January to 7 March 2026.
2. The assessment provides reasonable assurance and is subject to the inherent limitations of any assessment process, including the possibility that material misstatements or control weaknesses may exist but not be detected.
3. The scope of this assessment is limited to the areas described in Section 3.3. Items explicitly excluded from scope are not covered by this report's conclusions.
4. This report is prepared solely for the use of Bank Perdana Berhad and Bank Negara Malaysia and should not be relied upon by any other party without the prior written consent of CyberAssure Advisory Sdn Bhd.
5. The assessment of AWS physical and environmental controls is based on reliance on independent third-party assurance reports (SOC 2 Type II, ISO 27001). CyberAssure Advisory did not perform independent testing of AWS data centre controls.
6. The assessment reflects the state of controls as at the date of testing. Controls may change subsequent to the assessment, and this report does not provide assurance on the state of controls after the assessment period.

---

## Section 6: Authorised Signatory

### External Service Provider

I confirm that this risk assessment report has been prepared in accordance with professional standards and the requirements of the RMIT (November 2025). The assessment was conducted with objectivity and independence, and the findings represent our professional opinion based on the evidence obtained.

| | |
|---|---|
| **Name** | Puan Siti Nabilah binti Mohd Yusof |
| **Designation** | Director, Technology Risk Advisory |
| **Professional Qualifications** | CISA, CCSP, CISSP |
| **Signature** | *[Signed]* |
| **Date** | 7 March 2026 |
| **Company Stamp** | CyberAssure Advisory Sdn Bhd (201501023456) |

### Quality Review (Internal to ESP)

| | |
|---|---|
| **Reviewed by** | Encik Lim Wei Keat |
| **Designation** | Partner, Risk Advisory |
| **Professional Qualifications** | CISA, CRISC, CISM |
| **Signature** | *[Signed]* |
| **Date** | 7 March 2026 |

---

## Appendices

### Appendix I: Detailed Findings Register

Refer to the separate Detailed Findings Register (reference CA/IESP/2026/BPB-001/FR, dated 7 March 2026) which contains the full finding narratives, root cause analysis, evidence references, and management responses for all 11 findings.

### Appendix II: Evidence Inventory

A total of 87 evidence items were collected and reviewed during the assessment. The complete evidence inventory is maintained in the Evidence Tracker (reference CA/IESP/2026/BPB-001/ET). Key evidence categories include:

| Category | Count |
|----------|-------|
| Policies and procedures | 18 |
| Architecture and design documents | 12 |
| Configuration evidence (screenshots, exports) | 24 |
| Test reports (penetration test, DR test, UAT) | 8 |
| Third-party assurance reports (AWS SOC 2, ISO) | 4 |
| Meeting minutes and approvals | 9 |
| Training and certification records | 5 |
| Contracts and SLAs | 7 |
| **Total** | **87** |

### Appendix III: Personnel Interviewed

| # | Name | Title | Organisation | Date |
|---|------|-------|-------------|------|
| 1 | Encik Ahmad Razali | Chief Technology Officer | Bank Perdana Berhad | 13 Jan 2026 |
| 2 | Puan Faridah binti Hassan | Chief Information Security Officer | Bank Perdana Berhad | 14 Jan 2026 |
| 3 | Encik Raj Kumar a/l Subramaniam | Head of Cloud Engineering | Bank Perdana Berhad | 15 Jan 2026 |
| 4 | Puan Norazlina binti Ismail | Head of IT Operations | Bank Perdana Berhad | 15 Jan 2026 |
| 5 | Encik Tan Chee Keong | DBA Lead — Aurora Migration | Bank Perdana Berhad | 20 Jan 2026 |
| 6 | Puan Aisha binti Omar | Head of Network Security | Bank Perdana Berhad | 20 Jan 2026 |
| 7 | Encik Wong Kar Wai | IAM Lead | Bank Perdana Berhad | 22 Jan 2026 |
| 8 | Puan Shalini a/p Krishnan | Head of IT Risk Management | Bank Perdana Berhad | 23 Jan 2026 |
| 9 | Encik Mohd Faisal bin Othman | Head of Business Continuity | Bank Perdana Berhad | 27 Jan 2026 |
| 10 | Puan Lee Mei Ling | SOC Manager | Bank Perdana Berhad | 28 Jan 2026 |
| 11 | Encik Azman bin Yusof | Migration Programme Manager | Bank Perdana Berhad | 29 Jan 2026 |
| 12 | Puan Nurul Huda binti Razak | Head of Compliance | Bank Perdana Berhad | 30 Jan 2026 |
| 13 | Encik Vikram Singh | Solutions Architect | AWS Malaysia | 3 Feb 2026 |
| 14 | Puan Chen Wei Lin | Enterprise Support TAM | AWS Malaysia | 3 Feb 2026 |
| 15 | Encik Kamal bin Ibrahim | T24 Project Lead | Temenos Malaysia | 5 Feb 2026 |
| 16 | Puan Anita Devi | T24 Security Architect | Temenos Malaysia | 5 Feb 2026 |
| 17 | Encik Hafiz bin Hamid | Cloud CoE Engineer | Bank Perdana Berhad | 10 Feb 2026 |
| 18 | Puan Zainab binti Ali | Change Manager | Bank Perdana Berhad | 11 Feb 2026 |
| 19 | Encik David Lim | DevOps Lead | Bank Perdana Berhad | 12 Feb 2026 |
| 20 | Puan Rosnah binti Abdullah | Head of Internal Audit | Bank Perdana Berhad | 17 Feb 2026 |
| 21 | Encik Ahmad Razali | CTO — Exit Briefing | Bank Perdana Berhad | 5 Mar 2026 |
| 22 | Puan Faridah binti Hassan | CISO — Findings Discussion | Bank Perdana Berhad | 5 Mar 2026 |

### Appendix IV: Documents Reviewed

| # | Document Title | Version/Date | Classification |
|---|---------------|-------------|---------------|
| 1 | BPB Digital Transformation Strategy 2024–2028 | v1.0, Oct 2024 | Confidential |
| 2 | Cloud Migration Business Case | v2.1, Sep 2025 | Confidential |
| 3 | AWS Cloud Architecture Design Document | v3.2, Dec 2025 | Confidential |
| 4 | Information Security Policy | v6.0, Jul 2025 | Internal |
| 5 | Cloud Security Standard | v1.0, Nov 2025 | Internal |
| 6 | IAM Policy and Procedures | v2.0, Oct 2025 | Internal |
| 7 | Incident Management Policy | v5.0, Aug 2025 | Internal |
| 8 | Business Continuity Plan — Core Banking Cloud | v1.0, Jan 2026 | Confidential |
| 9 | Disaster Recovery Plan — AWS Cloud | v1.0, Jan 2026 | Confidential |
| 10 | Cloud Exit Strategy | v1.0, Dec 2025 | Confidential |
| 11 | AWS SOC 2 Type II Report | Oct 2024–Sep 2025 | Restricted |
| 12 | AWS Enterprise Support Agreement | Dec 2025 | Confidential |
| 13 | Penetration Test Report — Cloud Infrastructure | Jan 2026 | Confidential |
| 14 | T24/Transact R23 Security Configuration Guide | v1.2, Nov 2025 | Confidential |
| 15 | Data Migration Plan and Validation Framework | v2.0, Dec 2025 | Confidential |

### Appendix V: Abbreviations and Definitions

| Term | Definition |
|------|-----------|
| BNM | Bank Negara Malaysia |
| BPB | Bank Perdana Berhad |
| BRTC | Board Risk and Technology Committee |
| CAB | Change Advisory Board |
| CMK | Customer-Managed Key |
| CoE | Centre of Excellence |
| CSPM | Cloud Security Posture Management |
| DR | Disaster Recovery |
| DRP | Disaster Recovery Plan |
| EKS | Elastic Kubernetes Service |
| ESP | External Service Provider |
| FI | Financial Institution |
| IAM | Identity and Access Management |
| IaC | Infrastructure as Code |
| IESP | Independent External Service Provider |
| KMS | Key Management Service |
| MFA | Multi-Factor Authentication |
| NACL | Network Access Control List |
| RASP | Runtime Application Self-Protection |
| RDS | Relational Database Service |
| RMIT | Risk Management in Technology |
| RPO | Recovery Point Objective |
| RTO | Recovery Time Objective |
| SIEM | Security Information and Event Management |
| SoD | Segregation of Duties |
| SOC | Security Operations Centre |
| VPC | Virtual Private Cloud |
| WAF | Web Application Firewall |

---

*End of Risk Assessment Report*
