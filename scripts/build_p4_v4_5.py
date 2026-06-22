"""Build manuscript_v4_5.docx for the P4 Vietnam paper.

Sources:
  - 68924fe1 md draft (citation-rich) is the authoritative content template.
  - v4.4 docx supplies the variable-label and methodology language conventions.

Run from repo root:
    python3 scripts/build_p4_v4_5.py
"""
from __future__ import annotations

from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

TEMPLATE = Path(
    "/root/.claude/uploads/baf64a94-2e13-4dbf-8dcc-22587a547e56/"
    "1f16255e-manuscript_v4_4_1.docx"
)
import os

BLINDED = os.environ.get("BLINDED", "0") == "1"
OUTPUT = (
    Path(__file__).resolve().parents[1] / "manuscript_blinded.docx"
    if BLINDED
    else Path(__file__).resolve().parents[1] / "manuscript_v4_5.docx"
)

# The pandoc-generated v4.4 template stores style names with capitalised first
# letter (e.g. "Heading 1"), but python-docx's BabelFish.ui2internal lowercases
# them before lookup ("heading 1") and then fails. We bypass python-docx's
# lookup by writing pStyle directly using the styleId stored in styles.xml.
STYLE_ID = {
    "Heading 1": "Heading1",
    "Heading 2": "Heading2",
    "Heading 3": "Heading3",
    "Title": "Title",
    "Subtitle": "Subtitle",
    "Date": "Date",
    "First Paragraph": "FirstParagraph",
    "Body Text": "BodyText",
    "Block Text": "BlockText",
    "Abstract": "Abstract",
    "Abstract Title": "AbstractTitle",
    "Bibliography": "Bibliography",
    "Compact": "Compact",
    "Author": "Author",
}

H1 = "Heading 1"
H2 = "Heading 2"
H3 = "Heading 3"
FP = "First Paragraph"
BT = "Body Text"
BX = "Block Text"


def add_para(document, text, style_name):
    """Append a paragraph and assign style by writing pStyle directly."""
    para = document.add_paragraph(text)
    style_id = STYLE_ID[style_name]
    pPr = para._p.get_or_add_pPr()
    pStyle = pPr.find(qn("w:pStyle"))
    if pStyle is None:
        pStyle = OxmlElement("w:pStyle")
        pPr.insert(0, pStyle)
    pStyle.set(qn("w:val"), style_id)
    return para

# Load v4.4 as a styling template, then strip all body content so we keep
# its style definitions but rebuild the manuscript from scratch.
doc = Document(str(TEMPLATE))
body = doc.element.body
# Remove every direct child except the final sectPr (page setup).
for child in list(body):
    if child.tag.endswith("}sectPr"):
        continue
    body.remove(child)
# Drop the single legacy table that lived in v4.4 (already removed above by the
# generic clear, but guard against future python-docx caching of doc.tables).
for tbl in list(doc.tables):
    tbl._element.getparent().remove(tbl._element)

# Front matter -----------------------------------------------------------------
add_para(doc,
    "Revisiting the Internationalisation–Performance Relationship in an "
    "Emerging Market: The Roles of Technological Capability and Digital "
    "Adoption", "Title")
add_para(doc,
    ("v5.8 — IJoEM blinded manuscript: round-2 revision (H1 dual-mechanism, PSM Panel J, IV/2SLS Panel K, Oster bounds, macro-context §5.3)" if BLINDED
     else "v5.8 — IJoEM submission draft: round-2 revision (H1 dual-mechanism, PSM Panel J, IV/2SLS Panel K, Oster bounds, macro-context §5.3)"),
    "Subtitle")
add_para(doc, "2026-05-02", "Date")

if not BLINDED:
    add_para(doc, "Do Thuy Huong", "Author")
    add_para(doc,
        "PhD Candidate, College of Economics, Can Tho University, Can Tho, Vietnam. "
        "E-mail: huongp1323001@gstudent.ctu.edu.vn. "
        "ORCID: https://orcid.org/0000-0002-7711-2487.", BT)
    add_para(doc, "Phan Anh Tu (corresponding author)", "Author")
    add_para(doc,
        "School of Economics (International Business), Can Tho University, Can Tho, "
        "Vietnam. E-mail: patu@ctu.edu.vn. "
        "ORCID: https://orcid.org/0000-0003-0667-3137.", BT)
add_para(doc,
    "Manuscript classification: research article. "
    "Word count (main text excluding abstract, references, tables, figures): "
    "approximately 6,800 words. Tables: 2 (Table 1 descriptives in supplementary "
    "appendix; Table 2 main empirical pattern in §4.4). Figures: 2 (conceptual "
    "model and predicted I–P curves).", BT)

# Abstract ---------------------------------------------------------------------
add_para(doc, "Abstract", H1)
add_para(doc,
    "Purpose — This study revisits the internationalisation–performance "
    "relationship in an emerging market and examines how technological "
    "capability and digital adoption shape firms’ productivity outcomes under "
    "conditions of institutional and digital transition. Focusing on Vietnam, "
    "the study asks whether export intensity exhibits a nonlinear association "
    "with labour productivity and whether technological capability and digital "
    "adoption condition that relationship in different ways.", FP)
add_para(doc,
    "Design/methodology/approach — The study uses three waves of World Bank "
    "Enterprise Survey microdata for Vietnam (2009, 2015 and 2023; analytic "
    "N = 989, 956 and 1,013, pooled 2,958) and estimates ordinary least "
    "squares models with HC1 robust standard errors, quadratic export-intensity "
    "terms and interaction specifications. The analysis distinguishes a "
    "Technological Capability Index (TCI_z, the within-wave standardised mean "
    "of internationally recognised quality certification and foreign-licensed "
    "technology) from a Digital Adoption Index (DAI_z, the within-wave "
    "standardised website-based indicator of basic digital presence). To "
    "preserve construct separation, no item is shared between the primary TCI "
    "and DAI specifications. Lind–Mehlum (Lind and Mehlum, 2010) curvature tests, Heckman two-step and "
    "control-function selection corrections, Paternoster (1998) cross-wave "
    "z-tests and richer measurement panels (TCI_full, DAI_rich, micro-firm "
    "exclusion, common-N) complement the baseline.", BT)
add_para(doc,
    "Findings — The internationalisation–performance relationship is robustly "
    "nonlinear: the Lind–Mehlum test rejects monotonicity in all three waves "
    "(2009 p = .006, 2015 p = .009, 2023 p = .013) and in the pooled sample "
    "(p < .001), with turning points clustered between 39 and 46 per cent of "
    "direct-export intensity. Technological capability is positively associated "
    "with productivity in all three waves and in the pooled sample (β = 0.215, "
    "0.128, 0.123 and 0.179, all p ≤ .010), and moderates the curvature in "
    "three of four panels (M3 joint p = .040, .713, .027 and .003). Digital "
    "adoption is positive in 2009 (β = 0.175, p < .001), null in 2015 "
    "(β = −0.044, p = .377), positive in 2023 (β = 0.095, p = .038) and "
    "positive in the pooled sample (β = 0.078, p = .004); its moderation "
    "channel emerges most clearly in 2023 (FSTS_c × DAI_z = −0.912, p = .043; "
    "M8 joint p = .062, marginal). Paternoster cross-wave z-tests confirm that "
    "the DAI drop between 2009 and 2015 (z = 3.353, p < .001) and the DAI "
    "re-emergence between 2015 and 2023 (z = −2.051, p = .040) are "
    "statistically distinguishable shifts.", BT)
add_para(doc,
    "Originality/value — The study contributes to research on emerging markets "
    "by showing that the productivity returns to internationalisation depend "
    "not only on export intensity but also on how firms combine foreign-"
    "technology / standards capability with foundational website-based "
    "digital adoption under transitional institutional conditions. It also "
    "offers a cleaner measurement strategy by separating these two domains "
    "with no shared items, and shows that the wave-specific pattern of "
    "digital moderation is consistent with stage contingency, with detectable "
    "moderation concentrated in 2023.", BT)
add_para(doc,
    "Keywords: internationalisation–performance; emerging markets; digital "
    "adoption; technological capability; Vietnam; firm productivity.", BT)
add_para(doc,
    "JEL classification: F23 (multinational firms; international business); "
    "O33 (technological change: choices and consequences); D22 (firm "
    "behaviour: empirical analysis); L25 (firm performance); O53 (economywide "
    "country studies — Asia).", BT)
add_para(doc,
    "Paper type: Research paper.", BT)

# Highlights (Elsevier-style) --------------------------------------------------
add_para(doc, "Highlights", H1)
add_para(doc,
    "• The internationalisation–performance relationship in Vietnamese firms "
    "is robustly nonlinear: the Lind–Mehlum test rejects monotonicity in all "
    "three waves (2009 p = .006, 2015 p = .009, 2023 p = .013) and in the "
    "pooled sample (p < .001), with turning points clustered between 39 and "
    "46 % of direct-export intensity.", FP)

add_para(doc,
    "• Technological capability and digital adoption are separated as "
    "non-overlapping primary measures: TCI_z is the within-wave standardised "
    "mean of quality certification and foreign-licensed technology, whereas "
    "DAI_z is the within-wave standardised website-based digital-presence "
    "indicator.", BT)
add_para(doc,
    "• TCI_z is positively associated with productivity in all three waves "
    "(β = 0.215, 0.128, 0.123) and pooled (β = 0.179, p < .001), and "
    "moderates the curvature in three of four panels (M3 joint p = .040, "
    ".713, .027 and .003).", BT)
add_para(doc,
    "• DAI_z is strongest in 2009 (β = 0.175, p < .001), null in 2015 "
    "(β = −0.044, p = .377), positive in 2023 (β = 0.095, p = .038) and "
    "pooled (β = 0.078, p = .004); the cross-wave shifts are statistically "
    "distinguishable (Paternoster z = 3.353 between 2009 and 2015; "
    "z = −2.051 between 2015 and 2023).", BT)
add_para(doc,
    "• DAI moderation is concentrated in 2023, where FSTS_c × DAI_z = −0.912 "
    "(p = .043) and the M8 joint test is marginal (p = .062); the pooled M8 "
    "joint test is also marginal (p = .083), driven by 2023 rather than by a "
    "stable cross-period moderation.", BT)

# 1. Introduction --------------------------------------------------------------
add_para(doc, "1. Introduction", H1)

add_para(doc, "1.1 Background and motivation", H2)
add_para(doc, 
    "Vietnam offers an analytically valuable setting for revisiting the "
    "internationalisation–performance (I–P) relationship because firms expand abroad "
    "under conditions of institutional transition, uneven capability accumulation, and "
    "rapidly changing digital infrastructure. In such settings, internationalisation "
    "should not be assumed to generate a simple linear performance premium. Firms may "
    "gain access to larger markets, benefit from learning, and diversify revenue "
    "streams, but they may also face rising coordination costs, information-processing "
    "burdens, and organisational strain as their foreign involvement deepens "
    "(Wright et al., 2005; Cuervo-Cazurra and Genc, 2008; Wu et al., 2016).", FP)
add_para(doc, 
    "This tension lies at the heart of the I–P literature. A long tradition of research "
    "has argued that internationalisation can improve performance at lower and "
    "intermediate levels through scale, learning, and diversification, while also "
    "generating diminishing or negative returns at higher levels because of complexity "
    "and coordination burdens. Meta-analytic evidence strongly supports the view that "
    "nonlinearity is a central feature of this relationship rather than an empirical "
    "anomaly (Vernon, 1979; Lu and Beamish, 2004; Hennart, 2007; Coviello et al., 2017; Marano et al., 2016).", BT)
add_para(doc, 
    "Digitalisation adds a further layer of complexity to this debate. Digital tools "
    "can reduce communication frictions, accelerate transactions, and support "
    "coordination across borders. Yet those benefits do not arise automatically. Their "
    "realised value depends on whether firms possess the organisational depth, "
    "absorptive capacity, and complementary routines needed to translate digital "
    "adoption into productivity gains (Cohen and Levinthal, 1990; Vial, 2019; Verhoef et al., 2021). "
    "For this reason, digital capability should not be treated as a universally "
    "beneficial resource whose payoff is constant across firms and over time.", BT)
add_para(doc, 
    "The Vietnamese setting makes this issue especially important. Because firms are "
    "embedded in an economy undergoing capability upgrading and digital transition, "
    "both the benefits of internationalisation and the payoff from digitalisation may "
    "vary across stages of development. This raises a central question for the present "
    "study: does digital capability in Vietnam function as a stable "
    "performance-enhancing asset, or does it operate as a stage-contingent resource "
    "whose value changes over the lifecycle of internationalisation?", BT)
add_para(doc,
    "Three institutional turning points shape the observation window. Vietnam acceded "
    "to the World Trade Organization in early 2007, which opened the period preceding "
    "the 2009 wave and converted a domestically oriented exporter cohort into one with "
    "broader market exposure but limited absorptive infrastructure. The 2015 wave "
    "captures the middle of a second phase, in which expanding manufacturing exports "
    "coexisted with under-developed digital trade infrastructure, weak cross-border "
    "logistics integration, and an exporter cohort still concentrated in "
    "labour-intensive segments. The 2023 wave follows the launch of the National "
    "Digital Transformation Programme in 2020, the rapid expansion of cross-border "
    "e-payment and e-commerce platforms, and the rebalancing of foreign direct "
    "investment toward digitally-mediated and services-linked production. The three "
    "waves therefore observe firms under structurally different combinations of "
    "internationalisation pressure and digital infrastructure availability, which is "
    "what makes the lifecycle reading testable rather than purely conceptual.", BT)
