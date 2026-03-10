# NRA Scope Definition — Network Resilience Assessment

> BNM RMiT Nov 2025 — Paragraph 14.2, Scope: Paragraphs 10.36 to 10.43

**Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## Overview

The NRA scope encompasses the enterprise network infrastructure supporting the financial institution's business activities. The assessment must consider all major risks, determine the current level of resilience, and set proportionate controls aligned with the FI's risk appetite.

## In-Scope Areas

### 1. Network Design and Scalability (10.36)
- Enterprise network architecture design
- Reliability, scalability, and security of the network
- Support for current business activities
- Capacity for future growth plans

### 2. Network Resilience and Reliability (10.37, 10.38)
- Network services for critical systems
- Single point of failure analysis
- Protection against network faults and cyber threats
- Component redundancy
- Service diversity
- Alternate network paths

### 3. Network Monitoring and Traffic Analysis (10.39)
- Real-time network bandwidth monitoring
- Network service resilience metrics
- Over-utilisation and bandwidth congestion detection
- System disruption detection from network faults
- Traffic analysis for trends and anomalies

### 4. Network Confidentiality, Integrity, and Availability (10.40)
- Network services supporting critical systems
- Confidentiality controls (encryption, access controls)
- Integrity controls (data validation, tamper detection)
- Availability controls (redundancy, failover)

### 5. Network Design Blueprint (10.41)
- Network design blueprint documentation
- All internal and external network interfaces
- Physical connectivity mapping
- Logical connectivity mapping
- Network component inventory
- Network segmentation documentation

### 6. Network Device Logging (10.42)
- Sufficient network device logs
- Relevant network device logs for forensics
- Minimum 3-year log retention
- Log integrity and tamper protection

### 7. Network Segmentation and Isolation (10.43)
- Safeguards against cross-entity compromise within the group
- Logical network segmentation from other entities
- Prevention of lateral movement between segments

## Out-of-Scope (Unless Specifically Required)

- Data centre physical infrastructure (covered by DCRA under 14.1)
- Application-layer security (covered by digital services assessment)
- Cloud network architecture (covered by cloud IESP under 17.1, Appendix 10)
- End-user device security
- Wireless networks at branch offices (unless material)

## Technical Assessment Areas

| Area | Key Tests |
|------|-----------|
| **Architecture Review** | Topology analysis, redundancy assessment, SPOF identification |
| **Resilience Testing** | Failover testing, path diversity verification, load balancing |
| **Security Assessment** | Firewall rules, IDS/IPS configuration, ACLs, encryption |
| **Monitoring Review** | SNMP/NetFlow configuration, alerting thresholds, dashboard coverage |
| **Segmentation Validation** | VLAN configuration, inter-segment traffic rules, penetration testing |
| **Log Management** | Log sources, retention, SIEM integration, forensic readiness |
| **Documentation Review** | Blueprint accuracy, change management, version control |

## Key Interactions

| Related Assessment | Overlap Areas | Delineation |
|-------------------|---------------|-------------|
| DCRA (14.1) | DC network infrastructure | DCRA covers physical DC; NRA covers logical network design and resilience |
| Cloud IESP (17.1) | Cloud connectivity | Cloud IESP covers CSP network; NRA covers FI-side connectivity to cloud |
| Penetration Testing (11.6) | Vulnerability identification | NRA assesses design resilience; pen testing exploits vulnerabilities |
| Cybersecurity (11.1-11.20) | Threat detection | NRA covers network monitoring; cyber covers SOC operations |
