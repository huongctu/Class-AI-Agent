# Papers — Submission package dossier

> NCS Đỗ Thùy Hương · PhD candidate · Trường Kinh tế, Đại học Cần Thơ · Code P1323001

Folder này chứa **3 working papers công bố quốc tế** đang ở các vòng phản biện khác nhau, kèm đầy đủ artifact tái tạo (figures, tables, scripts, audit reports) và mapping với pipeline dữ liệu `wbes/` cũng như các chương luận án `thesis/`.

## Tổng quan 3 papers

| # | Paper | Country | Pool | Method | Journal | Status |
|---|---|---|---|---|---|---|
| **P3** | Technological Capability, Digital Adoption, and the I–P Relationship: A Firm-Level Study of Singapore | Singapore | WBES 2023 (B-READY), N=623/617 | OLS HC1, M0–M8 with TCI/DAI moderation | **MIR** (Management International Review) | Round 3 final + 12 patches → ready round 4 |
| **P4** | Revisiting the I–P Relationship in an Emerging Market: TCI and Digital Adoption — Three-Wave Evidence from Vietnam | Vietnam | WBES 2009/2015/2023, N=2,958 pooled | OLS HC1, wave-specific + pooled, PSM, IV/2SLS, Oster bounds | **IJoEM** (International Journal of Emerging Markets) | v5.9 (was v5.8) + 27 edits → ready round 3 |
| **P5** | The Export Intensity–Performance Relationship in Chinese Private Firms: A Threshold-Stability Perspective | China | WBES 2012/2024, ~4,800 firms + 217 panel | OLS HC1, threshold stability, three-way moderation | **APJM** (Asia Pacific Journal of Management) | v1.8 + Avenyo DOI fix → ready submission |

## Per-paper navigation

- [`p3-singapore/`](p3-singapore/) — MIR R3 final + figures + audit + replication
- [`p4-vietnam/`](p4-vietnam/) — IJoEM v5.9 + figures (PNG/PDF) + figures_excel + 10 tables CSV + 2 response letters
- [`p5-china/`](p5-china/) — APJM v1.8 + 6 markdown parts + Graphviz/matplotlib sources + 4 audit reports

## Cross-link với `thesis/`

Tất cả 3 papers (P3, P4, P5) cùng pipeline data với 2 papers đã công bố (P1 VEFR 2026, P2 JFAR 2026) tạo thành **dossier 5 papers** làm minh chứng cho Chương 4 luận án:

| Paper | Section luận án | Vai trò |
|---|---|---|
| P1 (Đỗ & Phan, 2026 — VEFR) | Ch.2.4 + Ch.4.1 baseline | Đã công bố — emerging Asia 17 nước, digital shield effect |
| P2 (Đỗ & Phan, 2026 — JFAR) | Ch.4.2 + Ch.4.5 robustness | Đã công bố — China cubic, turning point ~47.8% FSTS |
| **P3 Singapore** | **Ch.4.2 ASEAN benchmark** | TCI/DAI separation, conditional scaling DAI |
| **P4 Vietnam** | **Ch.4.2 transitional economy** | Resource Diversion Trap, 3-wave heterogeneity |
| **P5 China** | **Ch.4.5 temporal heterogeneity** | Threshold stability 2012 → 2024 |

→ Khung lý thuyết chung: TCI/DAI separation theo Bharadwaj et al. (2013), Verhoef et al. (2021), Lall (1992), Cohen & Levinthal (1990), Bhandari et al. (2023), Coltman et al. (2008).

## Pipeline dữ liệu chung

Tất cả 3 papers dùng **WBES microdata** đã hài hoà qua pipeline trong [`wbes/`](../wbes/):

- 47 nền kinh tế · 107 cặp quốc gia × năm · 14 mốc khảo sát · 2009–2025
- 3 thế hệ schema: PICS3 (2009–2012), Standardized (2013–2017), BREADY/BEE (2018–2025)
- Pool gộp 101.035 doanh nghiệp

Mỗi paper truy về subset của pool này:

- P3 Singapore → Singapore 2023 wave only (1 nước, 1 năm)
- P4 Vietnam → Vietnam 3 waves 2009/2015/2023 (1 nước, 3 năm)
- P5 China → China 2 waves 2012/2024 (1 nước, 2 năm)

## Reproducibility statement

Tất cả figures và tables trong mỗi paper được tái tạo từ scripts trong `replication/`:

- **P3**: `regenerate_fig1.py` (matplotlib) cho Figure 1; `fix_r3_post_revision.py` cho text patches
- **P4**: 6 file `figures_excel/*.xlsx` chứa data + chart + image; `apply_v59_edits.py` cho 20 reviewer edits
- **P5**: `build_docx.sh` one-shot pandoc build; `figures/source/render_figures.py` cho figs 2-4; Graphviz `.dot` cho fig 1

Xem chi tiết trong README của từng paper folder.

## Quy ước phiên bản

- File DOCX trong `manuscript/` của mỗi paper là **bản gửi journal cuối cùng** (đã apply tất cả patches)
- File legacy/reference (R2 original của P3, v5.8 của P4) được giữ trong cùng folder kèm suffix giải thích
- Branches gốc (`claude/p3-r3-revision`, `claude/update-p4-draft-W6UKL`, `claude/p5-china-sample-outline-1KXp4`) **không bị xoá** — giữ làm git history archive

## Sửa lỗi đã apply (cross-paper)

| Lỗi | P3 | P4 | P5 |
|---|---|---|---|
| Avenyo (2021) DOI sai (`s41287-020-XXX...`) → `s41287-021-00364-6` | ✅ fixed | ✅ fixed (chưa có trong P4) | ✅ fixed |
| Avenyo title sai → "Evidence from African firms" | ✅ fixed | n/a | ✅ fixed |
| Hypothesis numbering có gap | ✅ H3/H4 → H2/H3 | ✅ H1 reframe + H4 exploratory | ✅ already H1, H2, H3, H4a, H4b |
| Title chưa có country marker | ✅ "...Study of Singapore" | ✅ "... Three-Wave Evidence from Vietnam" | ✅ "...Chinese Private Firms" |
| Tables/Figures count mismatch trong metadata | n/a | ✅ Tables: 2 → 4; Figures: 2 → 3 | n/a |

## Submission targets ưu tiên

Theo phân tích `p5-china/audit/SUBMISSION_TARGETS.md` và literature positioning:

- **P3 Singapore** → MIR (current) hoặc IBR / Asian Business & Management — single-country digital-frontier setting
- **P4 Vietnam** → IJoEM (current) hoặc JIBS Round-2 từ chối có thể submit lại MIR
- **P5 China** → APJM (current) hoặc MIR / JIBS / JWB — threshold-stability + capability moderation fit

Xem chi tiết trong `p5-china/audit/SUBMISSION_TARGETS.md`.

---

*Last updated: 2026-05-06. Dossier maintained for thesis defense và journal resubmission cycles.*
