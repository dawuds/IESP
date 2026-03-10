# Cloud Services — Scope Definition

> BNM RMiT Nov 2025 — Scope Guidance for Cloud IESP Assessments

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 17.1 |
| **Scope Clauses** | 10.50, 10.51, 10.52, Appendix 10 |
| **Appendix 10 Part A** | Cloud Governance (7 areas) |
| **Appendix 10 Part B** | Cloud Design and Control (14 areas) |

## 2. Scope Determination Factors

| Factor | How to Determine |
|--------|-----------------|
| **Cloud service inventory** | Obtain the FI's complete cloud service catalogue — all CSPs, service models (IaaS/PaaS/SaaS), deployment models (public/private/hybrid/multi-cloud), and the systems/data hosted on each |
| **System criticality** | Map cloud-hosted systems to the FI's BIA/criticality classification; all critical systems on cloud are mandatory in scope |
| **Data classification** | Identify data classification (public, internal, confidential, restricted) for data in each cloud service; restricted/confidential data services are mandatory in scope |
| **CSP concentration** | Identify CSP concentration — if a single CSP hosts the majority of critical workloads, the assessment must focus on that CSP's governance and controls |
| **Service model** | IaaS requires deeper infrastructure assessment; SaaS focuses more on governance, data protection, and vendor oversight |
| **Shared responsibility** | Map the shared responsibility model per CSP and service model to determine what the FI controls vs. what the CSP controls |
| **Geographic scope** | Identify cloud regions in use and data residency implications |
| **Third-party dependencies** | Identify managed service providers (MSPs) involved in cloud operations |

## 3. In-Scope Items

### 3.1 Mandatory In-Scope

| Item | Rationale |
|------|-----------|
| All CSPs hosting critical systems | Criticality-driven; failure could impact financial services continuity |
| All CSPs processing restricted or confidential data | Data-driven; regulatory and privacy obligations |
| Cloud governance framework (Appendix 10 Part A — all 7 areas) | Regulatory requirement; governance applies regardless of CSP or service model |
| Cloud design and controls for critical workloads (Appendix 10 Part B — all 14 areas) | Regulatory requirement; controls must be assessed for critical deployments |
| CSP contracts and SLAs | Required under Appendix 10 Part A (contract management, oversight) |
| Cloud IAM and access controls | Cross-cutting control; applicable to all cloud deployments |
| Cloud security monitoring (CSPM, SOC integration) | Cross-cutting control; applicable to all cloud deployments |
| Data residency and sovereignty compliance | Regulatory requirement; BNM approval may be needed for offshore data |
| Cloud DR and backup arrangements | Required to ensure resilience of cloud-hosted critical systems |
| Cloud exit strategy | Required under Appendix 10 Part B; must be assessed for each critical CSP |

### 3.2 Conditionally In-Scope

| Item | Condition for Inclusion |
|------|------------------------|
| Non-critical systems on cloud | Include if they process confidential data, or if their compromise could impact critical systems |
| Development/staging cloud environments | Include if they contain production data, or if the deployment pipeline (CI/CD) can push to production |
| SaaS applications (e.g., CRM, HR, collaboration tools) | Include if they process customer data, financial data, or restricted/confidential information |
| Cloud-based AI/ML services | Include if used for customer-facing decisions or risk-sensitive analytics; also covered under Emerging Tech review |
| Multi-cloud management platforms | Include if they have privileged access across multiple CSPs |
| Cloud marketplace/third-party solutions deployed in the FI's cloud | Include if they have access to production data or critical systems |

### 3.3 Typically Out-of-Scope (with justification required)

| Item | Justification for Exclusion | Risk of Exclusion |
|------|---------------------------|-------------------|
| CSP's internal infrastructure (below the abstraction layer) | Assessed through CSP certifications (SOC 2, ISO 27001) | Gap if CSP certifications are incomplete or outdated |
| Cloud services used only for non-sensitive, non-critical purposes (e.g., developer sandbox with no real data) | Low risk; no critical or sensitive data exposure | Minimal, provided the environment is truly isolated |
| Personal cloud accounts of staff | Out of IESP scope; should be addressed by the FI's acceptable use policy and shadow IT controls | Shadow IT risk, but not within IESP engagement scope |

## 4. Key Areas to Assess

### 4.1 By Appendix 10 Part A (Cloud Governance)

