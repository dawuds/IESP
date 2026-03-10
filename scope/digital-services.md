# Digital Services Enhancement — Scope Definition

> BNM RMiT Nov 2025 — Scope Guidance for Digital Services IESP Engagements

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 16.4, 16.5 |
| **Trigger** | Prior to launching new or materially enhancing existing digital services |
| **Reporting** | Appendix 7 Part D |
| **Scope Controls** | Part D items 1a (access control), 2a-e (online transaction security, encryption, data integrity, mobile) |

## 2. What Constitutes a "Digital Service"

Per BNM RMiT, digital services include customer-facing technology services delivered through electronic channels:

| Service Type | Examples |
|-------------|----------|
| **Internet banking** | Web-based banking portal, account management, bill payment |
| **Mobile banking** | Native mobile application for banking services |
| **Digital payments** | QR payments, e-wallets, peer-to-peer transfers, DuitNow |
| **Digital onboarding** | eKYC, remote account opening, digital identity verification |
| **Open banking / API services** | Third-party API integrations, open banking platform |
| **Digital lending** | Online loan application, digital credit assessment |
| **Digital wealth / investment** | Robo-advisory, online investment platform |

## 3. Scope Determination Factors

| Factor | How to Determine |
|--------|-----------------|
| **Service type and channels** | Identify the digital service, its channels (web, mobile app, API), and target users (retail, corporate, third-party) |
| **New vs. enhancement** | Determine if this is a new service launch or a material enhancement to an existing service; both trigger IESP per 16.4 |
| **Materiality of enhancement** | For enhancements: does it change authentication, transaction flow, data handling, API exposure, or introduce new functionality? Material changes trigger IESP |
| **Technology stack** | Identify the technology components: front-end, back-end, APIs, databases, third-party services, hosting (on-premises, cloud) |
| **Integration points** | Map upstream and downstream integrations — core banking, payment switches, third-party APIs, CSPs |
| **Data sensitivity** | Identify what customer data is processed — PII, financial data, authentication credentials |
| **Threat landscape** | Identify the primary threat vectors for the service type (account takeover, fraud, data breach, API abuse) |

## 4. In-Scope Items

### 4.1 Mandatory In-Scope

| Item | Rationale |
|------|-----------|
| Customer authentication mechanisms | Part D item 1a — MFA, credential policy, session management |
| Online transaction security | Part D item 2 — transaction authentication, limits, fraud monitoring |
| Encryption (data in transit and at rest) | Part D item 2 — TLS configuration, certificate management, key management |
| Data integrity controls | Part D item 2d — input validation, anti-replay, anti-tampering |
| Mobile application security (if mobile channel) | Part D item 2e — root detection, secure storage, code protection, RASP |
| API security (if APIs are exposed) | Part D item 2 — API authentication, rate limiting, input validation, OWASP API Top 10 |
| Security testing results (SAST, DAST, pen test) | 16.4 — pre-launch security assurance |
| Secure development lifecycle (SSDLC) | 16.4 — security-by-design evidence |

### 4.2 Conditionally In-Scope

| Item | Condition for Inclusion |
|------|------------------------|
| Digital identity verification (eKYC) | Include if the service involves remote customer onboarding or identity verification |
| Biometric authentication | Include if biometrics are used for login or transaction authorisation |
| Third-party API integrations | Include if the service relies on or exposes APIs to third parties (open banking, payment gateways) |
| Fraud detection and monitoring | Include the fraud monitoring rules and response; depth depends on whether this is a payment/transaction service |
| Privacy impact assessment | Include if the service processes personal data in new ways or extends data collection |
| Business continuity / availability | Include per 16.5 — availability targets, HA architecture, DR coverage |
| Cloud hosting controls | Include the cloud-side controls if the service is cloud-hosted; coordinate with Cloud IESP scope |

### 4.3 Typically Out-of-Scope (with justification)

| Item | Justification | Risk of Exclusion |
|------|--------------|-------------------|
| Network infrastructure underlying the service | Covered by NRA (14.2) | Low if NRA is current |
| Data centre physical infrastructure | Covered by DCRA (14.1) | Low if DCRA is current |
| Core banking system internals | Not a digital service component; covered by internal audit | Low |
| Non-customer-facing internal systems | Not digital services per 16.4 | Low |
| Third-party vendor security posture (beyond API integration) | Covered by third-party risk management (Appendix 8) | Moderate; include API-level controls |

