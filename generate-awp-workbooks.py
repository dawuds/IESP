#!/usr/bin/env python3
"""Generate IESP AWP Excel workbooks in 13-column working paper format.

Changes from v1:
- 13 columns (added Level column: ORG/PLATFORM/WORKLOAD)
- Scoping sheet in all workbooks
- Planning & Reporting lifecycle sheets
- Part C self-assessment checklist
- Cloud AWP: filled gaps (strategy, compute, storage, vuln mgmt, etc.)
- Emerging Tech AWP: filled gaps (tech radar, concentration, ethics)

Changes from v2:
- Sampling methodology section in Methodology sheet
- Context rows under each section header (why, what good looks like, key risk)
- Cloud + Emerging Tech cross-reference overlap notes
"""

import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

# ── Styles ──────────────────────────────────────────────────────────
HEADER_FONT = Font(name='Calibri', bold=True, size=11, color='FFFFFF')
HEADER_FILL = PatternFill(start_color='2F5496', end_color='2F5496', fill_type='solid')
SECTION_FONT = Font(name='Calibri', bold=True, size=11, color='2F5496')
SECTION_FILL = PatternFill(start_color='D6E4F0', end_color='D6E4F0', fill_type='solid')
BODY_FONT = Font(name='Calibri', size=10)
CONTEXT_FONT = Font(name='Calibri', size=10, italic=True)
TITLE_FONT = Font(name='Calibri', bold=True, size=14, color='2F5496')
SUBTITLE_FONT = Font(name='Calibri', bold=True, size=12, color='2F5496')
LABEL_FONT = Font(name='Calibri', bold=True, size=10)
VALUE_FONT = Font(name='Calibri', size=10)
THIN_BORDER = Border(
    left=Side(style='thin'), right=Side(style='thin'),
    top=Side(style='thin'), bottom=Side(style='thin'))
WRAP_ALIGN = Alignment(wrap_text=True, vertical='top')
CENTER_ALIGN = Alignment(horizontal='center', vertical='top', wrap_text=True)

# 13-column layout
COL_WIDTHS = {
    'A': 10,   # Ref
    'B': 11,   # Level
    'C': 20,   # Control
    'D': 28,   # Sub-Procedure
    'E': 50,   # Assessment Procedures
    'F': 35,   # Expected Evidence
    'G': 14,   # Method
    'H': 30,   # Procedures Performed
    'I': 25,   # Evidence Obtained
    'J': 12,   # Evidence Ref
    'K': 30,   # Observation / Findings
    'L': 16,   # Conclusion
    'M': 30,   # Recommendations
}

ASSESSMENT_HEADERS = [
    'Ref', 'Level', 'Control', 'Sub-Procedure', 'Assessment Procedures',
    'Expected Evidence', 'Method', 'Procedures Performed',
    'Evidence Obtained', 'Evidence Ref', 'Observation / Findings',
    'Conclusion', 'Recommendations'
]
NUM_COLS = len(ASSESSMENT_HEADERS)  # 13


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
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=NUM_COLS)
    cell = ws.cell(row=row, column=1, value=title)
    cell.font = SECTION_FONT
    cell.fill = SECTION_FILL
    cell.border = THIN_BORDER
    for col in range(2, NUM_COLS + 1):
        ws.cell(row=row, column=col).fill = SECTION_FILL
        ws.cell(row=row, column=col).border = THIN_BORDER


def write_context_row(ws, row, context):
    """Write a merged context row with italic text explaining why/what/risk."""
    ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=NUM_COLS)
    cell = ws.cell(row=row, column=1, value=context)
    cell.font = CONTEXT_FONT
    cell.alignment = WRAP_ALIGN
    cell.border = THIN_BORDER
    for col in range(2, NUM_COLS + 1):
        ws.cell(row=row, column=col).border = THIN_BORDER


def write_test_row(ws, row, ref, level, control, sub_proc, procedures, evidence, method='Inspection'):
    data = [ref, level, control, sub_proc, procedures, evidence, method, '', '', '', '', '', '']
    for col, value in enumerate(data, 1):
        cell = ws.cell(row=row, column=col, value=value)
        cell.font = BODY_FONT
        cell.alignment = WRAP_ALIGN
        cell.border = THIN_BORDER


# ── Scoping Sheet ───────────────────────────────────────────────────
def add_scoping_sheet(wb, engagement_name, scoping_note=None):
    ws = wb.create_sheet(title='Scoping')
    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 30
    ws.column_dimensions['C'].width = 40
    ws.column_dimensions['D'].width = 20
    ws.column_dimensions['E'].width = 30
    ws.column_dimensions['F'].width = 20

    r = 1
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value=f'ENGAGEMENT SCOPING — {engagement_name}').font = TITLE_FONT
    r += 2

    # Scoping note (cross-reference)
    if scoping_note:
        ws.merge_cells(f'A{r}:F{r}')
        cell = ws.cell(row=r, column=1, value=scoping_note)
        cell.font = CONTEXT_FONT
        cell.alignment = WRAP_ALIGN
        r += 2

    # Assessment levels explanation
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value='ASSESSMENT LEVELS').font = SUBTITLE_FONT
    r += 1
    levels = [
        ('ORG', 'Organisation / Enterprise level. Assessed ONCE per engagement. Policies, frameworks, governance structures that apply across all platforms and systems.'),
        ('PLATFORM', 'Platform / CSP level. Assessed PER PLATFORM in scope. If the FI uses AWS and Azure, repeat these test steps for each. Covers platform-specific configurations and controls.'),
        ('WORKLOAD', 'Workload / Application / System level. Assessed PER CRITICAL SYSTEM in scope using sampling. Covers system-specific deployments, configurations, and arrangements.'),
    ]
    for level, desc in levels:
        ws.cell(row=r, column=1, value=level).font = LABEL_FONT
        ws.merge_cells(f'B{r}:F{r}')
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=2).alignment = WRAP_ALIGN
        r += 1
    r += 1

    # Platforms in scope
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value='PLATFORMS / CSPs IN SCOPE').font = SUBTITLE_FONT
    r += 1
    headers = ['#', 'Platform / CSP', 'Service Models (IaaS/PaaS/SaaS)', 'Regions', 'Contract Ref', 'Notes']
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
    r += 1
    for i in range(1, 6):
        for col in range(1, 7):
            c = ws.cell(row=r, column=col, value=str(i) if col == 1 else '')
            c.border = THIN_BORDER
            c.font = VALUE_FONT
        r += 1
    r += 1

    # Critical systems in scope
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value='CRITICAL SYSTEMS / WORKLOADS IN SCOPE').font = SUBTITLE_FONT
    r += 1
    headers = ['#', 'System / Application Name', 'Platform', 'Criticality', 'Data Classification', 'Notes']
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
    r += 1
    for i in range(1, 11):
        for col in range(1, 7):
            c = ws.cell(row=r, column=col, value=str(i) if col == 1 else '')
            c.border = THIN_BORDER
            c.font = VALUE_FONT
        r += 1
    r += 1

    # Sampling approach
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value='SAMPLING APPROACH').font = SUBTITLE_FONT
    r += 1
    samples = [
        ('Assessment Period:', '[Start Date] to [End Date]'),
        ('User Access Samples:', '[e.g., 20 user accounts, 10 leavers/transfers]'),
        ('Change Management Samples:', '[e.g., 10 recent changes]'),
        ('Incident Samples:', '[e.g., 15 SOC alerts, all significant incidents in period]'),
        ('Firewall Rule Samples:', '[e.g., 20 rules]'),
        ('Configuration Samples:', '[e.g., 10 network devices]'),
    ]
    for label, val in samples:
        ws.cell(row=r, column=1, value=label).font = LABEL_FONT
        ws.merge_cells(f'B{r}:F{r}')
        ws.cell(row=r, column=2, value=val).font = VALUE_FONT
        r += 1

    return ws


