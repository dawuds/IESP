# Digital Services Enhancement — Evidence Checklist

## Digital Services Security Assessment — Evidence Requirements (Appendix 7 Part D)

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

---

**Engagement Reference:** [Reference Number]

**Financial Institution:** [FI Name]

**Digital Service in Scope:** [Service name, type, channels]

**Assessment Period:** [Start Date] to [End Date]

---

## Instructions

This checklist maps evidence requirements to the Digital Services Enhancement IESP assessment per BNM RMiT paragraphs 16.4 and 16.5, aligned with Appendix 7 Part D control items. Status: [ ] = Not obtained, [P] = Partial, [X] = Obtained.

---

## 1. Service Specification and Architecture

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 1.1 | Digital service specification (scope, functionality, target users, channels) | 16.4 | FI | Document | Required | [ ] |
| 1.2 | Technology stack and architecture documentation | 16.4 | FI | Document / diagram | Required | [ ] |
| 1.3 | Security architecture and design document | 16.4 | FI | Document / diagram | Required | [ ] |
| 1.4 | Integration point mapping (upstream/downstream systems, third-party services) | 16.4 | FI | Diagram / document | Required | [ ] |
| 1.5 | Data flow diagrams showing sensitive data paths | 16.4 | FI | Diagram | Required | [ ] |
| 1.6 | Threat model for the digital service | 16.4 | FI | Document | Required | [ ] |

---

## 2. Access Control and Authentication (Part D item 1a, 2a-c)

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 2.1 | Authentication mechanism design (password, OTP, biometric, device binding) | Part D 1a | FI | Document | Required | [ ] |
| 2.2 | Multi-factor authentication (MFA) configuration for login and high-risk transactions | Part D 2a | FI | Configuration / screenshot | Required | [ ] |
| 2.3 | Password/credential policy (complexity, history, expiry, lockout) | Part D 1a | FI | Policy document | Required | [ ] |
| 2.4 | Session management configuration (token generation, timeout, concurrent sessions) | Part D 2c | FI | Configuration | Required | [ ] |
| 2.5 | Account lockout and rate limiting configuration | Part D 1a | FI | Configuration | Required | [ ] |
| 2.6 | CAPTCHA or bot protection implementation | Part D 1a | FI | Configuration / screenshot | Desirable | [ ] |
| 2.7 | Digital identity verification (eKYC) process documentation (if applicable) | Part D 1a | FI | Document | Conditional | [ ] |
| 2.8 | Liveness detection configuration for biometric verification | Part D 1a | FI / Vendor | Configuration | Conditional | [ ] |
| 2.9 | Authorisation model (RBAC/ABAC) documentation | Part D 1a | FI | Document | Required | [ ] |
| 2.10 | Role-to-function mapping | Part D 1a | FI | Matrix | Required | [ ] |

---

## 3. Online Transaction Security (Part D item 2)

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 3.1 | Transaction authentication mechanism design (TAC, OTP, biometric, transaction signing) | Part D 2 | FI | Document | Required | [ ] |
| 3.2 | Step-up authentication configuration for high-risk transactions | Part D 2 | FI | Configuration | Required | [ ] |
| 3.3 | Transaction confirmation flow documentation | Part D 2 | FI | Document / screenshots | Required | [ ] |
| 3.4 | Transaction limit configuration (daily, per-transaction, cumulative) | Part D 2 | FI | Configuration | Required | [ ] |
| 3.5 | Fraud monitoring rules and detection mechanisms | Part D 2 | FI | Rule set / document | Required | [ ] |
| 3.6 | Sample fraud alert records and investigation logs | Part D 2 | FI | Records | Required | [ ] |
| 3.7 | Anti-replay mechanism design (nonce, timestamp, sequence number) | Part D 2d | FI | Document | Required | [ ] |
| 3.8 | Duplicate transaction detection configuration | Part D 2 | FI | Configuration | Required | [ ] |
| 3.9 | Non-repudiation mechanism for critical transactions | Part D 2 | FI | Document | Required | [ ] |
| 3.10 | Transaction audit trail — sample records showing who, what, when, from where | Part D 2 | FI | Records | Required | [ ] |

---

## 4. Encryption and Data Protection

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 4.1 | TLS configuration (version, cipher suites) — SSL Labs test or equivalent | Part D 2 | FI | Report | Required | [ ] |
| 4.2 | Certificate details (CA, validity, hostname match) | Part D 2 | FI | Certificate / report | Required | [ ] |
| 4.3 | HSTS configuration | Part D 2 | FI | Configuration | Required | [ ] |
| 4.4 | Certificate pinning configuration for mobile applications | Part D 2e | FI | Configuration | Conditional | [ ] |
| 4.5 | Mutual TLS (mTLS) configuration for B2B API integrations | Part D 2 | FI | Configuration | Conditional | [ ] |
| 4.6 | Data-at-rest encryption for sensitive data | Part D 2d | FI | Configuration | Required | [ ] |
| 4.7 | Key management procedures and controls | Part D 2 | FI | Document | Required | [ ] |

---

