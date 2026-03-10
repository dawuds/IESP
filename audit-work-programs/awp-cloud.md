# Cloud IESP Audit Work Program
## Cloud Services Risk Assessment

> Per BNM RMiT Nov 2025 — Paragraph 17.1, mapped to paragraphs 10.50 to 10.52, Appendix 10

### Engagement Overview
- **Engagement Type:** Cloud IESP Assessment
- **Regulatory Basis:** Paragraph 17.1
- **Scope Clauses:** 10.50, 10.51, 10.52, Appendix 10 (Parts A and B)
- **Frequency:** Every 3 years or material change (including new CSP adoption, migration of critical systems, or significant architecture change)
- **Reporting:** Appendix 7 Part A

---

### Phase 1: Planning and Scoping

| Step | Activity | Deliverable |
|------|----------|-------------|
| P-01 | Obtain the FI's cloud services inventory — all CSPs, service models (IaaS/PaaS/SaaS), deployment models (public/private/hybrid), and the systems/data hosted | Cloud services inventory |
| P-02 | Request the FI's cloud risk assessment and classification of data hosted in cloud (public, confidential, restricted) | Cloud risk assessment and data classification |
| P-03 | Identify critical and sensitive systems in cloud and map them to CSPs and regions | Critical systems-to-CSP mapping |
| P-04 | Obtain CSP contracts, SLAs, and most recent SOC 2 Type II / ISO 27001 / CSA STAR reports for each in-scope CSP | CSP assurance pack |
| P-05 | Review prior cloud assessment reports and track remediation of prior findings | Prior findings tracker |
| P-06 | Understand the FI's cloud operating model — who manages what (FI vs. CSP vs. MSP) per the shared responsibility model | Shared responsibility mapping |

---

### Phase 2: Detailed Testing

## Part A: Cloud Governance

#### A1: Cloud Risk Management

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-01 | Verify cloud-specific risk assessment is performed and maintained | 1. Obtain the FI's cloud risk assessment framework<br>2. Verify it covers: data sovereignty, vendor lock-in, shared tenancy, supply chain, regulatory compliance<br>3. Check that risks are assessed per CSP and per service<br>4. Verify the risk assessment is reviewed at least annually | - Cloud risk assessment framework<br>- Risk register (cloud section)<br>- Review/approval records | Pass: Comprehensive cloud risk assessment exists covering all key risk domains, assessed per CSP/service, and reviewed within the last 12 months. Fail: No cloud-specific risk assessment, missing key risk domains, or stale assessment |
| CLD-02 | Verify cloud risk appetite and tolerance are defined | 1. Check that the FI has defined what can and cannot be placed in cloud<br>2. Verify data classification rules for cloud placement (e.g., restricted data cannot be in public cloud without specific controls)<br>3. Confirm risk appetite is approved by the board or designated committee | - Cloud risk appetite statement<br>- Data classification-to-cloud mapping<br>- Board/committee approval | Pass: Cloud risk appetite is formally defined, data classification rules exist for cloud placement, and approved at appropriate level. Fail: No risk appetite defined or no data classification rules for cloud |

#### A2: Cloud Usage Policy

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-03 | Verify a cloud usage policy governs adoption and operation of cloud services | 1. Obtain the FI's cloud usage policy<br>2. Verify it covers: approved CSPs, approved service/deployment models, data classification requirements, security baseline requirements, approval workflow for new cloud services<br>3. Check the policy is communicated to relevant stakeholders<br>4. Verify adherence — sample 3 recent cloud service adoptions and check they followed the policy | - Cloud usage policy<br>- Communication/awareness records<br>- Sample cloud adoption records | Pass: Policy exists covering all required elements, is communicated, and sampled adoptions demonstrate adherence. Fail: No policy, incomplete coverage, or adoptions bypass the policy |

#### A3: Due Diligence

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-04 | Verify due diligence is performed before CSP engagement | 1. Obtain due diligence procedures and checklists for CSP evaluation<br>2. For each in-scope CSP, verify that due diligence was performed covering: financial viability, security capabilities, regulatory compliance, data residency, subcontracting, and business continuity<br>3. Verify due diligence is refreshed periodically (at least annually for critical CSPs) | - Due diligence procedure<br>- Completed due diligence reports per CSP<br>- Refresh schedule and records | Pass: Documented due diligence performed for all CSPs covering required areas, refreshed at least annually for critical CSPs. Fail: No due diligence, incomplete coverage, or not refreshed |

