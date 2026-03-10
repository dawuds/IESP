# AI/Emerging Technology Audit Work Program
## AI and Emerging Technology Risk Assessment

> Per BNM RMiT Nov 2025 — Paragraph 17.1, mapped to Appendix 9

### Engagement Overview
- **Engagement Type:** AI/Emerging Technology IESP Assessment
- **Regulatory Basis:** Paragraph 17.1
- **Scope Clauses:** Appendix 9
- **Frequency:** Every 3 years or material change (including new AI/emerging tech deployment, significant model updates, or expansion to new use cases)
- **Reporting:** Appendix 7 Part A

---

### Phase 1: Planning and Scoping

| Step | Activity | Deliverable |
|------|----------|-------------|
| P-01 | Obtain the FI's AI/emerging technology inventory — all AI models, ML systems, RPA deployments, and other emerging technologies in use or under development | AI/emerging tech inventory |
| P-02 | Classify each technology by risk tier based on use case (e.g., customer-facing decisions, internal automation, advisory) and data sensitivity | Risk-tiered technology register |
| P-03 | Identify the governance structure for AI/emerging tech — committees, roles, policies | Governance structure mapping |
| P-04 | Review prior assessment reports and regulatory correspondence related to AI/emerging tech | Prior findings and regulatory correspondence pack |
| P-05 | Understand the technology stack — frameworks, platforms, training data sources, deployment infrastructure | Technology stack documentation |

---

### Phase 2: Detailed Testing

#### Domain 1: Governance Arrangements

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| AI-01 | Verify AI/emerging technology governance framework is established | 1. Obtain the FI's AI/emerging tech governance framework or policy<br>2. Verify it defines: accountability structure, decision rights, risk management approach, ethical principles, and oversight mechanisms<br>3. Check that a designated committee or senior management forum has oversight of AI/emerging tech<br>4. Verify the framework is approved at the board or senior management level | - AI governance framework/policy<br>- Committee terms of reference<br>- Board/senior management approval records | Pass: Governance framework exists with clear accountability, oversight committee established, and framework approved at senior management or board level. Fail: No governance framework, unclear accountability, or no designated oversight body |
| AI-02 | Verify roles and responsibilities for AI/emerging tech are defined | 1. Review organisational structure for AI/emerging tech management<br>2. Verify defined roles: model owner, model developer, model validator, risk manager, compliance officer<br>3. Check that each deployed model/technology has an assigned owner accountable for its performance and risk<br>4. Verify the FI has or has access to sufficient expertise in AI/ML | - Organisational chart (AI function)<br>- Role descriptions<br>- Model/technology ownership register<br>- Skills inventory or expertise assessment | Pass: Clear roles defined, each model/technology has an accountable owner, and sufficient expertise exists. Fail: Undefined roles, unowned models, or insufficient expertise |

#### Domain 2: Risk Assessment and Tolerance

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| AI-03 | Verify risk assessment is performed for each AI/emerging technology deployment | 1. Obtain the risk assessment methodology for AI/emerging tech<br>2. For each in-scope deployment, verify that a risk assessment was performed covering: model risk, data risk, bias/fairness risk, explainability risk, operational risk, and regulatory risk<br>3. Verify risk assessments are proportionate to the risk tier of the deployment<br>4. Check that residual risks are within the FI's approved risk tolerance | - Risk assessment methodology<br>- Completed risk assessments per deployment<br>- Risk tolerance thresholds<br>- Residual risk acceptance records | Pass: Risk assessments performed for all deployments, covering all required risk domains, proportionate to risk tier, and residual risks within tolerance. Fail: Missing risk assessments, incomplete coverage, or residual risks exceed tolerance without formal acceptance |
| AI-04 | Verify bias and fairness assessments are conducted | 1. Identify AI models that make or support decisions affecting customers (credit scoring, pricing, fraud detection, customer segmentation)<br>2. For each such model, verify that bias and fairness testing has been performed<br>3. Check that protected attributes (race, gender, age, etc.) are assessed for disparate impact<br>4. Verify ongoing monitoring for bias drift over time | - Bias and fairness testing methodology<br>- Bias test results per model<br>- Disparate impact analysis<br>- Ongoing monitoring configuration | Pass: Bias testing performed for all customer-impacting models, protected attributes assessed, and ongoing monitoring in place. Fail: No bias testing for customer-impacting models, or no ongoing monitoring |

