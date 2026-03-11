> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative.

---

# Appendix 7 Part D — Negative Attestation

## Technology Risk Assessment: Minimum Control Requirements

---

**Confidential**

**Report Reference:** CA/IESP/2026/BPB-001/PDA

**Date of Attestation:** 7 March 2026

**Assessment Period:** 6 January 2026 to 7 March 2026

**Financial Institution:** Bank Perdana Berhad

**System Under Assessment:** Core Banking System (Temenos T24/Transact R23) on Amazon Web Services

**External Service Provider:** CyberAssure Advisory Sdn Bhd

---

## 1. Purpose

This document provides the Part D negative attestation as required by Appendix 7 of the Risk Management in Technology (RMIT) Policy Document (November 2025). It sets out the assessment results against the minimum control requirements specified in Part D and provides the ESP's attestation on the effectiveness of those controls.

## 2. Assessment Scope

The assessment covered all Part D minimum control requirements applicable to the cloud-hosted core banking system, grouped into two categories:

- **Part D Section 1 (Items 1a–1f):** Security controls for systems, infrastructure, and operations
- **Part D Section 2 (Items 2a–2e):** Controls specific to electronic banking and payment systems

## 3. Assessment Results Against Part D Minimum Controls

### 3.1 Summary Matrix

| Part D Item | Control Area | Test Refs | Status | Findings |
|-------------|-------------|-----------|--------|----------|
| **1(a)** | Access Control | PD-001 to PD-008 | **Partially Met** | F-001 |
| **1(b)** | Physical Security | PD-009 to PD-012 | **Met** | — |
| **1(c)** | Operations Security | PD-013 to PD-020 | **Met** | — |
| **1(d)** | Communications Security | PD-021 to PD-026 | **Met** | — |
| **1(e)** | Incident Management | PD-027 to PD-034 | **Partially Met** | F-002, F-007 |
| **1(f)** | Business Continuity Management | PD-035 to PD-040 | **Partially Met** | F-006 |
| **2(a)** | Customer Authentication | PD-041 to PD-046 | **Met** | — |
| **2(b)** | Transaction Authorisation | PD-047 to PD-050 | **Met** | — |
| **2(c)** | Segregation of Duties & Access Control | PD-051 to PD-055 | **Met** | — |
| **2(d)** | Data Integrity | PD-056 to PD-060 | **Met** | — |
| **2(e)** | Mobile Device Security | PD-061 to PD-064 | **Met** | — |

### 3.2 Detailed Results — Section 1: Security Controls

#### Item 1(a): Access Control — Partially Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-001 | Documented access control policy exists | Met | IAM Policy v2.0 in place |
| PD-002 | Least-privilege principle enforced | **Not Met** | F-001: 4 of 12 IAM roles have excessive permissions |
| PD-003 | Privileged access management controls | Met | PAM solution (CyberArk) for administrative access |
| PD-004 | Multi-factor authentication enforcement | Met | MFA enforced for all IAM users and federated access |
| PD-005 | Access provisioning and de-provisioning process | Met | SOP in place; tested sample of 30 requests |
| PD-006 | Periodic access review conducted | **Not Met** | F-001: Stale service accounts (>90 days) not removed |
| PD-007 | Service account management | **Not Met** | F-001: 3 PoC service accounts with admin permissions |
| PD-008 | Logging of access events | Met | CloudTrail captures IAM and authentication events |

**Overall: Partially Met** — Gaps in least-privilege enforcement and service account lifecycle management. Remediation in progress.

#### Item 1(b): Physical Security — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-009 | Data centre physical security | Met | Reliance on AWS SOC 2 Type II (Oct 2024–Sep 2025) |
| PD-010 | Environmental controls | Met | AWS SOC 2 covers HVAC, fire suppression, power redundancy |
| PD-011 | Physical access logging | Met | AWS SOC 2 confirms biometric access and CCTV |
| PD-012 | Direct Connect termination security | Met | BPB Cyberjaya DC physical controls verified |

