# IESP Assessment Methodology

**Source:** BNM RMiT (BNM/RH/PD 028-98, 28 November 2025)
**Last updated:** 2026-03-31

---

## 1. What Is an IESP?

An Independent External Service Provider (IESP) is a third-party firm engaged by a financial institution (FI) to independently assess the FI's technology risk controls. BNM requires IESPs for specific assessments — the FI cannot self-certify.

The IESP's job: assess controls, form an opinion, and deliver a report. The opinion is a **negative attestation** — "nothing has come to our attention that causes us to believe the controls are not operating effectively."

---

## 2. The Regulatory Architecture

### 2.1 How BNM RMiT Is Structured

BNM RMiT is an 80-page policy document with two parts and 11 appendixes:

```
BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025)
│
├── Part A: Overview (Sections 1-7)
│   Applicability, legal basis, interpretation
│
├── Part B: Policy Requirements (Sections 8-18)
│   The "what FIs must do" — 11 sections covering governance,
│   risk management, operations, cybersecurity, digital services,
│   audit, external assurance, notifications, and cloud/emerging tech
│
└── Appendixes (1-11)
    The "how" — control measures, assessment guidance, report formats
```

### 2.2 Where IESP Requirements Live

IESP requirements are spread across four places in the document:

| Location | What It Says | Effect |
|----------|-------------|--------|
| **Section 14** (para 14.1, 14.2) | FI must engage IESP for DC resilience (DCRA) and network resilience (NRA) every 3 years or upon material change | Mandatory IESP trigger |
| **Section 16** (para 16.4, 16.5) | FI must have IESP assessment before launching new/enhanced digital services | Mandatory IESP trigger |
| **Section 17** (para 17.1-17.5) | FI must consult BNM before first-time cloud or emerging tech for critical systems — includes IESP pre-implementation review | Mandatory IESP trigger |
| **Section 1** (para 1.4) | BNM can direct an IESP review at any time for any reason | Discretionary IESP trigger |

### 2.3 What the IESP Actually Assesses

The IESP does NOT assess "compliance with RMiT" generically. The IESP assesses **specific controls** defined by specific sources:

| If the engagement is... | Controls come from... | BNM RMiT source |
|------------------------|----------------------|-----------------|
| Cloud (pre-impl or attestation) | 7 governance areas + 14 design/control areas | **Appendix 10** (Part A + Part B) |
| Emerging tech (pre-impl or attestation) | 2 items with sub-points | **Appendix 9** |
| DCRA | DC resilience controls | **Clauses 10.24–10.28** |
| NRA | Network resilience controls | **Clauses 10.36–10.43** |
| Digital services | Digital service security | **Clauses 16.4/16.5 + Appendix 3** |
| ALL engagements | Minimum controls baseline | **Appendix 7 Part D** |

**Appendix 7 is NOT a control source** (except Part D). It defines:
- Part A — how to format the report
- Part B — what the FI's CISO/board must attest to
- Part C — what the IESP must comply with
- Part D — minimum controls (the only part that defines what to test)

### 2.4 The Appendixes — What Each One Does

| Appendix | Title | Pages | Role for IESP |
|----------|-------|-------|--------------|
| 1 | Removable media controls | 1 | Not directly relevant |
| 2 | Self-service terminal controls | 3 | Not directly relevant |
| 3 | Digital services controls | 4 | Referenced by digital services IESP scope |
| 4 | Mobile app controls | 1 | Referenced by Part D item 2(e) |
| 5 | Cybersecurity controls | 5 | Referenced by cloud DLP and SOC areas |
| 6 | Simplified notification criteria | 1 | Determines when IESP is NOT needed |
| **7** | **IESP framework** | **6** | **Core: report format (A), FI attestation (B), IESP requirements (C), minimum controls (D)** |
| **8** | **Third-party service provider risks** | **1** | **Risk taxonomy for third-party engagements (DCRA, cloud)** |
| **9** | **Emerging technology guidance** | **1** | **Control source for emerging tech IESP** |
| **10** | **Cloud controls** | **15** | **Control source for cloud IESP (largest appendix)** |
| 11 | Fraud detection standards | 3 | Not directly relevant |

---

## 3. The Five IESP Engagement Types

### 3.1 Decision: Which Engagement Am I Doing?