#### Domain 3: Acceptance Criteria

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| AI-05 | Verify formal acceptance criteria exist for AI/emerging technology deployment to production | 1. Obtain the FI's acceptance criteria framework for AI/emerging tech<br>2. Verify criteria cover: model performance thresholds, validation results, security assessment, ethical review, operational readiness, and business sign-off<br>3. For each in-scope deployment, verify that acceptance criteria were met before production deployment<br>4. Check that acceptance was formally documented and signed off | - Acceptance criteria framework<br>- Completed acceptance checklists per deployment<br>- Sign-off records | Pass: Formal acceptance criteria exist, cover all required areas, and all deployments demonstrate documented compliance with criteria before production launch. Fail: No acceptance criteria, criteria are incomplete, or deployments went live without meeting criteria |

#### Domain 4: Technology and Cybersecurity Controls

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| AI-06 | Verify security controls protect AI models and training data | 1. Review access controls for AI model repositories, training data stores, and inference endpoints<br>2. Verify training data is classified, access-controlled, and protected (encryption at rest and in transit)<br>3. Check that model artefacts (trained models, weights, configurations) are version-controlled and integrity-protected<br>4. Verify that AI development environments are segmented from production<br>5. Assess protections against adversarial attacks on AI models (input validation, model hardening) | - Access control configurations<br>- Data classification and encryption evidence<br>- Model version control system<br>- Environment segmentation evidence<br>- Adversarial attack mitigation measures | Pass: Access controls enforced, training data protected, model artefacts version-controlled, environments segmented, and adversarial attack mitigations in place. Fail: Weak access controls, unprotected training data, no version control, or no adversarial attack considerations |
| AI-07 | Verify data quality and data governance for AI systems | 1. Review the data governance framework for AI/ML training and inference data<br>2. Verify data quality controls: completeness, accuracy, timeliness, consistency<br>3. Check that data lineage is tracked from source to model input<br>4. Verify that data privacy requirements are met (anonymisation, consent, purpose limitation)<br>5. Check that training data is representative and sufficient for the intended use case | - Data governance framework<br>- Data quality control procedures and metrics<br>- Data lineage documentation<br>- Privacy compliance evidence<br>- Training data representativeness assessment | Pass: Data governance framework in place, data quality controls active, lineage tracked, privacy requirements met, and training data is representative. Fail: No data governance, poor data quality controls, no lineage tracking, or privacy gaps |

#### Domain 5: Operating Control Effectiveness

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| AI-08 | Verify model performance monitoring is in place for production models | 1. Identify all AI models in production<br>2. Verify that each model has defined performance metrics (accuracy, precision, recall, F1, AUC, or business-specific KPIs)<br>3. Check that performance is monitored continuously or at defined intervals<br>4. Verify that performance degradation triggers alerts and investigation<br>5. Confirm model retraining/recalibration procedures exist and are triggered by performance decline | - Production model inventory<br>- Performance metric definitions per model<br>- Monitoring dashboard/tool configuration<br>- Alert configuration and sample alert records<br>- Retraining/recalibration procedures | Pass: All production models have defined metrics, continuous monitoring, degradation alerts, and documented retraining procedures. Fail: Unmonitored models, no performance metrics, or no retraining procedures |
| AI-09 | Verify model validation is performed independently | 1. Check that model validation is performed by a party independent of model development<br>2. Review the validation methodology — does it cover: conceptual soundness, data adequacy, performance benchmarking, sensitivity analysis, and stress testing?<br>3. Verify validation is performed before initial deployment and periodically thereafter<br>4. Check that validation findings are tracked and remediated | - Model validation policy<br>- Independence of validation function<br>- Validation reports<br>- Validation finding tracker | Pass: Independent validation performed for all models before deployment and periodically, covering required areas, with findings tracked and remediated. Fail: No independent validation, incomplete methodology, or unremediated findings |

#### Domain 6: Production Environment Prerequisites