#### A4: CSP Certifications

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-05 | Verify CSP certifications and independent assurance reports are obtained and reviewed | 1. Obtain current SOC 2 Type II, ISO 27001, and CSA STAR reports for each CSP<br>2. Verify the reports cover the services used by the FI<br>3. Review any exceptions, qualifications, or control deficiencies noted in the reports<br>4. Check that the FI has assessed the impact of any reported deficiencies on their risk posture<br>5. Verify complementary user entity controls (CUECs) identified in SOC reports are implemented by the FI | - SOC 2 Type II reports<br>- ISO 27001 certificates<br>- CSA STAR reports<br>- FI's review and assessment of report findings<br>- CUEC implementation evidence | Pass: Current reports obtained for all CSPs, covering relevant services, deficiencies assessed, and CUECs implemented. Fail: Missing or expired reports, reports don't cover relevant services, or CUECs not implemented |

#### A5: Contract Management

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-06 | Verify CSP contracts contain required regulatory provisions | 1. Review contracts with each in-scope CSP<br>2. Check for: right to audit, data ownership and portability, data residency and sovereignty, breach notification obligations, subcontracting controls, termination and exit provisions, regulatory access rights (BNM inspection)<br>3. Verify contracts are reviewed by legal and compliance | - CSP contracts<br>- Legal/compliance review records<br>- Contract compliance checklist | Pass: All contracts contain required provisions (audit rights, data ownership, breach notification, regulatory access, exit provisions). Fail: Missing critical provisions in any contract |

#### A6: Oversight over CSPs

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-07 | Verify ongoing monitoring and oversight of CSPs | 1. Review the FI's CSP oversight framework<br>2. Check that CSP performance is monitored against SLAs (availability, incident response times, support responsiveness)<br>3. Verify periodic service review meetings are held with CSPs<br>4. Confirm that CSP incident notifications are received, tracked, and assessed for impact<br>5. Check that the FI monitors CSP security advisories and applies relevant patches/mitigations | - CSP oversight framework<br>- SLA performance reports<br>- Service review meeting minutes<br>- CSP incident tracking records<br>- Security advisory tracking | Pass: Formal oversight framework with SLA monitoring, periodic reviews, incident tracking, and security advisory monitoring. Fail: No oversight framework, or any critical monitoring gap |

#### A7: Skilled Personnel

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-08 | Verify the FI has sufficient skilled personnel to manage cloud environments | 1. Review cloud team structure, roles, and responsibilities<br>2. Verify cloud-specific certifications held by key personnel (e.g., AWS/Azure/GCP professional certifications)<br>3. Check that a training and development plan exists for cloud skills<br>4. Assess whether the FI can independently assess CSP configurations and security posture without relying solely on the CSP | - Cloud team organisational chart<br>- Personnel certification records<br>- Training plan<br>- Evidence of independent assessment capability | Pass: Dedicated cloud team with relevant certifications, active training plan, and demonstrated ability to independently assess cloud security. Fail: No dedicated cloud resources, no certifications, or complete reliance on CSP for security assessment |

---

## Part B: Cloud Design and Control

#### B1: Cloud Architecture

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-09 | Verify cloud architecture is designed for resilience and security | 1. Obtain the FI's cloud architecture design documents and diagrams<br>2. Verify multi-AZ or multi-region deployment for critical workloads<br>3. Check that architecture follows well-architected framework principles (or equivalent)<br>4. Verify network architecture in cloud (VPC/VNET design, subnet segmentation, security groups, NACLs)<br>5. Confirm architecture has been reviewed by qualified cloud architects | - Cloud architecture documents<br>- Multi-AZ/region deployment evidence<br>- Well-architected review reports<br>- VPC/VNET design documents | Pass: Architecture is documented, uses multi-AZ for critical workloads, follows well-architected principles, and has proper network segmentation. Fail: No documentation, single-AZ critical workloads, or no network segmentation |