add_para(doc,
    "These shifts are not cosmetic. The composition of the exporter cohort itself "
    "evolves across the three waves: the share of firms reporting any positive "
    "direct-export intensity declines as services and FDI-linked supply-chain firms "
    "enter the sample, while the average level of foundational digital adoption rises "
    "with the diffusion of websites, electronic payment systems, and digital "
    "transaction interfaces. Reading the I–P relationship and the digital-adoption "
    "channel as fixed structural facts across this fourteen-year window misses the "
    "fact that the underlying firm population, the binding coordination costs, and "
    "the institutional scaffolding for cross-border trade all change materially.", BT)

add_para(doc, "1.2 Research gap", H2)
add_para(doc, 
    "Three gaps motivate this study. First, existing work often treats digitalisation "
    "as a broadly positive resource without paying sufficient attention to temporal "
    "and contextual variation in its payoff. Such a treatment risks implying that "
    "digital adoption produces a relatively stable performance premium across firms "
    "and across stages of economic transition. In reality, digitalisation may generate "
    "uneven returns because firms differ in scale, routines, and complementary "
    "capability.", FP)
add_para(doc, 
    "Second, the distinction between technological capability and digital adoption "
    "remains underdeveloped. Technological capability refers to deeper firm-internal "
    "stocks of learning, problem-solving, process improvement, and innovation capacity "
    "(Lall, 1992). Foundational digital adoption, by contrast, reflects a more basic "
    "layer of digital readiness and digitally enabled interfaces or transaction "
    "mechanisms (Bharadwaj et al., 2013; Verhoef et al., 2021; Hanelt et al., 2021). Although these "
    "constructs are related, they should not be treated as interchangeable. Collapsing "
    "them into a single umbrella variable can reduce construct clarity and blur the "
    "mechanisms linking digitalisation to performance.", BT)
add_para(doc, 
    "Third, pooled estimates may obscure substantial lifecycle heterogeneity. In a "
    "setting such as Vietnam, where firms and institutions pass through distinct "
    "stages of transition, the role of internationalisation, technological capability, "
    "and digital adoption may vary considerably across survey waves. A pooled model is "
    "useful for identifying average effects, but it is insufficient if the underlying "
    "relationships shift across time. A design that combines pooled and wave-specific "
    "analysis is therefore necessary to determine whether the observed effects are "
    "stable or stage contingent.", BT)

add_para(doc, "1.3 Contribution", H2)
add_para(doc, 
    "This study makes three contributions to the literature. First, it refines the I–P "
    "debate by showing that the Vietnamese evidence supports a nonlinear relationship, "
    "but that the salience and visibility of that relationship vary across time. "
    "Rather than treating nonlinearity as a fixed structural fact that appears "
    "identically in every period, the analysis shows that the I–P curve must be read "
    "in conjunction with the broader capability environment.", FP)
add_para(doc, 
    "Second, the study improves construct validity by separating technological "
    "capability from foundational digital adoption. This distinction matters "
    "theoretically because deeper capability stocks and basic digital enablement may "
    "generate performance through different channels. It also matters empirically "
    "because the two constructs do not exhibit identical patterns across the "
    "Vietnamese waves.", BT)
add_para(doc, 
    "Third, the study introduces a lifecycle interpretation of digital "
    "internationalisation. The evidence suggests that digital capability is neither a "
    "universally stable premium nor a uniformly ineffective resource. Instead, it is "
    "an uneven and stage-dependent source of performance heterogeneity. This "
    "perspective helps explain why pooled average effects may coexist with "
    "substantial wave-specific differences.", BT)

add_para(doc, "1.4 Roadmap", H2)
add_para(doc, 
    "The remainder of the paper is organised as follows. Section 2 develops the "
    "theoretical framework and hypotheses. Section 3 describes the data, variables, "
    "and empirical strategy. Section 4 presents the results. Section 5 discusses the "
    "theoretical and managerial implications. Section 6 concludes.", FP)

# 2. Theory and hypotheses -----------------------------------------------------
add_para(doc, "2. Theory and hypotheses", H1)

add_para(doc, "2.1 Internationalisation and firm performance", H2)
add_para(doc, 
    "The relationship between internationalisation and firm performance is unlikely to "
    "be linear in a transitional economy such as Vietnam. Foreign expansion can "
    "improve performance through greater market reach, diversification, and learning "
    "from external environments. Firms may use internationalisation to spread fixed "
    "costs, access new customers, and acquire knowledge that supports operational "
    "improvement.", FP)
add_para(doc, 
    "At the same time, deeper international involvement often generates coordination "
    "costs and organisational burdens. Firms must manage multiple markets, reconcile "
    "diverse customer demands, process more information, and sustain greater "
    "managerial control. As foreign expansion intensifies, these costs may grow faster "
    "than the benefits, producing diminishing returns or even a decline in "
    "performance. This basic logic underpins the classic nonlinear view of the I–P "
    "relationship (Marano et al., 2016).", BT)
add_para(doc, 
    "This argument is especially plausible in Vietnam because firms operate under "
    "uneven capability conditions. Some firms may convert foreign expansion into "
    "learning and scale advantages, whereas others may encounter organisational strain "
    "sooner. The relevant expectation is therefore not a uniformly positive slope, "
    "but a nonlinear relationship in which gains from internationalisation become "
    "progressively more difficult to sustain.", BT)
add_para(doc,
    "Two opposing forces underpin the curvature. On the upside, "
    "increasing direct-export intensity creates scale economies, "
    "knowledge spillovers from foreign customers, and learning-by-"
    "exporting effects that lift productivity (Wagner, 2007). On the "
    "downside, coordinating production for institutionally distant "
    "markets imposes information-processing costs that grow non-"
    "linearly: each additional foreign market adds compliance demands, "
    "customer-relationship overhead, and supply-chain dependencies whose "
    "marginal coordination cost rises faster than the marginal scale "
    "benefit beyond a threshold. In a transitional setting where ports, "
    "trade-finance institutions, digital marketplaces, and dispute-"
    "resolution mechanisms are still maturing, this threshold may bind "
    "at a lower level of export intensity than in mature economies, "
    "sharpening the curvature relative to the meta-analytic baseline "
    "(Hennart, 2007; Wagner, 2007; Marano et al., 2016).", BT)
add_para(doc,
    "A second consideration arises from the structure of direct-export "
    "intensity in WBES Vietnam: the FSTS variable is bounded at zero "
    "and is heavily zero-inflated (the non-exporter share is 71.6 % in "
    "2009, 79.3 % in 2015 and 81.2 % in 2023; pooled 77.4 %). The "
    "internationalisation–performance relationship therefore comprises "
    "two analytically distinct margins. The participation margin is the "
    "step from FSTS = 0 to FSTS > 0, where firms cross the entry "
    "threshold into international markets and absorb fixed entry costs. "
    "The intensity margin is the variation of FSTS within the exporter "
    "subsample. Theory predicts that productivity gains can accrue at "
    "either margin: the participation margin captures learning-by-"
    "exporting and exposure to foreign-market demand; the intensity "
    "margin captures scale economies on the upside and coordination "
    "burdens on the downside (Bernard et al., 2007; Wagner, 2007). In "
    "transitional economies with thin export infrastructure, the "
    "participation margin is plausibly the dominant productivity-"
    "enhancing margin, while the intensity margin may show diminishing "
    "or null returns once participation has been crossed.", BT)
add_para(doc,
    "H1. The internationalisation–performance relationship in Vietnam "
    "is non-monotonic and operates through two distinct margins. "
    "(H1a, participation margin) Crossing from non-exporting "
    "(FSTS = 0) to exporting (FSTS > 0) is positively associated with "
    "labour productivity, capturing the learning-and-scale jump at "
    "entry. (H1b, intensity margin) Within the exporter subsample, "
    "additional direct-export intensity exhibits diminishing or non-"
    "significant marginal returns, reflecting the binding coordination "
    "costs that emerge once participation has been crossed.", BX)

add_para(doc, "2.2 Foreign-technology and standards capability and firm performance", H2)
add_para(doc,
    "Following the Lall (1992) tradition for emerging-market firms, this paper uses "
    "a measurement-tight reading of technological capability: a foreign-technology "
    "and standards capability that captures a firm's exposure to externally "
    "validated technological inputs — internationally recognised quality "
    "certification and foreign-licensed technology. This is one observable "
    "facet of the broader Cohen-Levinthal (1990) absorptive-capacity construct "
    "and the dynamic-capability construct of Teece (2007), but the present "
    "measure does not claim to identify the full absorptive-capacity stock; it "
    "captures the externally facing component of that stock. In international "
    "settings, this externally facing capability is particularly important "
    "because firms must respond to unfamiliar markets, meet foreign quality "
    "standards, and integrate externally licensed technology into "
    "organisational routines.", FP)
add_para(doc,
    "A firm with stronger foreign-technology / standards capability is more "
    "likely to transform international exposure into productivity gains. It "
    "can adjust products and processes to meet foreign requirements more "
    "effectively, integrate licensed foreign technology into production, and "
    "cope better with the operational demands created by export activity. "
    "Even when this capability does not fundamentally alter the curvature of "
    "the I–P relationship, it should improve the firm's overall performance "
    "level by raising the productivity floor among exposed firms.", BT)
add_para(doc,
    "This implies a positive direct association between foreign-technology / "
    "standards capability and firm performance in Vietnam. We treat it here "
    "as a construct that should raise the firm's capacity to benefit from "
    "internationalisation and should also support productivity more broadly, "
    "without assuming that it indexes the full innovation-and-R&D dimension.", BT)
add_para(doc,
    "Operationally, the primary TCI_z is built from two items: internationally "
    "recognised quality certification (b8) and foreign-licensed technology "
    "(e6). These items measure exposure to foreign-technology and standards "
    "channels rather than internal R&D effort or patent activity. A broader "
    "innovation-augmented composite (TCI_full, adding product innovation h1 "
    "and R&D activity h8) is reported in §4.5 Panel A as a boundary condition: "
    "if direct effects attenuate when innovation items are added, this "
    "indicates that the primary measure is informative specifically about the "
    "foreign-technology / standards channel, not the broader absorptive-"
    "capacity stock.", BT)
add_para(doc,
    "H2. Foreign-technology / standards capability (TCI_z) is positively "
    "associated with firm performance in Vietnam.", BX)

add_para(doc, "2.3 Website-based digital presence and firm performance", H2)
add_para(doc,
    "The primary DAI_z used in this paper is a website-based digital "
    "presence measure: a binary indicator of whether the firm has its own "
    "website. This is a foundational and cross-wave-comparable marker of "
    "digital adoption — it does not measure transaction-level digital "
    "integration, electronic payment infrastructure, or digital "
    "transformation in the Bharadwaj et al. (2013) / Verhoef et al. (2021) / "
    "Vial (2019) sense. We use it here precisely because it is the only "
    "digital indicator the WBES instrument carries comparably across the "
    "2009 / 2015 / 2023 waves; transaction-level items such as electronic-"
    "payment shares appear only in the 2023 questionnaire.", FP)
add_para(doc,
    "For firms participating in foreign markets, even foundational website "
    "adoption may be valuable. A website lowers the cost at which foreign "
    "customers can locate the firm, supports asynchronous communication "
    "across time zones, and signals basic legitimacy in international "
    "transactions. The scope of these gains is bounded — a website does not "
    "by itself integrate transactions, supply chains, or decision-making — "
    "and the realised payoff depends on whether the firm has the scale and "
    "routines to translate online visibility into export business.", BT)
add_para(doc,
    "Website-based digital presence should therefore show a positive average "
    "association with performance, but not necessarily one that is uniform "
    "across waves and stages. The information value of a website may have "
    "shifted across the 2009–2023 window: in 2009 a website was a "
    "distinguishing market interface; by 2023 it is closer to a routine "
    "marker of basic digital presence. The §5 discussion takes this proxy "
    "obsolescence reading seriously as one alternative to a pure stage-"
    "contingency story.", BT)
add_para(doc,
    "Following Verhoef et al. (2021), digital capability can be located on "
    "a four-tier hierarchy: Tier 1 — digital presence (websites, e-mail); "
    "Tier 2 — digital communication and basic e-commerce; Tier 3 — digital "
    "process integration (electronic payment, supply-chain digitisation); "
    "Tier 4 — dynamic digital capability (data-driven decision-making, AI "
    "integration). The primary DAI_z anchors at Tier 1 only. A Tier 3-style "
    "extension (DAI_rich) is reported in §4.5 Panel B for the 2023 wave, "
    "where electronic-payment items become available. The label \"foundational "
    "website adoption\" therefore tracks what the construct can actually "
    "identify across the 2009–2023 window.", BT)
add_para(doc,
    "H3. Website-based digital presence (DAI_z) is positively associated "
    "with firm performance in Vietnam on average.", BX)

add_para(doc, "2.4 Stage-contingent digital value", H2)
add_para(doc, 
    "The core theoretical claim of this study is that digital capability is stage "
    "contingent. In early phases of internationalisation, digital tools may create "
    "relatively direct gains by helping firms communicate faster, access markets more "
    "easily, and manage transactions more efficiently. In later phases, however, the "
    "benefits of digitalisation may become more conditional because firms face more "
    "complex coordination demands. Under such conditions, the value of digital "
    "adoption depends increasingly on whether digital tools are embedded in broader "
    "organisational routines and aligned with export scale.", FP)
