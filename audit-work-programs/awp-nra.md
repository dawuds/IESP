# NRA Audit Work Program
## Network Resilience and Risk Assessment

> Per BNM RMiT Nov 2025 — Paragraph 14.1, mapped to paragraphs 10.36 to 10.43

### Engagement Overview
- **Engagement Type:** NRA
- **Regulatory Basis:** Paragraph 14.1
- **Scope Clauses:** 10.36, 10.37, 10.38, 10.39, 10.40, 10.41, 10.42, 10.43
- **Frequency:** Every 3 years or material change
- **Reporting:** Appendix 7 Part A

---

### Phase 1: Planning and Scoping

| Step | Activity | Deliverable |
|------|----------|-------------|
| P-01 | Obtain the FI's enterprise network architecture diagram (LAN, WAN, DMZ, cloud connectivity, third-party interconnections) | Validated network architecture pack |
| P-02 | Request inventory of all network devices (routers, switches, firewalls, load balancers, wireless APs, SD-WAN controllers) | Network device inventory |
| P-03 | Identify critical network segments and traffic flows that support critical business services | Critical network segment mapping |
| P-04 | Review prior NRA reports and track remediation status of prior findings | Prior findings tracker |
| P-05 | Obtain the FI's network policies, standards, and operational procedures | Policy document pack |
| P-06 | Agree on scope boundaries — clarify inclusion/exclusion of cloud network segments, branch networks, and third-party managed links | Scoping memorandum |

---

### Phase 2: Detailed Testing

#### Domain 1: Network Design and Scalability (10.36)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| NRA-01 | Verify network is designed to meet current and projected capacity requirements | 1. Obtain the network capacity planning document<br>2. Review current bandwidth utilisation across critical links (WAN, internet, DC interconnects)<br>3. Verify that capacity projections account for at least 2 years of growth<br>4. Check that utilisation thresholds trigger capacity augmentation (e.g., >70% sustained utilisation) | - Capacity planning document<br>- Bandwidth utilisation reports (last 12 months)<br>- Growth projection model | Pass: Documented capacity plan exists with growth projections, current utilisation is within acceptable thresholds, and augmentation triggers are defined. Fail: No capacity plan, links consistently above threshold, or no growth projection |
| NRA-02 | Verify network architecture supports scalability without major redesign | 1. Review the network architecture for modular and scalable design principles<br>2. Assess whether the architecture can accommodate new sites, services, or increased load without structural changes<br>3. Check for technology currency — are core network platforms within vendor support and capable of scaling | - Network architecture design principles document<br>- Technology lifecycle tracker<br>- Scalability assessment | Pass: Architecture uses modular design, core platforms are current and scalable, and past scaling events did not require redesign. Fail: Monolithic design, EOL core platforms, or recent scaling required significant redesign |
| NRA-03 | Verify network performance SLAs are defined and monitored | 1. Obtain defined network performance SLAs (latency, jitter, packet loss, availability) for critical segments<br>2. Verify SLA monitoring tools are in place and generating regular reports<br>3. Review SLA performance against targets for the past 6 months<br>4. Check that SLA breaches trigger investigation and remediation | - SLA definitions<br>- Performance monitoring reports<br>- SLA breach incident records | Pass: SLAs are defined for critical segments, actively monitored, and breaches are investigated with remediation. Fail: No SLAs, no monitoring, or breaches are unaddressed |

