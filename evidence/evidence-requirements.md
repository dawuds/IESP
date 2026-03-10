# Evidence Requirements Overview

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

---

## 1. Purpose

This document provides an overview of evidence requirements for IESP engagements conducted under the BNM Risk Management in Technology (RMIT) Policy Document (November 2025). It serves as a guide for both FI management and ESP assessors to ensure that sufficient, appropriate evidence is obtained to support the assessment conclusions and the risk assessment report (Appendix 7 Part A).

---

## 2. Evidence Principles

### 2.1 Sufficiency

Evidence must be sufficient in quantity and quality to support the assessment conclusions. The ESP must obtain enough evidence to form a reasonable basis for its findings and overall opinion.

### 2.2 Appropriateness

Evidence must be relevant to the control objective being assessed and reliable in its nature and source. The following hierarchy of evidence reliability applies (from most to least reliable):

| Rank | Evidence Type | Description | Example |
|------|-------------|-------------|---------|
| 1 | Direct observation | ESP directly observes a control in operation | Data centre physical walkthrough |
| 2 | Independent confirmation | Evidence obtained from independent third parties | SOC 2 reports, CSP certifications |
| 3 | System-generated | Evidence produced by systems without manual intervention | Automated logs, system configurations |
| 4 | Re-performance | ESP re-performs the control procedure | Re-testing access control settings |
| 5 | Documentary | Policies, procedures, and records maintained by the FI | Approved policies, meeting minutes |
| 6 | Inquiry | Verbal representations from FI personnel | Interview responses |

### 2.3 Timeliness

Evidence must be current and relate to the assessment period. Historical evidence may be used to assess the operating effectiveness of controls over a period, but the ESP must consider whether the controls have changed since the evidence was generated.

### 2.4 Completeness

The evidence collection must cover all control areas within the assessment scope. Gaps in evidence should be documented and their impact on the assessment conclusions should be assessed.

---

## 3. Evidence Requirements by Engagement Type

### 3.1 Overview Matrix

| Evidence Category | DCRA | NRA | Cloud | AI/Emerging Tech | System Acquisition |
|------------------|------|-----|-------|-----------------|-------------------|
| Governance and Strategy | Required | Required | Required | Required | Required |
| Policies and Procedures | Required | Required | Required | Required | Required |
| Architecture Documentation | Required | Required | Required | Required | Required |
| Configuration Evidence | Required | Required | Required | Desirable | Required |
| Monitoring and Logging | Required | Required | Required | Required | Required |
| Incident Records | Required | Required | Required | Required | Required |
| Change Management Records | Required | Required | Required | Required | Required |
| Access Control Evidence | Required | Required | Required | Required | Required |
| BCP/DR Documentation | Required | Required | Required | Desirable | Required |
| Third-Party/Vendor Records | Desirable | Desirable | Required | Desirable | Desirable |
| Prior Assessment Reports | Required | Required | Required | Required | Required |
| Testing Records | Required | Required | Required | Required | Required |
| Training Records | Desirable | Desirable | Desirable | Required | Desirable |
| CSP Certifications/Reports | N/A | N/A | Required | N/A | Conditional |
| Model Documentation | N/A | N/A | N/A | Required | N/A |

### 3.2 Engagement-Specific Checklists

Detailed evidence checklists for each engagement type are provided in separate documents:

| Engagement Type | Checklist Document |
|----------------|-------------------|
| Data Centre Resilience Assessment (DCRA) | `evidence-checklist-dcra.md` |
| Network Resilience Assessment (NRA) | `evidence-checklist-nra.md` |
| Cloud Services Assessment | `evidence-checklist-cloud.md` |
| AI / Emerging Technology Assessment | `evidence-checklist-ai.md` |

---

## 4. Evidence Collection Process

### 4.1 Pre-Engagement

1. Issue the document request list to the FI at least [X] weeks before fieldwork commencement.
2. Specify the format requirements for each evidence item.
3. Establish a secure evidence exchange mechanism (encrypted file sharing, secure portal).
4. Set a deadline for initial document submission.

### 4.2 During Fieldwork

1. Track evidence receipt against the checklist.
2. Assess evidence quality upon receipt and request clarification or additional evidence as needed.
3. Conduct interviews and walkthroughs to supplement documentary evidence.
4. Perform technical testing and capture system-generated evidence.
5. Maintain a chain of custody for all evidence obtained.

### 4.3 Post-Fieldwork