#### B2: Application Delivery Models (CI/CD, IaC)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-10 | Verify CI/CD pipelines have appropriate security controls | 1. Review CI/CD pipeline architecture and tools (e.g., Jenkins, GitLab CI, GitHub Actions)<br>2. Verify security gates are embedded in the pipeline (SAST, DAST, SCA, container scanning)<br>3. Check that deployment to production requires approval and cannot be bypassed<br>4. Verify pipeline configuration is version-controlled and access-restricted<br>5. Check that secrets are not hardcoded in pipeline configurations | - CI/CD architecture documentation<br>- Security gate configuration<br>- Approval workflow evidence<br>- Pipeline access controls<br>- Secrets management configuration | Pass: CI/CD pipelines have security scanning gates, production deployment requires approval, configurations are version-controlled, and secrets are managed securely. Fail: No security gates, direct deployment without approval, or hardcoded secrets |
| CLD-11 | Verify Infrastructure as Code (IaC) governance and security | 1. Identify IaC tools in use (Terraform, CloudFormation, ARM, Pulumi)<br>2. Verify IaC templates are stored in version control with change approval<br>3. Check that IaC templates are scanned for security misconfigurations before deployment<br>4. Verify that manual infrastructure changes (console/CLI) are detected and reconciled with IaC state<br>5. Confirm IaC state files are stored securely (encrypted, access-controlled) | - IaC tool inventory<br>- Version control repository<br>- IaC scanning tool configuration<br>- Drift detection mechanism<br>- State file storage configuration | Pass: IaC is version-controlled, scanned for misconfigurations, drift is detected, and state files are secured. Fail: IaC not version-controlled, no scanning, or no drift detection |

#### B3: Virtualisation and Containerisation

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-12 | Verify container and virtualisation security controls | 1. Identify container platforms in use (Kubernetes, ECS, AKS, GKE)<br>2. Verify container images are sourced from approved registries and scanned for vulnerabilities<br>3. Check that containers run with least-privilege (non-root, read-only filesystem where possible)<br>4. Verify pod/container network policies enforce segmentation<br>5. Check that orchestrator (e.g., Kubernetes) is hardened per CIS benchmarks | - Container platform inventory<br>- Image scanning reports<br>- Container runtime security configurations<br>- Network policy configurations<br>- CIS benchmark compliance reports | Pass: Approved image registries, vulnerability scanning, least-privilege runtime, network policies enforced, and orchestrator hardened. Fail: Unscanned images, containers running as root, or no network policies |

#### B4: Change Management

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-13 | Verify cloud change management controls | 1. Review the cloud change management procedure<br>2. Sample 10 recent cloud infrastructure/configuration changes<br>3. Verify each change has: request, risk assessment, approval, implementation plan, testing, and post-implementation validation<br>4. Check that changes to security-critical configurations (IAM, network, encryption) have enhanced approval | - Cloud change management procedure<br>- 10 sampled change records<br>- Enhanced approval evidence for security changes | Pass: All sampled changes are fully documented with appropriate approvals, and security-critical changes have enhanced controls. Fail: Incomplete change records, missing approvals, or no enhanced controls for security changes |

#### B5: Backup and Recovery

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-14 | Verify cloud backup and recovery arrangements | 1. Review cloud backup policy and configuration for critical workloads<br>2. Verify backup frequency, retention periods, and storage locations (cross-region for critical data)<br>3. Check that backups are encrypted at rest and in transit<br>4. Verify backup restoration has been tested within the last 12 months<br>5. Confirm backup monitoring — failed backups are detected and remediated | - Backup policy and configuration<br>- Backup retention settings<br>- Encryption configuration<br>- Restoration test results<br>- Backup monitoring/alerting configuration | Pass: Regular backups configured for critical workloads, cross-region for critical data, encrypted, tested within 12 months, and monitored. Fail: Missing backups for critical workloads, no encryption, untested, or unmonitored |

#### B6: Interoperability and Portability

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-15 | Verify cloud portability and interoperability arrangements | 1. Review the FI's approach to avoiding vendor lock-in (use of open standards, abstraction layers, multi-cloud strategy)<br>2. Verify that data can be exported from the CSP in standard, usable formats<br>3. Check that critical applications can be migrated to an alternative CSP or on-premises within acceptable timeframes<br>4. Verify data export and migration procedures have been tested | - Portability/interoperability strategy<br>- Data export format documentation<br>- Migration feasibility assessment<br>- Data export/migration test results | Pass: Portability strategy exists, data can be exported in standard formats, and migration feasibility has been assessed and tested. Fail: No portability consideration, proprietary data formats with no export, or no migration testing |

#### B7: Exit Strategy

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-16 | Verify a cloud exit strategy is documented and actionable | 1. Obtain the cloud exit strategy for each critical CSP engagement<br>2. Verify it covers: trigger events, data retrieval process, migration approach, timeline, resource requirements, and communication plan<br>3. Check that the exit strategy has been reviewed within the last 12 months<br>4. Verify contractual terms support the exit strategy (data retrieval period, assistance obligations) | - Cloud exit strategy document<br>- Contractual exit provisions<br>- Review/approval records | Pass: Exit strategy documented for each critical CSP, covers all required elements, reviewed within 12 months, and supported by contractual terms. Fail: No exit strategy, missing critical elements, or contractual terms do not support exit |

