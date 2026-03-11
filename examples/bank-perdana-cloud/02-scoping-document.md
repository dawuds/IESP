> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative. This does not constitute legal, regulatory, or professional advice. Always refer to the official BNM Policy Document and engage qualified professionals.

---

# IESP Scoping Document

**Engagement Reference:** CA/IESP/2026/BPB-001

**Financial Institution:** Bank Perdana Berhad

**ESP:** CyberAssure Advisory Sdn Bhd

**Version:** 1.0

**Date:** 10 January 2026

**Status:** Final

---

## 1. Engagement Type Selection

| # | Engagement Type | RMIT Reference | Selected |
|---|----------------|----------------|----------|
| 1 | Data Centre Resilience Assessment (DCRA) | Para 10.24–10.28 | [ ] |
| 2 | Network Resilience Assessment (NRA) | Para 10.36–10.43 | [ ] |
| 3 | Technology Risk Assessment (System Acquisition/Development) | Para 17.1, App 7 | [x] |
| 4 | Cloud Services Assessment | App 10 | [x] |
| 5 | AI / Emerging Technology Assessment | App 9 | [ ] |
| 6 | Combined Assessment | 17.1 + App 10 | [x] |
| 7 | Other | N/A | [ ] |

**Engagement trigger:**

- [ ] Scheduled periodic assessment (per RMIT frequency requirements)
- [x] New system/service implementation
- [ ] Material change to existing system/service
- [ ] Regulatory direction
- [ ] Incident-driven
- [ ] Other

**Trigger detail:** Bank Perdana Berhad is migrating its core banking system from an on-premises Silverlake deployment to Temenos T24/Transact R23 hosted on AWS. This is the FI's first adoption of public cloud for critical systems. Under paragraph 17.1, an IESP assessment is mandatory before go-live. The use of cloud services for critical systems also triggers the Appendix 10 cloud assessment requirements.

---

## 2. In-Scope Systems, Infrastructure, and Processes

### 2.1 Systems and Applications

| # | System/Application | Classification | Environment | Owner | Business Function |
|---|-------------------|---------------|-------------|-------|-------------------|
| 1 | Temenos T24/Transact R23 — Core Banking | Critical | Production (ap-southeast-1), DR (ap-southeast-3) | Encik Ahmad Razali bin Mohd Yusof, CTO | Deposits, lending, payments, GL, customer management |
| 2 | Internet Banking Gateway | Critical | Production (ap-southeast-1) | Puan Roslina binti Karim, Head of Digital Banking | Retail and corporate internet banking front-end |
| 3 | Mobile Banking API Layer | Critical | Production (ap-southeast-1) | Puan Roslina binti Karim, Head of Digital Banking | RESTful APIs serving mobile banking application |

### 2.2 Infrastructure Components

| # | Component | Type | Location | Details |
|---|-----------|------|----------|---------|
| 1 | EC2 m6i.4xlarge (x8) | Compute | AWS ap-southeast-1 (3 AZs) | T24 application servers, 16 vCPU / 64 GiB each, Amazon Linux 2023 |
| 2 | RDS Aurora PostgreSQL 15.4 | Database | AWS ap-southeast-1 (Multi-AZ) | Primary + 2 read replicas, r6g.4xlarge, encrypted (AES-256 via KMS CMK) |
| 3 | S3 Buckets (x4) | Storage | AWS ap-southeast-1 | bpb-t24-prod-data, bpb-t24-prod-logs, bpb-t24-dr-backup, bpb-t24-prod-reports |
| 4 | EKS Cluster v1.28 | Container Orchestration | AWS ap-southeast-1 | Managed Kubernetes; 12 worker nodes (m6i.2xlarge); runs T24 microservices and API layer |
| 5 | CloudFront Distribution | CDN / Edge | AWS Global Edge (APAC) | Internet Banking content delivery; integrated with WAF |
| 6 | Direct Connect (10 Gbps) | Network Connectivity | CyberJaya DC to AWS ap-southeast-1 | Dedicated fibre link via Equinix SG1; VLAN-tagged, MACsec encrypted |
| 7 | Application Load Balancer (x2) | Load Balancer | AWS ap-southeast-1 | Internal ALB for T24, external ALB for Internet Banking |
| 8 | NAT Gateway (x3) | Network | AWS ap-southeast-1 (per AZ) | Outbound internet for EKS pods (patching, API calls) |