#### Domain 2: Network Resilience and Reliability (10.37, 10.38)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| NRA-04 | Verify network redundancy for critical paths and components | 1. Review network topology for redundancy at each layer (core, distribution, access)<br>2. Verify redundant paths exist for critical traffic (dual WAN links, diverse carrier paths, redundant internet breakouts)<br>3. Confirm redundant devices at each critical layer (e.g., HA pairs for firewalls, stacked/clustered switches)<br>4. Verify that redundant paths are on diverse physical routes | - Network topology diagrams with redundancy annotations<br>- Carrier diversity documentation<br>- HA configuration evidence | Pass: All critical paths and devices have documented redundancy with physical diversity confirmed. Fail: Single points of failure in critical paths or no physical diversity |
| NRA-05 | Verify network failover mechanisms are tested regularly | 1. Obtain failover test plan and schedule<br>2. Review results of the most recent failover tests for: WAN links, internet links, core switches, firewalls<br>3. Verify that failover occurs within acceptable recovery times<br>4. Check that test failures were remediated<br>5. Confirm tests simulate realistic failure conditions (cable pull, device shutdown) | - Failover test plans<br>- Test execution reports<br>- Remediation records | Pass: Failover tested at least annually for all critical components, failover times meet requirements, and failures are remediated. Fail: No testing, failover times exceed requirements, or unremediated test failures |
| NRA-06 | Verify network disaster recovery arrangements | 1. Review the network component of the FI's DR plan<br>2. Verify that network recovery procedures are documented for each critical segment<br>3. Check that network DR has been tested as part of the FI's DR exercises<br>4. Confirm network RTO aligns with business requirements | - Network DR plan<br>- DR test results (network component)<br>- RTO alignment mapping | Pass: Network DR plan is documented, tested within the last 12 months, and network RTO meets business requirements. Fail: No network DR plan, untested, or network RTO exceeds business requirements |
| NRA-07 | Verify carrier and ISP management for resilience | 1. Review contracts with carriers/ISPs for SLA terms (availability, MTTR)<br>2. Verify that the FI uses at least two independent carriers for critical WAN/internet<br>3. Check carrier performance against SLAs for the past 12 months<br>4. Confirm escalation procedures and emergency contact arrangements with carriers | - Carrier contracts with SLA terms<br>- Carrier diversity mapping<br>- Carrier performance reports<br>- Escalation contact lists | Pass: Multiple independent carriers for critical links, SLAs defined and monitored, and escalation procedures in place. Fail: Single carrier dependency, no SLAs, or no escalation procedures |

#### Domain 3: Network Monitoring and Traffic Analysis (10.39)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| NRA-08 | Verify comprehensive network monitoring is deployed | 1. Obtain the network monitoring tool inventory (NMS, NPM, flow analysis)<br>2. Verify that all critical network devices and links are monitored<br>3. Check monitoring coverage — are all critical parameters captured (availability, performance, errors, utilisation)?<br>4. Confirm monitoring operates 24/7 with alerting to the NOC | - Monitoring tool inventory<br>- Device coverage report<br>- Parameter coverage matrix<br>- NOC alerting configuration | Pass: All critical devices and links are monitored 24/7 for availability, performance, and errors, with alerts routed to NOC. Fail: Gaps in device or parameter coverage, or no 24/7 alerting |
| NRA-09 | Verify network traffic analysis and anomaly detection | 1. Confirm traffic flow analysis tools are deployed (NetFlow, sFlow, or equivalent)<br>2. Review traffic baseline profiles and anomaly detection thresholds<br>3. Check that anomalies trigger investigation — sample 5 recent anomaly alerts<br>4. Verify integration with SIEM or SOC for correlation with security events | - Flow analysis tool configuration<br>- Traffic baselines and anomaly thresholds<br>- Sample anomaly investigation records<br>- SIEM integration evidence | Pass: Traffic analysis deployed, baselines established, anomalies investigated, and integrated with SIEM/SOC. Fail: No traffic analysis, no baselines, or anomalies not investigated |
| NRA-10 | Verify network performance trend analysis and reporting | 1. Obtain regular network performance reports (monthly or quarterly)<br>2. Verify reports include trend analysis for utilisation, latency, and availability<br>3. Check that trends are used to inform capacity planning decisions<br>4. Confirm reports are reviewed by appropriate management | - Network performance reports<br>- Trend analysis dashboards<br>- Management review records | Pass: Regular performance reports with trend analysis are produced and reviewed by management to inform capacity decisions. Fail: No regular reporting, no trend analysis, or reports not reviewed |

