# Emerging Technology Review — Detailed Requirements

> BNM RMiT Nov 2025 — Practitioner Guide for IESP Teams Performing Emerging Technology Reviews

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 17.1 |
| **Marker** | S (mandatory) |
| **Scope Reference** | Appendix 9 (Emerging Technology Risk Assessment) |
| **Appendix 9 Areas** | Governance arrangements, risk assessment, acceptance criteria, controls, production prerequisites |
| **Reporting** | Appendix 7 Part A (Risk Assessment Report) |
| **ESP Standards** | Appendix 7 Part C (Requirements on External Party Assurance) |
| **Board Governance** | 8.3 (designated board-level committee must deliberate outcome) |

## 2. What Constitutes "Emerging Technology"?

Emerging technology, in the context of RMIT, refers to technology that is relatively new, rapidly evolving, and not yet broadly adopted across the Malaysian financial services sector, or technology that introduces novel risk characteristics not addressed by existing risk management frameworks. Examples include but are not limited to:

| Technology | Examples |
|-----------|----------|
| **Artificial Intelligence / Machine Learning** | Large language models (LLMs), generative AI, predictive analytics, AI-driven decision-making, robotic process automation (RPA) with cognitive capabilities |
| **Distributed Ledger Technology** | Blockchain, tokenisation platforms, smart contracts, decentralised finance (DeFi) interfaces |
| **Quantum Computing** | Quantum-resistant cryptography readiness, quantum computing applications |
| **Internet of Things (IoT)** | Connected devices in branches, smart ATMs, wearable payment devices |
| **Advanced Analytics** | Real-time data streaming, alternative data usage for credit scoring, graph analytics |
| **Immersive Technologies** | Virtual reality (VR), augmented reality (AR) for customer engagement |
| **Autonomous Systems** | Algorithmic trading, automated underwriting, self-service automation |

The FI's board or designated committee should maintain a technology radar or equivalent mechanism to identify and classify emerging technologies relevant to the institution.

## 3. Trigger Conditions

An Emerging Technology Review under 17.1 is required when **any** of the following conditions are met:

1. **First-time adoption:** The FI is deploying an emerging technology for the first time in a production environment serving customers or supporting critical business processes.
2. **Material expansion:** The FI is significantly expanding the use of a previously adopted emerging technology (e.g., from pilot to enterprise-wide deployment, or from non-critical to critical system use).
3. **Material change in risk profile:** Changes to the technology that materially alter its risk characteristics (e.g., moving from rule-based automation to AI-driven autonomous decision-making).
4. **Periodic review cycle:** At least every 3 years for technologies that remain in production use (or more frequently if the technology is evolving rapidly).
5. **BNM direction:** BNM may direct a review at any time under clause 1.4 or 17.4.

## 4. Scope — What the Review Must Cover (Appendix 9)

### 4.1 Governance Arrangements

| Assessment Area | Key Questions |
|----------------|--------------|
| **Board oversight** | Has the board or designated committee approved the adoption of this emerging technology? Is there ongoing board-level visibility into its risks and performance? |
| **Governance framework** | Does the FI have a governance framework specific to emerging technology that covers evaluation, approval, risk management, and ongoing oversight? |
| **Roles and responsibilities** | Are roles clearly defined for the technology lifecycle — from evaluation through deployment, monitoring, and retirement? |
| **Policies and standards** | Are there policies governing the acceptable use of this technology? Do they address ethical considerations, bias, transparency, and fairness (particularly for AI/ML)? |
| **Technology radar** | Does the FI maintain a technology radar or equivalent to track emerging technologies and assess their maturity and applicability? |
| **Innovation governance** | Is there a structured process for evaluating and approving technology innovation initiatives (sandbox/proof-of-concept governance)? |

### 4.2 Risk Assessment

| Assessment Area | Key Questions |
|----------------|--------------|
| **Technology risk assessment** | Has a comprehensive risk assessment been performed specific to this technology? Does it cover operational, security, compliance, reputational, and strategic risks? |
| **Third-party risk** | If the technology involves third-party providers (e.g., AI model providers, blockchain platforms), have third-party risks been assessed? |
| **Data risk** | What data does the technology consume, process, or generate? Are there data quality, privacy, or sovereignty risks? |
| **Model risk** (for AI/ML) | Has model risk been assessed? Are there risks of bias, drift, explainability gaps, or adversarial manipulation? |
| **Integration risk** | What are the risks of integrating the emerging technology with existing systems and processes? |
| **Concentration risk** | Is there dependence on a single provider, single model, or single technology that creates concentration risk? |
| **Obsolescence risk** | Given the technology's rapid evolution, has the FI assessed the risk that the technology becomes obsolete or unsupported? |

### 4.3 Acceptance Criteria

