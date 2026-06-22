"""Build the round-2 point-by-point response letter for the IJoEM reviewer.

The letter responds to the Vietnamese-language Q1/Q2 IB editor-tone
peer-review report (4 major weaknesses + 4 actionable recommendations)
and maps each comment to the specific revisions implemented in v5.8.
"""

from pathlib import Path
from docx import Document
from docx.shared import Pt, Cm

OUT = Path("/home/user/Class-AI-Agent/response_letter_round2.docx")

doc = Document()
for s in doc.sections:
    s.top_margin = Cm(2.5)
    s.bottom_margin = Cm(2.5)
    s.left_margin = Cm(2.5)
    s.right_margin = Cm(2.5)

style = doc.styles["Normal"]
style.font.name = "Times New Roman"
style.font.size = Pt(11)


def H1(t):
    p = doc.add_paragraph()
    r = p.add_run(t); r.bold = True; r.font.size = Pt(13)


def H2(t):
    p = doc.add_paragraph()
    r = p.add_run(t); r.bold = True; r.font.size = Pt(11)


def P(t, italic=False, bold=False):
    p = doc.add_paragraph()
    r = p.add_run(t); r.italic = italic; r.bold = bold


def Q(t):
    p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(1.0)
    r = p.add_run(t); r.italic = True


# ---------------------------------------------------------------------------
H1("Response to Reviewer — Round 2")
P("Manuscript ID: [to be assigned]")
P('Title: "Revisiting the Internationalisation–Performance Relationship in '
  'an Emerging Market: The Roles of Technological Capability and Digital '
  'Adoption"')
P("Journal: International Journal of Emerging Markets (Emerald)")
P("Submission round: Revised manuscript v5.8 (responding to v5.7 review)")
P("")
P("Dear Editor and Reviewer,")
P("")
P("We thank the Reviewer for the rigorous round-2 assessment, which "
  "engages directly with the methodological core of the paper. The "
  "revised manuscript v5.8 implements every actionable recommendation "
  "that is feasible within the harmonised World Bank Enterprise Survey "
  "(WBES) data scope for Vietnam (waves 2009 / 2015 / 2023). We map "
  "the four major weaknesses (W1–W4) and the four actionable "
  "recommendations (R1–R4) to the specific revisions below; section "
  "references are to v5.8.")
P("")

# ---------------------------------------------------------------------------
H1("Part A — Major Weaknesses")

# W1 ------------------------------------------------------------------------
H2("W1. Inverted-U claim conflicts with the zero-inflated FSTS distribution")
P("Reviewer comment.", italic=True)
Q('"Việc khẳng định có \'đường cong chữ U ngược\' là gây hiểu lầm '
  '(misleading). Thực chất, tác động lên năng suất được thúc đẩy bởi '
  '\'biên độ tham gia\' (participation margin), chứ không phải do sự '
  'đánh đổi chi phí phối hợp ở mức độ cường độ xuất khẩu cao."')
P("Our response.", bold=True)
P("We agree, and have re-framed H1 as a dual-mechanism hypothesis "
  "explicitly separating the participation margin from the intensity "
  "margin:")
P("• §2.1 now states H1 as: \"The internationalisation–performance "
  "relationship in Vietnam is non-monotonic and operates through two "
  "distinct margins. (H1a, participation margin) Crossing from "
  "non-exporting (FSTS = 0) to exporting (FSTS > 0) is positively "
  "associated with labour productivity, capturing the learning-and-"
  "scale jump at entry. (H1b, intensity margin) Within the exporter "
  "subsample, additional direct-export intensity exhibits diminishing "
  "or non-significant marginal returns, reflecting the binding "
  "coordination costs that emerge once participation has been "
  "crossed.\"")
P("• §2.1 also reports the zero-inflation explicitly: non-exporter "
  "shares of 71.6 % (2009), 79.3 % (2015), 81.2 % (2023) and pooled "
  "77.4 %, providing the empirical motivation for the dual-margin "
  "framing.")
P("• §4.4 (\"Main empirical pattern: participation × intensity\") "
  "now opens with the honest reading that the full-sample inverted-U "
  "is identified primarily through the participation margin: only "
  "~1.0 % of pooled firms sit within ±5 percentage-points of the "
  "wave-specific turning points (§4.5 density check), and the bulk "
  "of mass lies at FSTS = 0. The exporter-only sub-sample (Panel H) "
  "is now explicitly anchored in §4.4 rather than buried in the "
  "robustness section: pooled FSTS_c = −0.861 *** but FSTS_c² = "
  "−0.200 n.s., M8 joint p = .462 — i.e., H1a (participation margin) "
  "is the dominant productivity-relevant margin while H1b (within-"
  "exporter intensity curvature) does not survive once participation "
  "is netted out. The full-sample inverted-U is retained as the "
  "headline empirical regularity but read explicitly through the "
  "dual-mechanism lens.")
P("")