1. Verify that all required evidence items have been obtained.
2. Document any evidence gaps and their impact on assessment conclusions.
3. Ensure all evidence is securely stored and indexed.
4. Retain working papers and evidence in accordance with professional standards.

---

## 5. Evidence Documentation Standards

### 5.1 Naming Convention

All evidence items should follow a consistent naming convention:

```
[Engagement Ref]-[Category Code]-[Sequence]-[Description]
```

Example: `DCRA-2026-GOV-001-Technology-Risk-Policy`

### 5.2 Category Codes

| Code | Category |
|------|----------|
| GOV | Governance and Strategy |
| POL | Policies and Procedures |
| ARC | Architecture and Design |
| CFG | Configuration |
| MON | Monitoring and Logging |
| INC | Incident Records |
| CHG | Change Management |
| ACC | Access Control |
| BCP | Business Continuity / Disaster Recovery |
| VEN | Vendor / Third Party |
| TST | Testing Records |
| RPT | Prior Reports |
| TRN | Training Records |
| CSP | Cloud Service Provider |
| MDL | Model Documentation (AI) |
| OTH | Other |

### 5.3 Evidence Register

Maintain an evidence register with the following fields:

| Field | Description |
|-------|-------------|
| Evidence ID | Unique identifier |
| Description | Brief description of the evidence item |
| Category | Category code |
| Source | Who provided the evidence |
| Date Received | Date the evidence was received |
| Date of Evidence | Date/period the evidence relates to |
| Format | Document / Screenshot / Log / Configuration / Report / Other |
| Classification | Confidential / Internal / Public |
| Relevance | Which finding(s) or control area(s) the evidence relates to |
| Status | Received / Pending / Not Available |
| Notes | Any notes on quality, completeness, or limitations |

---

## 6. Evidence Quality Assessment

### 6.1 Quality Criteria

For each evidence item, the ESP should assess:

| Criterion | Question |
|-----------|----------|
| **Relevance** | Does the evidence directly relate to the control being assessed? |
| **Reliability** | Is the evidence from a reliable source? Has it been tampered with? |
| **Currency** | Is the evidence current and within the assessment period? |
| **Completeness** | Does the evidence cover the full population or a representative sample? |
| **Authenticity** | Is the evidence genuine and from the stated source? |

### 6.2 Handling Evidence Gaps

When required evidence is not available, the ESP should:

1. Document the evidence gap and the reason for non-availability.
2. Assess whether alternative evidence can provide equivalent assurance.
3. Consider the impact on the assessment conclusion for the relevant control area.
4. Disclose the evidence gap and its impact in the findings report and risk assessment report.
5. If the gap is material, consider whether it constitutes a scope limitation.

---

## 7. Confidentiality and Security

### 7.1 Evidence Handling

- All evidence must be handled in accordance with the FI's data classification policy and the confidentiality terms of the engagement letter.
- Evidence containing personal data must be handled in compliance with applicable data protection laws.
- Evidence must be stored on encrypted media and transmitted via secure channels.
- Access to evidence must be restricted to authorised ESP team members.

### 7.2 Retention and Disposal

- Working papers and evidence should be retained for a minimum of [X] years in accordance with professional standards and contractual requirements.
- Upon expiry of the retention period or upon the FI's written instruction, evidence must be securely destroyed and a certificate of destruction provided.

---

## 8. Reliance on Third-Party Evidence

### 8.1 SOC Reports

When relying on SOC 1 or SOC 2 reports from third parties (e.g., CSPs, outsourced service providers):

- Verify the report covers the assessment period (or an acceptable portion thereof).
- Verify the scope of the report covers the relevant services and controls.
- Review any exceptions or qualifications noted in the report.
- Assess whether complementary user entity controls (CUECs) have been implemented by the FI.
- Consider whether bridging procedures are needed for any gap between the SOC report period and the assessment period.

### 8.2 ISO and Other Certifications

When relying on ISO 27001, ISO 22301, or other certifications:

- Verify the certification is current and issued by an accredited certification body.
- Verify the scope of the certification covers the relevant services and locations.
- Review the statement of applicability (for ISO 27001) to confirm relevant controls are included.
- Consider whether additional testing is needed beyond the certification scope.

### 8.3 Penetration Test and Vulnerability Assessment Reports

- Verify reports are from qualified, independent providers.
- Verify the scope covers the relevant systems and networks.
- Verify the reports are current (typically within the past 12 months).
- Review findings and assess whether identified vulnerabilities have been remediated.