| Assessment Area | Key Questions |
|----------------|--------------|
| **Go-live criteria** | Has the FI defined specific, measurable acceptance criteria that must be met before the technology is deployed to production? |
| **Performance thresholds** | Are performance benchmarks defined (accuracy, latency, throughput, error rates)? |
| **Security baseline** | Is a security baseline defined for the technology, and has compliance been verified? |
| **Regulatory compliance** | Has the FI confirmed that the technology deployment complies with all applicable regulations (RMIT, PDPA, AML/CFT, Shariah requirements where applicable)? |
| **Ethical standards** (for AI/ML) | Has the FI assessed the technology against ethical standards (fairness, non-discrimination, transparency, accountability)? |
| **User acceptance** | Has user acceptance testing been performed with representative users and scenarios? |
| **Pilot/sandbox results** | If a pilot or sandbox was conducted, have results been analysed and acceptance criteria validated? |

### 4.4 Controls

| Assessment Area | Key Questions |
|----------------|--------------|
| **Security controls** | Are security controls appropriate for the technology's risk profile? Do they address unique attack vectors (e.g., prompt injection for LLMs, 51% attacks for blockchain, adversarial inputs for AI models)? |
| **Access controls** | Is access to the technology, its data, and its configuration managed with least privilege and MFA? |
| **Monitoring and logging** | Is the technology monitored in real time? Are activities logged for audit and investigation? |
| **Model monitoring** (for AI/ML) | Is model performance monitored for accuracy drift, data drift, and bias? Are alerts defined for performance degradation? |
| **Human oversight** | Is there appropriate human-in-the-loop or human-on-the-loop oversight, particularly for autonomous decision-making? |
| **Kill switch / override** | Can the technology be rapidly disabled or overridden if it malfunctions or produces harmful outputs? |
| **Change management** | Is there a change management process for updates to the technology (model retraining, smart contract updates, firmware updates for IoT)? |
| **Data controls** | Are data quality, data lineage, and data governance controls in place for data consumed and produced by the technology? |

### 4.5 Production Prerequisites

| Assessment Area | Key Questions |
|----------------|--------------|
| **Security testing** | Has the technology undergone comprehensive security testing (penetration testing, vulnerability assessment, adversarial testing where applicable)? |
| **Resilience testing** | Has the technology been tested for resilience (failover, recovery, degraded-mode operation)? |
| **Integration testing** | Has end-to-end integration testing been performed with upstream and downstream systems? |
| **Operational readiness** | Are operational runbooks, support procedures, and escalation paths defined? Is the operations team trained? |
| **Incident response** | Do incident response procedures cover scenarios specific to this technology? |
| **Business continuity** | Is the technology covered by the FI's BCP/DRP? Has BC/DR been tested for this technology? |
| **Documentation** | Is technical documentation complete and current (architecture, configuration, dependencies, known limitations)? |
| **Skills** | Does the FI have sufficient skilled personnel to operate, monitor, and maintain the technology in production? |

## 5. Frequency and Triggers

| Aspect | Requirement |
|--------|-------------|
| **Pre-deployment** | Before first production deployment of the emerging technology |
| **Periodic** | At least every 3 years for technologies in production, or more frequently for rapidly evolving technologies |
| **Material change** | Upon material changes to the technology, its use case, or its risk profile |
| **BNM direction** | As directed by BNM |
| **Recommended practice** | Annual light-touch review for AI/ML models in production (model performance and risk review), with full IESP review every 3 years |

## 6. Reporting Requirements

The Emerging Technology Review report must follow the Appendix 7 Part A format:

### Section 1 — Financial Institution Details
- Full legal name, BNM license type and number, primary contact person

### Section 2 — External Service Provider Details
- IESP firm name, lead assessor name and qualifications, team composition, independence declaration
- Note: Assessors should have relevant expertise in the specific emerging technology under review

### Section 3 — Scope Details (adapted for Emerging Technology)
- Technology description and classification
- Use case(s) and business context
- Deployment scope (pilot, limited, enterprise-wide)
- Data processed by the technology (classification, volume, sources)
- Third-party providers involved
- Scope inclusions and exclusions
- Assessment period

### Section 4 — Technology Risk Assessment
- Assessment methodology (adapted for emerging technology risk)
- Detailed findings organized by Appendix 9 areas (governance, risk assessment, acceptance criteria, controls, production prerequisites)
- For each finding:
  - Description of the issue
  - RMIT clause/appendix reference
  - Risk rating (High/Medium/Low)
  - Evidence supporting the finding
  - Recommendation for remediation
  - Production readiness implication (must-fix before go-live vs. acceptable post-go-live)
- Overall technology risk assessment opinion
- Readiness opinion (for pre-deployment reviews)

### Section 5 — Quality Assurance
- Methodology description, peer review process, scope limitations
- Technology-specific expertise of the assessment team

### Section 6 — Authorised Signatory
- Lead assessor signature, date, qualifications, firm stamp

## 7. Key Activities Checklist

### Phase 1 — Planning and Scoping
- [ ] Confirm review trigger (first-time adoption, material change, periodic, or BNM direction)
- [ ] Understand the emerging technology: what it is, how it works, what it does
- [ ] Understand the use case and business context
- [ ] Identify the data consumed, processed, and generated by the technology
- [ ] Identify third-party providers and dependencies
- [ ] Request governance documentation (policies, risk assessments, board approvals)
- [ ] Request technical documentation (architecture, design, configuration)
- [ ] Confirm IESP team has relevant emerging technology expertise
- [ ] Issue engagement letter

