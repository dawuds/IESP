# Cloud Pre-Implementation Review — Detailed Requirements

> BNM RMiT Nov 2025 — Practitioner Guide for IESP Teams Performing Cloud Pre-Implementation Reviews

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 17.1 |
| **Marker** | S (mandatory) |
| **Scope References** | 10.50 (Cloud Risk Assessment), 10.51 (Cloud Security Controls), 10.52 (Cloud Governance), Appendix 10 |
| **Reporting** | Appendix 7 Parts A, B, C, D |
| **Board Governance** | Part B confirmation by CISO/board chair/senior management |
| **Applicability** | First-time adoption of public cloud for critical systems |

## 2. Trigger Conditions

A cloud pre-implementation review under 17.1 is required when:

1. **First-time adoption of public cloud for critical systems:** The FI has not previously deployed critical systems on public cloud infrastructure and intends to do so.
2. **First-time use of a new cloud deployment model for critical systems:** The FI is adopting a materially different cloud model (e.g., moving from IaaS to PaaS, or from private cloud to public cloud for critical workloads).
3. **BNM direction:** BNM may require a pre-implementation review under 17.4, including for non-critical systems.

**When the review is NOT required (17.3):**
- Enhancements to existing cloud implementations that do not materially alter the risk profile previously assessed
- The FI must document the materiality determination and retain it for audit

**Subsequent deployments (17.2):**
- After successful 17.1 consultation, subsequent critical system deployments may use a notification approach, subject to four prerequisites being met (see Section 9 below)

## 3. Three Prerequisites for BNM Consultation (17.1)

Before submitting the consultation to BNM, the FI must have completed all three prerequisites:

### Prerequisite (a) — Comprehensive Risk Assessment

| Attribute | Detail |
|-----------|--------|
| **Clause** | 17.1(a), referencing 10.50 and Appendix 10 |
| **What is required** | A comprehensive risk assessment covering technology, operational, legal, and regulatory risks specific to the cloud adoption |
| **Format** | Appendix 7 Part A (Risk Assessment Report) |
| **Scope** | Must address all risk areas in Appendix 10 (Part A: Cloud Governance — 7 areas; Part B: Cloud Design & Control — 14 areas) |
| **Who performs** | The FI conducts the risk assessment. The IESP independently validates it as part of prerequisite (c). |

### Prerequisite (b) — CISO/Board Confirmation

| Attribute | Detail |
|-----------|--------|
| **Clause** | 17.1(b) |
| **What is required** | A signed confirmation from the CISO, board committee chair, or designated senior management |
| **Format** | Appendix 7 Part B (9-point attestation) |
| **Content** | Confirms: risk assessment completed, risks mitigated, controls adequate, competent personnel, BCP adequate, contracts adequate, regulatory requirements met, board briefed, will notify BNM of changes |
| **Dependency** | Cannot be signed until the IESP review (prerequisite c) is complete and findings are addressed |

### Prerequisite (c) — Independent External Pre-Implementation Review

| Attribute | Detail |
|-----------|--------|
| **Clause** | 17.1(c) |
| **What is required** | A pre-implementation review by an independent external service provider |
| **IESP Standards** | Must comply with Appendix 7 Part C (6 requirements: independence, competence, scope, methodology, reporting, QA) |
| **Scope** | Appendix 10 (all 21 areas across Parts A and B) plus Appendix 7 Part D (minimum controls) |
| **Higher-Risk** | For services involving customer information processing/storage or cross-border data transmission, must also comply with Appendix 7 Part C additional requirements |
| **Output** | Risk Assessment Report per Appendix 7 Part A format |

## 4. Appendix 10 Assessment Scope

### Part A — Cloud Governance (7 Areas)

#### Area 1: Cloud Strategy
**What to Assess:**
- Cloud strategy exists and is approved by the board or designated committee
- Strategy is aligned with overall business and technology strategy
- Clear articulation of which workloads are cloud-eligible and which are not
- Cloud-first, cloud-selective, or hybrid approach is defined and justified
- Strategy addresses multi-cloud vs. single-cloud considerations
- Strategy considers long-term cost implications and total cost of ownership
- Regular review cycle for the cloud strategy

