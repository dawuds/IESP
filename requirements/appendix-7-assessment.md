# Appendix 7 Assessment Framework — IESP Practitioner Guide

> BNM RMiT Nov 2025 — The Universal Framework for ALL Independent External Service Provider Assessments

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document — *Risk Management in Technology (RMiT)*, November 2025 edition — for the authoritative and binding requirements.

---

## 1. Overview

Appendix 7 of BNM RMiT is the **single most important reference** for any IESP engagement. Every technology risk assessment conducted by an independent external service provider — regardless of the specific trigger (DCRA, NRA, cloud pre-implementation, emerging technology, or ad-hoc BNM direction) — must conform to this appendix.

### 1.1 Why Appendix 7 Is Universal

Appendix 7 is referenced by every major IESP trigger clause in RMiT:

| Trigger | Primary Clause | Appendix 7 Reference |
|---------|---------------|---------------------|
| Data Centre Resilience Assessment | 14.1 | Report per Part A; ESP conduct per Part C; controls per Part D |
| Network Resilience Assessment | 14.2 | Report per Part A; ESP conduct per Part C; controls per Part D |
| Cloud Services (pre-implementation) | 17.1 | Report per Part A; ESP conduct per Part C; controls per Part D + para 17.1 |
| Emerging Technology / AI | 17.1 | Report per Part A; ESP conduct per Part C; controls per Part D + para 17.1 |
| Digital Services / Online Transactions | 14.3 | Report per Part A; ESP conduct per Part C; controls per Part D (Items 1 and 2) |
| BNM-directed review | 1.4 | Scope as directed; format per Appendix 7 |

### 1.2 Structure of Appendix 7

Appendix 7 has four parts, each serving a distinct function:

| Part | Title | Pages (PDF) | Purpose |
|------|-------|-------------|---------|
| **A** | Risk Assessment Report | pp56–57 | Prescribes the report format and content requirements |
| **B** | Format of Confirmation | p58 | Board/senior management confirmation template |
| **C** | Requirements on External Party Assurance | p59 | Rules governing IESP conduct and deliverables |
| **D** | Minimum Controls | pp59–61 | The substantive control areas to be assessed |

### 1.3 Reading Order for Practitioners

The logical order for using this guide differs from the appendix numbering:

1. **Start with Part C** — understand what you, as the IESP, must comply with
2. **Move to Part D** — this is the substantive assessment scope
3. **Then Part A** — structure your report
4. **Finally Part B** — support the FI in preparing the confirmation

This guide follows this practitioner-oriented order.

---

## 2. Part C — Requirements on External Party Assurance

Part C defines the six requirements that govern the IESP's conduct, independence, and deliverables. Non-compliance with any of these requirements undermines the validity of the entire assessment.

### 2.1 Requirement C.1 — Independence

> "Assurance shall be conducted by an independent ESP engaged by the FI."

**What this means in practice:**

- The IESP must be **engaged directly by the financial institution**, not by the technology vendor or third-party service provider being assessed.
- The IESP must have **no conflicts of interest** — it cannot have been involved in designing, implementing, or operating the systems under review.
- Independence must be **documented** in the engagement letter and **affirmed** in the risk assessment report.

**Practical guidance:**

- Verify the engagement letter explicitly names the FI as the engaging party.
- Confirm no team member has provided consulting, implementation, or operational services to the FI for the systems in scope within the past 24 months (apply professional judgement on what constitutes a conflict).
- If the IESP firm has other engagements with the FI (e.g., external audit, IT consulting), document safeguards in the engagement letter.
- Maintain an independence register for each engagement.

### 2.2 Requirement C.2 — Understanding of Proposed Services

> "The independent ESP must understand the proposed services, data flows, system architecture, connectivity and dependencies."

**What this means in practice:**

- Before commencing the assessment, the IESP team must develop a **thorough understanding** of the technology environment being assessed.
- This goes beyond reading documentation — the team must understand how data moves, how systems connect, and what depends on what.

**Practical guidance:**

- Conduct a **kickoff walkthrough** with the FI's technology team covering:
  - Business context and purpose of the service/system
  - End-to-end data flow diagrams
  - System architecture diagrams (logical and physical)
  - Network connectivity and topology
  - Upstream and downstream dependencies (internal and external)
  - Integration points with other FI systems
- Document this understanding in the scoping document before starting fieldwork.
- If the IESP team does not understand the technology stack, **do not proceed** — either upskill, bring in subject matter experts, or decline the engagement.
- For cloud services: understand the shared responsibility model and which controls are the FI's versus the CSP's.

### 2.3 Requirement C.3 — Review and Validation

> "The independent ESP shall review comprehensiveness of the risk assessment and validate adequacy of control measures implemented or to be implemented."

**What this means in practice:**

- The IESP performs **two distinct activities**:
  1. **Review** — assess whether the FI's own risk assessment is comprehensive (did they identify all relevant risks?)
  2. **Validate** — confirm that the control measures addressing those risks are adequate

- Controls may be "implemented" (already in place) or "to be implemented" (planned). Both are in scope, but the attestation posture differs.

**Practical guidance:**

- Obtain the FI's own risk assessment documentation first.
- Map the FI's identified risks against the Part D minimum controls — identify any gaps.
- For implemented controls: verify through evidence (configuration screenshots, logs, policies, walkthroughs, testing).
- For controls "to be implemented": review the implementation plan, timeline, and interim mitigations. These must be **clearly flagged** in the report as not yet implemented.
- Distinguish between design effectiveness (is the control designed properly?) and operating effectiveness (is it working as designed?).
- For pre-implementation assessments (e.g., cloud, new digital services), the focus is primarily on design effectiveness and planned controls.

