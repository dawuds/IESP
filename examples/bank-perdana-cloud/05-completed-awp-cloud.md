> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative.

# Completed Cloud IESP Audit Work Program
## Bank Perdana Berhad — Temenos T24/Transact R23 Migration to AWS ap-southeast-1

### Engagement Details

| Field | Detail |
|-------|--------|
| **Client** | Bank Perdana Berhad |
| **IESP** | CyberAssure Advisory Sdn Bhd |
| **Engagement Type** | Cloud IESP Assessment |
| **Regulatory Basis** | BNM RMiT Nov 2025 — Paragraph 17.1 |
| **Scope** | Temenos T24/Transact R23 on AWS ap-southeast-1 (IaaS/PaaS) |
| **CSP** | Amazon Web Services (AWS) |
| **Engagement Period** | 6 Jan 2026 – 28 Feb 2026 |
| **Report Date** | 6 Mar 2026 |
| **Engagement Partner** | Rizal Ahmad, CyberAssure Advisory |
| **Assessment Team** | SNI — Siti Nabilah Ibrahim (Lead), HZ — Hafiz Zakaria, AK — Aisha Kaur, DT — Darren Tan, ML — Mei Ling Ong |

---

### Findings Summary

| ID | Title | Rating | Related CLD Tests |
|----|-------|--------|-------------------|
| F-001 | IAM governance gaps — stale accounts, overly permissive policies, incomplete MFA | High | CLD-18 |
| F-002 | Logging and SIEM integration gaps — CloudTrail not forwarded to SIEM for all accounts | High | CLD-19, CLD-22 |
| F-003 | Cloud exit strategy documented but untested | High | CLD-15, CLD-16 |
| F-004 | No CSPM tool deployed; misconfigurations detected manually | Medium | CLD-19, CLD-25 |
| F-005 | IaC drift detection not operational; manual console changes unreconciled | Medium | CLD-11, CLD-13 |
| F-006 | DR failover to ap-southeast-3 untested for Temenos workload | Medium | CLD-14, CLD-23 |
| F-007 | Cloud-specific incident response playbook incomplete — no CSP-outage scenario | Medium | CLD-23 |
| F-008 | KMS CMK rotation not enabled for 4 of 11 customer-managed keys | Medium | CLD-17 |
| F-009 | Cloud skills training plan exists but 3 of 8 cloud engineers lack AWS certifications | Low | CLD-08 |
| F-010 | Container image scanning enabled but not enforced as pipeline gate | Low | CLD-12 |
| F-011 | DDoS response playbook documented but never drill-tested | Low | CLD-20 |

---

### Phase 1: Planning and Scoping — Completed

| Step | Activity | Completed By | Date | Working Paper | Notes |
|------|----------|-------------|------|---------------|-------|
| P-01 | Obtained cloud services inventory — AWS ap-southeast-1, IaaS (EC2, EBS) and PaaS (RDS Aurora, ElastiCache, S3, EKS). Temenos T24 R23 core banking identified as critical system. | SNI | 8 Jan 2026 | WP-CLD-P01 | Inventory confirmed 47 AWS accounts under Bank Perdana AWS Organisation. Temenos workload spans 3 accounts (Prod, UAT, DR). |
| P-02 | Obtained cloud risk assessment v3.1 dated Sep 2025, approved by CRCO. Data classification: customer PII and transaction data classified as Restricted; config/logs as Confidential. | SNI | 9 Jan 2026 | WP-CLD-P02 | Risk assessment covers data sovereignty, shared tenancy, vendor lock-in, supply chain. Annual review cycle confirmed. |
| P-03 | Mapped critical systems to CSP and regions. Temenos T24 Prod in ap-southeast-1a/1b (multi-AZ). DR designated for ap-southeast-3 (Jakarta). | HZ | 10 Jan 2026 | WP-CLD-P03 | Internet/mobile banking front-end also in ap-southeast-1, behind CloudFront. |
| P-04 | Obtained AWS SOC 2 Type II report (period 1 Oct 2024 – 30 Sep 2025), AWS ISO 27001 certificate (valid to Dec 2026), and CSA STAR Level 2 report (Sep 2025). | AK | 10 Jan 2026 | WP-CLD-P04 | SOC 2 had no qualifications. 4 CUECs identified — tracked in CUEC matrix. |
| P-05 | Reviewed prior Cloud IESP report (Mar 2024, conducted by TechAudit Partners). 6 prior findings — 5 closed, 1 open (F-PRIOR-04 partial: exit strategy testing still pending). | SNI | 13 Jan 2026 | WP-CLD-P05 | Open finding F-PRIOR-04 directly relevant to current scope — tracked forward. |
| P-06 | Mapped shared responsibility: AWS responsible for physical, hypervisor, and managed service infrastructure. Bank Perdana responsible for IAM, OS patching (EC2), encryption config, network security groups, application security. MSP (CloudOps Malaysia Sdn Bhd) manages day-to-day infrastructure ops. | DT | 14 Jan 2026 | WP-CLD-P06 | Tri-party RACI obtained and reviewed. |