### Phase 2 — Governance Review (Appendix 9)
- [ ] Review board/committee approval for the technology adoption
- [ ] Review emerging technology governance framework
- [ ] Review roles and responsibilities
- [ ] Review acceptable use policies (including AI ethics policies where applicable)
- [ ] Review technology radar or equivalent
- [ ] Review innovation governance process (sandbox, PoC governance)

### Phase 3 — Risk Assessment Review
- [ ] Review the FI's risk assessment for the technology
- [ ] Assess coverage of key risk domains (operational, security, compliance, reputational, strategic)
- [ ] Review third-party risk assessment (if applicable)
- [ ] Review data risk assessment
- [ ] Review model risk assessment (for AI/ML)
- [ ] Assess integration risks
- [ ] Assess concentration and obsolescence risks

### Phase 4 — Acceptance Criteria and Controls Review
- [ ] Review go-live acceptance criteria
- [ ] Review performance benchmarks and security baselines
- [ ] Review regulatory compliance verification
- [ ] Review ethical assessment (for AI/ML)
- [ ] Review security controls (including technology-specific controls)
- [ ] Review access controls
- [ ] Review monitoring and logging
- [ ] Review human oversight arrangements
- [ ] Review kill switch / override capability
- [ ] Review change management procedures
- [ ] Review data governance controls

### Phase 5 — Production Readiness Review
- [ ] Review security testing results
- [ ] Review resilience and integration testing
- [ ] Review operational readiness (runbooks, training, support)
- [ ] Review incident response procedures (technology-specific scenarios)
- [ ] Review BCP/DRP coverage
- [ ] Review documentation completeness
- [ ] Assess skills adequacy

### Phase 6 — Reporting
- [ ] Draft findings with risk ratings and readiness implications
- [ ] Identify must-fix-before-go-live findings
- [ ] Conduct findings walkthrough with FI management
- [ ] Finalize report in Appendix 7 Part A format
- [ ] Issue readiness opinion (for pre-deployment reviews)

## 8. AI/ML-Specific Considerations

Given the prevalence of AI/ML adoption, the following additional considerations apply specifically to AI/ML reviews:

| Area | Specific Considerations |
|------|------------------------|
| **Model governance** | Model inventory, model ownership, model validation (independent of developers), model approval process |
| **Data governance** | Training data quality, representativeness, bias in training data, data lineage, consent for data use |
| **Explainability** | Can the model's decisions be explained to customers, regulators, and internal stakeholders? Is explainability proportionate to the risk of the use case? |
| **Bias and fairness** | Has the model been tested for bias across protected characteristics? Are fairness metrics defined and monitored? |
| **Model drift** | Is model performance monitored for accuracy drift and data drift? Are retraining triggers defined? |
| **Adversarial robustness** | Has the model been tested against adversarial inputs? For LLMs: prompt injection, jailbreaking, data exfiltration |
| **Transparency** | Are customers informed when they are interacting with AI? Are AI-generated outputs clearly labelled? |
| **Human override** | Can AI decisions be overridden by humans? Is there an appeal/review process for customers affected by AI decisions? |
| **Intellectual property** | Are there IP risks from using third-party AI models (e.g., training data IP, generated content IP)? |
| **Regulatory compliance** | Does the AI use case comply with BNM guidelines on AI, PDPA, consumer protection, and anti-discrimination requirements? |

## 9. Common Findings and Red Flags

| Finding Category | Common Issues |
|-----------------|---------------|
| **Governance** | No board awareness or approval, no emerging technology policy, technology adopted without formal evaluation process |
| **Risk Assessment** | Risk assessment is generic (not technology-specific), AI model risk not assessed, third-party AI provider risks not evaluated |
| **Acceptance Criteria** | No defined acceptance criteria, "move fast and fix later" culture, pilot deployed to production without formal go-live approval |
| **Controls** | No kill switch, no human oversight for autonomous decisions, AI model not monitored for drift, no adversarial testing |
| **AI-Specific** | Model bias not tested, decisions not explainable, customers not informed of AI interaction, training data quality not validated |
| **Skills** | FI lacks internal expertise to assess AI model quality, complete reliance on vendor for model management |
| **Documentation** | Architecture undocumented, model design and limitations not documented, operational runbooks not created |
| **Testing** | Security testing does not cover technology-specific attack vectors, no adversarial testing for AI models |

## 10. Cross-References

| Document | Path |
|----------|------|
| Regulatory Requirements (all clauses) | `/requirements/regulatory-requirements.md` |
| AI/Emerging Tech Evidence Checklist | `/evidence/evidence-checklist-ai.md` |
| AI/Emerging Tech AWP | `/audit-work-programs/awp-ai-emerging-tech.md` |
| AI/Emerging Tech Scope | `/scope/ai-emerging-tech.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
