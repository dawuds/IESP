> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative. This does not constitute legal, regulatory, or professional advice. Always refer to the official BNM Policy Document and engage qualified professionals.

---

# IESP Engagement Letter

**CyberAssure Advisory Sdn Bhd**
Level 18, Menara Cyber Point
Jalan Impact, Cyber 6
63000 Cyberjaya, Selangor
Tel: +603-8318 7500 | Email: engagements@cyberassure.com.my

**Date:** 3 January 2026

**Ref:** CA/IESP/2026/BPB-001

---

**To:**

Encik Ahmad Razali bin Mohd Yusof
Chief Technology Officer
Bank Perdana Berhad
Level 30, Menara Perdana
Jalan Sultan Ismail
50250 Kuala Lumpur

---

## 1. Parties

This engagement letter is entered into between:

**Financial Institution ("FI"):**
- Entity Name: Bank Perdana Berhad
- Registration Number: 199201015678 (Company No. 254321-K)
- BNM Licence: Commercial bank licensed under the Financial Services Act 2013
- Registered Address: Level 30, Menara Perdana, Jalan Sultan Ismail, 50250 Kuala Lumpur
- Contact Person: Encik Ahmad Razali bin Mohd Yusof, Chief Technology Officer, ahmad.razali@bankperdana.com.my, +6012-345 6789

**External Service Provider ("ESP"):**
- Entity Name: CyberAssure Advisory Sdn Bhd
- Registration Number: 201501024680 (Company No. 1140567-A)
- Registered Address: Level 18, Menara Cyber Point, Jalan Impact, Cyber 6, 63000 Cyberjaya, Selangor
- Engagement Lead: Puan Siti Nabilah binti Ismail, Managing Director, siti.nabilah@cyberassure.com.my, +6019-876 5432

---

## 2. Engagement Objective and Regulatory Basis

The objective of this engagement is to provide an independent assessment as required under the Bank Negara Malaysia (BNM) Risk Management in Technology (RMIT) Policy Document (November 2025).

This engagement is performed in the capacity of an Independent External Service Provider (IESP) pursuant to:

- [ ] Paragraph 10.24 — Data Centre Resilience Assessment (DCRA)
- [ ] Paragraph 10.36 — Network Resilience Assessment (NRA)
- [x] Paragraph 17.1 — Technology risk assessment for system acquisition/development
- [x] Appendix 10 — Cloud services assessment
- [ ] Appendix 9 — AI/emerging technology assessment
- [ ] Other: N/A

**Regulatory context:** Bank Perdana Berhad is migrating its core banking system (Temenos T24/Transact R23) from an on-premises Silverlake deployment to Amazon Web Services (AWS). This constitutes the first-time adoption of public cloud infrastructure for critical systems, triggering the mandatory IESP assessment under paragraph 17.1. As the deployment involves cloud services for critical systems processing customer data, Appendix 10 (Cloud Services) also applies. Cross-border data flow considerations arise as the primary AWS region (ap-southeast-1) is located in Singapore.

The IESP shall assess the effectiveness of the FI's technology risk controls and provide a risk assessment report in the format prescribed under Appendix 7 Part A of the RMIT.

---

## 3. Scope of Review

### 3.1 Engagement Type

Combined engagement: Cloud Pre-Implementation Technology Risk Assessment under paragraph 17.1, with cloud-specific assessment under Appendix 10.

The assessment focuses on the pre-implementation readiness of the cloud environment, architecture, security controls, operational processes, and governance arrangements prior to go-live of the Temenos T24/Transact R23 core banking system on AWS.

### 3.2 In-Scope Items

The following systems, infrastructure, processes, and controls are within the scope of this engagement:

