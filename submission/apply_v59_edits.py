"""
P4 Vietnam v5.8 -> v5.9 — Reviewer-driven clean-copy edits.

Triggered by reviewer review forwarded via NCS:
"Bản thảo này mạnh về ý tưởng và độ công phu, nhưng cần siết lại để
giảm overclaim ở H1, H4, ngôn ngữ về DAI moderation, và phân biệt rõ
'foundational digital adoption' (DAI_z = website-based) vs 'digital
capability' (theory-level construct)."

Applied 20 paragraph-level rewrites:

A. Abstract (4 blocks)
   1. Purpose: tighter framing, drop technical overload
   2. Design: drop Heckman/control-function/Paternoster details
   3. Findings: explicit dual-margin reading; quantitative TP range
   4. Originality: foreground "context-sensitive and wave-specific"

B. Theory (2 hypothesis rewrites)
   5. H1 (§2.1): dual-margin participation+intensity framing replacing
      "operates through two distinct margins" overclaim
   6. H4 (§2.4): tighter exploratory framing — "wave-specific" not
      "stage-contingent" structural moderation

C. Results (2 paragraph rewrites in §4.3)
   7. H1+H2+H3 reinterpretation: "qualified support" not "strongly
      supported"; explicit participation-margin caveat
   8. H4 reinterpretation: "limited exploratory support"; pooled wave x
      focal interaction does not detect cross-wave separability

D. Discussion (8 paragraph rewrites)
   9-10. §5.1 Reinterpreting digital capability: "foundational digital
         adoption" replaces "digital capability" where DAI_z is the
         referent
   11-13. §5.2 TCI/DAI matters: PSM/2SLS evidence sharpens construct
          distinction; closing take-away on identification-robustness
          vs context-sensitivity
   14-16. §5.3 2015 dip: "wave-specific compression" framing; explicit
          institutional-plausibility caveat ("not a formally identified
          explanation")

E. Limitations (2 paragraph rewrites)
   17. limitation 2: Tier-1-style proxy framing
   18. limitation 4: grammar fix + cross-wave evenness reframing

F. Conclusion (2 paragraph rewrites)
   19. §7 conclusion p1: dual-margin + non-monotonic framing
   20. §7 conclusion p2: TCI robust, DAI wave-sensitive, pooled averages
       conceal heterogeneity

Usage:
    pip install python-docx
    python3 apply_v59_edits.py

Inputs:
    submission/manuscript_blinded_FIXED.docx (= v5.8 + 7 prior fixes)
    submission/manuscript_full_with_authors_FIXED.docx

Outputs:
    submission/manuscript_v5_9_blinded.docx
    submission/manuscript_v5_9_full_with_authors.docx

Verification (run after):
    grep -c "H1 receives qualified support" -> 1
    grep -c "foundational digital adoption" -> >=8
    grep -c "operates through two distinct margins" -> 0
    grep -c "H1 is strongly supported" -> 0
"""
import shutil
from docx import Document


def replace_para_by_prefix(doc, prefix, new_text):
    """Find first body paragraph starting with `prefix` and replace its text."""
    for p in doc.paragraphs:
        if p.text.startswith(prefix):
            if p.runs:
                p.runs[0].text = new_text
                for run in p.runs[1:]:
                    run.text = ""
            else:
                p.add_run(new_text)
            return True
    return False