add_para(doc, 
    "This argument implies that digitalisation can be a double-edged sword in a "
    "transitional economy. It may generate observable gains, but those gains are "
    "uneven and dependent on timing, scale, and complementary capability. In some "
    "phases, digital adoption may operate mainly as a direct performance-enhancing "
    "factor. In others, it may weaken, disappear, or become conditional on the firm’s "
    "level of internationalisation.", BT)
add_para(doc,
    "This expectation is particularly relevant in Vietnam, where firms operate in an "
    "environment of transition rather than full institutional and capability "
    "stability. A lifecycle interpretation is therefore more appropriate than a "
    "uniform premium interpretation.", BT)
add_para(doc,
    "Two further considerations sharpen the prediction. First, when the exporter "
    "cohort is concentrated in low-export-intensity manufacturing, foundational "
    "digital tools mainly perform a market-access role: they help the firm find "
    "customers, communicate prices and product information, and process simple "
    "transactions. The marginal productivity gain from this role is positive but "
    "broadly distributed across the export-intensity range. Second, when the "
    "exporter cohort shifts toward firms that operate at higher export intensity "
    "and engage in tighter cross-border coordination, the same Tier 1–2 digital "
    "tools begin to interact with the marginal coordination cost of additional "
    "foreign markets. Whether this interaction is substitutive (digital tools lower "
    "coordination cost and amplify the productivity dividend) or complementary "
    "with diminishing returns (digital tools at high intensity reveal the absence "
    "of deeper integration and amplify coordination strain) is fundamentally an "
    "empirical question that this paper treats as the test of H4.", BT)
add_para(doc,
    "H4 (exploratory). The performance relevance of website-based digital "
    "presence (DAI_z) in Vietnam varies across stages of internationalisation; "
    "we treat the within-wave moderation as exploratory and concentrate the "
    "test on 2023, where the post-NDTP environment plausibly enables a "
    "moderation channel.", BX)

# Conceptual model (embedded in body, just after H4) ---------------------------
_FIG_DIR = Path("/home/user/Class-AI-Agent/p4_vietnam/output/figures")
from docx.shared import Inches  # local import (kept idempotent)
if (_FIG_DIR / "figure_1_conceptual_model.png").exists():
    doc.add_picture(str(_FIG_DIR / "figure_1_conceptual_model.png"),
                    width=Inches(6.5))
add_para(doc,
    "Figure 1. Conceptual model. The independent variable "
    "(internationalisation, FSTS_c and FSTS_c²) and the dependent variable "
    "(firm performance, ln labour productivity) anchor the IV–DV spine. "
    "Technological capability (TCI_z) and digital adoption (DAI_z) operate "
    "as moderators of the curvature; controls are firm size (lnEmp), firm "
    "age (FirmAge), foreign ownership (ForeignOwned), broad sector fixed "
    "effects, and wave fixed effects in the pooled specification. "
    "Source: World Bank Enterprise Surveys "
    "(https://www.enterprisesurveys.org); authors’ calculations on the "
    "2009, 2015 and 2023 Vietnam waves.", BT)

# 3. Data and methods ----------------------------------------------------------
add_para(doc, "3. Data, variables, and empirical strategy", H1)

add_para(doc, "3.1 Data structure", H2)
add_para(doc, 
    "The empirical analysis uses harmonised firm-level evidence for Vietnam across "
    "three waves of the World Bank Enterprise Survey: 2009, 2015 and 2023 "
    "(World Bank, 2010, 2016, 2024). Estimating the models separately by wave makes "
    "it possible to observe whether relationships are stable or time specific, "
    "while pooled estimation identifies average effects across the broader period.", FP)
add_para(doc, 
    "The effective estimation sample varies across model specifications because of "
    "missing values in the capability variables. In the full wave-specific models, "
    "the usable samples are 989 observations for 2009, 956 for 2015, and 1,013 for "
    "2023. The pooled full model contains 2,958 observations. This structure provides "
    "sufficient variation to compare direct effects and conditional patterns across "
    "stages.", BT)

add_para(doc, "3.2 Variables", H2)
add_para(doc, 
    "Firm performance is measured by log labour productivity (lnLP). "
    "Internationalisation is measured by direct-export intensity (FSTS), mean-centred "
    "within wave (FSTS_c) and squared (FSTS_c²) so that linear and quadratic terms "
    "can be entered jointly to test for nonlinearity.", FP)
add_para(doc, 
    "The analysis uses two distinct capability constructs. The Technological "
    "Capability Index (TCI_z) is interpreted narrowly as a foreign-technology "
    "and standards capability measure — international quality certification "
    "and foreign-licensed technology — that proxies a firm's exposure to "
    "external technological standards rather than the full Cohen-Levinthal "
    "absorptive-capacity stock (Lall, 1992; Cohen and Levinthal, 1990). The "
    "Digital Adoption Index (DAI_z) is interpreted narrowly as website-based "
    "digital presence — foundational website adoption — and not as a measure "
    "of transaction-level digital integration or digital transformation "
    "(Bharadwaj et al., 2013; Verhoef et al., 2021; Nambisan et al., 2019). "
    "Each composite is z-standardised within wave so that the reported "
    "coefficients are comparable in magnitude. This separation is deliberate "
    "because the study is interested in whether the two domains exhibit "
    "different empirical roles, while keeping the construct labels tight "
    "against what the underlying WBES items actually measure.", BT)
add_para(doc,
    "Item-level construction is as follows. The outcome is "
    "lnLP = ln(d2 / l1), where d2 is total annual sales and l1 is permanent "
    "full-time employees. Internationalisation is FSTS = d3c / 100, "
    "mean-centred within wave (FSTS_c) and squared (FSTS_c²). The primary "
    "Technological Capability Index (TCI_z) is the within-wave standardised "
    "mean of b8 (internationally recognised quality certification) and e6 "
    "(foreign-licensed technology), each recoded from WBES 1/2 to 1/0 binary "
    "form. The primary Digital Adoption Index (DAI_z) is the within-wave "
    "standardised website-presence indicator c22b, recoded from 1/2 to 1/0. "
    "Under this revised primary specification, no item is shared between the "
    "TCI and DAI composites — e6 belongs exclusively to the capability "
    "construct, while c22b alone serves as a harmonised cross-wave proxy for "
    "basic digital presence. Cross-wave-comparable transaction-level digital "
    "items are absent from the 2009 and 2015 instruments, so DAI_z should be "
    "interpreted as a Tier 1–2 digital-adoption measure rather than as a "
    "fully integrated digital-capability construct (Bharadwaj et al., 2013; "
    "Verhoef et al., 2021).", BT)
add_para(doc,
    "Two enriched composites are used in the §4.5 robustness panel where "
    "item availability allows. TCI_full adds h1 (introduced new or "
    "significantly improved product) and h8 (R&D expenditure indicator) to "
    "the TCI items in 2015 and 2023, where h1 and h8 are present. DAI_rich, "
    "constructed only for 2023, extends the website-presence indicator with "
    "k33 (share of sales received via electronic payment) and k38 (share of "
    "supplier payments made via electronic payment), in both continuous "
    "(k33 / 100, k38 / 100) and binary (k33 > 0, k38 > 0) variants. DAI_rich "
    "thus moves from basic digital presence toward a transaction-enabling "
    "digital-adoption construct, but it is treated as a measurement-depth "
    "robustness check rather than as the primary specification because k33 "
    "and k38 are unavailable in the 2009 and 2015 waves.", BT)
add_para(doc,
    "Controls are standard. Firm size lnEmp = ln(l1). Firm age FirmAge = survey "
    "year minus b5 (year established). Foreign ownership ForeignOwned = 1 if b2b "
    "(percentage of equity owned by private foreign individuals or firms) > 0. "
    "Sector fixed effects use the first digit of a4b (broad ISIC code) for the "
    "2009 and 2015 waves and the first digit of a4a for the 2023 wave, where a4b "
    "is not in the public release. Pooled specifications add wave fixed effects to "
    "absorb broad period differences in the productivity baseline.", BT)
add_para(doc,
    "A note on missing-code handling. The WBES instrument codes don’t-know and "
    "refused responses as −9. We treat −9 as missing before any composite is built "
    "and apply listwise deletion on the focal variable set (lnLP, lnEmp, FirmAge, "
    "ForeignOwned, FSTS, TCI_thin, DAI_thin, sector1). The resulting analytic "
    "samples are 989, 956, and 1,013 observations for 2009, 2015, and 2023 "
    "respectively; pooled N is 2,958.", BT)

add_para(doc, "3.3 Model sequence", H2)
add_para(doc, 
    "The empirical strategy follows a nested sequence of models, all estimated by "
    "ordinary least squares with HC1 robust standard errors. A control model "
    "establishes the baseline. A linear internationalisation model then introduces "
    "FSTS_c. A nonlinear model adds the quadratic term FSTS_c² to test for curvature. "
    "Additional models introduce TCI_z and DAI_z separately, first in specifications "
    "that allow interaction terms with FSTS_c and FSTS_c², and then in direct-effect "
    "specifications. The final full model includes the nonlinear "
    "internationalisation terms, both direct capability measures, and the interaction "
    "terms involving digital adoption.", FP)
add_para(doc,
    "This design separates three analytical questions. First, is the I–P relationship "
    "nonlinear? Second, are TCI_z and DAI_z directly associated with performance? "
    "Third, does the role of digital adoption become more conditional as export "
    "intensity rises? Throughout, results are described as associations rather than "
    "effects, consistent with the inferential limits of repeated-cross-section data (Antonakis et al., 2010; Wooldridge, 2010).", BT)

add_para(doc, "3.4 Replication and reproducibility", H2)
add_para(doc,
    "The full pipeline is implemented as a 10-step Stata blueprint distributed with "
    "the manuscript. The build steps (01–04) clean each WBES wave, harmonise the focal "
    "variable set, and append the three waves into a pooled file with within-wave "
    "centring and z-standardisation reapplied. Estimation steps (05–09) cover the "
    "M0–M8 nested sequence, the Lind–Mehlum turning-point check, manual Heckman "
    "selection probes, Paternoster (1998) cross-wave z-tests, and the robustness "
    "panels described in §4.5. The export step (10) writes the manuscript-facing "
    "tables and Figure 2 directly from the stored estimates. Rerunning the pipeline "
    "from a fresh clone reproduces every coefficient reported below; the manuscript "
    "text rather than the do-file output is the object that adjusts when the rerun "
    "drifts from the prose.", FP)

# 4. Results -------------------------------------------------------------------
add_para(doc, "4. Results", H1)

add_para(doc,
    "Table 1 reports analytic-sample summary statistics by wave. Three "
    "patterns are worth noting before the inferential analysis. The share of "
    "firms reporting any positive direct-export intensity declines from "
    "28.4 % in 2009 to 20.7 % in 2015 to 18.8 % in 2023, reflecting the "
    "rebalancing of the Vietnamese exporter cohort away from labour-intensive "
    "manufacturing toward services and FDI-linked supply-chain firms during "
    "the observation window. The within-wave mean of basic digital adoption "
    "(c22b website indicator) rises from 0.425 in 2009 to 0.483 in 2015 and "
    "0.498 in 2023, indicating broad diffusion of basic digital presence "
    "across the Vietnamese firm population over the 14-year window. The mean "
    "of log labour productivity rises monotonically (19.41 / 20.04 / 20.55), "
    "consistent with broader Vietnamese productivity convergence over the "
    "period.", FP)

# Embedded Table 1 ------------------------------------------------------------
desc_table = doc.add_table(rows=11, cols=5)
tbl_pr = desc_table._element.find(qn("w:tblPr"))
if tbl_pr is None:
    tbl_pr = OxmlElement("w:tblPr")
    desc_table._element.insert(0, tbl_pr)
tbl_style = tbl_pr.find(qn("w:tblStyle"))
if tbl_style is None:
    tbl_style = OxmlElement("w:tblStyle")
    tbl_pr.insert(0, tbl_style)
tbl_style.set(qn("w:val"), "Table")

desc_header = desc_table.rows[0].cells
desc_header[0].text = "Variable"
desc_header[1].text = "2009 (N = 989)"
desc_header[2].text = "2015 (N = 956)"
desc_header[3].text = "2023 (N = 1,013)"
desc_header[4].text = "Pooled (N = 2,958)"

desc_rows = [
    ("lnLP (log labour productivity)",     "19.41 (1.31)", "20.04 (1.46)", "20.55 (1.47)", "20.00 (1.49)"),
    ("FSTS (direct-export share)",         "0.168 (0.337)", "0.120 (0.284)", "0.131 (0.311)", "0.140 (0.312)"),
    ("Exporter (FSTS > 0) share",          "0.284", "0.208", "0.188", "0.226"),
    ("TCI_thin (mean of b8, e6 recoded)",  "0.169 (0.305)", "0.141 (0.295)", "0.146 (0.276)", "0.152 (0.292)"),
    ("DAI (c22b — own website, recoded)",  "0.425 (0.495)", "0.483 (0.500)", "0.498 (0.500)", "0.469 (0.499)"),
    ("lnEmp (log permanent employees)",    "4.07 (1.49)", "3.63 (1.48)", "3.58 (1.54)", "3.76 (1.52)"),
    ("FirmAge (years since b5)",           "11.9 (11.3)", "12.8 (9.6)", "14.1 (7.9)", "12.9 (9.7)"),
    ("ForeignOwned (b2b > 0) share",       "0.142", "0.090", "0.125", "0.119"),
    ("",                                   "", "", "", ""),
    ("ISIC sector FE",                     "a4b 1-digit", "a4b 1-digit", "a4a 1-digit", "wave + a4b/a4a 1-digit"),
]
for i, row in enumerate(desc_rows, start=1):
    cells = desc_table.rows[i].cells
    for j, val in enumerate(row):
        cells[j].text = val