### 2.4 Requirement C.4 — Report Content

> "The Risk Assessment Report (per Part D) shall state: scope of review, risk assessment methodology, summary of findings, and remedial actions (if any)."

**What this means in practice:**

The risk assessment report must contain four mandatory elements:

| Element | Description |
|---------|-------------|
| **Scope of review** | Clear statement of what was assessed, what was excluded, and why |
| **Risk assessment methodology** | How the IESP conducted the assessment (standards applied, tools used, sampling approach, rating scales) |
| **Summary of findings** | Key observations, both positive and negative, mapped to Part D controls |
| **Remedial actions** | For any gaps or weaknesses identified, what the FI has committed to do and by when |

**Practical guidance:**

- The scope statement must be precise enough that a reader can determine what was and was not assessed.
- Document the methodology before starting fieldwork and include it unchanged in the report.
- Findings should be structured by Part D control area, not by the order in which they were discovered.
- Every finding should have a risk rating (e.g., High / Medium / Low) with clear justification.
- Remedial actions must include owner, target date, and description — do not accept vague commitments.

### 2.5 Requirement C.5 — Negative Attestation

> "The Risk Assessment Report shall confirm there is no exception noted based on the prescribed risk areas (Negative attestation)."

**What this means in practice:**

- The IESP must provide a **negative attestation** — a statement that, based on the work performed, no exceptions were noted against the prescribed risk areas in Part D.
- This is the **most critical statement** in the entire report. It is the statement that BNM and the FI's board rely upon.
- If exceptions ARE noted, the attestation must clearly describe them.

**Practical guidance:**

- See Section 6 of this guide for detailed guidance on the three possible attestation outcomes.
- The attestation must cover every Part D control area — you cannot selectively omit areas.
- Use clear, unambiguous language. Do not hedge with qualifications that obscure the meaning.
- The attestation must be signed by the engagement lead (see Part A, Section 6).

### 2.6 Requirement C.6 — Accompanying Documentation

> "The FI shall provide the Risk Assessment Report accompanied by relevant documents."

**What this means in practice:**

- The FI (not the IESP) submits the report to BNM, accompanied by supporting documents.
- The IESP must ensure the report is **self-contained** enough to be understood without the supporting documents, but must reference what supporting documents exist.

**Practical guidance:**

- Provide the FI with a clear list of documents that should accompany the report submission.
- Typical accompanying documents include: engagement letter, scoping document, detailed findings workbook, evidence inventory, and the Part B confirmation letter.
- Retain your own copies of all evidence and working papers per your firm's retention policy.

---

## 3. Part D — Minimum Controls Assessment Guide

Part D defines the substantive control areas that the IESP must assess. It contains two main items:
- **Item 1** — Security requirements (applicable to all engagements)
- **Item 2** — Online transactions and services (applicable to digital/online service engagements)

The applicability of each item depends on the engagement type:

| Engagement Type | Item 1 (Security) | Item 2 (Online Transactions) |
|----------------|-------------------|------------------------------|
| DCRA | Yes | Typically no (unless DC hosts online services in scope) |
| NRA | Yes | Typically no (unless network supports online services in scope) |
| Cloud Services | Yes | Yes, if the cloud service delivers online/customer-facing services |
| Digital Services | Yes | Yes |
| Emerging Tech / AI | Yes | Yes, if the technology delivers online/customer-facing services |

### 3.1 Item 1 — Security Requirements

Item 1 prescribes six key security areas. These are aligned with ISO 27001/27002 domains but must be assessed in the context of the specific RMiT requirements.

---

#### 3.1.1 Item 1(a) — Access Control

**Regulatory expectation:** The FI must implement access controls that ensure only authorised individuals can access systems, data, and facilities relevant to the service or system under review.

**Assessment approach:**

1. **Policy and governance review:**
   - Obtain and review the FI's access control policy.
   - Confirm the policy covers logical access, privileged access, remote access, and service account management.
   - Verify the policy is approved, current, and communicated to relevant staff.

2. **User access management:**
   - Review user provisioning and de-provisioning processes.
   - Sample user access requests — verify proper authorisation, segregation of duties, and least-privilege principle.
   - Review access recertification records — confirm periodic reviews are conducted (at least annually for privileged users, at least semi-annually for critical systems).
   - Test for orphaned accounts (active accounts for departed employees).

3. **Privileged access management:**
   - Identify all privileged accounts (system administrators, database administrators, root/superuser).
   - Verify privileged access is restricted, logged, and monitored.
   - Confirm privileged access uses multi-factor authentication where technically feasible.
   - Review break-glass procedures for emergency access.

4. **Authentication mechanisms:**
   - Assess password policy enforcement (complexity, length, rotation, history).
   - Verify MFA implementation for remote access, privileged access, and critical systems.
   - Review session management (timeout, concurrent session limits).

**Key evidence to request:**
- Access control policy
- User access matrix / role-based access control documentation
- User provisioning/de-provisioning workflow
- Access recertification records (last two cycles)
- Privileged user list and justification
- PAM tool configuration and logs
- MFA configuration evidence
- Sample of user access request forms

**Red flags:**
- No periodic access recertification
- Shared privileged accounts without individual accountability
- No MFA on administrative access
- Active accounts for terminated staff
- Excessive privileged users with no business justification

---

#### 3.1.2 Item 1(b) — Physical and Environmental Security