**Key Evidence:**
- Board-approved cloud strategy document
- Workload classification and cloud eligibility criteria
- Cloud adoption roadmap
- Cost-benefit analysis for cloud adoption
- Strategy review records

#### Area 2: Roles and Responsibilities
**What to Assess:**
- Clear RACI matrix for cloud operations, security, and governance
- Cloud-specific roles defined (cloud architect, cloud security engineer, cloud operations)
- Shared responsibility model with CSP understood and documented
- Escalation paths for cloud-related issues
- Third-party management roles for cloud vendors

**Key Evidence:**
- Cloud RACI matrix
- Job descriptions for cloud-specific roles
- Shared responsibility model documentation per CSP
- Organizational chart showing cloud team structure
- Escalation procedures

#### Area 3: Policies and Procedures
**What to Assess:**
- Cloud-specific policies covering: security, access management, data management, change management, incident response, backup, configuration management
- Policies aligned with RMIT requirements
- Procedures operationalize the policies with step-by-step guidance
- Policies are communicated and acknowledged by relevant staff
- Regular review and update cycle

**Key Evidence:**
- Cloud security policy
- Cloud access management policy and procedures
- Cloud data management policy
- Cloud change management procedures
- Cloud incident response procedures
- Policy communication and acknowledgment records
- Policy review records

#### Area 4: Risk Management
**What to Assess:**
- Cloud risk register maintained and regularly updated
- Risk assessment methodology appropriate for cloud (considers shared responsibility, multi-tenancy, CSP risks)
- Risk acceptance criteria defined and approved
- Risk monitoring and reporting to senior management/board
- Risk treatment plans with owners and timelines

**Key Evidence:**
- Cloud risk register
- Risk assessment methodology documentation
- Risk acceptance records (signed by appropriate authority)
- Risk reporting to board/management (sample reports)
- Risk treatment plans and status

#### Area 5: Competency
**What to Assess:**
- Cloud skills gap analysis conducted
- Training plan for cloud-specific skills
- Relevant certifications held by key personnel (AWS SAA/SAP, Azure AZ-500, GCP Professional, CCSP, CCSK)
- Knowledge of shared responsibility model across the team
- Succession planning for critical cloud roles

**Key Evidence:**
- Skills gap analysis
- Training plan and completion records
- Certification records for key personnel
- Succession plans for cloud roles

#### Area 6: Compliance
**What to Assess:**
- Regulatory mapping for cloud-specific requirements (RMIT, PDPA, sectoral guidelines)
- Data residency requirements identified and addressed
- Cross-border data transmission requirements (if applicable)
- BNM access rights to data and systems preserved
- Audit access rights preserved in CSP contracts
- Compliance monitoring and reporting

**Key Evidence:**
- Regulatory compliance mapping document
- Data residency analysis and CSP region selection justification
- Cross-border data flow assessment (if applicable)
- CSP contract provisions for regulatory and audit access
- Compliance monitoring reports

#### Area 7: Oversight
**What to Assess:**
- Cloud performance monitoring framework (KPIs, KRIs)
- Regular reporting to board/senior management on cloud operations
- CSP performance monitoring against SLAs
- Independent assurance (internal audit coverage of cloud)
- Periodic review of cloud governance framework effectiveness

**Key Evidence:**
- KPI/KRI definitions for cloud services
- Board/management reporting (sample reports)
- CSP SLA monitoring reports
- Internal audit coverage of cloud (audit plan, reports)
- Governance framework review records

### Part B — Cloud Design and Control (14 Areas)

#### Area 1: Architecture Design
**What to Assess:**
- Reference architecture documented and approved
- Security zones defined (public, private, management, data)
- Multi-tenancy risks addressed in architecture
- Landing zone / account structure design
- Infrastructure as Code (IaC) approach and governance
- Architecture review process for new cloud deployments

