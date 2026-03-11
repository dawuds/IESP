> **⚠️ AI-GENERATED EXAMPLE — FOR EDUCATIONAL PURPOSES ONLY**
> This is a fictitious worked example. All entities, names, findings, and data are illustrative.

---

# Remediation Tracker

## IESP Finding Remediation Status — As at 10 March 2026

---

**Financial Institution:** Bank Perdana Berhad

**IESP Report Reference:** CA/IESP/2026/BPB-001/RAR (dated 7 March 2026)

**Tracker Reference:** BPB/IT/2026/RT-001

**Prepared by:** Puan Faridah binti Hassan, Chief Information Security Officer

**Reporting Date:** 10 March 2026

**Next Update Due:** 14 April 2026 (BRTC meeting)

---

## Status Summary

| Status | Count |
|--------|-------|
| Completed | 2 |
| In Progress | 5 |
| Not Started | 4 |
| **Total** | **11** |

**By Severity:**

| Severity | Total | Completed | In Progress | Not Started |
|----------|-------|-----------|-------------|-------------|
| High | 3 | 0 | 2 | 1 |
| Medium | 5 | 1 | 3 | 1 |
| Low | 3 | 1 | 0 | 2 |
| **Total** | **11** | **2** | **5** | **4** |

---

## Detailed Remediation Status

| Finding ID | Title | Rating | Owner | Action | Target Date | Status | Evidence | Verification |
|-----------|-------|--------|-------|--------|-------------|--------|----------|-------------|
| F-001 | Excessive IAM Permissions and Stale Service Accounts | High | Encik Wong Kar Wai, IAM Lead | Rescope IAM policies to least privilege; remove stale accounts; implement quarterly access review | 15 Apr 2026 | **In Progress** | IAM Access Analyzer deployed 3 Mar; 2 of 4 policies rescoped; 3 stale accounts disabled 5 Mar; quarterly review SOP drafted | Pending — IESP verification required before go-live |
| F-002 | Insufficient Audit Logging Configuration | High | Puan Lee Mei Ling, SOC Manager | Enable S3 data events; enable GuardDuty in DR region; complete SIEM integration | 31 Mar 2026 | **In Progress** | S3 data events enabled 6 Mar; GuardDuty DR scheduled 12 Mar; SIEM integration 75% complete (EKS and Lambda logs remaining) | Pending — IESP verification required before go-live |
| F-003 | Untested Cloud Exit Strategy | High | Encik Raj Kumar, Head of Cloud Engineering | Conduct exit strategy test; data extraction validation; cost estimate; timeline estimation | 30 Apr 2026 | **Not Started** | Scheduled to commence post go-live preparation phase; 2-person team ring-fenced | Pending — IESP verification required before go-live |
| F-004 | CSPM Tool Not Deployed | Medium | Encik Raj Kumar, Head of Cloud Engineering | Evaluate and deploy Wiz CSPM for continuous cloud security posture monitoring | 30 Apr 2026 | **Not Started** | Wiz procurement in progress; vendor demo completed 4 Mar; awaiting procurement approval | Internal Audit verification |
| F-005 | IaC Drift Detection Not Automated | Medium | Encik David Lim, DevOps Lead | Implement Terraform Cloud with automated drift detection and alerting | 30 Apr 2026 | **In Progress** | Terraform Cloud trial started 1 Mar; dev environment configured; staging rollout planned 20 Mar | Internal Audit verification |
| F-006 | DR Test Initially Exceeded RTO Target | Medium | Encik Mohd Faisal, Head of BCM | Optimise DR failover; conduct remediation DR test; validate RTO/RPO achievement | 28 Feb 2026 | **Completed** | DR test completed 28 Feb 2026; RTO achieved at 3hr 32min (target: 4hr); RPO at 47min (target: 1hr); Aurora failover optimised | Verified by IESP (observed test) |
| F-007 | Incomplete Cloud Incident Response Playbooks | Medium | Puan Lee Mei Ling, SOC Manager | Complete 3 cloud-specific playbooks (account compromise, data exfiltration, service disruption); conduct tabletop exercise | 20 Mar 2026 | **In Progress** | Account compromise playbook finalised; data exfiltration playbook in draft (80%); service disruption playbook in draft (60%); tabletop scheduled 18 Mar | Internal Audit verification |
| F-008 | Manual Cryptographic Key Rotation | Low | Encik Tan Chee Keong, DBA Lead | Enable automatic KMS CMK rotation for all customer-managed keys | 25 Feb 2026 | **Completed** | Auto-rotation enabled for all 7 CMKs on 25 Feb 2026; verified via AWS Config rule `cmk-backing-key-rotation-enabled` | Verified by IESP (configuration review) |
| F-009 | Cloud Skills Gap in Operations Team | Medium | Encik Raj Kumar, Head of Cloud Engineering | Execute structured training plan; target AWS certifications for all 8 CoE members | 31 Dec 2026 | **In Progress** | Training plan approved by CTO 5 Mar; 3 staff already certified (SA Pro, Security Specialty); 2 staff enrolled in SA Associate (exam Apr 2026); remaining 3 staff training scheduled Q3 2026 | Internal Audit verification (Dec 2026) |
| F-010 | Container Image Scanning Gap | Low | Encik David Lim, DevOps Lead | Integrate container image scanning (Trivy) as mandatory CI/CD pipeline gate | 30 Jun 2026 | **Not Started** | Trivy evaluation in progress; shortlisted alongside Snyk Container; decision expected Apr 2026 | Internal Audit verification |
| F-011 | Cloud Cost Optimisation Review Pending | Low | Encik Raj Kumar, Head of Cloud Engineering | Conduct cloud cost optimisation review; deploy AWS Cost Anomaly Detection and budget alerts | 30 Jun 2026 | **Not Started** | Planned for Q2 2026 post go-live; AWS Cost Explorer enabled; Cost Anomaly Detection configuration to follow | Internal Audit verification |

---

## Key Milestones

| Date | Milestone | Status |
|------|-----------|--------|
| 25 Feb 2026 | F-008 remediation complete (key rotation) | Done |
| 28 Feb 2026 | F-006 remediation complete (DR test) | Done |
| 12 Mar 2026 | F-002 GuardDuty DR enablement | Scheduled |
| 18 Mar 2026 | F-007 tabletop exercise | Scheduled |
| 20 Mar 2026 | F-007 all playbooks finalised | Target |
| 31 Mar 2026 | F-002 SIEM integration complete | Target |
| 15 Apr 2026 | F-001 full remediation | Target |
| 14 Apr 2026 | BRTC progress update | Scheduled |
| 30 Apr 2026 | F-003 exit strategy test complete | Target |
| 30 Apr 2026 | F-004 Wiz CSPM deployed | Target |
| May 2026 | Production go-live (conditional) | Planned |
| Q1 2027 | Follow-up IESP assessment | Planned |

---

*End of Remediation Tracker*