**Regulatory expectation:** Physical and environmental controls must protect the infrastructure supporting the service or system from unauthorised physical access, environmental threats, and utility failures.

**Assessment approach:**

1. **Physical access controls:**
   - Review physical access control mechanisms (biometrics, card access, mantraps).
   - Verify visitor management procedures.
   - Review physical access logs — sample entries for anomalies.
   - Confirm physical access rights are reviewed periodically.

2. **Environmental controls:**
   - Verify fire detection and suppression systems (type, coverage, testing records).
   - Review HVAC/cooling system design and redundancy.
   - Assess water leak detection and mitigation.
   - Verify environmental monitoring (temperature, humidity) is in place with alerting.

3. **Power supply:**
   - Verify UPS capacity and runtime for critical systems.
   - Review generator capacity, fuel supply, and automatic transfer switch testing.
   - Confirm redundant power feeds where applicable.

4. **CCTV and monitoring:**
   - Verify CCTV coverage of all entry points and critical areas.
   - Confirm recording retention period meets policy requirements.
   - Review monitoring procedures (24/7 vs business hours).

**Key evidence to request:**
- Physical security policy
- Physical access logs (sample period)
- Visitor logs (sample period)
- Environmental monitoring dashboard/reports
- Fire suppression system test records
- UPS and generator test records
- CCTV system documentation and coverage maps

**Red flags:**
- Tailgating not prevented (no mantraps or anti-tailgating measures)
- Environmental monitoring without automated alerting
- No generator testing within the last 6 months
- CCTV blind spots in server rooms or network closets
- No visitor escort policy for sensitive areas

---

#### 3.1.3 Item 1(c) — Operations Security

**Regulatory expectation:** Operational procedures and responsibilities must be defined and managed to ensure secure operations of the technology environment.

**Assessment approach:**

1. **Operational procedures:**
   - Verify documented operating procedures for critical systems.
   - Review change management process (request, approval, testing, rollback, post-implementation review).
   - Assess patch management process (identification, prioritisation, testing, deployment, verification).

2. **Malware protection:**
   - Confirm anti-malware solutions are deployed on all endpoints and servers.
   - Verify signature updates are current and automatic.
   - Review malware incident logs for the assessment period.

3. **Backup and recovery:**
   - Review backup policy (frequency, retention, media, offsite storage).
   - Verify backup success/failure logs.
   - Confirm backup restoration testing is performed regularly (at least annually).

4. **Logging and monitoring:**
   - Verify security event logging is enabled on critical systems.
   - Confirm logs are centralised (SIEM or equivalent).
   - Review log retention policy and verify compliance.
   - Assess real-time monitoring and alerting capabilities.

5. **Vulnerability management:**
   - Review vulnerability scanning frequency and scope.
   - Assess vulnerability remediation SLAs and compliance.
   - Verify critical and high vulnerabilities are remediated within defined timelines.

**Key evidence to request:**
- Change management policy and sample change records
- Patch management policy and current patch status report
- Anti-malware deployment and update reports
- Backup policy, backup logs, and restoration test records
- SIEM/log management architecture and configuration
- Vulnerability scan reports (last two scans)
- Vulnerability remediation tracking

**Red flags:**
- Critical patches not applied within 30 days
- No backup restoration testing evidence
- Security logs not centralised or retained for insufficient duration
- Change management bypassed for "urgent" changes without retrospective review
- No vulnerability scanning programme

---

#### 3.1.4 Item 1(d) — Communication Security

**Regulatory expectation:** Network and information transfer security must be managed to protect information in transit and the supporting network infrastructure.

**Assessment approach:**

1. **Network security:**
   - Review network architecture and segmentation (DMZ, internal zones, management zone).
   - Verify firewall rule sets — assess for overly permissive rules ("any-any").
   - Confirm intrusion detection/prevention systems (IDS/IPS) are deployed and monitored.
   - Review network access control mechanisms.

2. **Data in transit:**
   - Verify encryption of data in transit (TLS 1.2+ for external, internal as risk-appropriate).
   - Review certificate management (validity, trusted CAs, renewal process).
   - Assess VPN configurations for remote access.

3. **Information transfer:**
   - Review policies for secure information exchange (email, file transfer, APIs).
   - Verify secure file transfer mechanisms for sensitive data.
   - Assess API security (authentication, authorisation, rate limiting, input validation).

**Key evidence to request:**
- Network architecture diagrams (logical and physical)
- Firewall rule sets and last review date
- IDS/IPS deployment and alert reports
- Encryption standards documentation
- TLS/SSL certificate inventory
- VPN configuration documentation
- API security standards and testing results

**Red flags:**
- Unencrypted data transfer over public networks
- Firewall rules not reviewed within the last 12 months
- TLS versions below 1.2 in use
- No network segmentation between production and non-production
- IDS/IPS alerts not reviewed or acted upon

---

#### 3.1.5 Item 1(e) — Information Security Incident Management

**Regulatory expectation:** A consistent and effective approach to managing information security incidents must be in place, including detection, reporting, response, and recovery.

**Assessment approach:**

1. **Incident management framework:**
   - Review the incident response policy and plan.
   - Verify incident classification and severity levels are defined.
   - Confirm roles and responsibilities are clearly assigned (incident commander, response team, communications lead).

2. **Detection and reporting:**
   - Assess detection capabilities (SIEM correlation rules, use cases, alert thresholds).
   - Verify internal escalation procedures and timelines.
   - Confirm BNM notification procedures align with RMiT requirements (major incidents must be reported to BNM within specified timelines).