add_para(doc,
    "Notes. Cell entries are mean (standard deviation) for continuous "
    "variables and proportion for binary indicators. Listwise deletion is "
    "applied on the focal variable set with WBES non-response codes (−9) "
    "treated as missing. Source: World Bank Enterprise Surveys "
    "(https://www.enterprisesurveys.org); authors’ calculations on the "
    "Vietnam 2009, 2015 and 2023 waves. Replication output: "
    "p4_vietnam/output/tables/table_1_descriptives.csv.", BT)

add_para(doc, "4.1 Wave-specific findings", H2)
add_para(doc,
    "The 2009 wave displays a clearly nonlinear internationalisation–"
    "performance relationship together with strong direct capability and "
    "digital-adoption effects. The inverted-U specification (M2) yields a "
    "positive linear term (β = 1.045, p = .015) and a negative quadratic "
    "term (β = −1.774, p = .009); the Lind–Mehlum test rejects monotonicity "
    "at p = .006. In the dual-direct specification (M7) both TCI_z "
    "(β = 0.215, p < .001) and DAI_z (β = 0.175, p < .001) are positive and "
    "highly significant. TCI moderation is statistically distinguishable from "
    "zero (M3 joint p = .040; FSTS_c × TCI_z = −0.579, p = .087), but DAI "
    "moderation is not (M4 joint p = .825; full-model M8 joint p = .700). In "
    "substantive terms, both capability dimensions in 2009 operate primarily "
    "as direct level-shifters; the marginal coordination cost that bends the "
    "I–P curve is associated with technological capability rather than with "
    "basic digital presence.", FP)
add_para(doc,
    "The 2015 wave shows the curvature cleanly but the weakest digital "
    "channel. M2 produces FSTS_c β = 1.159 (p = .029) and FSTS_c² β = −2.115 "
    "(p = .004), with Lind–Mehlum p = .009. TCI_z retains a positive direct "
    "association (β = 0.128, p = .010) but at roughly 60 per cent of the "
    "2009 magnitude. DAI_z loses direct salience entirely (β = −0.044, "
    "p = .377). TCI moderation is null in this wave (M3 joint p = .713), and "
    "DAI moderation is at best marginal (M4 joint p = .125; M8 joint "
    "p = .093). Read as a phase characterisation, 2015 looks like a wave in "
    "which the I–P curvature is unusually sharp while the digital channel "
    "compresses entirely — consistent with the productivity J-curve account "
    "in which firms invest in basic digital tools before complementary "
    "organisational adjustments produce measurable productivity gains "
    "(Brynjolfsson et al., 2021).", BT)
add_para(doc,
    "The 2023 wave is where the digital-moderation signal emerges most "
    "sharply. M2 again indicates a clear inverted-U (FSTS_c β = 0.962, "
    "p = .039; FSTS_c² β = −1.686, p = .008; Lind–Mehlum p = .013). In the "
    "dual-direct M7, both capability dimensions are positive and significant "
    "(TCI_z β = 0.123, p = .006; DAI_z β = 0.095, p = .038). When the DAI "
    "interaction terms are added in M8, the linear interaction is negative "
    "and individually significant (FSTS_c × DAI_z = −0.912, p = .043), the "
    "quadratic interaction is positive and marginal (FSTS_c² × DAI_z = "
    "1.043, p = .099), and the joint test sits at marginal significance "
    "(M4 joint p = .102; M8 joint p = .062). The substantive reading is "
    "that, by 2023, basic digital adoption becomes more conditional on "
    "export intensity: as exporters move beyond moderate FSTS levels, the "
    "productivity contribution of basic digital presence attenuates and may "
    "amplify rather than relieve coordination burdens, consistent with the "
    "view that website-level adoption alone is insufficient when deeper "
    "transaction-enabling and process-integrating digital capability is "
    "still maturing.", BT)
add_para(doc,
    "Taken together, the wave-specific results trace two wave-specific "
    "associations consistent with stage contingency. Foreign-technology / "
    "standards capability is positive across all three waves with a modestly "
    "attenuating magnitude (TCI_z = 0.215 → 0.128 → 0.123) but with "
    "moderation that survives in the 2009, 2023 and pooled panels. Website-"
    "based digital presence follows a non-monotonic trajectory — strong in "
    "2009 (β = 0.175 ***), null in 2015 (β = −0.044 n.s.), and re-emerging "
    "in 2023 (β = 0.095 *) — and its moderation channel materialises only "
    "in 2023. The Paternoster cross-wave z-tests reported in §4.5 confirm "
    "that the 2009-to-2015 fall in DAI (z = 3.353, p < .001) and the "
    "2015-to-2023 recovery (z = −2.051, p = .040) are statistically "
    "distinguishable. A formal pooled wave × focal interaction test "
    "(reported as Panel I in §4.5) confirms that only the DAI direct shifts "
    "are cross-wave-distinguishable; the FSTS curvature and the FSTS × DAI "
    "moderation differences across waves are not statistically separable in "
    "the pooled saturated specification. We therefore read the pattern as "
    "wave-specific associations consistent with stage contingency, not as a "
    "fully cross-wave-identified structural shift.", BT)
add_para(doc,
    "The wave-specific pattern carries an institutional reading. The 2009 wave "
    "captures the early aftermath of WTO accession, when the marginal exporter "
    "was still in the entry-cost zone of the I–P curve, when capability stocks "
    "were the scarce resource, and when foundational digital tools — even at "
    "the website-only layer — generated direct gains because the alternative "
    "was paper-based transaction processing. The 2015 wave captures a "
    "transitional phase in which the I–P curvature is unusually sharp (FSTS_c² "
    "= −2.115, p = .004 in M2) but the digital channel compresses entirely: "
    "DAI_z loses direct salience and shows no joint moderation, suggesting "
    "that the differences in exporter composition across waves are reflected "
    "in productivity gains coming primarily from scale and from foreign-"
    "technology / standards capability rather than from foundational digital "
    "adoption in this wave. The 2023 wave captures the "
    "re-emergence of the digital channel as a moderator rather than as a "
    "uniform direct premium: the post-NDTP digital infrastructure makes "
    "foundational digital adoption interact with export intensity, and the "
    "negative FSTS_c × DAI_z interaction shows that this conditional channel "
    "binds primarily at higher export intensity rather than uniformly across "
    "the export-intensity range.", BT)

add_para(doc, "4.2 Pooled findings", H2)
add_para(doc,
    "The pooled estimates confirm that the internationalisation–performance "
    "relationship is nonlinear on average. In the pooled M2 specification, "
    "the linear FSTS_c term is positive (β = 0.984, p < .001) and the "
    "quadratic FSTS_c² term is negative (β = −1.909, p < .001); the "
    "Lind–Mehlum test rejects monotonicity at p < .001 with an estimated "
    "turning point at 39.7 per cent of direct-export intensity. The "
    "curvature persists in the full M8 specification (FSTS_c β = 0.845, "
    "p = .006; FSTS_c² β = −1.650, p < .001), supporting H1 and aligning "
    "with the meta-analytic evidence on the nonlinear shape of "
    "internationalisation returns in emerging-market firms (Marano et al., "
    "2016).", FP)
add_para(doc,
    "The pooled evidence shows that both technological capability and basic "
    "digital adoption are positively associated with firm performance on "
    "average. In the pooled M7 dual-direct specification, TCI_z is positive "
    "and highly significant (β = 0.179, p < .001), and DAI_z is positive "
    "and significant (β = 0.078, p = .004). In the full M8 specification, "
    "the TCI_z coefficient is essentially unchanged (β = 0.184, p < .001), "
    "while the DAI_z direct coefficient becomes statistically "
    "indistinguishable from zero (β = 0.032, p = .537) once the interaction "
    "terms are entered. This sensitivity is consistent with the "
    "interpretation that DAI_z combines a positive level effect with a "
    "negative interaction with FSTS_c at higher export intensities — "
    "precisely the pattern documented in §4.1 for the 2023 wave.", BT)
add_para(doc,
    "The pooled interaction terms involving DAI_z carry a marginal joint "
    "signal. The linear interaction is negative but not individually "
    "significant (FSTS_c × DAI_z = −0.448, p = .116), and the quadratic "
    "interaction is positive but not significant (FSTS_c² × DAI_z = 0.460, "
    "p = .276). The joint Wald test sits at marginal significance (M8 joint "
    "p = .083). This pooled signal is driven primarily by the 2023 wave: "
    "the M4 joint moderation test on DAI is null in 2009 (p = .825) and "
    "2015 (p = .125), and reaches marginal significance only in 2023 (M4 "
    "joint p = .102; M8 joint p = .062). Pooled estimates therefore "
    "understate the timing of the DAI moderation channel: the channel is "
    "concentrated in the most recent wave rather than uniformly distributed "
    "across the 2009–2023 window.", BT)
add_para(doc,
    "Technological-capability moderation, by contrast, is more uniformly "
    "distributed. The M3 joint test on FSTS_c × TCI_z and FSTS_c² × TCI_z "
    "is statistically distinguishable from zero in three of four panels "
    "(2009 p = .040, 2023 p = .027, pooled p = .003) and null only in 2015 "
    "(p = .713). Pooled, the linear interaction is negative (FSTS_c × "
    "TCI_z = −0.587, p = .003) and the quadratic is positive (FSTS_c² × "
    "TCI_z = 0.640, p = .031), indicating that the inverted-U flattens for "
    "high-capability firms rather than shifting in level. This is "
    "consistent with the absorptive-capacity reading in which firms with "
    "deeper capability stocks extract productivity gains across a wider "
    "range of export intensities than less capable peers (Cohen and "
    "Levinthal, 1990; Lall, 1992).", BT)
add_para(doc, 
    "If the analysis stopped at pooled estimation, one might conclude that "
    "digitalisation provides a broadly positive but structurally simple performance "
    "premium. The wave-specific evidence shows that this conclusion would be "
    "incomplete. The positive pooled average coexists with substantial temporal "
    "heterogeneity, and the conditional role of digital adoption emerges more "
    "clearly only in the later wave.", BT)

add_para(doc, "4.3 Interpretation of the hypothesis tests", H2)
add_para(doc,
    "H1 is strongly supported. The Lind–Mehlum test rejects the monotonicity "
    "null in all three waves (2009 p = .006, 2015 p = .009, 2023 p = .013) "
    "and in the pooled sample (p < .001), and the implied turning points are "
    "tightly clustered between 39.3 per cent (2015) and 46.2 per cent (2009) "
    "of direct-export intensity, with the pooled estimate at 39.7 per cent. "
    "H2 is supported by the positive TCI_z direct association in the pooled "
    "sample (β = 0.179, p < .001) and in all three wave-specific periods "
    "(2009 p < .001; 2015 p = .010; 2023 p = .006), reinforced by "
    "statistically distinguishable TCI moderation in three of four panels "
    "(M3 joint p = .040, .713, .027 and .003). H3 is supported on average: "
    "the pooled M7 estimate of DAI_z is positive and significant (β = "
    "0.078, p = .004), but DAI_z varies sharply across waves — strong in "
    "2009 (β = 0.175, p < .001), null in 2015 (β = −0.044, p = .377) and "
    "positive in 2023 (β = 0.095, p = .038). The Paternoster cross-wave "
    "z-tests (§4.5, Panel F) confirm that the 2009-to-2015 fall (z = 3.353, "
    "p < .001) and the 2015-to-2023 recovery (z = −2.051, p = .040) are "
    "both statistically distinguishable shifts.", FP)
add_para(doc,
    "H4 receives exploratory support concentrated in the 2023 wave. The DAI "
    "joint moderation test is null in 2009 (M4 p = .825), null in 2015 "
    "(M4 p = .125) and reaches the edge of significance in 2023 with the "
    "individual interaction FSTS_c × DAI_z = −0.912 (p = .043) and the "
    "joint test at M4 p = .102, M8 p = .062. The pooled M8 joint test "
    "(p = .083) is also at marginal significance, driven by the 2023 wave "
    "rather than by a stable cross-period moderation. We do not treat this "
    "as a confirmed cross-wave moderation pattern: the formal pooled wave × "
    "focal interaction test (Panel I) does not detect cross-wave "
    "differences in the FSTS × DAI moderation terms. The substantive "
    "reading is that 2023 is the only wave in which the digital moderation "
    "is within-sample detectable, and we frame this as exploratory rather "
    "than as a confirmed hypothesis test.", BT)

add_para(doc, "4.4 Main empirical pattern: participation × intensity", H2)
add_para(doc,
    "Before reading the table that follows, we anchor the reader in the "
    "two-margin structure introduced in §2.1. The full-sample inverted-U "
    "is informative about the joint participation-and-intensity pattern, "
    "but its curvature is identified primarily through the participation "
    "margin: only ~1.0 % of pooled firms sit within ±5 percentage-points "
    "of the wave-specific turning points (see §4.5 density check), and "
    "the bulk of mass lies at FSTS = 0. When we re-fit M2 / M7 / M8 on "
    "the exporter-only sub-sample (FSTS > 0; pooled N = 669, §4.5 "
    "Panel H), the linear FSTS_c term is negative (β = −0.861, "
    "p < .001) but the quadratic term is not significant (FSTS_c² "
    "β = −0.200, p = .660, M8 joint p = .462). H1a (participation "
    "margin) is therefore the dominant productivity-relevant margin in "
    "this dataset; the within-exporter intensity curvature claimed by "
    "H1b weakens once participation is netted out. We retain the full-"
    "sample inverted-U as the headline empirical regularity, but "
    "interpret it explicitly through the dual-mechanism lens: most of "
    "the productivity differential lies between non-exporters and "
    "exporters, with limited additional curvature within the exporter "
    "subsample. Table 1 therefore reads as a description of the "
    "combined participation × intensity pattern rather than as a "
    "structural statement about within-exporter intensity curvature.", FP)