#### Domain 4: Network Confidentiality, Integrity, Availability (10.40)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| NRA-11 | Verify encryption of data in transit over untrusted networks | 1. Identify all network links traversing untrusted networks (internet, public WAN, wireless)<br>2. Verify encryption is applied (IPSec VPN, TLS, MACsec as appropriate)<br>3. Check encryption standards — minimum TLS 1.2, AES-256 or equivalent<br>4. Verify certificate management for VPN/TLS endpoints | - Encryption standards policy<br>- VPN/TLS configuration evidence<br>- Certificate inventory and expiry tracking | Pass: All data traversing untrusted networks is encrypted to current standards, and certificates are managed. Fail: Unencrypted data over untrusted networks, weak encryption, or unmanaged certificates |
| NRA-12 | Verify network access controls and authentication | 1. Review network access control mechanisms (802.1X, NAC, MAC authentication)<br>2. Verify that network device management access uses strong authentication (RADIUS/TACACS+ with MFA)<br>3. Check that default credentials have been changed on all network devices<br>4. Verify that unused ports are administratively disabled<br>5. Sample-check 10 network device configurations for compliance | - NAC/802.1X configuration<br>- RADIUS/TACACS+ configuration<br>- Sample device configuration reviews<br>- Port status reports | Pass: NAC enforced, management access uses centralised AAA with MFA, no default credentials, and unused ports are disabled. Fail: No NAC, local authentication, default credentials found, or unused ports active |
| NRA-13 | Verify integrity controls for network device configurations | 1. Verify that network device configurations are backed up regularly (at least daily)<br>2. Check that configuration changes are detected and alerted (configuration drift monitoring)<br>3. Confirm that a golden/baseline configuration exists for each device type<br>4. Verify configuration backup is stored securely and separately from the devices | - Configuration backup schedule and logs<br>- Configuration drift monitoring tool<br>- Baseline configuration library<br>- Backup storage arrangements | Pass: Configurations backed up daily, drift is detected and alerted, baseline configs exist, and backups stored securely. Fail: No regular backups, no drift detection, or insecure backup storage |

#### Domain 5: Network Design Blueprint (10.41)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| NRA-14 | Verify a current and comprehensive network design blueprint exists | 1. Obtain the network design blueprint/architecture document<br>2. Verify it covers: logical topology, physical topology, IP addressing scheme, VLAN design, routing design, security zones, and connectivity to external parties<br>3. Check that the blueprint reflects the current state (not a stale document)<br>4. Verify the blueprint is version-controlled and updated upon changes | - Network design blueprint<br>- Version history<br>- Change control records | Pass: Comprehensive blueprint exists covering all required elements, reflects current state, and is version-controlled. Fail: No blueprint, missing critical elements, or blueprint does not match actual network |
| NRA-15 | Verify network design blueprint is reviewed and approved | 1. Check that the blueprint has been reviewed and approved by appropriate authority (e.g., network architecture board, CISO)<br>2. Verify the blueprint is reviewed at least annually or upon material change<br>3. Confirm the blueprint is accessible to relevant operational and security teams | - Approval records<br>- Review schedule/history<br>- Access/distribution records | Pass: Blueprint is approved by appropriate authority, reviewed within the last 12 months, and accessible to relevant teams. Fail: No approval, stale review, or limited accessibility |

#### Domain 6: Network Device Logging (10.42)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| NRA-16 | Verify comprehensive logging on network devices | 1. Review logging configuration on a sample of 10 network devices (firewalls, routers, core switches)<br>2. Verify that security-relevant events are logged: authentication attempts, configuration changes, ACL matches, administrative actions<br>3. Confirm logs are sent to a centralised log management system (syslog server or SIEM)<br>4. Verify time synchronisation (NTP) across all devices | - Sample device logging configurations<br>- Centralised log system evidence<br>- NTP configuration evidence | Pass: All sampled devices log security-relevant events, logs are centralised, and time is synchronised via NTP. Fail: Incomplete logging, logs not centralised, or time not synchronised |
| NRA-17 | Verify log retention and review procedures | 1. Check log retention periods against regulatory and policy requirements<br>2. Verify that logs are protected from tampering (write-once, access-controlled)<br>3. Confirm that network logs are regularly reviewed — either manually or through automated correlation (SIEM rules)<br>4. Sample 5 recent security events and trace them through log analysis to response | - Log retention policy and configuration<br>- Log protection mechanisms<br>- SIEM correlation rules for network events<br>- Sample event investigation records | Pass: Logs retained per policy (minimum 12 months online), protected from tampering, and reviewed through SIEM correlation or manual review. Fail: Insufficient retention, unprotected logs, or no review process |