3. **Response and recovery:**
   - Review incident response procedures for each severity level.
   - Verify forensic investigation capabilities (internal or contracted).
   - Assess evidence preservation procedures.
   - Review post-incident review process and lessons-learned documentation.

4. **Testing and exercises:**
   - Confirm incident response exercises are conducted at least annually.
   - Review results of the last exercise — verify identified gaps were remediated.
   - Assess tabletop exercises for plausible scenarios (ransomware, data breach, DDoS).

**Key evidence to request:**
- Incident response policy and plan
- Incident classification matrix
- Incident log for the assessment period
- Post-incident review reports (sample)
- Incident response exercise reports
- BNM notification procedures and templates
- SIEM use case catalogue

**Red flags:**
- No documented incident response plan
- No incident response exercise conducted in the past 12 months
- BNM notification procedures not aligned with RMiT timelines
- No post-incident review process
- Incident logs showing unresolved or unclassified incidents

---

#### 3.1.6 Item 1(f) — Information Security Aspects of Business Continuity Management

**Regulatory expectation:** Information security must be embedded in the FI's business continuity management framework to ensure the availability and integrity of systems during and after disruptive events.

**Assessment approach:**

1. **BCP integration:**
   - Verify information security is addressed in the BCP and disaster recovery plan (DRP).
   - Confirm recovery time objectives (RTO) and recovery point objectives (RPO) are defined for in-scope systems.
   - Assess alignment between stated RTOs/RPOs and actual DR capabilities.

2. **DR infrastructure:**
   - Review DR site capabilities (hot/warm/cold standby).
   - Verify data replication mechanisms and frequency.
   - Assess DR site security controls — should be equivalent to the primary site.

3. **Testing:**
   - Review DR test plans and results from the last 12 months.
   - Verify actual failover testing has been performed (not just tabletop).
   - Confirm testing covers all critical systems in scope.
   - Assess whether test results met RTO/RPO targets.

4. **Resilience:**
   - Assess single points of failure in the architecture.
   - Review high-availability configurations for critical components.
   - Verify automated failover mechanisms where applicable.

**Key evidence to request:**
- BCP and DRP documentation
- RTO/RPO definitions for critical systems
- DR architecture documentation
- DR test plans and results (last two tests)
- Data replication monitoring reports
- BIA (business impact analysis) documentation

**Red flags:**
- RTOs/RPOs not defined for in-scope systems
- No DR testing in the past 12 months
- DR test results showing failure to meet RTO/RPO targets with no remediation
- DR site security controls weaker than primary site
- No automated failover for critical systems

---

### 3.2 Item 2 — Online Transactions and Services

Item 2 applies when the assessment covers systems that deliver online or customer-facing transactional services. This includes internet banking, mobile banking, payment systems, e-wallet services, digital onboarding, and any customer-facing digital channel.

---

#### 3.2.1 Item 2(a) — Customer Identity Authentication

**Regulatory expectation:** The FI must implement robust customer identity authentication mechanisms that prevent unauthorised access, session compromise, and identity theft.

**Sub-item assessments:**

**(i) Prevention of session takeover and man-in-the-middle (MitM) attacks:**
- Verify anti-session-hijacking measures (secure cookies, session token rotation, IP binding where feasible).
- Confirm TLS is enforced end-to-end with no fallback to unencrypted connections.
- Assess certificate pinning implementation for mobile applications.
- Review HTTP security headers (HSTS, CSP, X-Frame-Options).

**(ii) Internal controls to prevent system, application, and database compromise:**
- Review hardening standards for web servers, application servers, and database servers.
- Verify input validation and output encoding to prevent injection attacks.
- Assess database access controls — confirm application service accounts use least privilege.
- Review code review and secure development lifecycle (SDLC) practices.

**(iii) Multi-level authentication, out-of-band verification, and real-time verification:**
- Verify MFA implementation for customer login (at minimum for high-risk transactions).
- Assess out-of-band verification channels (SMS OTP, push notification, hardware token).
- Review risk-based authentication / adaptive authentication capabilities.
- Confirm real-time fraud detection and transaction monitoring.

**(iv) Secure session handling and authentication databases:**
- Verify session timeout policies (idle and absolute timeouts).
- Confirm concurrent session controls.
- Assess authentication credential storage (hashing algorithms, salting).
- Review secure session token generation (CSPRNG, sufficient entropy).

**(v) Strong password and cryptographic implementation:**
- Verify password complexity requirements for customer-facing services.
- Assess cryptographic algorithms and key lengths in use.
- Confirm key management practices (generation, storage, rotation, destruction).
- Verify no deprecated or weak algorithms are in use (MD5, SHA-1, DES, RC4).

**Key evidence to request:**
- Authentication architecture documentation
- MFA implementation documentation
- Session management configuration
- Cryptographic standards policy
- VAPT report for web/mobile applications
- Secure SDLC documentation

---

#### 3.2.2 Item 2(b) — Transaction Authentication for Non-Repudiation

**Regulatory expectation:** Transaction authentication must provide proof of origin, integrity, and delivery to ensure non-repudiation.

**Sub-item assessments:**

**(i) Proof of origin, content, and integrity:**
- Verify transaction signing mechanisms (digital signatures, HMAC).
- Assess transaction integrity checks (hash verification, tamper detection).
- Confirm transaction records include origin metadata (timestamp, source IP, device fingerprint).

**(ii) Secure delivery channel:**
- Verify transaction confirmations are delivered through secure channels.
- Assess email/SMS notification security (avoid including sensitive details in notifications).
- Confirm delivery acknowledgement mechanisms where applicable.

