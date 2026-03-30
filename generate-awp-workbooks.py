#!/usr/bin/env python3
"""Generate IESP AWP Excel workbooks in DAC format (12-column working paper)."""

import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# Styles
HEADER_FONT = Font(name='Calibri', bold=True, size=11, color='FFFFFF')
HEADER_FILL = PatternFill(start_color='2F5496', end_color='2F5496', fill_type='solid')
SECTION_FONT = Font(name='Calibri', bold=True, size=11, color='2F5496')
SECTION_FILL = PatternFill(start_color='D6E4F0', end_color='D6E4F0', fill_type='solid')
BODY_FONT = Font(name='Calibri', size=10)
TITLE_FONT = Font(name='Calibri', bold=True, size=14, color='2F5496')
SUBTITLE_FONT = Font(name='Calibri', bold=True, size=12, color='2F5496')
LABEL_FONT = Font(name='Calibri', bold=True, size=10)
VALUE_FONT = Font(name='Calibri', size=10)
THIN_BORDER = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)
WRAP_ALIGN = Alignment(wrap_text=True, vertical='top')
CENTER_ALIGN = Alignment(horizontal='center', vertical='top', wrap_text=True)

# Column widths for assessment sheets
COL_WIDTHS = {
    'A': 10,   # Ref
    'B': 20,   # Control
    'C': 28,   # Sub-Procedure
    'D': 50,   # Assessment Procedures
    'E': 35,   # Expected Evidence
    'F': 14,   # Method
    'G': 30,   # Procedures Performed
    'H': 25,   # Evidence Obtained
    'I': 12,   # Evidence Ref
    'J': 30,   # Observation / Findings
    'K': 16,   # Conclusion
    'L': 30,   # Recommendations
}

ASSESSMENT_HEADERS = [
    'Ref', 'Control', 'Sub-Procedure', 'Assessment Procedures',
    'Expected Evidence', 'Method', 'Procedures Performed',
    'Evidence Obtained', 'Evidence Ref', 'Observation / Findings',
    'Conclusion', 'Recommendations'
]


def apply_col_widths(ws):
    for col_letter, width in COL_WIDTHS.items():
        ws.column_dimensions[col_letter].width = width


def write_header_row(ws, row):
    for col, header in enumerate(ASSESSMENT_HEADERS, 1):
        cell = ws.cell(row=row, column=col, value=header)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL
        cell.alignment = CENTER_ALIGN
        cell.border = THIN_BORDER


def write_section_row(ws, row, title):
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=12)
    cell = ws.cell(row=row, column=1, value=title)
    cell.font = SECTION_FONT
    cell.fill = SECTION_FILL
    cell.border = THIN_BORDER
    for col in range(2, 13):
        ws.cell(row=row, column=col).fill = SECTION_FILL
        ws.cell(row=row, column=col).border = THIN_BORDER


def write_test_row(ws, row, ref, control, sub_proc, procedures, evidence, method='Inspection'):
    data = [ref, control, sub_proc, procedures, evidence, method, '', '', '', '', '', '']
    for col, value in enumerate(data, 1):
        cell = ws.cell(row=row, column=col, value=value)
        cell.font = BODY_FONT
        cell.alignment = WRAP_ALIGN
        cell.border = THIN_BORDER


def create_methodology_sheet(wb, engagement_name, regulatory_basis, scope_desc,
                              assessment_covers, engagement_type_label):
    ws = wb.active
    ws.title = 'Methodology & Approach'

    # Column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 60
    for col in 'CDEFGHIJKL':
        ws.column_dimensions[col].width = 12

    r = 1
    # Title
    ws.merge_cells(f'A{r}:L{r}')
    cell = ws.cell(row=r, column=1, value=f'INDEPENDENT ASSESSMENT — METHODOLOGY & APPROACH')
    cell.font = TITLE_FONT
    r += 1
    ws.merge_cells(f'A{r}:L{r}')
    cell = ws.cell(row=r, column=1, value=f'{engagement_name}')
    cell.font = SUBTITLE_FONT
    r += 2

    # Engagement details
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='ENGAGEMENT DETAILS').font = SUBTITLE_FONT
    r += 1
    details = [
        ('Entity Name:', '[Entity Name]'),
        ('Engagement Type:', engagement_type_label),
        ('Regulatory Basis:', regulatory_basis),
        ('Assessment Date:', '[DD/MM/YYYY]'),
        ('Assessment Period:', '[Start Date] to [End Date]'),
        ('Lead Assessor:', '[Name, Qualification]'),
        ('Engagement Reference:', '[Ref Number]'),
        ('Report Classification:', 'Confidential (Sulit)'),
    ]
    for label, value in details:
        ws.cell(row=r, column=1, value=label).font = LABEL_FONT
        ws.cell(row=r, column=2, value=value).font = VALUE_FONT
        r += 1
    r += 1

    # Scope
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='SCOPE OF ASSESSMENT').font = SUBTITLE_FONT
    r += 1
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value=scope_desc).font = VALUE_FONT
    ws.cell(row=r, column=1).alignment = WRAP_ALIGN
    r += 1
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value=assessment_covers).font = VALUE_FONT
    ws.cell(row=r, column=1).alignment = WRAP_ALIGN
    r += 2

    # Engagement mode
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='ENGAGEMENT MODE').font = SUBTITLE_FONT
    r += 1
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='Design Adequacy (Pre-Implementation):').font = LABEL_FONT
    r += 1
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='Assess whether proposed/planned controls are designed to meet the requirement. Evidence is primarily documentary: architecture designs, policies, vendor assessments, staging test results.').font = VALUE_FONT
    ws.cell(row=r, column=1).alignment = WRAP_ALIGN
    r += 1
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='Operating Effectiveness (Independent Attestation):').font = LABEL_FONT
    r += 1
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='Assess whether controls operated effectively during the assessment period. Evidence is observation, sampling, re-performance, system-generated logs. Requires defined sampling methodology.').font = VALUE_FONT
    ws.cell(row=r, column=1).alignment = WRAP_ALIGN
    r += 2

    # Assessment methods
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='ASSESSMENT METHODS').font = SUBTITLE_FONT
    r += 1
    methods = [
        ('Inspection', 'Examination of documents, records, policies, configurations, and tangible evidence.'),
        ('Inquiry', 'Interviews with management, process owners, and staff to understand controls and decision-making.'),
        ('Observation', 'Direct observation of processes, systems, and activities being performed.'),
        ('Confirmation', 'Verification with external or independent parties.'),
        ('Re-performance', 'IESP independently re-performs the control procedure to verify it operates as designed.'),
    ]
    for method, desc in methods:
        ws.cell(row=r, column=1, value=method).font = LABEL_FONT
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=2).alignment = WRAP_ALIGN
        r += 1
    r += 1

    # Conclusion scale
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='CONCLUSION SCALE').font = SUBTITLE_FONT
    r += 1
    conclusions = [
        ('Compliant', 'Control/requirement fully implemented and operating effectively. Evidence supports regulatory criteria are met.'),
        ('Partially Compliant', 'Implemented but with gaps in scope, coverage, documentation, or effectiveness. Some criteria met.'),
        ('Non-Compliant', 'Absent, fundamentally deficient, or not operating. Regulatory criteria not met.'),
        ('N/A', 'Not applicable to entity\'s operations. Justification documented.'),
    ]
    for conc, desc in conclusions:
        ws.cell(row=r, column=1, value=conc).font = LABEL_FONT
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=2).alignment = WRAP_ALIGN
        r += 1
    r += 1

    # Evidence hierarchy
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='EVIDENCE HIERARCHY (prefer higher-ranked evidence)').font = SUBTITLE_FONT
    r += 1
    evidence_ranks = [
        ('Rank 1', 'Direct observation — IESP directly observes control in operation'),
        ('Rank 2', 'Independent confirmation — Third-party evidence (SOC 2, certifications)'),
        ('Rank 3', 'System-generated — Logs, configurations without manual intervention'),
        ('Rank 4', 'Re-performance — IESP re-performs control procedure'),
        ('Rank 5', 'Documentary — Policies, procedures, meeting minutes'),
        ('Rank 6', 'Inquiry — Verbal representations from FI personnel'),
    ]
    for rank, desc in evidence_ranks:
        ws.cell(row=r, column=1, value=rank).font = LABEL_FONT
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=2).alignment = WRAP_ALIGN
        r += 1
    r += 1

    # Limitations
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='LIMITATIONS').font = SUBTITLE_FONT
    r += 1
    limitations = [
        '1. Limited assurance engagement — conclusions based on procedures performed, not absolute assurance.',
        '2. Point-in-time assessment (design adequacy) or period assessment (operating effectiveness). Does not guarantee continued compliance.',
        '3. Reliance on management representations and documentation provided.',
        '4. Scope guided by BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025). BNM may update requirements.',
        '5. Does not constitute legal or regulatory advice.',
        '6. The IESP remains solely responsible for the sufficiency of work performed and conclusions reached.',
    ]
    for lim in limitations:
        ws.merge_cells(f'A{r}:L{r}')
        ws.cell(row=r, column=1, value=lim).font = VALUE_FONT
        ws.cell(row=r, column=1).alignment = WRAP_ALIGN
        r += 1
    r += 1

    # Sign-off
    ws.merge_cells(f'A{r}:L{r}')
    ws.cell(row=r, column=1, value='SIGN-OFF').font = SUBTITLE_FONT
    r += 1
    signoffs = ['Lead Assessor:', 'Quality Reviewer:', 'Entity Representative:']
    for s in signoffs:
        ws.cell(row=r, column=1, value=s).font = LABEL_FONT
        ws.cell(row=r, column=2, value='________________________').font = VALUE_FONT
        ws.cell(row=r, column=6, value='Date:').font = LABEL_FONT
        ws.cell(row=r, column=7, value='______________').font = VALUE_FONT
        r += 1

    return ws