#### Domain 7: Network Segmentation (10.43)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| NRA-18 | Verify network segmentation strategy and implementation | 1. Obtain the network segmentation policy and design<br>2. Verify that segmentation separates: production from non-production, internal from DMZ, PCI zones (if applicable), and guest/IoT networks<br>3. Review firewall/ACL rules enforcing segmentation<br>4. Conduct sample traffic flow tests to confirm segmentation is enforced (e.g., attempt cross-segment access that should be blocked) | - Segmentation policy and design<br>- Firewall/ACL rule sets<br>- Traffic flow test results | Pass: Segmentation policy exists, enforced through firewalls/ACLs, and confirmed through traffic flow testing. Fail: No segmentation policy, rules not enforced, or cross-segment access possible where it should be blocked |
| NRA-19 | Verify micro-segmentation or zero-trust for critical assets | 1. Identify the FI's most critical network segments (core banking, payment processing, internet banking)<br>2. Verify that additional segmentation controls exist for these segments beyond standard VLAN/firewall segmentation<br>3. Check for application-layer or workload-level segmentation where applicable<br>4. Verify access to critical segments requires explicit authorisation | - Critical segment identification<br>- Additional segmentation controls<br>- Access authorisation records | Pass: Critical segments have enhanced segmentation beyond standard controls, and access requires explicit authorisation. Fail: Critical segments have only standard segmentation with no additional controls |
| NRA-20 | Verify wireless network segmentation and security | 1. Identify all wireless networks (corporate, guest, IoT/OT)<br>2. Verify wireless networks are segmented from the wired corporate network<br>3. Check wireless authentication (WPA3-Enterprise or WPA2-Enterprise minimum)<br>4. Verify rogue AP detection is deployed and active<br>5. Review wireless security assessment results (if available) | - Wireless network inventory<br>- Wireless segmentation design<br>- Wireless authentication configuration<br>- Rogue AP detection system<br>- Wireless security assessment reports | Pass: Wireless networks are segmented, use enterprise-grade authentication, and rogue AP detection is active. Fail: Unsegmented wireless, pre-shared key authentication, or no rogue AP detection |

---

### Phase 3: Reporting

| Step | Activity | Deliverable |
|------|----------|-------------|
| R-01 | Consolidate all test results and assign risk ratings (High/Medium/Low) to each finding based on likelihood and impact to network resilience | Findings register with risk ratings |
| R-02 | Draft recommendations with specific, actionable remediation steps, responsible parties, and timelines | Recommendations tracker |
| R-03 | Conduct findings walkthrough with FI network and security teams to validate accuracy and agree on management responses | Walkthrough meeting minutes |
| R-04 | Prepare the formal NRA report in Appendix 7 Part A format | Final NRA report |
| R-05 | Obtain FI management sign-off on the report and management action plans | Signed report and action plans |

---

### Phase 4: Board Deliberation Support

| Step | Activity | Deliverable |
|------|----------|-------------|
| B-01 | Prepare executive summary highlighting critical network risks and recommendations for the designated board committee (per 8.3) | Board presentation deck |
| B-02 | Attend the designated committee meeting to present findings and respond to queries | Attendance record and meeting minutes |
| B-03 | Document any additional directives from the committee and incorporate into final report | Updated report (if required) |

---

### Appendices

- **Appendix A:** Document Request List (DRL) template
- **Appendix B:** Network device sample selection methodology
- **Appendix C:** Appendix 7 Part A report template
- **Appendix D:** Risk rating methodology
- **Appendix E:** Common network vulnerability checklist