**(iii) Alert user for further authentication on certain transactions:**
- Verify step-up authentication for high-value or unusual transactions.
- Assess transaction rules that trigger additional verification (threshold amounts, new payees, overseas transfers).
- Review customer notification for security-sensitive account changes (password reset, contact details change, device registration).

**(iv) Mutual authentication and digital certification:**
- Verify server certificate validation by client applications.
- Assess mutual TLS implementation for API-to-API communication.
- Confirm digital certificate management (issuance, revocation, OCSP/CRL checking).

**Key evidence to request:**
- Transaction authentication architecture
- Non-repudiation mechanism documentation
- Step-up authentication rules and configuration
- Digital certificate inventory and management procedures
- Transaction notification configuration

---

#### 3.2.3 Item 2(c) — Segregation of Duties and Access Control

**Regulatory expectation:** Segregation of duties and access controls must prevent any single individual from having the ability to initiate, approve, and execute transactions without independent oversight.

**Sub-item assessments:**

**(i) Dual control:**
- Verify maker-checker controls for high-value or high-risk transactions.
- Assess dual control requirements for system configuration changes.
- Confirm dual control for key management operations.

**(ii) Detect and prevent unauthorised access:**
- Review real-time access monitoring and alerting.
- Verify anomalous access detection capabilities (unusual times, locations, patterns).
- Assess account lockout and brute-force protection mechanisms.

**(iii) Tamper-resistant authorisation database:**
- Verify database integrity controls (checksums, audit triggers).
- Assess database access logging and monitoring.
- Confirm database encryption (at rest and in transit).
- Review database backup and recovery procedures.

**(iv) Periodic review of privileged users:**
- Verify frequency and thoroughness of privileged access reviews.
- Confirm reviews cover both internal staff and vendor/contractor accounts.
- Assess remediation of access issues identified during reviews.

**Key evidence to request:**
- Segregation of duties matrix
- Maker-checker configuration evidence
- Privileged access review records
- Database security configuration
- Access monitoring and alerting configuration

---

#### 3.2.4 Item 2(d) — Data Integrity

**Regulatory expectation:** The FI must maintain the integrity, confidentiality, and availability of transaction data through encryption, network security, and monitoring controls.

**Sub-item assessments:**

**(i) End-to-end encryption:**
- Verify encryption from the customer device to the backend processing system.
- Assess encryption protocols and cipher suites in use.
- Confirm no decryption/re-encryption at intermediate points without justification.

**(ii) Multi-layer network security:**
- Review defence-in-depth architecture (WAF, IPS, firewall, network segmentation).
- Verify each layer is independently managed and monitored.
- Assess lateral movement prevention between network zones.

**(iii) No single points of failure:**
- Verify high-availability configuration for transaction processing systems.
- Assess load balancing and failover mechanisms.
- Confirm redundancy at each architectural layer.

**(iv) Network security assessment and penetration testing:**
- Verify annual (at minimum) penetration testing of online transaction systems.
- Review penetration test scope — confirm it covers external, internal, and application layers.
- Assess remediation of findings from the last penetration test.
- Confirm pen testing is performed by qualified, independent testers.

**(v) Audit trail capabilities:**
- Verify comprehensive transaction audit trails (who, what, when, where).
- Confirm audit logs are tamper-resistant (centralised, integrity-protected).
- Assess audit log retention period (regulatory minimum and FI policy).

**(vi) Preserve confidentiality:**
- Verify data classification and handling procedures for transaction data.
- Assess data masking/tokenisation for sensitive fields (card numbers, account numbers).
- Confirm PCI DSS compliance where applicable.

**(vii) Stronger authentication for higher-risk transactions:**
- Verify risk-based transaction scoring.
- Assess tiered authentication requirements (low-risk vs high-risk transactions).
- Confirm rules for transaction limits and step-up authentication thresholds.

**(viii) Timely notification to customers:**
- Verify real-time or near-real-time transaction notifications.
- Assess notification channels (push, SMS, email) and customer preferences.
- Confirm notifications include sufficient detail for customers to identify unauthorised transactions.

**Key evidence to request:**
- Encryption architecture documentation
- Network security architecture diagrams
- Penetration test reports (last two tests)
- Audit trail configuration and sample logs
- Data classification policy
- Transaction notification configuration

---

#### 3.2.5 Item 2(e) — Mobile Device Risks

**Regulatory expectation:** Where online services are delivered through mobile applications, additional controls must address risks specific to the mobile platform.

**Sub-item assessments:**

**(i) Secure mobile operating system:**
- Verify the application enforces minimum OS version requirements.
- Assess the app's behaviour on outdated or unsupported OS versions.

**(ii) Not running on compromised devices:**
- Verify jailbreak/root detection is implemented and enforced.
- Assess the response when a compromised device is detected (block, warn, limit functionality).
- Confirm detection mechanisms are current and cover known bypass techniques.

**(iii) Penetration testing for mobile:**
- Verify dedicated mobile application penetration testing is conducted (not just web-based testing).
- Assess coverage of OWASP Mobile Top 10 risks.
- Review mobile-specific findings (insecure data storage, insecure communication, reverse engineering protection).

**(iv) Secure end-to-end communication:**
- Verify certificate pinning implementation.
- Assess TLS configuration for mobile API endpoints.
- Confirm no sensitive data is transmitted via insecure channels (HTTP, custom protocols without encryption).

**(v) Sensitive information not stored on devices:**
- Verify no sensitive data (passwords, PINs, tokens, account numbers) is stored in plaintext on the device.
- Assess use of secure storage mechanisms (Keychain, Keystore).
- Review application data caching and logging behaviour.

