# IESP Scoping Document

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

---

**Engagement Reference:** [Reference Number]

**Financial Institution:** [FI Name]

**ESP:** [ESP Name]

**Version:** [X.X]

**Date:** [DD/MM/YYYY]

**Status:** Draft / Final

---

## 1. Engagement Type Selection

Select the applicable engagement type(s):

| # | Engagement Type | RMIT Reference | Selected |
|---|----------------|----------------|----------|
| 1 | Data Centre Resilience Assessment (DCRA) | Para 10.24--10.28 | [ ] |
| 2 | Network Resilience Assessment (NRA) | Para 10.36--10.43 | [ ] |
| 3 | Technology Risk Assessment (System Acquisition/Development) | Para 17.1, App 7 | [ ] |
| 4 | Cloud Services Assessment | App 10 | [ ] |
| 5 | AI / Emerging Technology Assessment | App 9 | [ ] |
| 6 | Combined Assessment | [Specify] | [ ] |
| 7 | Other | [Specify] | [ ] |

**Engagement trigger:**

- [ ] Scheduled periodic assessment (per RMIT frequency requirements)
- [ ] New system/service implementation
- [ ] Material change to existing system/service
- [ ] Regulatory direction
- [ ] Incident-driven
- [ ] Other: [Specify]

---

## 2. In-Scope Systems, Infrastructure, and Processes

### 2.1 Systems and Applications

| # | System/Application | Classification | Environment | Owner | Business Function |
|---|-------------------|---------------|-------------|-------|-------------------|
| 1 | [Name] | Critical / Important / Other | Production / DR | [Name] | [Function] |
| 2 | [Name] | [Classification] | [Environment] | [Name] | [Function] |

### 2.2 Infrastructure Components

| # | Component | Type | Location | Details |
|---|-----------|------|----------|---------|
| 1 | [Name/ID] | Server / Network / Storage / Other | [Site] | [Model, OS, version] |
| 2 | [Name/ID] | [Type] | [Site] | [Details] |

### 2.3 Data Centres / Facilities

| # | Facility | Type | Location | Tier | Operator |
|---|----------|------|----------|------|----------|
| 1 | [Name] | Primary / DR / Near-site | [Address] | [Tier level] | In-house / Outsourced |

### 2.4 Network Segments

| # | Segment | Description | Classification |
|---|---------|-------------|---------------|
| 1 | [Name/ID] | [Description] | [Internal / DMZ / External / Cloud] |

### 2.5 Cloud Services (if applicable)

| # | Service | CSP | Model | Region | Classification |
|---|---------|-----|-------|--------|---------------|
| 1 | [Name] | [CSP Name] | IaaS / PaaS / SaaS | [Region] | Critical / Non-critical |

### 2.6 Processes

| # | Process | Owner | Frequency | Description |
|---|---------|-------|-----------|-------------|
| 1 | [Name] | [Name/Title] | [Daily/Weekly/etc.] | [Brief description] |

---

## 3. Out-of-Scope Items and Justification

| # | Item/Area | Justification for Exclusion | Approved By |
|---|-----------|---------------------------|-------------|
| 1 | [Item] | [Reason -- e.g., covered by separate engagement, not material, not applicable] | [Name/Title] |
| 2 | [Item] | [Reason] | [Name/Title] |

**Note:** All exclusions must be justified and approved by the FI's designated responsible officer. Exclusions that may affect the ability to provide the required assurance under Appendix 7 must be disclosed in the risk assessment report.

---

## 4. Applicable RMIT Clauses and Appendices

### 4.1 Core RMIT Paragraphs

| # | Paragraph | Title/Subject | Applicability Notes |
|---|-----------|---------------|-------------------|
| 1 | [Para X.X] | [Title] | [Notes on applicability] |

### 4.2 Applicable Appendices

| # | Appendix | Title | Sections Applicable |
|---|----------|-------|-------------------|
| 1 | Appendix 7 | Risk Assessment Report | Parts A, B, C, D |
| 2 | [Appendix X] | [Title] | [Sections] |

### 4.3 Part D Minimum Controls Mapping

The assessment shall, at minimum, cover the controls specified in Appendix 7 Part D applicable to the engagement type. The detailed control mapping is as follows:

| # | Part D Control Area | Applicable | Test Approach |
|---|-------------------|-----------|---------------|
| 1 | [Control area] | Yes / No / Partial | [Inspection / Interview / Testing / Observation] |

---

## 5. Assessment Criteria

### 5.1 Primary Assessment Criteria

The assessment will be conducted against:

1. **RMIT Appendix 7 Part D** -- Minimum controls for the applicable engagement type
2. **Specific RMIT paragraphs** -- As listed in Section 4.1
3. **FI's own policies and standards** -- Where they exceed RMIT minimum requirements

