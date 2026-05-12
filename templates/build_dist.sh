#!/bin/bash
# Build dist folder structure with DOCX files converted from MD via Pandoc with CTU templates.
#
# Prerequisites:
#   - pandoc (https://pandoc.org/installing.html)
#   - python3 with python-docx (`pip install python-docx`)
#
# Usage:
#   1. Clone repo: git clone -b claude/asia-internationalization-performance-2cYgO https://github.com/huongctu/Class-AI-Agent.git
#   2. cd Class-AI-Agent
#   3. Build CTU templates: pandoc -o /tmp/pandoc_default.docx --print-default-data-file reference.docx
#                            python3 templates/build_ctu_reference.py /tmp/pandoc_default.docx templates/
#   4. Run this script: bash templates/build_dist.sh
#   5. Output appears in dist/ folder
#
set -e

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="${ROOT}"
TEMPLATES="${ROOT}/templates"
DIST="${ROOT}/dist"
THESIS_REF="${TEMPLATES}/ctu_thesis_reference.docx"
PAPER_REF="${TEMPLATES}/ctu_paper_reference.docx"

rm -rf "${DIST}"
mkdir -p "${DIST}"/{luan_an/source_md,chuyen_de_1/source_md,chuyen_de_2/source_md,manuscripts/{p3_vietnam,p4_singapore,results,reference}/source_md}

PANDOC_VI="pandoc -f gfm -t docx --reference-doc=${THESIS_REF}"
PANDOC_EN="pandoc -f gfm -t docx --reference-doc=${PAPER_REF}"

echo "[1/4] Convert luận án..."
for f in 00_optimal_plan_vi 01_chapter_outline_vi 02_theoretical_framework_vi 03_methodology_vi 04_references_apa7; do
  ${PANDOC_VI} "${SRC}/thesis/${f}.md" -o "${DIST}/luan_an/${f}.docx"
  cp "${SRC}/thesis/${f}.md" "${DIST}/luan_an/source_md/"
done
${PANDOC_VI} "${SRC}/thesis/README.md" -o "${DIST}/luan_an/00_README_thesis.docx"
cp "${SRC}/thesis/README.md" "${DIST}/luan_an/source_md/"

echo "[2/4] Convert CĐ1..."
${PANDOC_VI} "${SRC}/thesis/12_chuyen_de_1_outline_vi.md" -o "${DIST}/chuyen_de_1/12_outline.docx"
${PANDOC_VI} "${SRC}/thesis/14_cd1_part1_intro_theory_vi.md" -o "${DIST}/chuyen_de_1/14_part1_intro_theory.docx"
${PANDOC_VI} "${SRC}/thesis/15_cd1_part2_findings_vi.md" -o "${DIST}/chuyen_de_1/15_part2_findings.docx"
${PANDOC_VI} "${SRC}/thesis/16_cd1_part3_cases_conclusion_vi.md" -o "${DIST}/chuyen_de_1/16_part3_cases_conclusion.docx"
for f in 12_chuyen_de_1_outline_vi 14_cd1_part1_intro_theory_vi 15_cd1_part2_findings_vi 16_cd1_part3_cases_conclusion_vi; do
  cp "${SRC}/thesis/${f}.md" "${DIST}/chuyen_de_1/source_md/"
done

echo "[3/4] Convert CĐ2..."
${PANDOC_VI} "${SRC}/thesis/13_chuyen_de_2_outline_vi.md" -o "${DIST}/chuyen_de_2/13_outline.docx"
${PANDOC_VI} "${SRC}/thesis/17_cd2_part1_intro_theory_vi.md" -o "${DIST}/chuyen_de_2/17_part1_intro_theory.docx"
${PANDOC_VI} "${SRC}/thesis/18_cd2_part2_review_framework_hypotheses_vi.md" -o "${DIST}/chuyen_de_2/18_part2_review_framework_hypotheses.docx"
${PANDOC_VI} "${SRC}/thesis/19_cd2_part3_models_data_conclusion_vi.md" -o "${DIST}/chuyen_de_2/19_part3_models_data_conclusion.docx"
for f in 13_chuyen_de_2_outline_vi 17_cd2_part1_intro_theory_vi 18_cd2_part2_review_framework_hypotheses_vi 19_cd2_part3_models_data_conclusion_vi; do
  cp "${SRC}/thesis/${f}.md" "${DIST}/chuyen_de_2/source_md/"
done

${PANDOC_VI} "${SRC}/thesis/11_dissertation_positioning_vi.md" -o "${DIST}/manuscripts/reference/11_TLTQ_dissertation_positioning.docx" 2>/dev/null || true
${PANDOC_VI} "${SRC}/thesis/20_cd1_cd2_review_report_vi.md" -o "${DIST}/manuscripts/reference/20_cd1_cd2_review_report.docx" 2>/dev/null || true

echo "[4/4] Convert manuscripts..."
# P3 = Vietnam (theo content)
${PANDOC_VI} "${SRC}/manuscripts/p3_vietnam_vi.md" -o "${DIST}/manuscripts/p3_vietnam/p3_vietnam_vi_concise.docx"
${PANDOC_EN} "${SRC}/manuscripts/p3_vietnam_en_clean.md" -o "${DIST}/manuscripts/p3_vietnam/p3_vietnam_en_clean.docx"
cp "${SRC}/manuscripts/p3_vietnam_vi.md" "${SRC}/manuscripts/p3_vietnam_en_clean.md" "${DIST}/manuscripts/p3_vietnam/source_md/"
# P4 = Singapore (theo content)
${PANDOC_VI} "${SRC}/manuscripts/p4_singapore_vi.md" -o "${DIST}/manuscripts/p4_singapore/p4_singapore_vi_concise.docx"
${PANDOC_EN} "${SRC}/manuscripts/p4_singapore_en_clean.md" -o "${DIST}/manuscripts/p4_singapore/p4_singapore_en_clean.docx"
cp "${SRC}/manuscripts/p4_singapore_vi.md" "${SRC}/manuscripts/p4_singapore_en_clean.md" "${DIST}/manuscripts/p4_singapore/source_md/"

for f in p1_emerging_asia_results p2_china_smes_results p_india_book_chapter_results p_meta_analysis_kyyeu_results; do
  ${PANDOC_VI} "${SRC}/manuscripts/${f}.md" -o "${DIST}/manuscripts/results/${f}.docx"
  cp "${SRC}/manuscripts/${f}.md" "${DIST}/manuscripts/results/source_md/"
done

${PANDOC_VI} "${SRC}/manuscripts/QD_legal_reference.md" -o "${DIST}/manuscripts/reference/QD_legal_reference.docx"
${PANDOC_VI} "${SRC}/manuscripts/published_works_index.md" -o "${DIST}/manuscripts/reference/published_works_index.docx"
${PANDOC_VI} "${SRC}/manuscripts/README.md" -o "${DIST}/manuscripts/00_README_manuscripts.docx"

echo ""
echo "=== Built ==="
find "${DIST}" -name "*.docx" | wc -l
echo "DOCX files"
du -sh "${DIST}"
echo ""
echo "To create zip: cd ${ROOT} && zip -rq luan_an_dossier_v1.zip dist/"