---

### Phase 2: Detailed Testing — Completed

---

## Part A: Cloud Governance

#### A1: Cloud Risk Management

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-01 | Verify cloud-specific risk assessment | 1. Obtained "Bank Perdana Cloud Risk Assessment Framework v3.1" dated 15 Sep 2025, approved by Chief Risk & Compliance Officer (CRCO) Encik Faizal.<br>2. Framework covers: data sovereignty (Malaysia-first policy), vendor lock-in (assessed as Medium), shared tenancy (Low — dedicated tenancy for RDS), supply chain (Medium), regulatory compliance (mapped to RMiT).<br>3. Risk register section CLD contains 23 risks assessed per AWS service.<br>4. Last annual review: 15 Sep 2025, next due Sep 2026. | **Pass** | SNI | 16 Jan 2026 | WP-CLD-01 | — |
| CLD-02 | Verify cloud risk appetite and tolerance | 1. "Cloud Risk Appetite Statement v2.0" dated 12 Aug 2025 defines: Restricted data may reside in AWS ap-southeast-1 only, with CMK encryption. No Restricted data in non-approved regions.<br>2. Data classification-to-cloud mapping matrix reviewed — 4 tiers mapped to permitted cloud services and controls.<br>3. Approved by Board Risk Committee on 28 Aug 2025 (BRC minutes ref BRC-2025-08-003). | **Pass** | SNI | 16 Jan 2026 | WP-CLD-02 | — |

#### A2: Cloud Usage Policy

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-03 | Verify cloud usage policy | 1. "Cloud Usage and Adoption Policy POL-CLD-001 v4.0" dated 1 Jul 2025 obtained. Covers: approved CSPs (AWS only for Restricted data), approved service models (IaaS/PaaS — SaaS requires separate approval), deployment model (public cloud with VPC isolation), data classification requirements, security baseline, and approval workflow (Cloud Architecture Review Board — CARB).<br>2. Policy communicated via mandatory e-learning module (93% completion as at Dec 2025).<br>3. Sampled 3 recent cloud service adoptions: (i) EKS adoption for Temenos API gateway — CARB approval 12 May 2025; (ii) ElastiCache adoption — CARB approval 3 Jun 2025; (iii) AWS Glue for ETL — CARB approval 18 Jul 2025. All followed policy. | **Pass** | AK | 20 Jan 2026 | WP-CLD-03 | — |

#### A3: Due Diligence

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-04 | Verify due diligence before CSP engagement | 1. "CSP Due Diligence Procedure SOP-CLD-DD-001 v2.0" obtained.<br>2. AWS due diligence report dated 20 Mar 2025 covers: financial viability (AWS Inc. public filings reviewed), security capabilities (SOC 2, ISO 27001, CSA STAR), regulatory compliance (confirmed ap-southeast-1 data residency), data residency (confirmed Malaysia region), subcontracting (AWS sub-processor list reviewed), and BCP (AWS multi-AZ architecture).<br>3. Annual refresh schedule confirmed — next refresh due Mar 2026. | **Pass** | AK | 21 Jan 2026 | WP-CLD-04 | — |

#### A4: CSP Certifications

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-05 | Verify CSP certifications and assurance reports | 1. AWS SOC 2 Type II (Oct 2024 – Sep 2025) — covers EC2, RDS, S3, EKS, KMS, CloudTrail, IAM. Services align with Bank Perdana's usage.<br>2. AWS ISO 27001 certificate (scope: global infrastructure including ap-southeast-1), valid to Dec 2026.<br>3. CSA STAR Level 2 — Sep 2025, no material exceptions.<br>4. SOC 2 report reviewed — no qualifications. 4 CUECs identified: (i) customer must configure MFA, (ii) customer must enable CloudTrail, (iii) customer must configure S3 bucket policies, (iv) customer must manage IAM policies. Bank Perdana CUEC implementation matrix obtained and cross-checked — CUECs (i) and (iv) have gaps noted under CLD-18 / F-001.<br>5. No deficiencies requiring FI risk assessment adjustment. | **Pass** | AK | 22 Jan 2026 | WP-CLD-05 | — |

#### A5: Contract Management

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-06 | Verify CSP contracts contain required provisions | 1. AWS Enterprise Agreement (EA) dated 1 Jan 2025, supplemented by AWS Malaysia Addendum dated 15 Feb 2025.<br>2. Reviewed against checklist: (i) Right to audit — AWS provides SOC/ISO reports in lieu of direct audit, with provision for regulator access upon request — **compliant**; (ii) Data ownership — EA clause 7.1 confirms customer data ownership — **compliant**; (iii) Data residency — Malaysia Addendum clause 3 restricts data to ap-southeast-1 — **compliant**; (iv) Breach notification — AWS commits to 72-hour notification — **compliant**; (v) Subcontracting — sub-processor list with notification of changes — **compliant**; (vi) Termination and exit — 90-day data retrieval period post-termination — **compliant**; (vii) Regulatory access — BNM inspection rights clause present — **compliant**.<br>3. Legal and Compliance review sign-off dated 20 Jan 2025 confirmed. | **Pass** | DT | 23 Jan 2026 | WP-CLD-06 | — |

