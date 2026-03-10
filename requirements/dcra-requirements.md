# Data Centre Resilience Assessment (DCRA) — Detailed Requirements

> BNM RMiT Nov 2025 — Practitioner Guide for IESP Teams Performing DCRA

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 14.1 |
| **Marker** | S (mandatory) |
| **Scope Clauses** | 10.24, 10.25, 10.26, 10.27, 10.28 |
| **Reporting** | Appendix 7 Part A (Risk Assessment Report) |
| **ESP Standards** | Appendix 7 Part C (Requirements on External Party Assurance) |
| **Board Governance** | 8.3 (designated board-level committee must deliberate outcome) |

## 2. Trigger Conditions

A DCRA must be conducted when **any** of the following conditions are met:

1. **Three-year cycle:** The last DCRA was completed more than 36 months ago.
2. **Material change to DC infrastructure:** Any change that could significantly alter the risk profile of the data centre, including but not limited to:
   - Relocation of the data centre (full or partial)
   - Major structural modifications to the facility
   - Significant changes to power supply or cooling infrastructure
   - Changes to the data centre tier/classification
   - Major expansion of capacity exceeding original design parameters
   - Changes to physical security systems (e.g., new access control technology)
   - Transition from owned to third-party data centre (or vice versa)
   - Consolidation or decommissioning of data centre facilities
3. **BNM direction:** BNM may direct a DCRA at any time under clause 1.4 or 17.4.

**Whichever comes first** determines when the DCRA is due.

## 3. Scope Definition — Paragraphs 10.24 to 10.28

The DCRA must assess the financial institution's compliance with the following requirements:

### 3.1 Paragraph 10.24 — Data Centre Resilience Design

**What to Assess:**
- The data centre design ensures high availability and fault tolerance for critical systems
- Redundancy is built into all critical infrastructure components (power, cooling, network, storage)
- The design accommodates growth and scalability requirements
- Single points of failure have been identified and mitigated
- The design meets or exceeds the FI's stated availability requirements (e.g., Tier III/IV equivalent)

**Key Evidence to Collect:**
- Data centre design documentation and architecture diagrams
- Tier classification or equivalent resilience standard documentation
- Single point of failure analysis
- Capacity planning documents
- Availability SLAs and historical performance against SLAs

### 3.2 Paragraph 10.25 — Redundancy and Failover

**What to Assess:**
- Power supply redundancy (dual utility feeds, UPS, generators, automatic transfer switches)
- Cooling system redundancy (N+1 or 2N configurations)
- Network connectivity redundancy (diverse carrier paths, redundant switches/routers)
- Storage redundancy (RAID, replication, backup systems)
- Automatic failover mechanisms and failover testing results
- Recovery time from component failures

**Key Evidence to Collect:**
- Power single-line diagrams showing redundancy
- UPS capacity and runtime specifications
- Generator capacity, fuel supply, and testing records
- Cooling system design and N+1/2N documentation
- Network topology showing diverse paths
- Failover test results (last 12 months)
- Component failure logs and recovery times

### 3.3 Paragraph 10.26 — Physical Security

**What to Assess:**
- Perimeter security (fencing, barriers, lighting, CCTV)
- Building access control (mantraps, biometric, card access, visitor management)
- Server room/cage access control (separate from building access)
- CCTV coverage (interior and exterior, retention period, monitoring)
- Security guard services (24/7, procedures, incident response)
- Environmental monitoring (fire detection, suppression, water leak detection, temperature/humidity)
- Visitor management procedures (escort requirements, access logging)

**Key Evidence to Collect:**
- Physical security policy and procedures
- Access control system configuration and logs
- CCTV coverage maps and retention policy
- Security guard procedures and shift records
- Environmental monitoring system configuration and alert thresholds
- Fire suppression system type, inspection records, and testing results
- Water leak detection system coverage
- Visitor logs (sample period)
- Access review records

### 3.4 Paragraph 10.27 — Data Centre Operations

**What to Assess:**
- Operational procedures for day-to-day DC management
- Environmental monitoring and alerting (temperature, humidity, power quality)
- Capacity monitoring and management
- Cable management and labeling standards
- Equipment lifecycle management (hardware refresh, decommissioning)
- Cleaning and maintenance schedules
- Change management procedures specific to DC infrastructure
- Incident management and escalation for DC events

