# DCRA Audit Work Program
## Data Centre Resilience and Risk Assessment

> Per BNM RMiT Nov 2025 — Paragraph 14.1, mapped to paragraphs 10.24 to 10.28

### Engagement Overview
- **Engagement Type:** DCRA
- **Regulatory Basis:** Paragraph 14.1
- **Scope Clauses:** 10.24, 10.25, 10.26, 10.27, 10.28
- **Frequency:** Every 3 years or material change
- **Reporting:** Appendix 7 Part A

---

### Phase 1: Planning and Scoping

**Objective:** Establish engagement scope, understand the FI's data centre environment, and plan detailed testing activities.

| Step | Activity | Deliverable |
|------|----------|-------------|
| P-01 | Obtain and review the FI's data centre inventory, including owned, co-located, and third-party managed facilities | Validated DC inventory list |
| P-02 | Request prior DCRA reports (internal and external) and track remediation status of prior findings | Prior findings tracker with closure evidence |
| P-03 | Identify in-scope data centres based on criticality classification (primary, DR, near-DR) | Scoping memorandum |
| P-04 | Obtain DC floor plans, rack layouts, and infrastructure single-line diagrams | Site documentation pack |
| P-05 | Schedule site visits and confirm access arrangements, escort requirements, and photography permissions | Site visit itinerary |
| P-06 | Request the FI's business recovery objectives (RTO/RPO) for critical systems hosted in each DC | Recovery objectives matrix |

---

### Phase 2: Detailed Testing

#### Domain 1: DC Resilience and Availability Objectives (10.24)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| DCRA-01 | Verify DC resilience objectives are defined and aligned with business recovery objectives | 1. Obtain DC resilience and availability strategy document<br>2. Extract stated resilience targets (availability %, RTO, RPO)<br>3. Compare against the FI's approved business recovery objectives for each critical system hosted<br>4. Check that resilience targets have been approved by the appropriate committee | - DC resilience strategy document<br>- Business recovery objectives matrix<br>- Committee approval minutes | Pass: Resilience objectives are documented, quantified (e.g., 99.99% availability), and demonstrably aligned with business recovery requirements. Fail: No formal resilience objectives exist, or objectives are not mapped to business recovery needs |
| DCRA-02 | Verify periodic review and update of DC resilience objectives | 1. Check version history of the resilience strategy<br>2. Confirm review frequency (at least annual or upon material change)<br>3. Verify that changes in business requirements triggered corresponding updates | - Document version history<br>- Change log entries<br>- Review sign-off records | Pass: Strategy reviewed within the last 12 months or after the last material change, whichever is more recent. Fail: Strategy is stale (>12 months without review) or business changes were not reflected |

#### Domain 2: Redundancy and Single Points of Failure (10.25)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| DCRA-03 | Verify redundant capacity exists for critical infrastructure components | 1. Obtain the DC redundancy design document (N+1, 2N, or 2N+1 configurations)<br>2. For each critical infrastructure layer (power, cooling, network), confirm the documented redundancy level<br>3. Verify actual installed capacity against design documents through site inspection<br>4. Check that redundant capacity can handle full load upon failover | - Redundancy design specifications<br>- Capacity planning reports<br>- Site inspection photographs | Pass: Redundant capacity is documented, physically verified, and tested under failover conditions for all critical layers. Fail: Any critical layer lacks redundancy or installed capacity does not match design |
| DCRA-04 | Verify multiple distribution paths for critical utilities | 1. Review electrical single-line diagrams for dual utility feeds or on-site generation<br>2. Review network connectivity diagrams for diverse carrier paths<br>3. Confirm physical path diversity (separate risers, conduits, or entry points)<br>4. Verify through site walk that paths are genuinely separate | - Electrical single-line diagrams<br>- Network path diversity documentation<br>- Site walk observations | Pass: At least two independent distribution paths exist for power and network with confirmed physical separation. Fail: Single path dependency exists for any critical utility |
| DCRA-05 | Verify single points of failure (SPOF) have been identified and mitigated | 1. Obtain the FI's SPOF analysis or risk register for each DC<br>2. Walk through each identified SPOF and confirm mitigation measures<br>3. Identify any unrecognised SPOFs through independent assessment during site walk<br>4. Check that SPOF analysis is periodically refreshed | - SPOF analysis/register<br>- Mitigation action plans<br>- Site walk findings | Pass: Comprehensive SPOF analysis exists, all identified SPOFs have documented mitigations, and no critical unmitigated SPOFs found during independent walkthrough. Fail: SPOF analysis is incomplete, mitigations are missing, or new critical SPOFs are identified |
| DCRA-06 | Verify failover testing of redundant components | 1. Obtain failover test plans and most recent test results for each redundant component (UPS, generators, cooling, network switches)<br>2. Review test frequency — should be at least annual<br>3. Confirm that tests simulate actual failure conditions, not just planned switchovers<br>4. Check that test failures resulted in corrective actions | - Failover test plans<br>- Test result reports<br>- Corrective action records | Pass: All redundant components tested at least annually under realistic failure conditions, with documented results and remediation of failures. Fail: Components untested, tests are superficial, or test failures not remediated |