#### A6: Oversight over CSPs

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-07 | Verify ongoing CSP monitoring and oversight | 1. "CSP Oversight Framework v2.0" dated Jun 2025 obtained. Defines quarterly service reviews, SLA monitoring, incident tracking.<br>2. AWS SLA performance reports for Q2-Q4 2025 reviewed — 99.98% availability (SLA target 99.95%). No SLA breach.<br>3. Quarterly service review meeting minutes obtained: 15 Jul 2025, 14 Oct 2025, 13 Jan 2026 — attended by Bank Perdana Cloud Ops, AWS Technical Account Manager (TAM).<br>4. AWS Health Dashboard notifications tracked in ServiceNow — 12 notifications in review period, all assessed for impact within 4 hours.<br>5. AWS Security Bulletins monitored via automated feed — 3 relevant advisories actioned (patched within SLA). | **Pass** | DT | 24 Jan 2026 | WP-CLD-07 | — |

#### A7: Skilled Personnel

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-08 | Verify FI has sufficient skilled cloud personnel | 1. Cloud Engineering team org chart: 8 FTEs (1 Head of Cloud, 2 Senior Cloud Engineers, 3 Cloud Engineers, 1 Cloud Security Engineer, 1 FinOps Analyst).<br>2. Certification records: 5 of 8 hold AWS certifications (2x AWS Solutions Architect Professional, 1x AWS Security Specialty, 1x AWS DevOps Professional, 1x AWS Cloud Practitioner). 3 engineers (hired Q3 2025) do not yet hold AWS certifications.<br>3. Training plan "Cloud Skills Development Plan FY2026" dated Nov 2025 exists — targets certification for all engineers by Dec 2026.<br>4. Independent assessment capability: Cloud Security Engineer demonstrated ability to run AWS Config rules, review IAM policies, and assess Security Hub findings without CSP assistance. However, depth of Temenos-on-AWS specific expertise is developing. | **Partial** | ML | 27 Jan 2026 | WP-CLD-08 | **F-009** |

---

## Part B: Cloud Design and Control

#### B1: Cloud Architecture

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-09 | Verify cloud architecture resilience and security | 1. "Temenos T24 AWS Architecture Design Document v2.3" dated Oct 2025 and associated diagrams obtained.<br>2. Multi-AZ confirmed: EC2 application tier across ap-southeast-1a and 1b with ALB; RDS Aurora multi-AZ with read replica; S3 with cross-AZ replication by default.<br>3. AWS Well-Architected Review conducted by AWS SA team on 8 Aug 2025 — report obtained, 4 improvement items identified (all addressed by Nov 2025).<br>4. VPC design: 3 VPCs (Prod, UAT, Management) with subnet segmentation — public subnets (ALB only), private subnets (app tier), isolated subnets (DB tier). Security groups follow least-privilege. NACLs enforce deny-by-default at subnet boundary.<br>5. Architecture reviewed and approved by Cloud Architecture Review Board (CARB) on 15 Oct 2025. | **Pass** | HZ | 28 Jan 2026 | WP-CLD-09 | — |

#### B2: Application Delivery Models (CI/CD, IaC)

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-10 | Verify CI/CD pipeline security controls | 1. CI/CD architecture: GitLab CI/CD (self-hosted on AWS) with pipelines for Temenos customisations and infrastructure code.<br>2. Security gates: SAST (SonarQube — integrated), SCA (Snyk — integrated), DAST (OWASP ZAP — integrated for API endpoints). Container image scanning (Trivy) is integrated but configured as advisory only (does not block — see CLD-12 / F-010).<br>3. Production deployment requires approval from Release Manager and Cloud Ops Lead via GitLab merge request approval — verified in pipeline configuration and sampled 5 recent deployments.<br>4. Pipeline YAML stored in GitLab repos with branch protection (main branch requires 2 approvals). Access restricted to DevOps team (8 users).<br>5. Secrets managed via AWS Secrets Manager — no hardcoded secrets found in pipeline configs (scanned with git-secrets). | **Pass** | HZ | 29 Jan 2026 | WP-CLD-10 | — |
| CLD-11 | Verify IaC governance and security | 1. IaC tool: Terraform v1.6 with modules stored in GitLab. AWS CloudFormation used for some legacy stacks.<br>2. Terraform code in GitLab with branch protection — changes require merge request with 2 approvals. Version history maintained.<br>3. IaC scanning: Checkov integrated in CI pipeline — scans Terraform for misconfigurations before plan/apply. Reviewed scan results — 12 findings in last quarter, 9 resolved, 3 risk-accepted.<br>4. **Drift detection gap identified:** Terraform state stored in S3 with DynamoDB locking (encrypted, access-controlled). However, AWS Config drift detection is configured but alerts are not actioned — 7 unreconciled manual console changes found in the past 6 months (3 security group changes, 2 IAM policy changes, 2 S3 bucket policy changes). No reconciliation process documented.<br>5. State files in S3 with SSE-KMS encryption and IAM access restricted to Terraform service account. | **Partial** | HZ | 30 Jan 2026 | WP-CLD-11 | **F-005** |