#### B8: Cryptographic Key Management

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-17 | Verify cryptographic key management in cloud environments | 1. Review the FI's cloud encryption and key management strategy<br>2. Identify whether FI uses CSP-managed keys (SSE-S3, Azure-managed), customer-managed keys (CMK), or bring-your-own-key (BYOK)<br>3. For customer-managed keys, verify key rotation schedule and access controls<br>4. Verify encryption at rest is enabled for all data stores (databases, object storage, block storage, file systems)<br>5. Verify encryption in transit (TLS 1.2+) for all cloud service endpoints | - Encryption and key management policy<br>- Key management configuration<br>- Encryption-at-rest configuration per data store<br>- TLS configuration evidence | Pass: Encryption at rest enabled for all data stores, encryption in transit enforced, key management strategy defined with appropriate key ownership, and key rotation in place. Fail: Unencrypted data stores, no key management strategy, or no key rotation for customer-managed keys |

#### B9: Access Controls

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-18 | Verify identity and access management in cloud environments | 1. Review cloud IAM architecture (identity federation, SSO, MFA)<br>2. Verify MFA is enforced for all cloud console and API access<br>3. Check that the principle of least privilege is applied — review IAM policies for overly permissive roles (e.g., wildcard permissions)<br>4. Verify privileged/admin access is limited, separately managed, and monitored<br>5. Verify service accounts and API keys are managed with rotation and least privilege<br>6. Check for unused/stale IAM accounts and access keys | - IAM architecture documentation<br>- MFA enforcement configuration<br>- IAM policy review results<br>- Privileged access inventory<br>- Service account/API key inventory<br>- Stale account report | Pass: Federation/SSO with MFA enforced, least-privilege IAM policies, privileged access controlled and monitored, and service accounts/keys managed. Fail: No MFA, overly permissive policies, uncontrolled privileged access, or stale accounts/keys |

#### B10: Cybersecurity Operations

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-19 | Verify cloud security monitoring and threat detection | 1. Verify cloud-native security monitoring is enabled (AWS CloudTrail/GuardDuty, Azure Defender/Sentinel, GCP Security Command Center)<br>2. Check that monitoring covers: API activity, network flows, identity events, and data access patterns<br>3. Verify alerts are routed to the SOC and triaged within defined SLAs<br>4. Check that cloud security posture management (CSPM) tools are deployed to detect misconfigurations<br>5. Review CSPM findings and remediation status | - Cloud security monitoring configuration<br>- SOC integration evidence<br>- CSPM tool deployment and configuration<br>- CSPM findings and remediation tracker | Pass: Cloud-native security monitoring enabled, integrated with SOC, CSPM deployed with active remediation of findings. Fail: Security monitoring not enabled, not integrated with SOC, or CSPM not deployed |

#### B11: DDoS Protection

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-20 | Verify DDoS protection for cloud-hosted services | 1. Verify DDoS protection is enabled for internet-facing cloud services (e.g., AWS Shield, Azure DDoS Protection, Cloud Armor)<br>2. Check that DDoS protection covers both network-layer (L3/L4) and application-layer (L7) attacks<br>3. Verify DDoS response playbooks exist and are tested<br>4. Confirm alerting is configured for DDoS events | - DDoS protection configuration<br>- DDoS response playbook<br>- DDoS test/drill results<br>- Alert configuration | Pass: DDoS protection enabled at L3/L4 and L7 for internet-facing services, response playbook exists and is tested, and alerts are configured. Fail: No DDoS protection, no response playbook, or untested |

#### B12: Data Loss Prevention

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-21 | Verify data loss prevention controls in cloud environments | 1. Review the FI's cloud DLP strategy and tooling<br>2. Verify DLP policies cover: data exfiltration detection, sensitive data exposure in storage (S3 bucket policies, blob storage access), and data sharing controls<br>3. Check that DLP alerts are triaged and investigated<br>4. Verify that public access to cloud storage is explicitly blocked unless specifically approved with compensating controls | - Cloud DLP strategy<br>- DLP policy configuration<br>- DLP alert investigation records<br>- Cloud storage public access settings | Pass: DLP strategy and tooling deployed, covering exfiltration and exposure, alerts investigated, and public storage access blocked by default. Fail: No DLP controls, no alert investigation, or public storage access uncontrolled |