| Category | Description | Details |
|----------|-------------|---------|
| **Core Banking System** | Temenos T24/Transact R23 | Application tier on EKS, database on Aurora PostgreSQL, blob storage on S3. PROD and DR environments. |
| **Digital Channels** | Internet Banking gateway | Customer-facing web application served via CloudFront and ALB |
| **Digital Channels** | Mobile Banking API layer | RESTful API services on EKS exposed via API Gateway |
| **Compute** | AWS EC2 instances | 8x m6i.4xlarge instances across 3 AZs in ap-southeast-1 |
| **Database** | AWS RDS Aurora PostgreSQL | Multi-AZ deployment, encrypted at rest (AES-256), automated backups |
| **Storage** | AWS S3 | 4 buckets: bpb-t24-prod-data, bpb-t24-prod-logs, bpb-t24-dr-backup, bpb-t24-prod-reports |
| **Container Orchestration** | AWS EKS v1.28 | Managed Kubernetes for T24 microservices and API layer |
| **Content Delivery** | AWS CloudFront | CDN and WAF integration for Internet Banking |
| **Connectivity** | AWS Direct Connect | 10 Gbps dedicated link from CyberJaya Data Centre to AWS ap-southeast-1 |
| **Identity & Access** | AWS IAM, Secrets Manager | Role-based access, service accounts, secrets rotation |
| **Encryption** | AWS KMS | Customer-managed keys (CMK) for data at rest and in transit |
| **Logging & Monitoring** | AWS CloudTrail, CloudWatch | API audit logging, performance monitoring, alerting |
| **Threat Detection** | AWS GuardDuty, Security Hub | Continuous threat detection and security posture management |
| **Network Security** | AWS WAF, Shield Advanced | Web application firewall and DDoS protection |
| **Configuration** | AWS Config, Systems Manager | Configuration compliance monitoring and patch management |
| **Processes** | Cloud change management | Change advisory board, deployment pipelines, rollback procedures |
| **Processes** | IAM lifecycle management | Joiner/mover/leaver, access recertification, privileged access |
| **Processes** | Cloud incident response | Detection, escalation, containment, recovery, reporting |
| **Processes** | Backup and DR | RPO/RTO targets, cross-region replication, DR testing |
| **Processes** | Monitoring and alerting | Security and operational monitoring, SOC integration |

### 3.3 Out-of-Scope Items

The following are explicitly excluded from this engagement:

| Item | Justification for Exclusion |
|------|----------------------------|
| Silverlake CBS (on-premises) | Legacy system being decommissioned post-migration; covered under separate decommissioning risk review |
| Non-critical SaaS applications (e.g., HR, email) | Do not meet the threshold for IESP assessment under paragraph 17.1; not part of the cloud migration programme |
| AWS sandbox and development accounts | Non-production environments with no customer data; governed by separate development security policy |
| Physical data centre security at CyberJaya DC | Subject to a separate DCRA engagement (BPB-DCRA-2025-002, completed September 2025) |
| End-user computing devices | Covered under the FI's existing endpoint security programme; not directly related to the cloud migration |

### 3.4 Applicable RMIT Clauses

- **Paragraph 17.1** — Technology risk assessment for system acquisition/development
- **Paragraphs 10.50–10.52** — Cloud-related controls and governance
- **Appendix 10 Part A** — 7 key areas for cloud risk assessment
- **Appendix 10 Part B** — 14 areas for detailed cloud controls assessment
- **Appendix 7 Part A** — Risk assessment report format
- **Appendix 7 Part B** — Findings report format
- **Appendix 7 Part C** — Summary of findings
- **Appendix 7 Part D** — Minimum controls for assessment

### 3.5 Reference Period

The assessment covers the pre-implementation period. All controls, configurations, and processes assessed are as at the time of fieldwork (20 January – 21 February 2026). The assessment evaluates readiness for go-live, not post-implementation operational effectiveness.

---

## 4. Methodology

The engagement will be conducted using the following methodology:

1. **Planning and Scoping** — Confirm scope, identify key stakeholders, establish communication protocols, and request initial documentation. Map RMIT clauses to specific test procedures.

2. **Document Review** — Review relevant policies, procedures, architectures, configurations, prior assessment reports, AWS Well-Architected Review outputs, and supporting evidence.

3. **Interviews and Walkthroughs** — Conduct interviews with key personnel across Technology, Information Security, Risk Management, Compliance, and Operations. Perform walkthroughs of cloud provisioning, change management, and incident response processes.