**Overall: Met** — Physical security is managed by AWS with independent SOC 2 Type II attestation. BPB's complementary controls at Direct Connect termination points are adequate.

#### Item 1(c): Operations Security — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-013 | Documented operational procedures | Met | Cloud Operations Runbook v2.1 |
| PD-014 | Change management process | Met | CAB process in place (F-005 is improvement observation) |
| PD-015 | Vulnerability management programme | Met | Monthly scanning; remediation within SLA |
| PD-016 | Patch management procedures | Met | Automated via AWS Systems Manager |
| PD-017 | Backup management | Met | Automated Aurora snapshots; S3 versioning |
| PD-018 | Capacity management | Met | Auto Scaling; capacity modelling completed |
| PD-019 | Separation of environments | Met | Separate AWS accounts for prod, staging, dev |
| PD-020 | Malware protection | Met | GuardDuty Malware Protection; EKS runtime security |

**Overall: Met** — Operational controls are well-established. Medium findings F-004 (CSPM) and F-005 (IaC drift) relate to enhancements beyond the minimum control requirements.

#### Item 1(d): Communications Security — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-021 | Network segmentation | Met | VPC segmentation; private subnets for data tier |
| PD-022 | Encryption of data in transit | Met | TLS 1.3 enforced on all external endpoints |
| PD-023 | Firewall / security group management | Met | Least-privilege security groups; no overly permissive rules |
| PD-024 | Intrusion detection / prevention | Met | GuardDuty network threat detection; WAF |
| PD-025 | DDoS protection | Met | AWS Shield Advanced |
| PD-026 | Secure remote access | Met | VPN with MFA; no direct SSH to production |

**Overall: Met** — Network and communications security controls are robust with defence-in-depth.

#### Item 1(e): Incident Management — Partially Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-027 | Incident management policy and procedures | Met | Incident Management Policy v5.0 |
| PD-028 | Security event monitoring and detection | **Partially Met** | F-002: S3 data events not logged; GuardDuty not enabled in DR |
| PD-029 | SIEM / log aggregation | **Partially Met** | F-002: SIEM integration 75% complete |
| PD-030 | Incident response team and capabilities | Met | SOC team with 24/7 coverage |
| PD-031 | Incident response playbooks | **Partially Met** | F-007: 1 of 3 cloud playbooks complete |
| PD-032 | Incident escalation procedures | Met | Escalation matrix defined and tested |
| PD-033 | Regulatory incident reporting | Met | BNM notification SOP in place |
| PD-034 | Post-incident review process | Met | Root cause analysis framework documented |

**Overall: Partially Met** — Incident management framework is sound but cloud-specific detection and response capabilities have gaps.

#### Item 1(f): Business Continuity Management — Partially Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-035 | BCP/DRP documented and approved | Met | BCP and DRP v1.0, approved Jan 2026 |
| PD-036 | RTO/RPO defined and appropriate | Met | RTO 4hr, RPO 1hr — appropriate for Tier 1 system |
| PD-037 | DR architecture implemented | Met | Cross-region DR with Aurora Global Database |
| PD-038 | DR test conducted successfully | **Partially Met** | F-006: Initial test failed RTO; remediation test passed |
| PD-039 | BCP/DRP reviewed periodically | Met | Annual review schedule established |
| PD-040 | Crisis communication plan | Met | Communication plan for DR activation documented |

**Overall: Partially Met** — BCP/DRP framework is adequate. The initial DR test failure (F-006) was remediated and the subsequent test on 28 Feb 2026 met all targets (RTO 3.5hr, RPO 47min). Only one successful test has been completed.

### 3.3 Detailed Results — Section 2: Electronic Banking Controls

