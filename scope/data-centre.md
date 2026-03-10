# Data Centre — Scope Definition

> BNM RMiT Nov 2025 — Scope Guidance for DCRA Engagements

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## 1. Regulatory Basis

| Attribute | Detail |
|-----------|--------|
| **Primary Clause** | 14.1 |
| **Scope Clauses** | 10.24 (DC Resilience Design), 10.25 (Redundancy and Failover), 10.26 (Physical Security), 10.27 (DC Operations), 10.28 (Segregation and Isolation) |

## 2. Scope Determination Factors

| Factor | How to Determine |
|--------|-----------------|
| **DC inventory** | Obtain the FI's complete data centre inventory — owned, co-located, third-party managed, primary, DR, and near-DR facilities |
| **System criticality** | Identify which critical systems are hosted in each DC; all DCs hosting critical systems are mandatory in scope |
| **DC classification** | Determine each DC's tier/classification (Tier I-IV equivalent) and its role (primary production, secondary, DR, archival) |
| **Ownership model** | Owned by FI, co-located (FI equipment in third-party facility), or fully managed by third party; this affects assessment approach |
| **Geographic location** | Identify DC locations and associated environmental risks (flood zone, earthquake zone, storm path) |
| **Material changes** | Identify any material infrastructure changes since the last DCRA (relocation, expansion, refresh, new DC, decommissioning) |
| **Third-party assurance** | For third-party DCs, identify available assurance reports (SOC 2, ISO 27001, Uptime Institute certification) |

## 3. In-Scope Items

### 3.1 Mandatory In-Scope

| Item | Rationale |
|------|-----------|
| Primary production data centre(s) | Hosts critical production systems; core to operational resilience |
| DR data centre(s) | Validates the FI's recovery capability; DR must meet RTO/RPO objectives |
| DC resilience design (10.24) | Regulatory requirement; DC design must support high availability and fault tolerance |
| Redundancy and failover (10.25) | Regulatory requirement; all critical infrastructure must have redundancy |
| Physical security (10.26) | Regulatory requirement; multi-layered physical access controls, environmental monitoring |
| DC operations (10.27) | Regulatory requirement; operational procedures, monitoring, change management |
| Segregation and isolation (10.28) | Regulatory requirement; production/non-production separation, SoD |
| Batch processing controls (10.28) | Regulatory requirement; batch job management and error handling |
| Power infrastructure | UPS, generators, ATS, power distribution — critical to DC availability |
| Cooling infrastructure | HVAC, CRAC/CRAH, redundancy — critical to equipment operation |
| Fire detection and suppression | Safety and equipment protection; regulatory and insurance requirements |
| Physical access control systems | Biometric, card access, mantraps, CCTV — security perimeter |
| Environmental monitoring systems | Temperature, humidity, water detection, power quality monitoring |

### 3.2 Conditionally In-Scope

| Item | Condition for Inclusion |
|------|------------------------|
| Near-DR or secondary DC facilities | Include if they host critical workloads or if their failure could impact recovery capability |
| Co-located facilities hosting non-critical systems only | Include if the co-lo also hosts some critical workloads, or if physical security weaknesses could enable lateral attack |
| DC network infrastructure (within the DC) | Physical network within DC is in DCRA scope; logical network design is covered by NRA. Include DC-internal switches, cabling, cross-connects |
| Cloud infrastructure hosted in the DC | Include the physical hosting layer; cloud-specific controls are covered by the Cloud assessment |
| Edge computing or branch server rooms | Include if they host locally critical applications and function as mini data centres |
| Third-party DC operator controls | In scope for assessment; may be assessed through reliance on assurance reports (SOC 2, ISO 27001) with gap analysis |

### 3.3 Typically Out-of-Scope (with justification required)

| Item | Justification for Exclusion | Risk of Exclusion |
|------|---------------------------|-------------------|
| Logical/application-level controls (e.g., OS hardening, application security) | Covered by other assessments (NRA for network, internal audit for application controls) | Low if other assessments are current |
| Public cloud infrastructure (AWS/Azure/GCP data centres) | FI does not control the physical infrastructure; assessed through CSP certifications | Residual risk addressed via Cloud assessment |
| Office server rooms housing only non-critical systems with no sensitive data | Low risk; not functioning as data centres | Minimal if genuinely non-critical |
| Decommissioned data centres (with confirmed decommissioning) | No longer operational; no risk | Verify decommissioning is complete (data destruction, asset disposal) |

## 4. Key Areas to Assess

### 4.1 By RMIT Paragraph