#### B3: Virtualisation and Containerisation

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-12 | Verify container and virtualisation security | 1. Container platform: Amazon EKS v1.28 in ap-southeast-1 for Temenos API gateway and microservices layer.<br>2. Container images sourced from Amazon ECR (private registry). Base images from approved list maintained by Cloud Security Engineer. Trivy scanning integrated — scans run on every build.<br>3. **Scanning enforcement gap:** Trivy scanning runs and produces reports, but is configured as "advisory" — pipeline does not block deployment of images with Critical/High vulnerabilities. 2 images with High-severity CVEs deployed to production in Dec 2025 (subsequently patched manually in Jan 2026).<br>4. Containers run as non-root (enforced via PodSecurityPolicy). Read-only root filesystem enabled for stateless pods. Resource limits configured.<br>5. Kubernetes network policies enforced — verified inter-namespace isolation. EKS hardened per CIS Amazon EKS Benchmark v1.3 — compliance report from kube-bench reviewed, 94% compliant (3 informational items outstanding). | **Partial** | HZ | 3 Feb 2026 | WP-CLD-12 | **F-010** |

#### B4: Change Management

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-13 | Verify cloud change management controls | 1. "Cloud Change Management Procedure SOP-CLD-CHG-001 v3.0" dated Aug 2025 obtained.<br>2. Sampled 10 recent changes (Jul 2025 – Jan 2026): CHG-2025-0712, CHG-2025-0789, CHG-2025-0834, CHG-2025-0891, CHG-2025-0923, CHG-2025-0967, CHG-2025-1004, CHG-2025-1038, CHG-2025-1071, CHG-2026-0015. All 10 had: request (ServiceNow), risk assessment, CAB approval, implementation plan, testing evidence, and post-implementation review.<br>3. Security-critical changes (IAM, network, encryption): 4 of 10 sampled were security-critical — all 4 required and received CISO approval in addition to CAB.<br>4. **However**, 7 unreconciled manual console changes detected by AWS Config (not going through change management) — cross-reference to CLD-11 / F-005. These bypassed the formal process. | **Partial** | DT | 4 Feb 2026 | WP-CLD-13 | **F-005** |

#### B5: Backup and Recovery

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-14 | Verify cloud backup and recovery | 1. Backup policy: "Cloud Backup and Recovery Policy POL-CLD-BKP-001 v2.0" dated May 2025.<br>2. Configuration verified: RDS Aurora automated backups (daily, 35-day retention), continuous backup via Aurora Backtrack. S3 versioning enabled with lifecycle policy (90-day retention for non-current versions). EC2 AMI snapshots weekly. EBS daily snapshots (30-day retention).<br>3. Cross-region backup: RDS Aurora snapshots replicated to ap-southeast-3 (Jakarta) daily — verified in AWS Backup console.<br>4. All backups encrypted: RDS with KMS CMK, S3 with SSE-KMS, EBS snapshots with KMS CMK. Verified encryption configuration.<br>5. Backup restoration tested: Most recent test 18 Nov 2025 — RDS restore to point-in-time completed in 47 minutes (RTO target: 2 hours). S3 object restore tested same date. EC2 AMI restore tested.<br>6. Backup monitoring via AWS Backup audit manager — failed backup alerts route to CloudOps PagerDuty. 2 failed backups in past 6 months — both remediated within 4 hours.<br>7. **Note:** DR failover of full Temenos workload to ap-southeast-3 has not been tested end-to-end — see CLD-23 / F-006. Backup restoration is tested, but full DR switchover is not. | **Partial** | DT | 5 Feb 2026 | WP-CLD-14 | **F-006** |

#### B6: Interoperability and Portability

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-15 | Verify cloud portability and interoperability | 1. "Cloud Portability and Exit Strategy v1.2" dated Apr 2025 addresses vendor lock-in. Approach: Temenos T24 runs on standard Linux/Java stack — portable. Kubernetes (EKS) workloads use standard K8s manifests — portable to any K8s platform. Data stored in PostgreSQL-compatible Aurora — portable to standard PostgreSQL.<br>2. Data export: RDS Aurora supports native PostgreSQL dump. S3 data exportable via standard APIs. Documented export procedures exist.<br>3. Migration feasibility assessment dated Apr 2025 — estimates 6–9 month migration to alternative CSP or on-premises, with 3-month parallel run. Assessment is theoretical — no practical testing performed.<br>4. **Data export/migration testing:** No practical test of full data export or migration to alternative environment has been performed. This is a repeat of prior finding F-PRIOR-04. | **Fail** | DT | 6 Feb 2026 | WP-CLD-15 | **F-003** |