```
Has the FI been directed by BNM?
  └── Yes → BNM Directed (1.4 / 17.4) — scope per BNM direction
  └── No ↓

What is the FI doing?
  ├── Adopting cloud for critical systems (first time)?
  │   └── Cloud Pre-Implementation (17.1) → Appendix 10 + Part D
  ├── Adopting emerging tech for critical systems (first time)?
  │   └── Emerging Tech Pre-Implementation (17.1) → Appendix 9 + Part D
  ├── Cloud/emerging tech already live, needs periodic attestation?
  │   └── Independent Attestation → Appendix 10 or 9 + Part D
  ├── Launching new/enhanced digital services?
  │   └── Digital Services (16.4/16.5) → Part D + Appendix 3
  ├── DC resilience due (3yr cycle or material change)?
  │   └── DCRA (14.1) → Clauses 10.24-10.28 + Part D
  └── Network resilience due (3yr cycle or material change)?
      └── NRA (14.2) → Clauses 10.36-10.43 + Part D
```

### 3.2 Engagement Summary

| # | Engagement | Trigger | Frequency | Control Source | Report Includes |
|---|-----------|---------|-----------|---------------|----------------|
| 1 | Cloud Pre-Implementation | 17.1 | First-time cloud for critical systems | Appendix 10 + Part D | Part A + Part B + Part C |
| 2 | Emerging Tech Pre-Implementation | 17.1 | First-time emerging tech for critical systems | Appendix 9 + Part D | Part A + Part B + Part C |
| 3 | Cloud Independent Attestation | Appendix 7 | Periodic / material change | Appendix 10 + Part D | Part A + Part C |
| 4 | Emerging Tech Independent Attestation | Appendix 7 | Periodic / material change | Appendix 9 + Part D | Part A + Part C |
| 5 | DCRA | 14.1 | Every 3 years / material DC change | Clauses 10.24-10.28 + Part D | Part A + Part C |
| 6 | NRA | 14.2 | Every 3 years / material network change | Clauses 10.36-10.43 + Part D | Part A + Part C |
| 7 | Digital Services | 16.4/16.5 | Before launch/enhancement | Part D + Appendix 3 | Part A |
| 8 | BNM Directed | 17.4 / 1.4 | As directed | Per BNM direction | Per BNM direction |

### 3.3 Overlap: Cloud + Emerging Tech

When a cloud deployment involves emerging technology (e.g., AI/ML workloads on cloud, cloud-native AI services like AWS Bedrock or Azure OpenAI):
- **Appendix 10** governs the cloud infrastructure controls
- **Appendix 9** governs the emerging technology controls
- Both must be assessed — use both AWP workbooks
- Part D applies once (not duplicated)

---

## 4. Two Engagement Modes

Every engagement operates in one of two modes. The same controls are assessed, but the **question you're asking** and the **evidence you need** differ:

### 4.1 Design Adequacy (Pre-Implementation)

**When:** 17.1 engagements (first-time cloud or emerging tech), digital services pre-launch

**Question:** "Is this control designed to meet the requirement?"

**Evidence type:** Primarily documentary — architecture designs, policies, vendor assessments, configuration plans, staging/UAT test results

**What you're looking for:** The FI has thought through the control, designed it appropriately, and plans to implement it before go-live. You're assessing intent and design, not operational evidence.

**Output:** The report informs the Part B confirmation — can the CISO/board attest that controls are adequate?

### 4.2 Operating Effectiveness (Independent Attestation)

**When:** Periodic cloud/emerging tech attestation, DCRA, NRA

**Question:** "Did this control operate effectively during the assessment period?"

**Evidence type:** Direct observation, sampling, re-performance, system-generated logs, configurations

**What you're looking for:** The control was actually in operation, not just documented. You sample transactions, review logs, observe processes, and verify configurations.

**Output:** The Part C negative attestation — can the IESP attest that controls are operating effectively?

---

## 5. The Assessment Process

### Phase 1: Engagement Setup

1. **Confirm the trigger** — which paragraph mandates this engagement?
2. **Determine the engagement type** — cloud, emerging tech, DCRA, NRA, digital services?
3. **Determine the mode** — design adequacy or operating effectiveness?
4. **Identify the control source** — which appendix/clauses define the scope?
5. **Confirm IESP compliance with Part C** — independence, understanding of architecture, competence
6. **Issue engagement letter** — scope, timeline, deliverables, team

### Phase 2: Scoping