| Ref | Test Objective | Test Steps | Expected Evidence | Pass/Fail Criteria |
|-----|---------------|------------|-------------------|-------------------|
| AI-10 | Verify adequate testing is performed before production deployment | 1. Review the testing strategy for AI/emerging tech deployments<br>2. Verify testing includes: unit testing, integration testing, performance/load testing, security testing, user acceptance testing, and A/B or shadow testing where applicable<br>3. For each in-scope deployment, verify test execution records and results<br>4. Confirm that test exit criteria were met before production release | - Testing strategy document<br>- Test plans and execution records<br>- Test results and exit criteria assessment<br>- Production release approval | Pass: Comprehensive testing performed including all required test types, exit criteria defined and met, and production release formally approved. Fail: Incomplete testing, exit criteria not met, or production release without approval |
| AI-11 | Verify compliance with applicable standards and regulations | 1. Identify applicable standards and regulations for the FI's AI deployments (BNM guidelines, PDPA, sector-specific requirements)<br>2. Verify that each deployment has been assessed for regulatory compliance<br>3. Check that required regulatory notifications or approvals have been obtained<br>4. Verify ongoing compliance monitoring is in place | - Regulatory requirements register<br>- Compliance assessment per deployment<br>- Regulatory notification/approval records<br>- Compliance monitoring procedures | Pass: Applicable regulations identified, compliance assessed per deployment, required approvals obtained, and ongoing monitoring in place. Fail: Regulations not identified, no compliance assessment, or missing regulatory approvals |
| AI-12 | Verify the ability to suspend or decommission AI systems | 1. Check that each production AI system has a documented suspension/kill-switch capability<br>2. Verify that the suspension mechanism can be activated quickly (within defined timeframes)<br>3. Test or review evidence of suspension testing<br>4. Verify that fallback/manual processes exist if the AI system is suspended<br>5. Confirm that the decision authority for suspension is clearly defined | - Suspension/kill-switch documentation<br>- Suspension test results<br>- Fallback process documentation<br>- Decision authority matrix | Pass: Kill-switch capability exists for all production AI systems, can be activated within defined timeframes, fallback processes documented, and decision authority defined. Fail: No suspension capability, untested, no fallback process, or unclear authority |
| AI-13 | Verify ongoing monitoring and human oversight of AI systems | 1. Verify that AI systems have defined levels of human oversight (human-in-the-loop, human-on-the-loop, or human-over-the-loop) proportionate to risk<br>2. Check that automated decisions can be overridden by authorised personnel<br>3. Verify that monitoring includes outcome tracking to detect unintended consequences<br>4. Confirm that escalation procedures exist for anomalous AI behaviour | - Human oversight framework<br>- Override capability evidence<br>- Outcome monitoring dashboard/reports<br>- Escalation procedures | Pass: Human oversight level is defined and proportionate, override capability exists, outcomes are tracked, and escalation procedures are in place. Fail: No human oversight framework, no override capability, or no outcome tracking |
| AI-14 | Verify transparency and disclosure requirements are met | 1. Identify AI systems that interact with or make decisions about customers<br>2. Verify that customers are informed when AI is used in decision-making (where required)<br>3. Check that explanations can be provided for AI-driven decisions (explainability)<br>4. Verify that a complaints/appeals process exists for AI-driven decisions<br>5. Review sample disclosures for adequacy | - Disclosure policy<br>- Customer notification evidence<br>- Explainability mechanism documentation<br>- Complaints/appeals process<br>- Sample disclosures | Pass: Customers are informed of AI use, explanations can be provided for decisions, and a complaints/appeals process exists. Fail: No customer disclosure, no explainability capability, or no complaints process |
| AI-15 | Verify AI/emerging tech incident management | 1. Review the incident management procedure for AI/emerging tech-specific incidents (model failure, biased outcomes, data poisoning, adversarial attacks)<br>2. Verify that AI-specific incident categories and severity levels are defined<br>3. Check incident log for AI-related incidents in the past 12 months and review response quality<br>4. Verify lessons learned are fed back into model improvement and governance | - AI incident management procedure<br>- AI incident categories and severity matrix<br>- AI incident log and response records<br>- Lessons learned register | Pass: AI-specific incident procedures exist, incidents are categorised and responded to appropriately, and lessons learned are fed back. Fail: No AI-specific incident procedures, or incidents not tracked |

---

### Phase 3: Reporting

| Step | Activity | Deliverable |
|------|----------|-------------|
| R-01 | Consolidate all test results and assign risk ratings (High/Medium/Low) to each finding | Findings register with risk ratings |
| R-02 | Draft recommendations with specific remediation steps, responsible parties, and timelines | Recommendations tracker |
| R-03 | Conduct findings walkthrough with FI AI/emerging tech, risk, and compliance teams | Walkthrough meeting minutes |
| R-04 | Prepare the formal AI/Emerging Tech IESP report in Appendix 7 Part A format | Final report |
| R-05 | Obtain FI management sign-off on the report and management action plans | Signed report and action plans |

---

### Phase 4: Board Deliberation Support

| Step | Activity | Deliverable |
|------|----------|-------------|
| B-01 | Prepare executive summary for the designated board committee (per 8.3), highlighting AI-specific risks, ethical considerations, and regulatory compliance | Board presentation deck |
| B-02 | Attend the designated committee meeting to present findings and respond to queries | Attendance record and meeting minutes |
| B-03 | Document any additional directives and incorporate into final report | Updated report (if required) |

---

### Appendices

- **Appendix A:** Document Request List (DRL) template
- **Appendix B:** Appendix 9 control mapping matrix
- **Appendix C:** Appendix 7 Part A report template
- **Appendix D:** Risk rating methodology
- **Appendix E:** AI model risk tiering criteria
- **Appendix F:** Common AI/ML risk taxonomy