#### B7: Exit Strategy

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-16 | Verify cloud exit strategy is documented and actionable | 1. "Cloud Exit Strategy — AWS Engagement" v1.2 dated Apr 2025 obtained.<br>2. Document covers: trigger events (CSP insolvency, material SLA breach, regulatory direction, strategic decision), data retrieval process (RDS dump + S3 sync + EBS snapshot export), migration approach (phased — DB first, app tier, then front-end), timeline (6–9 months), resource requirements (8 FTE + vendor support), and communication plan (internal + BNM notification).<br>3. Strategy reviewed 15 Apr 2025 and approved by CTO. Due for annual review Apr 2026.<br>4. Contractual terms: AWS EA provides 90-day data retrieval post-termination — consistent with exit strategy.<br>5. **Exit strategy has not been tested.** No tabletop exercise or partial execution test has been conducted. Management cites complexity and cost. This is a repeat of prior finding F-PRIOR-04 (originally raised Mar 2024). | **Fail** | DT | 6 Feb 2026 | WP-CLD-16 | **F-003** |

#### B8: Cryptographic Key Management

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-17 | Verify cryptographic key management in cloud | 1. "Cloud Encryption and Key Management Standard STD-CLD-ENC-001 v2.0" dated Jun 2025. Strategy: customer-managed keys (CMK) via AWS KMS for Restricted data; AWS-managed keys for Confidential data.<br>2. KMS CMK inventory: 11 CMKs in production — 7 for RDS, 2 for S3, 1 for EBS, 1 for Secrets Manager.<br>3. **Key rotation gap:** Automatic annual rotation enabled for 7 of 11 CMKs. 4 CMKs (2 RDS, 1 S3, 1 EBS) do not have automatic rotation enabled. Last manual rotation for these 4 keys was 14 months ago (Nov 2024). Bank Perdana's own standard requires annual rotation.<br>4. Encryption at rest: RDS Aurora — AES-256 via KMS CMK (verified). S3 — SSE-KMS default encryption on all buckets (verified via S3 bucket policy audit — 100% compliant). EBS — encrypted with KMS CMK (verified). ElastiCache — encryption at rest enabled (AWS-managed key).<br>5. Encryption in transit: TLS 1.2 enforced for all service endpoints. RDS SSL/TLS enforced via parameter group (rds.force_ssl=1). S3 bucket policy denies non-HTTPS access. Verified. | **Partial** | ML | 7 Feb 2026 | WP-CLD-17 | **F-008** |

#### B9: Access Controls

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-18 | Verify IAM in cloud environments | 1. IAM architecture: Azure AD (Entra ID) federated to AWS IAM via SAML 2.0 SSO. AWS Organizations with Service Control Policies (SCPs).<br>2. **MFA enforcement gap:** MFA enforced for AWS Console access via Azure AD conditional access policy. However, 3 service accounts with programmatic (API key) access do not have MFA — these are break-glass accounts and Terraform service account. Break-glass accounts have MFA configured at AWS IAM level but the Terraform service account does not and uses long-lived access keys (last rotated 8 months ago).<br>3. **Least privilege gap:** Reviewed 25 IAM policies. 4 custom policies use wildcard actions (`s3:*`, `ec2:*`) on specific resources — overly permissive. 2 IAM roles attached to EC2 instances have broader permissions than required (include `iam:PassRole` unnecessarily).<br>4. Privileged access: 6 admin-level IAM users. Admin access managed via AWS SSO with session duration limited to 8 hours. Privileged activity logged in CloudTrail. However, no PAM solution (e.g., CyberArk) — privileged sessions not recorded.<br>5. Service accounts/API keys: 9 service accounts. 3 have access keys older than 180 days (oldest: 243 days). No automated key rotation.<br>6. **Stale accounts:** IAM credential report reviewed — 4 IAM users with no activity in 90+ days (2 belong to former contractors whose offboarding was delayed). | **Fail** | ML | 10 Feb 2026 | WP-CLD-18 | **F-001** |

