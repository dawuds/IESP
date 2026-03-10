# AI and Emerging Technology — Scope Definition

> BNM RMiT Nov 2025 — Scope Guidance for Emerging Technology IESP Reviews

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 17.1 |
| **Scope Reference** | Appendix 9 (Emerging Technology Risk Assessment) |
| **Appendix 9 Areas** | Governance arrangements, risk assessment, acceptance criteria, controls, production prerequisites |

## 2. Scope Determination Factors

| Factor | How to Determine |
|--------|-----------------|
| **Technology inventory** | Obtain the FI's register of emerging technologies in use or under evaluation — AI/ML models, blockchain platforms, IoT deployments, RPA bots, etc. |
| **Use case classification** | Classify each technology use case by risk tier: (a) customer-facing decision-making (high risk), (b) internal decision support (medium risk), (c) operational automation (variable risk), (d) experimentation/sandbox (lower risk) |
| **System criticality** | Map the emerging technology to the systems it supports or replaces; if the system is critical per the FI's BIA, the technology is mandatory in scope |
| **Data sensitivity** | Identify what data the technology consumes, processes, and generates; restricted/confidential data use elevates scope priority |
| **Autonomy level** | Assess the level of autonomous decision-making: fully autonomous, human-on-the-loop, human-in-the-loop; higher autonomy = higher scope priority |
| **Deployment stage** | Pre-production (pilot/sandbox), limited production, or enterprise-wide production; production deployments are mandatory in scope |
| **Third-party dependency** | Identify third-party technology providers (AI model vendors, platform providers); assess whether the FI can independently evaluate the technology |
| **Regulatory sensitivity** | Determine whether the use case is in a regulated domain (credit decisioning, AML, customer suitability) that imposes additional requirements |

## 3. In-Scope Items

### 3.1 Mandatory In-Scope

| Item | Rationale |
|------|-----------|
| All AI/ML models deployed in production that support customer-facing decisions | High risk; direct impact on customers, regulatory scrutiny, fairness and bias obligations |
| All AI/ML models deployed in production for risk-sensitive functions (credit scoring, fraud detection, AML, market risk) | Regulatory sensitivity; errors could result in financial loss, compliance breaches |
| Emerging technology governance framework (Appendix 9 — governance arrangements) | Regulatory requirement; governance must be assessed regardless of specific technology |
| Technology risk assessment (Appendix 9 — risk assessment) | Regulatory requirement; risk assessment must exist for each emerging technology in production |
| Controls (Appendix 9 — controls) | Regulatory requirement; controls must be assessed for deployed technologies |
| Production prerequisites (Appendix 9) | Regulatory requirement for pre-deployment reviews; security testing, operational readiness |
| Third-party AI/ML providers (e.g., OpenAI, Google, cloud AI services) | Third-party risk; FI must demonstrate oversight and understanding of the technology |

### 3.2 Conditionally In-Scope

| Item | Condition for Inclusion |
|------|------------------------|
| AI/ML models for internal decision support (not customer-facing) | Include if model outputs materially influence business decisions (e.g., portfolio allocation, pricing recommendations) |
| RPA deployments | Include if RPA bots have access to critical systems or sensitive data, or if bot failures could cause operational disruption |
| Blockchain/DLT implementations | Include if used for transaction processing, settlement, or record-keeping in production |
| IoT deployments | Include if IoT devices are connected to the FI's network and could present a security entry point, or if they process sensitive data |
| Generative AI tools (e.g., ChatGPT, Copilot) | Include if used by staff for tasks involving customer data, financial analysis, or code generation for production systems |
| AI/ML models in advanced pilot/pre-production | Include if the pilot uses real customer data or if go-live is planned within the assessment period |
| Shadow AI (unsanctioned AI use by business units) | Assess the FI's shadow AI detection capability; specific shadow AI instances are flagged as findings rather than formally scoped |

### 3.3 Typically Out-of-Scope (with justification required)

| Item | Justification for Exclusion | Risk of Exclusion |
|------|---------------------------|-------------------|
| Pure research/experimentation with no production path and no real data | Not yet deployed; no customer or operational impact | Low, provided sandbox is truly isolated from production data and systems |
| Mature, broadly adopted technology that no longer qualifies as "emerging" (e.g., standard virtualisation, basic RPA) | No longer emerging; covered by standard RMIT controls | Minimal if covered by regular technology risk management |
| Vendor-proprietary AI models that the FI cannot access or assess (black-box models) | FI cannot perform technical assessment | High; the FI should demand transparency or consider alternative vendors. Flag as a finding |

## 4. Key Areas to Assess (Appendix 9 Mapping)

### 4.1 Governance Arrangements

| Assessment Area | Focus |
|----------------|-------|
| Board/committee oversight | Approval of emerging tech adoption, ongoing visibility |
| Governance framework | Emerging tech evaluation, approval, risk management, oversight lifecycle |
| Roles and responsibilities | Clear ownership across technology, risk, compliance, and business |
| Policies | Acceptable use policies, AI ethics policy (fairness, bias, transparency) |
| Technology radar | Mechanism for tracking and evaluating emerging technologies |
| Innovation governance | Sandbox/PoC approval process, graduation criteria to production |

