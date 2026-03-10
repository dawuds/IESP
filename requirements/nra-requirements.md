# Network Resilience Assessment (NRA) — Detailed Requirements

> BNM RMiT Nov 2025 — Practitioner Guide for IESP Teams Performing NRA

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 14.2 |
| **Marker** | S (mandatory) |
| **Scope Clauses** | 10.36, 10.37, 10.38, 10.39, 10.40, 10.41, 10.42, 10.43 |
| **Reporting** | Appendix 7 Part A (Risk Assessment Report) |
| **ESP Standards** | Appendix 7 Part C (Requirements on External Party Assurance) |
| **Board Governance** | 8.3 (designated board-level committee must deliberate outcome) |

## 2. Trigger Conditions

An NRA must be conducted when **any** of the following conditions are met:

1. **Three-year cycle:** The last NRA was completed more than 36 months ago.
2. **Material change to network design:** Any change that could significantly alter the risk profile of the network infrastructure, including but not limited to:
   - Major redesign of core network topology
   - Introduction of new network zones or segments
   - Significant changes to WAN architecture (e.g., MPLS to SD-WAN migration)
   - Changes to internet edge architecture
   - Introduction or significant modification of network security controls (firewalls, IDS/IPS)
   - Data centre network redesign (e.g., migration to spine-leaf architecture)
   - Major changes to remote access architecture
   - Integration of new business units or acquired entities into the network
   - Migration to or significant expansion of cloud connectivity
   - Introduction of new communication channels (e.g., API gateways, IoT connectivity)
3. **BNM direction:** BNM may direct an NRA at any time under clause 1.4 or 17.4.

**Whichever comes first** determines when the NRA is due.

## 3. Scope Definition — Paragraphs 10.36 to 10.43

### 3.1 Paragraph 10.36 — Network Design and Architecture

**What to Assess:**
- Network architecture is designed to support high availability of critical systems
- The design follows security-by-design principles with defence in depth
- Network topology documentation is current and accurate
- The architecture supports business requirements and growth projections
- Network design considers resilience against both internal and external threats
- Separation of management, production, and user traffic

**Key Evidence to Collect:**
- Network architecture diagrams (logical and physical)
- Network design standards and guidelines
- High-level and detailed topology documentation
- Network asset inventory (routers, switches, firewalls, load balancers, WAFs)
- IP addressing scheme and VLAN assignments
- Design review records and approval documentation
- Bandwidth provisioning and utilization reports

### 3.2 Paragraph 10.37 — Network Resilience and Redundancy

**What to Assess:**
- Redundancy of core network components (switches, routers, firewalls)
- Diverse network paths for critical connectivity (WAN, internet, inter-DC)
- High availability configurations (clustering, active-active, active-passive)
- Automatic failover capability and failover testing results
- Carrier diversity for WAN and internet links
- DNS resilience (primary/secondary, geographic distribution)
- Load balancing configurations for critical services
- Network recovery time objectives and demonstrated recovery capabilities

**Key Evidence to Collect:**
- Redundancy design documentation for each network layer
- High availability configuration extracts (HSRP/VRRP, firewall clustering, etc.)
- WAN circuit documentation showing carrier diversity and path diversity
- Internet link documentation showing diverse ISP arrangements
- Failover test results (last 12 months)
- DNS architecture documentation and failover configuration
- Load balancer configuration and health check mechanisms
- Network outage logs and recovery times (last 12 months)

### 3.3 Paragraph 10.38 — Network Security Controls

**What to Assess:**
- Firewall architecture and rule management (ingress/egress, default deny)
- Intrusion detection and prevention systems (IDS/IPS) deployment and tuning
- Web application firewalls (WAF) for internet-facing applications
- DDoS protection mechanisms (on-premise and/or cloud-based)
- Network access control (NAC) for endpoint admission
- VPN and remote access security (encryption, authentication, split tunneling policy)
- Wireless network security (WPA3, segmentation, rogue AP detection)
- API gateway security (rate limiting, authentication, input validation)
- Email security (anti-spam, anti-phishing, DMARC/DKIM/SPF)
- DNS security (DNSSEC, DNS filtering, sinkholing)