#### B10: Cybersecurity Operations

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-19 | Verify cloud security monitoring and threat detection | 1. AWS CloudTrail enabled in all 47 accounts (organisation-level trail). GuardDuty enabled in all accounts. AWS Security Hub enabled with CIS AWS Foundations Benchmark.<br>2. Monitoring coverage: CloudTrail captures API activity. VPC Flow Logs enabled for Prod and UAT VPCs. GuardDuty monitors network, identity, and S3 events.<br>3. **SIEM integration gap:** CloudTrail logs from the 3 Temenos accounts are forwarded to Splunk SIEM via S3-to-Splunk integration. However, the remaining 44 accounts are NOT forwarded to SIEM — SOC has visibility only over the 3 Temenos accounts. GuardDuty findings from all accounts route to a central SNS topic but only Critical/High findings trigger SOC alerts — Medium/Low findings are not triaged.<br>4. **CSPM gap:** No dedicated CSPM tool (e.g., Prisma Cloud, Wiz, Lacework) is deployed. AWS Security Hub partially serves this function but has limited misconfiguration detection. Misconfigurations are detected manually during quarterly reviews — 14 misconfigurations found in Q4 2025 review, 9 remediated, 5 open.<br>5. CSPM finding remediation: No systematic tracking — findings tracked in spreadsheet, no SLA for remediation. | **Fail** | ML | 11 Feb 2026 | WP-CLD-19 | **F-002, F-004** |

#### B11: DDoS Protection

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-20 | Verify DDoS protection for cloud-hosted services | 1. AWS Shield Advanced enabled for internet-facing resources: CloudFront distributions, Application Load Balancers, and Elastic IPs. Subscription confirmed (active since Mar 2025).<br>2. L3/L4 protection via Shield Advanced. L7 protection via AWS WAF with rate-limiting rules on ALBs and CloudFront. WAF rule set reviewed — 23 rules including OWASP Top 10, rate limiting (2,000 req/5min per IP), and geo-blocking for non-ASEAN traffic to admin endpoints.<br>3. **DDoS playbook untested:** "DDoS Response Playbook v1.0" dated Jul 2025 exists — covers detection, escalation to AWS Shield Response Team (SRT), communication plan, and post-incident review. However, no DDoS drill or simulation has been conducted. SRT engagement has not been tested.<br>4. Alerting: Shield Advanced alerts configured to PagerDuty via SNS — verified alert routing. CloudWatch alarms for traffic anomalies configured. | **Partial** | AK | 12 Feb 2026 | WP-CLD-20 | **F-011** |

#### B12: Data Loss Prevention

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-21 | Verify DLP controls in cloud | 1. "Cloud Data Loss Prevention Strategy v1.0" dated Aug 2025. Tools: Amazon Macie for S3 sensitive data discovery, AWS CloudTrail for data access monitoring, S3 Block Public Access enforced at organisation level via SCP.<br>2. Macie enabled on all S3 buckets containing Restricted data — scheduled weekly scans. Last scan 5 Feb 2026: 0 publicly accessible objects, 0 unencrypted objects. 3 buckets flagged for PII outside expected locations — investigated and resolved (test data from UAT).<br>3. DLP alerts reviewed: 7 Macie alerts in past 6 months — all investigated within 48 hours and documented in ServiceNow.<br>4. S3 Block Public Access: verified at account level and bucket level for all 3 Temenos accounts. Organisation-level SCP prevents disabling Block Public Access. Additionally, S3 bucket policies explicitly deny non-HTTPS and cross-account access (except for designated backup account). | **Pass** | AK | 13 Feb 2026 | WP-CLD-21 | — |

#### B13: Security Operations Centre (SOC)

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-22 | Verify SOC coverage extends to cloud | 1. SOC operated by Bank Perdana's internal Cyber Defence Centre (CDC), supplemented by MSSP (CyberGuard Malaysia) for 24/7 coverage.<br>2. **SIEM gap (cross-reference CLD-19):** Splunk SIEM ingests CloudTrail and VPC Flow Logs from the 3 Temenos accounts only. 44 non-Temenos AWS accounts not integrated. Cloud-specific detection rules: 18 use cases defined (e.g., root account login, IAM policy change, security group modification, S3 public access attempt, GuardDuty high-severity finding). Rules are well-designed but limited to the 3 ingested accounts.<br>3. SOC analysts: 2 of 8 SOC analysts hold AWS Security Specialty certification. Others received 2-day cloud security training in Oct 2025. Analysts can investigate cloud events using CloudTrail and Athena queries.<br>4. Sampled 5 recent cloud security incidents: (i) GuardDuty UnauthorizedAccess finding 12 Nov 2025 — investigated in 35 min, false positive; (ii) Root account login attempt 3 Dec 2025 — investigated in 12 min, legitimate break-glass by Cloud Ops (documented); (iii) S3 bucket policy change 18 Dec 2025 — investigated in 22 min, authorised change (verified against CHG record); (iv) Unusual API call pattern 5 Jan 2026 — investigated in 45 min, attributed to new Terraform module deployment; (v) IAM access key leak in public GitHub repo alert (GuardDuty) 19 Jan 2026 — investigated in 8 min, key revoked in 15 min, confirmed no data exfiltration. Response quality adequate for ingested accounts. | **Fail** | ML | 14 Feb 2026 | WP-CLD-22 | **F-002** |