## 5. Mobile Application Security (Part D item 2e)

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 5.1 | Mobile application security architecture | Part D 2e | FI | Document | Required | [ ] |
| 5.2 | Root/jailbreak detection configuration and response | Part D 2e | FI | Configuration | Required | [ ] |
| 5.3 | Local data storage review (keychain/keystore usage, no plaintext) | Part D 2e | FI / Tester | Report | Required | [ ] |
| 5.4 | Code obfuscation and anti-tampering evidence | Part D 2e | FI | Configuration / report | Required | [ ] |
| 5.5 | Data leakage assessment (logs, screenshots, clipboard) | Part D 2e | FI / Tester | Report | Required | [ ] |
| 5.6 | App store distribution evidence (official stores only) | Part D 2e | FI | Screenshot | Required | [ ] |
| 5.7 | Minimum version enforcement and forced update mechanism | Part D 2e | FI | Configuration | Required | [ ] |
| 5.8 | Runtime application self-protection (RASP) configuration | Part D 2e | FI / Vendor | Configuration | Desirable | [ ] |
| 5.9 | Anti-debugging and emulator detection configuration | Part D 2e | FI | Configuration | Desirable | [ ] |
| 5.10 | Device binding/registration mechanism | Part D 2e | FI | Document | Required | [ ] |

---

## 6. API Security

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 6.1 | API documentation (endpoints, methods, authentication) | Part D 2 | FI | Document | Required | [ ] |
| 6.2 | API authentication configuration (OAuth 2.0, API keys, mTLS) | Part D 2 | FI | Configuration | Required | [ ] |
| 6.3 | API rate limiting and throttling configuration | Part D 2 | FI | Configuration | Required | [ ] |
| 6.4 | API gateway security configuration | Part D 2 | FI | Configuration | Required | [ ] |
| 6.5 | OWASP API Security Top 10 assessment results | Part D 2 | FI / Tester | Report | Required | [ ] |
| 6.6 | Input validation and output encoding implementation evidence | Part D 2d | FI | Configuration / code review | Required | [ ] |

---

## 7. Application Security Testing

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 7.1 | Security testing scope and plan | 16.4 | FI / Tester | Document | Required | [ ] |
| 7.2 | Static application security testing (SAST) report | 16.4 | FI / Tester | Report | Required | [ ] |
| 7.3 | Dynamic application security testing (DAST) report | 16.4 | FI / Tester | Report | Required | [ ] |
| 7.4 | Penetration test report (web application) | 16.4 | Tester | Report | Required | [ ] |
| 7.5 | Penetration test report (mobile application, if applicable) | 16.4 | Tester | Report | Conditional | [ ] |
| 7.6 | API security testing report | 16.4 | Tester | Report | Required | [ ] |
| 7.7 | Infrastructure vulnerability assessment report | 16.4 | Tester | Report | Required | [ ] |
| 7.8 | Remediation evidence for high/critical findings | 16.4 | FI | Evidence pack | Required | [ ] |
| 7.9 | Tester qualifications and independence evidence | 16.4 | Tester | CV / certification | Required | [ ] |

---

## 8. Secure Development Lifecycle

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 8.1 | Secure software development lifecycle (SSDLC) documentation | 16.4 | FI | Document | Required | [ ] |
| 8.2 | Security requirements specification for the digital service | 16.4 | FI | Document | Required | [ ] |
| 8.3 | Secure coding standards | 16.4 | FI | Document | Required | [ ] |
| 8.4 | Code review or automated scanning records | 16.4 | FI | Records / reports | Required | [ ] |
| 8.5 | Security sign-off before production release | 16.4 | FI | Sign-off record | Required | [ ] |

---

## 9. Data Privacy and Protection

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 9.1 | Privacy impact assessment (PIA) for the digital service | 16.4 | FI | Document | Required | [ ] |
| 9.2 | Data collection inventory (what personal data is collected, purpose, legal basis) | 16.4 | FI | Inventory | Required | [ ] |
| 9.3 | Consent mechanism implementation evidence | 16.4 | FI | Screenshot / configuration | Required | [ ] |
| 9.4 | Data retention and deletion policy and enforcement | 16.4 | FI | Policy / configuration | Required | [ ] |
| 9.5 | Privacy notice for the digital service | 16.4 | FI | Document / screenshot | Required | [ ] |

---

## 10. Business Continuity and Availability

| # | Evidence Item | RMIT Ref | Source | Format | Criticality | Status |
|---|-------------|----------|--------|--------|-------------|--------|
| 10.1 | Availability targets for the digital service (SLA) | 16.5 | FI | Document | Required | [ ] |
| 10.2 | High availability architecture design (load balancing, auto-scaling, failover) | 16.5 | FI | Document / diagram | Required | [ ] |
| 10.3 | Monitoring and alerting configuration for service availability | 16.5 | FI | Configuration / dashboard | Required | [ ] |
| 10.4 | Disaster recovery plan covering the digital service | 16.5 | FI | Document | Required | [ ] |
| 10.5 | Most recent DR test results for the digital service | 16.5 | FI | Report | Required | [ ] |
| 10.6 | Incident response procedures specific to the digital service | 16.5 | FI | Document | Required | [ ] |

---

## Cross-References

| Document | Path |
|----------|------|
| Digital Services AWP | `/audit-work-programs/awp-digital-services.md` |
| Digital Services Scope | `/scope/digital-services.md` |
| Evidence Requirements Overview | `/evidence/evidence-requirements.md` |
| Findings Report Template | `/templates/findings-report.md` |
| Scoping Document Template | `/templates/scoping-document.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