## 5. Scoping by Service Type

### 5.1 Internet / Mobile Banking

| Focus Area | Priority | Key Concerns |
|-----------|----------|-------------|
| Authentication | Critical | MFA for login and transactions, session management, account lockout |
| Transaction security | Critical | Step-up authentication, transaction signing, fraud monitoring, limits |
| Mobile security | Critical | Root detection, secure storage, code protection, certificate pinning |
| Encryption | Critical | TLS 1.2+, HSTS, certificate management |
| API security | High | Backend API protection, OWASP API Top 10 |

### 5.2 Digital Payments (QR, e-Wallet, DuitNow)

| Focus Area | Priority | Key Concerns |
|-----------|----------|-------------|
| Transaction authentication | Critical | Transaction binding, anti-replay, non-repudiation |
| Fraud monitoring | Critical | Real-time fraud detection, velocity checks, anomaly detection |
| QR code security | High | QR code generation integrity, merchant verification, anti-tampering |
| Limits and controls | Critical | Transaction and daily limits, cooling-off periods for new payees |
| Reconciliation | High | Real-time reconciliation between channels and core systems |

### 5.3 Digital Onboarding (eKYC)

| Focus Area | Priority | Key Concerns |
|-----------|----------|-------------|
| Identity verification | Critical | Document validation, NFC chip, database checks, liveness detection |
| Fraud prevention | Critical | Device fingerprinting, velocity checks, duplicate detection |
| Privacy | High | Data minimisation, consent, retention, cross-border data |
| Audit trail | High | Full audit trail of verification steps and outcomes |

### 5.4 Open Banking / API Platform

| Focus Area | Priority | Key Concerns |
|-----------|----------|-------------|
| API security | Critical | OAuth 2.0, consent management, rate limiting, input validation |
| Third-party access | Critical | TPP registration, credential management, scope controls |
| Data sharing controls | Critical | Customer consent, data minimisation, purpose limitation |
| Monitoring | High | API usage monitoring, anomaly detection, SLA compliance |

## 6. Interaction with Other Assurance

| Other Engagement | Interaction | Boundary |
|-----------------|-------------|----------|
| **NRA (14.2)** | Network supporting the digital service | Digital Services covers application-layer security. NRA covers network resilience and security controls |
| **Cloud IESP (17.1)** | Cloud-hosted digital services | Digital Services covers the application security. Cloud IESP covers cloud governance, configuration, and operational controls |
| **DCRA (14.1)** | Physical hosting infrastructure | Digital Services does not cover DC physical infrastructure |
| **Penetration Testing** | Separate pen test engagement | Digital Services IESP reviews pen test results but does not typically perform the testing itself |

## 7. Scoping Checklist

- [ ] Identify the digital service (new launch or material enhancement)
- [ ] Document the service type, channels, and target users
- [ ] Obtain the technology stack and architecture documentation
- [ ] Map all integration points (core systems, third-party APIs, CSPs)
- [ ] Identify data types processed (PII, financial, authentication)
- [ ] Obtain threat model or threat assessment for the service
- [ ] Identify applicable Part D control items based on service type
- [ ] Determine if mobile channel is in scope (triggers Part D item 2e)
- [ ] Determine if API exposure is in scope (external APIs)
- [ ] Obtain security testing reports (SAST, DAST, pen test, API test)
- [ ] Review prior IESP findings for the same or similar service
- [ ] Identify interaction with NRA, DCRA, Cloud IESP
- [ ] Agree scope boundaries with the FI
- [ ] Document scope in scoping memorandum and obtain FI sign-off

## 8. Cross-References

| Document | Path |
|----------|------|
| Digital Services AWP | `/audit-work-programs/awp-digital-services.md` |
| Digital Services Evidence Checklist | `/evidence/evidence-checklist-digital.md` |
| Scoping Methodology | `/scope/scoping-methodology.md` |
| Risk Assessment Report Template | `/templates/risk-assessment-report.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