#### B14: Cyber Response and Recovery

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-23 | Verify cyber incident response and recovery for cloud | 1. "Cloud Incident Response Plan v2.0" dated Sep 2025 obtained. Covers: AWS account compromise (disable access keys, isolate VPC, forensic snapshot), data breach in cloud (Macie + CloudTrail investigation, notification to BNM within 6 hours for major incident), ransomware in cloud (isolate affected instances, restore from snapshot).<br>2. **CSP outage scenario missing:** The IR plan does not include a specific playbook for prolonged CSP outage (e.g., AWS regional outage > 4 hours). The plan references "activate DR" but does not detail the steps for cloud-specific failover, communication with AWS SRT, or interim manual processing procedures.<br>3. CSP escalation contacts documented: AWS Enterprise Support (24/7), AWS TAM (business hours), AWS SRT (for Shield Advanced events). Contact details verified current.<br>4. **DR failover untested for Temenos:** Cross-region DR to ap-southeast-3 is architecturally designed (Aurora cross-region replica, AMI copies, Terraform for DR infra). However, a full end-to-end DR failover test for the Temenos workload has NOT been conducted. Last DR test (Oct 2025) covered only RDS Aurora failover (database layer) — application tier, network reconfiguration, and DNS cutover were not tested.<br>5. Most recent cloud DR test: 18 Oct 2025 — RDS Aurora cross-region failover completed in 11 minutes. Application layer and full stack recovery not included. | **Partial** | SNI | 17 Feb 2026 | WP-CLD-23 | **F-006, F-007** |

---

### Supplementary Tests: Cloud Compliance and Data Residency

| Ref | Test Objective | Evidence Obtained | Test Result | Assessor | Date | WP Ref | Finding Ref |
|-----|---------------|-------------------|-------------|----------|------|--------|-------------|
| CLD-24 | Verify data residency compliance | 1. Regulatory requirement: BNM RMiT requires customer data to remain in Malaysia unless approved. Bank Perdana policy: all Restricted and Confidential data must reside in ap-southeast-1 (Kuala Lumpur/Singapore region — data centres located in Malaysia for ap-southeast-1a/1b).<br>2. Resource region mapping: All EC2, RDS, S3, EKS resources in Temenos accounts verified in ap-southeast-1 only. SCP "DenyNonApprovedRegions" enforced at Organisation level — tested by attempting to launch EC2 in us-east-1, correctly denied.<br>3. DR data in ap-southeast-3 (Jakarta) — Bank Perdana obtained BNM approval for DR data replication to Jakarta region (BNM approval letter ref BNM/FSKM/2025-0342 dated 12 Jun 2025).<br>4. CloudFront edge caching: confirmed that CloudFront is configured to cache only static assets (no PII/transaction data cached at edge). Cache policy reviewed. | **Pass** | AK | 18 Feb 2026 | WP-CLD-24 | — |
| CLD-25 | Verify cloud security baseline and hardening | 1. "AWS Security Baseline Standard STD-CLD-SEC-001 v2.0" dated Jul 2025 obtained. Aligned to CIS AWS Foundations Benchmark v3.0.<br>2. AWS Security Hub CIS compliance: Latest scan 10 Feb 2026 — 87% compliant (target: 95%). 14 non-compliant checks: 4 related to IAM (cross-ref F-001), 3 related to logging (cross-ref F-002), 3 related to KMS rotation (cross-ref F-008), 4 informational (S3 lifecycle policies).<br>3. **No dedicated CSPM tool** — reliance on Security Hub and manual quarterly reviews. Security Hub provides basic compliance checking but lacks the depth of a CSPM for runtime misconfiguration detection and remediation workflow.<br>4. Remediation tracker: spreadsheet-based, no SLA enforcement. 5 of 14 non-compliant findings open > 60 days. | **Partial** | ML | 19 Feb 2026 | WP-CLD-25 | **F-004** |

---

### Phase 3: Reporting — Completed