add_para(doc,
    "Table 1 summarises the directional interpretation of the focal "
    "coefficients from the full specifications by wave and for the "
    "pooled sample.", FP)

table = doc.add_table(rows=5, cols=5)
# Apply the "Table" style that the v4.4 template ships with, by writing the
# tblStyle element directly (BabelFish would mishandle the lookup).
tbl_pr = table._element.find(qn("w:tblPr"))
if tbl_pr is None:
    tbl_pr = OxmlElement("w:tblPr")
    table._element.insert(0, tbl_pr)
tbl_style = tbl_pr.find(qn("w:tblStyle"))
if tbl_style is None:
    tbl_style = OxmlElement("w:tblStyle")
    tbl_pr.insert(0, tbl_style)
tbl_style.set(qn("w:val"), "Table")
header = table.rows[0].cells
header[0].text = "Wave / model"
header[1].text = "I–P relationship"
header[2].text = "TCI_z direct"
header[3].text = "DAI_z direct"
header[4].text = "DAI_z interaction"

rows = [
    ("2009",
     "Inverted-U: FSTS_c 1.045** / FSTS_c² −1.774**; LM p = .006; TP = 46.2 %",
     "0.215 *** (M7)",
     "0.175 *** (M7)",
     "M4 joint p = .825 n.s.; M8 joint p = .700 n.s."),
    ("2015",
     "Inverted-U: FSTS_c 1.159* / FSTS_c² −2.115**; LM p = .009; TP = 39.3 %",
     "0.128 * (M7)",
     "−0.044 (p = .377) n.s.",
     "M4 joint p = .125 n.s.; M8 joint p = .093 †"),
    ("2023",
     "Inverted-U: FSTS_c 0.962* / FSTS_c² −1.686**; LM p = .013; TP = 41.6 %",
     "0.123 ** (M7)",
     "0.095 * (M7)",
     "M4 joint p = .102 †; M8 joint p = .062 †; FSTS_c × DAI_z = −0.912 *"),
    ("Pooled",
     "Inverted-U: FSTS_c 0.984*** / FSTS_c² −1.909***; LM p < .001; TP = 39.7 %",
     "0.179 *** (M7)",
     "0.078 ** (M7); 0.032 n.s. (M8)",
     "M4 joint p = .213 n.s.; M8 joint p = .083 †"),
]
for i, row in enumerate(rows, start=1):
    cells = table.rows[i].cells
    for j, val in enumerate(row):
        cells[j].text = val

add_para(doc,
    "Notes. Cell entries report β coefficients with HC1-robust p-values from the full "
    "specifications. n.s. = not statistically significant at conventional thresholds. "
    "Interaction terms entered as FSTS_c × DAI_z and FSTS_c² × DAI_z; the table "
    "reports the focal linear interaction. "
    "Source: World Bank Enterprise Surveys (https://www.enterprisesurveys.org); "
    "authors’ calculations.", BT)

# Predicted I–P curves embedded as four standalone sub-figures ----------------
for tag, label in [
    ("2a", "Vietnam 2009 (N = 989)"),
    ("2b", "Vietnam 2015 (N = 956)"),
    ("2c", "Vietnam 2023 (N = 1,013)"),
    ("2d", "Pooled Vietnam 2009/2015/2023 (N = 2,958)"),
]:
    fpath = _FIG_DIR / f"figure_{tag}.png"
    if fpath.exists():
        doc.add_picture(str(fpath), width=Inches(6.0))
    add_para(doc,
        f"Figure {tag}. Predicted ln(labour productivity) across direct-export "
        f"intensity, {label}. The fitted curve comes from the M2 inverted-U "
        "OLS specification with HC1 robust standard errors, holding controls "
        "(lnEmp, FirmAge, ForeignOwned, sector fixed effects, and wave fixed "
        "effects in the pooled panel) at within-wave means. The shaded band "
        "is the 95 % confidence interval for the predicted mean; the vertical "
        "dashed line marks the turning-point point estimate on the raw FSTS "
        "scale. Source: World Bank Enterprise Surveys "
        "(https://www.enterprisesurveys.org); authors’ calculations.", BT)

add_para(doc, "4.5 Robustness", H2)
add_para(doc,
    "Four robustness panels test whether the central inferences depend on "
    "measurement choices, sample composition, or the cross-wave alignment of the "
    "DAI construct. The panels are estimated on the same OLS HC1 design as the "
    "main models and are written to "
    "p4_vietnam/output/tables/table_3_robustness.csv.", FP)
add_para(doc,
    "Panel A — Enriched TCI_full composite (2015 and 2023, where h1 "
    "product-innovation and h8 R&D indicators are available). Adding h1 and "
    "h8 to the primary TCI items produces an attenuated direct effect: the "
    "TCI_full_z direct coefficient is 0.056 (p = .253) in 2015 and 0.096 "
    "(p = .024) in 2023 — both smaller than the corresponding TCI_thin "
    "estimates of 0.128 and 0.123. The moderation joint test is not "
    "statistically distinguishable from zero in either wave (2015 joint F "
    "p = .492; 2023 joint F p = .152). The attenuation is consistent with "
    "the interpretation that the TCI_thin items (b8 quality certification "
    "and e6 foreign-licensed technology) carry a sharper foreign-capability "
    "content than the broader product-innovation and R&D items add. The "
    "TCI_thin specification is therefore retained as the primary measurement "
    "throughout the paper.", BT)
add_para(doc,
    "Panel B — Enriched DAI_rich composite (2023 only). The richer "
    "specification extends the primary website-based DAI with k33 (customer "
    "e-payment intensity) and k38 (supplier e-payment intensity), in both "
    "continuous and binary forms. The 2023 DAI_rich_cont moderation joint "
    "test is marginal (joint F p = .099, with FSTS_c × DAI_rich_cont_z = "
    "−0.933, p = .076), and the binary specification is non-significant "
    "(joint F p = .243). The richer measure thus indicates a similar "
    "directional pattern to the primary DAI moderation finding but with "
    "weaker individual significance — consistent with the view that "
    "transaction-enabling digital adoption operates through a different "
    "productivity channel than basic digital presence and should not be "
    "treated as a one-for-one replacement for the harmonised primary "
    "specification.", BT)
add_para(doc,
    "Panel C — Common-N comparison (2023). The primary DAI_z and DAI_rich "
    "specifications are estimated on the same N = 1,013 sample, so the "
    "differences in Panel B reflect measurement rather than sample. The "
    "reconciled M8 joint test for the primary specification on this common-N "
    "sample yields F(3, 998) ≈ 2.50, p = .062 — matching the main 2023 M8 "
    "result, and confirming that the Panel B DAI_rich attenuation is not an "
    "artefact of selective missingness on k33 / k38. This rules out a "
    "missingness-driven alternative explanation and supports retaining the "
    "harmonised website-based DAI as the primary cross-wave specification.", BT)
add_para(doc,
    "Panel D — Micro-firm exclusion (l1 ≥ 10). Excluding firms with fewer "
    "than ten permanent employees reduces the pooled sample to N = 2,473 "
    "and leaves the substantive inferences intact. The inverted-U is "
    "preserved (FSTS_c β = 0.794, p = .008; FSTS_c² β = −1.647, p < .001), "
    "the TCI_z direct association is essentially unchanged (β = 0.188, "
    "p < .001), DAI_z direct is positive but not individually significant "
    "(β = 0.054, p = .288), and the DAI moderation joint test in the full "
    "M8 specification (joint F p = .167) is somewhat weaker than in the "
    "main pooled M8 (p = .083). The Lind–Mehlum monotonicity rejection and "
    "the broader lifecycle reading do not depend on the inclusion of very "
    "small firms.", BT)
add_para(doc,
    "Panel E — Sample-selection probes (Heckman, 1979; Wooldridge, 2010). "
    "The selection equation is a probit of export_any on lnEmp, FirmAge, "
    "ForeignOwned, sector fixed effects and the WBES sampling region a2, "
    "with a2 supplying the exclusion restriction (sampling region affects "
    "export selection through differential logistical access but is "
    "plausibly uncorrelated with the productivity outcome conditional on "
    "the other controls). The inverse Mills ratio added to the outcome "
    "equation estimated on exporters (FSTS > 0) is statistically "
    "insignificant in all four panels: λ = −0.111 (p = .846) in 2009, "
    "λ = −0.833 (p = .259) in 2015, λ = 0.665 (p = .399) in 2023, and "
    "λ = −0.462 (p = .347) pooled, indicating no detectable selection "
    "bias on the exporter sub-sample. We also report a control-function "
    "specification estimated on the full sample using the probit-based "
    "generalised residual, which yields a significant residual pooled "
    "(β = 0.304, p < .001) and in 2009 (β = 0.510, p < .001), a marginal "
    "residual in 2023 (β = 0.259, p = .092) and a null residual in 2015 "
    "(β = −0.112, p = .357). We do not interpret this gap as evidence of a "
    "different selection channel: in a probit, the generalised residual "
    "coincides with the inverse Mills ratio for selected observations, so "
    "the difference in significance reflects the larger estimation sample "
    "(non-exporters are included in the control-function regression) and "
    "the slightly different specification, not a substantively distinct "
    "selection mechanism. Either way, the focal H1 / H2 / H3 inferences "
    "survive both corrections.", BT)
add_para(doc,
    "Panel F — Paternoster (1998) cross-wave z-tests. To assess whether "
    "the cross-wave differences in the focal M7 / M8 coefficients are "
    "statistically distinguishable from sampling noise, we apply "
    "z = (β_A − β_B) / sqrt(SE_A² + SE_B²) for each pair of waves and each "
    "focal term. The DAI_z direct association shifts significantly between "
    "2009 and 2015 (z = 3.353, p < .001) and between 2015 and 2023 "
    "(z = −2.051, p = .040), confirming that the lifecycle pattern of basic "
    "digital adoption is not an artefact of sampling noise. The TCI_z "
    "magnitude attenuates more modestly: the 2009-to-2015 difference "
    "(z = 1.288, p = .198) and 2009-to-2023 difference (z = 1.423, "
    "p = .155) are not statistically distinguishable. All FSTS_c, "
    "FSTS_c², FSTS_c × DAI_z and FSTS_c² × DAI_z pairwise differences are "
    "non-significant (all |z| < 1.4, all p > .17), so the inverted-U shape "
    "and the DAI moderation patterns are best read as a common curvature "
    "with wave-specific magnitudes rather than as cross-period structural "
    "shifts in the curvature parameters.", BT)
add_para(doc,
    "Panel G — Sector split (manufacturing versus non-manufacturing). To "
    "test whether the digital and capability channels operate uniformly "
    "across the broad sectoral composition of the Vietnamese exporter "
    "cohort, we re-estimate the pooled M2 / M7 / M8 specifications "
    "separately on manufacturing firms (sector1 ∈ {1, 2, 3} — ISIC 15–37, "
    "N = 1,854) and non-manufacturing firms (utilities, construction, "
    "wholesale and retail, transport, finance and other services; "
    "sector1 ∈ {4, 5, 6, 7}; N = 1,104). The inverted-U is preserved in "
    "both subsets but is sharper in manufacturing (FSTS_c β = 0.971, "
    "p = .001; FSTS_c² β = −1.883, p < .001) than in non-manufacturing "
    "(FSTS_c β = 1.615, p = .064, marginal; FSTS_c² β = −2.479, p = .046).", FP)
add_para(doc,
    "More substantively, the capability and digital-adoption channels "
    "operate primarily in manufacturing. In the M7 dual-direct "
    "specification, manufacturing firms display a strong TCI_z direct "
    "association (β = 0.223, p < .001) and a positive DAI_z direct "
    "association (β = 0.087, p = .009), while non-manufacturing firms "
    "show only a marginal TCI_z effect (β = 0.090, p = .096) and a null "
    "DAI_z effect (β = 0.068, p = .133). The DAI moderation channel is "
    "concentrated in manufacturing (M8 joint p = .103, marginal; "
    "FSTS_c × DAI_z = −0.543, p = .079) and is uniformly null in "
    "non-manufacturing (M8 joint p = .280). TCI moderation, by contrast, "
    "is statistically distinguishable from zero in both subsets (M3 joint "
    "p = .011 in manufacturing and p = .007 in non-manufacturing), "
    "indicating that the curvature-flattening effect of capability "
    "operates broadly while the digital channel remains specific to the "
    "manufacturing exporter base. Substantively, this pattern is "
    "consistent with the view that basic digital adoption interacts with "
    "cross-border production-coordination demands more strongly in "
    "tradable-goods sectors than in service-oriented or domestically "
    "oriented sectors of the Vietnamese economy.", BT)