# ============================================================
# PART D TEST STEPS (shared across all workbooks)
# ============================================================
PART_D_SECTIONS = [
    ('Item 1(a) — Access Control', [
        ('PD-01', 'Access Control', 'Access control policies and mechanisms',
         '1. Obtain the FI\'s access control policy and supporting standards.\n2. Verify policy covers user registration, de-registration, access provisioning, and privilege management.\n3. Sample 20 user accounts — verify access rights are consistent with job roles (least privilege principle).\n4. Check that access reviews are performed periodically (at least quarterly for privileged accounts, semi-annually for standard users).\n5. Verify access revocation upon staff termination or role change — sample 10 recent leavers/transfers.',
         'Access control policy; User access provisioning records; Access review reports; HR leaver/transfer list vs. access revocation logs',
         'Inspection'),
        ('PD-02', 'Access Control', 'Privileged access management',
         '1. Obtain the privileged access management (PAM) policy or standard.\n2. Obtain the list of all privileged accounts (system admin, DBA, root, domain admin).\n3. Verify privileged accounts are individually assigned (no shared privileged accounts) or, if shared, compensating controls exist (e.g., PAM vault with session recording).\n4. Check that privileged access is time-bound and subject to approval workflow.\n5. Review privileged session logs for the past 3 months for anomalies.',
         'PAM policy; Privileged account inventory; PAM tool configuration and logs; Session recording samples',
         'Inspection'),
    ]),
    ('Item 1(b) — Physical and Environmental Security', [
        ('PD-03', 'Physical & Environmental Security', 'Physical security controls',
         '1. Identify all sensitive areas (data centres, server rooms, network rooms, tape vaults).\n2. Verify multi-layered physical access controls (badge, biometric, PIN) at each sensitive area.\n3. Review visitor management procedures — check that visitors are registered, escorted, and logged.\n4. Verify CCTV coverage at entry/exit points and sensitive areas with adequate retention period (minimum 90 days).\n5. Sample-check physical access logs against approved access lists.',
         'Physical security policy; Access control system configuration; Visitor logs; CCTV coverage map and retention settings; Physical access log reconciliation',
         'Inspection / Observation'),
        ('PD-04', 'Physical & Environmental Security', 'Environmental controls',
         '1. Verify fire detection and suppression systems are installed and current on inspections.\n2. Check water leak detection in areas housing technology assets.\n3. Verify temperature and humidity monitoring with defined thresholds and alerts.\n4. Confirm environmental incident response procedures exist and have been tested.',
         'Fire system inspection certificates; Water leak detection layout; Environmental monitoring dashboards; Incident response procedures and test records',
         'Inspection / Observation'),
    ]),
    ('Item 1(c) — Operations Security', [
        ('PD-05', 'Operations Security', 'Operational procedures and controls',
         '1. Obtain documented operating procedures for technology operations (change management, capacity management, backup and restore, malware protection).\n2. Verify change management — sample 10 changes and confirm each has request, assessment, approval, testing, implementation, and post-implementation review.\n3. Verify backup procedures — confirm critical systems are backed up per defined schedule and restore tests are performed periodically.\n4. Verify malware protection — confirm endpoint and server anti-malware is deployed, signatures are current, and incidents are logged.',
         'Operating procedures documentation; 10 sampled change records; Backup schedule and restore test results; Anti-malware deployment and signature status reports',
         'Inspection'),
        ('PD-06', 'Operations Security', 'Vulnerability management and patching',
         '1. Obtain the FI\'s vulnerability management policy and patching SLAs (e.g., critical patches within 14 days).\n2. Review the most recent vulnerability scan results for infrastructure and applications.\n3. Check patch compliance rates — verify critical and high vulnerabilities are remediated within SLA.\n4. Verify that exceptions are formally risk-accepted with documented compensating controls.',
         'Vulnerability management policy; Vulnerability scan reports; Patch compliance dashboard; Risk acceptance records for exceptions',
         'Inspection'),
    ]),
    ('Item 1(d) — Communications Security', [
        ('PD-07', 'Communications Security', 'Network security and secure communications',
         '1. Review network segmentation — verify sensitive zones (e.g., DMZ, internal, management) are appropriately segmented.\n2. Verify firewall rules — sample 20 rules and confirm they follow least-privilege, deny-by-default principles; check for overly permissive rules (e.g., any-any).\n3. Confirm encryption of data in transit for external and sensitive internal communications (TLS 1.2 minimum).\n4. Verify secure configuration of email, messaging, and file transfer systems.\n5. Check that network monitoring and IDS/IPS are deployed at critical network boundaries.',
         'Network architecture diagram with zone segmentation; Firewall rule base sample; TLS configuration evidence; IDS/IPS deployment and alert records',
         'Inspection'),
    ]),
    ('Item 1(e) — Incident Management', [
        ('PD-08', 'Incident Management', 'Incident management framework',
         '1. Obtain the information security incident management policy and procedures.\n2. Verify incident classification scheme (severity levels with defined response and escalation timelines).\n3. Review the incident log for the past 12 months — check completeness, classification accuracy, and timeliness of response.\n4. Verify that significant incidents triggered root cause analysis (RCA) and that RCA findings led to corrective/preventive actions.\n5. Confirm regulatory notification procedures for reportable incidents (per BNM requirements).',
         'Incident management policy and procedures; Incident classification matrix; Incident log (12 months); RCA reports for significant incidents; Regulatory notification records (if any)',
         'Inspection'),
        ('PD-09', 'Incident Management', 'Detection and response capabilities',
         '1. Confirm the FI operates a SOC (internal or outsourced) with 24/7 monitoring capability.\n2. Verify SIEM deployment — check that critical log sources are onboarded and correlation rules are active.\n3. Review SOC alert triage process and sample 15 alerts — verify appropriate investigation and disposition.\n4. Confirm incident response playbooks exist for common scenarios (ransomware, data breach, DDoS, insider threat).\n5. Verify incident response drills/tabletop exercises are conducted at least annually.',
         'SOC operational documentation; SIEM log source inventory and correlation rules; 15 sampled alert triage records; Incident response playbooks; Drill/tabletop exercise reports',
         'Inspection / Inquiry'),
    ]),
    ('Item 1(f) — Business Continuity', [
        ('PD-10', 'Business Continuity', 'Security in BCP/DRP',
         '1. Obtain the FI\'s business continuity plan (BCP) and IT disaster recovery plan (DRP).\n2. Verify that information security requirements are explicitly addressed in the BCP/DRP.\n3. Check that BCP/DRP includes scenarios for cyber incidents (e.g., ransomware, data centre loss due to cyber attack).\n4. Verify that recovery procedures include security validation steps before returning systems to production.',
         'BCP and IT DRP; Security requirements in BCP/DRP; Cyber incident scenarios; Recovery security validation checklists',
         'Inspection'),
        ('PD-11', 'Business Continuity', 'BCP/DRP testing with security controls',
         '1. Review the most recent BCP/DRP test plan and results.\n2. Verify that security controls were tested during the DR exercise.\n3. Confirm that test findings included security observations and that these were remediated.\n4. Verify DR site/environment maintains equivalent security posture to production.',
         'BCP/DRP test plan and results; Security test components within DR exercise; DR site security assessment; Test findings remediation tracker',
         'Inspection'),
        ('PD-12', 'Business Continuity', 'Redundancy of security infrastructure',
         '1. Identify critical security infrastructure (firewalls, IDS/IPS, SIEM, PAM, PKI) and verify redundancy/HA configuration.\n2. Confirm security infrastructure failover has been tested.\n3. Verify that security monitoring continues during failover/DR activation.\n4. Check that security tool licenses and subscriptions remain valid at DR site.',
         'Security infrastructure HA architecture; Failover test records; DR monitoring evidence; License/subscription records for DR',
         'Inspection'),
    ]),
    ('Item 2(a) — Customer Identity Authentication', [
        ('PD-13', 'Customer Authentication', 'Session and MITM protection',
         '1. Review the online service architecture for session management controls.\n2. Verify TLS implementation — check certificate validity, protocol version (TLS 1.2+), cipher suite strength, and HSTS enforcement.\n3. Confirm session tokens are cryptographically random, have appropriate expiry, and are invalidated on logout.\n4. Check for anti-session-fixation controls (new session ID on authentication).\n5. Verify certificate pinning for mobile applications (where applicable).',
         'TLS configuration scan results; Session management configuration; Application security assessment results; Mobile app certificate pinning evidence',
         'Inspection'),
        ('PD-14', 'Customer Authentication', 'Internal controls for online systems',
         '1. Verify application hardening — check that unnecessary services, default accounts, and debug modes are disabled in production.\n2. Review application security testing results (SAST, DAST, or penetration test) for customer-facing applications.\n3. Confirm database security — verify database access controls, encryption of sensitive data at rest, and database activity monitoring.\n4. Check that internal systems supporting online services are segmented from general corporate network.',
         'Hardening standards and compliance reports; Application security test reports; Database security configuration; Network segmentation evidence',
         'Inspection'),
        ('PD-15', 'Customer Authentication', 'Multi-level authentication',
         '1. Review the FI\'s authentication architecture for online services.\n2. Verify multi-factor authentication (MFA) is implemented for customer login and high-risk transactions.\n3. Check for out-of-band authentication mechanisms (e.g., OTP via SMS/push, hardware token).\n4. Verify real-time verification controls for high-value or unusual transactions.\n5. Assess the strength and appropriateness of authentication methods relative to transaction risk.',
         'Authentication architecture documentation; MFA configuration evidence; OTP/out-of-band mechanism design; Transaction risk-based authentication rules',
         'Inspection'),
        ('PD-16', 'Customer Authentication', 'Session handling and credential storage',
         '1. Verify session timeout is enforced (idle timeout and absolute timeout).\n2. Confirm concurrent session controls.\n3. Verify authentication credentials are stored using strong hashing (e.g., bcrypt, Argon2) with salting.\n4. Check that the authentication database is access-restricted, encrypted at rest, and backed up securely.\n5. Review authentication failure handling — account lockout after defined failed attempts.',
         'Session management configuration; Password hashing algorithm evidence; Authentication database access controls; Account lockout configuration',
         'Inspection'),
        ('PD-17', 'Customer Authentication', 'Cryptographic implementation',
         '1. Review the FI\'s cryptographic standards — verify use of recognised algorithms (AES-256, RSA-2048+, ECDSA P-256+).\n2. Verify key management practices — key generation, storage (HSM or equivalent), rotation schedule, and destruction.\n3. Check that deprecated algorithms (DES, 3DES, RC4, MD5, SHA-1) are not used for security functions.\n4. Verify cryptographic implementation has been reviewed or tested.',
         'Cryptographic standards document; Key management procedures; HSM configuration and inventory; Crypto assessment results',
         'Inspection'),
    ]),
    ('Item 2(b) — Transaction Authentication', [
        ('PD-18', 'Transaction Authentication', 'Proof of origin and integrity',
         '1. Review transaction signing or message authentication mechanisms (e.g., HMAC, digital signatures).\n2. Verify that transaction records include origin identification, timestamp, content hash, and integrity verification.\n3. Confirm audit trails for transactions are tamper-evident and retained per regulatory requirements.\n4. Check that transaction logs provide sufficient detail for dispute resolution.',
         'Transaction authentication mechanism design; Sample transaction records; Audit trail configuration and tamper-evidence controls; Log retention policy',
         'Inspection'),
        ('PD-19', 'Transaction Authentication', 'Secure delivery and mutual authentication',
         '1. Verify the chosen delivery channel for transactions is secured end-to-end.\n2. Check that the FI alerts users on specific transaction types requiring further authentication.\n3. Verify mutual authentication or appropriate digital certification for B2B or high-assurance channels.\n4. Review the criteria and thresholds that trigger additional authentication.',
         'Channel security architecture; Transaction alert configuration and rules; Mutual authentication or digital certificate implementation; Authentication trigger criteria',
         'Inspection'),
    ]),
    ('Item 2(c) — Segregation of Duties', [
        ('PD-20', 'Segregation of Duties', 'Dual control for online transactions',
         '1. Identify critical functions in online transaction systems (user management, transaction limits, system configuration).\n2. Verify dual control (maker-checker) is implemented for critical and high-risk operations.\n3. Review access control matrices — verify no single user can initiate and approve the same transaction.\n4. Verify controls to detect and prevent unauthorised access.',
         'Access control matrices; Maker-checker configuration evidence; Dual control workflow screenshots; Unauthorised access detection controls',
         'Inspection'),
        ('PD-21', 'Segregation of Duties', 'Authorisation database integrity',
         '1. Verify the authorisation database is tamper-resistant — check access controls, change logging, and integrity monitoring.\n2. Confirm that changes to authorisation data require formal approval and are logged.\n3. Obtain the list of privileged users for online transaction systems and verify periodic review (at least quarterly).\n4. Check that privileged user reviews result in revocation of unnecessary access.',
         'Authorisation database access controls and integrity monitoring; Change logs; Privileged user review records (quarterly); Revocation evidence',
         'Inspection'),
    ]),
    ('Item 2(d) — Data Integrity', [
        ('PD-22', 'Data Integrity', 'End-to-end encryption and multi-layer security',
         '1. Verify end-to-end encryption for all external communications involving sensitive or transaction data.\n2. Review multi-layer network security architecture — verify defence-in-depth.\n3. Confirm each security layer is independently managed and monitored.\n4. Verify security devices are current on firmware/signatures.',
         'Encryption architecture; Multi-layer security architecture diagram; Security device inventory with firmware/signature status; Management and monitoring evidence',
         'Inspection'),
        ('PD-23', 'Data Integrity', 'Absence of single points of failure',
         '1. Review the network architecture for single points of failure (SPOF) in components supporting online services.\n2. Verify redundancy at each critical network layer.\n3. Confirm failover mechanisms have been tested within the past 12 months.\n4. Check that SPOF analysis is documented and periodically refreshed.',
         'Network architecture with redundancy annotations; SPOF analysis document; Failover test results; SPOF analysis review history',
         'Inspection'),
        ('PD-24', 'Data Integrity', 'Security assessment and audit trails',
         '1. Obtain the most recent network security assessment and penetration test reports.\n2. Verify testing was conducted by a qualified independent party within the past 12 months.\n3. Confirm that identified vulnerabilities have been remediated or risk-accepted.\n4. Verify audit trail capabilities — all transaction and administrative activities are logged.\n5. Confirm audit logs are protected from tampering, centrally collected, and retained per policy.',
         'Penetration test report and remediation tracker; Network security assessment report; Audit trail configuration and sample logs; Log integrity and retention controls',
         'Inspection'),
        ('PD-25', 'Data Integrity', 'Data confidentiality and risk-based authentication',
         '1. Verify that confidentiality of customer and transaction information is preserved through encryption, masking, and access controls.\n2. Confirm data classification is applied to online service data.\n3. Verify stronger authentication is required for higher-risk transactions.\n4. Check that customers receive timely notifications of completed transactions.',
         'Data classification scheme; Encryption and masking configuration; Risk-based authentication rules; Customer notification configuration and samples',
         'Inspection'),
    ]),
    ('Item 2(e) — Mobile Device Risks', [
        ('PD-26', 'Mobile Device Security', 'Mobile application security baseline',
         '1. Confirm the mobile application enforces minimum secure OS version requirements and prevents execution on compromised (jailbroken/rooted) devices.\n2. Review the most recent mobile application penetration test report.\n3. Verify that identified vulnerabilities have been remediated.\n4. Confirm secure end-to-end communication between the mobile device and host systems (certificate pinning, TLS 1.2+).',
         'OS version enforcement configuration; Jailbreak/root detection implementation; Mobile penetration test report; Remediation evidence; Communication security configuration',
         'Inspection'),
        ('PD-27', 'Mobile Device Security', 'Mobile data protection and storage',
         '1. Review the mobile application\'s data storage practices — verify sensitive information is not stored on the device or is stored only in secure enclaves/keystores.\n2. Confirm that application cache, logs, and temporary files do not contain sensitive data.\n3. Verify that clipboard access is restricted for sensitive fields.\n4. Check that data is wiped on application uninstall or remote wipe capability exists.',
         'Mobile application security architecture; Data storage review results; Secure enclave/keystore usage evidence; Remote wipe capability documentation',
         'Inspection'),
        ('PD-28', 'Mobile Device Security', 'Transaction notification and code controls',
         '1. Verify users are notified of successful transactions via push notification, SMS, or email.\n2. Verify users are notified of suspicious transactions with ability to take immediate action.\n3. Confirm that a unique code is generated per transaction where applicable (e.g., TAC, OTP).\n4. Verify timely expiry of transaction codes (typically 2-5 minutes) and codes are single-use.',
         'Transaction notification configuration; Suspicious transaction alert rules and samples; Transaction code generation mechanism; Code expiry and single-use configuration',
         'Inspection'),
        ('PD-29', 'Mobile Device Security', 'App distribution and fake app monitoring',
         '1. Verify controls over uploading of the application to distribution platforms — check that only authorised personnel can publish.\n2. Confirm continuous monitoring for fake or fraudulent applications impersonating the FI.\n3. Verify that a takedown process exists and has been exercised.\n4. Review the history of fake application incidents and response timelines.',
         'Application publishing access controls and process; Fake application monitoring service/tool; Takedown process documentation; Fake application incident log',
         'Inspection'),
    ]),
]