#### Domain 3: Physical Security and Environmental Controls (10.26)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| DCRA-07 | Verify DC is in a dedicated, purpose-built space with appropriate physical separation | 1. Confirm DC is in a dedicated space not shared with non-IT functions<br>2. Verify physical separation from public areas, loading docks, and other tenants (for co-located facilities)<br>3. Check that walls extend from true floor to true ceiling (no false ceiling bypass) | - Site inspection observations<br>- Building layout plans<br>- Lease/facility agreements for co-lo | Pass: DC is in a dedicated space with full physical separation from non-DC areas. Fail: DC space is shared, or physical barriers can be bypassed |
| DCRA-08 | Verify multi-layered physical access controls | 1. Walk the physical access path from building perimeter to server rack<br>2. Verify each access layer (perimeter, building, floor, DC hall, cage/rack) has independent controls<br>3. Test access control mechanisms (badge, biometric, PIN) at each layer<br>4. Review access provisioning and de-provisioning procedures<br>5. Sample-check the access list against HR records for terminated staff | - Physical security policy<br>- Access control system configuration<br>- Access list vs. HR reconciliation<br>- Site walk observations | Pass: Minimum 3 layers of access control, active provisioning/de-provisioning process, and no stale access found in sample. Fail: Fewer than 3 layers, no formal provisioning process, or stale access entries found |
| DCRA-09 | Verify DC is not located in a disaster-prone area, or adequate mitigations exist | 1. Obtain the FI's site risk assessment covering natural hazards (flood, earthquake, lightning)<br>2. Cross-reference DC location against publicly available hazard maps<br>3. Where risks are identified, verify mitigation measures (e.g., raised floor for flood, seismic bracing)<br>4. Check that the site risk assessment is periodically updated | - Site risk assessment<br>- Hazard map cross-reference<br>- Mitigation implementation evidence | Pass: Formal site risk assessment performed, natural hazards identified and mitigated, and assessment is current. Fail: No site risk assessment, unmitigated natural hazard exposure, or assessment is outdated |
| DCRA-10 | Verify electrical infrastructure resilience and capacity | 1. Review UPS configuration (online double-conversion, N+1 or 2N)<br>2. Verify UPS battery runtime under full load (minimum 15 minutes)<br>3. Confirm generator start-up time and fuel autonomy (minimum 48-72 hours)<br>4. Check automatic transfer switch (ATS) operation and test records<br>5. Verify fuel replenishment contracts and delivery SLAs | - UPS specifications and test reports<br>- Generator load test reports<br>- ATS test records<br>- Fuel supply contracts | Pass: UPS provides minimum 15 min runtime, generator auto-starts within design parameters, fuel autonomy meets FI policy (typically 48-72 hrs), and all tested within last 12 months. Fail: Insufficient battery runtime, generator start-up failures, or inadequate fuel arrangements |
| DCRA-11 | Verify thermal management and cooling infrastructure | 1. Review cooling design and redundancy level (N+1 minimum)<br>2. Check current cooling load vs. installed capacity<br>3. Verify temperature and humidity monitoring at rack level<br>4. Confirm alerting thresholds and escalation procedures<br>5. Review hot/cold aisle containment strategy | - Cooling system design documents<br>- Capacity utilisation reports<br>- Monitoring system configuration<br>- Alert threshold settings | Pass: Cooling is N+1 or better, capacity headroom exists, monitoring is at rack level with defined alerting thresholds. Fail: No cooling redundancy, capacity is at or above limits, or monitoring is inadequate |
| DCRA-12 | Verify environmental monitoring and fire suppression | 1. Confirm VESDA or equivalent early warning detection is installed<br>2. Verify fire suppression system type (gas-based for IT areas) and inspection records<br>3. Check water leak detection under raised floor and around cooling units<br>4. Verify environmental monitoring dashboard and 24/7 alert capability<br>5. Review incident response procedures for environmental events | - Fire suppression inspection certificates<br>- VESDA configuration records<br>- Water leak detection layout<br>- Monitoring dashboard screenshots<br>- Environmental incident response procedures | Pass: Early warning detection installed, gas-based suppression current on inspections, water leak detection in place, and 24/7 monitoring with defined escalation. Fail: Missing detection/suppression, expired inspections, or no 24/7 monitoring |
| DCRA-13 | Verify hardware asset management and lifecycle controls | 1. Obtain hardware asset register and verify it is up to date<br>2. Sample-check physical assets on the floor against the register<br>3. Verify end-of-life/end-of-support hardware is identified and has a replacement plan<br>4. Check that decommissioned equipment undergoes secure data destruction | - Hardware asset register<br>- Physical verification results<br>- EOL/EOS tracker<br>- Data destruction certificates | Pass: Asset register is accurate (>95% match on sample), EOL hardware is tracked with replacement timelines, and secure destruction is evidenced. Fail: Register inaccuracies >5%, untracked EOL hardware, or no destruction evidence |