| Step | Activity | Completed By | Date | Working Paper | Notes |
|------|----------|-------------|------|---------------|-------|
| R-01 | Consolidated all test results. 11 findings identified: 0 Critical, 3 High, 5 Medium, 3 Low. Findings register finalised. | SNI | 20 Feb 2026 | WP-CLD-R01 | Risk ratings assigned per CyberAssure Risk Rating Methodology v3.0. Reviewed by Engagement Partner. |
| R-02 | Mapped findings to Appendix 10 control areas: F-001 → Appendix 10 Part B (Access Control); F-002 → Appendix 10 Part B (Monitoring); F-003 → Appendix 10 Part B (Exit Strategy); F-004 → Appendix 10 Part B (Security Monitoring); F-005 → Appendix 10 Part B (Change Management); F-006 → Appendix 10 Part B (BCP/DR); F-007 → Appendix 10 Part B (Incident Response); F-008 → Appendix 10 Part B (Encryption); F-009 → Appendix 10 Part A (Governance); F-010 → Appendix 10 Part B (Container Security); F-011 → Appendix 10 Part B (DDoS). | AK | 21 Feb 2026 | WP-CLD-R02 | All 11 findings mapped. |
| R-03 | Drafted recommendations with specific remediation steps, responsible parties, and target dates. Each finding has 2–4 remediation actions. | SNI | 24 Feb 2026 | WP-CLD-R03 | Remediation timelines: High findings — 60 days; Medium — 90 days; Low — 120 days. |
| R-04 | Findings walkthrough conducted with Bank Perdana CISO (Puan Zarina), Head of Cloud (Encik Ravi), Head of IT Risk (Encik Faizal), and VP Technology (Encik Kumar). All findings accepted. Minor factual corrections to F-005 description incorporated. | SNI | 26 Feb 2026 | WP-CLD-R04 | Meeting held at Bank Perdana HQ, Level 28 Menara Perdana, KL. Duration: 3 hours. |
| R-05 | Formal Cloud IESP report prepared in Appendix 7 Part A format. Report ref: CA-IESP-BP-CLD-2026-001. | SNI | 28 Feb 2026 | WP-CLD-R05 | 48-page report including executive summary, detailed findings, recommendations, and Part D attestation. |
| R-06 | Management sign-off obtained. Signed by CISO Puan Zarina and CTO Encik Kumar on 4 Mar 2026. Management action plans confirmed for all 11 findings. | SNI | 4 Mar 2026 | WP-CLD-R06 | Signed copies filed. BNM submission scheduled for 10 Mar 2026. |

---

### Phase 4: Board Deliberation Support — Completed

| Step | Activity | Completed By | Date | Working Paper | Notes |
|------|----------|-------------|------|---------------|-------|
| B-01 | Executive summary and presentation deck prepared for Board Risk Committee (BRC). 12-slide deck highlighting: overall assessment (Satisfactory with Findings), 3 High findings requiring Board attention, cloud-specific risk posture, and remediation roadmap. | SNI | 3 Mar 2026 | WP-CLD-B01 | Deck reviewed by Engagement Partner prior to presentation. |
| B-02 | Attended BRC meeting on 5 Mar 2026. Presented findings to 5 Independent Directors, CEO, CISO, CTO, and Chief Risk Officer. Board directed management to prioritise F-001 (IAM) and F-002 (SIEM) remediation within 45 days (accelerated from 60 days). | SNI | 5 Mar 2026 | WP-CLD-B02 | BRC meeting minutes ref BRC-2026-03-001 filed. |
| B-03 | Board directive on accelerated remediation for F-001 and F-002 incorporated into final report addendum dated 6 Mar 2026. | SNI | 6 Mar 2026 | WP-CLD-B03 | Final report updated and re-signed by CISO. |

---

### Test Results Summary

| Ref | Test Area | Result | Finding |
|-----|-----------|--------|---------|
| CLD-01 | Cloud risk assessment | Pass | — |
| CLD-02 | Cloud risk appetite | Pass | — |
| CLD-03 | Cloud usage policy | Pass | — |
| CLD-04 | CSP due diligence | Pass | — |
| CLD-05 | CSP certifications | Pass | — |
| CLD-06 | Contract management | Pass | — |
| CLD-07 | CSP oversight | Pass | — |
| CLD-08 | Skilled personnel | Partial | F-009 |
| CLD-09 | Cloud architecture | Pass | — |
| CLD-10 | CI/CD security | Pass | — |
| CLD-11 | IaC governance | Partial | F-005 |
| CLD-12 | Container security | Partial | F-010 |
| CLD-13 | Change management | Partial | F-005 |
| CLD-14 | Backup and recovery | Partial | F-006 |
| CLD-15 | Portability / interoperability | Fail | F-003 |
| CLD-16 | Exit strategy | Fail | F-003 |
| CLD-17 | Key management | Partial | F-008 |
| CLD-18 | IAM / access controls | Fail | F-001 |
| CLD-19 | Security monitoring | Fail | F-002, F-004 |
| CLD-20 | DDoS protection | Partial | F-011 |
| CLD-21 | DLP | Pass | — |
| CLD-22 | SOC coverage | Fail | F-002 |
| CLD-23 | Cyber response and recovery | Partial | F-006, F-007 |
| CLD-24 | Data residency | Pass | — |
| CLD-25 | Security baseline / hardening | Partial | F-004 |

**Overall Assessment: Satisfactory with Findings**
- 25 test areas assessed
- 10 Pass, 9 Partial, 6 Fail
- 11 unique findings: 0 Critical, 3 High, 5 Medium, 3 Low

---

### Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Engagement Partner | Rizal Ahmad | [Signed] | 6 Mar 2026 |
| Engagement Lead | Siti Nabilah Ibrahim | [Signed] | 6 Mar 2026 |
| Quality Reviewer | Dr. Tan Wei Ming | [Signed] | 6 Mar 2026 |

---

*Document ref: CA-IESP-BP-CLD-AWP-2026-001 | Classification: Confidential*