def add_part_d_sheet(wb, sheet_name='Appendix 7 Part D'):
    ws = wb.create_sheet(title=sheet_name)
    apply_col_widths(ws)

    r = 1
    write_header_row(ws, r)
    r += 1

    for section_title, tests in PART_D_SECTIONS:
        write_section_row(ws, r, section_title)
        r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1

    return ws


# ============================================================
# WORKBOOK 1: CLOUD IESP
# ============================================================
def create_cloud_workbook():
    wb = openpyxl.Workbook()
    create_methodology_sheet(
        wb,
        engagement_name='BNM RMiT IESP — Cloud Services Assessment',
        regulatory_basis='Paragraph 17.1 / Appendix 7, mapped to Appendix 10',
        scope_desc='This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Appendix 7 and Appendix 10. The objective is to assess cloud service controls for the purpose of forming the IESP negative attestation under Appendix 7 Part C.',
        assessment_covers='Assessment covers: (1) Appendix 10 Part A — Cloud Governance (7 areas), (2) Appendix 10 Part B — Cloud Design and Control (14 areas), (3) Appendix 7 Part D — Minimum Controls (universal baseline).',
        engagement_type_label='Cloud IESP Assessment (Pre-Implementation or Independent Attestation)'
    )

    # Sheet 2: Appendix 10 Part A
    ws = wb.create_sheet(title='App 10 Part A - Governance')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    part_a_sections = [
        ('A1 — Cloud Risk Management', [
            ('CLD-01', 'Cloud Risk Management', 'Cloud-specific risk assessment',
             '1. Obtain the FI\'s cloud risk assessment framework.\n2. Verify it covers: data sovereignty, vendor lock-in, shared tenancy, supply chain, regulatory compliance.\n3. Check that risks are assessed per CSP and per service.\n4. Verify the risk assessment is reviewed at least annually.',
             'Cloud risk assessment framework; Risk register (cloud section); Review/approval records',
             'Inspection'),
            ('CLD-02', 'Cloud Risk Management', 'Cloud risk appetite and tolerance',
             '1. Check that the FI has defined what can and cannot be placed in cloud.\n2. Verify data classification rules for cloud placement.\n3. Confirm risk appetite is approved by the board or designated committee.',
             'Cloud risk appetite statement; Data classification-to-cloud mapping; Board/committee approval',
             'Inspection'),
        ]),
        ('A2 — Cloud Usage Policy', [
            ('CLD-03', 'Cloud Usage Policy', 'Cloud usage governance',
             '1. Obtain the FI\'s cloud usage policy.\n2. Verify it covers: approved CSPs, approved service/deployment models, data classification requirements, security baseline requirements, approval workflow for new cloud services.\n3. Check the policy is communicated to relevant stakeholders.\n4. Verify adherence — sample 3 recent cloud service adoptions and check they followed the policy.',
             'Cloud usage policy; Communication/awareness records; Sample cloud adoption records',
             'Inspection'),
        ]),
        ('A3 — Due Diligence', [
            ('CLD-04', 'Due Diligence', 'CSP evaluation due diligence',
             '1. Obtain due diligence procedures and checklists for CSP evaluation.\n2. For each in-scope CSP, verify that due diligence was performed covering: financial viability, security capabilities, regulatory compliance, data residency, subcontracting, and business continuity.\n3. Verify due diligence is refreshed periodically (at least annually for critical CSPs).',
             'Due diligence procedure; Completed due diligence reports per CSP; Refresh schedule and records',
             'Inspection'),
        ]),
        ('A4 — CSP Certifications', [
            ('CLD-05', 'CSP Certifications', 'Independent assurance reports',
             '1. Obtain current SOC 2 Type II, ISO 27001, and CSA STAR reports for each CSP.\n2. Verify the reports cover the services used by the FI.\n3. Review any exceptions, qualifications, or control deficiencies noted in the reports.\n4. Check that the FI has assessed the impact of any reported deficiencies.\n5. Verify complementary user entity controls (CUECs) identified in SOC reports are implemented by the FI.',
             'SOC 2 Type II reports; ISO 27001 certificates; CSA STAR reports; FI\'s review of report findings; CUEC implementation evidence',
             'Inspection'),
        ]),
        ('A5 — Contract Management', [
            ('CLD-06', 'Contract Management', 'Regulatory contract provisions',
             '1. Review contracts with each in-scope CSP.\n2. Check for: right to audit, data ownership and portability, data residency and sovereignty, breach notification obligations, subcontracting controls, termination and exit provisions, regulatory access rights (BNM inspection).\n3. Verify contracts are reviewed by legal and compliance.',
             'CSP contracts; Legal/compliance review records; Contract compliance checklist',
             'Inspection'),
        ]),
        ('A6 — Oversight over CSPs', [
            ('CLD-07', 'CSP Oversight', 'Ongoing CSP monitoring',
             '1. Review the FI\'s CSP oversight framework.\n2. Check that CSP performance is monitored against SLAs.\n3. Verify periodic service review meetings are held with CSPs.\n4. Confirm that CSP incident notifications are received, tracked, and assessed.\n5. Check that the FI monitors CSP security advisories and applies relevant patches/mitigations.',
             'CSP oversight framework; SLA performance reports; Service review meeting minutes; CSP incident tracking records; Security advisory tracking',
             'Inspection'),
        ]),
        ('A7 — Skilled Personnel', [
            ('CLD-08', 'Skilled Personnel', 'Cloud team capability',
             '1. Review cloud team structure, roles, and responsibilities.\n2. Verify cloud-specific certifications held by key personnel.\n3. Check that a training and development plan exists for cloud skills.\n4. Assess whether the FI can independently assess CSP configurations and security posture.',
             'Cloud team organisational chart; Personnel certification records; Training plan; Evidence of independent assessment capability',
             'Inspection / Inquiry'),
        ]),
    ]

    for section_title, tests in part_a_sections:
        write_section_row(ws, r, section_title)
        r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1

    # Sheet 3: Appendix 10 Part B
    ws = wb.create_sheet(title='App 10 Part B - Controls')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    part_b_sections = [
        ('B1 — Cloud Architecture', [
            ('CLD-09', 'Cloud Architecture', 'Resilience and security design',
             '1. Obtain the FI\'s cloud architecture design documents and diagrams.\n2. Verify multi-AZ or multi-region deployment for critical workloads.\n3. Check that architecture follows well-architected framework principles.\n4. Verify network architecture in cloud (VPC/VNET design, subnet segmentation, security groups, NACLs).\n5. Confirm architecture has been reviewed by qualified cloud architects.',
             'Cloud architecture documents; Multi-AZ/region deployment evidence; Well-architected review reports; VPC/VNET design documents',
             'Inspection'),
        ]),
        ('B2 — CI/CD and IaC', [
            ('CLD-10', 'CI/CD Security', 'Pipeline security controls',
             '1. Review CI/CD pipeline architecture and tools.\n2. Verify security gates are embedded in the pipeline (SAST, DAST, SCA, container scanning).\n3. Check that deployment to production requires approval and cannot be bypassed.\n4. Verify pipeline configuration is version-controlled and access-restricted.\n5. Check that secrets are not hardcoded in pipeline configurations.',
             'CI/CD architecture documentation; Security gate configuration; Approval workflow evidence; Pipeline access controls; Secrets management configuration',
             'Inspection'),
            ('CLD-11', 'IaC Governance', 'Infrastructure as Code security',
             '1. Identify IaC tools in use (Terraform, CloudFormation, ARM, Pulumi).\n2. Verify IaC templates are stored in version control with change approval.\n3. Check that IaC templates are scanned for security misconfigurations before deployment.\n4. Verify that manual infrastructure changes are detected and reconciled with IaC state.\n5. Confirm IaC state files are stored securely (encrypted, access-controlled).',
             'IaC tool inventory; Version control repository; IaC scanning tool configuration; Drift detection mechanism; State file storage configuration',
             'Inspection'),
        ]),
        ('B3 — Virtualisation and Containerisation', [
            ('CLD-12', 'Container Security', 'Container and virtualisation controls',
             '1. Identify container platforms in use (Kubernetes, ECS, AKS, GKE).\n2. Verify container images are sourced from approved registries and scanned for vulnerabilities.\n3. Check that containers run with least-privilege (non-root, read-only filesystem where possible).\n4. Verify pod/container network policies enforce segmentation.\n5. Check that orchestrator is hardened per CIS benchmarks.',
             'Container platform inventory; Image scanning reports; Container runtime security configurations; Network policy configurations; CIS benchmark compliance reports',
             'Inspection'),
        ]),
        ('B4 — Change Management', [
            ('CLD-13', 'Change Management', 'Cloud change controls',
             '1. Review the cloud change management procedure.\n2. Sample 10 recent cloud infrastructure/configuration changes.\n3. Verify each change has: request, risk assessment, approval, implementation plan, testing, and post-implementation validation.\n4. Check that changes to security-critical configurations (IAM, network, encryption) have enhanced approval.',
             'Cloud change management procedure; 10 sampled change records; Enhanced approval evidence for security changes',
             'Inspection'),
        ]),
        ('B5 — Backup and Recovery', [
            ('CLD-14', 'Backup & Recovery', 'Cloud backup arrangements',
             '1. Review cloud backup policy and configuration for critical workloads.\n2. Verify backup frequency, retention periods, and storage locations (cross-region for critical data).\n3. Check that backups are encrypted at rest and in transit.\n4. Verify backup restoration has been tested within the last 12 months.\n5. Confirm backup monitoring — failed backups are detected and remediated.',
             'Backup policy and configuration; Backup retention settings; Encryption configuration; Restoration test results; Backup monitoring/alerting configuration',
             'Inspection'),
        ]),
        ('B6 — Interoperability and Portability', [
            ('CLD-15', 'Portability', 'Cloud portability arrangements',
             '1. Review the FI\'s approach to avoiding vendor lock-in (use of open standards, abstraction layers, multi-cloud strategy).\n2. Verify that data can be exported from the CSP in standard, usable formats.\n3. Check that critical applications can be migrated to an alternative CSP or on-premises within acceptable timeframes.\n4. Verify data export and migration procedures have been tested.',
             'Portability/interoperability strategy; Data export format documentation; Migration feasibility assessment; Data export/migration test results',
             'Inspection'),
        ]),
        ('B7 — Exit Strategy', [
            ('CLD-16', 'Exit Strategy', 'Cloud exit planning',
             '1. Obtain the cloud exit strategy for each critical CSP engagement.\n2. Verify it covers: trigger events, data retrieval process, migration approach, timeline, resource requirements, and communication plan.\n3. Check that the exit strategy has been reviewed within the last 12 months.\n4. Verify contractual terms support the exit strategy.',
             'Cloud exit strategy document; Contractual exit provisions; Review/approval records',
             'Inspection'),
        ]),
        ('B8 — Cryptographic Key Management', [
            ('CLD-17', 'Key Management', 'Cloud encryption and key management',
             '1. Review the FI\'s cloud encryption and key management strategy.\n2. Identify whether FI uses CSP-managed keys, customer-managed keys (CMK), or bring-your-own-key (BYOK).\n3. For customer-managed keys, verify key rotation schedule and access controls.\n4. Verify encryption at rest is enabled for all data stores.\n5. Verify encryption in transit (TLS 1.2+) for all cloud service endpoints.',
             'Encryption and key management policy; Key management configuration; Encryption-at-rest configuration per data store; TLS configuration evidence',
             'Inspection'),
        ]),
        ('B9 — Access Controls', [
            ('CLD-18', 'Cloud IAM', 'Identity and access management',
             '1. Review cloud IAM architecture (identity federation, SSO, MFA).\n2. Verify MFA is enforced for all cloud console and API access.\n3. Check that the principle of least privilege is applied — review IAM policies for overly permissive roles.\n4. Verify privileged/admin access is limited, separately managed, and monitored.\n5. Verify service accounts and API keys are managed with rotation and least privilege.\n6. Check for unused/stale IAM accounts and access keys.',
             'IAM architecture documentation; MFA enforcement configuration; IAM policy review results; Privileged access inventory; Service account/API key inventory; Stale account report',
             'Inspection'),
        ]),
        ('B10 — Cybersecurity Operations', [
            ('CLD-19', 'Security Monitoring', 'Cloud security monitoring and threat detection',
             '1. Verify cloud-native security monitoring is enabled (AWS CloudTrail/GuardDuty, Azure Defender/Sentinel, GCP Security Command Center).\n2. Check that monitoring covers: API activity, network flows, identity events, and data access patterns.\n3. Verify alerts are routed to the SOC and triaged within defined SLAs.\n4. Check that cloud security posture management (CSPM) tools are deployed.\n5. Review CSPM findings and remediation status.',
             'Cloud security monitoring configuration; SOC integration evidence; CSPM tool deployment and configuration; CSPM findings and remediation tracker',
             'Inspection'),
        ]),
        ('B11 — DDoS Protection', [
            ('CLD-20', 'DDoS Protection', 'DDoS protection for cloud services',
             '1. Verify DDoS protection is enabled for internet-facing cloud services.\n2. Check that DDoS protection covers both network-layer (L3/L4) and application-layer (L7) attacks.\n3. Verify DDoS response playbooks exist and are tested.\n4. Confirm alerting is configured for DDoS events.',
             'DDoS protection configuration; DDoS response playbook; DDoS test/drill results; Alert configuration',
             'Inspection'),
        ]),
        ('B12 — Data Loss Prevention', [
            ('CLD-21', 'DLP', 'Cloud data loss prevention',
             '1. Review the FI\'s cloud DLP strategy and tooling.\n2. Verify DLP policies cover: data exfiltration detection, sensitive data exposure in storage, and data sharing controls.\n3. Check that DLP alerts are triaged and investigated.\n4. Verify that public access to cloud storage is explicitly blocked unless specifically approved.',
             'Cloud DLP strategy; DLP policy configuration; DLP alert investigation records; Cloud storage public access settings',
             'Inspection'),
        ]),
        ('B13 — SOC Coverage', [
            ('CLD-22', 'SOC', 'SOC coverage for cloud',
             '1. Verify that cloud security events are ingested into the SOC\'s SIEM.\n2. Check that cloud-specific detection rules and use cases are defined.\n3. Verify SOC analysts have the skills and access to investigate cloud security events.\n4. Review 5 recent cloud security incidents and assess SOC response quality.',
             'SIEM log source configuration; Cloud detection rules/use cases; SOC analyst skill assessment; 5 sampled cloud incident records',
             'Inspection / Inquiry'),
        ]),
        ('B14 — Cyber Response and Recovery', [
            ('CLD-23', 'Cyber Response', 'Cloud incident response and recovery',
             '1. Review the FI\'s incident response plan for cloud-specific scenarios.\n2. Verify that response procedures account for the shared responsibility model.\n3. Check that CSP incident notification and escalation contacts are documented.\n4. Verify that cloud DR/failover has been tested.\n5. Review results of the most recent cloud DR test.',
             'Cloud incident response procedures; CSP escalation contacts; Cloud DR/failover test plan; Cloud DR test results',
             'Inspection'),
        ]),
        ('Supplementary — Compliance and Data Residency', [
            ('CLD-24', 'Data Residency', 'Data residency compliance',
             '1. Identify regulatory data residency requirements applicable to the FI.\n2. Map each cloud service and data store to its hosting region(s).\n3. Verify that restricted data resides only in approved regions.\n4. Check that CSP configurations prevent data replication to non-approved regions.\n5. Verify that BNM approval was obtained for any data hosted outside Malaysia (if required).',
             'Data residency requirements register; Cloud resource region mapping; CSP region configuration; BNM approval records (if applicable)',
             'Inspection'),
            ('CLD-25', 'Security Baseline', 'Cloud security baseline and hardening',
             '1. Obtain the FI\'s cloud security baseline/hardening standard.\n2. Verify alignment with CIS Cloud Benchmarks or equivalent.\n3. Run or review results of automated compliance checks against the baseline.\n4. Check remediation status of non-compliant findings.',
             'Cloud security baseline document; CIS Benchmark alignment mapping; Automated compliance scan results; Remediation tracker',
             'Inspection'),
        ]),
    ]

    for section_title, tests in part_b_sections:
        write_section_row(ws, r, section_title)
        r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1

    # Sheet 4: Part D
    add_part_d_sheet(wb)

    wb.save('audit-work-programs/IESP-Cloud-WorkProgram.xlsx')
    print('Created IESP-Cloud-WorkProgram.xlsx')


