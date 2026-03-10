# Network Infrastructure — Scope Definition

> BNM RMiT Nov 2025 — Scope Guidance for NRA Engagements

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 14.2 |
| **Scope Clauses** | 10.36 (Network Design and Architecture), 10.37 (Network Resilience and Redundancy), 10.38 (Network Security Controls), 10.39 (Network Monitoring), 10.40 (Network Segmentation), 10.41 (Network Change Management), 10.42 (Network Logging), 10.43 (Network Incident Response) |

## 2. Scope Determination Factors

| Factor | How to Determine |
|--------|-----------------|
| **Network asset inventory** | Obtain the FI's network asset register — routers, switches (core, distribution, access), firewalls, load balancers, WAFs, IDS/IPS, DNS servers, VPN concentrators, wireless controllers/APs, SD-WAN devices |
| **Network domains** | Identify all network domains: core/backbone, data centre network, WAN (inter-site), internet edge, DMZ, wireless, remote access/VPN, cloud connectivity, branch/office networks |
| **System criticality** | Identify which network segments carry traffic for critical systems; all network paths for critical systems are mandatory in scope |
| **Network topology** | Obtain logical and physical network topology diagrams to understand the network architecture |
| **Third-party managed services** | Identify network services managed by third parties (managed firewall, managed SD-WAN, MSSP, ISP-managed services) |
| **Material changes** | Identify network changes since the last NRA (topology redesign, new segments, SD-WAN migration, cloud connectivity, security control changes) |
| **Sites and locations** | Identify all sites connected to the FI's network (headquarters, branches, DCs, DR sites, remote offices) |

## 3. In-Scope Items

### 3.1 Mandatory In-Scope

| Item | Rationale |
|------|-----------|
| Core/backbone network | Foundation of all network connectivity; failure impacts all services |
| Data centre network (logical layer) | Supports all DC-hosted critical systems; segmentation and resilience critical |
| Internet edge and DMZ | Highest threat exposure; customer-facing services, attack surface |
| WAN links between critical sites | Inter-site connectivity for critical operations; redundancy essential |
| Firewalls (all tiers) | Primary security control; rule management, architecture, HA |
| IDS/IPS | Threat detection; deployment coverage, signature currency, tuning |
| Network design and architecture (10.36) | Regulatory requirement; architecture must support HA and defence in depth |
| Network resilience and redundancy (10.37) | Regulatory requirement; component redundancy, path diversity, failover |
| Network security controls (10.38) | Regulatory requirement; firewall, IDS/IPS, WAF, DDoS, VPN, wireless, email security |
| Network monitoring (10.39) | Regulatory requirement; real-time monitoring, alerting, 24/7 coverage |
| Network segmentation (10.40) | Regulatory requirement; zone separation, DMZ, production/non-production, third-party isolation |
| Network change management (10.41) | Regulatory requirement; change process, risk assessment, rollback, configuration management |
| Network logging (10.42) | Regulatory requirement; comprehensive logging, integrity, retention, review |
| Network incident response (10.43) | Regulatory requirement; IR procedures, DDoS playbook, forensic capability |

### 3.2 Conditionally In-Scope

| Item | Condition for Inclusion |
|------|------------------------|
| Wireless network (Wi-Fi) | Include if wireless carries corporate traffic, connects to production networks, or covers sensitive areas. Exclude guest-only Wi-Fi that is fully isolated |
| VPN / remote access infrastructure | Include if remote access is used by staff or third parties to access critical systems |
| SD-WAN overlay | Include if SD-WAN manages connectivity for critical sites or replaces traditional WAN |
| Cloud connectivity (Direct Connect, ExpressRoute, Cloud Interconnect) | Include the network path from FI to cloud edge; cloud-side networking is covered by Cloud assessment |
| API gateway infrastructure | Include if API gateways handle external-facing APIs for digital services |
| Email security infrastructure | Include if email is a critical communication channel and email-borne threats are a significant risk vector |
| DNS infrastructure | Include internal and external DNS; DNS failure can cause wide-spread service disruption |
| Branch/office networks | Include a representative sample of branch networks; full coverage may be impractical for large branch networks |
| Load balancers | Include if they front critical services; HA configuration and security are key |
| Network management infrastructure (NMS, SNMP, jump hosts) | Include if compromise of management infrastructure could enable lateral movement across the network |

### 3.3 Typically Out-of-Scope (with justification required)

| Item | Justification for Exclusion | Risk of Exclusion |
|------|---------------------------|-------------------|
| Physical network cabling within data centres | Covered by DCRA (physical infrastructure). NRA covers logical network design | Low if DCRA is current |
| Application-layer security (beyond WAF/API gateway) | Covered by Digital Services or application security assessments | Low if other assessments are current |
| Endpoint security (desktop, laptop, mobile) | Covered by endpoint security assessment or internal audit | Moderate; endpoints connect to the network but are not network infrastructure |
| Telephony/voice network (traditional PBX) | Unless converged with data network (VoIP) | Low for isolated telephony; include VoIP |
| IoT device networks | Unless IoT is connected to the FI's production network; IoT device security covered by Emerging Tech | Moderate if IoT devices are on the network |
| CSP internal network (AWS/Azure/GCP backbone) | FI does not control CSP internal networking; covered by CSP certifications | Low if Cloud assessment is performed |

