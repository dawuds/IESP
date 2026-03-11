> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative.

---

# Confirmation Letter

## BNM RMIT Appendix 7 Part B

---

**Bank Perdana Berhad**
Level 30, Menara Perdana
50 Jalan Sultan Ismail
50250 Kuala Lumpur

**Date:** 14 March 2026

**Ref:** BPB/BRTC/2026/CL-001

---

**To:**

Bank Negara Malaysia
Jalan Dato' Onn
50480 Kuala Lumpur

**Attention:** Department of Financial Technology & Innovation and the Department of Banking Supervision

---

**Re: Confirmation Letter pursuant to Appendix 7 Part B of the Risk Management in Technology Policy Document (November 2025)**

**Subject:** Migration of Core Banking System (Temenos T24/Transact R23) to Amazon Web Services (AWS) Public Cloud

---

Dear Sir/Madam,

In connection with the implementation of the migration of Bank Perdana Berhad's core banking system (Temenos T24/Transact R23) from on-premises infrastructure to Amazon Web Services (AWS) public cloud, and pursuant to the requirements of the Risk Management in Technology (RMIT) Policy Document (November 2025), the Board of Directors of Bank Perdana Berhad hereby confirms the following:

---

### 1. Consistency with Strategic and Business Plans

We confirm that the migration of the core banking system to AWS is consistent with the Bank's strategic and business plans.

**Supporting details:**

- The cloud migration is a cornerstone initiative of the BPB Digital Transformation Strategy 2024–2028 (v1.0), which was reviewed and approved by the Board of Directors on 15 October 2024.
- The business case for the migration (reference BPB/IT/2025/BC-T24Cloud, version 2.1) was approved by the Board Risk and Technology Committee (BRTC) on 18 December 2025, with a total approved budget of RM45 million.
- The migration supports the following strategic objectives: (i) modernise aging core banking infrastructure to enable scalable digital banking services; (ii) reduce operational risk from end-of-life hardware; (iii) improve system resilience through cloud-native multi-AZ and cross-region architecture; and (iv) achieve long-term cost optimisation through a shift to operational expenditure model.

---

### 2. Board/Senior Management Understanding of RMIT Responsibilities

We confirm that the Board of Directors and senior management understand their responsibilities under the RMIT in relation to the cloud migration.

**Supporting details:**

- The Board Risk and Technology Committee (BRTC) was briefed on the RMIT requirements applicable to the cloud migration on 18 December 2025 (pre-engagement briefing) and 10 March 2026 (IESP results deliberation).
- Roles and responsibilities for technology risk management in the cloud environment have been clearly defined in the Cloud Governance Framework (v1.0, November 2025) and communicated to all relevant stakeholders.
- The BRTC is the designated Board-level committee responsible for oversight of technology risk, including the cloud migration programme, in accordance with paragraph 8.3 of the RMIT.
- Senior management, including the CTO, CISO, and CRO, have completed cloud technology risk awareness briefings conducted by CyberAssure Advisory on 8 January 2026.

---

### 3. Risk Management Process Subject to Appropriate Oversight

We confirm that the risk management process in respect of the cloud migration is subject to appropriate oversight.

**Supporting details:**

- A technology risk assessment has been conducted by CyberAssure Advisory Sdn Bhd as an Independent External Service Provider (IESP), in accordance with paragraph 17.1 and Appendix 7 of the RMIT.
- The risk assessment report (dated 7 March 2026, reference CA/IESP/2026/BPB-001/RAR) identified 11 findings (0 Critical, 3 High, 5 Medium, 3 Low) and the overall recommendation is "Recommend with Conditions."
- The IESP assessment report and findings were reviewed and deliberated upon by the BRTC at its meeting on 10 March 2026.
- Ongoing risk monitoring and reporting mechanisms are in place, including monthly cloud risk reporting to the IT Risk Management Committee, quarterly risk reporting to the BRTC, and continuous monitoring via the Cloud Security Operations Centre.
- The risk management process is governed by the Bank's Enterprise Risk Management Framework (v4.0) and the Cloud Risk Management Standard (v1.0, November 2025).

---

### 4. Appropriate Security Measures in Place

We confirm that appropriate security measures are in place for the cloud-hosted core banking system.

**Supporting details:**