4. **Technical Assessment** — Evaluate AWS account structure, IAM policies, network architecture, encryption configurations, logging completeness, and security service configurations. Review infrastructure-as-code (Terraform) templates against security baselines.

5. **Testing** — Execute test procedures in accordance with the Audit Work Programme (AWP), including configuration sampling, access control testing, DR plan review, and compliance checks against CIS AWS Foundations Benchmark v3.0.

6. **Analysis and Reporting** — Analyse findings, assess risk ratings using the agreed methodology, and prepare the risk assessment report in Appendix 7 Part A format.

7. **Management Discussion** — Present draft findings to FI management for factual accuracy review and management response. Allow 5 business days for response.

8. **Final Reporting** — Incorporate management responses and issue the final risk assessment report and supporting deliverables.

The assessment will be conducted in accordance with:
- RMIT Appendix 7 Part D — Minimum controls for the applicable engagement type
- ISO 27001:2022 — Information security management (supplementary)
- AWS Well-Architected Framework — Cloud architecture best practices
- CIS Amazon Web Services Foundations Benchmark v3.0 — Technical configuration baselines
- NIST Cybersecurity Framework 2.0 — Risk management structure
- ISACA IT Audit and Assurance Standards

---

## 5. Timeline

| Phase | Activity | Start Date | End Date |
|-------|----------|------------|----------|
| 1 | Planning and Scoping | 6 Jan 2026 | 17 Jan 2026 |
| 2 | Document Review | 13 Jan 2026 | 24 Jan 2026 |
| 3 | Interviews and Walkthroughs | 20 Jan 2026 | 7 Feb 2026 |
| 4 | Technical Assessment | 27 Jan 2026 | 14 Feb 2026 |
| 5 | Testing | 3 Feb 2026 | 21 Feb 2026 |
| 6 | Draft Report | 22 Feb 2026 | 28 Feb 2026 |
| 7 | Management Discussion | 1 Mar 2026 | 7 Mar 2026 |
| 8 | Final Report Issuance | 8 Mar 2026 | 14 Mar 2026 |

**Total estimated duration:** 10 weeks

**Note:** Phases 2–5 overlap as fieldwork activities run in parallel. The core fieldwork window is 20 January – 21 February 2026 (5 weeks).

---

## 6. Deliverables

The following deliverables will be provided upon completion of the engagement:

| # | Deliverable | Format | Recipient |
|---|-------------|--------|-----------|
| 1 | Risk Assessment Report (Appendix 7 Part A format) | PDF (signed) | Board Risk Committee, CTO, CISO |
| 2 | Detailed Findings Report (Appendix 7 Parts B & C) | PDF | CTO, CISO, Head of Cloud Engineering |
| 3 | Evidence Summary and Working Papers Index | Secured encrypted archive (AES-256) | CTO, Internal Audit |
| 4 | Executive Presentation for Board Risk Committee | PPTX / PDF | Board Risk Committee Chairman |

All deliverables will be classified as **CONFIDENTIAL** and transmitted via encrypted channels agreed with the FI.

---

## 7. Responsibilities

### 7.1 Financial Institution Management

The FI management is responsible for:

- Establishing and maintaining effective technology risk management controls
- Providing timely and complete access to all relevant documentation, systems, personnel, and premises
- Providing a management representation letter confirming the completeness and accuracy of information provided
- Facilitating interviews and walkthroughs within agreed timelines
- Providing management responses to findings within **5 business days** of receiving the draft report
- Ensuring Board Risk Committee deliberation on the IESP findings (per paragraph 8.3)
- Designating Puan Faridah binti Osman (CISO) as the primary liaison for the engagement

### 7.2 External Service Provider

The ESP is responsible for:

- Conducting the assessment with professional competence, objectivity, and due care
- Maintaining independence throughout the engagement
- Applying the agreed methodology and assessment criteria
- Reporting findings accurately and in compliance with Appendix 7 requirements
- Maintaining confidentiality of all information obtained during the engagement
- Issuing the final report within the agreed timeline
- Assigning appropriately qualified personnel with relevant cloud and banking sector experience