#### Domain 4: DC Operations and Control Procedures (10.27)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| DCRA-14 | Verify automated monitoring and management tools are deployed | 1. Obtain inventory of DC monitoring tools (DCIM, BMS, network monitoring)<br>2. Verify coverage of critical parameters: power, cooling, capacity, network<br>3. Test that alerts are generated for threshold breaches<br>4. Confirm monitoring is integrated into the NOC/SOC for 24/7 visibility | - Tool inventory and architecture<br>- Monitoring coverage matrix<br>- Sample alert records<br>- NOC/SOC integration evidence | Pass: Automated monitoring covers all critical parameters with 24/7 alerting and NOC/SOC integration. Fail: Manual-only monitoring, gaps in coverage, or no 24/7 alerting |
| DCRA-15 | Verify batch processing controls and scheduling | 1. Obtain batch job scheduling procedures and tool configuration<br>2. Verify that batch jobs have defined run windows, dependencies, and error handling<br>3. Review batch job failure logs for the past 3 months and confirm remediation<br>4. Check that batch schedules are reviewed and approved before changes | - Batch scheduling procedures<br>- Job scheduler configuration<br>- Failure logs and remediation records<br>- Change approval records | Pass: Batch jobs are formally scheduled with defined error handling, failures are tracked and remediated, and schedule changes are controlled. Fail: Ad-hoc scheduling, no error handling, or uncontrolled changes |
| DCRA-16 | Verify change management controls for DC infrastructure changes | 1. Obtain the DC change management procedure<br>2. Sample 10 recent infrastructure changes (network, power, rack moves)<br>3. Verify each change has: request, impact assessment, approval, implementation plan, rollback plan, and post-implementation review<br>4. Check that emergency changes follow a defined expedited process | - Change management procedure<br>- Sample of 10 change records<br>- Emergency change records | Pass: All sampled changes have complete records (request through post-implementation review), and emergency changes follow a defined process. Fail: Incomplete change records, missing approvals, or uncontrolled emergency changes |
| DCRA-17 | Verify error and incident handling procedures for DC operations | 1. Obtain DC operations incident management procedure<br>2. Review incident log for the past 6 months — check categorisation, escalation, and resolution<br>3. Verify root cause analysis (RCA) was performed for significant incidents<br>4. Check that RCA findings led to preventive actions | - Incident management procedure<br>- Incident log (6 months)<br>- RCA reports<br>- Preventive action tracker | Pass: Formal incident procedure exists, incidents are categorised and escalated per procedure, RCAs completed for significant incidents with preventive actions. Fail: No formal procedure, inconsistent categorisation, or RCAs not performed |