#### Item 2(a): Customer Authentication — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-041 | Multi-factor authentication for customers | Met | Risk-based adaptive MFA |
| PD-042 | Password/credential management | Met | Password policy meets RMIT requirements |
| PD-043 | Session management | Met | Timeout and re-authentication controls |
| PD-044 | Device identification/fingerprinting | Met | Device fingerprinting for internet and mobile banking |
| PD-045 | Failed login attempt management | Met | Progressive lockout with account recovery |
| PD-046 | Secure credential storage | Met | Argon2 hashing; HSM for cryptographic operations |

#### Item 2(b): Transaction Authorisation — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-047 | Transaction authorisation workflows | Met | Maker-checker for high-value transactions |
| PD-048 | Transaction signing / verification | Met | OTP and push notification for transaction signing |
| PD-049 | Transaction limits and controls | Met | Configurable limits with threshold-based alerts |
| PD-050 | Real-time transaction monitoring | Met | Fraud detection rules and anomaly monitoring |

#### Item 2(c): Segregation of Duties and Access Control — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-051 | SoD matrix defined and enforced | Met | T24 role matrix with SoD conflict analysis |
| PD-052 | Developer/operator separation | Met | Separate AWS accounts; CI/CD role separation |
| PD-053 | Approval workflows for sensitive operations | Met | Dual approval for production deployments |
| PD-054 | Audit trail for privileged operations | Met | CloudTrail and session recording |
| PD-055 | Periodic SoD review | Met | Quarterly SoD review documented |

#### Item 2(d): Data Integrity — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-056 | Data validation controls | Met | Input validation and referential integrity checks |
| PD-057 | Database integrity mechanisms | Met | Aurora checksums and WAL verification |
| PD-058 | End-of-day reconciliation | Met | Automated reconciliation with exception reporting |
| PD-059 | Data migration integrity | Met | Hash-based verification and parallel-run comparison |
| PD-060 | Backup integrity verification | Met | Automated backup restoration tests |

#### Item 2(e): Mobile Device Security — Met

| Test Ref | Control Tested | Result | Observation |
|----------|---------------|--------|-------------|
| PD-061 | Mobile app security (RASP, certificate pinning) | Met | RASP, jailbreak/root detection, cert pinning |
| PD-062 | Secure local storage | Met | No sensitive data in local storage; encrypted keychain |
| PD-063 | MDM for staff mobile access | Met | MDM enrolment required for AWS console access |
| PD-064 | Mobile app penetration testing | Met | Annual pen test (Dec 2025) — no critical findings |

---

## 4. Negative Attestation

### Option B — Attestation with Exceptions

Based on the work performed and the evidence obtained during the assessment period of 6 January to 7 March 2026, nothing has come to our attention that causes us to believe that the technology risk management controls assessed against the minimum requirements of Appendix 7 Part D of the RMIT (November 2025) are not, in all material respects, designed and operating effectively, **except for the following matters:**

1. **F-001 (High) — Excessive IAM Permissions and Stale Service Accounts:** Access control requirements under Item 1(a) are partially met due to the identification of four IAM roles with excessive permissions and three stale service accounts with administrative-level access.

2. **F-002 (High) — Insufficient Audit Logging Configuration:** Incident management requirements under Item 1(e) are partially met due to incomplete audit logging (S3 data events not enabled, GuardDuty not enabled in DR region, SIEM integration incomplete).

3. **F-003 (High) — Untested Cloud Exit Strategy:** While not a Part D minimum control, this finding is material to the overall technology risk posture and is included as an exception to the attestation in accordance with professional standards.

These exceptions are reflected in the conditions set out in the Risk Assessment Report (reference CA/IESP/2026/BPB-001/RAR, Section 5.2).

---

## 5. Authorised Signatory

| | |
|---|---|
| **Name** | Puan Siti Nabilah binti Mohd Yusof |
| **Designation** | Director, Technology Risk Advisory |
| **Professional Qualifications** | CISA, CCSP, CISSP |
| **Firm** | CyberAssure Advisory Sdn Bhd (SSM 201501023456) |
| **Signature** | *[Signed]* |
| **Date** | 7 March 2026 |

---

*End of Part D Attestation*
