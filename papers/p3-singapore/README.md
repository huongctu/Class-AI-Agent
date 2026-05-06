# P3 Singapore — MIR R3 final

> Status: **Round 3 final + 12 post-revision patches → ready round 4 submission**
> Last update: 2026-05-06
> Source branch (archive): [`claude/p3-r3-revision`](https://github.com/huongctu/Class-AI-Agent/tree/claude/p3-r3-revision)

## Manuscript info

| Item | Value |
|---|---|
| **Title** | Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship: A Firm-Level Study of Singapore |
| **Target journal** | **Management International Review** (MIR), Springer |
| **Tier** | ABS 3, SSCI Q2 |
| **Authors** | Đỗ Thùy Hương, Phan Anh Tú |
| **Data** | WBES Singapore 2023 (B-READY methodology) |
| **Sample** | N = 623 (full); N = 617 (with DAI items) |
| **Method** | OLS with HC1 robust SE, M0–M8 hierarchical, item-swap falsification, bootstrap CI for turning point |
| **Word count** | ~7,800 words main text |

## File map

```
p3-singapore/
├── README.md                     # this file
├── manuscript/
│   ├── manuscript_R3_FIGFIXED.docx           # FINAL: R3 + 12 patches + Fig 1 fix (USE THIS)
│   ├── Manuscript_Blinded_MIR_2_revised.docx # R3 reference (before our 12 patches)
│   ├── Manuscript_Blinded_MIR_2_original.docx # R2 reference (before R3 revision)
│   ├── Cover_Letter.docx
│   └── Title_Page.docx
├── submission/
│   ├── README.md                              # MIR submission upload mapping
│   ├── 01_Manuscript.docx + .pdf
│   ├── 02_Title_Page.docx + .pdf
│   ├── 03_Cover_Letter.docx + .pdf
│   ├── 04_Master_Revision_Memo.md
│   └── figures/                               # final 3 figures (PNG)
├── figures/
│   ├── figure1_conceptual_model.png           # FIXED via matplotlib (used in R3 final)
│   ├── figure2_dai_marginal.png               # support-aware version
│   ├── figure3_predicted_curve.png            # bootstrap-aware version
│   └── source/
│       ├── regenerate_fig1.py                 # matplotlib script
│       └── README.md
├── replication/
│   ├── README.md
│   ├── fix_r3_post_revision.py                # 11 text patches
│   ├── regenerate_fig1.py                     # Figure 1 source (duplicate of figures/source/)
│   └── data_source.md                         # WBES Singapore 2023 mapping
└── audit/
    ├── R3_Post_Revision_Audit.md              # 12 post-revision patches log
    ├── R3_Master_Revision_Memo.md             # round-3 strategic memo
    ├── R3_Editor_Simulation_Verdict.md        # editor-simulation verdict
    ├── R3_vs_R2_Comparison.md                 # R3 vs R2 detailed diff
    └── P3_Revision_Package.md                 # complete package summary
```

## Theoretical positioning (TCI/DAI separation)

P3 separates two constructs along the digital-business-strategy literature:

- **Technological Capability Index (TCI)** — anchored in Lall (1992) and Cohen & Levinthal (1990) absorptive-capacity tradition; firm-internal capability depth via R&D, ISO certification, foreign-licensed technology
- **Digital Adoption Index (DAI)** — anchored in Bharadwaj et al. (2013) and Verhoef et al. (2021) digitalisation hierarchy (Tier 1–2: digital presence + transaction-enabling)

Methodologically, both constructs satisfy 4-criterion test for formative composites (Coltman et al., 2008). The separation is **not** an FDCI alternative — these constructs travel along genuinely different theoretical traditions per Bhandari et al. (2023) resource-orchestration logic.

## Hypothesis structure

- **H1** (TCI direct effect): Technological capability is positively associated with firm performance — **supported** (β = 0.168, p < .001)
- **H2** (DAI conditional effect): The productivity association of DAI is conditional rather than uniform — **supported** at FSTS = 0% (+0.080, p = .045)
- **H3** (DAI moderation): DAI–productivity association becomes more positive at high export intensity — **supported** by FSTS² × DAI = +3.119** (p = .005); marginal effect at FSTS = 70% is +0.588* (p = .025), at FSTS = 100% is +1.742** (p = .002)
- *(Open empirical question)* TCI moderation tested supplementarily; no statistically distinguishable moderation under present design

## Key findings

1. **Inverted-U not formally identified** within observed export-intensity range. Lind–Mehlum p = .303; bootstrap CI for turning point [53%, 253%] — interpretation: "predominantly positive with mild quadratic curvature"
2. **TCI = level-shift effect** on productivity intercept; identification-robust under PSM and 2SLS
3. **DAI = conditional scaling resource** for high-export firms; effect concentrated in upper tail (~3% of firms have FSTS > 50%)
4. **Item-swap falsification**: reassigning website indicator (c22b) from DAI to TCI collapses DAI moderation joint F from 4.56 (p = .011) to 1.88 (p = .154) — confirms construct boundary

## 12 patches applied post-R3

See [`audit/R3_Post_Revision_Audit.md`](audit/R3_Post_Revision_Audit.md) for full detail. Summary:

1. **Avenyo (2021) DOI** verified via Crossref → corrected `s41287-020-00328-2` → `s41287-021-00364-6`; subtitle updated to "Evidence from African firms"
2-7. **Hypothesis renumbering** (H1, H3, H4 → H1, H2, H3) since R3 demoted original H2 to "open empirical question"
8-11. **Figure 1 caption + Figure 1 image** regenerated via matplotlib with corrected hypothesis labels
12. Cross-references in supplementary materials list updated

## Replication

See [`replication/README.md`](replication/README.md) for step-by-step.

Quick reproduce:
```bash
pip install python-docx matplotlib pillow
python3 replication/fix_r3_post_revision.py    # apply 11 text patches
python3 figures/source/regenerate_fig1.py       # regenerate Figure 1
# then merge fig1_FIXED.png into manuscript_R3_FIGFIXED.docx (already done in repo)
```

Data prerequisites: WBES Singapore 2023 raw data — see [`replication/data_source.md`](replication/data_source.md).

## Cross-link với thesis

P3 evidence được cite trong:

- [`../../thesis/04_references_apa7.md`](../../thesis/04_references_apa7.md) Section M
- [`../../thesis/01_chapter_outline_vi.md`](../../thesis/01_chapter_outline_vi.md) Ch.4.2 (ASEAN benchmark)
- [`../../thesis/05_p5_china_design_vi.md`](../../thesis/05_p5_china_design_vi.md) cho cross-paper comparison
- [`../../manuscripts/p4_singapore_en_clean.md`](../../manuscripts/p4_singapore_en_clean.md) markdown summary internal