**(vi) Notify successful transactions:**
- Verify real-time push notifications for completed transactions.
- Confirm notifications are sent through channels independent of the transaction channel where feasible.

**(vii) Notify suspicious transactions:**
- Verify alerting for transactions flagged as suspicious by fraud detection systems.
- Assess customer response options (confirm, deny, block) within the notification flow.

**(viii) Monitor and takedown fake apps:**
- Verify the FI actively monitors app stores for fraudulent or impersonating applications.
- Assess the takedown process and typical response time.
- Confirm monitoring covers major app stores (Google Play, Apple App Store) and third-party repositories.

**(ix) Controls over app distribution platforms:**
- Verify the official application is only distributed through authorised channels.
- Assess measures to prevent sideloading or unauthorised distribution.
- Confirm app integrity verification mechanisms (code signing).

**(x) Unique code per transaction:**
- Verify transaction authorisation codes are unique, unpredictable, and time-bound.
- Assess OTP generation mechanisms (TOTP, HOTP, challenge-response).
- Confirm codes cannot be reused or intercepted.

**(xi) Timely expiry of transaction code:**
- Verify OTP/transaction code expiry periods are appropriate (typically 60–180 seconds).
- Confirm expired codes are rejected by the system.
- Assess rate-limiting on code validation attempts.

**Key evidence to request:**
- Mobile application security architecture
- Mobile penetration test reports
- Jailbreak/root detection implementation documentation
- App store monitoring reports and takedown records
- Mobile-specific security configuration documentation
- OTP mechanism documentation

---

## 4. Part A — Risk Assessment Report Production Guide

Part A prescribes the format of the Risk Assessment Report. The report has six mandatory sections. The IESP must ensure every section is completed, as BNM will review submissions for compliance with this format.

### 4.1 Section 1 — Financial Institution Details

**Content required:**
- Full legal name of the financial institution
- BNM licence category (commercial bank, Islamic bank, investment bank, insurer, takaful operator, payment system operator, etc.)
- Registered address
- Contact person (name, title, phone, email)

**Practical notes:**
- Verify all details with the FI before finalising. Inaccurate details may delay BNM processing.
- Use the FI's full legal name as registered with BNM, not trading names or abbreviations.

### 4.2 Section 2 — External Service Provider Details

**Content required:**
- Full legal name of the IESP firm
- Business registration number
- Registered address
- Engagement lead (name, title, professional qualifications, phone, email)
- Key team members and their roles

**Practical notes:**
- Include relevant professional certifications of the engagement lead (CISA, CISSP, ISO 27001 Lead Auditor, etc.).
- If the engagement involves sub-contracted specialists, disclose this in Section 2.

### 4.3 Section 3 — Detail of Application

**Content required:**
This section has two sub-components, each approximately **200 words**:

1. **Business case:** Why the FI is implementing or operating this service/system. This should articulate the business objectives, target customers, expected volumes, and strategic alignment.

2. **Technology description:** What the technology is, how it works, key components, deployment model, and significant third-party dependencies.

**Practical notes:**
- The 200-word guidance is approximate — prioritise clarity over word count.
- The business case should be written from the FI's perspective (the IESP may draft it, but the FI must own the content).
- The technology description should be written at a level that a technically literate regulator can understand — avoid excessive jargon.
- For cloud services: include the cloud service model (IaaS/PaaS/SaaS), deployment model (public/private/hybrid), and CSP identity.
- For emerging technology: include the specific technology type (AI/ML, blockchain, RPA, etc.) and its application.

### 4.4 Section 4 — Technology Risk Assessment

**Content required:**
This is the substantive body of the report. Per the regulation, the IESP *"shall provide assurance on the effectiveness of technology risk control and mitigation performed by the financial institution in meeting expectations outlined in Part D of this Appendix and paragraph 17.1 (for cloud services and emerging technology)."*

**Practical notes:**

Structure this section as follows:

1. **Scope of review** — precise description of what was assessed
2. **Risk assessment methodology** — standards and approach applied
3. **Assessment period** — dates of fieldwork
4. **Summary of findings by control area:**
   - For each Part D control area, provide:
     - Control area reference (e.g., "Item 1(a) — Access Control")
     - Assessment scope within this area
     - Key observations (positive and negative)
     - Finding details (if any exceptions)
     - Risk rating for each finding
     - Remedial actions agreed with the FI
5. **Overall assessment outcome** — aggregated view of the control environment

- Use a consistent findings template across all control areas.
- Findings should distinguish between design deficiencies and operating deficiencies.
- For pre-implementation assessments, note that operating effectiveness cannot be assessed and state this limitation.
- Cross-reference findings to specific RMiT clauses where possible.

### 4.5 Section 5 — Quality Assurance

**Content required:**
- Overall recommendation: whether the technology risk controls are adequate for the proposed or existing service.
- Any conditions or qualifications to the recommendation.
- The negative attestation statement (see Section 6 of this guide).

**Practical notes:**
- This section should be concise — one to two pages maximum.
- The overall recommendation must be one of: Adequate, Adequate with Conditions, or Not Adequate.
- Quality assurance also encompasses the IESP's internal review process — confirm that the report has been subject to an independent quality review within the firm.

### 4.6 Section 6 — Authorised Signatory

**Content required:**
- Name, title, and qualifications of the authorised signatory
- Signature
- Date
- Firm name and stamp

