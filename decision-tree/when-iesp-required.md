# When is an IESP Review Required?

> BNM RMiT Nov 2025 — Independent External Service Provider Decision Guide

## Overview

An Independent External Service Provider (IESP) review is mandated by BNM under several scenarios in the Risk Management in Technology (RMiT) policy document. This guide helps compliance and attestation teams determine when an IESP engagement must be initiated.

## Decision Flowchart

```
┌─────────────────────────────────────────┐
│     What technology activity is the     │
│     financial institution undertaking?  │
└──────────────────┬──────────────────────┘
                   │
    ┌──────────────┼──────────────┬──────────────┬──────────────┬──────────────┐
    ▼              ▼              ▼              ▼              ▼              ▼
┌────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐
│  Data  │  │ Network  │  │  Cloud   │  │ Emerging │  │ Digital  │  │  BNM   │
│ Centre │  │ Infra    │  │ Adoption │  │   Tech   │  │ Services │  │Directed│
└───┬────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └───┬────┘
    ▼            ▼             ▼              ▼             ▼             ▼
 DCRA due?   NRA due?    First time     First time     Simplified    Comply as
 (3yr/mat    (3yr/mat    for critical?  for critical?  notification  directed
  change)     change)         │              │          criteria?     (17.4/1.4)
    │            │        ┌───┴───┐      ┌───┴───┐     ┌───┴───┐         │
    │            │        ▼       ▼      ▼       ▼     ▼       ▼         │
    │            │      YES      NO    YES      NO   YES      NO         │
    │            │        │       │      │       │     │       │         │
    ▼            ▼        ▼       ▼      ▼       ▼     ▼       ▼         ▼
┌────────────────────────────────────────────────────────────────────────────┐
│                        IESP REVIEW REQUIRED                               │
│  • DCRA (14.1)           • Cloud Pre-Impl (17.1)                         │
│  • NRA (14.2)            • Emerging Tech Pre-Impl (17.1)                 │
│  • Cloud Subsequent      • Digital Services (16.4)                       │
│    (17.2) if material    • BNM Directed (17.4/1.4)                      │
│    change                                                                 │
└────────────────────────────────────────────────────────────────────────────┘
                          OR
┌────────────────────────────────────────────────────────────────────────────┐
│                     NO IESP CURRENTLY REQUIRED                            │
│  • DCRA/NRA current and no material change                               │
│  • Cloud enhancement with no material alteration (17.3)                  │
│  • Digital services qualifying for simplified notification (16.3)        │
│  • Monitor for trigger events                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

## Engagement Types

### 1. Data Centre Resilience Assessment (DCRA)
| Attribute | Detail |
|-----------|--------|
| **Trigger Clause** | 14.1 |
| **Marker** | S (mandatory) |
| **Frequency** | Every 3 years or material change to DC infrastructure, whichever is earlier |
| **Scope** | Paragraphs 10.24 to 10.28 (DC resilience, redundancy, physical security, operations, segregation) |
| **Assessor** | Technically competent external service provider |
| **Board Requirement** | Designated board-level committee (per 8.3) must deliberate the outcome |
| **Third-Party DC** | May rely on independent third-party assurance reports if consistent with risk appetite and the assurance considers similar risks and meets DCRA requirements |
| **Reporting** | Appendix 7 Part A (Risk Assessment Report) |

### 2. Network Resilience Assessment (NRA)
| Attribute | Detail |
|-----------|--------|
| **Trigger Clause** | 14.2 |
| **Marker** | S (mandatory) |
| **Frequency** | Every 3 years or material change to network design, whichever is earlier |
| **Scope** | Paragraphs 10.36 to 10.43 (network design, resilience, monitoring, segmentation, logs) |
| **Assessor** | Technically competent external service provider |
| **Board Requirement** | Designated board-level committee (per 8.3) must deliberate the outcome |
| **Reporting** | Appendix 7 Part A (Risk Assessment Report) |

### 3. Cloud Services Pre-Implementation Review
| Attribute | Detail |
|-----------|--------|
| **Trigger Clause** | 17.1(c) |
| **Marker** | S (mandatory) |
| **Frequency** | First-time adoption of public cloud for critical systems |
| **Prerequisites** | (a) Comprehensive risk assessment per 10.50 and Appendix 10, format per App 7 Part A; (b) CISO/board confirmation per App 7 Part B; (c) Third-party pre-implementation review |
| **Scope** | Appendix 10 (Cloud Governance + Cloud Design & Control — 14 domains) |
| **Higher-Risk Services** | Must also cover Part C of Appendix 7 for services involving customer information processing/storage or cross-border data transmission |
| **BNM Consultation** | Required before adoption |
| **Reporting** | Appendix 7 Parts A, B, C, D |

### 4. Emerging Technology Pre-Implementation Review
| Attribute | Detail |
|-----------|--------|
| **Trigger Clause** | 17.1(c) |
| **Marker** | S (mandatory) |
| **Frequency** | First-time adoption of emerging technology (AI/ML/etc.) for critical systems |
| **Scope** | Appendix 9 (Guidance on Emerging Technologies) |
| **BNM Consultation** | Required before adoption |
| **Reporting** | Appendix 7 Parts A, B, C, D |

### 5. Digital Services Enhancement Assurance
| Attribute | Detail |
|-----------|--------|
| **Trigger Clause** | 16.4(a), 16.5 |
| **Marker** | S (mandatory) |
| **Frequency** | Prior to BNM notification for non-simplified digital service enhancements |
| **Scope** | Technology risks and security controls per Appendix 7 Part D |
| **Assessor Requirements** | Competent, good track record, comply with Part C and D of Appendix 7 (per 16.5) |
| **Reporting** | Appendix 7 Part A format |

### 6. Subsequent Cloud/Emerging Tech Notification
| Attribute | Detail |
|-----------|--------|
| **Trigger Clause** | 17.2 |
| **Marker** | S (mandatory) |
| **Prerequisites** | (a) 17.1 consultation completed with no BNM concerns; (b) Enhanced TRMF for cloud/emerging tech risks; (c) Independent assurance established on framework; (d) Sufficient incident response plans |
| **Exemption** | Not required for enhancements that do not materially alter prior assessments (17.3) |

### 7. BNM Discretionary Direction
| Attribute | Detail |
|-----------|--------|
| **Trigger Clause** | 17.4 and/or 1.4 |
| **Marker** | S (mandatory) |
| **Applicability** | May apply to non-critical systems; may be triggered when 17.1/17.2 prerequisites not met |
| **Under 1.4** | BNM may require independent external review when material technology risk management weaknesses are identified |
| **Response** | Comply promptly and to the satisfaction of BNM |

## Key Definitions

| Term | Definition |
|------|-----------|
| **Critical system** | Any application system supporting provision of critical banking, insurance, takaful, payment, investment or trading services, where failure could significantly impair the FI's services, business operations, financial position, reputation, or compliance |
| **Third party service provider** | Any internal group affiliate or external entity providing technology-related functions/services, including cloud computing software, platform and infrastructure service providers |
| **Material change** | Change that could significantly alter the risk profile of the assessed infrastructure |
| **Emerging technology** | New/evolving technologies (AI, ML, quantum computing, etc.) where industry standards and best practices may not yet be fully established |

## Appendix 7 Structure

The IESP reporting framework under Appendix 7 consists of:

| Part | Title | Purpose |
|------|-------|---------|
| **Part A** | Risk Assessment Report | 6-section report format: FI details, ESP details, application details, technology risk assessment, quality assurance, authorised signatory |
| **Part B** | Format of Confirmation | 9-point attestation signed by CISO/board chair/senior management confirming readiness |
| **Part C** | Requirements on External Party Assurance | 6 requirements the independent ESP must follow when conducting the review |
| **Part D** | Minimum Controls to be Assessed | Control domains the IESP must assess: access control, physical security, operations security, communication security, incident management, BCP, plus online transaction and mobile controls |

## Cross-References to RMIT Repo

This IESP repo is a subset of the [BNM RMIT Compliance Database](https://github.com/dawuds/RMIT). The following RMIT sections are directly relevant:

- **S13** — Technology Audits (audit function, competency, independence)
- **S14** — External Party Assurance (DCRA, NRA)
- **S16** — Notification for Technology-Related Applications (digital services)
- **S17** — Consultation and Notification for Cloud/Emerging Tech
- **Appendix 7** — Risk Assessment Report and Supervisory Expectations on External Party
- **Appendix 8** — IT and Cyber Risks Associated with Third Party Service Providers
- **Appendix 9** — Guidance on Emerging Technologies
- **Appendix 10** — Key Risks and Control Measures for Cloud Services