- Security controls have been designed and implemented in accordance with the Bank's Information Security Policy (v6.0) and Cloud Security Standard (v1.0), aligned with the RMIT, ISO 27001:2022, and the CSA Cloud Controls Matrix v4.0.
- The controls address the following areas at minimum:
  - **Encryption at rest:** All data stores (RDS Aurora, S3, EBS) are encrypted using AWS KMS with customer-managed keys (CMK), with automatic annual key rotation enabled.
  - **Encryption in transit:** TLS 1.3 is enforced on all external-facing endpoints; internal service-to-service communication uses mTLS within the EKS service mesh.
  - **Web application security:** AWS WAF with managed rule sets (OWASP Top 10, known bad inputs) and custom rules; AWS Shield Advanced for DDoS protection.
  - **Threat detection:** Amazon GuardDuty is enabled across all AWS accounts and regions (including DR) for continuous threat monitoring.
  - **Access control:** Multi-factor authentication (MFA) is enforced for all IAM users, federated access, and privileged operations. AWS SSO with Active Directory federation provides centralised identity management.
  - **Network security:** Defence-in-depth architecture with VPC segmentation, security groups, NACLs, and private subnets for all data-tier resources. Direct Connect with VPN backup for private connectivity.
- Penetration testing of the cloud infrastructure was conducted by an independent firm in January 2026, with all critical and high findings remediated.
- Three High-rated findings from the IESP assessment (F-001, F-002, F-003) have approved remediation plans with target completion before the May 2026 go-live date.

---

### 5. Customer Support Services in Place

We confirm that adequate customer support services are in place for the cloud-hosted core banking system.

**Supporting details:**

- Customer support channels include: (i) 24/7 call centre (1-800-88-PERDANA) with dedicated Tier 2 escalation for digital banking issues; (ii) online banking support via live chat and secure messaging; (iii) mobile app in-app support; and (iv) branch-based support across 95 branches nationwide.
- Service level targets for customer support have been established: initial response within 15 minutes for critical issues, resolution within 4 hours for Priority 1 incidents, and 8 hours for Priority 2 incidents.
- Customer complaint handling procedures (SOP-CS-007, v3.0) are in place and address technology-related service disruptions.
- Customer communication plans have been prepared for the migration go-live, including pre-migration notifications (14 days and 3 days prior), migration weekend communications, and post-migration support reinforcement.

---

### 6. Performance Monitoring Established

We confirm that performance monitoring has been established for the cloud-hosted core banking system.

**Supporting details:**

- Key performance indicators and service level agreements have been defined, including: system availability target of 99.95% (measured monthly), API response time p95 < 200ms, batch processing completion within 2-hour window, and database query response time p99 < 50ms.
- Monitoring is implemented through a dual-layer approach: (i) AWS CloudWatch for infrastructure-level metrics, alarms, and dashboards; and (ii) Datadog APM for application-level performance monitoring, distributed tracing, and real-time user experience monitoring.
- The AWS Enterprise Support agreement (signed December 2025) provides access to a designated Technical Account Manager (TAM) and a 99.95% uptime SLA for the underlying AWS services.
- Performance reports are generated daily (automated) and reviewed weekly by the Cloud Operations team. Monthly performance summaries are reported to the IT Steering Committee.
- Escalation procedures for performance threshold breaches are defined in the Cloud Operations Runbook (v2.1), with automated alerting to the on-call Cloud CoE engineer and escalation to the CTO for P1 incidents.

---

### 7. Contingency and Business Resumption Plans

We confirm that contingency and business resumption plans are in place for the cloud-hosted core banking system.

**Supporting details:**

- A Business Continuity Plan covering the cloud-hosted core banking system (BCP — Core Banking Cloud v1.0) has been developed and approved by the BRTC on 22 January 2026.
- A Disaster Recovery Plan (DRP — AWS Cloud v1.0) has been established with the following targets: Recovery Time Objective (RTO) of 4 hours and Recovery Point Objective (RPO) of 1 hour.
- The DR architecture leverages Aurora Global Database for cross-region replication (ap-southeast-1 to ap-southeast-3), S3 Cross-Region Replication, and pre-provisioned EKS infrastructure in the Jakarta DR region.
- DR testing was conducted on 28 February 2026 with successful results: RTO achieved at 3 hours 32 minutes (within 4-hour target) and RPO verified at 47 minutes (within 1-hour target).
- The BCP/DRP is subject to review and update annually, or upon any material change to the cloud infrastructure. Semi-annual DR tests are scheduled post go-live.