add_para(doc,
    "Panel H — Exporter-only sub-sample (FSTS > 0). Because the exporter "
    "share is 28.4 %, 20.7 % and 18.8 % across waves, the inverted-U fitted "
    "on the full sample is partly identified by the participation margin "
    "between FSTS = 0 and FSTS > 0. We re-fit M2 / M7 / M8 on the exporter-"
    "only sub-sample (N ≈ 281 in 2009, 198 in 2015, 190 in 2023, and 669 "
    "pooled). The pooled exporter-only specification yields a negative "
    "linear FSTS_c term (β = −0.861, p < .001) but a non-significant "
    "quadratic term (FSTS_c² β = −0.200, p = .660), and the joint M8 test "
    "of the curvature plus moderation block is not significant (joint "
    "F p = .462). The wave-specific exporter-only estimates are similarly "
    "noisier and individually weaker than the full-sample counterparts. "
    "We read this as showing that the inverted-U documented in the main "
    "specification is meaningfully identified by the participation margin "
    "rather than purely by within-exporter intensity variation; this is "
    "consistent with the §3.1 descriptive evidence that direct-export "
    "intensity is a zero-inflated variable in Vietnamese WBES data, with "
    "limited mass between the participation margin and the implied turning "
    "point. The substantive H1 claim is therefore best read as a non-"
    "monotonic association between participation-and-intensity in exporting "
    "and productivity, not as a strict within-exporter intensity-curvature "
    "claim.", FP)
add_para(doc,
    "Panel I — Pooled wave × focal interaction test. To formally test "
    "whether the wave-specific patterns of curvature and moderation are "
    "statistically separable from the pooled estimates, we re-estimate the "
    "pooled M8 with a saturated set of wave interactions on the focal "
    "terms (FSTS_c × wave, FSTS_c² × wave, DAI_z × wave, TCI_z × wave). "
    "The joint Wald tests show that only DAI_z × wave is statistically "
    "distinguishable from the pooled average (joint p = .016); the FSTS_c, "
    "FSTS_c² and TCI_z direct-effect cross-wave differences are not "
    "statistically separable (all joint p > .25), and the FSTS_c × DAI_z "
    "and FSTS_c² × DAI_z cross-wave differences are not separable either "
    "(joint p > .55). This formal test confirms the descriptive Paternoster "
    "result: only the DAI direct shifts are cross-wave-distinguishable, "
    "while the curvature parameters and the FSTS × DAI moderation terms "
    "share a common pooled magnitude across waves.", BT)
add_para(doc,
    "Density-around-turning-point check. We also report the within-sample "
    "mass of firms in the curvature zone. Defining a ±5 percentage-point "
    "band around the wave-specific turning point (TP), the share of firms "
    "with FSTS within the band is 0.6 % (6 of 989) in 2009, 1.2 % (11 of "
    "956) in 2015, 0.9 % (9 of 1,013) in 2023 and 1.0 % (29 of 2,958) "
    "pooled. The bulk of mass lies at FSTS = 0; the turning-point "
    "estimates are identified primarily through the contrast between "
    "non-exporters and exporters and the right tail above the TP, not "
    "through dense within-band variation. Readers should bear this density "
    "structure in mind when interpreting the precise turning-point "
    "magnitude.", BT)

add_para(doc,
    "Panel J — Propensity-score matching (PSM). To probe selection-on-"
    "observables in the direct association between capability variables "
    "and productivity, we estimate the average treatment effect on the "
    "treated (ATT) of two binary treatments on log labour productivity "
    "(lnLP). Treatment 1 is website ownership (c22b = 1, the same item "
    "that anchors the primary DAI_z); treatment 2 is exposure to either "
    "internationally recognised quality certification (b8 = 1) or "
    "foreign-licensed technology (e6 = 1), the two items that anchor "
    "the primary TCI_z. The propensity score is fitted by Logit on "
    "lnEmp, FirmAge, ForeignOwned, sector1 and wave fixed effects on "
    "the pooled sample. Two matching algorithms are reported: 1-NN "
    "with caliper = 0.05 and Epanechnikov kernel matching with "
    "bandwidth = 0.06. The website-treatment ATT is 0.298 (SE 0.061) "
    "under 1-NN and 0.321 (SE 0.043) under kernel matching, both "
    "p < .001 (matched N ≈ 1,085); the cert/foreign-tech-treatment "
    "ATT is 0.637 (SE 0.078) under 1-NN and 0.609 (SE 0.056) under "
    "kernel matching, both p < .001 (matched N ≈ 640). Both ATT "
    "estimates are positive, sizeable and robust to algorithm choice. "
    "Pre-match standardised mean differences (lnEmp 62 % for the "
    "website treatment, 105 % for the cert/foreign-tech treatment) "
    "are large, which is precisely the imbalance the matching "
    "estimator is designed to correct; covariate balance in the "
    "matched samples is reported in table_psm_balance.csv. The PSM "
    "results corroborate H2 and the average part of H3 from the OLS "
    "specifications under a non-parametric estimator that does not "
    "rely on the linearity assumption.", BT)
add_para(doc,
    "Panel K — Two-stage least squares (2SLS) with leave-one-out "
    "industry × region instruments. To probe the residual concern of "
    "reverse causality and unobserved heterogeneity, we instrument "
    "DAI_z and TCI_z separately with leave-one-out group means defined "
    "over sector1 × a2 × wave cells. Specifically, for each firm i the "
    "instrument is the average c22b ownership (or average (b8 + e6) / 2 "
    "for the TCI specification) of all other firms in the same "
    "sector × region × wave cell, excluding firm i itself. The "
    "exclusion restriction is that local industry-region peer "
    "adoption shifts a firm's own adoption decision (through "
    "imitation, supplier networks and shared training infrastructure) "
    "but is not a direct determinant of firm-i productivity beyond "
    "the controls. The first-stage F-statistic is 34.6 for the DAI "
    "instrument and 22.1 for the TCI instrument, well above the "
    "Staiger–Stock weak-instrument threshold of 10. The 2SLS estimates "
    "are informative: instrumented DAI_z = 0.018 (SE 0.249, p = .942), "
    "while instrumented TCI_z = 1.639 (SE 0.299, p < .001). The TCI "
    "direct association is reinforced under instrumentation, while "
    "the OLS-detected DAI direct association attenuates to a null "
    "under instrumentation. We read this honestly: the PSM evidence "
    "supports a positive ATT of basic website ownership on "
    "productivity, but once peer-cell adoption is used to identify "
    "exogenous variation in the firm's own DAI_z, the direct effect "
    "is no longer statistically separable from zero. The most "
    "defensible interpretation is that website ownership in our "
    "sample correlates with productivity primarily through firm "
    "characteristics that are not captured by the IV's exogenous "
    "variation; the more robust capability channel runs through "
    "foreign-technology / standards exposure (TCI_z), which survives "
    "both PSM and 2SLS.", BT)
add_para(doc,
    "Oster (2019) δ-stability bounds. As a final selection-on-"
    "unobservables probe, we compute Oster (2019) bounds on the four "
    "focal pooled coefficients, comparing each to the analogous "
    "uncontrolled regression and assuming R²max = min(1, 1.3 × R²"
    "controlled), the canonical default. Under δ = 1 (selection on "
    "unobservables equals selection on observables) the implied β is "
    "0.615 for FSTS_c, −1.174 for FSTS_c², 0.194 for TCI_z, and "
    "0.080 for DAI_z. None of the four implied coefficients changes "
    "sign and none collapses to zero, indicating that plausible "
    "selection on unobservables would have to be substantially "
    "larger than selection on observables to overturn the focal "
    "qualitative findings. The Oster bound is reported as "
    "table_oster_bounds.csv.", BT)
add_para(doc,
    "Multiple-testing caveat. §4.5 reports eleven robustness panels (A–K plus Oster bounds) "
    "across two enriched composites, three sub-samples, two selection "
    "corrections, cross-wave z-tests and a wave-saturated interaction test, "
    "each touching multiple focal terms. We do not apply a formal multiple-"
    "testing correction because the panels probe different identification "
    "concerns rather than testing the same hypothesis repeatedly, but "
    "readers should weight any single marginal panel result accordingly. "
    "Our substantive inferences in §5 rely on the pattern across panels "
    "and the directional consistency of the focal estimates rather than on "
    "the significance of any single robustness panel.", BT)

# Figure 3 — Predicted I-P curves at low/high DAI and TCI (inline) -----------
if (_FIG_DIR / "figure_3_moderator_marginals.png").exists():
    from docx.enum.text import WD_ALIGN_PARAGRAPH as _WD_ALIGN
    add_para(doc, "", BT)
    fig3_p = doc.add_paragraph()
    fig3_p.alignment = _WD_ALIGN.CENTER
    fig3_p.add_run().add_picture(
        str(_FIG_DIR / "figure_3_moderator_marginals.png"),
        width=Inches(6.5),
    )
    add_para(doc,
        "Figure 3. Predicted log labour productivity along the FSTS export-"
        "intensity range, evaluated at the 25th vs 75th percentile of the "
        "moderator. Panel 3a shows the FSTS curve at low (p25) vs high "
        "(p75) DAI_z; Panel 3b shows the FSTS curve at low (p25) vs high "
        "(p75) TCI_z. Curves are obtained from the pooled M8 specification "
        "with controls and wave + sector fixed effects fixed at their "
        "sample modes / means; predictions are reported on the within-"
        "sample FSTS support. Source: World Bank Enterprise Surveys "
        "(https://www.enterprisesurveys.org); authors' calculations.", BT)

# Table 3 — Robustness summary embedded -----------------------------------
add_para(doc,
    "Table 3 collates the robustness panels documented in §4.5 in a "
    "single overview to ease cross-comparison.", FP)

t3 = doc.add_table(rows=17, cols=4)
t3_pr = t3._element.find(qn("w:tblPr"))
if t3_pr is None:
    t3_pr = OxmlElement("w:tblPr")
    t3._element.insert(0, t3_pr)
t3_style = t3_pr.find(qn("w:tblStyle"))
if t3_style is None:
    t3_style = OxmlElement("w:tblStyle")
    t3_pr.insert(0, t3_style)
t3_style.set(qn("w:val"), "Table")

hdr = t3.rows[0].cells
hdr[0].text = "Panel / Sample"
hdr[1].text = "N"
hdr[2].text = "Focal coefficient"
hdr[3].text = "Joint test"

t3_rows = [
    ("A. TCI_full direct (2015)", "956",
     "TCI_full_z = 0.056 (p = .253) n.s.; DAI_z = −0.033 n.s.",
     "M3 joint p = .492 n.s."),
    ("A. TCI_full direct (2023)", "1,013",
     "TCI_full_z = 0.096 (p = .024) *; DAI_z = 0.097 (p = .037) *",
     "M3 joint p = .152 n.s."),
    ("B. DAI_rich continuous (2023)", "1,013",
     "FSTS_c × DAI_rich_cont_z = −0.933 (p = .076) †",
     "M8 joint p = .099 †"),
    ("B. DAI_rich binary (2023)", "1,013",
     "FSTS_c × DAI_rich_bin_z = −0.893 (p = .169) n.s.",
     "M8 joint p = .243 n.s."),
    ("C. Common-N reconciled (2023)", "1,013",
     "DAI_z moderation re-estimated on identical 2023 sample",
     "M8 joint p = .062 † (matches main 2023 M8)"),
    ("D. Micro-firm exclusion (l1 ≥ 10)", "2,473",
     "TCI_z = 0.188 ***; DAI_z = 0.054 n.s.",
     "M8 joint p = .167 n.s."),
    ("G. Manufacturing (sector1 ∈ {1,2,3})", "1,854",
     "TCI_z = 0.223 ***; DAI_z = 0.087 **; FSTS_c × DAI_z = −0.543 †",
     "M8 joint p = .103 †"),
    ("H. Exporter-only (FSTS > 0, pooled)", "669",
     "FSTS_c = −0.861 ***; FSTS_c² = −0.200 n.s.",
     "M8 joint p = .462 n.s."),
    ("I. Wave × focal interaction (pooled)", "2,958",
     "DAI_z × wave detectable (p = .016); FSTS_c, FSTS_c², TCI_z × wave n.s.",
     "Only DAI direct shifts cross-wave-separable"),
    ("Density around TP (±5 pp band)", "29 of 2,958",
     "1.0 % of firms within band; bulk of mass at FSTS = 0",
     "Curvature identified by participation margin"),
    ("J. PSM ATT — website (1-NN, caliper 0.05)", "1,085",
     "ATT_DAI = 0.298 *** (SE 0.061)",
     "Positive and large under matching"),
    ("J. PSM ATT — website (kernel BW 0.06)", "1,085",
     "ATT_DAI = 0.321 *** (SE 0.043)",
     "Robust to algorithm"),
    ("J. PSM ATT — cert / foreign-tech (1-NN)", "640",
     "ATT_TCI = 0.637 *** (SE 0.078)",
     "Positive and large under matching"),
    ("K. IV / 2SLS — DAI_z (industry × region IV)", "2,298",
     "DAI_z = 0.018 (p = .942) n.s.",
     "First-stage F = 34.6 (strong); positive OLS DAI direct effect attenuates under IV"),
    ("K. IV / 2SLS — TCI_z (industry × region IV)", "2,298",
     "TCI_z = 1.639 *** (SE 0.299)",
     "First-stage F = 22.1 (strong); TCI direct effect reinforced under IV"),
    ("Oster (2019) δ = 1 bounds", "2,958",
     "FSTSc 0.92 → 0.61; FSTSc² −2.21 → −1.17; TCI 0.14 → 0.19; DAI 0.07 → 0.08",
     "No sign change; focal qualitative findings stable"),
]
for i, row in enumerate(t3_rows, start=1):
    for j, val in enumerate(row):
        t3.rows[i].cells[j].text = val