**Key Evidence to Collect:**
- Firewall rule base and last review date
- IDS/IPS deployment architecture and signature update policy
- WAF configuration and rule sets
- DDoS protection architecture and capacity
- NAC policy configuration
- VPN configuration standards
- Wireless security configuration and rogue AP detection reports
- API gateway configuration and security policies
- Email security gateway configuration
- DNS security configuration

### 3.4 Paragraph 10.39 — Network Monitoring

**What to Assess:**
- Real-time network monitoring coverage (all critical network components)
- Network performance monitoring (latency, packet loss, bandwidth utilization)
- Security event monitoring and correlation (SIEM integration)
- Alerting thresholds and escalation procedures
- Network anomaly detection capabilities
- Monitoring of third-party network services (WAN, internet, cloud connectivity)
- Monitoring dashboard and reporting
- 24/7 monitoring coverage and NOC/SOC integration

**Key Evidence to Collect:**
- Network monitoring tool inventory and coverage map
- Monitoring architecture documentation
- Alert threshold configuration
- Escalation procedures and contact lists
- Sample monitoring dashboards and reports
- SIEM integration documentation for network events
- Anomaly detection rules and tuning records
- NOC/SOC operating procedures for network events
- Monitoring coverage gap analysis

### 3.5 Paragraph 10.40 — Network Segmentation

**What to Assess:**
- Network segmentation strategy and implementation
- Separation of critical and non-critical systems
- DMZ architecture for internet-facing services
- Microsegmentation for sensitive workloads (where applicable)
- Segmentation between production and non-production environments
- Segmentation of third-party/vendor access
- Segmentation of user and server networks
- Inter-segment access controls (firewall rules between zones)
- Effectiveness of segmentation (validated through testing)

**Key Evidence to Collect:**
- Network segmentation policy and standards
- Zone definitions and classification criteria
- VLAN assignments and inter-VLAN routing controls
- DMZ architecture documentation
- Firewall rules governing inter-zone traffic
- Microsegmentation implementation documentation (if applicable)
- Third-party access network isolation controls
- Penetration test results validating segmentation effectiveness
- Segmentation review records

### 3.6 Paragraph 10.41 — Network Change Management

**What to Assess:**
- Network change management process aligned with overall ITIL/change management
- Risk assessment for network changes (impact on availability, security)
- Testing procedures for network changes (lab, staging, production validation)
- Rollback procedures and tested rollback capability
- Emergency change procedures with post-implementation review
- Configuration management and version control for network devices
- Segregation of duties (requestor, approver, implementer)
- Change freeze/blackout period policies

**Key Evidence to Collect:**
- Network change management procedure
- Sample change records (last 12 months) — successful and failed
- Change risk assessment templates and completed examples
- Rollback procedure documentation
- Emergency change records and post-implementation reviews
- Configuration management database/repository
- Change approval board records
- Change freeze policy documentation

### 3.7 Paragraph 10.42 — Network Logging

**What to Assess:**
- Comprehensive logging of network device activities (firewalls, switches, routers, WAF, IDS/IPS)
- Log integrity protection (tamper-evident, centralized, write-once)
- Log retention period aligned with regulatory requirements and incident investigation needs
- Log review processes (automated and manual)
- Time synchronization across all network devices (NTP)
- Log aggregation and correlation (SIEM)
- Privileged access logging for network device management
- NetFlow/sFlow collection for traffic analysis

**Key Evidence to Collect:**
- Logging policy and standards
- Log sources inventory and coverage analysis
- Centralized log management architecture (SIEM, log aggregator)
- Log retention configuration and policy
- NTP configuration across network devices
- Log review procedures and evidence of execution
- Sample log analysis reports
- Privileged access logging configuration for network devices
- NetFlow/sFlow collection architecture and retention

### 3.8 Paragraph 10.43 — Network Incident Response

**What to Assess:**
- Network-specific incident response procedures
- DDoS response playbook and tested response capability
- Network intrusion response procedures
- Network outage response and communication procedures
- Coordination with SOC for network security events
- Forensic capability for network incidents (packet capture, flow analysis)
- Lessons learned process for network incidents
- Integration with overall incident management framework