## 4. Key Areas to Assess

### 4.1 By RMIT Paragraph

| Paragraph | Key Assessment Focus |
|-----------|---------------------|
| **10.36 — Design and Architecture** | Architecture supports HA, defence in depth, security-by-design; documentation is current and accurate; design accommodates growth; management/production/user traffic separation |
| **10.37 — Resilience and Redundancy** | Component redundancy (core switches, routers, firewalls in HA), path diversity (WAN, internet), carrier diversity, failover capability and testing, DNS resilience, load balancing |
| **10.38 — Security Controls** | Firewall architecture and rule management, IDS/IPS deployment and tuning, WAF for internet-facing apps, DDoS protection (L3/L4 and L7), NAC, VPN security, wireless security, API gateway security, email security, DNS security |
| **10.39 — Monitoring** | Real-time monitoring coverage (all critical components), performance monitoring, SIEM integration, alerting thresholds and escalation, anomaly detection, 24/7 monitoring (NOC/SOC), third-party service monitoring |
| **10.40 — Segmentation** | Segmentation strategy, zone definitions, DMZ architecture, production/non-production separation, third-party isolation, microsegmentation, inter-zone access controls, segmentation validation through testing |
| **10.41 — Change Management** | Change process, risk assessment, testing, rollback, emergency changes, configuration management/version control, SoD, change freeze policies |
| **10.42 — Logging** | Log sources and coverage, log integrity, retention, review processes, time synchronization (NTP), SIEM aggregation, privileged access logging, NetFlow/sFlow |
| **10.43 — Incident Response** | Network-specific IR procedures, DDoS response playbook, intrusion response, outage communication, SOC coordination, forensic capability, lessons learned |

### 4.2 Network Assessment by Domain

| Network Domain | Priority | Key Concerns |
|---------------|----------|-------------|
| **Core/backbone** | Critical | Redundancy, HA, capacity, single points of failure |
| **Data centre network** | Critical | Segmentation, east-west traffic controls, spine-leaf resilience |
| **Internet edge** | Critical | DDoS protection, firewall architecture, WAF, IDS/IPS |
| **DMZ** | Critical | Proper isolation from internal network, only necessary services exposed |
| **WAN** | Critical | Path diversity, carrier diversity, failover, bandwidth adequacy |
| **Cloud connectivity** | High | Redundant connections, encryption, routing security |
| **Remote access / VPN** | High | Authentication (MFA), encryption, split tunnelling policy, access controls |
| **Wireless** | Medium-High | WPA3, segmentation from production, rogue AP detection |
| **Branch network** | Medium | Standardised design, security controls, monitoring coverage |
| **Management network** | High | Isolation from production, access controls, logging |

## 5. Interaction with Other Assurance

| Other Engagement | Interaction | Boundary |
|-----------------|-------------|----------|
| **DCRA** | DC network infrastructure | NRA covers logical network design and security within the DC. DCRA covers physical infrastructure (cabling, physical switches as physical assets, cross-connects). The boundary is at the logical vs. physical layer |
| **Cloud Assessment** | Cloud connectivity and cloud-side networking | NRA covers the network path from FI to cloud edge (Direct Connect, ExpressRoute, VPN to cloud). Cloud assessment covers cloud-side networking (VPC, security groups, NACLs) |
| **Digital Services** | Network supporting digital services | NRA covers network resilience and security controls (firewall, WAF, DDoS). Digital Services covers application-layer security. API gateways may be assessed by both from different perspectives |
| **Penetration Testing** | Network penetration testing | NRA may include network vulnerability assessment. Full penetration testing is typically a separate engagement but NRA should review pen test results |

## 6. Scoping Checklist for NRA

- [ ] Obtain complete network asset inventory (all device types across all domains)
- [ ] Obtain logical and physical network topology diagrams
- [ ] Identify all network domains (core, DC, WAN, internet, wireless, cloud connectivity, VPN, branch)
- [ ] Map critical systems to network paths (which network segments carry critical traffic?)
- [ ] Identify third-party managed network services
- [ ] Identify material network changes since last NRA
- [ ] Identify all sites/locations connected to the network
- [ ] Determine which branch networks to sample (if large branch network)
- [ ] Review prior NRA scope and findings
- [ ] Identify interaction with DCRA and other IESP engagements
- [ ] Coordinate any active testing windows (vulnerability scanning, segmentation testing)
- [ ] Agree scope boundaries with the FI
- [ ] Document scope in scoping memorandum and obtain FI sign-off

## 7. Cross-References

| Document | Path |
|----------|------|
| NRA Requirements | `/requirements/nra-requirements.md` |
| NRA Evidence Checklist | `/evidence/evidence-checklist-nra.md` |
| NRA AWP | `/audit-work-programs/awp-nra.md` |
| Scoping Methodology | `/scope/scoping-methodology.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