# ============================================================
# WORKBOOK 2: EMERGING TECH IESP
# ============================================================
def create_emerging_tech_workbook():
    wb = openpyxl.Workbook()
    create_methodology_sheet(
        wb,
        engagement_name='BNM RMiT IESP — Emerging Technology Assessment',
        regulatory_basis='Paragraph 17.1 / Appendix 7, mapped to Appendix 9',
        scope_desc='This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Appendix 7 and Appendix 9. The objective is to assess emerging technology controls for the purpose of forming the IESP negative attestation under Appendix 7 Part C.',
        assessment_covers='Assessment covers: (1) Appendix 9 — Emerging Technology Assessment (5 domains: governance, risk assessment, acceptance criteria, controls, production prerequisites), (2) Appendix 7 Part D — Minimum Controls (universal baseline).',
        engagement_type_label='Emerging Technology IESP Assessment (Pre-Implementation or Independent Attestation)'
    )

    ws = wb.create_sheet(title='Appendix 9 - Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    app9_sections = [
        ('Domain 1 — Governance Arrangements', [
            ('AI-01', 'Governance', 'Governance framework',
             '1. Obtain the FI\'s AI/emerging tech governance framework or policy.\n2. Verify it defines: accountability structure, decision rights, risk management approach, ethical principles, and oversight mechanisms.\n3. Check that a designated committee or senior management forum has oversight.\n4. Verify the framework is approved at the board or senior management level.',
             'AI governance framework/policy; Committee terms of reference; Board/senior management approval records',
             'Inspection'),
            ('AI-02', 'Governance', 'Roles and responsibilities',
             '1. Review organisational structure for AI/emerging tech management.\n2. Verify defined roles: model owner, model developer, model validator, risk manager, compliance officer.\n3. Check that each deployed model/technology has an assigned owner accountable for its performance and risk.\n4. Verify the FI has or has access to sufficient expertise in AI/ML.',
             'Organisational chart (AI function); Role descriptions; Model/technology ownership register; Skills inventory or expertise assessment',
             'Inspection / Inquiry'),
        ]),
        ('Domain 2 — Risk Assessment and Tolerance', [
            ('AI-03', 'Risk Assessment', 'Technology-specific risk assessment',
             '1. Obtain the risk assessment methodology for AI/emerging tech.\n2. For each in-scope deployment, verify that a risk assessment was performed covering: model risk, data risk, bias/fairness risk, explainability risk, operational risk, and regulatory risk.\n3. Verify risk assessments are proportionate to the risk tier of the deployment.\n4. Check that residual risks are within the FI\'s approved risk tolerance.',
             'Risk assessment methodology; Completed risk assessments per deployment; Risk tolerance thresholds; Residual risk acceptance records',
             'Inspection'),
            ('AI-04', 'Risk Assessment', 'Bias and fairness assessment',
             '1. Identify AI models that make or support decisions affecting customers.\n2. For each such model, verify that bias and fairness testing has been performed.\n3. Check that protected attributes (race, gender, age, etc.) are assessed for disparate impact.\n4. Verify ongoing monitoring for bias drift over time.',
             'Bias and fairness testing methodology; Bias test results per model; Disparate impact analysis; Ongoing monitoring configuration',
             'Inspection'),
        ]),
        ('Domain 3 — Acceptance Criteria', [
            ('AI-05', 'Acceptance Criteria', 'Production deployment acceptance',
             '1. Obtain the FI\'s acceptance criteria framework for AI/emerging tech.\n2. Verify criteria cover: model performance thresholds, validation results, security assessment, ethical review, operational readiness, and business sign-off.\n3. For each in-scope deployment, verify that acceptance criteria were met before production deployment.\n4. Check that acceptance was formally documented and signed off.',
             'Acceptance criteria framework; Completed acceptance checklists per deployment; Sign-off records',
             'Inspection'),
        ]),
        ('Domain 4 — Technology and Cybersecurity Controls', [
            ('AI-06', 'Security Controls', 'AI model and training data security',
             '1. Review access controls for AI model repositories, training data stores, and inference endpoints.\n2. Verify training data is classified, access-controlled, and protected (encryption at rest and in transit).\n3. Check that model artefacts are version-controlled and integrity-protected.\n4. Verify that AI development environments are segmented from production.\n5. Assess protections against adversarial attacks on AI models.',
             'Access control configurations; Data classification and encryption evidence; Model version control system; Environment segmentation evidence; Adversarial attack mitigation measures',
             'Inspection'),
            ('AI-07', 'Data Governance', 'Data quality and governance for AI',
             '1. Review the data governance framework for AI/ML training and inference data.\n2. Verify data quality controls: completeness, accuracy, timeliness, consistency.\n3. Check that data lineage is tracked from source to model input.\n4. Verify that data privacy requirements are met (anonymisation, consent, purpose limitation).\n5. Check that training data is representative and sufficient.',
             'Data governance framework; Data quality control procedures and metrics; Data lineage documentation; Privacy compliance evidence; Training data representativeness assessment',
             'Inspection'),
        ]),
        ('Domain 5 — Production Environment Prerequisites', [
            ('AI-08', 'Model Monitoring', 'Production model performance monitoring',
             '1. Identify all AI models in production.\n2. Verify that each model has defined performance metrics (accuracy, precision, recall, F1, AUC, or business-specific KPIs).\n3. Check that performance is monitored continuously or at defined intervals.\n4. Verify that performance degradation triggers alerts and investigation.\n5. Confirm model retraining/recalibration procedures exist.',
             'Production model inventory; Performance metric definitions per model; Monitoring dashboard/tool configuration; Alert configuration and sample alert records; Retraining/recalibration procedures',
             'Inspection'),
            ('AI-09', 'Model Validation', 'Independent model validation',
             '1. Check that model validation is performed by a party independent of model development.\n2. Review the validation methodology — does it cover: conceptual soundness, data adequacy, performance benchmarking, sensitivity analysis, and stress testing?\n3. Verify validation is performed before initial deployment and periodically thereafter.\n4. Check that validation findings are tracked and remediated.',
             'Model validation policy; Independence of validation function; Validation reports; Validation finding tracker',
             'Inspection'),
            ('AI-10', 'Testing', 'Pre-production testing',
             '1. Review the testing strategy for AI/emerging tech deployments.\n2. Verify testing includes: unit testing, integration testing, performance/load testing, security testing, user acceptance testing, and A/B or shadow testing where applicable.\n3. For each in-scope deployment, verify test execution records and results.\n4. Confirm that test exit criteria were met before production release.',
             'Testing strategy document; Test plans and execution records; Test results and exit criteria assessment; Production release approval',
             'Inspection'),
            ('AI-11', 'Regulatory Compliance', 'Standards and regulations compliance',
             '1. Identify applicable standards and regulations for the FI\'s AI deployments (BNM guidelines, PDPA, sector-specific requirements).\n2. Verify that each deployment has been assessed for regulatory compliance.\n3. Check that required regulatory notifications or approvals have been obtained.\n4. Verify ongoing compliance monitoring is in place.',
             'Regulatory requirements register; Compliance assessment per deployment; Regulatory notification/approval records; Compliance monitoring procedures',
             'Inspection'),
            ('AI-12', 'Kill Switch', 'Suspension and decommissioning capability',
             '1. Check that each production AI system has a documented suspension/kill-switch capability.\n2. Verify that the suspension mechanism can be activated quickly (within defined timeframes).\n3. Test or review evidence of suspension testing.\n4. Verify that fallback/manual processes exist if the AI system is suspended.\n5. Confirm that the decision authority for suspension is clearly defined.',
             'Suspension/kill-switch documentation; Suspension test results; Fallback process documentation; Decision authority matrix',
             'Inspection'),
            ('AI-13', 'Human Oversight', 'Ongoing monitoring and human oversight',
             '1. Verify that AI systems have defined levels of human oversight proportionate to risk.\n2. Check that automated decisions can be overridden by authorised personnel.\n3. Verify that monitoring includes outcome tracking to detect unintended consequences.\n4. Confirm that escalation procedures exist for anomalous AI behaviour.',
             'Human oversight framework; Override capability evidence; Outcome monitoring dashboard/reports; Escalation procedures',
             'Inspection'),
            ('AI-14', 'Transparency', 'Transparency and disclosure',
             '1. Identify AI systems that interact with or make decisions about customers.\n2. Verify that customers are informed when AI is used in decision-making.\n3. Check that explanations can be provided for AI-driven decisions (explainability).\n4. Verify that a complaints/appeals process exists for AI-driven decisions.\n5. Review sample disclosures for adequacy.',
             'Disclosure policy; Customer notification evidence; Explainability mechanism documentation; Complaints/appeals process; Sample disclosures',
             'Inspection'),
            ('AI-15', 'AI Incident Management', 'AI-specific incident management',
             '1. Review the incident management procedure for AI-specific incidents (model failure, biased outcomes, data poisoning, adversarial attacks).\n2. Verify that AI-specific incident categories and severity levels are defined.\n3. Check incident log for AI-related incidents in the past 12 months.\n4. Verify lessons learned are fed back into model improvement and governance.',
             'AI incident management procedure; AI incident categories and severity matrix; AI incident log and response records; Lessons learned register',
             'Inspection'),
        ]),
    ]

    for section_title, tests in app9_sections:
        write_section_row(ws, r, section_title)
        r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1

    add_part_d_sheet(wb)
    wb.save('audit-work-programs/IESP-EmergingTech-WorkProgram.xlsx')
    print('Created IESP-EmergingTech-WorkProgram.xlsx')