1. **Identify platforms in scope** — which CSPs, which data centres, which network segments?
2. **Identify critical systems in scope** — which applications, workloads, services?
3. **Determine assessment levels:**
   - **ORG** — organisation-level controls assessed once (governance, policies, frameworks)
   - **PLATFORM** — platform-level controls assessed per CSP/DC/network segment
   - **WORKLOAD** — system-level controls assessed per critical system (sample-based)
4. **Define sampling approach** — sample sizes, assessment period, evidence coverage
5. **Issue Document Request List (DRL)**
6. **Determine if higher-risk services apply** — customer data processing, cross-border transmission

### Phase 3: Controls Assessment

Use the AWP workbook for the relevant engagement type. Each workbook contains:
- Pre-populated test steps anchored to the control source (appendix/clauses)
- Assessment level tags (ORG/PLATFORM/WORKLOAD) telling you what to repeat
- Context rows explaining why each control matters
- Part D minimum controls (embedded in every workbook)

For each test step:
1. Perform the assessment procedures as documented
2. Gather evidence — prefer higher-ranked evidence (observation > system-generated > documentary > inquiry)
3. Document procedures performed, evidence obtained, and evidence reference
4. Record observations/findings
5. Assign conclusion: **Compliant / Partially Compliant / Non-Compliant / N/A**
6. Document recommendations for non-compliant/partially compliant findings

### Phase 4: Opinion Formation

1. **Aggregate findings** across all assessment sheets
2. **Review the Scoring Dashboard** — compliance percentages, level breakdown
3. **Determine the Part C opinion type:**

| Opinion | When | Effect |
|---------|------|--------|
| **Type A (Clean)** | No material exceptions | IESP attests controls are operating effectively |
| **Type B (With Exceptions)** | Material exceptions exist but are not pervasive | IESP attests with listed exceptions |
| **Type C (Adverse)** | Pervasive control failures | IESP cannot attest controls are effective |

4. **Complete the Part C Self-Assessment** — confirm IESP compliance with the 6 Part C requirements

### Phase 5: Reporting

1. **Draft the report** in Appendix 7 Part A format (6 sections):
   - Section 1: Financial Institution Details
   - Section 2: External Service Provider (IESP) Details
   - Section 3: Scope Details (systems, platforms, period, mode)
   - Section 4: Technology Risk Assessment Findings (detailed findings with condition/criteria/cause/effect/recommendation)
   - Section 5: Quality Assurance (methodology, peer review, limitations)
   - Section 6: Authorised Signatory
2. **Include the Part C attestation statement** (Type A, B, or C)
3. **Include Part D summary** — minimum controls assessment matrix
4. **Conduct findings walkthrough** with FI management
5. **Incorporate management responses** and agreed action plans
6. **Peer review** (Part C requirement 6)
7. **Issue final signed report**

### Phase 6: Post-Report (Pre-Implementation Only)