---

### 8. Adequate Resources

We confirm that adequate resources have been allocated for the cloud-hosted core banking system.

**Supporting details:**

- A Cloud Centre of Excellence (CoE) comprising 8 full-time employees has been established with the following roles: Cloud Architect (1), Cloud Security Engineer (2), Cloud Operations Engineer (3), DevOps Engineer (1), and Cloud CoE Lead (1).
- AWS Enterprise Support has been procured, providing 24/7 access to senior cloud support engineers, a designated Technical Account Manager, and Infrastructure Event Management support for the go-live.
- Key vendor support arrangements are in place: Temenos Premium Support for T24/Transact R23, Datadog Enterprise licence for APM and monitoring, and CyberAssure Advisory retained for post-go-live advisory support (3 months).
- A structured training programme has been approved to upskill the Cloud CoE, with a target for all members to achieve at minimum AWS Solutions Architect Associate and AWS Security Specialty certifications by December 2026.
- Adequate financial resources have been budgeted: RM45 million for the migration programme (approved October 2024) and RM12 million per annum for ongoing cloud operations (approved in the FY2026 IT budget).

---

### 9. Systems, Procedures, and Security Measures Will Be Constantly Reviewed

We confirm that the systems, procedures, and security measures for the cloud-hosted core banking system will be constantly reviewed.

**Supporting details:**

- A periodic review schedule has been established:
  - **Security reviews:** Quarterly reviews by the CISO function, including cloud security posture assessment
  - **Vulnerability assessments:** Monthly automated scanning using Qualys and AWS-native tools; ad hoc scanning upon significant changes
  - **Penetration testing:** Annual penetration testing by an independent third party (next scheduled: January 2027)
  - **Policy and procedure reviews:** Annual review of all cloud-related policies and SOPs
  - **Technology risk assessments (IESP):** Annual IESP assessment (next scheduled: Q1 2027)
- Change management procedures are in place to assess the impact of all changes on the security and risk posture, including mandatory security review for all infrastructure and application changes classified as "Major" or "Emergency."
- Continuous monitoring mechanisms include: AWS GuardDuty for threat detection, AWS Config for configuration compliance, CloudWatch alarms for operational anomalies, Datadog for application performance, and centralised SIEM (Splunk) for log aggregation and correlation.
- The Bank will engage an IESP for subsequent assessments in accordance with the RMIT requirements, with the next assessment planned for Q1 2027.

---

### Declaration

We declare that the information provided in this confirmation letter is true and accurate to the best of our knowledge and belief.

We acknowledge that this confirmation letter is provided to Bank Negara Malaysia pursuant to the RMIT Policy Document (November 2025) and that any material misstatement may constitute a breach of regulatory requirements.

We further note that three conditions have been imposed by the IESP (CyberAssure Advisory Sdn Bhd) in respect of findings F-001 (excessive IAM permissions), F-002 (audit logging gaps), and F-003 (untested exit strategy). The BRTC has approved remediation plans for all three conditions with target completion before the May 2026 go-live date. Evidence of remediation will be provided to the IESP for verification prior to production deployment.

---

### Authorised Signatories

**Signatory 1:**

| | |
|---|---|
| **Name** | Tan Sri Dato' Mohamad Ibrahim bin Abdul Rahman |
| **Designation** | Chairman, Board Risk and Technology Committee |
| **Signature** | *[Signed]* |
| **Date** | 14 March 2026 |

**Signatory 2:**

| | |
|---|---|
| **Name** | Encik Ahmad Razali bin Mohd Noor |
| **Designation** | Chief Technology Officer |
| **Signature** | *[Signed]* |
| **Date** | 14 March 2026 |

---

**Enclosures:**

1. Risk Assessment Report (Appendix 7 Part A) — Reference: CA/IESP/2026/BPB-001/RAR, dated 7 March 2026
2. Attestation (Appendix 7 Part D) — Reference: CA/IESP/2026/BPB-001/PDA, dated 7 March 2026
3. Remediation Plan — Reference: BPB/IT/2026/RP-001, dated 10 March 2026

---

**Company Stamp:** Bank Perdana Berhad (199301012345)
