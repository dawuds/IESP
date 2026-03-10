# IESP Engagement Scoping Methodology

> BNM RMiT Nov 2025 — Practitioner Guide for Determining IESP Engagement Scope

> **Disclaimer:** This is an indicative/educational resource. It does not constitute legal advice. Always refer to the official BNM Policy Document.

## 1. Purpose

This document provides a structured methodology for IESP teams to determine the appropriate scope for each type of RMIT assurance engagement. Correct scoping is critical — too narrow a scope leaves gaps in assurance coverage; too broad a scope results in an unfocused engagement that may not deliver actionable findings.

## 2. Regulatory Basis for Scoping

| Clause | Relevance to Scoping |
|--------|---------------------|
| **14.1** | Defines scope for DCRA (paragraphs 10.24-10.28) |
| **14.2** | Defines scope for NRA (paragraphs 10.36-10.43) |
| **17.1** | Defines scope for Cloud and Emerging Technology reviews (Appendix 9, Appendix 10) |
| **16.4, 16.5** | Defines scope for Digital Services reviews (Appendix 7 Part D) |
| **Appendix 7 Part C** | Requirements on External Party Assurance — quality and independence standards |

## 3. Scoping Methodology — Five-Step Process

### Step 1: Identify the Engagement Type

Determine which RMIT assurance engagement is required based on the trigger condition:

| Engagement Type | Primary Clause | Trigger | Scope Reference |
|----------------|---------------|---------|-----------------|
| **DCRA** | 14.1 | 3-year cycle, material DC change, or BNM direction | 10.24-10.28 |
| **NRA** | 14.2 | 3-year cycle, material network change, or BNM direction | 10.36-10.43 |
| **Cloud Assessment** | 17.1 | 3-year cycle, new CSP, material cloud change, or BNM direction | 10.50-10.52, Appendix 10 |
| **Emerging Tech Review** | 17.1 | First-time adoption, material change, periodic, or BNM direction | Appendix 9 |
| **Digital Services Review** | 16.4, 16.5 | New or materially enhanced digital service launch | Appendix 7 Part D |

### Step 2: Determine the Scope Boundary

For each engagement type, determine the boundary of what is in scope:

#### Scope Determination Factors

| Factor | Description | How to Assess |
|--------|-------------|--------------|
| **Asset inventory** | What physical/logical assets are subject to the engagement? | Obtain the FI's asset inventory for the relevant domain (DC inventory, network asset register, cloud service catalogue, technology register) |
| **Criticality classification** | Which assets support critical systems? | Map assets to the FI's Business Impact Analysis (BIA) and system criticality classification |
| **Data classification** | What data is processed, stored, or transmitted by in-scope assets? | Cross-reference with the FI's data classification framework |
| **Geographic scope** | Which locations, regions, or jurisdictions are covered? | Identify all relevant sites (DCs, offices, cloud regions) |
| **Third-party scope** | Which third-party providers are in scope? | Identify outsourced components within the engagement boundary |
| **Prior assessment coverage** | What was covered in the previous assessment? | Review prior IESP reports to identify continuity and gaps |
| **Material changes** | What has changed since the last assessment? | Obtain change logs and compare with prior assessment scope |

#### Scoping Decision Matrix

| Question | If Yes | If No |
|----------|--------|-------|
| Does the asset support a critical system (per BIA)? | In scope (mandatory) | Consider for scope based on risk |
| Does the asset process restricted or confidential data? | In scope (mandatory) | Consider for scope based on risk |
| Has the asset undergone material change since last assessment? | In scope (mandatory) | In scope if within the periodic cycle |
| Is the asset managed by a third party? | In scope, but may rely on third-party assurance (with gap analysis) | In scope (directly assessed) |
| Has BNM specifically directed inclusion? | In scope (mandatory) | Apply standard scoping criteria |
| Was the asset excluded from the prior assessment? | Assess whether exclusion was justified; consider for inclusion | Apply standard scoping criteria |

### Step 3: Define In-Scope and Out-of-Scope Items

Document explicitly what is in scope and what is out of scope. The scoping memorandum should include:

**In-Scope:**
- Specific assets, systems, facilities, or services to be assessed
- RMIT paragraphs and appendix areas to be covered
- Time period for evidence review (e.g., "12 months preceding the assessment date")
- Locations and sites to be visited or assessed
- Third-party providers to be assessed (directly or through reliance on assurance reports)

**Out-of-Scope (with justification):**
- Assets or systems excluded and the reason for exclusion
- RMIT requirements that are not applicable and why
- Locations not visited and the rationale
- Reliance on other assurance engagements (with identification of the engagement and coverage)

### Step 4: Validate Scope with the FI

Before commencing detailed work, validate the proposed scope with the FI:

- Present the scoping memorandum to the FI's engagement sponsor
- Confirm asset inventory completeness
- Confirm that material changes have been identified
- Agree on sites to be visited and access arrangements
- Agree on the evidence review period
- Agree on any scope limitations (with documentation of the limitation and its impact on assurance)
- Obtain FI sign-off on the scoping memorandum