#### Domain 5: Segregation of Incompatible Activities (10.28)

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| DCRA-18 | Verify vendor and programmer access to DC is controlled and segregated | 1. Review the policy for vendor/third-party access to the DC<br>2. Check that vendors require pre-approved access requests with defined scope and duration<br>3. Verify escort requirements for vendors in sensitive areas<br>4. Sample-check vendor access logs against approved requests<br>5. Confirm that vendor access is revoked promptly after engagement ends | - Vendor access policy<br>- Access request forms/system<br>- Escort logs<br>- Access log vs. approval reconciliation | Pass: Vendors require pre-approval, are escorted in sensitive areas, access logs match approvals, and access is revoked within 24 hours of engagement end. Fail: Uncontrolled vendor access, no escort for sensitive areas, or stale vendor access |
| DCRA-19 | Verify production environment is segregated from development and testing | 1. Review logical and physical segregation between production and non-production environments<br>2. Verify that developers do not have direct access to production servers in the DC<br>3. Check network segmentation between production and non-production zones<br>4. Confirm that data used in non-production environments is masked/anonymised | - Environment segregation architecture<br>- Access control matrices<br>- Network segmentation diagrams<br>- Data masking procedures | Pass: Production is physically or logically segregated, developers have no direct production access, network segmentation enforced, and non-production data is masked. Fail: No segregation, developers with production access, or unmasked production data in non-production |
| DCRA-20 | Verify segregation of duties in DC operations | 1. Obtain the DC operations RACI or role matrix<br>2. Verify that incompatible duties are separated (e.g., change requester vs. approver, access provisioner vs. user)<br>3. Check that privileged access to DC infrastructure is limited and monitored<br>4. Review privileged access usage logs for the past 3 months | - RACI matrix<br>- Role definitions<br>- Privileged access list<br>- Privileged access usage logs | Pass: Incompatible duties are formally separated, privileged access is limited to named individuals with justified need, and usage is logged and reviewed. Fail: No SoD controls, excessive privileged access, or unreviewed privileged access usage |

---

### Phase 3: Reporting

| Step | Activity | Deliverable |
|------|----------|-------------|
| R-01 | Consolidate all test results and assign risk ratings (High/Medium/Low) to each finding | Findings register with risk ratings |
| R-02 | Draft recommendations with specific, actionable remediation steps and timelines | Recommendations tracker |
| R-03 | Conduct findings walkthrough with FI management to validate accuracy and agree on management responses | Walkthrough meeting minutes |
| R-04 | Prepare the formal DCRA report in Appendix 7 Part A format | Final DCRA report |
| R-05 | Obtain FI management sign-off on the report and management action plans | Signed report and action plans |

---

### Phase 4: Board Deliberation Support

| Step | Activity | Deliverable |
|------|----------|-------------|
| B-01 | Prepare executive summary and presentation materials for the designated board committee (per 8.3) | Board presentation deck |
| B-02 | Attend the designated committee meeting to present findings and respond to queries | Attendance record and meeting minutes |
| B-03 | Document any additional directives from the committee and incorporate into final report | Updated report (if required) |

---

### Appendices

- **Appendix A:** Document Request List (DRL) template
- **Appendix B:** Site visit checklist
- **Appendix C:** Appendix 7 Part A report template
- **Appendix D:** Risk rating methodology
