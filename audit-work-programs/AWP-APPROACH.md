# AWP Architecture and Approach

**Last updated:** 2026-03-31

## Principle: AWPs Are Anchored to Appendixes

Audit Work Programs (AWPs) are structured around the BNM RMiT Appendix that defines the controls to be assessed, not around engagement types or audit phases. This ensures the AWP scope directly mirrors the regulatory requirement.

### Logic Chain

```
BNM requires negative attestation (Appendix 7 Part C)
  -> IESP must perform a controls assessment to form that opinion
    -> Controls to assess are defined by the relevant Appendix
      -> Cloud: Appendix 10 (Part A + Part B)
      -> Emerging Tech: Appendix 9 (5 areas)
      -> All engagements: Appendix 7 Part D (minimum controls)
    -> The AWP walks through every control in that Appendix
      -> Each test step: objective, procedure, evidence, pass/fail
  -> Findings feed into Part A report and Part C attestation opinion
```

### Negative Attestation (Part C)

The IESP's deliverable is a negative assurance opinion under Appendix 7 Part C:

> "Nothing has come to our attention that causes us to believe the controls are not operating effectively..."

The AWP is the tool that generates sufficient appropriate evidence to support (or qualify) that opinion. Three opinion types:
- **Type A (Clean):** No material exceptions identified
- **Type B (With Exceptions):** Material exceptions identified but not pervasive
- **Type C (Adverse):** Pervasive control failures

### AWP Set

| # | AWP File | Anchored To | Used By |
|---|----------|------------|---------|
| 1 | `awp-cloud.md` | Appendix 10 (Part A: 7 governance areas, Part B: 14 design/control areas) | Cloud pre-impl (17.1) and cloud attestation |
| 2 | `awp-ai-emerging-tech.md` | Appendix 9 (5 assessment areas) | Emerging tech pre-impl (17.1) and emerging tech attestation |
| 3 | `awp-appendix-7-part-d.md` | Appendix 7 Part D items 1(a-f) + 2(a-e) | ALL engagements — universal baseline |
| 4 | `awp-dcra.md` | RMiT clauses 10.24–10.28 | DCRA engagements (14.1) |
| 5 | `awp-nra.md` | RMiT clauses 10.36–10.43 | NRA engagements (14.2) |
| 6 | `awp-digital-services.md` | RMiT 16.4/16.5 + Part D | Digital services pre-launch |

### Engagement Mode: Pre-Implementation vs. Attestation

The same AWP serves both engagement modes. Each test step includes guidance for both:

**Design Adequacy (Pre-Implementation — 17.1):**
- Assessing proposed/planned controls before go-live
- Evidence is primarily documentary: architecture designs, policies, vendor assessments, staging test results
- Question: "Is this control designed to meet the requirement?"

**Operating Effectiveness (Independent Attestation):**
- Assessing controls that are live and operational
- Evidence is observation, sampling, re-performance, system-generated logs
- Question: "Did this control operate effectively during the assessment period?"
- Requires defined sampling methodology and assessment period

### Evidence Hierarchy

When gathering evidence for the attestation, prefer higher-ranked evidence:

| Rank | Evidence Type | Description |
|------|-------------|-------------|
| 1 | Direct observation | IESP directly observes control in operation |
| 2 | Independent confirmation | Third-party evidence (SOC 2, CSP certifications) |
| 3 | System-generated | Logs, configurations without manual intervention |
| 4 | Re-performance | IESP re-performs control procedure |
| 5 | Documentary | Policies, procedures, meeting minutes |
| 6 | Inquiry | Verbal representations from FI personnel |

### AWP Test Step Format

Every test step must be prescriptive enough for a junior auditor to execute without senior interpretation:

```
| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
```

- **Ref:** Unique identifier (e.g., CLD-01, AI-03, PD-07)
- **Test Objective:** What you are trying to verify (one sentence)
- **Test Steps:** Numbered, specific actions the auditor performs
- **Expected Evidence:** What documents/artifacts/observations support the test
- **Pass/Fail Criteria:** Unambiguous criteria — what constitutes pass, what constitutes fail

### Engagement-to-AWP Mapping

| Engagement | Trigger | Mode | AWPs Required |
|-----------|---------|------|---------------|
| Cloud Pre-Implementation | 17.1 | Design adequacy | Appendix 10 AWP + Part D AWP |
| Cloud Independent Attestation | Appendix 7 | Operating effectiveness | Appendix 10 AWP + Part D AWP |
| Emerging Tech Pre-Implementation | 17.1 | Design adequacy | Appendix 9 AWP + Part D AWP |
| Emerging Tech Independent Attestation | Appendix 7 | Operating effectiveness | Appendix 9 AWP + Part D AWP |
| DCRA | 14.1 | Operating effectiveness | DCRA AWP + Part D AWP |
| NRA | 14.2 | Operating effectiveness | NRA AWP + Part D AWP |
| Digital Services Pre-Launch | 16.4/16.5 | Design adequacy | Digital Services AWP (Part D embedded) |
| BNM Directed | 17.4/1.4 | As directed | Scoped per BNM direction |