### 5.2 Supplementary Frameworks (if applicable)

| Framework | Version | Application |
|-----------|---------|-------------|
| ISO 27001 | [Year] | [How it supplements the assessment] |
| NIST CSF | [Version] | [How it supplements the assessment] |
| CSA CCM | [Version] | [Cloud-specific controls] |
| [Other] | [Version] | [Application] |

### 5.3 Risk Rating Methodology

Findings will be rated using the following scale:

| Rating | Definition | Expected Remediation |
|--------|-----------|---------------------|
| **Critical** | Immediate threat to confidentiality, integrity, or availability of critical systems; regulatory non-compliance with material impact | Immediate action required |
| **High** | Significant control weakness with potential for material impact | Remediation within 30 days |
| **Medium** | Control weakness with moderate risk exposure | Remediation within 90 days |
| **Low** | Minor control improvement opportunity | Remediation within 180 days |
| **Observation** | Best practice recommendation; no immediate risk | For management consideration |

---

## 6. Key Contacts and Stakeholders

### 6.1 FI Contacts

| Role | Name | Title | Email | Phone |
|------|------|-------|-------|-------|
| Engagement Sponsor | [Name] | [Title] | [Email] | [Phone] |
| Primary Liaison | [Name] | [Title] | [Email] | [Phone] |
| IT/Technology Lead | [Name] | [Title] | [Email] | [Phone] |
| Risk Management | [Name] | [Title] | [Email] | [Phone] |
| Compliance | [Name] | [Title] | [Email] | [Phone] |
| Internal Audit | [Name] | [Title] | [Email] | [Phone] |

### 6.2 ESP Team

| Role | Name | Qualifications | Contact |
|------|------|---------------|---------|
| Engagement Partner | [Name] | [Certs] | [Email] |
| Engagement Manager | [Name] | [Certs] | [Email] |
| Lead Assessor | [Name] | [Certs] | [Email] |
| Technical Specialist | [Name] | [Certs] | [Email] |

### 6.3 Third Parties (if applicable)

| Organisation | Role | Contact | Access Required |
|-------------|------|---------|----------------|
| [CSP Name] | Cloud Service Provider | [Contact] | [Access details] |
| [Vendor Name] | [Role] | [Contact] | [Access details] |

---

## 7. Timeline and Milestones

| # | Milestone | Target Date | Owner | Status |
|---|-----------|-------------|-------|--------|
| 1 | Engagement letter signed | [Date] | FI / ESP | [ ] |
| 2 | Scoping document finalised | [Date] | ESP | [ ] |
| 3 | Document request issued | [Date] | ESP | [ ] |
| 4 | Documents received (deadline) | [Date] | FI | [ ] |
| 5 | Fieldwork commencement | [Date] | ESP | [ ] |
| 6 | Fieldwork completion | [Date] | ESP | [ ] |
| 7 | Draft report issued | [Date] | ESP | [ ] |
| 8 | Management response received | [Date] | FI | [ ] |
| 9 | Final report issued | [Date] | ESP | [ ] |
| 10 | Board/Committee presentation | [Date] | ESP / FI | [ ] |

**Fieldwork schedule:**

| Day/Week | Activity | Personnel | Location |
|----------|----------|-----------|----------|
| [Date range] | [Activity] | [Names] | [On-site / Remote] |

---

## 8. Assumptions and Constraints

### 8.1 Assumptions

1. The FI will provide complete and accurate documentation within the agreed timelines.
2. Key personnel will be available for interviews during the fieldwork period.
3. Access to systems and premises will be granted as per the access request form.
4. The FI's policies, procedures, and controls documentation is current and reflects the actual operating environment.
5. No material changes to the in-scope environment will occur during the assessment period without prior notification to the ESP.
6. Management representations provided by the FI are made in good faith.

### 8.2 Constraints

1. The assessment is limited to the scope defined in this document.
2. Testing will be conducted in [production / non-production / both] environments.
3. Destructive or intrusive testing [will / will not] be performed. Any such testing requires separate written approval.
4. Assessment timelines are subject to the FI's timely provision of documentation and access.
5. [List any other constraints -- e.g., regulatory deadlines, blackout periods, change freezes.]

### 8.3 Dependencies

| # | Dependency | Owner | Impact if Not Met |
|---|-----------|-------|-------------------|
| 1 | [Dependency] | [Owner] | [Impact] |

---

## 9. Document Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [Date] | [Name] | Initial draft |
| 1.0 | [Date] | [Name] | Finalised |

---

## 10. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| FI Engagement Sponsor | [Name] | _________ | [Date] |
| ESP Engagement Lead | [Name] | _________ | [Date] |