# ============================================================
# WORKBOOK 3: DIGITAL SERVICES
# ============================================================
def create_digital_services_workbook():
    wb = openpyxl.Workbook()
    create_methodology_sheet(
        wb,
        engagement_name='BNM RMiT IESP — Digital Services Enhancement Assessment',
        regulatory_basis='Paragraphs 16.4, 16.5 / Appendix 7 Part D',
        scope_desc='This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Paragraphs 16.4 and 16.5. The objective is to assess the security of new or materially enhanced digital services prior to launch.',
        assessment_covers='Assessment covers: (1) Digital Services Security Assessment — access control, transaction security, mobile security, data integrity, application security, (2) Appendix 7 Part D — Minimum Controls (universal baseline).',
        engagement_type_label='Digital Services Enhancement IESP Assessment (Pre-Launch)'
    )

    ws = wb.create_sheet(title='Digital Services Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    ds_sections = [
        ('Domain 1 — Access Control (Part D 1a + 2a-c)', [
            ('DS-01', 'Access Control', 'Customer authentication mechanisms',
             '1. Review the authentication mechanisms for the digital service (password, OTP, biometric, device binding).\n2. Verify multi-factor authentication (MFA) is enforced for login and high-risk transactions.\n3. Check password/credential policy: minimum complexity, history, expiry, lockout thresholds.\n4. Verify authentication tokens/sessions are securely managed.',
             'Authentication design document; MFA configuration; Password/credential policy; Session management configuration',
             'Inspection'),
            ('DS-02', 'Access Control', 'Digital identity verification (eKYC)',
             '1. Review the digital identity verification process (eKYC).\n2. Verify identity document validation mechanisms (OCR, NFC chip reading, database verification).\n3. Check liveness detection for biometric verification.\n4. Verify that identity verification results are logged and auditable.\n5. Assess fraud detection controls during onboarding.',
             'eKYC process flow; Identity verification tool configuration; Liveness detection configuration; Audit log samples; Fraud detection rules',
             'Inspection'),
            ('DS-03', 'Access Control', 'Authorisation and RBAC',
             '1. Review the authorisation model for the digital service (RBAC, ABAC).\n2. Verify that access to functions and data is based on the user\'s role and entitlements.\n3. Check that privilege escalation is prevented.\n4. Verify API authorisation — are API endpoints protected?\n5. Test for insecure direct object references (IDOR).',
             'Authorisation model design; Role-to-function mapping; API authorisation configuration; Penetration test results (IDOR testing)',
             'Inspection'),
            ('DS-04', 'Access Control', 'Session management security',
             '1. Review session management implementation.\n2. Verify session tokens are cryptographically random and of sufficient length.\n3. Check that sessions expire after idle and absolute periods.\n4. Verify session is invalidated on logout, password change, and MFA re-challenge.\n5. Check concurrent session controls.',
             'Session management configuration; Token generation mechanism; Session timeout settings; Concurrent session policy',
             'Inspection'),
            ('DS-05', 'Access Control', 'Account lockout and brute-force protection',
             '1. Review account lockout policy (threshold, duration, reset mechanism).\n2. Verify rate limiting is implemented for authentication endpoints.\n3. Check CAPTCHA or equivalent bot protection.\n4. Verify that lockout notifications are sent to the customer.\n5. Test that lockout cannot be bypassed.',
             'Lockout policy configuration; Rate limiting configuration; CAPTCHA/bot protection; Notification configuration; Bypass testing results',
             'Inspection'),
        ]),
        ('Domain 2 — Online Transaction Security (Part D 2)', [
            ('DS-06', 'Transaction Security', 'Transaction authentication and authorisation',
             '1. Review the transaction authentication mechanism (transaction signing, OTP, biometric confirmation, TAC).\n2. Verify that high-risk transactions require step-up authentication.\n3. Check that transaction details are presented for confirmation before execution.\n4. Verify that the authentication is bound to the specific transaction.\n5. Assess protection against MITM and MITB attacks.',
             'Transaction authentication design; Step-up authentication configuration; Transaction confirmation flow; Transaction binding mechanism; MitM/MitB protection measures',
             'Inspection'),
            ('DS-07', 'Transaction Security', 'Transaction limits and fraud monitoring',
             '1. Obtain default and configurable transaction limits.\n2. Verify that limits are enforced at the application and backend levels.\n3. Review fraud monitoring rules (anomaly detection, velocity checks, geolocation, device fingerprinting).\n4. Check that suspicious transactions trigger alerts and/or blocks.\n5. Verify that customers can manage their own limits.',
             'Transaction limit configuration; Fraud monitoring rules; Sample fraud alert records; Customer limit management interface',
             'Inspection'),
            ('DS-08', 'Transaction Security', 'End-to-end encryption',
             '1. Verify TLS 1.2 or higher is enforced for all communications.\n2. Check certificate configuration (valid, trusted CA, correct hostname, HSTS enabled).\n3. Verify that sensitive data in transit is not exposed in URLs, logs, or error messages.\n4. Check for certificate pinning in mobile applications.\n5. Verify API endpoint encryption and mutual TLS for B2B integrations.',
             'TLS configuration (SSL Labs test or equivalent); Certificate details; HSTS configuration; Log review for sensitive data exposure; Certificate pinning configuration; mTLS configuration',
             'Inspection'),
            ('DS-09', 'Transaction Security', 'Secure API design',
             '1. Obtain API documentation and review against OWASP API Security Top 10.\n2. Verify API authentication (OAuth 2.0, API keys, mTLS as appropriate).\n3. Check rate limiting and throttling on API endpoints.\n4. Verify input validation and output encoding.\n5. Check API versioning and deprecation management.\n6. Review API gateway configuration.',
             'API documentation; OWASP API Security assessment results; API authentication configuration; Rate limiting configuration; API gateway configuration',
             'Inspection'),
            ('DS-10', 'Transaction Security', 'Non-repudiation for critical transactions',
             '1. Identify critical transaction types requiring non-repudiation.\n2. Verify that transaction records capture: who, what, when, from where, and how authenticated.\n3. Check that transaction records are tamper-proof.\n4. Verify audit trail retention meets regulatory requirements.',
             'Non-repudiation design; Transaction record format and content; Tamper-proofing mechanism; Audit trail retention configuration',
             'Inspection'),
        ]),
        ('Domain 3 — Mobile Device Security (Part D 2e)', [
            ('DS-11', 'Mobile Security', 'Mobile application security controls',
             '1. Review the mobile application security architecture.\n2. Verify that the app detects rooted/jailbroken devices and responds appropriately.\n3. Check that sensitive data is not stored in plaintext on the device.\n4. Verify code obfuscation and anti-tampering mechanisms.\n5. Verify that the app does not expose sensitive data in logs, screenshots, or clipboard.',
             'Mobile security architecture; Root/jailbreak detection configuration; Local data storage review; Obfuscation/anti-tampering evidence; Data leakage assessment',
             'Inspection'),
            ('DS-12', 'Mobile Security', 'App distribution and update management',
             '1. Verify the app is distributed only through official app stores.\n2. Check that the app enforces minimum version requirements.\n3. Verify app signing and integrity verification.\n4. Check that push notification content does not include sensitive information.\n5. Review MDM/MAM requirements for corporate users.',
             'App store distribution evidence; Minimum version enforcement; App signing configuration; Push notification content policy; MDM/MAM policy (if applicable)',
             'Inspection'),
            ('DS-13', 'Mobile Security', 'Mobile-specific threat protections',
             '1. Check for runtime application self-protection (RASP).\n2. Verify that the app detects debugging attempts, emulator execution, and hooking frameworks.\n3. Check that secure communication channels cannot be intercepted without detection.\n4. Verify device binding/registration mechanisms.',
             'RASP configuration; Anti-debugging/emulator detection; Proxy/MitM detection; Device binding mechanism',
             'Inspection'),
        ]),
        ('Domain 4 — Data Integrity (Part D 2d)', [
            ('DS-14', 'Data Integrity', 'Input validation and data integrity',
             '1. Review input validation implementation (server-side validation is mandatory).\n2. Verify validation covers: data type, length, range, format, and allowed characters.\n3. Test for common injection attacks: SQL injection, XSS, command injection, LDAP injection.\n4. Verify output encoding is applied to prevent XSS.\n5. Check file upload functionality validates file type, size, and content.',
             'Input validation design; Server-side validation configuration; Penetration test results (injection testing); Output encoding implementation; File upload validation configuration',
             'Inspection'),
            ('DS-15', 'Data Integrity', 'Data integrity during processing and storage',
             '1. Review data integrity controls in the transaction processing chain.\n2. Verify checksums or hash verification for data in transit between components.\n3. Check database integrity controls (constraints, referential integrity, transaction logging).\n4. Verify reconciliation processes between the digital channel and core systems.\n5. Confirm that data integrity violations trigger alerts.',
             'Data integrity control design; Checksum/hash implementation; Database integrity configuration; Reconciliation procedures and reports; Alert configuration',
             'Inspection'),
            ('DS-16', 'Data Integrity', 'Data manipulation and replay attack protection',
             '1. Verify anti-replay mechanisms (nonce, timestamp, sequence number) for critical transactions.\n2. Check that transaction requests cannot be intercepted and modified.\n3. Verify duplicate transaction detection.\n4. Test for parameter tampering vulnerabilities.',
             'Anti-replay mechanism design; Transit integrity protection; Duplicate detection configuration; Parameter tampering test results',
             'Inspection'),
        ]),
        ('Supplementary — Application Security Testing', [
            ('DS-17', 'App Security Testing', 'Comprehensive security testing pre-launch',
             '1. Obtain the security testing scope and plan.\n2. Verify that the following tests were performed: SAST, DAST, penetration testing (web and mobile), API security testing, and infrastructure VA.\n3. Review test results and finding severity distribution.\n4. Verify that all high and critical findings are remediated before launch.\n5. Confirm testing was performed by qualified testers.',
             'Security testing plan; SAST report; DAST report; Penetration test report; API security test report; VA report; Remediation evidence; Tester qualifications',
             'Inspection'),
            ('DS-18', 'App Security Testing', 'Secure SDLC practices',
             '1. Review the FI\'s SSDLC for the digital service.\n2. Verify that security requirements are defined at the design phase.\n3. Check that threat modelling was performed.\n4. Verify secure coding standards are applied and enforced.\n5. Confirm that security sign-off is required before production release.',
             'SSDLC documentation; Security requirements specification; Threat model; Secure coding standards; Code review/scanning records; Security sign-off records',
             'Inspection'),
            ('DS-19', 'Privacy', 'Privacy and data protection controls',
             '1. Review privacy impact assessment (PIA) for the digital service.\n2. Verify that personal data collection is limited (data minimisation).\n3. Check that consent mechanisms are implemented where required.\n4. Verify data retention and deletion policies are enforced.\n5. Confirm privacy notices are clear and accessible.',
             'Privacy impact assessment; Data collection inventory; Consent mechanism implementation; Data retention/deletion configuration; Privacy notice review',
             'Inspection'),
            ('DS-20', 'Availability', 'Business continuity and availability',
             '1. Review the availability targets for the digital service.\n2. Verify that the service architecture supports high availability.\n3. Check monitoring and alerting for service availability.\n4. Verify that a disaster recovery plan covers the digital service.\n5. Review results of the most recent DR test.',
             'Availability targets; HA architecture design; Monitoring and alerting configuration; DR plan (digital service section); DR test results',
             'Inspection'),
        ]),
    ]

    for section_title, tests in ds_sections:
        write_section_row(ws, r, section_title)
        r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1

    add_part_d_sheet(wb)
    wb.save('audit-work-programs/IESP-DigitalServices-WorkProgram.xlsx')
    print('Created IESP-DigitalServices-WorkProgram.xlsx')