**Key Evidence:**
- Cloud reference architecture document
- Security zone design and network diagrams
- Landing zone / account structure documentation
- IaC templates and governance process
- Architecture review board records

#### Area 2: Identity and Access Management
**What to Assess:**
- Cloud IAM policies and implementation
- Privileged access management (PAM) for cloud admin accounts
- Multi-factor authentication (MFA) enforcement
- Federation with enterprise identity provider
- Service account management and rotation
- Access review and recertification processes
- Break-glass / emergency access procedures
- Least privilege principle implementation

**Key Evidence:**
- IAM policy configuration (from cloud console/API)
- PAM tool deployment and configuration
- MFA enforcement configuration
- Federation/SSO configuration
- Service account inventory and rotation schedule
- Access review records
- Break-glass procedures and usage logs

#### Area 3: Data Protection
**What to Assess:**
- Encryption of data at rest (server-side, client-side, KMS)
- Encryption of data in transit (TLS 1.2+, VPN, private connectivity)
- Encryption of data in use (where applicable — confidential computing)
- Key management (CSP-managed vs. customer-managed keys, rotation, access controls)
- Data classification applied to cloud resources
- Data loss prevention (DLP) controls
- Data backup and recovery
- Data residency enforcement (region locking)

**Key Evidence:**
- Encryption configuration for storage services
- TLS configuration for cloud services
- KMS configuration and key rotation policy
- Data classification tagging on cloud resources
- DLP tool configuration and alert reports
- Backup configuration and recovery test results
- Region/location restriction policies

#### Area 4: Network Security
**What to Assess:**
- Virtual network design and segmentation (VPC/VNet architecture)
- Network security groups / security rules configuration
- Private connectivity to cloud (Direct Connect, ExpressRoute, Interconnect)
- DNS architecture in cloud
- API gateway security
- Web application firewall (WAF) deployment
- DDoS protection
- Network flow logging

**Key Evidence:**
- VPC/VNet architecture diagrams
- Security group rule configurations
- Private connectivity architecture and redundancy
- DNS configuration
- API gateway configuration
- WAF rules and configuration
- DDoS protection configuration
- Network flow log configuration and sample analysis

#### Area 5: Compute Security
**What to Assess:**
- VM/instance hardening standards and compliance
- Container security (image scanning, runtime security, registry security)
- Serverless security (function permissions, secrets management)
- Patch management for cloud compute resources
- Anti-malware / endpoint protection for cloud instances
- Secure boot and integrity monitoring

**Key Evidence:**
- Hardening standards for cloud instances
- Compliance scan results
- Container image scanning reports
- Serverless function permission configurations
- Patch management reports for cloud instances
- Anti-malware deployment evidence

#### Area 6: Storage Security
**What to Assess:**
- Storage bucket/blob/object access policies (no public access by default)
- Access logging for storage services
- Encryption configuration for all storage types
- Lifecycle management policies (data retention, deletion)
- Versioning and deletion protection for critical data
- Cross-region replication security

**Key Evidence:**
- Storage access policy configurations
- Public access block configurations
- Access logging configuration
- Encryption settings for storage services
- Lifecycle policy configurations
- Versioning and deletion protection settings

#### Area 7: Logging and Monitoring
**What to Assess:**
- Cloud-native logging enabled (CloudTrail, Activity Log, Audit Log)
- Centralized log aggregation (SIEM integration)
- Alert rules for security-relevant events
- Log retention aligned with regulatory requirements
- Monitoring of cloud resource configuration changes
- Cost monitoring and anomaly detection
- Performance monitoring and capacity management

**Key Evidence:**
- Cloud audit log configuration
- SIEM integration architecture
- Alert rule configurations
- Log retention policies
- Configuration change monitoring (Config Rules, Azure Policy, etc.)
- Cost monitoring dashboards and alert configurations
- Performance monitoring setup