add_para(doc,
    "Notes. Each row summarises one robustness panel from §4.5 estimated "
    "by OLS with HC1 robust standard errors. Significance markers: *** "
    "p < .001, ** p < .01, * p < .05, † p < .10, n.s. = not significant. "
    "Panel E (Heckman / control function) and Panel F (Paternoster "
    "cross-wave z-tests) are reported in the prose because their natural "
    "presentation is per-sample rather than per-row. Source: World Bank "
    "Enterprise Surveys (https://www.enterprisesurveys.org); authors’ "
    "calculations. Full coefficient output: "
    "p4_vietnam/output/tables/table_3_robustness.csv.", BT)

# Table LM — turning points + Lind–Mehlum p-values ------------------------
add_para(doc,
    "Table LM reports the implied turning points of the inverted-U "
    "specification (M2) and the Lind–Mehlum p-values for each wave and "
    "the pooled sample.", FP)

tLM = doc.add_table(rows=5, cols=5)
tLM_pr = tLM._element.find(qn("w:tblPr"))
if tLM_pr is None:
    tLM_pr = OxmlElement("w:tblPr")
    tLM._element.insert(0, tLM_pr)
tLM_style = tLM_pr.find(qn("w:tblStyle"))
if tLM_style is None:
    tLM_style = OxmlElement("w:tblStyle")
    tLM_pr.insert(0, tLM_style)
tLM_style.set(qn("w:val"), "Table")

lm_hdr = tLM.rows[0].cells
lm_hdr[0].text = "Sample"
lm_hdr[1].text = "N"
lm_hdr[2].text = "Turning point (raw FSTS)"
lm_hdr[3].text = "95 % delta-method CI"
lm_hdr[4].text = "Lind–Mehlum p"

lm_rows = [
    ("VNM 2009",   "989",   "46.2 %", "[37.4 %, 55.1 %]", ".006"),
    ("VNM 2015",   "956",   "39.3 %", "[30.3 %, 48.4 %]", ".009"),
    ("VNM 2023", "1,013",   "41.6 %", "[31.7 %, 51.5 %]", ".013"),
    ("VNM pooled", "2,958", "39.7 %", "[34.0 %, 45.5 %]", "< .001"),
]
for i, row in enumerate(lm_rows, start=1):
    for j, val in enumerate(row):
        tLM.rows[i].cells[j].text = val

add_para(doc,
    "Notes. Turning points are derived from the M2 inverted-U "
    "specification (lnLP = β₀ + β₁ FSTS_c + β₂ FSTS_c² + controls + sector "
    "FE [+ wave FE in pooled]) and back-transformed to the raw FSTS scale. "
    "95 % confidence intervals use the delta method on the within-sample "
    "FSTSc range. Lind–Mehlum p-values follow the Sasabuchi-style endpoint "
    "test for an inverted-U over the observed FSTS range. Source: World "
    "Bank Enterprise Surveys (https://www.enterprisesurveys.org); authors’ "
    "calculations.", BT)

# 5. Discussion ----------------------------------------------------------------
add_para(doc, "5. Discussion", H1)

add_para(doc, "5.1 Reinterpreting digital capability in Vietnam", H2)
add_para(doc, 
    "The central implication of the findings is that digital capability in Vietnam "
    "should not be interpreted as a universal and temporally stable premium. Both "
    "TCI_z and DAI_z are beneficial on average, but their empirical salience changes "
    "across waves. This means that digitalisation is not simply a constant background "
    "advantage. It is a context-sensitive and stage-dependent source of performance "
    "heterogeneity.", FP)
add_para(doc, 
    "This interpretation helps reconcile the coexistence of positive pooled effects "
    "and uneven wave-specific results. The pooled model captures the average "
    "tendency for stronger capability to be associated with better performance. The "
    "wave-specific models show that this tendency is not equally strong in every "
    "phase. The value of digital capability therefore depends on where firms stand in "
    "the broader lifecycle of internationalisation and transition.", BT)

add_para(doc, "5.2 Why the distinction between TCI and DAI matters", H2)
add_para(doc,
    "The results strengthen the theoretical case for separating "
    "foreign-technology / standards capability from website-based "
    "digital presence. The PSM and IV evidence in §4.5 (Panels J and "
    "K) makes the distinction sharper. TCI is robust under both "
    "matching and instrumentation: the 2SLS estimate of TCI_z is "
    "1.64 (p < .001) under a strong instrument (first-stage F = "
    "22.1), and the matching ATT for the cert / foreign-tech "
    "treatment is 0.61–0.64 (p < .001) on a matched sample of "
    "approximately 640 firms. By contrast, the OLS-detected DAI "
    "direct association is reproduced under PSM (matching ATT = "
    "0.30–0.32, p < .001) but attenuates to a null under 2SLS "
    "(β = 0.02, p = .94). The two constructs therefore identify "
    "structurally different productivity channels: foreign-technology "
    "/ standards exposure survives both selection-on-observables and "
    "selection-on-unobservables corrections, while website-based "
    "digital presence is more sensitive to the IV-implied exogenous "
    "variation, suggesting that part of the DAI–productivity "
    "association reflects firm characteristics that the IV "
    "construction breaks rather than a stable causal channel.", FP)
add_para(doc,
    "The DAI_rich extension reported in §4.5 Panel B reinforces the "
    "construct interpretation rather than weakening it. Although the "
    "primary DAI_z anchored on c22b (website presence) is by 2023 "
    "close to a Tier-1 baseline indicator, the DAI_rich extension "
    "available only in 2023 — combining c22b with electronic-payment "
    "shares (k33, k38) — produces a similarly directioned and "
    "marginally significant moderation pattern (FSTS_c × DAI_rich_"
    "cont_z = −0.93, M8 joint p = .099). Whether digital adoption is "
    "measured by the thin Tier-1 website indicator or by the deeper "
    "Tier-2 / 3 transaction items, the 2023 moderation pattern goes "
    "in the same direction. This common-direction evidence guards "
    "against the proxy-obsolescence reading of the DAI pattern in "
    "isolation: even under a richer measurement that is harder to "
    "dismiss as a routine marker, the within-2023 moderation is "
    "consistent with the headline finding.", BT)
add_para(doc,
    "The difference between TCI and DAI matters because the two "
    "constructs do not behave identically across periods or under "
    "different identification strategies. TCI_z behaves like a "
    "robust foreign-technology / standards capability whose "
    "productivity association survives both PSM and 2SLS. DAI_z "
    "behaves like a context-sensitive marker whose productivity "
    "association is documented under matched comparison but not "
    "under exogenous instrumental variation. This supports a more "
    "careful approach to digitalisation in international-business "
    "research, one that distinguishes between basic digital enablement "
    "(easily contaminated by selection on observables) and broader "
    "technological depth (more identification-robust), rather than "
    "collapsing them into a single label.", BT)

add_para(doc, "5.2.1 An alternative reading: proxy obsolescence", H2)
add_para(doc,
    "A purely stage-contingency interpretation is not the only reading of "
    "the wave-specific DAI pattern. An alternative — and to a degree "
    "complementary — explanation is proxy obsolescence: the c22b indicator "
    "of website ownership measures something different in 2009, 2015 and "
    "2023 even though the question text is identical across waves. In 2009, "
    "having a corporate website was a relatively distinguishing market "
    "interface that signalled basic digital legitimacy in international "
    "transactions; by 2023, a website is closer to a routine marker of "
    "basic digital presence shared across exporting and non-exporting firms "
    "alike. Under this reading, the falling DAI direct association across "
    "waves partly reflects the shrinking informational content of c22b "
    "rather than a structural change in the productivity payoff to "
    "foundational digital adoption itself. We do not view proxy "
    "obsolescence and stage contingency as mutually exclusive: both can be "
    "operating jointly. We flag the proxy-obsolescence reading because it "
    "is not testable within the cross-wave-comparable WBES instrument and "
    "future work using waves with richer Tier 2–3 digital items will be "
    "needed to disentangle the two channels.", FP)

add_para(doc, "5.3 The significance of the 2015 dip", H2)
add_para(doc,
    "The 2015 pattern is especially revealing. It shows that even "
    "when the nonlinear I–P structure becomes clearer, the direct "
    "payoff from website-based digital presence can compress to a "
    "null. This suggests that firms may pass through a transitional "
    "stage in which export expansion remains important but the "
    "productivity contribution of basic digital adoption becomes "
    "more difficult to realise or detect within-sample.", FP)
add_para(doc,
    "We treat the 2015 compression honestly as a wave-specific "
    "association consistent with stage contingency rather than as a "
    "fully cross-wave-identified structural shift. As reported in "
    "§4.5 Panel I, the formal pooled wave × focal interaction test "
    "detects only the DAI direct shifts as cross-wave-distinguishable; "
    "the FSTS curvature and the FSTS × DAI moderation cross-wave "
    "differences are not statistically separable. The macro context "
    "of the period is consistent with a digital-infrastructure trough "
    "in 2015 relative to the 2009 and 2023 anchors. Public secondary "
    "indicators support this reading. World Bank World Development "
    "Indicators (WDI) record Vietnam's individuals-using-the-Internet "
    "share at approximately 26 % in 2009, 45 % in 2015 and over 78 % "
    "by 2023; ITU's fixed-broadband subscriptions per 100 people grew "
    "from approximately 3 in 2009 to 8 in 2015 and to over 20 by "
    "2023. Vietnam's National Digital Transformation Programme (NDTP) "
    "was issued in 2020, and cross-border e-payment platforms (VNPAY, "
    "MoMo, ZaloPay) and B2B exporter marketplaces (Alibaba.com, "
    "Amazon Global Selling) reached scale in Vietnam only after 2018–"
    "2019. The 2015 wave therefore observes Vietnamese exporters "
    "during a transitional infrastructure phase in which a website "
    "could not yet plug into a transaction-supporting digital "
    "ecosystem; the 2023 wave observes them after the post-NDTP "
    "scaffolding had matured. We do not treat these macro indicators "
    "as identifying variation — they are not entered into the "
    "regression — but they make the wave-specific reading "
    "institutionally plausible rather than purely post-hoc.", BT)
add_para(doc,
    "Rather than treating this wave as an anomaly, it is more useful "
    "to interpret it as evidence of wave-specific heterogeneity that "
    "is consistent with stage contingency. The dip demonstrates why "
    "pooled averages alone are insufficient. Without the wave-"
    "specific analysis, one would miss the possibility that "
    "capability payoffs compress or fade temporarily before re-"
    "emerging in a later phase, even when the curvature parameters "
    "of the I–P relationship themselves remain statistically "
    "indistinguishable across waves.", BT)

add_para(doc, "5.4 Managerial implications", H2)
add_para(doc, 
    "The managerial implication is not that firms should invest less in "
    "digitalisation. Rather, it is that digitalisation should be aligned with "
    "organisational readiness and international scale. Foundational digital tools may "
    "create value, but the payoff depends on whether those tools are embedded in "
    "routines that support export coordination and performance.", FP)
add_para(doc, 
    "Managers should also avoid conflating basic digital adoption with deeper "
    "technological capability. A firm may adopt digital tools without having the "
    "learning and upgrading capacity needed to sustain performance gains over time. "
    "Conversely, stronger internal capability may allow the firm to convert "
    "relatively basic digital adoption into more meaningful outcomes. This "
    "distinction is especially important in transitional economies, where firms move "
    "through uneven stages of capability development.", BT)

add_para(doc, "5.5 Policy implications", H2)
add_para(doc,
    "We frame the policy reading as tentative considerations rather than directive "
    "prescriptions. The associational nature of the evidence, the breadth of the "
    "wave-specific heterogeneity, and the single-economy scope all weigh against "
    "converting the findings into firm policy targets. With those caveats kept "
    "explicit, three considerations follow for Vietnam’s trade and digital-economy "
    "policy design.", FP)
add_para(doc,
    "First, export-promotion instruments designed around a uniformly positive "
    "internationalisation premium will overshoot in transitional periods such as "
    "the 2015 wave, when capability payoffs were compressed even as export intensity "
    "remained productivity-relevant. Targeting export support at firms positioned in "
    "the entry-cost zone, rather than at firms already operating at high export "
    "intensity, is consistent with the curvature documented in the pooled and "
    "later-wave samples. Second, digital-economy programmes that treat foundational "
    "adoption (websites, basic e-payment) as a sufficient policy lever are likely to "
    "be attenuated by the implementation lag and by the conditional nature of the "
    "digital channel at higher export intensity. Programmes that bundle Tier 1–2 "
    "digital adoption with deeper capability upgrading — quality certification, "
    "absorptive-capacity investment, organisational routines for cross-border "
    "coordination — will be more consistent with the pattern that emerges in 2023.", BT)
add_para(doc,
    "Third, the lifecycle reading suggests that policy evaluation windows matter. "
    "A digital-transformation programme assessed only against a 2015-style "
    "transitional baseline would understate its long-run productivity contribution; "
    "a programme assessed against a 2009-style or 2023-style baseline would "
    "overstate it relative to the in-between phase. Policy evaluation that takes "
    "the lifecycle structure seriously will couple short-window outcome measurement "
    "with sustained measurement of the capability and infrastructure environment "
    "in which firms operate.", BT)

# 6. Limitations and future research ------------------------------------------
add_para(doc, "6. Limitations and future research", H1)
add_para(doc,
    "The findings should be read against five limitations. First and most "
    "fundamentally, the WBES microdata are repeated cross-sections rather than a "
    "true firm panel. Within-firm change over time cannot be identified, and "
    "time-invariant unobserved heterogeneity cannot be netted out at the firm level. "
    "The associational language used throughout the paper reflects this constraint "
    "and should not be relaxed in any reader’s interpretation of the results.", FP)