# W2 ------------------------------------------------------------------------
H2("W2. Endogeneity (reverse causality + omitted-variable bias) not addressed")
P("Reviewer comment.", italic=True)
Q('"Mô hình Heckman không giải quyết được rủi ro quan hệ nhân quả ngược '
  '(reverse causality) hay thiên lệch do biến bỏ sót (omitted variable '
  'bias) liên quan đến hai biến điều tiết TCI_z và DAI_z."')
P("Our response.", bold=True)
P("Valid. We have added three identification probes that go beyond the "
  "Heckman / control-function correction:")
P("• §4.5 Panel J — Propensity-score matching (PSM). Two binary "
  "treatments are matched on lnEmp, FirmAge, ForeignOwned, sector1 "
  "and wave fixed effects on the pooled sample, under both 1-NN "
  "(caliper 0.05) and Epanechnikov kernel matching (BW 0.06). The "
  "website-treatment ATT is 0.298 *** (1-NN) and 0.321 *** (kernel), "
  "matched N ≈ 1,085. The cert / foreign-tech-treatment ATT is "
  "0.637 *** (1-NN) and 0.609 *** (kernel), matched N ≈ 640. Both "
  "treatments produce sizeable, positive and algorithm-robust ATT "
  "estimates. Pre-match standardised mean differences and matched "
  "balance are reported in `table_psm_balance.csv`.")
P("• §4.5 Panel K — Two-stage least squares (2SLS) with leave-one-out "
  "industry × region instruments. We instrument DAI_z and TCI_z "
  "separately with the leave-one-out average c22b ownership (or "
  "average (b8 + e6) / 2 for TCI) within each sector1 × a2 × wave "
  "cell. First-stage F-statistics are 34.6 (DAI) and 22.1 (TCI), "
  "well above the Staiger–Stock weak-instrument threshold of 10. "
  "The 2SLS estimates are honest: instrumented TCI_z = 1.639 *** "
  "(SE 0.299) — the TCI direct effect is reinforced under "
  "instrumentation; instrumented DAI_z = 0.018 (p = .942) — the OLS-"
  "detected DAI direct effect attenuates to a null under "
  "instrumentation. We do not hide this attenuation; instead, §5.2 "
  "interprets it as evidence that website-based digital presence is "
  "more sensitive to selection-on-observables than is foreign-"
  "technology / standards capability.")
P("• §4.5 Oster (2019) δ-stability bounds. Under the canonical R²max "
  "= min(1, 1.3 × R²controlled) and δ = 1 (selection-on-unobservables "
  "= selection-on-observables), the implied focal coefficients are "
  "0.615 (FSTS_c), −1.174 (FSTS_c²), 0.194 (TCI_z) and 0.080 "
  "(DAI_z). None of the four implied coefficients changes sign or "
  "collapses to zero, so plausible selection on unobservables would "
  "have to be substantially larger than selection on observables to "
  "overturn the focal qualitative findings.")
P("• Language calibration: throughout §1, §3, §4 and §5 we have kept "
  "the associational framing of the OLS evidence and reserved "
  "stronger causal claims for the PSM / 2SLS panels, with each panel "
  "interpreted under its own identification assumption.")
P("")

# W3 ------------------------------------------------------------------------
H2("W3. DAI_z proxy obsolescence (website is \"table stakes\" by 2023)")
P("Reviewer comment.", italic=True)
Q('"Việc dùng một biến đã có dấu hiệu \'lỗi thời\' (như tác giả tự '
  'nhận ở phần 5.2.1) để làm trọng tâm đo lường sự điều tiết trong '
  'nền kinh tế số hiện nay là thiếu thuyết phục đối với IB scholars."')
P("Our response.", bold=True)
P("Valid. We have promoted the DAI_rich evidence from Panel B into "
  "the §5.2 Discussion as a substantive defence against the proxy-"
  "obsolescence reading:")
P("• §5.2 now reports that the DAI_rich extension available in 2023 "
  "(combining c22b with electronic-payment shares k33 and k38) "
  "produces a directionally identical and marginally significant "
  "moderation pattern (FSTS_c × DAI_rich_cont_z = −0.93, M8 joint "
  "p = .099). Whether digital adoption is measured by the thin "
  "Tier-1 website indicator or by the deeper Tier-2 / 3 transaction "
  "items, the 2023 moderation pattern goes in the same direction. "
  "This common-direction evidence guards against the proxy-"
  "obsolescence reading: even under a richer measurement that is "
  "harder to dismiss as a routine marker, the within-2023 "
  "moderation is consistent with the headline finding.")
P("• §5.2.1 (\"An alternative reading: proxy obsolescence\") is "
  "retained as an honest disclosure but is now positioned as one of "
  "two complementary readings, not as a stand-alone weakening of "
  "the construct.")
P("")