| Paragraph | Key Assessment Focus |
|-----------|---------------------|
| **10.24 — Resilience Design** | DC strategy and objectives, resilience targets (availability %), alignment with business RTO/RPO, capacity planning, single point of failure analysis, DC governance |
| **10.25 — Redundancy and Failover** | Power redundancy (N+1, 2N), cooling redundancy, network redundancy, diverse distribution paths, failover mechanisms, failover testing results, recovery time validation |
| **10.26 — Physical Security** | Perimeter security, multi-layered access control (building, floor, hall, cage, rack), CCTV coverage, visitor management, security guard services |
| **10.27 — DC Operations** | Environmental monitoring (temperature, humidity, water, fire), automated monitoring tools, operational procedures, capacity management, hardware lifecycle, change management, incident management |
| **10.28 — Segregation** | Production/non-production separation, multi-tenant segregation (co-lo), vendor/programmer access controls, segregation of duties, batch processing controls |

### 4.2 On-Site Assessment Areas

| Physical Area | What to Inspect |
|--------------|----------------|
| **Perimeter** | Fencing, lighting, CCTV coverage, barriers, vehicle access controls |
| **Building entrance** | Access control (badge/biometric), mantrap, reception, visitor management |
| **DC floor entrance** | Separate access control layer, anti-tailgating measures |
| **DC hall** | Rack layout, cable management, hot/cold aisle containment, cleanliness, labelling |
| **Power room** | UPS systems, battery banks, PDUs, ATS, power monitoring panels |
| **Generator area** | Generators, fuel storage, fuel delivery access, exhaust systems |
| **Cooling plant** | CRAC/CRAH units, chillers, cooling towers, piping, monitoring |
| **Fire suppression room** | Gas suppression systems (FM200, Novec), cylinders, inspection tags |
| **Network room / MDF** | Cross-connects, carrier meet-me room, fibre management |
| **Monitoring / NOC** | Monitoring dashboards, alert displays, staffing |

## 5. Interaction with Other Assurance

| Other Engagement | Interaction | Boundary |
|-----------------|-------------|----------|
| **NRA** | DC network infrastructure sits at the boundary | DCRA covers physical network infrastructure within the DC (cabling, physical switches, cross-connects). NRA covers logical network design, network security controls, and network resilience across all sites including inter-DC links |
| **Cloud Assessment** | Private cloud or cloud hosting from owned DC | DCRA covers the physical facility and infrastructure. Cloud assessment covers cloud platform controls (virtualisation, IAM, monitoring) |
| **Digital Services** | Digital services hosted from the DC | DCRA covers the physical infrastructure layer. Digital Services covers application-level security |
| **Business Continuity** | DC-level DR and BCP | DCRA assesses DC resilience design and failover capability. BCP assessment (if separate) covers business process continuity. DCRA validates that DR site meets resilience requirements |

## 6. Third-Party Data Centre Assessment Approach

Per clause 14.1, where the FI uses a third-party DC, the IESP may rely on independent third-party assurance, subject to:

| Step | Activity |
|------|----------|
| 1 | Obtain the SOC 2 Type II, ISO 27001, or Uptime Institute certification for the third-party DC |
| 2 | Map the assurance report's scope to RMIT paragraphs 10.24-10.28 |
| 3 | Identify gaps where the assurance report does not cover RMIT requirements |
| 4 | Perform supplementary testing for any identified gaps |
| 5 | Assess the FI's own controls that layer on top of the DC provider's controls (e.g., logical access, monitoring, change management) |
| 6 | Verify that the FI conducts periodic oversight of the DC provider (service reviews, SLA monitoring, incident tracking) |
| 7 | Document the reliance assessment and gap analysis in the DCRA report |

## 7. Scoping Checklist for DCRA

- [ ] Obtain complete data centre inventory (all facilities, roles, ownership models)
- [ ] Identify critical systems hosted in each DC (map to BIA)
- [ ] Determine DC tier/classification for each facility
- [ ] Identify ownership model (owned, co-lo, managed) for each facility
- [ ] Identify material changes since last DCRA
- [ ] For third-party DCs: obtain current assurance reports
- [ ] Identify all locations requiring site visits
- [ ] Confirm site visit logistics (access approvals, escort, photography permissions)
- [ ] Review prior DCRA scope and findings
- [ ] Identify interaction with NRA and other IESP engagements
- [ ] Agree scope boundaries with the FI
- [ ] Document scope in scoping memorandum and obtain FI sign-off

## 8. Cross-References

| Document | Path |
|----------|------|
| DCRA Requirements | `/requirements/dcra-requirements.md` |
| DCRA Evidence Checklist | `/evidence/evidence-checklist-dcra.md` |
| DCRA AWP | `/audit-work-programs/awp-dcra.md` |
| Scoping Methodology | `/scope/scoping-methodology.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