add_para(doc,
    "Second, the DAI_z composite captures a foundational layer of digital adoption "
    "(digital presence and basic digital transaction support) rather than the full "
    "depth of digitally integrated organisational capability. The DAI_rich extension "
    "for the 2023 wave shows that the conditional pattern survives when richer items "
    "are available, but a panel of digitally integrated firms with deeper measurement "
    "would tighten the construct further.", BT)
add_para(doc,
    "Third, the analysis is conducted on a single transitional economy. Vietnam is "
    "informative precisely because its institutional and digital environment shifted "
    "noticeably across the 2009–2023 observation window, but the lifecycle pattern "
    "documented here may not generalise without modification to economies whose "
    "digital infrastructure or export composition follows a different trajectory.", BT)
add_para(doc,
    "Fourth, although the Paternoster (1998) z-tests reported in §4.5 confirm "
    "that the DAI_z drop between 2009 and 2015 is a statistically distinguishable "
    "cross-wave shift (z = 3.353, p < .001) and the 2015-to-2023 recovery is also distinguishable (z = −2.051, p = .040). Most other cross-wave coefficient "
    "differences sit at marginal or non-significant magnitudes. The lifecycle "
    "narrative therefore relies more on the directional consistency of "
    "wave-specific estimates and the joint moderation tests than on uniformly "
    "significant pairwise z-tests. Future work could exploit policy timing — "
    "for example, Vietnam’s National Digital Transformation Programme launched "
    "in 2020 — for sharper identification of the digital channel through a "
    "policy-evaluation design rather than a cross-wave comparison.", BT)
add_para(doc,
    "Fifth, the sector fixed effects in the main models are intentionally "
    "broad to keep the cross-wave specification comparable. Section 4.5 "
    "Panel G addresses one natural extension by re-estimating the pooled "
    "M2 / M7 / M8 specifications on manufacturing (sector1 ∈ {1, 2, 3}; "
    "N = 1,854) versus non-manufacturing (sector1 ∈ {4, 5, 6, 7}; N = "
    "1,104) subsets, and shows that the digital-adoption channel "
    "operates primarily in manufacturing while the technological-"
    "capability channel is present in both. Finer industry-level "
    "mechanisms — for example, contrasting digitally intensive services "
    "with traditional services, or contrasting export-oriented with "
    "domestically oriented manufacturing sub-sectors — would benefit "
    "from a research design that exploits richer industry classification "
    "than the WBES one-digit codes allow.", BT)

# 7. Conclusion ----------------------------------------------------------------
add_para(doc, "7. Conclusion", H1)
add_para(doc,
    "This study revisits the I–P relationship in Vietnam by distinguishing "
    "technological capability from foundational digital adoption and by comparing "
    "pooled and wave-specific evidence. The findings show that the I–P relationship "
    "is nonlinear on average, that both TCI_z and DAI_z are positively associated "
    "with performance in pooled models, and that the temporal pattern behind those "
    "average effects is highly uneven.", FP)
add_para(doc,
    "The central theoretical implication is that digital capability in a transitional "
    "economy is best understood as a stage-contingent resource. Its value is real, "
    "but it is not uniformly distributed across time or across stages of "
    "internationalisation. This lifecycle perspective helps explain why average "
    "estimates can be informative while still concealing important differences in the "
    "timing and form of digital payoff.", BT)

# Author contributions (suppressed in blinded version) -----------------------
if not BLINDED:
    add_para(doc, "Author contributions", H1)
    add_para(doc,
        "Do Thuy Huong contributed to conceptualisation, data curation, formal "
        "analysis, investigation, methodology, visualisation, and drafting of "
        "the manuscript. Phan Anh Tu contributed to conceptualisation, "
        "supervision, methodology, validation, review and editing, and overall "
        "guidance of the study. Both authors approved the final version of the "
        "manuscript.", FP)

# Conflict of interest --------------------------------------------------------
add_para(doc, "Conflict of interest", H1)
add_para(doc, "The authors declare no conflict of interest.", FP)

# Funding ---------------------------------------------------------------------
add_para(doc, "Funding", H1)
add_para(doc,
    "This research received no specific grant from any funding agency in "
    "the public, commercial, or not-for-profit sectors.", FP)

# Data availability statement -------------------------------------------------
add_para(doc, "Data availability statement", H1)
add_para(doc,
    "The data that support the findings of this study are from the World "
    "Bank Enterprise Surveys and are available from the World Bank "
    "Enterprise Surveys portal, subject to registration and compliance "
    "with the World Bank Enterprise Surveys Data Access Protocol. Because "
    "the protocol restricts redistribution of the original .dta files to "
    "third parties, the authors do not redistribute the raw survey files. "
    "Replication materials, including variable-construction details, "
    "model specifications, and computational outputs, are available from "
    "the authors upon reasonable request and may be shared to the extent "
    "permitted by the data-access terms.", FP)

# Use of generative AI ---------------------------------------------------------
add_para(doc, "Use of generative AI in the writing process", H1)
add_para(doc,
    "Generative AI tools were used during manuscript preparation to assist "
    "with language editing, structure suggestions, and the assembly of the "
    "replication package documentation. All conceptual framing, hypothesis "
    "development, empirical analysis, results interpretation, and final "
    "wording were authored by the human authors, who take full "
    "responsibility for the content of the publication.", FP)

# Acknowledgements -------------------------------------------------------------
add_para(doc, "Acknowledgements", H1)
add_para(doc,
    "This study uses data from the World Bank Enterprise Surveys. We thank "
    "the Enterprise Analysis Unit of the Development Economics Global "
    "Indicators Group of the World Bank for providing access to the data. "
    "The original collector of the data, the authorised distributor, and "
    "the relevant funding agency bear no responsibility for the use of the "
    "data or for interpretations based on such use. The findings, "
    "interpretations, and conclusions expressed in this article are those "
    "of the authors and do not necessarily represent the views of the "
    "World Bank Group, its Executive Directors, or the governments they "
    "represent. The authors received no specific grant from any funding "
    "agency in the public, commercial, or not-for-profit sectors. The "
    "replication package accompanying this manuscript was developed to "
    "support methodological transparency and computational "
    "reproducibility.", FP)

# Supplementary CSV outputs (replication package pointers) ---------------------
add_para(doc, "Supplementary materials", H1)
add_para(doc,
    "All figures and tables in the manuscript are embedded inline. The "
    "underlying coefficient outputs are also distributed as plain CSV files "
    "in the replication package for downstream re-analysis: "
    "tables/table_1_descriptives.csv (Table 1), "
    "tables/coefs_main_models.csv (M0–M8 long-format coefficient table), "
    "tables/joint_tests_main_models.csv (H2 and P1 joint F-tests), "
    "tables/table_lind_mehlum.csv (Table LM source), "
    "tables/table_3_robustness.csv (Table 3 panels A–D + G), "
    "tables/selection_checks.csv (Heckman / control function), and "
    "tables/table_paternoster.csv (cross-wave z-tests). Replication "
    "package and instructions: see p4_vietnam/README.md.", FP)

# References -------------------------------------------------------------------
add_para(doc, "References", H1)
references = [
    'Antonakis, J., Bendahan, S., Jacquart, P. and Lalive, R. (2010), '
    '"On making causal claims: A review and recommendations", '
    'The Leadership Quarterly, Vol. 21 No. 6, pp. 1086-1120.',
    'Banalieva, E.R. and Dhanaraj, C. (2019), "Internalization theory '
    'for the digital economy", Journal of International Business Studies, '
    'Vol. 50 No. 8, pp. 1372-1387.',
    'Bharadwaj, A., El Sawy, O.A., Pavlou, P.A. and Venkatraman, N. (2013), '
    '"Digital business strategy: Toward a next generation of insights", '
    'MIS Quarterly, Vol. 37 No. 2, pp. 471-482.',
    'Brynjolfsson, E., Rock, D. and Syverson, C. (2021), '
    '"The productivity J-curve: How intangibles complement general purpose '
    'technologies", American Economic Journal: Macroeconomics, Vol. 13 '
    'No. 1, pp. 333-372.',
    'Cohen, W.M. and Levinthal, D.A. (1990), "Absorptive capacity: A new '
    'perspective on learning and innovation", Administrative Science '
    'Quarterly, Vol. 35 No. 1, pp. 128-152.',
    'Coviello, N., Kano, L. and Liesch, P.W. (2017), "Adapting the '
    'Uppsala model to a modern world: Macro-context and microfoundations", '
    'Journal of International Business Studies, Vol. 48 No. 9, pp. 1151-1164.',
    'Cuervo-Cazurra, A. and Genc, M. (2008), "Transforming disadvantages '
    'into advantages: Developing-country MNEs in the least developed '
    'countries", Journal of International Business Studies, Vol. 39 No. 6, '
    'pp. 957-979.',
    'Heckman, J.J. (1979), "Sample selection bias as a specification '
    'error", Econometrica, Vol. 47 No. 1, pp. 153-161.',
    'Hanelt, A., Bohnsack, R., Marz, D. and Antunes Marante, C. (2021), '
    '"A systematic review of the literature on digital transformation: '
    'Insights and implications for strategy and organizational change", '
    'Journal of Management Studies, Vol. 58 No. 5, pp. 1159-1197.',
    'Helfat, C.E. and Peteraf, M.A. (2003), "The dynamic resource-based '
    'view: Capability lifecycles", Strategic Management Journal, Vol. 24 '
    'No. 10, pp. 997-1010.',
    'Hennart, J.-F. (2007), "The theoretical rationale for a '
    'multinationality–performance relationship", Management International '
    'Review, Vol. 47 No. 3, pp. 423-452.',
    'Lall, S. (1992), "Technological capabilities and industrialization", '
    'World Development, Vol. 20 No. 2, pp. 165-186.',
    'Lind, J.T. and Mehlum, H. (2010), "With or without U? The appropriate '
    'test for a U-shaped relationship", Oxford Bulletin of Economics and '
    'Statistics, Vol. 72 No. 1, pp. 109-118.',
    'Lu, J.W. and Beamish, P.W. (2004), "International diversification and '
    'firm performance: The S-curve hypothesis", Academy of Management '
    'Journal, Vol. 47 No. 4, pp. 598-609.',
    'Marano, V., Arregle, J.-L., Hitt, M.A., Spadafora, E. and van Essen, '
    'M. (2016), "Home country institutions and the internationalization–'
    'performance relationship: A meta-analytic review", Journal of '
    'Management, Vol. 42 No. 5, pp. 1075-1110.',
    'Nambisan, S., Wright, M. and Feldman, M. (2019), "The digital '
    'transformation of innovation and entrepreneurship: Progress, '
    'challenges and key themes", Research Policy, Vol. 48 No. 8, '
    'article 103773.',
    'Paternoster, R., Brame, R., Mazerolle, P. and Piquero, A. (1998), '
    '"Using the correct statistical test for the equality of regression '
    'coefficients", Criminology, Vol. 36 No. 4, pp. 859-866.',
    'Teece, D.J. (2007), "Explicating dynamic capabilities: The nature and '
    'microfoundations of (sustainable) enterprise performance", Strategic '
    'Management Journal, Vol. 28 No. 13, pp. 1319-1350.',
    'Verhoef, P.C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, '
    'J.Q., Fabian, N. and Haenlein, M. (2021), "Digital transformation: A '
    'multidisciplinary reflection and research agenda", Journal of '
    'Business Research, Vol. 122, pp. 889-901.',
    'Vial, G. (2019), "Understanding digital transformation: A review '
    'and a research agenda", Journal of Strategic Information Systems, '
    'Vol. 28 No. 2, pp. 118-144.',
    'Vernon, R. (1979), "The product cycle hypothesis in a new '
    'international environment", Oxford Bulletin of Economics and '
    'Statistics, Vol. 41 No. 4, pp. 255-267.',
    'Wagner, J. (2007), "Exports and productivity: A survey of the '
    'evidence from firm-level data", The World Economy, Vol. 30 No. 1, '
    'pp. 60-82.',
    'Wooldridge, J.M. (2010), Econometric Analysis of Cross Section and '
    'Panel Data, 2nd ed., MIT Press, Cambridge, MA.',
    'World Bank (2010), Vietnam Enterprise Survey 2009: Data file, World '
    'Bank Enterprise Surveys, available at: '
    'https://www.enterprisesurveys.org',
    'World Bank (2016), Vietnam Enterprise Survey 2015: Data file, World '
    'Bank Enterprise Surveys, available at: '
    'https://www.enterprisesurveys.org',
    'World Bank (2024), Vietnam Enterprise Survey 2023: Data file, World '
    'Bank Enterprise Surveys, available at: '
    'https://www.enterprisesurveys.org',
    'Wright, M., Filatotchev, I., Hoskisson, R.E. and Peng, M.W. (2005), '
    '"Strategy research in emerging economies: Challenging the '
    'conventional wisdom", Journal of Management Studies, Vol. 42 No. 1, '
    'pp. 1-33.',
    'Wu, J., Wang, C., Hong, J., Piperopoulos, P. and Zhuo, S. (2016), '
    '"Internationalization and innovation performance of emerging market '
    'enterprises: The role of host-country institutional development", '
    'Journal of World Business, Vol. 51 No. 2, pp. 251-263.',
]
for ref in references:
    add_para(doc, ref, BT)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc.save(OUTPUT)
print(f"Wrote {OUTPUT}")