---

## 8. Access Requirements

The FI shall provide the ESP with:

- **Logical access:** Read-only access to the AWS PROD and DR accounts via a dedicated IAM role (cyberassure-iesp-readonly) with CloudTrail logging enabled. Access to AWS Console and CLI. No write or modify permissions required.
- **Physical access:** Access to the Bank Perdana Berhad Technology Division office at Menara Perdana, Level 28, for on-site fieldwork days.
- **Personnel access:** Access to relevant personnel for interviews and clarifications, including:
  - Cloud Engineering team
  - Information Security team
  - IT Operations / SRE team
  - Risk Management and Compliance
  - Internal Audit
  - Vendor management (for AWS and Temenos contacts)
- **Documentation access:** All relevant documentation, including but not limited to:
  - Technology risk management policies and procedures
  - Cloud adoption strategy and architecture design documents
  - AWS account configuration exports and Terraform state files
  - Network architecture diagrams (physical and logical)
  - IAM policies, role definitions, and access matrix
  - Security monitoring configuration and sample alert outputs
  - DR plan and most recent DR test results
  - Change management records for the cloud migration programme
  - Temenos T24 deployment architecture and integration specifications
  - AWS shared responsibility model acknowledgement and CSP contract
  - AWS SOC 2 Type II report (current) and ISO 27001 certificate
  - Prior internal audit and risk assessment reports related to the migration

Access arrangements shall be documented in a separate access request form and are subject to the FI's security policies.

---

## 9. Confidentiality

All information obtained during this engagement shall be treated as strictly confidential. The ESP shall:

- Not disclose any information to third parties without prior written consent of the FI
- Ensure all ESP personnel involved in the engagement sign individual confidentiality undertakings (Non-Disclosure Agreements) prior to commencement of fieldwork
- Store all engagement materials securely using AES-256 encryption, within CyberAssure's ISO 27001-certified document management system
- Not store any FI data on personal devices or unsecured cloud storage
- Return or securely destroy all FI materials within 30 days of final report issuance, as directed by the FI
- Retain working papers for a minimum of 7 years in accordance with professional standards and applicable legal requirements

---

## 10. Independence Declaration

The ESP hereby declares that:

1. The ESP, its partners, directors, and personnel assigned to this engagement have no financial interest in, or financial relationship with, Bank Perdana Berhad that could compromise independence.
2. The ESP has not provided any services to Bank Perdana Berhad in the past **24 months** that would create a self-review threat to independence.
3. The ESP personnel assigned to this engagement have not been employed by Bank Perdana Berhad in the past **3 years**.
4. The ESP has no existing engagements with AWS, Temenos, or any other vendor involved in the Bank Perdana cloud migration programme that could create a conflict of interest.
5. The ESP will disclose any potential or actual conflicts of interest that arise during the engagement.
6. The ESP meets the qualifications and competency requirements expected of an independent external service provider under the RMIT.

Any exceptions to the above are disclosed in Annexure A to this letter.

---

## 11. Limitations

This engagement is subject to the following limitations:

1. The assessment is based on information provided by the FI and available at the time of the assessment. The ESP does not guarantee the completeness or accuracy of information provided by the FI.
2. The assessment provides reasonable assurance, not absolute assurance, regarding the effectiveness of controls.
3. The assessment is limited to the scope defined in Section 3 and does not extend to areas not explicitly covered.
4. The ESP's opinion is based on the controls in place during the assessment period and does not guarantee future effectiveness.
5. The assessment does not constitute a legal opinion, financial audit, or regulatory examination.
6. Sampling methodologies are applied where complete population testing is not practicable.
7. As a pre-implementation review, certain controls (e.g., operational monitoring effectiveness, production incident response) can only be assessed on a design basis, not operating effectiveness.
8. The assessment of AWS native services relies in part on AWS's SOC 2 Type II report and ISO 27001 certification; the ESP does not independently audit AWS's internal controls.