**Key Evidence to Collect:**
- Network incident response procedures
- DDoS response playbook and exercise results
- Network intrusion response procedures
- Outage communication procedures and templates
- SOC integration documentation for network events
- Forensic tools and capability documentation
- Incident reports and lessons learned (last 12 months)
- Incident response exercise records (tabletop, simulation)

## 4. Board Deliberation Requirement

Per paragraph 8.3, the NRA results must be presented to and deliberated by a designated board-level committee:

- **Which committee:** The board risk committee, board technology committee, or equivalent as designated by the FI
- **What must be presented:** Full NRA report including findings, risk ratings, and remediation recommendations
- **What must be documented:** Committee minutes recording deliberation, questions raised, management responses, and directions given
- **Timeline:** Deliberation should occur within a reasonable period after NRA completion (typically within one board cycle)
- **Follow-up:** The committee should receive updates on remediation progress at subsequent meetings

## 5. Reporting Requirements — Appendix 7 Part A Format

The NRA report must follow the Appendix 7 Part A format:

### Section 1 — Financial Institution Details
- Full legal name, BNM license type and number, primary contact person

### Section 2 — External Service Provider Details
- IESP firm name, lead assessor name and qualifications, team composition, independence declaration

### Section 3 — Scope Details (adapted for NRA)
- Network infrastructure in scope (core, distribution, access, WAN, internet, wireless, DC network)
- Sites and locations covered
- Critical systems and services dependent on the network infrastructure
- Third-party managed network services in scope
- Scope inclusions and exclusions
- Assessment period

### Section 4 — Technology Risk Assessment
- Assessment methodology
- Detailed findings organized by RMIT paragraphs (10.36–10.43)
- For each finding:
  - Description of the issue
  - RMIT clause reference
  - Risk rating (High/Medium/Low)
  - Evidence supporting the finding
  - Recommendation for remediation
  - Management response (if available)
- Summary risk heat map
- Comparison with previous NRA findings (if applicable)

### Section 5 — Quality Assurance
- Methodology description
- Peer review process
- Scope limitations or caveats
- Standards and frameworks referenced (e.g., NIST CSF, ISO 27001, CIS Controls)

### Section 6 — Authorised Signatory
- Lead assessor signature and date, professional qualifications, firm stamp

## 6. Key Activities Checklist

### Phase 1 — Planning and Scoping
- [ ] Confirm NRA trigger (3-year cycle, material change, or BNM direction)
- [ ] Obtain previous NRA report (if any) and review findings
- [ ] Request network architecture documentation (logical, physical, security zones)
- [ ] Identify all network domains in scope (core, WAN, internet, wireless, DC, cloud connectivity)
- [ ] Identify third-party managed network services
- [ ] Define assessment timeline and resource requirements
- [ ] Confirm IESP team qualifications meet Appendix 7 Part C (network security expertise required)
- [ ] Issue engagement letter with scope, timeline, and deliverables
- [ ] Coordinate any active testing (vulnerability scanning, penetration testing) windows
- [ ] Obtain necessary access credentials and VPN access for remote assessment

### Phase 2 — Documentation Review
- [ ] Review network architecture documentation against 10.36
- [ ] Review redundancy and HA design against 10.37
- [ ] Review network security control documentation against 10.38
- [ ] Review monitoring architecture and procedures against 10.39
- [ ] Review segmentation design and policies against 10.40
- [ ] Review network change management procedures against 10.41
- [ ] Review logging architecture and policies against 10.42
- [ ] Review network incident response procedures against 10.43
- [ ] Review previous audit/assessment findings and remediation status
- [ ] Review network incident history (last 12 months)
- [ ] Review firewall rule review records
- [ ] Review penetration test results relevant to network infrastructure

### Phase 3 — Technical Assessment
- [ ] Validate network topology against documentation (configuration review)
- [ ] Verify redundancy configurations (HA, failover, diverse paths)
- [ ] Review firewall rule bases for compliance with policy (default deny, least privilege)
- [ ] Verify IDS/IPS deployment, tuning, and signature currency
- [ ] Assess DDoS protection adequacy (capacity, response time)
- [ ] Review network monitoring coverage and alert configuration
- [ ] Verify network segmentation effectiveness (configuration review and/or testing)
- [ ] Review network device hardening against standards (CIS benchmarks or equivalent)
- [ ] Verify logging coverage and centralization
- [ ] Review NTP configuration across network devices
- [ ] Assess wireless security configuration and rogue AP detection
- [ ] Review VPN and remote access configuration
- [ ] Review DNS architecture and security configuration
- [ ] Assess network device patch levels and vulnerability exposure
- [ ] Review network device access controls (management access, AAA)
- [ ] Review certificate management for network services (TLS, VPN)