| Area | Key Assessment Focus |
|------|---------------------|
| **A1: Cloud Risk Management** | Cloud-specific risk assessment per CSP and service; risk appetite for cloud |
| **A2: Cloud Usage Policy** | Policy governing cloud adoption, approved CSPs, data classification rules for cloud |
| **A3: Due Diligence** | Pre-engagement due diligence on CSPs; periodic refresh |
| **A4: CSP Certifications** | Currency and coverage of SOC 2, ISO 27001, CSA STAR; FI's review of findings and CUECs |
| **A5: Contract Management** | Audit rights, data ownership, breach notification, data residency, exit provisions, BNM access |
| **A6: Oversight** | SLA monitoring, service reviews, incident tracking, security advisory monitoring |
| **A7: Skilled Personnel** | Cloud-certified staff, independent assessment capability, shared responsibility understanding |

### 4.2 By Appendix 10 Part B (Cloud Design and Control)

| Area | Key Assessment Focus |
|------|---------------------|
| **B1: Architecture** | Multi-AZ/region design, VPC/VNET segmentation, well-architected review |
| **B2: CI/CD and IaC** | Pipeline security gates, IaC scanning, drift detection, state file security |
| **B3: Virtualisation/Containerisation** | Image scanning, runtime security, orchestrator hardening, network policies |
| **B4: Change Management** | Cloud change process, enhanced controls for security-critical changes |
| **B5: Backup and Recovery** | Backup frequency, cross-region, encryption, restoration testing, monitoring |
| **B6: Interoperability and Portability** | Vendor lock-in assessment, data export capability, migration feasibility |
| **B7: Exit Strategy** | Documented exit plan, contractual support, tested data retrieval |
| **B8: Key Management** | Encryption at rest/transit, key ownership (CSP-managed, CMK, BYOK), rotation |
| **B9: Access Controls** | IAM architecture, MFA, least privilege, privileged access, service accounts |
| **B10: Cybersecurity Operations** | Cloud-native monitoring, CSPM, SOC integration |
| **B11: DDoS Protection** | L3/L4 and L7 protection, playbooks, testing |
| **B12: DLP** | Data exfiltration detection, storage exposure, public access controls |
| **B13: SOC** | Cloud event ingestion, cloud-specific detections, analyst skills |
| **B14: Cyber Response and Recovery** | Cloud IR procedures, shared responsibility in IR, cloud DR testing |

## 5. Interaction with Other Assurance

| Other Engagement | Interaction | Boundary |
|-----------------|-------------|----------|
| **DCRA** | If the FI's cloud runs from owned DC (private cloud) or co-located infrastructure | DCRA covers physical facility; Cloud assessment covers cloud platform and workload controls |
| **NRA** | Network connectivity to cloud (VPN, Direct Connect, ExpressRoute) | NRA covers network path resilience and security to the cloud edge; Cloud assessment covers cloud-side networking (VPC, security groups, NACLs) |
| **Emerging Tech** | AI/ML services deployed on cloud (e.g., AWS SageMaker, Azure OpenAI, GCP Vertex AI) | Cloud assessment covers cloud infrastructure controls; Emerging Tech review covers AI-specific risks (bias, explainability, model governance) |
| **Digital Services** | Digital services hosted on cloud (web/mobile banking on AWS/Azure/GCP) | Digital Services review covers application-layer security (Appendix 7 Part D); Cloud assessment covers cloud infrastructure underpinning the application |
| **CSP certifications** | SOC 2 Type II, ISO 27001, CSA STAR reports from CSPs | Cloud assessment may rely on CSP certifications for controls below the shared responsibility line, but must perform gap analysis against RMIT requirements |

## 6. Scoping Checklist for Cloud Assessments

- [ ] Obtain complete cloud service inventory (all CSPs, services, regions, data hosted)
- [ ] Map cloud-hosted systems to criticality classification
- [ ] Identify data classification for data in each cloud service
- [ ] Determine shared responsibility model per CSP and service model
- [ ] Obtain current CSP certifications/assurance reports
- [ ] Identify third-party MSPs involved in cloud operations
- [ ] Determine data residency requirements and current compliance
- [ ] Review prior cloud assessment scope and findings
- [ ] Identify material changes since last assessment
- [ ] Agree scope boundaries with the FI (in-scope, out-of-scope, reliance areas)
- [ ] Identify interaction with other ongoing/planned IESP engagements
- [ ] Document scope in scoping memorandum and obtain FI sign-off

## 7. Cross-References

| Document | Path |
|----------|------|
| Cloud Pre-Implementation Requirements | `/requirements/cloud-pre-implementation.md` |
| Cloud Evidence Checklist | `/evidence/evidence-checklist-cloud.md` |
| Cloud AWP | `/audit-work-programs/awp-cloud.md` |
| Scoping Methodology | `/scope/scoping-methodology.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
