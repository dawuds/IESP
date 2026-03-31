#!/usr/bin/env bash
#
# create-evidence-structure.sh
# Creates a standardized evidence folder structure for an IESP engagement.
#
# Usage: ./create-evidence-structure.sh <Engagement-Ref>
# Example: ./create-evidence-structure.sh IESP-2026-001-CloudPreImpl
#

set -euo pipefail

# --- Validate input -----------------------------------------------------------

if [ $# -lt 1 ]; then
  echo "Usage: $0 <Engagement-Ref>"
  echo ""
  echo "Creates a standardized IESP audit evidence folder structure."
  echo ""
  echo "Examples:"
  echo "  $0 IESP-2026-001-CloudPreImpl"
  echo "  $0 IESP-2026-002-DCRA"
  echo "  $0 IESP-2026-003-NRA"
  exit 1
fi

ENGAGEMENT_REF="$1"
ROOT_DIR="$ENGAGEMENT_REF"

if [ -d "$ROOT_DIR" ]; then
  echo "ERROR: Directory '$ROOT_DIR' already exists. Aborting to avoid overwriting."
  exit 1
fi

# --- Define folder structure --------------------------------------------------

FOLDERS=(
  # 00 - Engagement Administration
  "00-Engagement-Admin/engagement-letter"
  "00-Engagement-Admin/independence-declaration"
  "00-Engagement-Admin/team-qualifications"

  # 01 - Planning
  "01-Planning/prior-reports"
  "01-Planning/scoping-memo"
  "01-Planning/document-request-list"

  # 02 - Scoping
  "02-Scoping/platform-inventory"
  "02-Scoping/critical-systems-inventory"
  "02-Scoping/sampling-methodology"

  # 03 - Evidence: Governance (Appendix 10 Part A / Appendix 9 Domain 1-3)
  "03-Evidence-Governance/strategy"
  "03-Evidence-Governance/policies"
  "03-Evidence-Governance/risk-assessment"
  "03-Evidence-Governance/roles-responsibilities"
  "03-Evidence-Governance/competency"
  "03-Evidence-Governance/compliance-mapping"
  "03-Evidence-Governance/oversight"

  # 04 - Evidence: Controls (Appendix 10 Part B / Appendix 9 Domain 4-5)
  "04-Evidence-Controls/architecture"
  "04-Evidence-Controls/identity-access-management"
  "04-Evidence-Controls/data-protection"
  "04-Evidence-Controls/network-security"
  "04-Evidence-Controls/compute-security"
  "04-Evidence-Controls/storage-security"
  "04-Evidence-Controls/logging-monitoring"
  "04-Evidence-Controls/vulnerability-management"
  "04-Evidence-Controls/change-management"
  "04-Evidence-Controls/incident-response"
  "04-Evidence-Controls/business-continuity"
  "04-Evidence-Controls/vendor-management"
  "04-Evidence-Controls/exit-strategy"
  "04-Evidence-Controls/regulatory-compliance"

  # 05 - Evidence: Part D minimum controls
  "05-Evidence-PartD/1a-access-control"
  "05-Evidence-PartD/1b-physical-security"
  "05-Evidence-PartD/1c-operations-security"
  "05-Evidence-PartD/1d-communications-security"
  "05-Evidence-PartD/1e-incident-management"
  "05-Evidence-PartD/1f-business-continuity"
  "05-Evidence-PartD/2a-customer-authentication"
  "05-Evidence-PartD/2b-transaction-authentication"
  "05-Evidence-PartD/2c-segregation-of-duties"
  "05-Evidence-PartD/2d-data-integrity"
  "05-Evidence-PartD/2e-mobile-device-risks"

  # 06 - Evidence: DCRA (for DCRA engagements)
  "06-Evidence-DCRA/resilience-objectives"
  "06-Evidence-DCRA/redundancy"
  "06-Evidence-DCRA/physical-security"
  "06-Evidence-DCRA/dc-operations"
  "06-Evidence-DCRA/segregation"

  # 07 - Evidence: NRA (for NRA engagements)
  "07-Evidence-NRA/network-design"
  "07-Evidence-NRA/network-resilience"
  "07-Evidence-NRA/network-monitoring"
  "07-Evidence-NRA/network-security"
  "07-Evidence-NRA/network-blueprint"
  "07-Evidence-NRA/network-logging"
  "07-Evidence-NRA/network-segmentation"

  # 08 - Working Papers
  "08-Working-Papers/awp-workbooks"
  "08-Working-Papers/sampling-records"
  "08-Working-Papers/interview-notes"
  "08-Working-Papers/screenshots"

  # 09 - Findings
  "09-Findings/draft-findings"
  "09-Findings/management-responses"
  "09-Findings/final-findings"

  # 10 - Report
  "10-Report/draft-report"
  "10-Report/review-comments"
  "10-Report/final-report"

  # 11 - Sign-Off
  "11-Sign-Off/management-sign-off"
  "11-Sign-Off/board-presentation"
  "11-Sign-Off/part-c-attestation"
)

# --- Create structure ---------------------------------------------------------

echo "Creating evidence folder structure for: $ENGAGEMENT_REF"
echo "---"

dir_count=0
gitkeep_count=0

for folder in "${FOLDERS[@]}"; do
  mkdir -p "$ROOT_DIR/$folder"
  touch "$ROOT_DIR/$folder/.gitkeep"
  ((dir_count++))
  ((gitkeep_count++))
done

# --- Create root README.md ---------------------------------------------------

CREATION_DATE=$(date +%Y-%m-%d)

cat > "$ROOT_DIR/README.md" << EOF
# IESP Evidence Pack: $ENGAGEMENT_REF

**Created:** $CREATION_DATE

## Folder Structure

| Folder | Purpose |
|--------|---------|
| 00-Engagement-Admin | Engagement letter, independence declarations, team CVs |
| 01-Planning | Prior reports, scoping memo, document request list |
| 02-Scoping | Platform inventory, critical systems, sampling methodology |
| 03-Evidence-Governance | Strategy, policies, risk assessment (App 10 Part A / App 9 Domain 1-3) |
| 04-Evidence-Controls | Technical controls evidence (App 10 Part B / App 9 Domain 4-5) |
| 05-Evidence-PartD | Appendix 7 Part D minimum controls |
| 06-Evidence-DCRA | Data Centre Resilience Assessment (DCRA engagements only) |
| 07-Evidence-NRA | Network Resilience Assessment (NRA engagements only) |
| 08-Working-Papers | AWP workbooks, sampling records, interview notes, screenshots |
| 09-Findings | Draft findings, management responses, final findings |
| 10-Report | Draft and final reports, review comments |
| 11-Sign-Off | Management sign-off, board presentation, Part C attestation |

## Naming Convention

Evidence files should follow: \`[ControlRef]-[Description].[ext]\`

Examples:
- \`CLD-12-IAM-policy-review.pdf\`
- \`PD-1a-access-control-matrix.xlsx\`
- \`GOV-03-risk-assessment-2026.pdf\`

## Notes

- Folders 06 and 07 are engagement-type-specific; remove if not applicable.
- See \`templates/evidence-folder-structure.md\` in the IESP repo for full documentation.
EOF

# --- Summary ------------------------------------------------------------------

echo ""
echo "Folder structure created successfully."
echo ""
echo "  Engagement ref : $ENGAGEMENT_REF"
echo "  Root directory  : $ROOT_DIR/"
echo "  Folders created : $dir_count"
echo "  .gitkeep files  : $gitkeep_count"
echo "  README.md       : $ROOT_DIR/README.md"
echo ""
echo "Top-level structure:"
ls -1d "$ROOT_DIR"/*/