#### Area 8: Vulnerability Management
**What to Assess:**
- Cloud resource vulnerability scanning (instances, containers, serverless)
- CSP-native security posture management (Security Hub, Defender, SCC)
- Patching SLAs and compliance rates
- Penetration testing of cloud environment (with CSP policies compliance)
- Remediation tracking and SLA adherence

**Key Evidence:**
- Vulnerability scanning tool configuration and reports
- Security posture management dashboards
- Patching compliance reports
- Penetration test reports for cloud environment
- Remediation tracking records

#### Area 9: Change Management
**What to Assess:**
- IaC governance (code review, version control, approval workflows)
- CI/CD pipeline security (pipeline hardening, secrets management, artifact signing)
- Change approval process for cloud infrastructure changes
- Rollback capability and procedures
- Configuration drift detection and remediation
- Emergency change procedures for cloud

**Key Evidence:**
- IaC repository and governance process documentation
- CI/CD pipeline configuration and security controls
- Change records for cloud infrastructure (last 12 months)
- Rollback procedure documentation and test results
- Configuration drift detection tool and reports
- Emergency change records

#### Area 10: Incident Response
**What to Assess:**
- Cloud-specific incident response procedures
- CSP coordination procedures (security notifications, support escalation)
- Forensic capability in cloud (snapshot, log preservation, evidence collection)
- Communication procedures for cloud incidents
- Integration with overall incident management framework
- Incident response testing/exercises for cloud scenarios

**Key Evidence:**
- Cloud IR procedures
- CSP support and escalation contacts
- Forensic procedures for cloud
- Communication templates for cloud incidents
- Incident response exercise records (cloud-specific scenarios)
- Cloud incident reports (if any)

#### Area 11: Business Continuity
**What to Assess:**
- Multi-region / multi-AZ architecture for critical workloads
- Backup strategy and cross-region replication
- DR architecture and tested recovery capability
- RTO/RPO defined and validated for cloud-hosted critical systems
- CSP outage response procedures
- Data recovery testing results

**Key Evidence:**
- Multi-region/AZ architecture documentation
- Backup configuration and cross-region replication settings
- DR architecture documentation
- RTO/RPO definitions for cloud workloads
- DR test results (last 12 months)
- CSP outage response procedures