# ============================================================
# WORKBOOK 4: DCRA
# ============================================================
def create_dcra_workbook():
    wb = openpyxl.Workbook()
    create_methodology_sheet(
        wb,
        engagement_name='BNM RMiT IESP — Data Centre Resilience Assessment (DCRA)',
        regulatory_basis='Paragraph 14.1, mapped to paragraphs 10.24 to 10.28',
        scope_desc='This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Paragraph 14.1. The objective is to assess data centre resilience controls for the purpose of forming the IESP negative attestation under Appendix 7 Part C.',
        assessment_covers='Assessment covers: (1) DCRA Assessment — DC resilience objectives, redundancy, physical security, operations, segregation (clauses 10.24-10.28), (2) Appendix 7 Part D — Minimum Controls (universal baseline).',
        engagement_type_label='Data Centre Resilience Assessment (DCRA)'
    )

    ws = wb.create_sheet(title='DCRA Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    dcra_sections = [
        ('Domain 1 — DC Resilience and Availability Objectives (10.24)', [
            ('DCRA-01', 'Resilience Objectives', 'Resilience objectives alignment',
             '1. Obtain DC resilience and availability strategy document.\n2. Extract stated resilience targets (availability %, RTO, RPO).\n3. Compare against the FI\'s approved business recovery objectives for each critical system hosted.\n4. Check that resilience targets have been approved by the appropriate committee.',
             'DC resilience strategy document; Business recovery objectives matrix; Committee approval minutes',
             'Inspection'),
            ('DCRA-02', 'Resilience Objectives', 'Periodic review and update',
             '1. Check version history of the resilience strategy.\n2. Confirm review frequency (at least annual or upon material change).\n3. Verify that changes in business requirements triggered corresponding updates.',
             'Document version history; Change log entries; Review sign-off records',
             'Inspection'),
        ]),
        ('Domain 2 — Redundancy and Single Points of Failure (10.25)', [
            ('DCRA-03', 'Redundancy', 'Redundant capacity for critical infrastructure',
             '1. Obtain the DC redundancy design document (N+1, 2N, or 2N+1 configurations).\n2. For each critical infrastructure layer (power, cooling, network), confirm the documented redundancy level.\n3. Verify actual installed capacity against design documents through site inspection.\n4. Check that redundant capacity can handle full load upon failover.',
             'Redundancy design specifications; Capacity planning reports; Site inspection photographs',
             'Inspection / Observation'),
            ('DCRA-04', 'Redundancy', 'Multiple distribution paths',
             '1. Review electrical single-line diagrams for dual utility feeds or on-site generation.\n2. Review network connectivity diagrams for diverse carrier paths.\n3. Confirm physical path diversity (separate risers, conduits, or entry points).\n4. Verify through site walk that paths are genuinely separate.',
             'Electrical single-line diagrams; Network path diversity documentation; Site walk observations',
             'Inspection / Observation'),
            ('DCRA-05', 'Redundancy', 'Single point of failure (SPOF) analysis',
             '1. Obtain the FI\'s SPOF analysis or risk register for each DC.\n2. Walk through each identified SPOF and confirm mitigation measures.\n3. Identify any unrecognised SPOFs through independent assessment during site walk.\n4. Check that SPOF analysis is periodically refreshed.',
             'SPOF analysis/register; Mitigation action plans; Site walk findings',
             'Inspection / Observation'),
            ('DCRA-06', 'Redundancy', 'Failover testing',
             '1. Obtain failover test plans and most recent test results for each redundant component (UPS, generators, cooling, network switches).\n2. Review test frequency — should be at least annual.\n3. Confirm that tests simulate actual failure conditions, not just planned switchovers.\n4. Check that test failures resulted in corrective actions.',
             'Failover test plans; Test result reports; Corrective action records',
             'Inspection'),
        ]),
        ('Domain 3 — Physical Security and Environmental Controls (10.26)', [
            ('DCRA-07', 'Physical Security', 'Dedicated purpose-built space',
             '1. Confirm DC is in a dedicated space not shared with non-IT functions.\n2. Verify physical separation from public areas, loading docks, and other tenants.\n3. Check that walls extend from true floor to true ceiling.',
             'Site inspection observations; Building layout plans; Lease/facility agreements for co-lo',
             'Observation'),
            ('DCRA-08', 'Physical Security', 'Multi-layered physical access controls',
             '1. Walk the physical access path from building perimeter to server rack.\n2. Verify each access layer has independent controls.\n3. Test access control mechanisms (badge, biometric, PIN) at each layer.\n4. Review access provisioning and de-provisioning procedures.\n5. Sample-check the access list against HR records for terminated staff.',
             'Physical security policy; Access control system configuration; Access list vs. HR reconciliation; Site walk observations',
             'Inspection / Observation'),
            ('DCRA-09', 'Physical Security', 'Disaster-prone location assessment',
             '1. Obtain the FI\'s site risk assessment covering natural hazards.\n2. Cross-reference DC location against publicly available hazard maps.\n3. Where risks are identified, verify mitigation measures.\n4. Check that the site risk assessment is periodically updated.',
             'Site risk assessment; Hazard map cross-reference; Mitigation implementation evidence',
             'Inspection'),
            ('DCRA-10', 'Environmental Controls', 'Electrical infrastructure resilience',
             '1. Review UPS configuration (online double-conversion, N+1 or 2N).\n2. Verify UPS battery runtime under full load (minimum 15 minutes).\n3. Confirm generator start-up time and fuel autonomy (minimum 48-72 hours).\n4. Check automatic transfer switch (ATS) operation and test records.\n5. Verify fuel replenishment contracts and delivery SLAs.',
             'UPS specifications and test reports; Generator load test reports; ATS test records; Fuel supply contracts',
             'Inspection / Observation'),
            ('DCRA-11', 'Environmental Controls', 'Thermal management and cooling',
             '1. Review cooling design and redundancy level (N+1 minimum).\n2. Check current cooling load vs. installed capacity.\n3. Verify temperature and humidity monitoring at rack level.\n4. Confirm alerting thresholds and escalation procedures.\n5. Review hot/cold aisle containment strategy.',
             'Cooling system design documents; Capacity utilisation reports; Monitoring system configuration; Alert threshold settings',
             'Inspection / Observation'),
            ('DCRA-12', 'Environmental Controls', 'Environmental monitoring and fire suppression',
             '1. Confirm VESDA or equivalent early warning detection is installed.\n2. Verify fire suppression system type (gas-based for IT areas) and inspection records.\n3. Check water leak detection under raised floor and around cooling units.\n4. Verify environmental monitoring dashboard and 24/7 alert capability.\n5. Review incident response procedures for environmental events.',
             'Fire suppression inspection certificates; VESDA configuration records; Water leak detection layout; Monitoring dashboard screenshots; Environmental incident response procedures',
             'Inspection / Observation'),
            ('DCRA-13', 'Asset Management', 'Hardware asset management and lifecycle',
             '1. Obtain hardware asset register and verify it is up to date.\n2. Sample-check physical assets on the floor against the register.\n3. Verify end-of-life/end-of-support hardware is identified and has a replacement plan.\n4. Check that decommissioned equipment undergoes secure data destruction.',
             'Hardware asset register; Physical verification results; EOL/EOS tracker; Data destruction certificates',
             'Inspection / Observation'),
        ]),
        ('Domain 4 — DC Operations and Control Procedures (10.27)', [
            ('DCRA-14', 'DC Operations', 'Automated monitoring and management',
             '1. Obtain inventory of DC monitoring tools (DCIM, BMS, network monitoring).\n2. Verify coverage of critical parameters: power, cooling, capacity, network.\n3. Test that alerts are generated for threshold breaches.\n4. Confirm monitoring is integrated into the NOC/SOC for 24/7 visibility.',
             'Tool inventory and architecture; Monitoring coverage matrix; Sample alert records; NOC/SOC integration evidence',
             'Inspection'),
            ('DCRA-15', 'DC Operations', 'Batch processing controls',
             '1. Obtain batch job scheduling procedures and tool configuration.\n2. Verify that batch jobs have defined run windows, dependencies, and error handling.\n3. Review batch job failure logs for the past 3 months and confirm remediation.\n4. Check that batch schedules are reviewed and approved before changes.',
             'Batch scheduling procedures; Job scheduler configuration; Failure logs and remediation records; Change approval records',
             'Inspection'),
            ('DCRA-16', 'DC Operations', 'Change management for DC infrastructure',
             '1. Obtain the DC change management procedure.\n2. Sample 10 recent infrastructure changes (network, power, rack moves).\n3. Verify each change has: request, impact assessment, approval, implementation plan, rollback plan, and post-implementation review.\n4. Check that emergency changes follow a defined expedited process.',
             'Change management procedure; Sample of 10 change records; Emergency change records',
             'Inspection'),
            ('DCRA-17', 'DC Operations', 'Error and incident handling',
             '1. Obtain DC operations incident management procedure.\n2. Review incident log for the past 6 months.\n3. Verify root cause analysis (RCA) was performed for significant incidents.\n4. Check that RCA findings led to preventive actions.',
             'Incident management procedure; Incident log (6 months); RCA reports; Preventive action tracker',
             'Inspection'),
        ]),
        ('Domain 5 — Segregation of Incompatible Activities (10.28)', [
            ('DCRA-18', 'Segregation', 'Vendor and programmer access controls',
             '1. Review the policy for vendor/third-party access to the DC.\n2. Check that vendors require pre-approved access requests with defined scope and duration.\n3. Verify escort requirements for vendors in sensitive areas.\n4. Sample-check vendor access logs against approved requests.\n5. Confirm that vendor access is revoked promptly after engagement ends.',
             'Vendor access policy; Access request forms/system; Escort logs; Access log vs. approval reconciliation',
             'Inspection'),
            ('DCRA-19', 'Segregation', 'Production environment segregation',
             '1. Review logical and physical segregation between production and non-production environments.\n2. Verify that developers do not have direct access to production servers.\n3. Check network segmentation between production and non-production zones.\n4. Confirm that data used in non-production environments is masked/anonymised.',
             'Environment segregation architecture; Access control matrices; Network segmentation diagrams; Data masking procedures',
             'Inspection'),
            ('DCRA-20', 'Segregation', 'Segregation of duties in DC operations',
             '1. Obtain the DC operations RACI or role matrix.\n2. Verify that incompatible duties are separated.\n3. Check that privileged access to DC infrastructure is limited and monitored.\n4. Review privileged access usage logs for the past 3 months.',
             'RACI matrix; Role definitions; Privileged access list; Privileged access usage logs',
             'Inspection'),
        ]),
    ]

    for section_title, tests in dcra_sections:
        write_section_row(ws, r, section_title)
        r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1

    add_part_d_sheet(wb)
    wb.save('audit-work-programs/IESP-DCRA-WorkProgram.xlsx')
    print('Created IESP-DCRA-WorkProgram.xlsx')