### 4.2 Risk Assessment

| Assessment Area | Focus |
|----------------|-------|
| Technology-specific risk assessment | Operational, security, compliance, reputational, strategic risks |
| Model risk (AI/ML) | Bias, drift, explainability, adversarial robustness, training data quality |
| Third-party risk | Vendor viability, lock-in, data sharing, subcontracting |
| Data risk | Data quality, privacy, sovereignty, consent, lineage |
| Integration risk | Compatibility with existing systems, cascading failure potential |
| Concentration risk | Single-vendor dependency, single-model dependency |
| Obsolescence risk | Technology evolution, vendor support lifecycle |

### 4.3 Acceptance Criteria

| Assessment Area | Focus |
|----------------|-------|
| Go-live criteria | Specific, measurable criteria documented before deployment |
| Performance benchmarks | Accuracy, latency, throughput, error rates; tested and validated |
| Security baseline | Technology-specific security requirements met |
| Regulatory compliance | RMIT, PDPA, AML/CFT, consumer protection, Shariah (where applicable) |
| Ethical review (AI/ML) | Fairness testing, non-discrimination, transparency, accountability |
| Pilot/sandbox results | Formal analysis and acceptance based on pilot outcomes |

### 4.4 Controls

| Assessment Area | Focus |
|----------------|-------|
| Security controls | Technology-specific attack vectors (prompt injection, adversarial inputs, 51% attacks) |
| Access controls | Least privilege, MFA, separation of model development and production |
| Monitoring and logging | Real-time monitoring, performance tracking, audit logging |
| Model monitoring (AI/ML) | Accuracy drift, data drift, bias monitoring, retraining triggers |
| Human oversight | Human-in-the-loop for high-risk decisions, override capability |
| Kill switch | Ability to rapidly disable the technology |
| Change management | Model retraining governance, smart contract update process, version control |
| Data governance | Data quality controls, lineage tracking, consent management |

### 4.5 Production Prerequisites

| Assessment Area | Focus |
|----------------|-------|
| Security testing | Penetration testing, vulnerability assessment, adversarial testing |
| Resilience testing | Failover, degraded-mode operation, recovery |
| Integration testing | End-to-end with upstream/downstream systems |
| Operational readiness | Runbooks, support procedures, escalation paths, team training |
| Incident response | Technology-specific IR scenarios |
| BCP/DRP coverage | Continuity planning for the technology |
| Documentation | Architecture, configuration, dependencies, known limitations |
| Skills assessment | Sufficient internal expertise to operate and oversee the technology |

## 5. Interaction with Other Assurance

| Other Engagement | Interaction | Boundary |
|-----------------|-------------|----------|
| **Cloud Assessment** | AI/ML services deployed on cloud (SageMaker, Azure OpenAI, Vertex AI) | Cloud assessment covers cloud infrastructure controls; Emerging Tech covers AI-specific risks (model governance, bias, explainability). Both may assess IAM and monitoring |
| **Digital Services** | AI-powered digital services (chatbots, recommendation engines, automated underwriting) | Digital Services covers application-layer security (Appendix 7 Part D); Emerging Tech covers AI-specific risk dimensions |
| **NRA** | IoT devices connected to the network | NRA covers network resilience and security for IoT connectivity; Emerging Tech covers IoT device security, data handling, and governance |
| **DCRA** | Edge computing or on-premises AI infrastructure | DCRA covers physical infrastructure resilience; Emerging Tech covers the AI/emerging technology layer |
| **Internal Audit** | Model validation, AI ethics reviews | IESP engagement provides independent external assurance; should coordinate with (not duplicate) internal audit or model validation work |

## 6. Scoping Checklist for Emerging Technology Reviews

- [ ] Obtain the FI's emerging technology inventory/register
- [ ] Classify each technology by risk tier (customer-facing, internal, operational, experimental)
- [ ] Map technologies to system criticality (BIA)
- [ ] Identify data consumed, processed, and generated by each technology
- [ ] Assess autonomy level of each technology deployment
- [ ] Determine deployment stage (sandbox, pilot, limited production, enterprise-wide)
- [ ] Identify third-party technology providers and dependencies
- [ ] Determine regulatory sensitivity of use cases
- [ ] Review prior emerging technology assessments and findings
- [ ] Identify material changes since last assessment
- [ ] Agree scope boundaries with the FI
- [ ] Identify interaction with other ongoing/planned IESP engagements
- [ ] Confirm IESP team has relevant expertise for the specific technology
- [ ] Document scope in scoping memorandum and obtain FI sign-off

## 7. Cross-References

| Document | Path |
|----------|------|
| Emerging Tech Requirements | `/requirements/emerging-tech-review.md` |
| AI/Emerging Tech Evidence Checklist | `/evidence/evidence-checklist-ai.md` |
| AI/Emerging Tech AWP | `/audit-work-programs/awp-ai-emerging-tech.md` |
| Scoping Methodology | `/scope/scoping-methodology.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