---

## 12. Fees

### 12.1 Professional Fees

| Component | Amount (RM) |
|-----------|-------------|
| Professional fees | 285,000 |
| Disbursements (travel, accommodation, secure communications) | 15,000 |
| **Total (excluding SST)** | **300,000** |

### 12.2 Payment Terms

- **30%** (RM90,000) upon signing of this engagement letter
- **40%** (RM120,000) upon issuance of the draft report
- **30%** (RM90,000) upon issuance of the final report

Payment is due within **30 days** of invoice date. All amounts are in Ringgit Malaysia (RM) and exclude Sales and Service Tax (SST) at the prevailing rate.

### 12.3 Additional Work

Any work beyond the agreed scope will be subject to a separate engagement letter or addendum, agreed in advance by both parties. Additional work will be billed at the following day rates:

| Role | Day Rate (RM) |
|------|---------------|
| Managing Director / Engagement Lead | 6,500 |
| Senior Consultant | 4,500 |
| Consultant | 3,500 |

---

## 13. Agreement

By signing below, both parties acknowledge and agree to the terms set out in this engagement letter.

**For the Financial Institution:**

| | |
|---|---|
| Name | Encik Ahmad Razali bin Mohd Yusof |
| Title | Chief Technology Officer, Bank Perdana Berhad |
| Signature | _________________________________ |
| Date | _________________________________ |

**For the External Service Provider:**

| | |
|---|---|
| Name | Puan Siti Nabilah binti Ismail |
| Title | Managing Director, CyberAssure Advisory Sdn Bhd |
| Signature | _________________________________ |
| Date | _________________________________ |

---

## Annexure A: Disclosure of Independence Exceptions

None. CyberAssure Advisory Sdn Bhd confirms that no independence exceptions exist with respect to this engagement.

---

## Annexure B: ESP Team Composition

| Name | Role | Qualifications | Experience |
|------|------|---------------|------------|
| Puan Siti Nabilah binti Ismail | Engagement Lead / Quality Review Partner | CISA, CCSP, CISSP | 18 years in IT audit and cybersecurity advisory; 6 IESP cloud engagements for Malaysian banks; former Big 4 IT Risk Director |
| Encik Khairul Anwar bin Zainal | Senior Cloud Assessor | CCSP, AWS Solutions Architect Professional, CISA | 12 years in cloud security and IT audit; led AWS migration assessments for 3 financial institutions; specialises in RMIT Appendix 10 |
| Puan Nurul Izzah binti Abdullah | IT Audit Consultant | CISA, ISO 27001 Lead Auditor, CRISC | 8 years in IT governance, risk, and compliance; experienced in RMIT-aligned assessments across banking and takaful sectors |
| Encik Danial Hakim bin Roslan | Cloud Infrastructure Specialist | AWS Solutions Architect Professional, CKA (Certified Kubernetes Administrator), AWS Security Specialty | 7 years in cloud infrastructure and DevSecOps; hands-on experience with EKS, Terraform, and AWS security services |
| Puan Amirah binti Hassan | Junior Consultant / Evidence Coordinator | CISA (candidate), AWS Cloud Practitioner | 3 years in IT audit; responsible for evidence collection, working paper documentation, and logistics coordination |

---

## Annexure C: Higher-Risk Engagement Classification

This engagement is classified as **higher-risk** under the RMIT framework due to the following factors:

| Factor | Detail |
|--------|--------|
| **Critical system** | The T24/Transact core banking system is classified as Critical by the FI, processing all deposit, lending, and payment transactions |
| **Customer data in cloud** | Customer personally identifiable information (PII) and financial data will be processed and stored in the AWS cloud environment |
| **Cross-border data flow** | The primary AWS region (ap-southeast-1) is located in Singapore, constituting cross-border transfer of Malaysian customer data |
| **First-time cloud adoption** | This is the FI's first migration of a critical system to public cloud infrastructure, introducing new risk domains |

These factors necessitate enhanced assessment procedures, including detailed review of data residency controls, cross-border data governance, and cloud-specific security architecture.