### Phase 4 — Testing (where agreed with FI)
- [ ] Conduct network vulnerability assessment
- [ ] Validate segmentation through controlled testing
- [ ] Test failover mechanisms (where feasible and agreed)
- [ ] Validate DDoS protection response (simulation if available)
- [ ] Test monitoring alerting (generate test events)
- [ ] Validate log collection from sample network devices

### Phase 5 — Analysis and Reporting
- [ ] Analyze all findings and assign risk ratings
- [ ] Map findings to RMIT clause requirements (10.36–10.43)
- [ ] Identify trends and systemic issues
- [ ] Draft findings with evidence, risk ratings, and recommendations
- [ ] Conduct quality assurance / peer review
- [ ] Discuss draft findings with FI management
- [ ] Incorporate management responses
- [ ] Finalize report in Appendix 7 Part A format
- [ ] Issue signed report to designated FI contact

### Phase 6 — Board Presentation Support
- [ ] Prepare executive summary for board committee
- [ ] Support FI in presenting findings to designated board committee (if requested)
- [ ] Confirm board deliberation is documented in committee minutes

## 7. Common Findings and Red Flags

| Finding Category | Common Issues |
|-----------------|---------------|
| **Design** | Outdated network diagrams, undocumented changes, flat network architecture, no defence in depth |
| **Redundancy** | Single WAN carrier, no diverse path for critical links, untested failover, single firewall (no HA), single DNS server |
| **Security Controls** | Overly permissive firewall rules, "any-any" rules, disabled IDS/IPS signatures, no WAF for internet-facing apps, no DDoS protection, default credentials on network devices |
| **Monitoring** | Incomplete coverage (not all devices monitored), stale alert thresholds, no 24/7 monitoring, SIEM not integrated with network events, no anomaly detection |
| **Segmentation** | Flat network, production and non-production on same VLAN, unrestricted inter-zone traffic, vendor access not isolated, PCI/sensitive zones not properly segmented |
| **Change Management** | Changes without risk assessment, no rollback testing, emergency changes not reviewed, configuration drift between documented and actual state |
| **Logging** | Incomplete log collection, short retention period, no log integrity protection, no time synchronization, no regular log review, logging disabled on some devices |
| **Incident Response** | No network-specific IR procedures, no DDoS playbook, no forensic capability, lessons learned not implemented |
| **Hardening** | Network devices running vulnerable firmware, unnecessary services enabled, SNMP v1/v2c in use, Telnet enabled, weak encryption for management access |
| **Third-Party** | Managed service provider access not restricted, no monitoring of provider activities, SLAs not aligned with FI requirements |

## 8. Technical Standards Reference

The following standards and frameworks should be referenced during NRA assessments:

| Standard | Relevance |
|----------|-----------|
| **NIST SP 800-53** | Security and privacy controls — network security family (SC) |
| **CIS Controls v8** | Controls 9 (Email Security), 12 (Network Infrastructure), 13 (Network Monitoring) |
| **CIS Benchmarks** | Device-specific hardening guides (Cisco IOS, Palo Alto, Fortinet, etc.) |
| **ISO 27001:2022** | A.8 (Technology controls) — network security, segmentation, monitoring |
| **PCI DSS v4.0** | Requirement 1 (Network controls), Requirement 10 (Logging), Requirement 11 (Testing) |
| **NIST CSF 2.0** | Protect (PR.DS, PR.AC), Detect (DE.CM, DE.AE) functions |

## 9. Cross-References

| Document | Path |
|----------|------|
| Regulatory Requirements (all clauses) | `/requirements/regulatory-requirements.md` |
| DCRA Requirements | `/requirements/dcra-requirements.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |
| Appendix 7 Part A Template | See RMIT source documents |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