**Key Evidence to Collect:**
- DC operations manual/runbook
- Environmental monitoring dashboards and alert configuration
- Capacity utilization reports (current and trend)
- Cable management standards documentation
- Hardware asset inventory and lifecycle status
- Maintenance schedules and completion records
- DC-specific change management records (last 12 months)
- DC incident logs (last 12 months)
- Staff training records for DC operations personnel

### 3.5 Paragraph 10.28 — Segregation and Isolation

**What to Assess:**
- Logical and physical segregation between production and non-production environments
- Segregation between the FI's infrastructure and other tenants (for shared/colocation facilities)
- Segregation of duties for DC operations staff
- Network segmentation within the data centre
- Segregation of backup and DR systems

**Key Evidence to Collect:**
- Network segmentation diagrams showing production/non-production boundaries
- Colocation agreement terms (if applicable) addressing segregation
- Physical cage/room separation documentation
- Role-based access control matrix for DC staff
- Backup infrastructure isolation documentation

## 4. Third-Party Data Centre Considerations

Where the FI uses a third-party data centre, 14.1 allows reliance on independent third-party assurance reports, **subject to the following conditions:**

| Condition | Assessment Required |
|-----------|-------------------|
| **Consistency with risk appetite** | Verify that the scope and depth of the third-party assurance aligns with the FI's risk appetite for DC resilience |
| **Similar risks considered** | The assurance must address the same risk domains as a direct DCRA (10.24–10.28) |
| **Meets DCRA requirements** | The assurance report must cover all areas that would be covered in a direct DCRA |
| **Currency** | The assurance report must be reasonably current (within the 3-year DCRA cycle) |
| **Qualifications** | The assurance provider must be technically competent and independent |

**Practitioner Guidance for Third-Party DC:**
1. Obtain the SOC 2 Type II, ISO 27001, or equivalent assurance report
2. Map the report's scope to RMIT paragraphs 10.24–10.28
3. Identify any gaps where the third-party report does not cover RMIT requirements
4. Perform supplementary testing for any identified gaps
5. Assess the FI's own controls (e.g., logical access, monitoring) that layer on top of the DC provider's controls
6. Document the reliance assessment and gap analysis in the DCRA report

## 5. Board Deliberation Requirement

Per paragraph 8.3, the DCRA results must be presented to and deliberated by a designated board-level committee:

- **Which committee:** The board risk committee, board technology committee, or equivalent as designated by the FI
- **What must be presented:** Full DCRA report including findings, risk ratings, and remediation recommendations
- **What must be documented:** Committee minutes recording deliberation, questions raised, management responses, and any directions given
- **Timeline:** Deliberation should occur within a reasonable period after DCRA completion (typically within one board cycle)
- **Follow-up:** The committee should receive updates on remediation progress at subsequent meetings

## 6. Reporting Requirements — Appendix 7 Part A Format

The DCRA report must follow the Appendix 7 Part A format:

### Section 1 — Financial Institution Details
- Full legal name
- BNM license type and number
- Primary contact person (name, title, email, phone)

### Section 2 — External Service Provider Details
- IESP firm name and registration details
- Lead assessor name and professional qualifications
- Team composition and relevant certifications
- Contact details
- Independence declaration

### Section 3 — Application/System Details (adapted for DCRA)
- Data centre name(s) and location(s)
- Data centre classification/tier
- Critical systems hosted
- Third-party DC provider details (if applicable)
- Scope inclusions and exclusions

### Section 4 — Technology Risk Assessment
- Assessment methodology used
- Detailed findings organized by RMIT paragraphs (10.24–10.28)
- For each finding:
  - Description of the issue
  - RMIT clause reference
  - Risk rating (High/Medium/Low)
  - Evidence supporting the finding
  - Recommendation for remediation
  - Management response (if available)
- Summary risk heat map
- Comparison with previous DCRA findings (if applicable)

### Section 5 — Quality Assurance
- Methodology description
- Peer review process
- Scope limitations or caveats
- Standards and frameworks referenced (e.g., TIA-942, Uptime Institute, ISO 27001)

### Section 6 — Authorised Signatory
- Lead assessor signature and date
- Professional qualifications stated
- Firm stamp/seal

## 7. Key Activities Checklist