### 2.3 Data Centres / Facilities

| # | Facility | Type | Location | Tier | Operator |
|---|----------|------|----------|------|----------|
| 1 | AWS ap-southeast-1 | Primary Cloud Region | Singapore | N/A (AWS manages) | AWS (CSP) |
| 2 | AWS ap-southeast-3 | DR Cloud Region | Jakarta, Indonesia | N/A (AWS manages) | AWS (CSP) |
| 3 | CyberJaya Data Centre | On-premises (Direct Connect termination) | Cyberjaya, Selangor | Tier III | AIMS Data Centre (colocation) |

### 2.4 Network Segments

| # | Segment | Description | Classification |
|---|---------|-------------|---------------|
| 1 | VPC bpb-prod-vpc (10.100.0.0/16) | Production VPC with public, private, and database subnets | Cloud — Production |
| 2 | VPC bpb-dr-vpc (10.200.0.0/16) | DR VPC in ap-southeast-3, mirrored architecture | Cloud — DR |
| 3 | Transit Gateway | Connects prod VPC, DR VPC, and Direct Connect | Cloud — Internal |
| 4 | Direct Connect VLAN 100 | Dedicated link from CyberJaya DC to AWS | Hybrid — WAN |
| 5 | CloudFront Edge | Internet-facing CDN distribution | Cloud — External / DMZ |

### 2.5 Cloud Services

| # | Service | CSP | Model | Region | Classification |
|---|---------|-----|-------|--------|---------------|
| 1 | EC2 | AWS | IaaS | ap-southeast-1 | Critical |
| 2 | RDS Aurora PostgreSQL | AWS | PaaS | ap-southeast-1 | Critical |
| 3 | S3 | AWS | PaaS | ap-southeast-1 | Critical |
| 4 | EKS | AWS | PaaS | ap-southeast-1 | Critical |
| 5 | CloudFront | AWS | PaaS | Global (APAC edges) | Critical |
| 6 | IAM | AWS | Security | Global | Critical |
| 7 | KMS | AWS | Security | ap-southeast-1 | Critical |
| 8 | CloudTrail | AWS | Monitoring | ap-southeast-1 | Critical |
| 9 | GuardDuty | AWS | Security | ap-southeast-1 | Important |
| 10 | Security Hub | AWS | Security | ap-southeast-1 | Important |
| 11 | WAF | AWS | Security | Global (CloudFront) | Critical |
| 12 | Shield Advanced | AWS | Security | Global | Important |
| 13 | Secrets Manager | AWS | Security | ap-southeast-1 | Critical |
| 14 | Systems Manager | AWS | Operations | ap-southeast-1 | Important |
| 15 | AWS Config | AWS | Compliance | ap-southeast-1 | Important |

### 2.6 Processes

| # | Process | Owner | Frequency | Description |
|---|---------|-------|-----------|-------------|
| 1 | Cloud Change Management | Encik Hafiz bin Othman, Head of Cloud Engineering | Per change | CAB review, CI/CD pipeline approval gates, Terraform plan/apply workflow, rollback procedures |
| 2 | IAM Lifecycle Management | Puan Faridah binti Osman, CISO | Continuous | Joiner/mover/leaver provisioning, quarterly access recertification, PAM for privileged accounts |
| 3 | Cloud Incident Response | Puan Faridah binti Osman, CISO | Event-driven | Detection via GuardDuty/Security Hub, escalation matrix, containment playbooks, BNM notification procedures |
| 4 | Backup and Disaster Recovery | Encik Hafiz bin Othman, Head of Cloud Engineering | Daily backup / Bi-annual DR test | Aurora automated snapshots, S3 cross-region replication, DR runbook, RPO 15 min / RTO 2 hours |
| 5 | Security Monitoring and Alerting | Puan Faridah binti Osman, CISO | Continuous (24/7) | CloudTrail log analysis, GuardDuty alerts, Security Hub findings, integration with on-premises SIEM (Splunk) |

---

## 3. Out-of-Scope Items and Justification