# ── Planning Sheet ──────────────────────────────────────────────────
def add_planning_sheet(wb):
    ws = wb.create_sheet(title='Planning')
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 50
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 30

    r = 1
    ws.merge_cells(f'A{r}:E{r}')
    ws.cell(row=r, column=1, value='PLANNING AND SCOPING CHECKLIST').font = TITLE_FONT
    r += 2

    headers = ['Step', 'Activity', 'Responsible', 'Status', 'Notes']
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
    r += 1

    planning_steps = [
        ('P-01', 'Confirm engagement trigger and regulatory basis'),
        ('P-02', 'Issue engagement letter with scope, timeline, and deliverables'),
        ('P-03', 'Confirm IESP team qualifications and independence (Part C compliance)'),
        ('P-04', 'Issue Document Request List (DRL) to the FI'),
        ('P-05', 'Obtain and review prior assessment reports and remediation status'),
        ('P-06', 'Identify platforms/CSPs in scope and complete scoping sheet'),
        ('P-07', 'Identify critical systems/workloads in scope'),
        ('P-08', 'Define assessment period and sampling approach'),
        ('P-09', 'Determine engagement mode: design adequacy (pre-impl) or operating effectiveness (attestation)'),
        ('P-10', 'Determine if higher-risk services criteria apply (customer data, cross-border)'),
        ('P-11', 'Schedule site visits / remote assessment sessions'),
        ('P-12', 'Conduct kick-off meeting with FI management'),
        ('P-13', 'Receive and catalogue DRL responses'),
        ('P-14', 'Finalise scoping memorandum'),
    ]
    for ref, activity in planning_steps:
        data = [ref, activity, '', '', '']
        for col, val in enumerate(data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = BODY_FONT
            c.alignment = WRAP_ALIGN
            c.border = THIN_BORDER
        r += 1

    return ws


# ── Reporting Sheet ─────────────────────────────────────────────────
def add_reporting_sheet(wb):
    ws = wb.create_sheet(title='Reporting & Attestation')
    ws.column_dimensions['A'].width = 8
    ws.column_dimensions['B'].width = 50
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 15
    ws.column_dimensions['E'].width = 30

    r = 1
    ws.merge_cells(f'A{r}:E{r}')
    ws.cell(row=r, column=1, value='REPORTING AND ATTESTATION CHECKLIST').font = TITLE_FONT
    r += 2

    headers = ['Step', 'Activity', 'Responsible', 'Status', 'Notes']
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
    r += 1

    steps = [
        ('R-01', 'Consolidate all test results — compile conclusions from all assessment sheets'),
        ('R-02', 'Assign risk ratings (High/Medium/Low) to each finding based on likelihood and impact'),
        ('R-03', 'Map findings to specific regulatory references (Appendix clauses, Part D items)'),
        ('R-04', 'Draft recommendations with specific remediation steps, responsible parties, and timelines'),
        ('R-05', 'Distinguish must-fix-before-go-live findings from post-launch improvements (for pre-impl)'),
        ('R-06', 'Conduct quality assurance / peer review of working papers and findings'),
        ('R-07', 'Conduct findings walkthrough with FI management'),
        ('R-08', 'Incorporate management responses and agreed action plans'),
        ('R-09', 'Form Part C attestation opinion: Type A (Clean), Type B (With Exceptions), or Type C (Adverse)'),
        ('R-10', 'Prepare the formal report in Appendix 7 Part A format'),
        ('R-11', 'Confirm independence declaration and Part C compliance statement'),
        ('R-12', 'Obtain FI management sign-off on report and management action plans'),
        ('R-13', 'Prepare executive summary for designated board committee (per 8.3)'),
        ('R-14', 'Attend board committee meeting to present findings (if required)'),
        ('R-15', 'Document board committee directives and incorporate into final report'),
        ('R-16', 'Issue final signed report'),
    ]
    for ref, activity in steps:
        data = [ref, activity, '', '', '']
        for col, val in enumerate(data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = BODY_FONT
            c.alignment = WRAP_ALIGN
            c.border = THIN_BORDER
        r += 1

    return ws


# ── Part C Self-Assessment ──────────────────────────────────────────
def add_part_c_sheet(wb):
    ws = wb.create_sheet(title='Part C Self-Assessment')
    ws.column_dimensions['A'].width = 6
    ws.column_dimensions['B'].width = 20
    ws.column_dimensions['C'].width = 45
    ws.column_dimensions['D'].width = 40
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 30

    r = 1
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value='APPENDIX 7 PART C — IESP SELF-ASSESSMENT').font = TITLE_FONT
    r += 1
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value='The IESP must comply with these 6 requirements. Complete this self-assessment before issuing the report.').font = VALUE_FONT
    ws.cell(row=r, column=1).alignment = WRAP_ALIGN
    r += 2

    headers = ['#', 'Requirement', 'Assessment Criteria', 'Evidence / Justification', 'Compliant?', 'Notes']
    for col, h in enumerate(headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
    r += 1

    requirements = [
        ('1', 'Independence', 'The IESP is independent of the FI\'s technology operations and the systems/services being assessed. No conflicts of interest exist between the IESP and the FI.'),
        ('2', 'Competence', 'The IESP team has relevant professional qualifications (CISA, CISSP, CCSP, CSP-specific certs), certifications, and experience in the subject matter being assessed.'),
        ('3', 'Scope', 'The assessment covers ALL areas specified in the relevant appendix (Appendix 10, Appendix 9, or Part D as applicable). No required areas were excluded without documented justification.'),
        ('4', 'Methodology', 'The IESP uses a systematic, risk-based assessment methodology with clear criteria for evaluating controls. The methodology is documented and consistently applied.'),
        ('5', 'Reporting', 'Findings are reported in the Appendix 7 Part A format with clear risk ratings and actionable recommendations. The report is complete, accurate, and traceable to evidence.'),
        ('6', 'Quality Assurance', 'Internal QA processes were followed, including peer review of assessment work by a qualified reviewer who did not perform the assessment.'),
    ]
    for num, req, criteria in requirements:
        data = [num, req, criteria, '', '', '']
        for col, val in enumerate(data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = BODY_FONT
            c.alignment = WRAP_ALIGN
            c.border = THIN_BORDER
        r += 1

    r += 1
    ws.merge_cells(f'A{r}:F{r}')
    ws.cell(row=r, column=1, value='SIGN-OFF').font = SUBTITLE_FONT
    r += 1
    for label in ['Lead Assessor:', 'Quality Reviewer:']:
        ws.cell(row=r, column=1, value=label).font = LABEL_FONT
        ws.cell(row=r, column=2, value='________________________').font = VALUE_FONT
        ws.cell(row=r, column=4, value='Date:').font = LABEL_FONT
        ws.cell(row=r, column=5, value='______________').font = VALUE_FONT
        r += 1

    return ws


# ── Methodology Sheet ───────────────────────────────────────────────
def create_methodology_sheet(wb, engagement_name, regulatory_basis, scope_desc,
                              assessment_covers, engagement_type_label):
    ws = wb.active
    ws.title = 'Methodology & Approach'
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 60
    for col in 'CDEFGHIJKLM':
        ws.column_dimensions[col].width = 12

    r = 1
    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='INDEPENDENT ASSESSMENT — METHODOLOGY & APPROACH').font = TITLE_FONT
    r += 1
    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value=engagement_name).font = SUBTITLE_FONT
    r += 2

    ws.merge_cells(f'A{r}:M{r}')
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

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='SCOPE OF ASSESSMENT').font = SUBTITLE_FONT
    r += 1
    for text in [scope_desc, assessment_covers]:
        ws.merge_cells(f'A{r}:M{r}')
        ws.cell(row=r, column=1, value=text).font = VALUE_FONT
        ws.cell(row=r, column=1).alignment = WRAP_ALIGN
        r += 1
    r += 1

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='ENGAGEMENT MODE').font = SUBTITLE_FONT
    r += 1
    modes = [
        ('Design Adequacy (Pre-Implementation):', 'Assess whether proposed/planned controls are designed to meet the requirement. Evidence is primarily documentary: architecture designs, policies, vendor assessments, staging test results.'),
        ('Operating Effectiveness (Independent Attestation):', 'Assess whether controls operated effectively during the assessment period. Evidence is observation, sampling, re-performance, system-generated logs. Requires defined sampling methodology.'),
    ]
    for label, desc in modes:
        ws.merge_cells(f'A{r}:M{r}')
        ws.cell(row=r, column=1, value=label).font = LABEL_FONT
        r += 1
        ws.merge_cells(f'A{r}:M{r}')
        ws.cell(row=r, column=1, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=1).alignment = WRAP_ALIGN
        r += 1
    r += 1

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='ASSESSMENT LEVELS').font = SUBTITLE_FONT
    r += 1
    lvls = [
        ('ORG', 'Organisation-level. Assessed once per engagement (policies, governance, frameworks).'),
        ('PLATFORM', 'Platform/CSP-level. Assessed per platform in scope (configurations, controls per CSP).'),
        ('WORKLOAD', 'System/application-level. Assessed per critical system using sampling.'),
    ]
    for lvl, desc in lvls:
        ws.cell(row=r, column=1, value=lvl).font = LABEL_FONT
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=2).alignment = WRAP_ALIGN
        r += 1
    r += 1

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='ASSESSMENT METHODS').font = SUBTITLE_FONT
    r += 1
    for method, desc in [
        ('Inspection', 'Examination of documents, records, policies, configurations, and tangible evidence.'),
        ('Inquiry', 'Interviews with management, process owners, and staff.'),
        ('Observation', 'Direct observation of processes, systems, and activities.'),
        ('Confirmation', 'Verification with external or independent parties.'),
        ('Re-performance', 'IESP independently re-performs the control procedure.'),
    ]:
        ws.cell(row=r, column=1, value=method).font = LABEL_FONT
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=2).alignment = WRAP_ALIGN
        r += 1
    r += 1

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='CONCLUSION SCALE').font = SUBTITLE_FONT
    r += 1
    for conc, desc in [
        ('Compliant', 'Control fully implemented and operating effectively. Evidence supports regulatory criteria are met.'),
        ('Partially Compliant', 'Implemented but with gaps in scope, coverage, documentation, or effectiveness.'),
        ('Non-Compliant', 'Absent, fundamentally deficient, or not operating. Regulatory criteria not met.'),
        ('N/A', 'Not applicable to entity\'s operations. Justification documented.'),
    ]:
        ws.cell(row=r, column=1, value=conc).font = LABEL_FONT
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        ws.cell(row=r, column=2).alignment = WRAP_ALIGN
        r += 1
    r += 1

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='EVIDENCE HIERARCHY (prefer higher-ranked)').font = SUBTITLE_FONT
    r += 1
    for rank, desc in [
        ('Rank 1', 'Direct observation — IESP directly observes control in operation'),
        ('Rank 2', 'Independent confirmation — Third-party evidence (SOC 2, certifications)'),
        ('Rank 3', 'System-generated — Logs, configurations without manual intervention'),
        ('Rank 4', 'Re-performance — IESP re-performs control procedure'),
        ('Rank 5', 'Documentary — Policies, procedures, meeting minutes'),
        ('Rank 6', 'Inquiry — Verbal representations from FI personnel'),
    ]:
        ws.cell(row=r, column=1, value=rank).font = LABEL_FONT
        ws.cell(row=r, column=2, value=desc).font = VALUE_FONT
        r += 1
    r += 1

    # ── SAMPLING METHODOLOGY ──────────────────────────────────────
    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='SAMPLING METHODOLOGY').font = SUBTITLE_FONT
    r += 1

    ws.cell(row=r, column=1, value='Sampling Approach:').font = LABEL_FONT
    ws.merge_cells(f'B{r}:M{r}')
    ws.cell(row=r, column=2, value='Judgmental (not statistical) — appropriate for limited assurance engagements under BNM RMiT. Sample sizes are based on population size and control risk tier.').font = VALUE_FONT
    ws.cell(row=r, column=2).alignment = WRAP_ALIGN
    r += 2

    # Sample Size Table
    ws.cell(row=r, column=1, value='Sample Size Table:').font = LABEL_FONT
    r += 1
    sample_headers = ['Population Size', 'Standard Risk', 'High Risk', 'Rationale']
    for col, h in enumerate(sample_headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = LABEL_FONT
        c.border = THIN_BORDER
    r += 1
    sample_rows = [
        ('1-5', 'All', 'All', 'Full coverage feasible'),
        ('6-15', '3', '5', '~25-40% coverage'),
        ('16-50', '5', '8', 'Sufficient for pattern detection'),
        ('51-100', '8', '12', 'Diminishing returns beyond this'),
        ('100+', '10', '15', 'Cap with stratification'),
    ]
    for pop, std, high, rationale in sample_rows:
        data = [pop, std, high, rationale]
        for col, val in enumerate(data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = VALUE_FONT
            c.border = THIN_BORDER
            c.alignment = WRAP_ALIGN
        r += 1
    r += 1

    # Time-Based Evidence Coverage Table
    ws.cell(row=r, column=1, value='Time-Based Evidence Coverage:').font = LABEL_FONT
    r += 1
    time_headers = ['Evidence Type', 'Coverage Period', 'Rationale']
    for col, h in enumerate(time_headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = LABEL_FONT
        c.border = THIN_BORDER
    r += 1
    time_rows = [
        ('Board/committee reports', 'Last 4 quarters', 'Full annual governance cycle'),
        ('Operational records (incidents, changes, patches)', 'Last 3-6 months', 'Recent operating effectiveness'),
        ('Annual processes (risk assessment, DR test, pen test)', 'Last 12 months', 'Full cycle'),
        ('Continuous monitoring (SOC, logs, alerts)', 'Last 30 days', 'Current state verification'),
        ('Policies and frameworks', 'Current version + prior', 'Change tracking'),
    ]
    for etype, period, rationale in time_rows:
        data = [etype, period, rationale]
        for col, val in enumerate(data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = VALUE_FONT
            c.border = THIN_BORDER
            c.alignment = WRAP_ALIGN
        r += 1
    r += 1

    # Control Risk Tiers Table
    ws.cell(row=r, column=1, value='Control Risk Tiers:').font = LABEL_FONT
    r += 1
    tier_headers = ['Tier', 'Controls', 'Sampling Level']
    for col, h in enumerate(tier_headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = LABEL_FONT
        c.border = THIN_BORDER
    r += 1
    tier_rows = [
        ('Critical', 'Governance framework, SOC, incident response, regulatory notification, BCM, customer data protection', 'High risk samples'),
        ('Standard', 'Most controls (risk assessment, vuln mgmt, vendor assessment, change mgmt, etc.)', 'Standard risk samples'),
        ('Conditional', 'Emerging tech, specialised areas — may be N/A', 'Standard if applicable'),
    ]
    for tier, controls, sampling in tier_rows:
        data = [tier, controls, sampling]
        for col, val in enumerate(data, 1):
            c = ws.cell(row=r, column=col, value=val)
            c.font = VALUE_FONT
            c.border = THIN_BORDER
            c.alignment = WRAP_ALIGN
        r += 1
    r += 1

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='LIMITATIONS').font = SUBTITLE_FONT
    r += 1
    for lim in [
        '1. Limited assurance engagement — conclusions based on procedures performed, not absolute assurance.',
        '2. Point-in-time (design adequacy) or period assessment (operating effectiveness).',
        '3. Reliance on management representations and documentation provided.',
        '4. Scope guided by BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025).',
        '5. Does not constitute legal or regulatory advice.',
        '6. The IESP remains solely responsible for the sufficiency of work performed.',
    ]:
        ws.merge_cells(f'A{r}:M{r}')
        ws.cell(row=r, column=1, value=lim).font = VALUE_FONT
        ws.cell(row=r, column=1).alignment = WRAP_ALIGN
        r += 1
    r += 1

    ws.merge_cells(f'A{r}:M{r}')
    ws.cell(row=r, column=1, value='SIGN-OFF').font = SUBTITLE_FONT
    r += 1
    for s in ['Lead Assessor:', 'Quality Reviewer:', 'Entity Representative:']:
        ws.cell(row=r, column=1, value=s).font = LABEL_FONT
        ws.cell(row=r, column=2, value='________________________').font = VALUE_FONT
        ws.cell(row=r, column=6, value='Date:').font = LABEL_FONT
        ws.cell(row=r, column=7, value='______________').font = VALUE_FONT
        r += 1
    return ws


# ── Part D (shared) ─────────────────────────────────────────────────
PART_D_SECTIONS = [
    ('Item 1(a) — Access Control',
     'Access control is foundational — who can access what. Expect policy-driven provisioning, periodic reviews, PAM controls, timely revocation. Excessive access is the most common audit finding.',
     [
        ('PD-01', 'ORG', 'Access Control', 'Access control policies and mechanisms',
         '1. Obtain the FI\'s access control policy and supporting standards.\n2. Verify policy covers user registration, de-registration, access provisioning, and privilege management.\n3. Sample 20 user accounts — verify access rights are consistent with job roles (least privilege).\n4. Check that access reviews are performed periodically (quarterly for privileged, semi-annually for standard).\n5. Verify access revocation upon termination — sample 10 recent leavers/transfers.',
         'Access control policy; User access provisioning records; Access review reports; HR leaver/transfer list vs. access revocation logs', 'Inspection'),
        ('PD-02', 'ORG', 'Access Control', 'Privileged access management',
         '1. Obtain the PAM policy or standard.\n2. Obtain the list of all privileged accounts (system admin, DBA, root, domain admin).\n3. Verify privileged accounts are individually assigned or vault-managed with session recording.\n4. Check that privileged access is time-bound and subject to approval workflow.\n5. Review privileged session logs for the past 3 months for anomalies.',
         'PAM policy; Privileged account inventory; PAM tool configuration and logs; Session recording samples', 'Inspection'),
    ]),
    ('Item 1(b) — Physical and Environmental Security',
     'Physical controls protect technology assets from unauthorised access and environmental threats. Expect multi-layered access, CCTV, environmental monitoring. Physical compromise bypasses logical controls.',
     [
        ('PD-03', 'ORG', 'Physical Security', 'Physical security controls',
         '1. Identify all sensitive areas (data centres, server rooms, network rooms).\n2. Verify multi-layered physical access controls (badge, biometric, PIN).\n3. Review visitor management procedures.\n4. Verify CCTV coverage with minimum 90-day retention.\n5. Sample-check physical access logs against approved access lists.',
         'Physical security policy; Access control system config; Visitor logs; CCTV coverage map; Physical access log reconciliation', 'Inspection / Observation'),
        ('PD-04', 'ORG', 'Physical Security', 'Environmental controls',
         '1. Verify fire detection and suppression systems are current on inspections.\n2. Check water leak detection.\n3. Verify temperature and humidity monitoring with alerts.\n4. Confirm environmental incident response procedures are tested.',
         'Fire system inspection certificates; Water leak detection layout; Environmental monitoring dashboards; Incident response test records', 'Inspection / Observation'),
    ]),
    ('Item 1(c) — Operations Security',
     'Operational controls ensure systems are managed securely. Expect documented procedures, controlled changes, tested backups, malware protection, vulnerability management. Operational failures cause avoidable incidents.',
     [
        ('PD-05', 'ORG', 'Operations Security', 'Operational procedures and controls',
         '1. Obtain documented operating procedures (change mgmt, capacity mgmt, backup, malware protection).\n2. Verify change management — sample 10 changes with full lifecycle.\n3. Verify backup procedures — confirm critical systems backed up and restore tested.\n4. Verify anti-malware deployed with current signatures.',
         'Operating procedures; 10 sampled change records; Backup schedule and restore test results; Anti-malware deployment reports', 'Inspection'),
        ('PD-06', 'ORG', 'Operations Security', 'Vulnerability management and patching',
         '1. Obtain vulnerability management policy and patching SLAs.\n2. Review most recent vulnerability scan results.\n3. Check patch compliance rates.\n4. Verify exceptions are formally risk-accepted.',
         'Vulnerability management policy; Scan reports; Patch compliance dashboard; Risk acceptance records', 'Inspection'),
    ]),
    ('Item 1(d) — Communications Security',
     'Network controls protect data in transit and network integrity. Expect segmentation, least-privilege firewall rules, encryption, IDS/IPS. Network compromise provides access to all connected systems.',
     [
        ('PD-07', 'ORG', 'Communications Security', 'Network security and secure communications',
         '1. Review network segmentation.\n2. Verify firewall rules — sample 20 rules for least-privilege.\n3. Confirm encryption of data in transit (TLS 1.2+).\n4. Verify secure configuration of email, messaging, file transfer.\n5. Check IDS/IPS deployed at critical boundaries.',
         'Network architecture diagram; Firewall rule base sample; TLS configuration; IDS/IPS deployment and alert records', 'Inspection'),
    ]),
    ('Item 1(e) — Incident Management',
     'Incident management ensures timely detection, response, and recovery. Expect 24/7 SOC, SIEM, IR playbooks, annual exercises. Without incident management, breaches escalate unchecked.',
     [
        ('PD-08', 'ORG', 'Incident Management', 'Incident management framework',
         '1. Obtain incident management policy and procedures.\n2. Verify incident classification scheme.\n3. Review incident log for past 12 months.\n4. Verify RCA for significant incidents with corrective actions.\n5. Confirm regulatory notification procedures.',
         'Incident management policy; Classification matrix; Incident log (12 months); RCA reports; Regulatory notification records', 'Inspection'),
        ('PD-09', 'ORG', 'Incident Management', 'Detection and response capabilities',
         '1. Confirm SOC operates 24/7.\n2. Verify SIEM deployment with critical log sources.\n3. Sample 15 alerts — verify triage.\n4. Confirm IR playbooks for common scenarios.\n5. Verify annual IR drills/tabletop exercises.',
         'SOC operational documentation; SIEM log source inventory; 15 sampled alert records; IR playbooks; Drill/tabletop reports', 'Inspection / Inquiry'),
    ]),
    ('Item 1(f) — Business Continuity',
     'Business continuity ensures operations continue during disruptions. Expect BCP/DRP with cyber scenarios, tested DR including security controls, redundant security infrastructure. Untested DR fails when needed.',
     [
        ('PD-10', 'ORG', 'Business Continuity', 'Security in BCP/DRP',
         '1. Obtain BCP and IT DRP.\n2. Verify security requirements addressed in BCP/DRP.\n3. Check BCP/DRP includes cyber incident scenarios.\n4. Verify recovery procedures include security validation.',
         'BCP and IT DRP; Security requirements in BCP/DRP; Cyber incident scenarios; Recovery security validation checklists', 'Inspection'),
        ('PD-11', 'ORG', 'Business Continuity', 'BCP/DRP testing with security controls',
         '1. Review most recent BCP/DRP test.\n2. Verify security controls tested during DR exercise.\n3. Confirm security findings remediated.\n4. Verify DR site maintains equivalent security posture.',
         'BCP/DRP test plan and results; Security test components; DR site security assessment; Remediation tracker', 'Inspection'),
        ('PD-12', 'ORG', 'Business Continuity', 'Redundancy of security infrastructure',
         '1. Identify critical security infrastructure and verify HA configuration.\n2. Confirm failover tested.\n3. Verify monitoring continues during DR.\n4. Check licenses valid at DR site.',
         'Security infrastructure HA architecture; Failover test records; DR monitoring evidence; License/subscription records', 'Inspection'),
    ]),
    ('Item 2(a) — Customer Identity Authentication',
     'Customer authentication protects online services from unauthorised access. Expect MFA, secure sessions, strong cryptography, anti-session-fixation. Weak authentication directly exposes customers.',
     [
        ('PD-13', 'WORKLOAD', 'Customer Authentication', 'Session and MITM protection',
         '1. Review session management controls.\n2. Verify TLS 1.2+, HSTS, certificate validity.\n3. Confirm session tokens are cryptographically random with proper expiry.\n4. Check anti-session-fixation controls.\n5. Verify certificate pinning for mobile apps.',
         'TLS scan results; Session management config; Application security assessment; Mobile cert pinning evidence', 'Inspection'),
        ('PD-14', 'WORKLOAD', 'Customer Authentication', 'Internal controls for online systems',
         '1. Verify application hardening.\n2. Review app security testing results (SAST, DAST, pen test).\n3. Confirm database security controls.\n4. Check segmentation from corporate network.',
         'Hardening standards; App security test reports; Database security config; Network segmentation evidence', 'Inspection'),
        ('PD-15', 'WORKLOAD', 'Customer Authentication', 'Multi-level authentication',
         '1. Review authentication architecture.\n2. Verify MFA for login and high-risk transactions.\n3. Check out-of-band authentication mechanisms.\n4. Verify real-time verification for high-value transactions.\n5. Assess authentication strength relative to transaction risk.',
         'Authentication architecture; MFA config; OTP/out-of-band mechanism; Risk-based authentication rules', 'Inspection'),
        ('PD-16', 'WORKLOAD', 'Customer Authentication', 'Session handling and credential storage',
         '1. Verify session timeouts (idle and absolute).\n2. Confirm concurrent session controls.\n3. Verify credentials stored with strong hashing (bcrypt, Argon2).\n4. Check auth database access-restricted and encrypted.\n5. Review account lockout configuration.',
         'Session management config; Password hashing evidence; Auth database access controls; Account lockout config', 'Inspection'),
        ('PD-17', 'ORG', 'Customer Authentication', 'Cryptographic implementation',
         '1. Review cryptographic standards (AES-256, RSA-2048+, ECDSA P-256+).\n2. Verify key management practices.\n3. Check no deprecated algorithms.\n4. Verify crypto implementation reviewed/tested.',
         'Cryptographic standards document; Key management procedures; HSM config; Crypto assessment results', 'Inspection'),
    ]),
    ('Item 2(b) — Transaction Authentication',
     'Transaction authentication ensures non-repudiation and integrity. Expect transaction signing, tamper-evident audit trails, mutual authentication. Without non-repudiation, disputes cannot be resolved.',
     [
        ('PD-18', 'WORKLOAD', 'Transaction Authentication', 'Proof of origin and integrity',
         '1. Review transaction signing/MAC mechanisms.\n2. Verify records include origin, timestamp, hash, integrity verification.\n3. Confirm tamper-evident audit trails.\n4. Check logs sufficient for dispute resolution.',
         'Transaction authentication mechanism; Sample transaction records; Audit trail controls; Log retention policy', 'Inspection'),
        ('PD-19', 'WORKLOAD', 'Transaction Authentication', 'Secure delivery and mutual authentication',
         '1. Verify delivery channel secured end-to-end.\n2. Check alerts for high-risk transaction types.\n3. Verify mutual authentication for B2B channels.\n4. Review triggers for additional authentication.',
         'Channel security architecture; Transaction alert config; Mutual authentication implementation; Authentication trigger criteria', 'Inspection'),
    ]),
    ('Item 2(c) — Segregation of Duties',
     'SoD prevents single-person control over critical operations. Expect maker-checker, privileged user reviews, tamper-resistant authorisation. SoD failures enable fraud.',
     [
        ('PD-20', 'WORKLOAD', 'Segregation of Duties', 'Dual control for online transactions',
         '1. Identify critical functions in online transaction systems.\n2. Verify maker-checker for critical operations.\n3. Review access control matrices — no single user can initiate and approve.\n4. Verify unauthorised access detection.',
         'Access control matrices; Maker-checker config; Dual control workflow; Unauthorised access detection controls', 'Inspection'),
        ('PD-21', 'WORKLOAD', 'Segregation of Duties', 'Authorisation database integrity',
         '1. Verify authorisation database is tamper-resistant.\n2. Confirm changes require approval and are logged.\n3. Obtain privileged user list — verify quarterly review.\n4. Check reviews result in revocation of unnecessary access.',
         'Auth database access controls; Change logs; Privileged user review records; Revocation evidence', 'Inspection'),
    ]),
    ('Item 2(d) — Data Integrity',
     'Data integrity controls prevent tampering and ensure confidentiality. Expect E2E encryption, defence-in-depth, pen testing, audit trails. Data integrity failure causes financial loss and regulatory breach.',
     [
        ('PD-22', 'ORG', 'Data Integrity', 'End-to-end encryption and multi-layer security',
         '1. Verify E2E encryption for external communications.\n2. Review multi-layer network security (defence-in-depth).\n3. Confirm each layer independently managed.\n4. Verify security devices current on firmware/signatures.',
         'Encryption architecture; Multi-layer security diagram; Security device inventory; Management and monitoring evidence', 'Inspection'),
        ('PD-23', 'ORG', 'Data Integrity', 'Absence of single points of failure',
         '1. Review network architecture for SPOF.\n2. Verify redundancy at each critical layer.\n3. Confirm failover tested within 12 months.\n4. Check SPOF analysis documented.',
         'Network architecture with redundancy; SPOF analysis; Failover test results; SPOF review history', 'Inspection'),
        ('PD-24', 'ORG', 'Data Integrity', 'Security assessment and audit trails',
         '1. Obtain most recent pen test and network security assessment.\n2. Verify testing by qualified party within 12 months.\n3. Confirm vulnerabilities remediated or risk-accepted.\n4. Verify audit trail capabilities.\n5. Confirm logs tamper-protected and retained.',
         'Pen test report; Network security assessment; Audit trail config and sample logs; Log integrity controls', 'Inspection'),
        ('PD-25', 'WORKLOAD', 'Data Integrity', 'Data confidentiality and risk-based auth',
         '1. Verify confidentiality controls (encryption, masking, access controls).\n2. Confirm data classification applied.\n3. Verify risk-based step-up authentication.\n4. Check customers receive timely transaction notifications.',
         'Data classification scheme; Encryption and masking config; Risk-based auth rules; Customer notification samples', 'Inspection'),
    ]),
    ('Item 2(e) — Mobile Device Risks',
     'Mobile apps require additional protections due to the untrusted device environment. Expect jailbreak detection, secure storage, certificate pinning, fake app monitoring. Mobile-specific attacks bypass server-side controls.',
     [
        ('PD-26', 'WORKLOAD', 'Mobile Device Security', 'Mobile app security baseline',
         '1. Confirm minimum OS version enforced and jailbreak/root detection.\n2. Review most recent mobile pen test.\n3. Verify vulnerabilities remediated.\n4. Confirm secure E2E communication (cert pinning, TLS 1.2+).',
         'OS version enforcement; Jailbreak/root detection; Mobile pen test report; Remediation evidence; Communication security config', 'Inspection'),
        ('PD-27', 'WORKLOAD', 'Mobile Device Security', 'Mobile data protection',
         '1. Verify sensitive data not stored on device or only in secure enclaves.\n2. Confirm cache/logs sanitised.\n3. Verify clipboard access restricted.\n4. Check remote wipe capability.',
         'Mobile app security architecture; Data storage review; Secure enclave usage; Remote wipe documentation', 'Inspection'),
        ('PD-28', 'WORKLOAD', 'Mobile Device Security', 'Transaction notification and codes',
         '1. Verify transaction notifications (push, SMS, email).\n2. Verify suspicious transaction alerts.\n3. Confirm unique per-transaction codes (TAC, OTP).\n4. Verify code expiry (2-5 min) and single-use.',
         'Transaction notification config; Suspicious alert rules; Code generation mechanism; Code expiry config', 'Inspection'),
        ('PD-29', 'WORKLOAD', 'Mobile Device Security', 'App distribution and fake app monitoring',
         '1. Verify publishing access controls.\n2. Confirm monitoring for fake/fraudulent apps.\n3. Verify takedown process exists and exercised.\n4. Review fake app incident history.',
         'Publishing access controls; Fake app monitoring service; Takedown process docs; Fake app incident log', 'Inspection'),
    ]),
]


def add_part_d_sheet(wb, sheet_name='Appendix 7 Part D'):
    ws = wb.create_sheet(title=sheet_name)
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1
    for section_data in PART_D_SECTIONS:
        section_title, context, tests = section_data
        write_section_row(ws, r, section_title)
        r += 1
        if context:
            write_context_row(ws, r, context)
            r += 1
        for test in tests:
            write_test_row(ws, r, *test)
            r += 1
    return ws


# ── Scoring Dashboard ──────────────────────────────────────────────
NON_ASSESSMENT_SHEETS = {
    'Methodology & Approach', 'Scoping', 'Planning',
    'Reporting & Attestation', 'Part C Self-Assessment', 'Scoring Dashboard',
}

COMPLIANT_FILL = PatternFill(start_color='C6EFCE', end_color='C6EFCE', fill_type='solid')
PARTIAL_FILL = PatternFill(start_color='FFEB9C', end_color='FFEB9C', fill_type='solid')
NON_COMPLIANT_FILL = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')
NA_FILL = PatternFill(start_color='D9D9D9', end_color='D9D9D9', fill_type='solid')
SCORE_FONT_GREEN = Font(name='Calibri', bold=True, size=11, color='006100')
SCORE_FONT_AMBER = Font(name='Calibri', bold=True, size=11, color='9C6500')
SCORE_FONT_RED = Font(name='Calibri', bold=True, size=11, color='9C0006')


def add_scoring_sheet(wb):
    """Add a Scoring Dashboard sheet with per-sheet summaries, overall totals,
    Part C opinion indicator, and level breakdown using live COUNTIF formulas."""
    ws = wb.create_sheet(title='Scoring Dashboard')
    ws.column_dimensions['A'].width = 35
    ws.column_dimensions['B'].width = 16
    ws.column_dimensions['C'].width = 20
    ws.column_dimensions['D'].width = 18
    ws.column_dimensions['E'].width = 14
    ws.column_dimensions['F'].width = 16
    ws.column_dimensions['G'].width = 16
    ws.column_dimensions['H'].width = 18

    # Identify assessment sheets
    assessment_sheets = [
        s for s in wb.sheetnames if s not in NON_ASSESSMENT_SHEETS
    ]

    r = 1
    # ── Title ──
    ws.merge_cells(f'A{r}:H{r}')
    ws.cell(row=r, column=1, value='SCORING DASHBOARD').font = TITLE_FONT
    r += 2

    # ── Overall Summary ──
    ws.merge_cells(f'A{r}:H{r}')
    ws.cell(row=r, column=1, value='OVERALL SUMMARY').font = SUBTITLE_FONT
    r += 1

    overall_headers = ['Metric', 'Value']
    for col, h in enumerate(overall_headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
    r += 1

    # We'll place per-sheet data starting at per_sheet_start_row
    # Overall summary references those rows via SUM formulas
    # We need to know where per-sheet data will be, so calculate offsets
    # Overall summary rows: 7 metric rows (Compliant, Partial, NC, NA, Not Assessed, Total, Compliance %)
    # + 1 blank + Part C opinion = 9 rows
    # Then blank, level breakdown section
    overall_start_row = r  # first data row of overall summary

    overall_labels = [
        'Total Compliant',
        'Total Partially Compliant',
        'Total Non-Compliant',
        'Total N/A',
        'Total Not Assessed',
        'Total Test Steps',
        'Overall Compliance %',
    ]
    # Reserve rows for overall metrics (we'll fill formulas after per-sheet section)
    for label in overall_labels:
        ws.cell(row=r, column=1, value=label).font = LABEL_FONT
        ws.cell(row=r, column=1).border = THIN_BORDER
        ws.cell(row=r, column=2).font = VALUE_FONT
        ws.cell(row=r, column=2).border = THIN_BORDER
        r += 1

    r += 1
    # Part C opinion indicator
    ws.merge_cells(f'A{r}:B{r}')
    ws.cell(row=r, column=1, value='PART C OPINION INDICATOR').font = SUBTITLE_FONT
    r += 1
    ws.cell(row=r, column=1, value='Opinion Type').font = LABEL_FONT
    ws.cell(row=r, column=1).border = THIN_BORDER
    ws.cell(row=r, column=2).border = THIN_BORDER
    opinion_row = r
    r += 1

    ws.cell(row=r, column=1, value='Criteria:').font = CONTEXT_FONT
    ws.cell(row=r, column=1).border = THIN_BORDER
    ws.merge_cells(f'B{r}:H{r}')
    ws.cell(row=r, column=2,
            value='Type A (Clean): NC=0 and PC<=3  |  '
                  'Type B (With Exceptions): NC>0 and NC<=5  |  '
                  'Type C (Adverse): NC>5').font = CONTEXT_FONT
    ws.cell(row=r, column=2).alignment = WRAP_ALIGN
    ws.cell(row=r, column=2).border = THIN_BORDER
    r += 2

    # ── Per-Sheet Summary ──
    ws.merge_cells(f'A{r}:H{r}')
    ws.cell(row=r, column=1, value='PER-SHEET BREAKDOWN').font = SUBTITLE_FONT
    r += 1

    ps_headers = ['Sheet', 'Compliant', 'Partially Compliant',
                  'Non-Compliant', 'N/A', 'Not Assessed', 'Total Steps',
                  'Compliance %']
    for col, h in enumerate(ps_headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
        c.alignment = CENTER_ALIGN
    r += 1

    per_sheet_first_row = r
    per_sheet_col_map = {
        'compliant': 'B',
        'partial': 'C',
        'nc': 'D',
        'na': 'E',
        'not_assessed': 'F',
        'total': 'G',
        'pct': 'H',
    }

    for sheet_name in assessment_sheets:
        ws.cell(row=r, column=1, value=sheet_name).font = LABEL_FONT
        ws.cell(row=r, column=1).border = THIN_BORDER

        safe = sheet_name.replace("'", "''")

        # Compliant count — COUNTIF on column L
        ws.cell(row=r, column=2).font = VALUE_FONT
        ws.cell(row=r, column=2).border = THIN_BORDER
        ws.cell(row=r, column=2).fill = COMPLIANT_FILL
        ws.cell(row=r, column=2,
                value=f"=COUNTIF('{safe}'!L:L,\"Compliant\")")

        # Partially Compliant
        ws.cell(row=r, column=3).font = VALUE_FONT
        ws.cell(row=r, column=3).border = THIN_BORDER
        ws.cell(row=r, column=3).fill = PARTIAL_FILL
        ws.cell(row=r, column=3,
                value=f"=COUNTIF('{safe}'!L:L,\"Partially Compliant\")")

        # Non-Compliant
        ws.cell(row=r, column=4).font = VALUE_FONT
        ws.cell(row=r, column=4).border = THIN_BORDER
        ws.cell(row=r, column=4).fill = NON_COMPLIANT_FILL
        ws.cell(row=r, column=4,
                value=f"=COUNTIF('{safe}'!L:L,\"Non-Compliant\")")

        # N/A
        ws.cell(row=r, column=5).font = VALUE_FONT
        ws.cell(row=r, column=5).border = THIN_BORDER
        ws.cell(row=r, column=5).fill = NA_FILL
        ws.cell(row=r, column=5,
                value=f"=COUNTIF('{safe}'!L:L,\"N/A\")")

        # Not Assessed (blank conclusions where a Ref exists in col A)
        ws.cell(row=r, column=6).font = VALUE_FONT
        ws.cell(row=r, column=6).border = THIN_BORDER
        ws.cell(row=r, column=6,
                value=f"=COUNTIFS('{safe}'!A:A,\"<>\",'{safe}'!L:L,\"=\")"
                      f"-COUNTIF('{safe}'!A:A,\"Ref\")")

        # Total test steps (rows with a Ref value, minus header row)
        ws.cell(row=r, column=7).font = VALUE_FONT
        ws.cell(row=r, column=7).border = THIN_BORDER
        ws.cell(row=r, column=7,
                value=f"=COUNTA('{safe}'!A:A)"
                      f"-COUNTIF('{safe}'!A:A,\"Ref\")-COUNTBLANK('{safe}'!A1)")

        # Compliance % = Compliant / (Total - N/A - Not Assessed)
        b_col = f'B{r}'
        g_col = f'G{r}'
        e_col = f'E{r}'
        f_col = f'F{r}'
        ws.cell(row=r, column=8).font = VALUE_FONT
        ws.cell(row=r, column=8).border = THIN_BORDER
        ws.cell(row=r, column=8).number_format = '0.0%'
        ws.cell(row=r, column=8,
                value=f'=IF(({g_col}-{e_col}-{f_col})=0,"—",'
                      f'{b_col}/({g_col}-{e_col}-{f_col}))')

        r += 1

    per_sheet_last_row = r - 1

    # ── Fill Overall Summary formulas ──
    # Row references for per-sheet columns
    ps_range_b = f'B{per_sheet_first_row}:B{per_sheet_last_row}'
    ps_range_c = f'C{per_sheet_first_row}:C{per_sheet_last_row}'
    ps_range_d = f'D{per_sheet_first_row}:D{per_sheet_last_row}'
    ps_range_e = f'E{per_sheet_first_row}:E{per_sheet_last_row}'
    ps_range_f = f'F{per_sheet_first_row}:F{per_sheet_last_row}'
    ps_range_g = f'G{per_sheet_first_row}:G{per_sheet_last_row}'

    or_row = overall_start_row  # Total Compliant
    ws.cell(row=or_row, column=2, value=f'=SUM({ps_range_b})')
    ws.cell(row=or_row, column=2).fill = COMPLIANT_FILL
    or_row += 1  # Total Partially Compliant
    ws.cell(row=or_row, column=2, value=f'=SUM({ps_range_c})')
    ws.cell(row=or_row, column=2).fill = PARTIAL_FILL
    or_row += 1  # Total Non-Compliant
    ws.cell(row=or_row, column=2, value=f'=SUM({ps_range_d})')
    ws.cell(row=or_row, column=2).fill = NON_COMPLIANT_FILL
    nc_cell = f'B{or_row}'
    or_row += 1  # Total N/A
    ws.cell(row=or_row, column=2, value=f'=SUM({ps_range_e})')
    ws.cell(row=or_row, column=2).fill = NA_FILL
    na_total_cell = f'B{or_row}'
    or_row += 1  # Total Not Assessed
    ws.cell(row=or_row, column=2, value=f'=SUM({ps_range_f})')
    not_assessed_cell = f'B{or_row}'
    or_row += 1  # Total Test Steps
    ws.cell(row=or_row, column=2, value=f'=SUM({ps_range_g})')
    total_cell = f'B{or_row}'
    or_row += 1  # Overall Compliance %
    compliant_cell = f'B{overall_start_row}'
    ws.cell(row=or_row, column=2).number_format = '0.0%'
    ws.cell(row=or_row, column=2,
            value=f'=IF(({total_cell}-{na_total_cell}-{not_assessed_cell})=0,"—",'
                  f'{compliant_cell}/({total_cell}-{na_total_cell}-{not_assessed_cell}))')

    # Part C opinion IF formula
    pc_cell = f'B{overall_start_row + 1}'  # Partially Compliant total
    ws.cell(row=opinion_row, column=2,
            value=f'=IF({nc_cell}>5,"Type C (Adverse)",'
                  f'IF({nc_cell}>0,"Type B (With Exceptions)",'
                  f'IF({pc_cell}<=3,"Type A (Clean)","Type B (With Exceptions)")))')

    r += 2

    # ── Level Breakdown ──
    ws.merge_cells(f'A{r}:H{r}')
    ws.cell(row=r, column=1, value='LEVEL BREAKDOWN').font = SUBTITLE_FONT
    r += 1

    lvl_headers = ['Level', 'Compliant', 'Partially Compliant',
                   'Non-Compliant', 'N/A', 'Not Assessed', 'Total', '']
    for col, h in enumerate(lvl_headers, 1):
        c = ws.cell(row=r, column=col, value=h)
        c.font = HEADER_FONT
        c.fill = HEADER_FILL
        c.border = THIN_BORDER
        c.alignment = CENTER_ALIGN
    r += 1

    for level in ['ORG', 'PLATFORM', 'WORKLOAD']:
        ws.cell(row=r, column=1, value=level).font = LABEL_FONT
        ws.cell(row=r, column=1).border = THIN_BORDER

        # Build COUNTIFS formulas summing across all assessment sheets
        # Each conclusion type needs: COUNTIFS(sheet!B:B,"LEVEL",sheet!L:L,"conclusion")
        conclusions = [
            ('Compliant', 2, COMPLIANT_FILL),
            ('Partially Compliant', 3, PARTIAL_FILL),
            ('Non-Compliant', 4, NON_COMPLIANT_FILL),
            ('N/A', 5, NA_FILL),
        ]
        for conclusion, col_idx, fill in conclusions:
            parts = []
            for sn in assessment_sheets:
                safe = sn.replace("'", "''")
                parts.append(
                    f"COUNTIFS('{safe}'!B:B,\"{level}\",'{safe}'!L:L,\"{conclusion}\")"
                )
            formula = '=' + '+'.join(parts) if parts else '=0'
            c = ws.cell(row=r, column=col_idx, value=formula)
            c.font = VALUE_FONT
            c.border = THIN_BORDER
            c.fill = fill

        # Not Assessed by level: rows with matching level in B and blank in L
        na_parts = []
        for sn in assessment_sheets:
            safe = sn.replace("'", "''")
            na_parts.append(
                f"COUNTIFS('{safe}'!B:B,\"{level}\",'{safe}'!L:L,\"=\")"
            )
        na_formula = '=' + '+'.join(na_parts) if na_parts else '=0'
        c = ws.cell(row=r, column=6, value=na_formula)
        c.font = VALUE_FONT
        c.border = THIN_BORDER

        # Total by level
        ws.cell(row=r, column=7,
                value=f'=SUM(B{r}:F{r})').font = VALUE_FONT
        ws.cell(row=r, column=7).border = THIN_BORDER

        r += 1

    return ws


# ── Helper to build a workbook with all common sheets ───────────────
def build_workbook(engagement_name, regulatory_basis, scope_desc,
                   assessment_covers, engagement_type_label,
                   domain_sheets_fn, scoping_note=None):
    """Build a complete workbook with methodology, scoping, planning,
    domain assessment sheets, Part D, reporting, and Part C."""
    wb = openpyxl.Workbook()
    create_methodology_sheet(wb, engagement_name, regulatory_basis,
                             scope_desc, assessment_covers, engagement_type_label)
    add_scoping_sheet(wb, engagement_name, scoping_note=scoping_note)
    add_planning_sheet(wb)
    domain_sheets_fn(wb)  # Add domain-specific assessment sheets
    add_part_d_sheet(wb)
    add_reporting_sheet(wb)
    add_part_c_sheet(wb)
    add_scoring_sheet(wb)
    return wb


# ── CLOUD AWP ───────────────────────────────────────────────────────
def add_cloud_sheets(wb):
    # Part A — Governance
    ws = wb.create_sheet(title='App 10 Part A - Governance')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    part_a = [
        ('A1 — Cloud Strategy',
         'BNM expects the FI\'s cloud strategy to be board-approved and aligned with business strategy. Assessor should find a documented strategy with clear workload eligibility criteria. Without this, cloud adoption is ad hoc and uncontrolled.',
         [
            ('CLD-01', 'ORG', 'Cloud Strategy', 'Board-approved cloud strategy',
             '1. Obtain the FI\'s board-approved cloud strategy document.\n2. Verify alignment with overall business and technology strategy.\n3. Check that the strategy defines cloud-eligible vs non-eligible workloads.\n4. Verify cloud-first, cloud-selective, or hybrid approach is defined and justified.\n5. Check multi-cloud vs single-cloud considerations.\n6. Verify regular review cycle (at least annual).',
             'Board-approved cloud strategy; Workload classification criteria; Cloud adoption roadmap; Strategy review records', 'Inspection'),
        ]),
        ('A2 — Roles and Responsibilities',
         'RMiT requires clear accountability for cloud operations, security, and governance. Expect a RACI matrix and documented shared responsibility model per CSP. Without defined roles, accountability gaps lead to control failures.',
         [
            ('CLD-02', 'ORG', 'Roles & Responsibilities', 'RACI and shared responsibility model',
             '1. Obtain the cloud RACI matrix covering operations, security, and governance.\n2. Verify cloud-specific roles are defined (cloud architect, cloud security engineer, cloud operations).\n3. Check that the shared responsibility model with each CSP is documented and understood.\n4. Verify escalation paths for cloud-related issues.\n5. Check third-party management roles for cloud vendors.',
             'Cloud RACI matrix; Cloud role descriptions; Shared responsibility model per CSP; Org chart; Escalation procedures', 'Inspection / Inquiry'),
        ]),
        ('A3 — Policies and Procedures',
         'Cloud-specific policies operationalise the governance framework. Expect policies covering security, access, data, change, and incident response, communicated to staff. Without policies, controls lack a basis for enforcement.',
         [
            ('CLD-03', 'ORG', 'Cloud Policy', 'Cloud usage governance',
             '1. Obtain the FI\'s cloud usage/security policy.\n2. Verify it covers: approved CSPs, service/deployment models, data classification requirements, security baselines, approval workflow.\n3. Check the policy is communicated to stakeholders.\n4. Sample 3 recent cloud adoptions and check adherence.',
             'Cloud usage policy; Communication/awareness records; Sample cloud adoption records', 'Inspection'),
        ]),
        ('A4 — Risk Management',
         'BNM requires cloud risk assessment per 10.50 and Appendix 10. Expect a maintained risk register with risks assessed per CSP/service, reviewed annually. Without cloud-specific risk assessment, risk decisions are uninformed.',
         [
            ('CLD-04', 'ORG', 'Cloud Risk Management', 'Cloud-specific risk assessment',
             '1. Obtain the FI\'s cloud risk assessment framework.\n2. Verify it covers: data sovereignty, vendor lock-in, shared tenancy, supply chain, regulatory compliance.\n3. Check risks are assessed per CSP and per service.\n4. Verify risk assessment reviewed at least annually.',
             'Cloud risk assessment framework; Risk register (cloud section); Review/approval records', 'Inspection'),
            ('CLD-05', 'ORG', 'Cloud Risk Management', 'Cloud risk appetite and tolerance',
             '1. Check the FI has defined what can/cannot be placed in cloud.\n2. Verify data classification rules for cloud placement.\n3. Confirm risk appetite approved by board or designated committee.',
             'Cloud risk appetite statement; Data classification-to-cloud mapping; Board/committee approval', 'Inspection'),
        ]),
        ('A5 — Competency',
         'RMiT requires the FI to independently assess cloud posture. Expect cloud certifications, training plans, and succession planning. Without skilled personnel, the FI cannot manage cloud risk independently.',
         [
            ('CLD-06', 'ORG', 'Competency', 'Cloud team capability',
             '1. Review cloud team structure, roles, and responsibilities.\n2. Verify cloud certifications held by key personnel (AWS SAA/SAP, Azure AZ-500, GCP Professional, CCSP, CCSK).\n3. Check training and development plan exists.\n4. Assess whether the FI can independently assess CSP configurations.\n5. Review succession planning for critical cloud roles.',
             'Cloud team org chart; Certification records; Training plan; Skills gap analysis; Succession plans', 'Inspection / Inquiry'),
        ]),
        ('A6 — Compliance',
         'Data residency, BNM access rights, and PDPA compliance are non-negotiable. Expect regulatory mapping and verified compliance controls. Non-compliance can result in regulatory action.',
         [
            ('CLD-07', 'ORG', 'Compliance', 'Regulatory mapping and compliance',
             '1. Obtain the FI\'s regulatory compliance mapping for cloud (RMiT, PDPA, sectoral guidelines).\n2. Verify data residency requirements identified and addressed.\n3. Check cross-border data transmission requirements assessed.\n4. Verify BNM access rights to data and systems preserved contractually and technically.\n5. Confirm audit access rights preserved in CSP contracts.\n6. Check compliance monitoring and reporting in place.',
             'Regulatory compliance mapping; Data residency analysis; Cross-border data flow assessment; CSP contract provisions for regulatory/audit access; Compliance monitoring reports', 'Inspection'),
        ]),
        ('A7 — Oversight',
         'Board-level visibility into cloud risk is required. Expect KPI/KRI reporting, SLA monitoring, and internal audit coverage. Without oversight, emerging risks go undetected.',
         [
            ('CLD-08', 'ORG', 'Oversight', 'Cloud performance and oversight framework',
             '1. Review the FI\'s cloud performance monitoring framework (KPIs, KRIs).\n2. Verify regular reporting to board/senior management on cloud operations.\n3. Check CSP performance monitored against SLAs.\n4. Verify internal audit coverage of cloud.\n5. Check periodic review of cloud governance framework effectiveness.',
             'KPI/KRI definitions for cloud; Board/management reports; CSP SLA monitoring reports; Internal audit plan and reports; Governance framework review records', 'Inspection'),
            ('CLD-09', 'PLATFORM', 'Oversight', 'CSP due diligence and certifications',
             '1. Obtain due diligence reports for each in-scope CSP covering: financial viability, security capabilities, regulatory compliance, data residency, subcontracting, BCP.\n2. Obtain current SOC 2 Type II, ISO 27001, CSA STAR reports per CSP.\n3. Verify reports cover services used by the FI.\n4. Review exceptions or deficiencies in reports.\n5. Verify CUECs identified in SOC reports are implemented.\n6. Verify due diligence refreshed at least annually.',
             'Due diligence reports per CSP; SOC 2 Type II reports; ISO 27001 certificates; CSA STAR reports; FI review of findings; CUEC implementation evidence', 'Inspection'),
            ('CLD-10', 'PLATFORM', 'Oversight', 'CSP contract management',
             '1. Review contracts with each in-scope CSP.\n2. Check for: right to audit, data ownership/portability, data residency, breach notification, subcontracting controls, termination/exit provisions, BNM inspection access.\n3. Verify contracts reviewed by legal and compliance.\n4. Check ongoing CSP performance monitoring against SLAs.\n5. Verify periodic service review meetings held.',
             'CSP contracts; Legal/compliance review records; Contract compliance checklist; SLA performance reports; Service review meeting minutes', 'Inspection'),
        ]),
    ]

    for section_data in part_a:
        title, context, tests = section_data
        write_section_row(ws, r, title)
        r += 1
        if context:
            write_context_row(ws, r, context)
            r += 1
        for t in tests:
            write_test_row(ws, r, *t)
            r += 1

    # Part B — Design & Controls
    ws = wb.create_sheet(title='App 10 Part B - Controls')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    part_b = [
        ('B1 — Architecture Design',
         'Cloud architecture must support resilience and security. Expect multi-AZ for critical workloads, well-architected review, proper network segmentation. Poor architecture creates systemic risk.',
         [
            ('CLD-11', 'PLATFORM', 'Architecture', 'Cloud architecture design',
             '1. Obtain cloud architecture design documents and diagrams.\n2. Verify multi-AZ or multi-region deployment for critical workloads.\n3. Check architecture follows well-architected framework principles.\n4. Verify network architecture (VPC/VNET design, subnet segmentation, security groups, NACLs).\n5. Confirm architecture reviewed by qualified cloud architects.\n6. Verify landing zone / account structure design.',
             'Cloud architecture docs; Multi-AZ/region deployment evidence; Well-architected review; VPC/VNET design; Landing zone documentation', 'Inspection'),
        ]),
        ('B2 — Identity and Access Management',
         'Identity is the primary control plane in cloud. Expect MFA enforced, least-privilege policies, service account management, break-glass procedures. Weak IAM is the most common cloud compromise vector.',
         [
            ('CLD-12', 'PLATFORM', 'Cloud IAM', 'Identity and access management',
             '1. Review cloud IAM architecture (identity federation, SSO, MFA).\n2. Verify MFA enforced for all cloud console and API access.\n3. Check least privilege — review IAM policies for overly permissive roles.\n4. Verify privileged/admin access limited, separately managed, monitored.\n5. Verify service accounts and API keys managed with rotation.\n6. Check for unused/stale IAM accounts and access keys.\n7. Review break-glass / emergency access procedures.',
             'IAM architecture; MFA enforcement config; IAM policy review; Privileged access inventory; Service account inventory; Stale account report; Break-glass procedures', 'Inspection'),
        ]),
        ('B3 — Data Protection',
         'Data classification and encryption are foundational. Expect classification tagging, encryption at rest/transit, key management strategy, DLP controls. Unprotected data in cloud is a regulatory breach.',
         [
            ('CLD-13', 'ORG', 'Data Protection', 'Data classification for cloud',
             '1. Obtain the FI\'s data classification scheme as applied to cloud resources.\n2. Verify classification tags are applied to cloud resources (storage, databases, compute).\n3. Check that handling requirements are defined per classification level.\n4. Verify controls are proportionate to classification.',
             'Data classification scheme; Cloud resource tagging evidence; Handling requirements per level; Classification compliance reports', 'Inspection'),
            ('CLD-14', 'PLATFORM', 'Data Protection', 'Encryption and key management',
             '1. Review cloud encryption and key management strategy.\n2. Identify key ownership model (CSP-managed, CMK, BYOK).\n3. Verify encryption at rest for all data stores.\n4. Verify encryption in transit (TLS 1.2+) for all endpoints.\n5. For CMK: verify key rotation schedule and access controls.\n6. Verify DLP policies cover exfiltration detection, storage exposure, sharing controls.\n7. Verify public access to cloud storage explicitly blocked.',
             'Encryption/key management policy; Key management config; Encryption-at-rest per data store; TLS config; DLP policy config; Cloud storage public access settings', 'Inspection'),
        ]),
        ('B4 — Network Security',
         'Cloud network controls replace traditional perimeter security. Expect VPC segmentation, WAF, DDoS protection, private connectivity, flow logging. Misconfigured cloud networking exposes services to the internet.',
         [
            ('CLD-15', 'PLATFORM', 'Network Security', 'Virtual network design and segmentation',
             '1. Review VPC/VNet architecture and segmentation.\n2. Verify security groups / network ACLs follow least-privilege.\n3. Check private connectivity to cloud (Direct Connect, ExpressRoute, Interconnect).\n4. Verify WAF deployed for internet-facing applications.\n5. Verify DDoS protection enabled (L3/L4 and L7).\n6. Check network flow logging enabled.\n7. Verify API gateway security configuration.',
             'VPC/VNet architecture diagrams; Security group configs; Private connectivity architecture; WAF rules; DDoS protection config; Network flow log config; API gateway config', 'Inspection'),
        ]),
        ('B5 — Compute Security',
         'All compute resources must be hardened and patched. Expect hardening standards, container scanning, serverless permission controls, endpoint protection. Unpatched compute is the primary attack surface.',
         [
            ('CLD-16', 'PLATFORM', 'Compute Security', 'VM, container, and serverless security',
             '1. Obtain VM/instance hardening standards and verify compliance.\n2. Verify container images from approved registries and scanned for vulnerabilities.\n3. Check containers run least-privilege (non-root, read-only FS).\n4. Verify pod/container network policies enforce segmentation.\n5. Check orchestrator hardened per CIS benchmarks.\n6. Review serverless function permissions and secrets management.\n7. Verify anti-malware / endpoint protection for cloud instances.\n8. Check patch management for cloud compute resources.',
             'Hardening standards and compliance reports; Container image scanning reports; Runtime security config; Network policies; CIS benchmark reports; Serverless function permissions; Anti-malware deployment; Patch management reports', 'Inspection'),
        ]),
        ('B6 — Storage Security',
         'Cloud storage misconfigurations are a leading cause of data breaches. Expect public access blocked by default, access logging, lifecycle management. A single misconfigured bucket can expose all customer data.',
         [
            ('CLD-17', 'PLATFORM', 'Storage Security', 'Cloud storage controls',
             '1. Review storage bucket/blob/object access policies.\n2. Verify public access blocked by default (public access block enabled).\n3. Check access logging enabled for storage services.\n4. Verify encryption configuration for all storage types.\n5. Review lifecycle management policies (retention, deletion).\n6. Check versioning and deletion protection for critical data.\n7. Verify cross-region replication security.',
             'Storage access policy configs; Public access block settings; Access logging config; Encryption settings; Lifecycle policies; Versioning/deletion protection; Cross-region replication config', 'Inspection'),
        ]),
        ('B7 — Logging and Monitoring',
         'Visibility into cloud activity is essential for detection and response. Expect cloud-native logging enabled, SIEM integration, CSPM deployed. Without logging, breaches go undetected.',
         [
            ('CLD-18', 'PLATFORM', 'Logging & Monitoring', 'Cloud security monitoring',
             '1. Verify cloud-native audit logging enabled (CloudTrail, Activity Log, etc.).\n2. Confirm centralised log aggregation (SIEM integration).\n3. Check alert rules for security-relevant events.\n4. Verify log retention aligned with regulatory requirements.\n5. Check CSPM deployed to detect misconfigurations.\n6. Review CSPM findings and remediation status.\n7. Verify cost monitoring and anomaly detection.',
             'Cloud audit log config; SIEM integration; Alert rule configs; Log retention policies; CSPM config and findings; Cost monitoring dashboards', 'Inspection'),
        ]),
        ('B8 — Vulnerability Management',
         'Cloud resources must be scanned and patched systematically. Expect vulnerability scanning, patching SLAs, cloud-specific pen testing. Unmanaged vulnerabilities are exploitable at scale.',
         [
            ('CLD-19', 'PLATFORM', 'Vulnerability Management', 'Cloud vulnerability scanning and patching',
             '1. Verify cloud resource vulnerability scanning (instances, containers, serverless).\n2. Check CSP-native security posture management tools deployed.\n3. Review patching SLAs and compliance rates for cloud resources.\n4. Obtain most recent cloud environment penetration test report.\n5. Verify pen testing complies with CSP policies.\n6. Check remediation tracking and SLA adherence.',
             'Vulnerability scanning tool config and reports; Security posture management dashboards; Patching compliance reports; Cloud pen test report; Remediation tracker', 'Inspection'),
        ]),
        ('B9 — Change Management',
         'Infrastructure as Code and CI/CD must be governed. Expect version control, security gates, drift detection, approval workflows. Uncontrolled changes introduce misconfigurations.',
         [
            ('CLD-20', 'PLATFORM', 'Change Management', 'CI/CD and IaC governance',
             '1. Review CI/CD pipeline architecture and security gates (SAST, DAST, SCA, container scanning).\n2. Verify production deployment requires approval.\n3. Check pipeline config is version-controlled and access-restricted.\n4. Verify secrets not hardcoded.\n5. Review IaC governance (code review, version control, approval).\n6. Check IaC templates scanned for misconfigurations.\n7. Verify configuration drift detection.\n8. Confirm IaC state files stored securely.',
             'CI/CD architecture; Security gate config; Approval workflow; Pipeline access controls; IaC repository; IaC scanning tool; Drift detection; State file storage', 'Inspection'),
            ('CLD-21', 'PLATFORM', 'Change Management', 'Cloud infrastructure change controls',
             '1. Review cloud change management procedure.\n2. Sample 10 recent cloud changes.\n3. Verify each has: request, risk assessment, approval, implementation, post-implementation review.\n4. Check security-critical changes (IAM, network, encryption) have enhanced approval.\n5. Verify rollback capability and procedures.\n6. Check emergency change procedures.',
             'Change management procedure; 10 sampled change records; Enhanced approval evidence; Rollback procedure; Emergency change records', 'Inspection'),
        ]),
        ('B10 — Incident Response',
         'Cloud incidents require adapted IR procedures. Expect cloud-specific playbooks, CSP coordination, forensic capability, SOC coverage. Standard IR procedures may not address cloud-specific scenarios.',
         [
            ('CLD-22', 'PLATFORM', 'Incident Response', 'Cloud incident response and forensics',
             '1. Review IR plan for cloud-specific scenarios (account compromise, data breach, CSP outage, ransomware).\n2. Verify procedures account for shared responsibility model.\n3. Check CSP escalation contacts documented.\n4. Verify forensic capability in cloud (snapshot, log preservation, evidence collection).\n5. Check IR exercises include cloud scenarios.\n6. Verify SOC coverage extends to cloud events with cloud-specific detection rules.',
             'Cloud IR procedures; CSP escalation contacts; Forensic procedures; IR exercise records; SIEM cloud log sources; Cloud detection rules; SOC analyst skill assessment', 'Inspection / Inquiry'),
        ]),
        ('B11 — Business Continuity',
         'Cloud DR must be tested, not assumed. Expect multi-AZ deployment, tested failover, defined RTO/RPO per workload. Cloud availability is not a substitute for tested DR.',
         [
            ('CLD-23', 'WORKLOAD', 'Business Continuity', 'Cloud DR and availability',
             '1. Verify multi-AZ/multi-region deployment for each critical workload.\n2. Review backup strategy and cross-region replication config.\n3. Verify backup encryption and restore testing within 12 months.\n4. Verify RTO/RPO defined and validated for cloud-hosted critical systems.\n5. Check cloud DR/failover tested (cross-region failover).\n6. Review CSP outage response procedures.\n7. Verify backup monitoring — failed backups detected.',
             'Multi-AZ/region deployment evidence; Backup config and replication; Restore test results; RTO/RPO definitions; DR/failover test results; CSP outage procedures; Backup monitoring config', 'Inspection'),
        ]),
        ('B12 — Vendor Management',
         'CSP oversight is ongoing, not one-time. Expect due diligence, SLA monitoring, shared responsibility mapping, concentration risk assessment. Over-reliance on CSP assurances without independent verification is a risk.',
         [
            ('CLD-24', 'PLATFORM', 'Vendor Management', 'CSP assessment and oversight',
             '1. Review CSP assessment documentation (financial stability, security, compliance).\n2. Verify shared responsibility model documented and understood.\n3. Check SLA monitoring (availability, performance, support response).\n4. Review CSP risk profile assessment.\n5. Check sub-processor management (CSP third parties).\n6. Assess concentration risk — dependency on single/limited CSPs.',
             'CSP assessment docs; Shared responsibility mapping; SLA monitoring reports; CSP risk assessment; Sub-processor review; Concentration risk assessment', 'Inspection'),
        ]),
        ('B13 — Exit Strategy',
         'Vendor lock-in is a strategic risk. Expect documented exit strategy, tested data portability, contractual exit provisions. Without exit planning, the FI is captive to the CSP.',
         [
            ('CLD-25', 'PLATFORM', 'Exit Strategy', 'Cloud exit and portability',
             '1. Obtain exit strategy for each critical CSP engagement.\n2. Verify it covers: trigger events, data retrieval, migration approach, timeline, resources, communication plan.\n3. Check exit strategy reviewed within 12 months.\n4. Verify contractual terms support exit.\n5. Verify data can be exported in standard formats.\n6. Check migration feasibility assessed and tested.\n7. Review cost estimates for exit scenarios.',
             'Exit strategy document; Contractual exit provisions; Data export format docs; Migration feasibility assessment; Export/migration test results; Cost estimates', 'Inspection'),
        ]),
        ('B14 — Regulatory Compliance',
         'BNM access rights and data residency are enforceable requirements. Expect verified region controls, tested audit access, PDPA compliance. Non-compliance is a regulatory breach.',
         [
            ('CLD-26', 'WORKLOAD', 'Regulatory Compliance', 'Data residency and regulatory access',
             '1. Map each cloud service/data store to hosting region.\n2. Verify restricted data resides only in approved regions.\n3. Check CSP configs prevent replication to non-approved regions.\n4. Verify BNM approval obtained for data outside Malaysia (if required).\n5. Verify BNM access rights preserved (contractual and technical).\n6. Confirm audit access rights tested (not just contractual).\n7. Check regulatory reporting capabilities maintained from cloud.\n8. Verify PDPA compliance for cloud.',
             'Data residency mapping; CSP region config; BNM approval records; BNM access provisions; Audit access test evidence; Regulatory reporting capability; PDPA compliance docs', 'Inspection'),
        ]),
        ('Supplementary — Security Baseline',
         'A consistent security baseline prevents configuration drift. Expect CIS Benchmark alignment and automated compliance checking. Without a baseline, each workload\'s security posture varies.',
         [
            ('CLD-27', 'PLATFORM', 'Security Baseline', 'Cloud security baseline and hardening',
             '1. Obtain cloud security baseline/hardening standard.\n2. Verify alignment with CIS Cloud Benchmarks or equivalent.\n3. Run or review automated compliance checks.\n4. Check remediation status of non-compliant findings.',
             'Cloud security baseline; CIS Benchmark alignment; Automated compliance scan results; Remediation tracker', 'Inspection'),
        ]),
    ]

    for section_data in part_b:
        title, context, tests = section_data
        write_section_row(ws, r, title)
        r += 1
        if context:
            write_context_row(ws, r, context)
            r += 1
        for t in tests:
            write_test_row(ws, r, *t)
            r += 1


def create_cloud_workbook():
    scope_desc = (
        'This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Appendix 7 and Appendix 10. '
        'Where the cloud deployment involves emerging technology (AI/ML, DLT, IoT, etc.), the IESP-EmergingTech-WorkProgram.xlsx (Appendix 9) must also be used in conjunction with this workbook.'
    )
    scoping_note = 'Note: Where the cloud deployment involves emerging technology (AI/ML, DLT, IoT, etc.), the IESP-EmergingTech-WorkProgram.xlsx (Appendix 9) must also be used in conjunction with this workbook.'
    wb = build_workbook(
        'BNM RMiT IESP — Cloud Services Assessment',
        'Paragraph 17.1 / Appendix 7, mapped to Appendix 10',
        scope_desc,
        'Assessment covers: (1) Appendix 10 Part A — Cloud Governance (7 areas), (2) Appendix 10 Part B — Cloud Design and Control (14 areas), (3) Appendix 7 Part D — Minimum Controls.',
        'Cloud IESP Assessment (Pre-Implementation or Independent Attestation)',
        add_cloud_sheets,
        scoping_note=scoping_note)
    wb.save('audit-work-programs/IESP-Cloud-WorkProgram.xlsx')
    print('Created IESP-Cloud-WorkProgram.xlsx')


# ── EMERGING TECH AWP ───────────────────────────────────────────────
def add_emerging_tech_sheets(wb):
    ws = wb.create_sheet(title='Appendix 9 - Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    sections = [
        ('Domain 1 — Governance Arrangements',
         'BNM expects board-level approval and oversight for emerging technology adoption. Assessor should find a governance framework with clear accountability, ethical principles, and a technology radar. Without governance, emerging tech adoption is uncontrolled.',
         [
            ('AI-01', 'ORG', 'Governance', 'Governance framework',
             '1. Obtain the FI\'s AI/emerging tech governance framework.\n2. Verify it defines accountability, decision rights, risk management, ethical principles, oversight.\n3. Check designated committee has oversight.\n4. Verify framework approved at board/senior management level.',
             'AI governance framework; Committee ToR; Board/senior management approval records', 'Inspection'),
            ('AI-02', 'ORG', 'Governance', 'Roles and responsibilities',
             '1. Review organisational structure for AI/emerging tech.\n2. Verify defined roles: model owner, developer, validator, risk manager, compliance officer.\n3. Check each deployed model/technology has an accountable owner.\n4. Verify sufficient expertise exists.',
             'Org chart (AI function); Role descriptions; Model ownership register; Skills inventory', 'Inspection / Inquiry'),
            ('AI-03', 'ORG', 'Governance', 'Technology radar and innovation governance',
             '1. Check whether the FI maintains a technology radar or equivalent mechanism.\n2. Verify it tracks emerging technologies and assesses maturity and applicability.\n3. Review the innovation governance process (sandbox/PoC governance).\n4. Check formal evaluation and approval process exists for new technology initiatives.',
             'Technology radar; Innovation governance policy; PoC/sandbox evaluation records; Technology evaluation board minutes', 'Inspection'),
        ]),
        ('Domain 2 — Risk Assessment and Tolerance',
         'Technology-specific risk assessment is required. Expect risk assessments covering model risk, data risk, bias, explainability, concentration, and obsolescence. Generic risk assessments miss technology-specific threats.',
         [
            ('AI-04', 'WORKLOAD', 'Risk Assessment', 'Technology-specific risk assessment',
             '1. Obtain risk assessment methodology for AI/emerging tech.\n2. For each in-scope deployment, verify risk assessment covers: model risk, data risk, bias/fairness, explainability, operational, regulatory.\n3. Verify assessments proportionate to risk tier.\n4. Check residual risks within approved tolerance.',
             'Risk assessment methodology; Completed risk assessments; Risk tolerance thresholds; Residual risk acceptance records', 'Inspection'),
            ('AI-05', 'WORKLOAD', 'Risk Assessment', 'Bias and fairness assessment',
             '1. Identify AI models making/supporting customer decisions.\n2. Verify bias and fairness testing performed per model.\n3. Check protected attributes assessed for disparate impact.\n4. Verify ongoing monitoring for bias drift.',
             'Bias testing methodology; Bias test results per model; Disparate impact analysis; Ongoing monitoring config', 'Inspection'),
            ('AI-06', 'ORG', 'Risk Assessment', 'Concentration and obsolescence risk',
             '1. Assess whether the FI depends on a single provider, model, or technology.\n2. Verify concentration risk formally assessed.\n3. Check technology obsolescence risk considered given rapid evolution.\n4. Verify alternative provider/model identification.\n5. Review integration risk assessment for existing systems.',
             'Concentration risk assessment; Technology lifecycle assessment; Alternative provider analysis; Integration risk assessment', 'Inspection'),
        ]),
        ('Domain 3 — Acceptance Criteria',
         'Production deployment must meet formal acceptance criteria. Expect defined performance thresholds, security baselines, ethical review, and formal sign-off. Without acceptance criteria, untested technology reaches production.',
         [
            ('AI-07', 'ORG', 'Acceptance Criteria', 'Production deployment acceptance',
             '1. Obtain acceptance criteria framework.\n2. Verify criteria cover: performance thresholds, validation results, security assessment, ethical review, operational readiness, business sign-off.\n3. For each in-scope deployment, verify criteria met before production.\n4. Check acceptance formally documented and signed off.',
             'Acceptance criteria framework; Completed acceptance checklists; Sign-off records', 'Inspection'),
            ('AI-08', 'WORKLOAD', 'Acceptance Criteria', 'Ethical assessment',
             '1. Verify the FI has assessed the technology against ethical standards.\n2. Check fairness, non-discrimination, transparency, and accountability assessed.\n3. Verify ethical review is proportionate to the risk of the use case.\n4. Review pilot/sandbox results where applicable.\n5. Confirm regulatory compliance verified before deployment.',
             'Ethical assessment framework; Fairness assessment per deployment; Pilot/sandbox results; Regulatory compliance verification', 'Inspection'),
        ]),
        ('Domain 4 — Technology and Cybersecurity Controls',
         'Security controls must address technology-specific attack vectors. Expect access controls, data governance, model integrity, environment segmentation, adversarial protections. Standard security controls may not address AI/emerging tech threats.',
         [
            ('AI-09', 'PLATFORM', 'Security Controls', 'AI model and training data security',
             '1. Review access controls for model repositories, training data, inference endpoints.\n2. Verify training data classified, access-controlled, encrypted.\n3. Check model artefacts version-controlled and integrity-protected.\n4. Verify dev environments segmented from production.\n5. Assess protections against adversarial attacks.',
             'Access control configs; Data classification and encryption; Model version control; Environment segmentation; Adversarial mitigation measures', 'Inspection'),
            ('AI-10', 'WORKLOAD', 'Data Governance', 'Data quality and governance for AI',
             '1. Review data governance framework for AI training/inference data.\n2. Verify data quality controls: completeness, accuracy, timeliness, consistency.\n3. Check data lineage tracked from source to model input.\n4. Verify privacy requirements met (anonymisation, consent, purpose limitation).\n5. Check training data is representative and sufficient.',
             'Data governance framework; Data quality procedures and metrics; Data lineage docs; Privacy compliance evidence; Training data representativeness assessment', 'Inspection'),
        ]),
        ('Domain 5 — Production Environment Prerequisites',
         'Production readiness requires comprehensive testing, monitoring, human oversight, and kill-switch capability. Without these, the FI cannot respond to model failure or harmful outputs.',
         [
            ('AI-11', 'WORKLOAD', 'Model Monitoring', 'Production model performance',
             '1. Identify all models in production.\n2. Verify each has defined performance metrics.\n3. Check performance monitored continuously or at intervals.\n4. Verify degradation triggers alerts and investigation.\n5. Confirm retraining/recalibration procedures exist.',
             'Production model inventory; Performance metrics per model; Monitoring config; Alert config; Retraining procedures', 'Inspection'),
            ('AI-12', 'WORKLOAD', 'Model Validation', 'Independent model validation',
             '1. Check validation performed independently of development.\n2. Review methodology: conceptual soundness, data adequacy, benchmarking, sensitivity, stress testing.\n3. Verify validation before deployment and periodically.\n4. Check findings tracked and remediated.',
             'Model validation policy; Independence evidence; Validation reports; Finding tracker', 'Inspection'),
            ('AI-13', 'WORKLOAD', 'Testing', 'Pre-production testing',
             '1. Review testing strategy.\n2. Verify: unit, integration, performance, security, UAT, A/B or shadow testing.\n3. Verify test execution records and results.\n4. Confirm exit criteria met before release.',
             'Testing strategy; Test plans and records; Test results; Production release approval', 'Inspection'),
            ('AI-14', 'ORG', 'Regulatory', 'Standards and regulations compliance',
             '1. Identify applicable regulations (BNM, PDPA, sector-specific).\n2. Verify each deployment assessed for compliance.\n3. Check regulatory notifications/approvals obtained.\n4. Verify ongoing compliance monitoring.',
             'Regulatory requirements register; Compliance assessment per deployment; Notification/approval records; Monitoring procedures', 'Inspection'),
            ('AI-15', 'WORKLOAD', 'Kill Switch', 'Suspension and decommissioning',
             '1. Check each production AI system has kill-switch capability.\n2. Verify activation within defined timeframes.\n3. Review suspension testing evidence.\n4. Verify fallback/manual processes exist.\n5. Confirm decision authority defined.',
             'Kill-switch documentation; Suspension test results; Fallback process docs; Decision authority matrix', 'Inspection'),
            ('AI-16', 'WORKLOAD', 'Human Oversight', 'Ongoing monitoring and oversight',
             '1. Verify human oversight levels defined and proportionate to risk.\n2. Check automated decisions can be overridden.\n3. Verify outcome tracking for unintended consequences.\n4. Confirm escalation procedures for anomalous behaviour.',
             'Human oversight framework; Override capability evidence; Outcome monitoring; Escalation procedures', 'Inspection'),
            ('AI-17', 'WORKLOAD', 'Transparency', 'Transparency and disclosure',
             '1. Identify AI systems interacting with customers.\n2. Verify customers informed of AI use in decision-making.\n3. Check explanations can be provided (explainability).\n4. Verify complaints/appeals process exists.\n5. Review sample disclosures.',
             'Disclosure policy; Customer notification evidence; Explainability mechanism; Complaints process; Sample disclosures', 'Inspection'),
            ('AI-18', 'ORG', 'AI Incident Management', 'AI-specific incident management',
             '1. Review IR procedure for AI incidents (model failure, biased outcomes, data poisoning, adversarial attacks).\n2. Verify AI incident categories and severity levels defined.\n3. Check incident log for past 12 months.\n4. Verify lessons learned fed back into governance.',
             'AI incident management procedure; AI incident categories; AI incident log; Lessons learned register', 'Inspection'),
        ]),
    ]

    for section_data in sections:
        title, context, tests = section_data
        write_section_row(ws, r, title)
        r += 1
        if context:
            write_context_row(ws, r, context)
            r += 1
        for t in tests:
            write_test_row(ws, r, *t)
            r += 1


def create_emerging_tech_workbook():
    scope_desc = (
        'This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Appendix 7 and Appendix 9. '
        'Where emerging technology is deployed on cloud infrastructure, the IESP-Cloud-WorkProgram.xlsx (Appendix 10) must also be used in conjunction with this workbook.'
    )
    scoping_note = 'Note: Where emerging technology is deployed on cloud infrastructure, the IESP-Cloud-WorkProgram.xlsx (Appendix 10) must also be used in conjunction with this workbook.'
    wb = build_workbook(
        'BNM RMiT IESP — Emerging Technology Assessment',
        'Paragraph 17.1 / Appendix 7, mapped to Appendix 9',
        scope_desc,
        'Assessment covers: (1) Appendix 9 — Emerging Technology (5 domains), (2) Appendix 7 Part D — Minimum Controls.',
        'Emerging Technology IESP Assessment (Pre-Implementation or Independent Attestation)',
        add_emerging_tech_sheets,
        scoping_note=scoping_note)
    wb.save('audit-work-programs/IESP-EmergingTech-WorkProgram.xlsx')
    print('Created IESP-EmergingTech-WorkProgram.xlsx')


# ── DIGITAL SERVICES AWP ───────────────────────────────────────────
def add_digital_services_sheets(wb):
    ws = wb.create_sheet(title='Digital Services Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    sections = [
        ('Domain 1 — Access Control (Part D 1a + 2a-c)',
         'Customer-facing authentication is a primary defence against fraud and account takeover. Expect MFA, secure session management, brute-force protection. Weak authentication directly impacts customers.',
         [
            ('DS-01', 'WORKLOAD', 'Access Control', 'Customer authentication',
             '1. Review authentication mechanisms (password, OTP, biometric, device binding).\n2. Verify MFA enforced for login and high-risk transactions.\n3. Check credential policy: complexity, history, expiry, lockout.\n4. Verify session tokens securely managed.',
             'Authentication design; MFA config; Credential policy; Session management config', 'Inspection'),
            ('DS-02', 'WORKLOAD', 'Access Control', 'Digital identity verification (eKYC)',
             '1. Review eKYC process.\n2. Verify identity document validation (OCR, NFC, database).\n3. Check liveness detection.\n4. Verify results logged and auditable.\n5. Assess fraud detection controls during onboarding.',
             'eKYC process flow; Identity verification config; Liveness detection; Audit logs; Fraud detection rules', 'Inspection'),
            ('DS-03', 'WORKLOAD', 'Access Control', 'Authorisation and RBAC',
             '1. Review authorisation model (RBAC, ABAC).\n2. Verify access based on role/entitlements.\n3. Check privilege escalation prevented.\n4. Verify API authorisation.\n5. Test for IDOR.',
             'Authorisation model; Role-to-function mapping; API auth config; Pen test results (IDOR)', 'Inspection'),
            ('DS-04', 'WORKLOAD', 'Access Control', 'Session management',
             '1. Review session management.\n2. Verify tokens cryptographically random.\n3. Check idle and absolute timeouts.\n4. Verify session invalidated on logout/password change.\n5. Check concurrent session controls.',
             'Session management config; Token generation; Timeout settings; Concurrent session policy', 'Inspection'),
            ('DS-05', 'WORKLOAD', 'Access Control', 'Account lockout and brute-force protection',
             '1. Review lockout policy.\n2. Verify rate limiting.\n3. Check CAPTCHA/bot protection.\n4. Verify lockout notifications.\n5. Test bypass resistance.',
             'Lockout config; Rate limiting config; CAPTCHA/bot protection; Notification config; Bypass test results', 'Inspection'),
        ]),
        ('Domain 2 — Online Transaction Security (Part D 2)',
         'Transaction integrity and fraud monitoring protect customer funds. Expect step-up authentication, transaction binding, fraud monitoring rules, encryption. Transaction fraud is a direct financial and reputational impact.',
         [
            ('DS-06', 'WORKLOAD', 'Transaction Security', 'Transaction authentication',
             '1. Review transaction authentication (signing, OTP, biometric, TAC).\n2. Verify step-up for high-risk transactions.\n3. Check confirmation presented before execution.\n4. Verify authentication bound to specific transaction.\n5. Assess MITM/MITB protections.',
             'Transaction auth design; Step-up config; Confirmation flow; Transaction binding; MitM protections', 'Inspection'),
            ('DS-07', 'WORKLOAD', 'Transaction Security', 'Transaction limits and fraud monitoring',
             '1. Obtain transaction limits.\n2. Verify enforced at application and backend.\n3. Review fraud monitoring rules.\n4. Check suspicious transactions trigger alerts/blocks.\n5. Verify customer limit management.',
             'Transaction limit config; Fraud monitoring rules; Sample fraud alerts; Customer limit management', 'Inspection'),
            ('DS-08', 'WORKLOAD', 'Transaction Security', 'End-to-end encryption',
             '1. Verify TLS 1.2+ enforced.\n2. Check certificate config (valid, HSTS).\n3. Verify no sensitive data in URLs/logs.\n4. Check certificate pinning for mobile.\n5. Verify mTLS for B2B.',
             'TLS config (SSL Labs); Certificate details; HSTS config; Log review; Cert pinning config; mTLS config', 'Inspection'),
            ('DS-09', 'WORKLOAD', 'Transaction Security', 'Secure API design',
             '1. Review API design against OWASP API Top 10.\n2. Verify API auth (OAuth 2.0, API keys, mTLS).\n3. Check rate limiting.\n4. Verify input validation and output encoding.\n5. Check API versioning.\n6. Review API gateway config.',
             'API documentation; OWASP assessment; API auth config; Rate limiting; API gateway config', 'Inspection'),
            ('DS-10', 'WORKLOAD', 'Transaction Security', 'Non-repudiation',
             '1. Identify critical transaction types.\n2. Verify records capture who, what, when, where, how authenticated.\n3. Check records tamper-proof.\n4. Verify audit trail retention.',
             'Non-repudiation design; Transaction record format; Tamper-proofing mechanism; Retention config', 'Inspection'),
        ]),
        ('Domain 3 — Mobile Device Security (Part D 2e)',
         'Mobile applications extend the attack surface to customer devices. Expect root detection, secure storage, RASP, certificate pinning. Mobile apps are exposed to reverse engineering and tampering.',
         [
            ('DS-11', 'WORKLOAD', 'Mobile Security', 'Mobile app security controls',
             '1. Review mobile security architecture.\n2. Verify root/jailbreak detection.\n3. Check no plaintext sensitive data on device.\n4. Verify code obfuscation and anti-tampering.\n5. Check no data leakage in logs/screenshots/clipboard.',
             'Mobile security architecture; Root/jailbreak detection; Data storage review; Obfuscation evidence; Leakage assessment', 'Inspection'),
            ('DS-12', 'WORKLOAD', 'Mobile Security', 'App distribution and updates',
             '1. Verify official app store only.\n2. Check forced updates for critical patches.\n3. Verify app signing and integrity.\n4. Check push notifications don\'t include sensitive data.\n5. Review MDM/MAM requirements.',
             'App store distribution; Minimum version enforcement; App signing config; Push notification policy; MDM/MAM policy', 'Inspection'),
            ('DS-13', 'WORKLOAD', 'Mobile Security', 'Mobile threat protections',
             '1. Check for RASP.\n2. Verify anti-debugging, emulator, hooking framework detection.\n3. Check proxy/MitM detection.\n4. Verify device binding.',
             'RASP config; Anti-debugging/emulator detection; Proxy detection; Device binding mechanism', 'Inspection'),
        ]),
        ('Domain 4 — Data Integrity (Part D 2d)',
         'Input validation and anti-replay controls prevent data manipulation. Expect server-side validation, injection testing, integrity controls. Data integrity failures can lead to financial loss.',
         [
            ('DS-14', 'WORKLOAD', 'Data Integrity', 'Input validation',
             '1. Review server-side input validation.\n2. Verify: data type, length, range, format validation.\n3. Test for injection attacks (SQL, XSS, command, LDAP).\n4. Verify output encoding.\n5. Check file upload validation.',
             'Input validation design; Server-side validation config; Pen test results (injection); Output encoding; File upload config', 'Inspection'),
            ('DS-15', 'WORKLOAD', 'Data Integrity', 'Processing and storage integrity',
             '1. Review integrity controls in processing chain.\n2. Verify checksums/hash verification between components.\n3. Check database integrity controls.\n4. Verify reconciliation with core systems.\n5. Confirm integrity violation alerts.',
             'Integrity control design; Checksum implementation; Database integrity config; Reconciliation procedures; Alert config', 'Inspection'),
            ('DS-16', 'WORKLOAD', 'Data Integrity', 'Replay and manipulation protection',
             '1. Verify anti-replay mechanisms (nonce, timestamp, sequence).\n2. Check transaction integrity in transit.\n3. Verify duplicate detection.\n4. Test for parameter tampering.',
             'Anti-replay mechanism; Transit integrity protection; Duplicate detection config; Parameter tampering test results', 'Inspection'),
        ]),
        ('Supplementary — Application Security Testing',
         'Comprehensive security testing before launch is the last gate. Expect SAST, DAST, pen testing, SSDLC, privacy assessment. Launching without testing exposes customers to known vulnerabilities.',
         [
            ('DS-17', 'WORKLOAD', 'App Security', 'Comprehensive security testing',
             '1. Obtain testing scope and plan.\n2. Verify: SAST, DAST, pen testing, API security testing, infrastructure VA.\n3. Review results and severity distribution.\n4. Verify high/critical findings remediated before launch.\n5. Confirm qualified testers.',
             'Security testing plan; SAST/DAST/pen test/API/VA reports; Remediation evidence; Tester qualifications', 'Inspection'),
            ('DS-18', 'ORG', 'App Security', 'Secure SDLC',
             '1. Review SSDLC.\n2. Verify security requirements at design phase.\n3. Check threat modelling performed.\n4. Verify secure coding standards enforced.\n5. Confirm security sign-off before release.',
             'SSDLC documentation; Security requirements; Threat model; Secure coding standards; Security sign-off records', 'Inspection'),
            ('DS-19', 'WORKLOAD', 'Privacy', 'Privacy and data protection',
             '1. Review PIA for the digital service.\n2. Verify data minimisation.\n3. Check consent mechanisms.\n4. Verify retention/deletion policies.\n5. Confirm privacy notices clear.',
             'PIA; Data collection inventory; Consent mechanism; Retention/deletion config; Privacy notice review', 'Inspection'),
            ('DS-20', 'WORKLOAD', 'Availability', 'Business continuity and availability',
             '1. Review availability targets.\n2. Verify HA architecture.\n3. Check monitoring and alerting.\n4. Verify DR plan covers the service.\n5. Review most recent DR test.',
             'Availability targets; HA architecture; Monitoring config; DR plan; DR test results', 'Inspection'),
        ]),
    ]

    for section_data in sections:
        title, context, tests = section_data
        write_section_row(ws, r, title)
        r += 1
        if context:
            write_context_row(ws, r, context)
            r += 1
        for t in tests:
            write_test_row(ws, r, *t)
            r += 1


def create_digital_services_workbook():
    wb = build_workbook(
        'BNM RMiT IESP — Digital Services Enhancement Assessment',
        'Paragraphs 16.4, 16.5 / Appendix 7 Part D',
        'This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Paragraphs 16.4 and 16.5.',
        'Assessment covers: (1) Digital Services Security Assessment, (2) Appendix 7 Part D — Minimum Controls.',
        'Digital Services Enhancement IESP Assessment (Pre-Launch)',
        add_digital_services_sheets)
    wb.save('audit-work-programs/IESP-DigitalServices-WorkProgram.xlsx')
    print('Created IESP-DigitalServices-WorkProgram.xlsx')


# ── DCRA AWP ────────────────────────────────────────────────────────
def add_dcra_sheets(wb):
    ws = wb.create_sheet(title='DCRA Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    sections = [
        ('Domain 1 — DC Resilience and Availability Objectives (10.24)',
         'DC resilience objectives must align with business recovery requirements. Expect quantified targets (availability %, RTO, RPO) approved by committee. Misaligned objectives mean the DC cannot support business recovery.',
         [
            ('DCRA-01', 'ORG', 'Resilience Objectives', 'Objectives alignment',
             '1. Obtain DC resilience strategy.\n2. Extract resilience targets (availability %, RTO, RPO).\n3. Compare against approved business recovery objectives.\n4. Check targets approved by appropriate committee.',
             'DC resilience strategy; Business recovery objectives matrix; Committee approval minutes', 'Inspection'),
            ('DCRA-02', 'ORG', 'Resilience Objectives', 'Periodic review',
             '1. Check version history.\n2. Confirm annual review or upon material change.\n3. Verify business requirement changes triggered updates.',
             'Document version history; Change log; Review sign-off records', 'Inspection'),
        ]),
        ('Domain 2 — Redundancy and Single Points of Failure (10.25)',
         'Critical infrastructure must have no single points of failure. Expect N+1 or 2N redundancy, diverse paths, tested failover. A single failure in power, cooling, or network can cause a DC outage.',
         [
            ('DCRA-03', 'PLATFORM', 'Redundancy', 'Redundant capacity',
             '1. Obtain redundancy design (N+1, 2N, 2N+1).\n2. For each critical layer (power, cooling, network), confirm redundancy.\n3. Verify actual capacity against design through site inspection.\n4. Check redundant capacity handles full load on failover.',
             'Redundancy design specs; Capacity planning reports; Site inspection photographs', 'Inspection / Observation'),
            ('DCRA-04', 'PLATFORM', 'Redundancy', 'Multiple distribution paths',
             '1. Review electrical single-line diagrams for dual feeds.\n2. Review network diagrams for diverse carrier paths.\n3. Confirm physical path diversity.\n4. Verify through site walk.',
             'Electrical single-line diagrams; Network path diversity docs; Site walk observations', 'Inspection / Observation'),
            ('DCRA-05', 'PLATFORM', 'Redundancy', 'SPOF analysis',
             '1. Obtain SPOF analysis per DC.\n2. Walk through each SPOF and confirm mitigations.\n3. Identify unrecognised SPOFs during independent walkthrough.\n4. Check SPOF analysis periodically refreshed.',
             'SPOF analysis/register; Mitigation action plans; Site walk findings', 'Inspection / Observation'),
            ('DCRA-06', 'PLATFORM', 'Redundancy', 'Failover testing',
             '1. Obtain failover test plans and results (UPS, generators, cooling, switches).\n2. Review test frequency (at least annual).\n3. Confirm tests simulate actual failure conditions.\n4. Check test failures remediated.',
             'Failover test plans; Test result reports; Corrective action records', 'Inspection'),
        ]),
        ('Domain 3 — Physical Security and Environmental Controls (10.26)',
         'Physical security protects against unauthorised access and environmental threats. Expect multi-layered access, environmental monitoring, fire suppression, hazard assessment. Physical compromise bypasses all logical controls.',
         [
            ('DCRA-07', 'PLATFORM', 'Physical Security', 'Dedicated space',
             '1. Confirm DC in dedicated space.\n2. Verify physical separation from public areas.\n3. Check walls extend true floor to true ceiling.',
             'Site inspection observations; Building layout plans; Lease/facility agreements', 'Observation'),
            ('DCRA-08', 'PLATFORM', 'Physical Security', 'Multi-layered access controls',
             '1. Walk access path from perimeter to rack.\n2. Verify independent controls at each layer.\n3. Test access mechanisms.\n4. Review provisioning/de-provisioning.\n5. Sample-check access list against HR for terminated staff.',
             'Physical security policy; Access control config; Access list vs HR reconciliation; Site walk observations', 'Inspection / Observation'),
            ('DCRA-09', 'PLATFORM', 'Physical Security', 'Disaster-prone location assessment',
             '1. Obtain site risk assessment (flood, earthquake, lightning).\n2. Cross-reference against hazard maps.\n3. Verify mitigations.\n4. Check assessment periodically updated.',
             'Site risk assessment; Hazard map cross-reference; Mitigation evidence', 'Inspection'),
            ('DCRA-10', 'PLATFORM', 'Environmental Controls', 'Electrical infrastructure',
             '1. Review UPS configuration (N+1 or 2N).\n2. Verify UPS runtime (min 15 min).\n3. Confirm generator auto-start and fuel autonomy (48-72 hrs).\n4. Check ATS operation and tests.\n5. Verify fuel replenishment contracts.',
             'UPS specs and test reports; Generator load test reports; ATS test records; Fuel supply contracts', 'Inspection / Observation'),
            ('DCRA-11', 'PLATFORM', 'Environmental Controls', 'Thermal management',
             '1. Review cooling design (N+1 min).\n2. Check cooling load vs capacity.\n3. Verify rack-level monitoring.\n4. Confirm alerting thresholds.\n5. Review hot/cold aisle containment.',
             'Cooling design docs; Capacity reports; Monitoring config; Alert thresholds', 'Inspection / Observation'),
            ('DCRA-12', 'PLATFORM', 'Environmental Controls', 'Fire suppression and monitoring',
             '1. Confirm VESDA or equivalent.\n2. Verify gas-based suppression with current inspections.\n3. Check water leak detection.\n4. Verify 24/7 monitoring and alerting.\n5. Review environmental incident response procedures.',
             'Fire suppression certificates; VESDA config; Water leak detection; Monitoring dashboard; Environmental IR procedures', 'Inspection / Observation'),
            ('DCRA-13', 'PLATFORM', 'Asset Management', 'Hardware lifecycle',
             '1. Obtain hardware asset register.\n2. Sample-check physical assets against register.\n3. Verify EOL/EOS hardware tracked with replacement plan.\n4. Check secure data destruction for decommissioned equipment.',
             'Hardware asset register; Physical verification; EOL/EOS tracker; Data destruction certificates', 'Inspection / Observation'),
        ]),
        ('Domain 4 — DC Operations and Control Procedures (10.27)',
         'Operational controls ensure stable, monitored DC operations. Expect automated monitoring, controlled changes, incident management with RCA. Uncontrolled operations lead to avoidable outages.',
         [
            ('DCRA-14', 'PLATFORM', 'DC Operations', 'Automated monitoring',
             '1. Obtain monitoring tool inventory (DCIM, BMS, network).\n2. Verify coverage of critical parameters.\n3. Test alerts for threshold breaches.\n4. Confirm NOC/SOC integration.',
             'Tool inventory; Monitoring coverage matrix; Sample alerts; NOC/SOC integration', 'Inspection'),
            ('DCRA-15', 'PLATFORM', 'DC Operations', 'Batch processing controls',
             '1. Obtain batch job procedures.\n2. Verify jobs have defined run windows, dependencies, error handling.\n3. Review failure logs (3 months).\n4. Check schedule changes controlled.',
             'Batch scheduling procedures; Job scheduler config; Failure logs; Change approval records', 'Inspection'),
            ('DCRA-16', 'PLATFORM', 'DC Operations', 'Change management',
             '1. Obtain DC change management procedure.\n2. Sample 10 infrastructure changes.\n3. Verify full lifecycle (request through post-impl review).\n4. Check emergency changes follow defined process.',
             'Change management procedure; 10 sampled change records; Emergency change records', 'Inspection'),
            ('DCRA-17', 'PLATFORM', 'DC Operations', 'Error and incident handling',
             '1. Obtain DC incident management procedure.\n2. Review incident log (6 months).\n3. Verify RCA for significant incidents.\n4. Check RCA findings led to preventive actions.',
             'Incident management procedure; Incident log (6 months); RCA reports; Preventive action tracker', 'Inspection'),
        ]),
        ('Domain 5 — Segregation of Incompatible Activities (10.28)',
         'Segregation prevents unauthorised changes and maintains environment integrity. Expect production isolation, controlled vendor access, SoD enforcement. Without segregation, a single actor can compromise production.',
         [
            ('DCRA-18', 'PLATFORM', 'Segregation', 'Vendor access controls',
             '1. Review vendor/third-party access policy.\n2. Check pre-approved access requests.\n3. Verify escort requirements.\n4. Sample-check vendor access logs.\n5. Confirm access revoked promptly.',
             'Vendor access policy; Access request forms; Escort logs; Access log reconciliation', 'Inspection'),
            ('DCRA-19', 'PLATFORM', 'Segregation', 'Production segregation',
             '1. Review logical and physical segregation (prod vs non-prod).\n2. Verify developers have no direct production access.\n3. Check network segmentation.\n4. Confirm non-prod data masked.',
             'Environment segregation architecture; Access control matrices; Network segmentation; Data masking procedures', 'Inspection'),
            ('DCRA-20', 'ORG', 'Segregation', 'Segregation of duties',
             '1. Obtain DC operations RACI.\n2. Verify incompatible duties separated.\n3. Check privileged access limited and monitored.\n4. Review privileged access usage logs (3 months).',
             'RACI matrix; Role definitions; Privileged access list; Privileged access usage logs', 'Inspection'),
        ]),
    ]

    for section_data in sections:
        title, context, tests = section_data
        write_section_row(ws, r, title)
        r += 1
        if context:
            write_context_row(ws, r, context)
            r += 1
        for t in tests:
            write_test_row(ws, r, *t)
            r += 1


def create_dcra_workbook():
    wb = build_workbook(
        'BNM RMiT IESP — Data Centre Resilience Assessment (DCRA)',
        'Paragraph 14.1, mapped to paragraphs 10.24 to 10.28',
        'This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Paragraph 14.1.',
        'Assessment covers: (1) DCRA — DC resilience, redundancy, physical security, operations, segregation (10.24-10.28), (2) Appendix 7 Part D — Minimum Controls.',
        'Data Centre Resilience Assessment (DCRA)',
        add_dcra_sheets)
    wb.save('audit-work-programs/IESP-DCRA-WorkProgram.xlsx')
    print('Created IESP-DCRA-WorkProgram.xlsx')


# ── NRA AWP ─────────────────────────────────────────────────────────
def add_nra_sheets(wb):
    ws = wb.create_sheet(title='NRA Assessment')
    apply_col_widths(ws)
    r = 1
    write_header_row(ws, r)
    r += 1

    sections = [
        ('Domain 1 — Network Design and Scalability (10.36)',
         'Network must be designed for current and future capacity. Expect documented capacity planning, scalability, performance SLAs. Under-capacity networks degrade service availability.',
         [
            ('NRA-01', 'ORG', 'Network Design', 'Capacity requirements',
             '1. Obtain capacity planning document.\n2. Review bandwidth utilisation across critical links.\n3. Verify 2-year growth projections.\n4. Check utilisation thresholds trigger augmentation.',
             'Capacity planning document; Bandwidth utilisation reports (12 months); Growth projection model', 'Inspection'),
            ('NRA-02', 'ORG', 'Network Design', 'Scalability',
             '1. Review architecture for modular/scalable design.\n2. Assess whether it can accommodate growth without redesign.\n3. Check technology currency — platforms within vendor support.',
             'Architecture design principles; Technology lifecycle tracker; Scalability assessment', 'Inspection'),
            ('NRA-03', 'PLATFORM', 'Network Design', 'Performance SLAs',
             '1. Obtain SLA definitions (latency, jitter, packet loss, availability).\n2. Verify monitoring tools.\n3. Review SLA performance (6 months).\n4. Check breaches trigger investigation.',
             'SLA definitions; Performance monitoring reports; SLA breach incident records', 'Inspection'),
        ]),
        ('Domain 2 — Network Resilience and Reliability (10.37, 10.38)',
         'Network redundancy and tested failover prevent outages. Expect diverse paths, HA pairs, tested failover, carrier diversity. Network outage impacts all services.',
         [
            ('NRA-04', 'PLATFORM', 'Network Resilience', 'Redundancy for critical paths',
             '1. Review topology for redundancy at each layer.\n2. Verify redundant paths (dual WAN, diverse carriers).\n3. Confirm redundant devices (HA pairs).\n4. Verify physical route diversity.',
             'Network topology with redundancy; Carrier diversity docs; HA configuration evidence', 'Inspection'),
            ('NRA-05', 'PLATFORM', 'Network Resilience', 'Failover testing',
             '1. Obtain failover test plan.\n2. Review most recent tests (WAN, internet, core switches, firewalls).\n3. Verify failover within acceptable times.\n4. Check failures remediated.\n5. Confirm realistic failure simulation.',
             'Failover test plans; Test execution reports; Remediation records', 'Inspection'),
            ('NRA-06', 'ORG', 'Network Resilience', 'Network DR',
             '1. Review network DR plan.\n2. Verify recovery procedures per critical segment.\n3. Check network DR tested in DR exercises.\n4. Confirm network RTO aligns with business requirements.',
             'Network DR plan; DR test results (network); RTO alignment mapping', 'Inspection'),
            ('NRA-07', 'PLATFORM', 'Network Resilience', 'Carrier/ISP management',
             '1. Review carrier contracts and SLAs.\n2. Verify at least two independent carriers.\n3. Check carrier performance against SLAs (12 months).\n4. Confirm escalation procedures.',
             'Carrier contracts; Carrier diversity mapping; Performance reports; Escalation contacts', 'Inspection'),
        ]),
        ('Domain 3 — Network Monitoring and Traffic Analysis (10.39)',
         'Network visibility enables performance management and threat detection. Expect comprehensive monitoring, flow analysis, anomaly detection, trend reporting. Unmonitored networks hide performance degradation and security threats.',
         [
            ('NRA-08', 'PLATFORM', 'Network Monitoring', 'Comprehensive monitoring',
             '1. Obtain monitoring tool inventory.\n2. Verify all critical devices/links monitored.\n3. Check parameter coverage (availability, performance, errors).\n4. Confirm 24/7 alerting to NOC.',
             'Monitoring tool inventory; Device coverage report; Parameter coverage matrix; NOC alerting config', 'Inspection'),
            ('NRA-09', 'PLATFORM', 'Network Monitoring', 'Traffic analysis and anomaly detection',
             '1. Confirm flow analysis tools deployed.\n2. Review traffic baselines and anomaly thresholds.\n3. Sample 5 anomaly alerts — verify investigation.\n4. Verify SIEM/SOC integration.',
             'Flow analysis config; Traffic baselines; Sample anomaly investigation; SIEM integration', 'Inspection'),
            ('NRA-10', 'ORG', 'Network Monitoring', 'Performance trend analysis',
             '1. Obtain regular performance reports.\n2. Verify trend analysis (utilisation, latency, availability).\n3. Check trends inform capacity planning.\n4. Confirm management review.',
             'Performance reports; Trend analysis dashboards; Management review records', 'Inspection'),
        ]),
        ('Domain 4 — Network Confidentiality, Integrity, Availability (10.40)',
         'Network confidentiality, integrity, and availability require layered controls. Expect encryption, NAC, device hardening, configuration integrity monitoring. Network compromise provides access to all connected systems.',
         [
            ('NRA-11', 'PLATFORM', 'Network Security', 'Encryption in transit',
             '1. Identify links over untrusted networks.\n2. Verify encryption (IPSec, TLS, MACsec).\n3. Check standards (TLS 1.2+, AES-256).\n4. Verify certificate management.',
             'Encryption standards policy; VPN/TLS config; Certificate inventory', 'Inspection'),
            ('NRA-12', 'PLATFORM', 'Network Security', 'Access controls and authentication',
             '1. Review NAC mechanisms (802.1X).\n2. Verify management access uses RADIUS/TACACS+ with MFA.\n3. Check default credentials changed.\n4. Verify unused ports disabled.\n5. Sample 10 device configs.',
             'NAC config; RADIUS/TACACS+ config; Sample device configs; Port status reports', 'Inspection'),
            ('NRA-13', 'PLATFORM', 'Network Security', 'Configuration integrity',
             '1. Verify daily config backups.\n2. Check drift detection and alerting.\n3. Confirm baseline configs exist per device type.\n4. Verify secure backup storage.',
             'Config backup schedule; Drift monitoring tool; Baseline config library; Backup storage', 'Inspection'),
        ]),
        ('Domain 5 — Network Design Blueprint (10.41)',
         'A current network blueprint is essential for security and change management. Expect a comprehensive, version-controlled, approved blueprint. Stale blueprints lead to security gaps and uncontrolled changes.',
         [
            ('NRA-14', 'ORG', 'Network Blueprint', 'Current blueprint',
             '1. Obtain network design blueprint.\n2. Verify it covers: logical/physical topology, IP addressing, VLAN design, routing, security zones, external connectivity.\n3. Check it reflects current state.\n4. Verify version-controlled.',
             'Network design blueprint; Version history; Change control records', 'Inspection'),
            ('NRA-15', 'ORG', 'Network Blueprint', 'Review and approval',
             '1. Check blueprint approved by appropriate authority.\n2. Verify reviewed at least annually.\n3. Confirm accessible to relevant teams.',
             'Approval records; Review schedule; Access/distribution records', 'Inspection'),
        ]),
        ('Domain 6 — Network Device Logging (10.42)',
         'Network device logging supports incident investigation and compliance. Expect centralised, tamper-protected, time-synchronised logs with defined retention. Without logs, incidents cannot be investigated.',
         [
            ('NRA-16', 'PLATFORM', 'Network Logging', 'Comprehensive logging',
             '1. Review logging config on 10 sample devices.\n2. Verify security events logged (auth, config changes, ACL, admin actions).\n3. Confirm centralised log management.\n4. Verify NTP synchronisation.',
             'Sample device logging configs; Centralised log system; NTP config', 'Inspection'),
            ('NRA-17', 'ORG', 'Network Logging', 'Log retention and review',
             '1. Check retention against policy (min 12 months online).\n2. Verify tamper protection.\n3. Confirm logs reviewed through SIEM or manual process.\n4. Sample 5 events and trace to response.',
             'Log retention policy; Log protection mechanisms; SIEM rules; Sample event investigation records', 'Inspection'),
        ]),
        ('Domain 7 — Network Segmentation (10.43)',
         'Network segmentation limits blast radius and lateral movement. Expect zone-based segmentation, micro-segmentation for critical assets, wireless isolation. Flat networks allow unrestricted lateral movement.',
         [
            ('NRA-18', 'PLATFORM', 'Segmentation', 'Segmentation strategy',
             '1. Obtain segmentation policy and design.\n2. Verify: prod vs non-prod, internal vs DMZ, PCI zones, guest/IoT.\n3. Review firewall/ACL rules.\n4. Conduct sample traffic flow tests.',
             'Segmentation policy; Firewall/ACL rule sets; Traffic flow test results', 'Inspection'),
            ('NRA-19', 'PLATFORM', 'Segmentation', 'Micro-segmentation for critical assets',
             '1. Identify most critical segments.\n2. Verify additional controls beyond standard segmentation.\n3. Check application-layer segmentation.\n4. Verify explicit authorisation required.',
             'Critical segment identification; Additional segmentation controls; Access authorisation records', 'Inspection'),
            ('NRA-20', 'PLATFORM', 'Segmentation', 'Wireless network security',
             '1. Identify all wireless networks.\n2. Verify segmentation from wired corporate.\n3. Check WPA3-Enterprise or WPA2-Enterprise minimum.\n4. Verify rogue AP detection.\n5. Review wireless security assessment.',
             'Wireless inventory; Segmentation design; Auth config; Rogue AP detection; Wireless security reports', 'Inspection'),
        ]),
    ]

    for section_data in sections:
        title, context, tests = section_data
        write_section_row(ws, r, title)
        r += 1
        if context:
            write_context_row(ws, r, context)
            r += 1
        for t in tests:
            write_test_row(ws, r, *t)
            r += 1


def create_nra_workbook():
    wb = build_workbook(
        'BNM RMiT IESP — Network Resilience Assessment (NRA)',
        'Paragraph 14.2, mapped to paragraphs 10.36 to 10.43',
        'This assessment is conducted pursuant to BNM RMiT (BNM/RH/PD 028-98, 28 Nov 2025), Paragraph 14.2.',
        'Assessment covers: (1) NRA — network design, resilience, monitoring, security, segmentation (10.36-10.43), (2) Appendix 7 Part D — Minimum Controls.',
        'Network Resilience Assessment (NRA)',
        add_nra_sheets)
    wb.save('audit-work-programs/IESP-NRA-WorkProgram.xlsx')
    print('Created IESP-NRA-WorkProgram.xlsx')


# ── MAIN ────────────────────────────────────────────────────────────
if __name__ == '__main__':
    create_cloud_workbook()
    create_emerging_tech_workbook()
    create_digital_services_workbook()
    create_dcra_workbook()
    create_nra_workbook()
    print('\nAll 5 IESP AWP workbooks generated (v3).')