#### B13: Security Operations Centre (SOC)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-22 | Verify SOC coverage extends to cloud environments | 1. Verify that cloud security events are ingested into the SOC's SIEM<br>2. Check that cloud-specific detection rules and use cases are defined (e.g., unusual API calls, cross-account access, privilege escalation)<br>3. Verify SOC analysts have the skills and access to investigate cloud security events<br>4. Review 5 recent cloud security incidents and assess SOC response quality | - SIEM log source configuration<br>- Cloud detection rules/use cases<br>- SOC analyst skill assessment<br>- 5 sampled cloud incident records | Pass: Cloud events in SIEM, cloud-specific detections defined, analysts can investigate cloud events, and sampled incidents show adequate response. Fail: Cloud events not in SIEM, no cloud-specific detections, or poor incident response quality |

#### B14: Cyber Response and Recovery

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-23 | Verify cyber incident response and recovery plans cover cloud environments | 1. Review the FI's incident response plan for cloud-specific scenarios (cloud account compromise, data breach, CSP outage, ransomware in cloud)<br>2. Verify that response procedures account for the shared responsibility model<br>3. Check that CSP incident notification and escalation contacts are documented<br>4. Verify that cloud DR/failover has been tested (e.g., cross-region failover)<br>5. Review results of the most recent cloud DR test | - Cloud incident response procedures<br>- CSP escalation contacts<br>- Cloud DR/failover test plan<br>- Cloud DR test results | Pass: Cloud-specific incident response procedures exist, shared responsibility is addressed, CSP contacts documented, and cloud DR tested within 12 months. Fail: No cloud-specific IR procedures, shared responsibility not addressed, or cloud DR untested |

---

### Supplementary Tests: Cloud Compliance and Data Residency

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| CLD-24 | Verify data residency compliance | 1. Identify regulatory data residency requirements applicable to the FI<br>2. Map each cloud service and data store to its hosting region(s)<br>3. Verify that restricted data resides only in approved regions<br>4. Check that CSP configurations prevent data replication to non-approved regions<br>5. Verify that BNM approval was obtained for any data hosted outside Malaysia (if required) | - Data residency requirements register<br>- Cloud resource region mapping<br>- CSP region configuration<br>- BNM approval records (if applicable) | Pass: All data residency requirements mapped, cloud configurations enforce approved regions, and regulatory approvals obtained where required. Fail: Data in non-approved regions, no region enforcement, or missing regulatory approvals |
| CLD-25 | Verify cloud security baseline and hardening | 1. Obtain the FI's cloud security baseline/hardening standard<br>2. Verify alignment with CIS Cloud Benchmarks or equivalent<br>3. Run or review results of automated compliance checks against the baseline<br>4. Check remediation status of non-compliant findings | - Cloud security baseline document<br>- CIS Benchmark alignment mapping<br>- Automated compliance scan results<br>- Remediation tracker | Pass: Security baseline exists, aligned with CIS or equivalent, automated compliance checking in place, and non-compliant findings are tracked and remediated. Fail: No baseline, no automated checking, or significant unremediated findings |

---

### Phase 3: Reporting

| Step | Activity | Deliverable |
|------|----------|-------------|
| R-01 | Consolidate all test results and assign risk ratings (High/Medium/Low) to each finding | Findings register with risk ratings |
| R-02 | Map findings to specific Appendix 10 control areas for structured reporting | Findings-to-Appendix 10 mapping |
| R-03 | Draft recommendations with specific remediation steps, responsible parties, and timelines | Recommendations tracker |
| R-04 | Conduct findings walkthrough with FI cloud, security, and risk teams | Walkthrough meeting minutes |
| R-05 | Prepare the formal Cloud IESP report in Appendix 7 Part A format | Final Cloud IESP report |
| R-06 | Obtain FI management sign-off on the report and management action plans | Signed report and action plans |

---

### Phase 4: Board Deliberation Support

| Step | Activity | Deliverable |
|------|----------|-------------|
| B-01 | Prepare executive summary and presentation for the designated board committee (per 8.3), highlighting cloud-specific risks | Board presentation deck |
| B-02 | Attend the designated committee meeting to present findings and respond to queries | Attendance record and meeting minutes |
| B-03 | Document any additional directives and incorporate into final report | Updated report (if required) |

---

### Appendices

- **Appendix A:** Document Request List (DRL) template
- **Appendix B:** Appendix 10 control mapping matrix
- **Appendix C:** Appendix 7 Part A report template
- **Appendix D:** Risk rating methodology
- **Appendix E:** Cloud security baseline checklist (by CSP)
- **Appendix F:** Shared responsibility model reference (by CSP and service model)