| # | Item/Area | Justification for Exclusion | Approved By |
|---|-----------|---------------------------|-------------|
| 1 | Silverlake CBS (on-premises legacy) | Being decommissioned post-migration; separate decommissioning risk review in progress (BPB-DECOM-2026-001) | Encik Ahmad Razali, CTO |
| 2 | Non-critical SaaS (Microsoft 365, SAP SuccessFactors, ServiceNow) | Not part of the core banking migration programme; do not process critical banking data; below the IESP trigger threshold | Encik Ahmad Razali, CTO |
| 3 | AWS sandbox account (bpb-sandbox-001) | Non-production; no customer data; isolated from production via AWS Organizations SCP; governed by development security policy | Puan Faridah binti Osman, CISO |
| 4 | AWS development account (bpb-dev-001) | Non-production; no customer data; separate VPC with no peering to production | Puan Faridah binti Osman, CISO |
| 5 | Physical data centre security (CyberJaya DC) | Covered under separate DCRA engagement completed September 2025 (BPB-DCRA-2025-002); only the Direct Connect logical configuration is in scope | Encik Ahmad Razali, CTO |
| 6 | Third-party penetration testing of cloud environment | Separate engagement contracted to NetAssure Sdn Bhd (scheduled Feb 2026); results will be reviewed as evidence where available | Puan Faridah binti Osman, CISO |

**Note:** All exclusions have been reviewed and approved by the FI's designated responsible officers as indicated above. These exclusions do not affect the IESP's ability to provide the required assurance under Appendix 7.

---

## 4. Applicable RMIT Clauses and Appendices

### 4.1 Core RMIT Paragraphs

| # | Paragraph | Title/Subject | Applicability Notes |
|---|-----------|---------------|-------------------|
| 1 | 17.1 | Technology risk assessment for system acquisition/development | Primary trigger — first-time critical system on public cloud |
| 2 | 10.49 | Cloud risk management framework | FI's cloud governance and risk management arrangements |
| 3 | 10.50 | Cloud service provider due diligence | AWS due diligence, shared responsibility model understanding |
| 4 | 10.51 | Cloud data governance and security | Data classification, encryption, residency, cross-border controls |
| 5 | 10.52 | Cloud exit strategy and portability | Vendor lock-in mitigation, data portability, exit planning |
| 6 | 10.18 | Cryptographic controls | KMS configuration, key management, TLS enforcement |
| 7 | 10.44 | Access control management | IAM policies, RBAC, privileged access, MFA |
| 8 | 10.46 | Security monitoring and logging | CloudTrail, GuardDuty, SIEM integration |
| 9 | 10.47 | Incident management | Cloud-specific incident response procedures |
| 10 | 10.22 | Backup and recovery | Aurora snapshots, S3 replication, DR procedures |
| 11 | 10.23 | Business continuity for technology | Cloud DR architecture, RTO/RPO, failover testing |
| 12 | 8.3 | Board oversight of technology risk | Board Risk Committee deliberation on IESP findings |

### 4.2 Applicable Appendices

| # | Appendix | Title | Sections Applicable |
|---|----------|-------|-------------------|
| 1 | Appendix 7 | Risk Assessment Report | Part A (report format), Part B (findings), Part C (summary), Part D (minimum controls) |
| 2 | Appendix 10 | Cloud Services | Part A (7 key assessment areas), Part B (14 detailed control areas) |

### 4.3 Appendix 10 Coverage Mapping

**Part A — 7 Key Assessment Areas:**

| # | Area | Description | Applicable |
|---|------|-------------|-----------|
| 1 | Governance and oversight | Cloud governance framework, roles, board reporting | Yes |
| 2 | Risk management | Cloud risk assessment, risk appetite, residual risk | Yes |
| 3 | Data management | Data classification, residency, sovereignty, cross-border | Yes |
| 4 | Security | Identity, encryption, network security, threat detection | Yes |
| 5 | Resilience | Availability, DR, backup, failover, RTO/RPO | Yes |
| 6 | Compliance | Regulatory compliance, audit rights, CSP certifications | Yes |
| 7 | Exit strategy | Portability, reversibility, data retrieval, termination | Yes |