# ============================================================
# WORKBOOK 5: NRA
# ============================================================
def create_nra_workbook():
    wb = openpyxl.Workbook()
    create_methodology_sheet(
        wb,
        engagement_name='BNM RMiT IESP — Network Resilience Assessment (NRA)',
        regulatory_basis='Paragraph 14.2, mapped to paragraphs 10.36 to 10.43',
        scope_desc='This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Paragraph 14.2. The objective is to assess network resilience controls for the purpose of forming the IESP negative attestation under Appendix 7 Part C.',
        assessment_covers='Assessment covers: (1) NRA Assessment — network design, resilience, monitoring, security, segmentation (clauses 10.36-10.43), (2) Appendix 7 Part D — Minimum Controls (universal baseline).',
        engagement_type_label='Network Resilience Assessment (NRA)'
    )

    ws = wb.create_sheet(title='NRA Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    nra_sections = [
        ('Domain 1 — Network Design and Scalability (10.36)', [
            ('NRA-01', 'Network Design', 'Capacity requirements',
             '1. Obtain the network capacity planning document.\n2. Review current bandwidth utilisation across critical links (WAN, internet, DC interconnects).\n3. Verify that capacity projections account for at least 2 years of growth.\n4. Check that utilisation thresholds trigger capacity augmentation (e.g., >70% sustained utilisation).',
             'Capacity planning document; Bandwidth utilisation reports (last 12 months); Growth projection model',
             'Inspection'),
            ('NRA-02', 'Network Design', 'Scalability',
             '1. Review the network architecture for modular and scalable design principles.\n2. Assess whether the architecture can accommodate new sites, services, or increased load without structural changes.\n3. Check for technology currency — are core network platforms within vendor support and capable of scaling.',
             'Network architecture design principles document; Technology lifecycle tracker; Scalability assessment',
             'Inspection'),
            ('NRA-03', 'Network Design', 'Performance SLAs',
             '1. Obtain defined network performance SLAs (latency, jitter, packet loss, availability) for critical segments.\n2. Verify SLA monitoring tools are in place.\n3. Review SLA performance against targets for the past 6 months.\n4. Check that SLA breaches trigger investigation and remediation.',
             'SLA definitions; Performance monitoring reports; SLA breach incident records',
             'Inspection'),
        ]),
        ('Domain 2 — Network Resilience and Reliability (10.37, 10.38)', [
            ('NRA-04', 'Network Resilience', 'Redundancy for critical paths',
             '1. Review network topology for redundancy at each layer (core, distribution, access).\n2. Verify redundant paths exist for critical traffic.\n3. Confirm redundant devices at each critical layer (e.g., HA pairs for firewalls).\n4. Verify that redundant paths are on diverse physical routes.',
             'Network topology diagrams with redundancy annotations; Carrier diversity documentation; HA configuration evidence',
             'Inspection'),
            ('NRA-05', 'Network Resilience', 'Failover testing',
             '1. Obtain failover test plan and schedule.\n2. Review results of the most recent failover tests for: WAN links, internet links, core switches, firewalls.\n3. Verify that failover occurs within acceptable recovery times.\n4. Check that test failures were remediated.\n5. Confirm tests simulate realistic failure conditions.',
             'Failover test plans; Test execution reports; Remediation records',
             'Inspection'),
            ('NRA-06', 'Network Resilience', 'Network disaster recovery',
             '1. Review the network component of the FI\'s DR plan.\n2. Verify that network recovery procedures are documented for each critical segment.\n3. Check that network DR has been tested as part of DR exercises.\n4. Confirm network RTO aligns with business requirements.',
             'Network DR plan; DR test results (network component); RTO alignment mapping',
             'Inspection'),
            ('NRA-07', 'Network Resilience', 'Carrier and ISP management',
             '1. Review contracts with carriers/ISPs for SLA terms.\n2. Verify that the FI uses at least two independent carriers for critical WAN/internet.\n3. Check carrier performance against SLAs for the past 12 months.\n4. Confirm escalation procedures and emergency contact arrangements.',
             'Carrier contracts with SLA terms; Carrier diversity mapping; Carrier performance reports; Escalation contact lists',
             'Inspection'),
        ]),
        ('Domain 3 — Network Monitoring and Traffic Analysis (10.39)', [
            ('NRA-08', 'Network Monitoring', 'Comprehensive network monitoring',
             '1. Obtain the network monitoring tool inventory (NMS, NPM, flow analysis).\n2. Verify that all critical network devices and links are monitored.\n3. Check monitoring coverage — are all critical parameters captured?\n4. Confirm monitoring operates 24/7 with alerting to the NOC.',
             'Monitoring tool inventory; Device coverage report; Parameter coverage matrix; NOC alerting configuration',
             'Inspection'),
            ('NRA-09', 'Network Monitoring', 'Traffic analysis and anomaly detection',
             '1. Confirm traffic flow analysis tools are deployed (NetFlow, sFlow, or equivalent).\n2. Review traffic baseline profiles and anomaly detection thresholds.\n3. Check that anomalies trigger investigation — sample 5 recent anomaly alerts.\n4. Verify integration with SIEM or SOC.',
             'Flow analysis tool configuration; Traffic baselines and anomaly thresholds; Sample anomaly investigation records; SIEM integration evidence',
             'Inspection'),
            ('NRA-10', 'Network Monitoring', 'Performance trend analysis',
             '1. Obtain regular network performance reports (monthly or quarterly).\n2. Verify reports include trend analysis for utilisation, latency, and availability.\n3. Check that trends are used to inform capacity planning decisions.\n4. Confirm reports are reviewed by appropriate management.',
             'Network performance reports; Trend analysis dashboards; Management review records',
             'Inspection'),
        ]),
        ('Domain 4 — Network Confidentiality, Integrity, Availability (10.40)', [
            ('NRA-11', 'Network Security', 'Encryption of data in transit',
             '1. Identify all network links traversing untrusted networks.\n2. Verify encryption is applied (IPSec VPN, TLS, MACsec as appropriate).\n3. Check encryption standards — minimum TLS 1.2, AES-256 or equivalent.\n4. Verify certificate management for VPN/TLS endpoints.',
             'Encryption standards policy; VPN/TLS configuration evidence; Certificate inventory and expiry tracking',
             'Inspection'),
            ('NRA-12', 'Network Security', 'Network access controls and authentication',
             '1. Review network access control mechanisms (802.1X, NAC, MAC authentication).\n2. Verify that network device management access uses strong authentication (RADIUS/TACACS+ with MFA).\n3. Check that default credentials have been changed on all network devices.\n4. Verify that unused ports are administratively disabled.\n5. Sample-check 10 network device configurations.',
             'NAC/802.1X configuration; RADIUS/TACACS+ configuration; Sample device configuration reviews; Port status reports',
             'Inspection'),
            ('NRA-13', 'Network Security', 'Configuration integrity controls',
             '1. Verify that network device configurations are backed up regularly (at least daily).\n2. Check that configuration changes are detected and alerted.\n3. Confirm that a golden/baseline configuration exists for each device type.\n4. Verify configuration backup is stored securely.',
             'Configuration backup schedule and logs; Configuration drift monitoring tool; Baseline configuration library; Backup storage arrangements',
             'Inspection'),
        ]),
        ('Domain 5 — Network Design Blueprint (10.41)', [
            ('NRA-14', 'Network Blueprint', 'Current and comprehensive blueprint',
             '1. Obtain the network design blueprint/architecture document.\n2. Verify it covers: logical topology, physical topology, IP addressing scheme, VLAN design, routing design, security zones, and connectivity to external parties.\n3. Check that the blueprint reflects the current state.\n4. Verify the blueprint is version-controlled.',
             'Network design blueprint; Version history; Change control records',
             'Inspection'),
            ('NRA-15', 'Network Blueprint', 'Review and approval',
             '1. Check that the blueprint has been reviewed and approved by appropriate authority.\n2. Verify the blueprint is reviewed at least annually or upon material change.\n3. Confirm the blueprint is accessible to relevant operational and security teams.',
             'Approval records; Review schedule/history; Access/distribution records',
             'Inspection'),
        ]),
        ('Domain 6 — Network Device Logging (10.42)', [
            ('NRA-16', 'Network Logging', 'Comprehensive device logging',
             '1. Review logging configuration on a sample of 10 network devices.\n2. Verify that security-relevant events are logged: authentication attempts, configuration changes, ACL matches, administrative actions.\n3. Confirm logs are sent to a centralised log management system.\n4. Verify time synchronisation (NTP) across all devices.',
             'Sample device logging configurations; Centralised log system evidence; NTP configuration evidence',
             'Inspection'),
            ('NRA-17', 'Network Logging', 'Log retention and review',
             '1. Check log retention periods against regulatory and policy requirements.\n2. Verify that logs are protected from tampering.\n3. Confirm that network logs are regularly reviewed through SIEM or manual review.\n4. Sample 5 recent security events and trace through log analysis to response.',
             'Log retention policy and configuration; Log protection mechanisms; SIEM correlation rules for network events; Sample event investigation records',
             'Inspection'),
        ]),
        ('Domain 7 — Network Segmentation (10.43)', [
            ('NRA-18', 'Network Segmentation', 'Segmentation strategy and implementation',
             '1. Obtain the network segmentation policy and design.\n2. Verify that segmentation separates: production from non-production, internal from DMZ, PCI zones (if applicable), and guest/IoT networks.\n3. Review firewall/ACL rules enforcing segmentation.\n4. Conduct sample traffic flow tests to confirm segmentation.',
             'Segmentation policy and design; Firewall/ACL rule sets; Traffic flow test results',
             'Inspection'),
            ('NRA-19', 'Network Segmentation', 'Micro-segmentation for critical assets',
             '1. Identify the FI\'s most critical network segments.\n2. Verify that additional segmentation controls exist for these segments.\n3. Check for application-layer or workload-level segmentation.\n4. Verify access to critical segments requires explicit authorisation.',
             'Critical segment identification; Additional segmentation controls; Access authorisation records',
             'Inspection'),
            ('NRA-20', 'Network Segmentation', 'Wireless network security',
             '1. Identify all wireless networks (corporate, guest, IoT/OT).\n2. Verify wireless networks are segmented from the wired corporate network.\n3. Check wireless authentication (WPA3-Enterprise or WPA2-Enterprise minimum).\n4. Verify rogue AP detection is deployed and active.\n5. Review wireless security assessment results.',
             'Wireless network inventory; Wireless segmentation design; Wireless authentication configuration; Rogue AP detection system; Wireless security assessment reports',
             'Inspection'),
        ]),
    ]

    for section_title, tests in nra_sections:
        write_section_row(ws, r, section_title)
        r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1

    add_part_d_sheet(wb)
    wb.save('audit-work-programs/IESP-NRA-WorkProgram.xlsx')
    print('Created IESP-NRA-WorkProgram.xlsx')


# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    create_cloud_workbook()
    create_emerging_tech_workbook()
    create_digital_services_workbook()
    create_dcra_workbook()
    create_nra_workbook()
    print('\nAll 5 IESP AWP workbooks generated.')