# W4 ------------------------------------------------------------------------
H2("W4. Stage-contingency framing is post-hoc and lacks macro evidence")
P("Reviewer comment.", italic=True)
Q('"Cách lý giải này không đi kèm với các kiểm định vĩ mô trực tiếp '
  'trong mô hình mà chỉ dựa vào phỏng đoán về bối cảnh… Điều này '
  'khiến lập luận H4 trở nên thiếu tính quy nạp chặt chẽ."')
P("Our response.", bold=True)
P("Valid. We have soft-framed H4 as an emerging pattern (already in "
  "v5.7) and added a macro-context paragraph in §5.3 that anchors "
  "the 2015 dip institutionally rather than purely post-hoc:")
P("• H4 is framed as exploratory: \"H4 (exploratory). The "
  "performance relevance of website-based digital presence (DAI_z) "
  "in Vietnam varies across stages of internationalisation; we "
  "treat the within-wave moderation as exploratory and concentrate "
  "the test on 2023, where the post-NDTP environment plausibly "
  "enables a moderation channel.\"")
P("• §4.5 Panel I (formal pooled wave × focal interaction test) "
  "confirms that only the DAI direct shifts are cross-wave-"
  "distinguishable; the FSTS curvature and the FSTS × DAI "
  "moderation cross-wave differences are not statistically "
  "separable.")
P("• §5.3 now adds public secondary indicators that make the 2015 "
  "dip institutionally plausible: World Bank WDI individuals-using-"
  "the-Internet share rose from ~26 % (2009) to ~45 % (2015) to "
  ">78 % (2023); ITU fixed-broadband subscriptions per 100 people "
  "from ~3 (2009) to ~8 (2015) to >20 (2023); Vietnam's National "
  "Digital Transformation Programme issued in 2020; cross-border "
  "e-payment platforms (VNPAY, MoMo, ZaloPay) and B2B exporter "
  "marketplaces reaching scale only after 2018–2019. We do not "
  "enter these as identifying variation — they are not in the "
  "regression — but they make the wave-specific reading "
  "institutionally plausible rather than purely post-hoc.")
P("")

# ---------------------------------------------------------------------------
H1("Part B — Actionable Recommendations")

H2("R1. Re-frame H1: participation × intensity (covered under W1)")
P("Implemented in §2.1, §4.4 and §5.1. See response to W1 above.")
P("")

H2("R2. Endogeneity robustness — PSM, IV / 2SLS, Oster bounds")
P("Implemented in §4.5 Panel J (PSM), §4.5 Panel K (IV / 2SLS) and "
  "§4.5 Oster bounds. See response to W2 above.")
P("New artefacts:")
P("• `table_3_robustness.csv` — Panel J and Panel K rows added")
P("• `table_psm_balance.csv` — covariate balance for the PSM panel")
P("• `table_oster_bounds.csv` — δ = 1 implied β under R²max = 1.3 × R²con")
P("")

H2("R3. Promote DAI_rich into the Discussion")
P("Implemented in §5.2 (covered under W3). The DAI_rich common-"
  "direction evidence is now part of the substantive narrative, not "
  "only a robustness panel.")
P("")

H2("R4. Soften stage-contingency + add macro context for the 2015 dip")
P("Implemented in §5.3 (covered under W4). The macro-indicator "
  "paragraph is reported as descriptive context, not as identifying "
  "variation.")
P("")

# ---------------------------------------------------------------------------
H1("Summary of new artefacts in v5.8")
P("• §2.1 H1 reformulated as dual-mechanism (H1a participation + H1b intensity)")
P("• §4.4 retitled \"Main empirical pattern: participation × intensity\" — "
  "Panel H (exporter-only) elevated into the main results narrative")
P("• §4.5 Panel J — PSM ATT for website and cert/foreign-tech treatments "
  "(1-NN + kernel matching, both p < .001)")
P("• §4.5 Panel K — IV / 2SLS with leave-one-out industry × region "
  "instruments (first-stage F = 34.6 / 22.1; instrumented TCI_z = 1.64 ***, "
  "instrumented DAI_z = 0.02 n.s.)")
P("• §4.5 Oster (2019) δ = 1 stability bounds — no sign change for any "
  "of the four focal coefficients")
P("• §5.2 — DAI_rich evidence promoted into substantive Discussion as a "
  "defence against the proxy-obsolescence reading")
P("• §5.3 — macro-context paragraph (WDI internet penetration, ITU "
  "broadband, Vietnam NDTP 2020, e-payment platforms) makes the 2015 "
  "dip institutionally plausible")
P("")
P("We thank the Reviewer once again for the substantive engagement. "
  "We believe v5.8 substantively addresses every actionable comment "
  "within the WBES data scope and is ready for re-evaluation.")
P("")
P("Sincerely,")
P("Do Thuy Huong (Author)")
P("Phan Anh Tu (Corresponding author)")
P("Can Tho University, Vietnam")

doc.save(str(OUT))
print(f"Wrote {OUT}")
