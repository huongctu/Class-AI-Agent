# P5 China — APJM Submission Outline

## 1. Title (recommended)

**Threshold Stability in the Export Intensity–Performance Relationship: Evidence from Chinese Private Firms**

Lý do đổi: đưa contribution (*threshold stability*) lên đầu thay vì để setting dẫn dắt; APJM editors screen contribution ngay từ title. Sample identity đã được đổi sang "Chinese Private Firms" để phản ánh đúng full WBES private-firm frame (xem `patch_list_v1_2_to_v1_3.md`).

## 2. Abstract (8 câu, ~200 từ)

1. **Question** — Do nonlinear thresholds in the export intensity–performance relationship represent durable structural features of an emerging-economy private-firm setting, or are they sample-specific regularities?
2. **Setting** — Chinese private firms over two World Bank Enterprise Survey waves (2012 and 2024), spanning a period of substantial structural and policy change.
3. **Method** — Quadratic specifications with Lind-Mehlum tests, delta-method confidence intervals for turning points, Paternoster z-tests for cross-wave coefficient equality, and cluster-robust standard errors on firm identifiers in pooled estimation.
4. **Sample** — 2,619 firms (2012) and 1,940 firms (2024), pooled to 4,559 firm-year observations.
5. **Main finding** — Estimated turning points of approximately 49.4% (2012), 47.6% (2024), and 48.9% (pooled); Paternoster z-tests fail to reject cross-wave equality, providing evidence of threshold stability.
6. **Secondary** — Technological capability is a robust positive level shifter of labour productivity in both waves; a thin digital-adoption proxy is weak and measurement-sensitive.
7. **Implication** — Findings suggest a durable bounded operating range (roughly 30–60% export intensity) for Chinese private firms rather than a knife-edge optimum.
8. **Contribution** — First cross-wave threshold-stability test for the export intensity–performance relationship in an emerging-economy private-firm setting.

## 3. Section structure

### 3.1 Introduction (4–5 paragraphs)

- ¶1 — Open with internationalization–performance debate; identify unresolved question of *threshold durability over time*.
- ¶2 — Position Chinese private firms as theoretically salient (export dependence + financing constraints + coordination costs in emerging economy).
- ¶3 — Three motives: (i) test threshold stability, (ii) consider working-capital interpretation, (iii) keep digital adoption and tech capability analytically separate.
- ¶4 — Three contributions, ordered: threshold stability (main), TCI as robust level shifter, working-capital as bounded interpretive lens.
- ¶5 — Roadmap.

### 3.2 Theory & hypotheses

| # | Hypothesis | Status |
|---|---|---|
| H1 | Inverted-U: lnLP rises then falls in FSTS | Standard nonlinear IB logic |
| H2 | Turning point in 2024 is substantively similar to 2012 | **Central to APJM contribution** |
| H3 | Technological capability positively shifts lnLP | Secondary level effect |
| (interpretive) | Working-capital pressure plausibly underlies right-side decline | Frame, not hypothesis |

### 3.3 Data & methods

- WBES 2012 + 2024, full private-firm frame for China (covers manufacturing, services, retail, IT, construction).
- **Sample-construction protocol** — link to `audit/audit_N_checklist.csv`; 6 tầng lọc: raw → (optional mfg) → recode missing → analytic → sample flags → composites within-wave standardized.
- **ISIC version note** — 2012 uses ISIC Rev 3.1 (a4a 15–38); 2024 uses ISIC Rev 4 (d1a2_v4 4-digit). Aggregate frame is comparable cross-wave; sectoral subgroup comparisons not attempted.
- **Variable definitions** — `lnLP = ln(d2/l1)`; `FSTS = d3c/100`; `firmage = year − b5`; `foreigndummy = b2b > 0`; `TCIfull` z-mean of e6/b8/h1/h8 with ≥3/4 nonmissing; `DAIthin` z-mean of c22b + e6 (cross-wave comparable); within-wave standardization preserved through pooling.
- **Pooled clustered SE** — 217 panel firms appear in both waves; pooled regressions use `vce(cluster idstd)` for valid inference. (Document this as alternative to dropping panel firms or running firm fixed effects.)
- **Tests** — Lind-Mehlum utest for inverted-U; delta-method CIs for turning point; Paternoster z for cross-wave coefficient equality on FSTS and FSTSsq.
- **Language discipline** — associational throughout (repeated cross-section, not panel identification).

### 3.4 Results