**Practical notes:**
- The signatory must be the engagement lead or a partner/director of the IESP firm with authority to sign on the firm's behalf.
- The signatory takes personal and professional accountability for the content of the report.
- Verify your firm's internal policies on signing authority before finalising.

---

## 5. Part B — Confirmation Support

Part B is the FI's own document — a confirmation letter signed by the Chairman of the Board, CISO, or designated senior management. The IESP does not sign this document, but plays a critical supporting role.

### 5.1 The Nine Confirmation Points

The FI must confirm all nine points. The IESP's role is to ensure the FI can substantiate each one:

| # | Confirmation Point | IESP Supporting Activity |
|---|-------------------|-------------------------|
| 1 | Consistent with strategic and business plans | Review the FI's strategic plan and verify alignment. Ensure this is documented in Section 3 of the report. |
| 2 | Board understands and is ready to assume RMiT roles and responsibilities | Verify board deliberation minutes. Confirm board has been briefed on technology risks and governance requirements. |
| 3 | Risk management process subject to board/senior management oversight | Review risk management governance structure. Confirm reporting lines and escalation procedures. |
| 4 | Appropriate security measures in place | This is directly validated by the Part D assessment. Reference the report findings. |
| 5 | Customer support services and education in place | Review customer support arrangements, FAQs, user guides, and customer communication plans. |
| 6 | Performance monitoring established | Verify SLA monitoring, KPI dashboards, and performance reporting mechanisms. |
| 7 | Included in contingency and BCP plans | Cross-reference with Item 1(f) assessment. Verify the service/system is included in BCP/DRP scope. |
| 8 | Adequate resources to support | Review staffing plans, training programmes, and resource allocation for ongoing operations. |
| 9 | Systems, procedures, security measures will be constantly reviewed | Verify ongoing monitoring, periodic review schedule, and continuous improvement framework. |

### 5.2 Practical Guidance for IESP

- **Do not draft the confirmation letter for the FI.** The FI must own this document. You may provide the template (see `templates/confirmation-letter.md`) and explain what each point means, but the FI must prepare and sign it.
- **Do raise concerns** if the IESP assessment reveals that the FI cannot substantiate a confirmation point. For example, if Item 1(f) assessment shows inadequate BCP, alert the FI that point 7 may be difficult to confirm.
- **Document your advisory role** — note in your working papers that you explained the confirmation requirements to the FI and any concerns raised.

---

## 6. Negative Attestation — The Three Outcomes

The negative attestation is the central deliverable of every IESP engagement. It follows a "negative assurance" model: the IESP states that nothing came to its attention to indicate non-compliance, rather than positively asserting compliance.

### 6.1 Outcome 1 — Clean Attestation (No Exceptions)

**When to issue:** The assessment identified no exceptions against the prescribed risk areas in Part D.

**Suggested wording:**

> "Based on the procedures performed and the evidence obtained, nothing has come to our attention that causes us to believe that the technology risk controls implemented by [FI name] in respect of [service/system name] do not meet the expectations outlined in Part D of Appendix 7 of BNM's Risk Management in Technology policy [and paragraph 17.1, where applicable]."

**Practical notes:**
- This is the ideal outcome. It does not mean zero findings — minor observations that do not represent control failures may exist.
- Minor observations should still be reported in Section 4 but are not treated as exceptions.
- Clearly distinguish between observations (informational, best-practice recommendations) and exceptions (control failures or gaps against Part D requirements).

### 6.2 Outcome 2 — Attestation with Exceptions

**When to issue:** The assessment identified one or more exceptions against Part D requirements, but the exceptions are specific and manageable — the FI has committed to remediation with a credible plan and timeline.

**Suggested wording:**

> "Based on the procedures performed and the evidence obtained, nothing has come to our attention that causes us to believe that the technology risk controls implemented by [FI name] in respect of [service/system name] do not meet the expectations outlined in Part D of Appendix 7 of BNM's Risk Management in Technology policy [and paragraph 17.1, where applicable], except for the matters described in [Section X] of this report."

**Practical notes:**
- Each exception must be clearly described with risk rating, impact assessment, and agreed remedial action.
- The FI and IESP must discuss whether BNM will accept the submission with exceptions — this is ultimately the FI's decision.
- For pre-implementation assessments: exceptions may relate to controls "to be implemented" — ensure timelines are realistic and the FI accepts accountability.
- Consider recommending a follow-up review to verify remediation.

### 6.3 Outcome 3 — Adverse Attestation

**When to issue:** The assessment identified pervasive or critical exceptions that fundamentally undermine the adequacy of the technology risk control environment. The IESP cannot provide even a qualified negative attestation.

**Suggested wording:**

> "Based on the procedures performed and the evidence obtained, we have identified significant deficiencies in the technology risk controls implemented by [FI name] in respect of [service/system name] that, in our assessment, do not meet the expectations outlined in Part D of Appendix 7 of BNM's Risk Management in Technology policy [and paragraph 17.1, where applicable]. The details of these deficiencies are described in [Section X] of this report. We are unable to provide a negative attestation at this time."

**Practical notes:**
- An adverse outcome is serious. It typically means the FI should not proceed with the service/system launch or must undertake significant remediation before resubmission.
- Discuss with the FI early if the assessment is trending towards adverse — do not surprise them in the final report.
- The FI may choose not to submit an adverse report to BNM and instead remediate first, then engage the IESP for a reassessment.
- Document your communications with the FI regarding the adverse outcome.

---

## 7. Supplementary Assessment Considerations

### 7.1 Cloud Services — Additional Requirements (Paragraph 17.1)