For 17.1 engagements:
1. The FI remediates critical/high findings
2. The CISO/board reviews findings and signs **Part B confirmation** (9-point attestation)
3. The FI submits the consultation package to BNM:
   - Part A report (IESP's report)
   - Part B confirmation (FI's attestation)
   - Supporting documentation
4. BNM reviews and may approve, request more information, or direct additional assessment

---

## 6. Evidence Hierarchy

When multiple evidence types are available, prefer higher-ranked evidence:

| Rank | Type | Description | Example |
|------|------|-------------|---------|
| 1 | Direct observation | IESP directly observes control in operation | Watching a DR failover test |
| 2 | Independent confirmation | Third-party evidence | SOC 2 Type II report, ISO 27001 certificate |
| 3 | System-generated | Logs and configurations without manual intervention | CloudTrail logs, firewall rule exports |
| 4 | Re-performance | IESP re-performs the control procedure | Re-running an access review |
| 5 | Documentary | Policies, procedures, meeting minutes | Board-approved cloud strategy document |
| 6 | Inquiry | Verbal representations from FI personnel | Interview with CISO on risk appetite |

**Rule of thumb:** For operating effectiveness engagements, you need Rank 1-4 evidence for critical controls. Documentary evidence (Rank 5) alone is insufficient to conclude a control is operating effectively — it only proves the control is designed. Inquiry (Rank 6) alone should never be the sole basis for a conclusion.

---

## 7. Sampling Methodology

### Approach
Judgmental (not statistical) — appropriate for limited assurance engagements.

### Sample Sizes

| Population | Standard Risk | High Risk | Rationale |
|-----------|--------------|-----------|-----------|
| 1-5 | All | All | Full coverage feasible |
| 6-15 | 3 | 5 | ~25-40% coverage |
| 16-50 | 5 | 8 | Sufficient for pattern detection |
| 51-100 | 8 | 12 | Diminishing returns beyond this |
| 100+ | 10 | 15 | Cap with stratification |

### Time-Based Evidence

| Evidence Type | Coverage Period | Rationale |
|-------------|----------------|-----------|
| Board/committee reports | Last 4 quarters | Full annual governance cycle |
| Operational records (incidents, changes, patches) | Last 3-6 months | Recent operating effectiveness |
| Annual processes (risk assessment, DR test, pen test) | Last 12 months | Full cycle |
| Continuous monitoring (SOC, logs, alerts) | Last 30 days | Current state verification |
| Policies and frameworks | Current version + prior | Change tracking |

---

## 8. Conclusion Scale

| Conclusion | Definition | Action |
|-----------|-----------|--------|
| **Compliant** | Control fully implemented and operating effectively. Evidence supports regulatory criteria are met. | No finding raised |
| **Partially Compliant** | Implemented but with gaps in scope, coverage, documentation, or effectiveness. Some criteria met. | Finding raised (Medium/Low) |
| **Non-Compliant** | Absent, fundamentally deficient, or not operating. Regulatory criteria not met. | Finding raised (High/Critical) |
| **N/A** | Not applicable to entity's operations. Justification documented. | Document rationale |

---

## 9. Appendix 7 — The IESP Framework

### Part A: Report Format (p.56-57)

The mandatory output template. 6 sections:

| Section | Content |
|---------|---------|
| 1 | Financial Institution details (name, license, address, contact) |
| 2 | External Service Provider details (firm, lead assessor, qualifications, contact, engagement period) |
| 3 | Detail of application (overview, technology description) |
| 4 | Technology risk assessment (findings — must reference Part D and para 17.1 for cloud/emerging tech) |
| 5 | Quality assurance (overall recommendation) |
| 6 | Authorised signatory (name, designation, date) |

### Part B: Format of Confirmation (p.58)

Signed by the FI's CISO / board committee chair / designated senior management officer. 9-point attestation confirming:

1. Consistent with strategic and business plans
2. Board/senior management understand and accept RMiT responsibilities
3. Risk management process subject to board oversight
4. Appropriate security measures in place
5. Customer support services in place
6. Performance monitoring established
7. Included in contingency and business resumption plans
8. Adequate resources to support
9. Systems, procedures, and security measures will be reviewed to keep current

**The IESP does not sign Part B.** The IESP's findings inform whether the FI can sign it.

### Part C: Requirements on External Party Assurance (p.59)

6 requirements the IESP must comply with:

1. Assurance by an **independent** ESP engaged by the FI
2. ESP must **understand** the proposed services, data flows, system architecture, connectivity, and dependencies
3. ESP shall **review comprehensiveness** of the risk assessment and **validate adequacy** of controls
4. Report (per Part D) shall state **scope, methodology, findings, and remedial actions**
5. Report shall confirm **no exception noted** based on prescribed risk areas (negative attestation)
6. FI shall provide the report **accompanied by relevant documents**

### Part D: Minimum Controls (p.59-61)

The only part of Appendix 7 that defines controls. Two items:

**Item 1 — Security Requirements (6 areas):**
- (a) Access control
- (b) Physical and environmental security
- (c) Operations security
- (d) Communication security
- (e) Information security incident management
- (f) Information security aspects of business continuity management

**Item 2 — Online Transactions and Services (5 areas, where applicable):**
- (a) Customer identity authentication (5 sub-items)
- (b) Transaction authentication (4 sub-items)
- (c) Segregation of duties (4 sub-items)
- (d) Data integrity (8 sub-items)
- (e) Mobile device risks (11 sub-items)

Part D applies to **every** IESP engagement as a minimum baseline.

---

## 10. Cross-References

| Resource | Location |
|----------|----------|
| Source document | `source/pd-rmit-nov25.pdf` |
| Engagement types (structured JSON) | `engagements.json` |
| Decision tree | `decision-tree/decision-tree.json` |
| Control domains | `controls/control-domains.json` |
| Evidence checklists | `evidence/` |
| Requirements breakdowns | `requirements/` |
| AWP workbooks (Excel) | Tech-Audit/IESP/ (private repo) |
| Report template (Word) | Tech-Audit/IESP/ (private repo) |