| Subsection | Content | Visual |
|---|---|---|
| 4.1 Baseline inverted-U | M0–M2 across 2012 / 2024 / pooled | Coefficient table |
| 4.2 Threshold stability (main) | Turning points + 95% CIs three samples; Paternoster z | **Forest-plot style figure** of three TPs with CIs side-by-side |
| 4.3 Level-shift effects | M3–M8: TCI consistent positive; DAIthin weak | Coefficient table |
| 4.4 Supplementary mechanism | Working-capital exploratory checks (mixed) | Brief table |

### 3.5 Discussion

- ¶1 — Restate paper as threshold-stability study, not working-capital study.
- ¶2 — Why stability matters for APJM readers: durable structural feature of Chinese private firms, not period artifact.
- ¶3 — Managerial implication: bounded operating range ~30–60% export intensity, not single optimum.
- ¶4 — TCI as productivity-enhancing condition; DAIthin as measurement-limited construct.
- ¶5 — Working-capital lens: theoretically plausible, not directly identified; future-research agenda using richer financial microdata.

### 3.6 Limitations

1. Repeated cross-section — associational claims only, no within-firm causal identification.
2. ISIC Rev 3.1 → Rev 4 frame change between waves — no sector decomposition cross-wave.
3. Thin DAI proxy — c22b + e6 chosen for cross-wave availability; richer 2024 digital items reported as robustness, not main.
4. 217 panel firms in 2024 — handled via clustered SE rather than firm fixed effects (preserves N and avoids changing paper architecture to panel design).
5. WBES weighting — base estimates unweighted (per manuscript v1.2 convention); robustness available with `wmedian`.

## 4. Submission package

| Component | File | Notes |
|---|---|---|
| Title page | `title_page.docx` | Authors, ORCID, affiliations, corresponding author, acknowledgments |
| Blinded manuscript | `manuscript_blinded.docx` | Strip authors/identifiers; mask self-citations to "Author (year)" |
| Cover letter | `cover_letter.docx` | APJM fit + threshold-stability contribution + originality + 217-firm clustered SE note |
| Tables/figures | per APJM rules | Verify embed vs separate file at submission portal |
| Declarations | within manuscript | Competing interests, funding, data availability (WBES public domain) |
| Online appendix (optional) | `appendix.pdf` | Audit N table, robustness with `DAIrich`, weighted estimates |

## 5. Cover letter outline

> Dear Editor, We submit *Threshold Stability in the Export Intensity–Performance Relationship: Evidence from Chinese Private Firms* for consideration at *Asia Pacific Journal of Management*. The paper uses the World Bank Enterprise Survey data for China in 2012 and 2024 to test whether the inverted-U turning point in the export intensity–performance relationship represents a durable structural feature of an Asia-Pacific emerging-economy private-firm setting. We estimate substantively similar turning points (49.4%, 47.6%, 48.9%) across both wave-specific and pooled samples and use Paternoster z-tests to formally fail to reject cross-wave coefficient equality. Pooled estimates use cluster-robust standard errors on firm identifiers to handle 217 panel firms appearing in both waves. We position the paper's contribution at the level of internationalization–performance theory in the Asia-Pacific context and at the boundary of replication-as-discovery in international business. The manuscript is original, has not been published elsewhere, and is not under consideration at any other journal. Authors declare no competing interests.

## 6. Pre-submission checklist

- [ ] Audit N table from `01–03` matches expected ±10 firms at every step.
- [ ] M2 turning points within [48%, 51%] (2012) and [46%, 49%] (2024). — **Verified Python**.
- [ ] Paternoster z on FSTS and FSTSsq fails to reject equality (p > 0.10). — **Verified Python (p = 0.412, 0.545)**.
- [ ] Pooled clustered SE recognized ~4,342 unique `idstd` clusters. — **WARN: Python found 0 panel duplicates; investigate**.
- [ ] Manuscript blinded (no author names, no self-references revealing identity).
- [ ] Title page submitted as separate file.
- [ ] Cover letter contribution language matches abstract and introduction.
- [ ] APJM author guidelines re-read at moment of submission (formatting, word count, references style).
- [ ] Internal review by ≥1 colleague before upload.
- [ ] Data availability statement points to WBES public portal.

## 7. Open items to verify against manuscript v1.2 before submission

1. `firmage` exact formula in current draft (`year − b5` vs alternative).
2. `foreigndummy` threshold (b2b > 0% vs b2b ≥ 10%).
3. TCI/DAI variable mapping in BREADY 2024 questionnaire (item codes may have changed from `e6/b8/h1/h8/c22b` to BREADY equivalents).
4. Panel link mechanism: 2024 panel=1 firms (n=217) should match 2012 idstd; current Python finds 0 matches — cluster SE may be a no-op.
5. WBES sampling weights — base unweighted in v1.2? Robustness with `wmedian`?