When the assessment scope includes cloud services, Part D controls must be supplemented with the requirements of paragraph 17.1. Key additional considerations include:

- Cloud service provider due diligence and risk assessment
- Data residency and sovereignty (Malaysian data must remain accessible to BNM)
- Shared responsibility model — clarity on which controls are the FI's vs the CSP's
- Contractual protections (audit rights, incident notification, exit provisions)
- Concentration risk assessment
- Subcontracting and fourth-party risk

Refer to `requirements/cloud-pre-implementation.md` for the detailed cloud assessment requirements.

### 7.2 Emerging Technology — Additional Requirements (Paragraph 17.1)

For emerging technology assessments (AI, blockchain, RPA, etc.), additional considerations include:

- Technology maturity assessment
- Ethical and fairness considerations (particularly for AI/ML models)
- Explainability and auditability of automated decisions
- Model risk management
- Data quality and bias assessment

Refer to `requirements/emerging-tech-review.md` for detailed requirements.

### 7.3 Engagement-Specific Scoping

While Appendix 7 is universal, the depth of assessment for each Part D control area varies by engagement type:

| Control Area | DCRA Focus | NRA Focus | Cloud Focus | Digital Focus |
|-------------|-----------|-----------|-------------|---------------|
| 1(a) Access control | DC physical & logical | Network device access | IAM in cloud, CSP admin | Customer & admin access |
| 1(b) Physical/environmental | Primary focus | Network facilities | CSP facilities (SOC2/ISO) | Hosting facilities |
| 1(c) Operations security | DC operations | Network operations | Cloud operations, DevOps | App operations |
| 1(d) Communication security | DC interconnects | Primary focus | Cloud connectivity | API & channel security |
| 1(e) Incident management | DC incidents | Network incidents | Cloud incidents, shared | Security incidents |
| 1(f) BCP/DR | DC resilience | Network resilience | Cloud DR, multi-region | Service continuity |
| 2(a)–2(e) Online transactions | N/A typically | N/A typically | If customer-facing | Primary focus |

---

## 8. Cross-References to Repository Documents

### 8.1 Requirements

| Document | Path | Relevance |
|----------|------|-----------|
| Regulatory Requirements | `requirements/regulatory-requirements.md` | All RMiT clauses triggering IESP engagement |
| Cloud Pre-Implementation | `requirements/cloud-pre-implementation.md` | Supplementary requirements for cloud assessments |
| DCRA Requirements | `requirements/dcra-requirements.md` | Detailed DCRA scope and methodology |
| NRA Requirements | `requirements/nra-requirements.md` | Detailed NRA scope and methodology |
| Emerging Tech Review | `requirements/emerging-tech-review.md` | AI and emerging technology assessment requirements |

### 8.2 Templates

| Document | Path | Relevance |
|----------|------|-----------|
| Risk Assessment Report | `templates/risk-assessment-report.md` | Template for the Part A report |
| Confirmation Letter | `templates/confirmation-letter.md` | Template for the Part B confirmation |
| Engagement Letter | `templates/engagement-letter.md` | Template for formalising the IESP engagement |
| Findings Report | `templates/findings-report.md` | Template for detailed findings |
| Board Deliberation Pack | `templates/board-deliberation-pack.md` | Pack supporting board deliberation of IESP outcomes |
| Scoping Document | `templates/scoping-document.md` | Engagement scoping template |
| Management Representation | `templates/management-representation.md` | FI management representation letter |

### 8.3 Audit Work Programs

| Document | Path | Relevance |
|----------|------|-----------|
| DCRA Work Program | `audit-work-programs/awp-dcra.md` | Step-by-step DCRA fieldwork programme |
| NRA Work Program | `audit-work-programs/awp-nra.md` | Step-by-step NRA fieldwork programme |
| Cloud Work Program | `audit-work-programs/awp-cloud.md` | Step-by-step cloud assessment programme |
| Digital Services Work Program | `audit-work-programs/awp-digital-services.md` | Step-by-step digital services assessment programme |
| AI/Emerging Tech Work Program | `audit-work-programs/awp-ai-emerging-tech.md` | Step-by-step emerging tech assessment programme |

### 8.4 Evidence and Scoping

| Document | Path | Relevance |
|----------|------|-----------|
| Evidence Requirements | `evidence/evidence-requirements.md` | General evidence collection guidance |
| Evidence Checklist — DCRA | `evidence/evidence-checklist-dcra.md` | DCRA-specific evidence checklist |
| Evidence Checklist — NRA | `evidence/evidence-checklist-nra.md` | NRA-specific evidence checklist |
| Evidence Checklist — Cloud | `evidence/evidence-checklist-cloud.md` | Cloud-specific evidence checklist |
| Evidence Checklist — Digital | `evidence/evidence-checklist-digital.md` | Digital services evidence checklist |
| Evidence Checklist — AI | `evidence/evidence-checklist-ai.md` | AI/emerging tech evidence checklist |
| Scoping Methodology | `scope/scoping-methodology.md` | How to scope an IESP engagement |

### 8.5 Controls

| Document | Path | Relevance |
|----------|------|-----------|
| Control Domains | `controls/control-domains.json` | Control domain taxonomy |
| Control Mapping | `controls/control-mapping.json` | Mapping of controls to RMiT clauses |

---

## 9. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-11 | IESP Framework Team | Initial release — Appendix 7 practitioner guide covering Parts A–D, negative attestation framework, and cross-references |
| | | | |
| | | | |

---

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document — *Risk Management in Technology (RMiT)*, November 2025 edition — for the authoritative and binding requirements.