**Part B — 14 Detailed Control Areas:**

| # | Control Area | Applicable | Test Approach |
|---|-------------|-----------|---------------|
| 1 | Cloud strategy and governance | Yes | Inspection, Interview |
| 2 | Cloud risk assessment | Yes | Inspection, Interview |
| 3 | CSP due diligence and selection | Yes | Inspection |
| 4 | Contractual arrangements | Yes | Inspection |
| 5 | Data governance and classification | Yes | Inspection, Interview, Testing |
| 6 | Data residency and sovereignty | Yes | Inspection, Testing |
| 7 | Identity and access management | Yes | Inspection, Testing |
| 8 | Encryption and key management | Yes | Inspection, Testing |
| 9 | Network security | Yes | Inspection, Testing |
| 10 | Logging and monitoring | Yes | Inspection, Testing |
| 11 | Incident management | Yes | Inspection, Interview |
| 12 | Business continuity and DR | Yes | Inspection, Interview, Testing |
| 13 | Change management | Yes | Inspection, Interview |
| 14 | Exit planning and portability | Yes | Inspection, Interview |

### 4.4 Part D Minimum Controls Mapping

The assessment shall, at minimum, cover the controls specified in Appendix 7 Part D applicable to the engagement type:

| # | Part D Control Area | Applicable | Test Approach |
|---|-------------------|-----------|---------------|
| 1 | Technology governance and oversight | Yes | Inspection, Interview |
| 2 | Technology risk management | Yes | Inspection, Interview |
| 3 | Technology operations management | Yes | Inspection, Interview, Testing |
| 4 | Cybersecurity management | Yes | Inspection, Interview, Testing |
| 5 | Technology audit | Yes | Inspection |
| 6 | Access control | Yes | Inspection, Testing |
| 7 | Cryptography | Yes | Inspection, Testing |
| 8 | Network security | Yes | Inspection, Testing |
| 9 | System development and acquisition | Yes | Inspection, Interview |
| 10 | Change management | Yes | Inspection, Testing |
| 11 | IT service management | Yes | Inspection, Interview |
| 12 | Business continuity management | Yes | Inspection, Interview |
| 13 | Cloud computing | Yes | Inspection, Interview, Testing |

---

## 5. Assessment Criteria

### 5.1 Primary Assessment Criteria

The assessment will be conducted against:

1. **RMIT Appendix 7 Part D** — Minimum controls for the applicable engagement type
2. **RMIT Appendix 10 Parts A and B** — Cloud-specific assessment areas and controls
3. **Specific RMIT paragraphs** — As listed in Section 4.1
4. **FI's own policies and standards** — Where they exceed RMIT minimum requirements (Bank Perdana Technology Risk Management Policy v4.2, Cloud Security Policy v1.0)

### 5.2 Supplementary Frameworks

| Framework | Version | Application |
|-----------|---------|-------------|
| ISO 27001 | 2022 | Information security controls mapping; supplements RMIT controls where RMIT is less prescriptive (e.g., supplier relationships, HR security) |
| AWS Well-Architected Framework | 2025 | Cloud architecture best practices across security, reliability, performance, cost, and operational excellence pillars |
| CIS AWS Foundations Benchmark | v3.0 | Technical configuration baselines for IAM, logging, monitoring, networking; used for configuration compliance testing |
| NIST Cybersecurity Framework | 2.0 | Overarching risk management structure (Govern, Identify, Protect, Detect, Respond, Recover); used to organise findings |

### 5.3 Risk Rating Methodology

Findings will be rated using the following scale:

| Rating | Definition | Expected Remediation |
|--------|-----------|---------------------|
| **Critical** | Immediate threat to confidentiality, integrity, or availability of critical systems; regulatory non-compliance with material impact | Immediate action required (before go-live) |
| **High** | Significant control weakness with potential for material impact; may affect go-live readiness | Remediation within 30 days |
| **Medium** | Control weakness with moderate risk exposure; does not prevent go-live but requires attention | Remediation within 90 days |
| **Low** | Minor control improvement opportunity; defence-in-depth enhancement | Remediation within 180 days |
| **Observation** | Best practice recommendation; no immediate risk; enhancement opportunity | For management consideration |