### Phase 1 — Planning and Scoping
- [ ] Confirm DCRA trigger (3-year cycle, material change, or BNM direction)
- [ ] Obtain previous DCRA report (if any) and review findings
- [ ] Identify all data centres in scope (primary, DR, third-party)
- [ ] Request preliminary documentation (DC design, network diagrams, policies)
- [ ] Define assessment timeline and resource requirements
- [ ] Confirm IESP team qualifications meet Appendix 7 Part C
- [ ] Issue engagement letter with scope, timeline, and deliverables
- [ ] Schedule site visit(s)

### Phase 2 — Documentation Review
- [ ] Review DC design documentation against 10.24 requirements
- [ ] Review redundancy specifications against 10.25 requirements
- [ ] Review physical security policies and procedures against 10.26
- [ ] Review DC operations procedures against 10.27
- [ ] Review segregation controls against 10.28
- [ ] Review previous audit/assessment findings and remediation status
- [ ] Review incident history for DC-related events
- [ ] Review capacity planning and utilization reports
- [ ] For third-party DC: obtain and review assurance reports

### Phase 3 — On-Site Assessment
- [ ] Conduct physical walkthrough of data centre facility
- [ ] Verify power infrastructure (UPS, generators, transfer switches)
- [ ] Verify cooling infrastructure (CRAC/CRAH units, redundancy)
- [ ] Verify physical security controls (access control, CCTV, guards)
- [ ] Verify environmental monitoring systems (temperature, humidity, water detection)
- [ ] Verify fire detection and suppression systems
- [ ] Verify cable management and labeling
- [ ] Verify segregation controls (physical cages, room separation)
- [ ] Interview DC operations staff on procedures and incident handling
- [ ] Observe access control procedures (entry/exit, visitor management)
- [ ] Test failover mechanisms (where feasible and agreed with the FI)

### Phase 4 — Analysis and Testing
- [ ] Analyze power capacity vs. current load and growth projections
- [ ] Analyze cooling capacity vs. heat load
- [ ] Review failover test results and recovery times
- [ ] Analyze access control logs for anomalies
- [ ] Review environmental monitoring alerts and responses
- [ ] Analyze incident logs for recurring issues
- [ ] Assess compliance with stated tier/resilience standards
- [ ] Perform gap analysis against RMIT requirements (10.24–10.28)
- [ ] For third-party DC: perform gap analysis of assurance report vs. RMIT

### Phase 5 — Reporting
- [ ] Draft findings with risk ratings, evidence, and recommendations
- [ ] Conduct quality assurance / peer review of draft report
- [ ] Discuss draft findings with FI management
- [ ] Incorporate management responses
- [ ] Finalize report in Appendix 7 Part A format
- [ ] Issue signed report to designated FI contact

### Phase 6 — Board Presentation Support
- [ ] Prepare executive summary for board committee
- [ ] Support FI in presenting findings to designated board committee (if requested)
- [ ] Confirm board deliberation is documented in committee minutes

## 8. Common Findings and Red Flags

The following are frequently identified issues in DCRA engagements. Assessors should pay particular attention to these areas:

| Finding Category | Common Issues |
|-----------------|---------------|
| **Power** | Single utility feed, insufficient generator runtime, UPS batteries past useful life, no automatic transfer testing |
| **Cooling** | No redundancy (N+0), insufficient capacity for peak load, reliance on single chilled water loop |
| **Physical Security** | Tailgating possible, CCTV blind spots, no mantrap, visitor escort not enforced, access reviews not performed |
| **Environmental** | Fire suppression inspection overdue, no water leak detection under raised floor, temperature/humidity out of spec with no alerts |
| **Operations** | No documented runbooks, no capacity trending, hardware past end-of-support, inconsistent cable labeling |
| **Segregation** | Shared racks between production and development, no logical segmentation between tenants in shared facility |
| **BCP/DR** | DR site not assessed, no coordinated failover testing, RPO/RTO not validated |
| **Third-Party** | Assurance report does not cover all RMIT domains, no FI-specific controls assessment, reliance without gap analysis |

## 9. Cross-References

| Document | Path |
|----------|------|
| Regulatory Requirements (all clauses) | `/requirements/regulatory-requirements.md` |
| NRA Requirements | `/requirements/nra-requirements.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |
| Appendix 7 Part A Template | See RMIT source documents |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