EDITS = [
    ("Purpose — This study revisits the internationalisation",
     "Purpose — This study revisits the internationalisation–performance relationship in an emerging market and examines how technological capability and foundational digital adoption are associated with firms' productivity under conditions of institutional and digital transition. Focusing on Vietnam, it asks whether export intensity is nonlinearly associated with labour productivity and whether technological capability and digital adoption play distinct roles across survey waves.",
     "Abstract Purpose"),

    ("Design/methodology/approach — The study uses three waves",
     "Design/methodology/approach — The study uses three waves of World Bank Enterprise Survey data for Vietnam (2009, 2015 and 2023; pooled N = 2,958) and estimates wave-specific and pooled OLS models with HC1 robust standard errors, quadratic export-intensity terms and interaction specifications. The analysis distinguishes a technological capability index based on internationally recognised quality certification and foreign-licensed technology from a foundational digital-adoption measure based on website presence, with no shared items between the two constructs. Supplementary checks assess the stability of the main findings.",
     "Abstract Design"),

    ("Findings — The internationalisation–performance relationship is robustly nonlinear",
     "Findings — The internationalisation–performance relationship is robustly nonlinear in the full sample, with turning points clustered around 39–46 per cent of direct-export intensity. Technological capability is positively associated with productivity in all three waves and in the pooled sample, and its moderating role is more stable than that of digital adoption. Foundational digital adoption is positive in 2009 and 2023, null in 2015, and only shows within-sample detectable moderation in 2023. The full-sample inverted-U is best interpreted through a participation-and-intensity structure, because the curvature weakens substantially in exporter-only models.",
     "Abstract Findings"),

    ("Originality/value — The study contributes to research on emerging markets",
     "Originality/value — The study contributes to research on emerging markets by distinguishing foreign-technology/standards capability from foundational digital adoption and by showing that pooled digital effects can mask substantial temporal heterogeneity. The findings suggest that the productivity relevance of basic digital adoption is context-sensitive and wave-specific rather than uniformly stable across stages of internationalisation.",
     "Abstract Originality"),

    ("H1. The internationalisation–performance relationship in Vietnam is non-monotonic and operates through two distinct margins",
     "H1. In Vietnam, the internationalisation–performance relationship is non-monotonic in the full sample and is best understood through a participation-and-intensity structure in which the productivity-relevant contrast is strongest between non-exporters and exporters, while additional export intensity within the exporter subsample yields weaker, diminishing, or non-significant marginal returns. (H1a, participation margin) Crossing from non-exporting (FSTS = 0) to exporting (FSTS > 0) is positively associated with labour productivity. (H1b, intensity margin) Within the exporter subsample, additional direct-export intensity is expected to yield weaker, diminishing, or non-significant marginal returns relative to the participation margin.",
     "H1"),

    ("H4 (exploratory). The performance relevance of website-based digital presence",
     "H4 (exploratory). The productivity relevance of foundational digital adoption varies across phases of internationalisation and institutional transition. Any moderation of the export-intensity curve by digital adoption is therefore expected to be wave-specific rather than uniformly present across periods, with the strongest within-sample detectability anticipated in 2023.",
     "H4"),

    ("H1 is strongly supported. The Lind–Mehlum test rejects the monotonicity null",
     "H1 receives qualified support. The Lind–Mehlum test rejects the monotonicity null in all three waves and in the pooled sample, and the implied turning points are tightly clustered within a relatively narrow range. At the same time, exporter-only models show that this curvature weakens substantially once the participation margin is netted out. The most defensible interpretation is therefore that the full-sample inverted-U reflects a combined participation-and-intensity structure, with the productivity-relevant contrast concentrated primarily at the transition from non-exporting to exporting rather than in strong within-exporter curvature alone. "
     "H2 is supported by the positive TCI_z association in the pooled sample and in all three wave-specific periods, reinforced by moderation evidence that is statistically distinguishable in three of four panels. Across specifications, technological capability behaves as the more stable capability channel in the Vietnamese setting. "
     "H3 is supported on average but not uniformly across waves. In pooled models, DAI_z is positively associated with labour productivity, but wave-specific estimates show that this association is strong in 2009, absent in 2015 and re-emerges in 2023. The Paternoster cross-wave z-tests confirm that the 2009-to-2015 decline and the 2015-to-2023 recovery in the DAI_z direct association are statistically distinguishable shifts.",
     "§4.3 H1+H2+H3"),

    ("H4 receives exploratory support concentrated in the 2023 wave",
     "H4 receives limited exploratory support. The moderation pattern involving DAI_z is only within-sample detectable in 2023 and remains marginal at the joint-test level. We therefore interpret the evidence as suggestive of wave-specific conditionality rather than as confirmation of a stable cross-wave moderation pattern. This reading is reinforced by the pooled wave × focal interaction test, which does not detect statistically separable cross-wave differences in the FSTS × DAI moderation terms.",
     "§4.3 H4"),

    ("The central implication of the findings is that digital capability in Vietnam should not be interpreted",
     "The central implication of the findings is that foundational digital adoption in Vietnam should not be interpreted as a universal and temporally stable productivity premium. Although both TCI_z and DAI_z are positive on average in pooled specifications, their empirical roles differ materially across waves and across identification strategies. This means that digitalisation is not simply a constant background advantage. Rather, the productivity relevance of basic digital adoption is context-sensitive and wave-specific within a broader process of internationalisation and transition (Vahlne, 2020; Stallkamp and Schotter, 2021).",
     "§5.1 para1"),

    ("This interpretation helps reconcile the coexistence of positive pooled effects and uneven wave-specific results",
     "This interpretation helps reconcile the coexistence of positive pooled effects and uneven wave-specific results. The pooled model captures the average tendency for stronger capability to be associated with better performance. The wave-specific models show that this tendency is not equally strong in every phase. The value of foundational digital adoption therefore depends on where firms stand in the broader lifecycle of internationalisation and transition.",
     "§5.1 para2"),

    ("The results strengthen the theoretical case for separating foreign-technology / standards capability",
     "The results strengthen the theoretical case for separating foreign-technology/standards capability from website-based digital presence. The PSM and IV evidence in §4.5 (Panels J and K) makes the distinction sharper (Karna et al., 2016). TCI is robust under both matching and instrumentation: the 2SLS estimate of TCI_z remains large and statistically distinguishable under a strong instrument, and the matching ATT for the certification/foreign-technology treatment is also positive and sizeable. By contrast, the OLS-detected DAI direct association is reproduced under PSM but attenuates to a null under 2SLS. The two constructs therefore identify different productivity channels: foreign-technology/standards exposure survives both selection-on-observables and selection-on-unobservables probes, whereas website-based digital presence is more sensitive to the IV-implied exogenous variation.",
     "§5.2 para1"),

    ("The DAI_rich extension reported in §4.5 Panel B reinforces the construct interpretation",
     "The DAI_rich extension reported in §4.5 Panel B reinforces the construct interpretation rather than weakening it. Although the primary DAI_z anchored on c22b (website presence) is by 2023 close to a Tier-1 baseline indicator, the DAI_rich extension available only in 2023 — combining c22b with electronic-payment shares (k33, k38) — produces a similarly directed and marginal moderation pattern. Whether digital adoption is measured by the thin website indicator or by richer transaction-enabling items, the 2023 moderation pattern goes in the same direction. This common-direction evidence guards against a purely proxy-obsolescence reading of the 2023 result.",
     "§5.2 para2"),

    ("The difference between TCI and DAI matters because the two constructs do not behave identically",
     "Taken together, the results suggest that foreign-technology/standards capability behaves like a more identification-robust productivity channel, whereas foundational digital adoption behaves like a more context-sensitive and selection-sensitive marker of performance heterogeneity. These two domains should therefore not be collapsed into a single \"digital capability\" label.",
     "§5.2 para3"),

    ("The 2015 pattern is especially revealing. It shows that even when the nonlinear",
     "The 2015 pattern is especially revealing. It is best interpreted not as an anomaly, but as a wave-specific compression of the foundational digital-adoption channel under transitional infrastructure conditions. Even when the nonlinear I–P structure becomes clearer, the direct payoff from website-based digital presence can compress to a null, suggesting a phase in which export expansion remains productivity-relevant while the contribution of basic digital adoption becomes more difficult to realise or detect within-sample.",
     "§5.3 para1"),

    ("We treat the 2015 compression honestly as a wave-specific association consistent with stage contingency",
     "We treat the 2015 compression honestly as a wave-specific association consistent with stage contingency rather than as a fully cross-wave-identified structural shift. As reported in §4.5 Panel I, the formal pooled wave × focal interaction test detects only the DAI direct shifts as cross-wave-distinguishable; the FSTS curvature and the FSTS × DAI moderation cross-wave differences are not statistically separable. Public secondary indicators are consistent with a digital-infrastructure trough in 2015 relative to the 2009 and 2023 anchors. The 2015 wave therefore appears to capture Vietnamese exporters during a transitional infrastructure phase in which a website could not yet plug into a transaction-supporting digital ecosystem, whereas the 2023 wave observes them after the post-NDTP scaffolding had matured. This reading is institutionally plausible, but it should not be treated as a formally identified explanation of the coefficient pattern.",
     "§5.3 para2"),

    ("Rather than treating this wave as an anomaly, it is more useful to interpret it as evidence",
     "Rather than treating this wave as an anomaly, it is more useful to interpret it as evidence of wave-specific heterogeneity that is consistent with stage contingency. The dip demonstrates why pooled averages alone are insufficient. Without the wave-specific analysis, one would miss the possibility that capability payoffs compress or fade temporarily before re-emerging in a later phase, even when the curvature parameters of the I–P relationship themselves remain statistically indistinguishable across waves.",
     "§5.3 para3"),

    ("Second, the DAI_z composite captures a foundational layer of digital adoption",
     "Second, DAI_z captures only a foundational, Tier-1-style layer of digital adoption centred on website presence, rather than digitally integrated organisational capability. Although the 2023 DAI_rich extension points in the same direction, richer cross-wave measures would be needed to test whether deeper digital integration exhibits a more stable productivity channel.",
     "§6 limit2"),

    ("Fourth, although the Paternoster (1998) z-tests reported in §4.5 confirm",
     "Fourth, the cross-wave evidence is uneven in statistical strength. The Paternoster (1998) z-tests confirm that the DAI_z drop between 2009 and 2015 and its recovery between 2015 and 2023 are statistically distinguishable, but most other cross-wave coefficient differences are not. The lifecycle interpretation therefore rests primarily on the directional consistency of the wave-specific estimates and on the concentration of the digital signal in 2023, rather than on uniformly significant pairwise coefficient differences across all focal terms. Future work could exploit policy timing — for example, Vietnam's National Digital Transformation Programme launched in 2020 — for sharper identification of the digital channel through a policy-evaluation design rather than a cross-wave comparison.",
     "§6 limit4"),

    ("This study revisits the I–P relationship in Vietnam by distinguishing technological capability",
     "This study revisits the internationalisation–performance relationship in Vietnam by distinguishing foreign-technology/standards capability from foundational digital adoption and by comparing pooled with wave-specific evidence. The findings show that the internationalisation–performance relationship is non-monotonic in the full sample, but that this pattern is driven primarily by a participation-and-intensity structure rather than by strong within-exporter curvature alone.",
     "§7 conclusion p1"),

    ("The central theoretical implication is that digital capability in a transitional economy is best understood",
     "The results also show that the two capability domains should not be treated as interchangeable. Technological capability is comparatively stable and identification-robust across specifications, whereas foundational digital adoption is more wave-sensitive and only exhibits within-sample detectable moderation in 2023. The broader implication is that the productivity relevance of basic digital adoption in a transitional economy is real but uneven, and that pooled averages can conceal important temporal heterogeneity in when and how digital adoption matters.",
     "§7 conclusion p2"),
]


if __name__ == '__main__':
    for kind in ['blinded', 'full_with_authors']:
        SRC = f'submission/manuscript_{kind}_FIXED.docx'
        DST = f'submission/manuscript_v5_9_{kind}.docx'
        shutil.copy(SRC, DST)
        doc = Document(DST)

        print(f'=== {kind} ===')
        applied = 0
        for prefix, new_text, label in EDITS:
            if replace_para_by_prefix(doc, prefix, new_text):
                applied += 1
                print(f'  ✓ {label}')
            else:
                print(f'  ✗ {label}: NOT FOUND')

        doc.save(DST)
        print(f'  Total: {applied}/{len(EDITS)} edits → {DST}')
        print()