**Go-live impact:** Any finding rated Critical must be remediated before the T24 production go-live. High-rated findings must have an approved remediation plan with committed timeline before go-live.

---

## 6. Key Contacts and Stakeholders

### 6.1 FI Contacts

| Role | Name | Title | Email | Phone |
|------|------|-------|-------|-------|
| Engagement Sponsor | Encik Ahmad Razali bin Mohd Yusof | Chief Technology Officer | ahmad.razali@bankperdana.com.my | +6012-345 6789 |
| Primary Liaison | Puan Faridah binti Osman | Chief Information Security Officer | faridah.osman@bankperdana.com.my | +6012-456 7890 |
| Cloud Engineering Lead | Encik Hafiz bin Othman | Head of Cloud Engineering | hafiz.othman@bankperdana.com.my | +6013-567 8901 |
| Risk Management | Puan Noraini binti Ahmad | Head of Operational Risk | noraini.ahmad@bankperdana.com.my | +6019-678 9012 |
| Compliance | Encik Zahir bin Iskandar | Head of Regulatory Compliance | zahir.iskandar@bankperdana.com.my | +6017-789 0123 |
| Internal Audit | Puan Lim Mei Ling | Head of IT Audit | meiling.lim@bankperdana.com.my | +6016-890 1234 |

### 6.2 ESP Team

| Role | Name | Qualifications | Contact |
|------|------|---------------|---------|
| Engagement Lead / QR Partner | Puan Siti Nabilah binti Ismail | CISA, CCSP, CISSP | siti.nabilah@cyberassure.com.my |
| Senior Cloud Assessor | Encik Khairul Anwar bin Zainal | CCSP, AWS SAP, CISA | khairul.anwar@cyberassure.com.my |
| IT Audit Consultant | Puan Nurul Izzah binti Abdullah | CISA, ISO 27001 LA, CRISC | nurul.izzah@cyberassure.com.my |
| Cloud Infrastructure Specialist | Encik Danial Hakim bin Roslan | AWS SAP, CKA, AWS Security Specialty | danial.hakim@cyberassure.com.my |

### 6.3 Third Parties

| Organisation | Role | Contact | Access Required |
|-------------|------|---------|----------------|
| Amazon Web Services (AWS) | Cloud Service Provider | AWS Malaysia Enterprise Support — Encik Lee Wei Jian, Technical Account Manager | No direct access; FI to coordinate any AWS TAM queries as needed during assessment |

---

## 7. Timeline and Milestones

| # | Milestone | Target Date | Owner | Status |
|---|-----------|-------------|-------|--------|
| 1 | Engagement letter signed | 3 Jan 2026 | FI / ESP | Complete |
| 2 | Scoping document finalised | 10 Jan 2026 | ESP | Complete |
| 3 | Document request list issued | 10 Jan 2026 | ESP | Complete |
| 4 | Documents received (deadline) | 17 Jan 2026 | FI | Pending |
| 5 | Fieldwork commencement | 20 Jan 2026 | ESP | Pending |
| 6 | Fieldwork mid-point review | 7 Feb 2026 | ESP / FI | Pending |
| 7 | Fieldwork completion | 21 Feb 2026 | ESP | Pending |
| 8 | Draft report issued | 28 Feb 2026 | ESP | Pending |
| 9 | Management response received | 7 Mar 2026 | FI | Pending |
| 10 | Final report issued and board presentation | 14 Mar 2026 | ESP / FI | Pending |

**Fieldwork schedule:**

| Week | Dates | Activity | Personnel | Location |
|------|-------|----------|-----------|----------|
| Week 3 | 20–24 Jan 2026 | Kick-off; document review; initial interviews (CTO, CISO, Cloud Eng Lead) | Siti Nabilah, Khairul Anwar, Nurul Izzah | On-site (Menara Perdana) |
| Week 4 | 27–31 Jan 2026 | Technical assessment: AWS account structure, IAM, networking, encryption | Khairul Anwar, Danial Hakim | On-site + Remote (AWS Console) |
| Week 5 | 3–7 Feb 2026 | Technical assessment: EKS, RDS, S3, monitoring; process walkthroughs | Khairul Anwar, Danial Hakim, Nurul Izzah | On-site + Remote |
| Week 6 | 10–14 Feb 2026 | Interviews (Risk, Compliance, Internal Audit); DR review; change mgmt testing | Siti Nabilah, Nurul Izzah | On-site |
| Week 7 | 17–21 Feb 2026 | Gap analysis; evidence follow-up; exit meeting with FI management | Full team | On-site |

