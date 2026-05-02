# P3 R3 Revision — Master Memo

**Manuscript.** Technological Capability, Digital Adoption, and the Internationalization–Performance Relationship: A Firm-Level Study of Singapore.
**Authors.** Do Thuy Huong (lead); Phan Anh Tu (corresponding).
**Target.** Management International Review (Round 3 resubmission).
**Date.** 2 May 2026.
**Branch / PR.** `claude/p3-r3-revision` · GitHub PR #6 (8 commits, 51/51 audit pass).

---

## 1. Why this revision

R2 reviewer raised five framing/identification concerns and two factual errors. The three most consequential were (a) the full-sample quadratic OLS being anchored by the extensive margin (82.2% of firms have FSTS = 0); (b) the headline DAI moderation appearing only in the thinly populated upper tail (3.2% of firms above FSTS = 70%); and (c) Table 3 baseline values inconsistent with Table 2 Model M8.

## 2. Strategic decisions locked

- **Title.** Drop "Digital-Frontier Economy"; recast as **"A Firm-Level Study of Singapore."**
- **Framing.** Singapore as an **extreme-case, within-context setting**, not a basis for a universal boundary-condition claim.
- **Empirical architecture.** Extensive–intensive split: exporter-only intensive analysis is the primary inferential test; full-sample polynomial is descriptive baseline only.
- **Corresponding author.** Phan Anh Tu (permanent institutional email).

## 3. What changed in the manuscript

- Title, Abstract, Sections 1.1–1.3 / 5 / 6 reframed; "digital-frontier" removed from manuscript, cover letter, and title page.
- **H2** rewritten — no longer interprets a non-significant interaction as evidence of "no moderation."
- **H3** rewritten — replaces "positive average DAI association" with conditional-on-export-intensity logic.
- **Table 3** corrected: all six rows had stale numbers from an earlier draft; replaced with canonical re-estimation.
- **Section 7 caveat** re-grounded in (i) thin upper-tail support and (ii) borderline precision in the small exporter subsample — no longer cites cross-sample adjusted R² (D2 fix).
- Cover Letter and Title Page synced with the new title and framing.

## 4. Key empirical findings (canonical)

- Canonical M8 reproduces Table 2 M8 exactly: TCI = +0.153, FSTS² × DAI = +3.119, Adj R² = 0.196, N = 617.
- **Within exporters (N = 84): no inverted-U detected** (Lind–Mehlum p = 0.78). The full-sample inverted-U was an extensive-margin artifact.
- DAI moderation is robust: 100% of 617 LOO fits keep FSTS² × DAI significant; trimming firms with FSTS > 70% makes the effect *stronger* (β = +7.09, p = .004), not weaker.
- 5,000-rep cluster bootstrap on the M2 turning point: shape robust (96.3% of replications recover an inverted-U), location loosely identified (95% CI [53%, 253%]). Treat 82% as indicative.
- Intensive-margin joint F-test for DAI moderation: F = 6.32, p = .003 — moderation survives within exporters.

## 5. Construct validity (Phase 3)

- Mean cross-construct correlation (TCI item × DAI item) = 0.106 — low fungibility risk.
- **Item-swap falsification:** moving the firm-website indicator (c22b) from DAI to TCI **breaks** the moderation (joint F drops from p = .011 to p = .154). Construct assignment matters.
- DAI moderation depends on the foundational digital-infrastructure indicators (c22b website + k33 e-payment); dropping c22b alone collapses the joint F (p = .215).

## 6. Pending — co-author confirm

- [ ] Confirm corresponding author = Phan Anh Tu (vs. switching to Huong).
- [ ] Verify postal address on Title Page: "Campus II, 3/2 Street, Ninh Kieu District, Can Tho City 900000."
- [ ] Funding statement: default is "no support" — declare any CTU/Vietnam grant?
- [ ] Acknowledgments: currently a generic line — anyone specific to thank?

## 7. Outstanding work

- [ ] Regenerate the embedded Figure 2 / Figure 3 PNGs in the manuscript using `outputs/r3/figures/Fig2_v2.png` and `Fig3_v2.png` (support-aware versions with rug + decile counts + bootstrap CI).
- [ ] Save the manuscript as PDF and submit via the MIR portal (https://www.editorialmanager.com/mir/).

## 8. Where to find the evidence

- Code (re-runnable end-to-end): `tools/r3/` — eight numbered scripts.
- Outputs: `outputs/r3/audit/` (JSON), `outputs/r3/tables/` (LaTeX), `outputs/r3/figures/` (PNG).
- D1 root-cause memo: `outputs/r3/audit/D1_root_cause.md`.
- Canonical M8 sheet: `outputs/r3/audit/m8_canonical.{json,csv,txt}`.
- Full diff and commit history: PR #6 on GitHub.