#### Area 12: Vendor Management
**What to Assess:**
- CSP assessment (financial stability, security certifications, compliance)
- Shared responsibility model documented and understood
- SLA monitoring (availability, performance, support response)
- CSP security certifications reviewed (SOC 2, ISO 27001, CSA STAR)
- Regular review of CSP risk profile
- Sub-processor management (CSP's third parties)

**Key Evidence:**
- CSP assessment documentation
- Shared responsibility model mapping
- SLA monitoring reports
- CSP certification copies (SOC 2 Type II, ISO 27001, etc.)
- CSP risk assessment records
- Sub-processor notification and review process

#### Area 13: Exit Strategy
**What to Assess:**
- Exit strategy documented and approved
- Data portability assessment (formats, APIs, export mechanisms)
- Migration plan to alternative provider or on-premise
- Data destruction procedures upon exit
- Contractual provisions for exit (notice period, data return, transition support)
- Cost estimate for exit/migration
- Regular testing or validation of exit strategy feasibility

**Key Evidence:**
- Exit strategy document
- Data portability assessment
- Migration plan (at least conceptual)
- Data destruction provisions in contract
- Exit-related contractual provisions
- Cost estimates for exit scenarios

#### Area 14: Regulatory Compliance
**What to Assess:**
- Data residency compliance (data stays in approved jurisdictions)
- BNM access rights preserved (contractual and technical)
- Audit access rights (FI auditors, external auditors, BNM)
- Regulatory reporting capabilities maintained
- Compliance with PDPA and sector-specific data protection requirements
- Record-keeping requirements met in cloud

**Key Evidence:**
- Data residency configuration and verification
- Contractual provisions for BNM and audit access
- Technical mechanism for regulatory access
- Regulatory reporting capability from cloud systems
- PDPA compliance documentation for cloud
- Record retention configuration

## 5. Higher-Risk Services — Additional Requirements

For cloud services involving **customer information processing/storage** or **cross-border data transmission**, the submission must also comply with Appendix 7 Part C additional requirements:

| Requirement | Detail |
|-------------|--------|
| **Data classification** | Customer data must be classified and handling requirements defined |
| **Cross-border assessment** | Legal and regulatory risks of cross-border data transmission must be assessed |
| **Data protection impact** | PDPA and sector-specific data protection impact assessment required |
| **Encryption requirements** | Enhanced encryption requirements for customer data (customer-managed keys recommended) |
| **Access restrictions** | Strict access controls for customer data, including CSP personnel access limitations |
| **Incident notification** | Enhanced incident notification requirements for breaches involving customer data |
| **Data residency** | Primary data must reside in Malaysia unless regulatory exemption obtained |

## 6. BNM Consultation Process

The pre-implementation review is one component of the BNM consultation submission. The overall process:

1. **FI conducts risk assessment** per 10.50 and Appendix 10
2. **FI engages IESP** to perform independent pre-implementation review
3. **IESP conducts review** covering Appendix 10 (21 areas) and Appendix 7 Part D (minimum controls)
4. **IESP issues report** in Appendix 7 Part A format
5. **FI remediates** critical and high findings identified by the IESP
6. **CISO/board signs Part B confirmation** (only after IESP findings are addressed)
7. **FI submits consultation package to BNM** including:
   - Risk Assessment Report (Part A)
   - Confirmation (Part B)
   - IESP Review Report (Part A format, referencing Part C compliance)
   - For higher-risk: additional Part C documentation
8. **BNM reviews** the submission and may:
   - Approve with no concerns
   - Request additional information or assessment
   - Raise concerns requiring remediation before approval
   - Direct additional IESP review (under 17.4)
9. **FI proceeds with implementation** only after BNM consultation is completed satisfactorily

## 7. Key Activities Checklist

### Phase 1 — Planning and Scoping
- [ ] Confirm trigger condition (first-time cloud for critical systems)
- [ ] Identify cloud deployment scope (CSP, services, regions, workloads)
- [ ] Request FI's cloud risk assessment (prerequisite a)
- [ ] Request FI's cloud strategy, governance, and policy documentation
- [ ] Identify if higher-risk services criteria apply (customer info, cross-border)
- [ ] Define assessment timeline aligned with BNM consultation timeline
- [ ] Confirm IESP team qualifications (cloud certifications: CCSP, CSP-specific certs, per Part C)
- [ ] Issue engagement letter with scope, timeline, and deliverables

### Phase 2 — Cloud Governance Assessment (Appendix 10 Part A)
- [ ] Assess cloud strategy (Area 1)
- [ ] Assess roles and responsibilities (Area 2)
- [ ] Assess policies and procedures (Area 3)
- [ ] Assess risk management (Area 4)
- [ ] Assess competency (Area 5)
- [ ] Assess compliance framework (Area 6)
- [ ] Assess oversight mechanisms (Area 7)

### Phase 3 — Cloud Design and Control Assessment (Appendix 10 Part B)
- [ ] Assess architecture design (Area 1)
- [ ] Assess identity and access management (Area 2)
- [ ] Assess data protection controls (Area 3)
- [ ] Assess network security (Area 4)
- [ ] Assess compute security (Area 5)
- [ ] Assess storage security (Area 6)
- [ ] Assess logging and monitoring (Area 7)
- [ ] Assess vulnerability management (Area 8)
- [ ] Assess change management (Area 9)
- [ ] Assess incident response (Area 10)
- [ ] Assess business continuity (Area 11)
- [ ] Assess vendor management (Area 12)
- [ ] Assess exit strategy (Area 13)
- [ ] Assess regulatory compliance (Area 14)

### Phase 4 — Minimum Controls Assessment (Appendix 7 Part D)
- [ ] Assess access control domains
- [ ] Assess physical security (if applicable to cloud — e.g., on-premise connectivity)
- [ ] Assess operations security
- [ ] Assess communications security
- [ ] Assess incident management
- [ ] Assess business continuity
- [ ] Assess online transaction controls (if applicable)
- [ ] Assess mobile application controls (if applicable)

### Phase 5 — Higher-Risk Services Assessment (if applicable)
- [ ] Assess customer data classification and handling
- [ ] Assess cross-border data transmission controls
- [ ] Assess data protection impact
- [ ] Assess enhanced encryption for customer data
- [ ] Assess customer data access restrictions
- [ ] Assess incident notification for customer data breaches
- [ ] Assess data residency compliance

### Phase 6 — Reporting
- [ ] Draft findings with risk ratings, evidence, and recommendations
- [ ] Map all findings to Appendix 10 areas and Appendix 7 Part D domains
- [ ] Conduct quality assurance / peer review
- [ ] Discuss draft findings with FI management
- [ ] Incorporate management responses and remediation timelines
- [ ] Finalize report in Appendix 7 Part A format
- [ ] Confirm independence declaration and Part C compliance statement
- [ ] Issue signed report

### Phase 7 — Post-Report Support
- [ ] Support FI in addressing findings before Part B confirmation
- [ ] Review remediation evidence for critical/high findings (if engaged to do so)
- [ ] Support BNM consultation process (if requested — respond to BNM queries)

## 8. Common Findings and Red Flags

| Category | Common Issues |
|----------|---------------|
| **Governance** | No board-approved cloud strategy, undefined shared responsibility model, no cloud-specific policies, skills gap not addressed |
| **IAM** | Root/global admin accounts without MFA, excessive service account permissions, no access reviews for cloud, no PAM for cloud admin |
| **Data Protection** | Unencrypted storage, CSP-managed keys only (no CMK), no DLP, data residency not enforced, no data classification |
| **Network** | Public endpoints for internal services, overly permissive security groups, no private connectivity, no WAF for internet-facing apps |
| **Logging** | Audit logging not enabled for all services, logs not sent to SIEM, short retention, no alert rules for security events |
| **Vulnerability** | No cloud vulnerability scanning, infrequent patching, no penetration testing of cloud environment, security posture management not deployed |
| **Change Management** | IaC not used (manual console changes), no code review for infrastructure changes, no configuration drift detection |
| **BCP/DR** | Single-region deployment for critical systems, untested DR, no RTO/RPO defined for cloud workloads, no CSP outage response plan |
| **Exit** | No exit strategy, data portability not assessed, no contractual exit provisions, vendor lock-in risks not mitigated |
| **Compliance** | Data residency not verified, BNM access not contractually preserved, PDPA impact not assessed, audit access not tested |

## 9. Subsequent Deployments — 17.2 Notification Approach

After successful 17.1 consultation, the FI may use a notification approach for subsequent cloud deployments of critical systems, provided **all four prerequisites** are met:

| # | Prerequisite | IESP Role |
|---|-------------|-----------|
| (a) | 17.1 consultation completed with no BNM concerns | N/A — historical condition |
| (b) | TRMF enhanced to address cloud/emerging tech risks | IESP may assess TRMF adequacy |
| (c) | Independent assurance established on the enhanced framework | **IESP required** to provide this assurance |
| (d) | Sufficient incident response plans in place | IESP may assess IR plan adequacy |

**17.3 Exemption:** Enhancements that do not materially alter the risk profile previously assessed are exempt from 17.1 and 17.2. The FI must document the materiality determination.

## 10. Cross-References

| Document | Path |
|----------|------|
| Regulatory Requirements (all clauses) | `/requirements/regulatory-requirements.md` |
| Emerging Tech Review Requirements | `/requirements/emerging-tech-review.md` |
| DCRA Requirements | `/requirements/dcra-requirements.md` |
| NRA Requirements | `/requirements/nra-requirements.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