### Step 5: Document the Scope in the Report

The final report (Appendix 7 Part A) must clearly document the scope:

- Section 3 of the report should detail exactly what was assessed
- Any scope limitations must be disclosed in Section 5 (Quality Assurance)
- The impact of scope limitations on the overall assurance opinion must be stated

## 4. Scope Interaction Between Engagement Types

IESP engagements may overlap. The following matrix identifies common interaction points:

| Engagement A | Engagement B | Interaction Area | How to Handle |
|-------------|-------------|-----------------|--------------|
| DCRA | NRA | DC network infrastructure | DCRA covers physical network within the DC; NRA covers logical network design and security. Avoid duplication by agreeing boundary |
| DCRA | Cloud | Co-located cloud infrastructure | DCRA covers physical facility; Cloud assessment covers cloud-specific controls. DC hosting cloud infrastructure is assessed in DCRA for physical resilience |
| NRA | Cloud | Cloud connectivity and network security | NRA covers network path to cloud; Cloud assessment covers cloud-side network controls (VPC, security groups). Agree handoff point |
| Cloud | Emerging Tech | AI/ML deployed on cloud | Cloud assessment covers infrastructure; Emerging Tech review covers AI-specific risks. Both may assess IAM and monitoring from different perspectives |
| Digital Services | Cloud | Digital service hosted on cloud | Digital Services review covers application-layer controls; Cloud assessment covers infrastructure. Ensure no gap at the platform layer |
| Digital Services | NRA | Network supporting digital services | NRA covers network resilience and security; Digital Services review covers application-level security. API gateway may be assessed by both |

### Handling Overlaps

1. **Review recent and planned engagements:** Before scoping, identify what other IESP engagements have been or will be conducted for the FI
2. **Agree boundaries:** Where overlaps exist, agree with the FI which engagement covers which area
3. **Cross-reference findings:** Where a related engagement has been completed, reference its findings rather than re-testing (with appropriate caveats on timing and scope)
4. **Document reliance:** If relying on another engagement's findings, document the reliance, the engagement details, and any limitations

## 5. Scoping Pitfalls to Avoid

| Pitfall | Description | Mitigation |
|---------|-------------|-----------|
| **Scope creep** | Scope expands during the engagement without formal agreement | Use a formal scope change process; any scope expansion requires written agreement and may impact timeline/fees |
| **Under-scoping** | Critical assets or areas are excluded | Use the criticality-based scoping approach; validate scope against BIA; err on the side of inclusion for critical assets |
| **Over-reliance on prior scope** | Using the previous engagement's scope without reassessing | Always reassess scope considering material changes, new assets, and lessons learned |
| **Ignoring third parties** | Excluding third-party managed components from scope | Third-party components are in scope; the question is how to assess them (directly or through assurance reliance) |
| **Scoping by convenience** | Excluding areas because they are difficult to assess (e.g., overseas DC, cloud-native services) | Scope should be driven by risk, not convenience. If an area is difficult to assess, discuss alternative approaches with the FI |
| **Ambiguous boundaries** | Not clearly defining where one engagement's scope ends and another begins | Document explicit boundaries, especially for overlapping engagements |

## 6. Scoping Memorandum Template

The scoping memorandum should contain the following sections:

1. **Engagement type** and regulatory basis
2. **Trigger condition** (what triggered this engagement)
3. **FI context** (brief description of the FI's technology environment relevant to this engagement)
4. **In-scope assets and systems** (specific list or categorisation)
5. **In-scope RMIT requirements** (specific paragraph/appendix references)
6. **Out-of-scope items** (with justification for each exclusion)
7. **Assessment period** (evidence review window)
8. **Sites/locations** to be visited
9. **Third-party scope** (which third parties are in scope and assessment approach)
10. **Interaction with other engagements** (overlaps and agreed boundaries)
11. **Scope limitations** (if any, with impact assessment)
12. **Resource requirements** (team composition and expertise needed)
13. **Timeline** (key milestones)
14. **FI sign-off** (engagement sponsor approval)

## 7. Cross-References

| Document | Path |
|----------|------|
| Data Centre Scope | `/scope/data-centre.md` |
| Network Infrastructure Scope | `/scope/network-infrastructure.md` |
| Cloud Services Scope | `/scope/cloud-services.md` |
| AI/Emerging Tech Scope | `/scope/ai-emerging-tech.md` |
| DCRA Requirements | `/requirements/dcra-requirements.md` |
| NRA Requirements | `/requirements/nra-requirements.md` |
| Cloud Requirements | `/requirements/cloud-pre-implementation.md` |
| Emerging Tech Requirements | `/requirements/emerging-tech-review.md` |
| Decision Tree | `/decision-tree/when-iesp-required.md` |

---

## Revision History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-11 | Initial compilation from BNM RMiT Nov 2025 |