---

## 8. Assumptions and Constraints

### 8.1 Assumptions

1. The FI will provide complete and accurate documentation within the agreed timelines (by 17 January 2026).
2. Key personnel (as listed in Section 6.1) will be available for interviews during the fieldwork period (20 January – 21 February 2026).
3. Read-only access to the AWS production and DR accounts will be granted via a dedicated IAM role by 17 January 2026.
4. The FI's cloud environment configuration will remain in a stable state during the assessment period (no major architectural changes without prior notification to ESP).
5. The Temenos T24/Transact R23 cloud environment will be in a near-production-ready state (UAT complete or in progress) by the start of fieldwork.
6. AWS SOC 2 Type II report (covering the period ending no earlier than June 2025) and ISO 27001 certificate will be made available.
7. Management representations provided by the FI are made in good faith.
8. The pending penetration test by NetAssure Sdn Bhd (scheduled February 2026) may provide supplementary evidence; however, the IESP assessment does not depend on its completion.

### 8.2 Constraints

1. The assessment is limited to the scope defined in this document.
2. Testing will be conducted in **production and DR** cloud environments on a **read-only, non-intrusive** basis. No configuration changes, vulnerability scanning, or penetration testing will be performed by the ESP.
3. As a pre-implementation review, operational effectiveness testing is limited to controls that are already operational (e.g., IAM, logging). Controls not yet in production (e.g., production incident response) will be assessed on a design-adequacy basis only.
4. Assessment timelines are subject to the FI's timely provision of documentation and access. Delays of more than 5 business days may require timeline renegotiation.
5. The T24 go-live is tentatively scheduled for April 2026. The final IESP report must be issued by 14 March 2026 to allow the Board Risk Committee to deliberate before go-live approval.
6. FI has a change freeze in production environments from 15 February 2026 onwards (pre-go-live stabilisation); this does not impact the assessment but limits the FI's ability to remediate findings before assessment completion.

### 8.3 Dependencies

| # | Dependency | Owner | Impact if Not Met |
|---|-----------|-------|-------------------|
| 1 | AWS read-only IAM role provisioned and tested | FI (Cloud Engineering) | Delays technical assessment; may push fieldwork beyond 21 Feb |
| 2 | T24 cloud environment in near-production-ready state | FI (Cloud Engineering / Temenos) | Limits the assessable control surface; findings may carry caveats |
| 3 | Documentation package delivered by 17 Jan 2026 | FI (CISO / CTO office) | Delays document review phase; compresses fieldwork timeline |
| 4 | Key personnel availability during fieldwork | FI (all departments) | Incomplete interview coverage; may result in qualified opinion |
| 5 | AWS SOC 2 Type II report availability | FI (Vendor Management) | Limits assurance over AWS-managed controls; must be disclosed in report |
| 6 | Board Risk Committee meeting scheduled by 14 Mar 2026 | FI (Company Secretary) | Delays board deliberation requirement under paragraph 8.3 |

---

## 9. Document Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 6 Jan 2026 | Encik Khairul Anwar bin Zainal | Initial draft based on engagement letter and kick-off discussions |
| 0.2 | 8 Jan 2026 | Puan Siti Nabilah binti Ismail | QR review; added Appendix 10 mapping and higher-risk classification |
| 1.0 | 10 Jan 2026 | Puan Siti Nabilah binti Ismail | Finalised following FI review and approval by CTO and CISO |

---

## 10. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| FI Engagement Sponsor | Encik Ahmad Razali bin Mohd Yusof, CTO | _________ | 10 Jan 2026 |
| FI Primary Liaison | Puan Faridah binti Osman, CISO | _________ | 10 Jan 2026 |
| ESP Engagement Lead | Puan Siti Nabilah binti Ismail, Managing Director | _________ | 10 Jan 2026 |
