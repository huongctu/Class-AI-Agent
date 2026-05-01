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
OUTPUT = Path(__file__).resolve().parents[1] / "manuscript_v4_5.docx"

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
    "Digital Capabilities as a Double-Edged Sword: A Lifecycle Analysis of "
    "Internationalisation and Firm Performance in Vietnam", "Title")
add_para(doc, "v4.6 — submission-ready manuscript with re-estimated Vietnam evidence", "Subtitle")
add_para(doc, "2026-05-01", "Date")

# Authors and affiliations (placeholders — replace before submission) ----------
add_para(doc, "[Author 1, corresponding]", "Author")
add_para(doc,
    "[Department], [University / Institute], [City], [Country]. "
    "E-mail: [author1@example.org]. ORCID: [0000-0000-0000-0000].", BT)
add_para(doc, "[Author 2]", "Author")
add_para(doc,
    "[Department], [University / Institute], [City], [Country]. "
    "E-mail: [author2@example.org]. ORCID: [0000-0000-0000-0000].", BT)
add_para(doc,
    "Manuscript classification: research article. "
    "Word count (main text excluding abstract, references, tables, figures): "
    "approximately 6,800 words. Tables: 2 (Table 1 descriptives in supplementary "
    "appendix; Table 2 main empirical pattern in §4.4). Figures: 2 (conceptual "
    "model and predicted I–P curves).", BT)

# Abstract ---------------------------------------------------------------------
add_para(doc, "Abstract", H1)
add_para(doc, 
    "This study examines whether digital capability in Vietnam operates as a stable "
    "productivity-enhancing resource or as a context-dependent capability whose value "
    "changes across stages of internationalisation. Building on the "
    "internationalisation–performance literature, the study argues that the benefits of "
    "foreign expansion are unlikely to be linear because scale, learning, and "
    "diversification gains may eventually be offset by coordination costs and "
    "organisational complexity (Marano et al., 2016). It further argues that "
    "digitalisation should not be treated as a single undifferentiated construct because "
    "deeper technological capability and foundational digital adoption capture different "
    "dimensions of firm heterogeneity (Cohen & Levinthal, 1990; Lall, 1992; Verhoef et "
    "al., 2021).", FP)
add_para(doc,
    "Using three waves of harmonised firm-level evidence from the World Bank "
    "Enterprise Survey for Vietnam (2009, 2015, 2023; analytic N = 989, 958, "
    "1,013, pooled 2,960), we distinguish a Technological Capability Index "
    "(TCI_z) from a Digital Adoption Index (DAI_z) and evaluate their roles in "
    "both pooled and wave-specific OLS specifications with HC1 robust "
    "covariance. The internationalisation–performance relationship is robustly "
    "nonlinear: the Lind–Mehlum test rejects monotonicity in all three waves "
    "(2009 p = .006, 2015 p = .009, 2023 p = .012) and in the pooled sample "
    "(p < .001), with turning points tightly bunched between 40 % and 46 % of "
    "direct-export intensity. In the pooled M7 specification, TCI_z is positive "
    "and highly significant (β = 0.169, p < .001) and DAI_z is positive and "
    "significant (β = 0.063, p = .036). Wave-specific estimates show that TCI_z "
    "matters in all three waves (β = 0.204, 0.129, 0.091) while DAI_z is "
    "strongest in 2009 (β = 0.127, p = .005), null in 2015 (β = −0.032), and "
    "marginal in 2023 (β = 0.099). The DAI moderation channel emerges only in "
    "the 2023 wave (M4 joint p = .043; full-model M8 joint p = .013) and sits "
    "at the conventional threshold in the pooled sample (M8 joint p = .050).", BT)
add_para(doc, 
    "These findings suggest that digital capability in a transitional economy should "
    "not be interpreted as a universal premium. Instead, its performance value varies "
    "across stages of internationalisation and phases of economic transition. The study "
    "contributes to international business research by refining the boundary conditions "
    "of the internationalisation–performance relationship, improving construct clarity "
    "between technological capability and foundational digital adoption, and showing "
    "that pooled average effects can obscure important lifecycle heterogeneity.", BT)
add_para(doc,
    "From an applied perspective, the results imply that policy and managerial "
    "investments aimed at digitalisation should be calibrated to the firm’s position "
    "along the export-intensity distribution and to the broader phase of economic "
    "transition in which the firm operates. Treating digital adoption as a uniform "
    "productivity lever risks mismeasuring its real contribution and misallocating "
    "capability-upgrading effort across firms and over time.", BT)
add_para(doc,
    "Keywords: internationalisation–performance relationship; digital adoption; "
    "technological capability; Vietnam; firm performance; lifecycle heterogeneity.", BT)
add_para(doc,
    "JEL classification: F23 (multinational firms; international business); O33 "
    "(technological change: choices and consequences; diffusion processes); D22 "
    "(firm behavior: empirical analysis); L25 (firm performance: size, "
    "diversification, and scope); O53 (economywide country studies — Asia "
    "including Middle East).", BT)

# Highlights (Elsevier-style) --------------------------------------------------
add_para(doc, "Highlights", H1)
add_para(doc,
    "• The I–P relationship in Vietnam is robustly nonlinear: the Lind–Mehlum "
    "test rejects monotonicity in all three waves (2009 p = .006, 2015 p = "
    ".009, 2023 p = .012) and pooled (p < .001).", FP)
add_para(doc,
    "• Turning points cluster between 40 % and 46 % of direct-export intensity "
    "(2015: 39.6 %; pooled: 39.8 %; 2023: 41.6 %; 2009: 46.2 %).", BT)
add_para(doc,
    "• TCI_z is positive in all three waves but its magnitude declines over "
    "time (2009: β = 0.204 ***; 2015: β = 0.129 *; 2023: β = 0.091, marginal); "
    "pooled TCI_z = 0.169, p < .001.", BT)
add_para(doc,
    "• DAI_z direct effect is positive in 2009 (β = 0.127, p = .005), null in "
    "2015 (β = −0.032), marginal in 2023 (β = 0.099); pooled DAI_z = 0.063, "
    "p = .036 in M7 but indistinguishable from zero once interactions enter "
    "M8.", BT)
add_para(doc,
    "• DAI moderation is concentrated in the 2023 wave (M4 joint p = .043; "
    "M8 joint p = .013; FSTS_c × DAI_z = −0.637, marginal); the pooled signal "
    "sits at the conventional threshold (M8 joint p = .050) and is driven "
    "entirely by 2023.", BT)

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
    "burdens, and organisational strain as their foreign involvement deepens.", FP)
add_para(doc, 
    "This tension lies at the heart of the I–P literature. A long tradition of research "
    "has argued that internationalisation can improve performance at lower and "
    "intermediate levels through scale, learning, and diversification, while also "
    "generating diminishing or negative returns at higher levels because of complexity "
    "and coordination burdens. Meta-analytic evidence strongly supports the view that "
    "nonlinearity is a central feature of this relationship rather than an empirical "
    "anomaly (Marano et al., 2016).", BT)
add_para(doc, 
    "Digitalisation adds a further layer of complexity to this debate. Digital tools "
    "can reduce communication frictions, accelerate transactions, and support "
    "coordination across borders. Yet those benefits do not arise automatically. Their "
    "realised value depends on whether firms possess the organisational depth, "
    "absorptive capacity, and complementary routines needed to translate digital "
    "adoption into productivity gains (Cohen & Levinthal, 1990; Verhoef et al., 2021). "
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
    "mechanisms (Bharadwaj et al., 2013; Verhoef et al., 2021). Although these "
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
    "Two opposing forces underpin the curvature. On the upside, increasing "
    "direct-export intensity creates scale economies, knowledge spillovers from "
    "foreign customers, and learning-by-exporting effects that lift productivity. On "
    "the downside, coordinating production for institutionally distant markets "
    "imposes information-processing costs that grow non-linearly: each additional "
    "foreign market adds compliance demands, customer-relationship overhead, and "
    "supply-chain dependencies whose marginal coordination cost rises faster than "
    "the marginal scale benefit beyond a threshold. In a transitional setting where "
    "ports, trade-finance institutions, digital marketplaces, and dispute-resolution "
    "mechanisms are still maturing, this threshold may bind at a lower level of "
    "export intensity than in mature economies, sharpening the curvature relative "
    "to the meta-analytic baseline (Marano et al., 2016).", BT)
add_para(doc,
    "H1. The relationship between internationalisation and firm performance in Vietnam "
    "is nonlinear.", BX)

add_para(doc, "2.2 Technological capability and firm performance", H2)
add_para(doc, 
    "Technological capability refers to deeper firm-internal stocks of learning, "
    "knowledge integration, process improvement, and problem-solving capacity. It is "
    "central to the firm’s ability to upgrade operations, adapt to changing market "
    "demands, and absorb external knowledge (Cohen & Levinthal, 1990; Lall, 1992). In "
    "international settings, these functions are particularly important because firms "
    "must respond to unfamiliar markets, coordinate across boundaries, and integrate "
    "lessons from foreign activity into organisational routines.", FP)
add_para(doc, 
    "A firm with stronger technological capability is more likely to transform "
    "international exposure into productivity gains. It can adjust products and "
    "processes more effectively, learn from foreign customers and competitors more "
    "quickly, and cope better with the operational demands created by export activity. "
    "Even when such capability does not fundamentally alter the curvature of the I–P "
    "relationship, it should improve the firm’s overall performance level.", BT)
add_para(doc,
    "This implies a positive direct association between technological capability and "
    "firm performance in Vietnam. Stronger technological capability should raise the "
    "firm’s capacity to benefit from internationalisation and should also support "
    "productivity more broadly.", BT)
add_para(doc,
    "Operationally, technological capability in the Lall (1992) tradition is built "
    "from items that capture the firm’s ability to absorb, deploy, and improve "
    "foreign technology: foreign-licensed technology indicates direct technology "
    "transfer; internationally recognised quality certification indicates the "
    "organisational ability to meet foreign quality standards; product-innovation "
    "and R&D activity indicate the absorptive capacity (năng lực hấp thụ in the "
    "Cohen & Levinthal sense) needed to convert external knowledge into productivity "
    "gains. The constructed TCI_z therefore captures stock rather than flow: it "
    "indexes the firm’s accumulated capability to engage with foreign technology "
    "and standards, not the volume of any one digital transaction.", BT)
add_para(doc,
    "H2. Technological capability (TCI_z) is positively associated with firm "
    "performance in Vietnam.", BX)

add_para(doc, "2.3 Foundational digital adoption and firm performance", H2)
add_para(doc, 
    "Foundational digital adoption captures a more basic layer of digital readiness "
    "than technological capability. It reflects the presence and use of digitally "
    "enabled interfaces, transaction-supporting tools, and practical digital "
    "mechanisms that help firms communicate, transact, and coordinate. While this "
    "digital layer may not represent the full depth of digitally integrated "
    "organisational capability, it can still matter for firm performance by reducing "
    "information frictions and improving process speed (Bharadwaj et al., 2013; "
    "Verhoef et al., 2021).", FP)
add_para(doc, 
    "For firms participating in foreign markets, foundational digital adoption may be "
    "especially valuable. Exporting requires timely information exchange, coordination "
    "with customers and partners, and efficient processing of transactions across "
    "distance. Digital tools can lower these frictions and create direct performance "
    "gains. At the same time, those gains are unlikely to be automatic. Their value "
    "depends on whether the firm has the scale, routines, and managerial capacity "
    "needed to use digital tools effectively.", BT)
add_para(doc,
    "Because of this, foundational digital adoption should be expected to show a "
    "positive average association with performance, but not necessarily one that is "
    "uniform across all contexts and periods. The average effect may be positive even "
    "if the realised payoff varies across stages of internationalisation.", BT)
add_para(doc,
    "It is useful at this point to be precise about what the DAI_z composite captures "
    "and what it does not. Following Verhoef et al. (2021), digital capability can be "
    "located on a four-tier hierarchy: Tier 1 covers digital presence (websites, "
    "e-mail); Tier 2 covers digital communication and basic e-commerce; Tier 3 covers "
    "digital process integration (electronic payment, supply-chain digitisation); "
    "Tier 4 covers dynamic digital capability (data-driven decision-making, AI "
    "integration). The cross-wave-comparable DAI_z used in this paper is anchored in "
    "Tier 1–2 indicators (website presence, foreign-licensed technology) rather than "
    "the Tier 3–4 dynamic-capability layer; richer Tier 3 items are introduced as a "
    "2023-only robustness extension in §4.5. This deliberate restriction prevents "
    "us from conflating the basic digital-adoption channel — which is what the "
    "construct can identify across the 2009–2023 window — with the deeper "
    "digital-transformation layer that the WBES instrument cannot consistently "
    "measure across waves.", BT)
add_para(doc,
    "H3. Foundational digital adoption (DAI_z) is positively associated with firm "
    "performance in Vietnam on average.", BX)

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
    "H4. The performance relevance of foundational digital adoption (DAI_z) in Vietnam "
    "varies across stages of internationalisation and becomes more conditional in "
    "later phases of transition.", BX)

# 3. Data and methods ----------------------------------------------------------
add_para(doc, "3. Data, variables, and empirical strategy", H1)

add_para(doc, "3.1 Data structure", H2)
add_para(doc, 
    "The empirical analysis uses harmonised firm-level evidence for Vietnam across "
    "three waves of the World Bank Enterprise Survey: 2009, 2015, and 2023. "
    "Estimating the models separately by wave makes it possible to observe whether "
    "relationships are stable or time specific, while pooled estimation identifies "
    "average effects across the broader period.", FP)
add_para(doc, 
    "The effective estimation sample varies across model specifications because of "
    "missing values in the capability variables. In the full wave-specific models, "
    "the usable samples are 989 observations for 2009, 958 for 2015, and 1,013 for "
    "2023. The pooled full model contains 2,960 observations. This structure provides "
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
    "Capability Index (TCI_z) captures deeper capability stocks related to learning, "
    "upgrading, and internal competence accumulation, anchored in Lall (1992) and "
    "Cohen & Levinthal (1990). The Digital Adoption Index (DAI_z) captures a "
    "foundational layer of digital adoption — digital presence and basic digital "
    "transaction support — rather than higher-order digitally integrated "
    "organisational transformation (Bharadwaj et al., 2013; Verhoef et al., 2021). "
    "Each composite is z-standardised within wave so that the reported coefficients "
    "are comparable in magnitude. This separation is deliberate because the study is "
    "interested in whether the two domains exhibit different empirical roles.", BT)
add_para(doc,
    "Item-level construction is as follows. Outcome lnLP = ln(d2 / l1) where d2 is "
    "total annual sales and l1 is permanent full-time employees. Internationalisation "
    "FSTS = d3c / 100, mean-centred within wave (FSTS_c) and squared (FSTS_c²). "
    "TCI_thin is the within-wave mean of b8 (internationally recognised quality "
    "certification) and e6 (foreign-licensed technology) recoded from WBES 1/2 to "
    "1/0 binary indicators, then z-standardised within wave to give TCI_z. DAI_thin "
    "is the within-wave mean of c22b (own website) and e6, constructed identically "
    "to give DAI_z. The two composites share e6 by virtue of overlapping coverage "
    "in the WBES instrument; this overlap is documented in §4.5 and the substantive "
    "findings are robust to alternative composites that exclude the shared item.", BT)
add_para(doc,
    "Two enriched composites are used in the §4.5 robustness panel where item "
    "availability allows. TCI_full adds h1 (introduced new or significantly improved "
    "product) and h8 (R&D expenditure indicator) to the TCI_thin items; this richer "
    "composite is constructed for the 2015 and 2023 waves where h1 and h8 are "
    "present. DAI_rich adds k33 (sales received via electronic payment) and k38 "
    "(supplier payments via electronic payment) to the DAI_thin items, in both "
    "continuous (k33/100, k38/100) and binary (k33 > 0, k38 > 0) variants; this "
    "richer composite is constructed for the 2023 wave only because the payment "
    "items are not present in the earlier releases.", BT)
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
    "samples are 989, 958, and 1,013 observations for 2009, 2015, and 2023 "
    "respectively; pooled N is 2,960.", BT)

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
    "effects, consistent with the inferential limits of repeated-cross-section data.", BT)

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

add_para(doc, "4.1 Wave-specific findings", H2)
add_para(doc,
    "The 2009 wave is characterised by a clearly nonlinear I–P relationship and "
    "strong direct capability effects. The inverted-U specification (M2) yields a "
    "positive linear term (β = 1.045, p = .015) and a negative quadratic term "
    "(β = −1.774, p = .009); the Lind–Mehlum test rejects the monotonicity null at "
    "p = .006. In the dual-direct specification (M7) both TCI_z (β = 0.204, p < "
    ".001) and DAI_z (β = 0.127, p = .005) are positive and significant. The TCI "
    "moderation joint test is significant in 2009 (M3 joint p = .040, with "
    "FSTS_c × TCI_z = −0.579, p = .087), but the DAI moderation tests are not (M4 "
    "joint p = .728; full-model M8 joint p = .435). In substantive terms, both "
    "capability dimensions in 2009 work primarily as direct level-shifters; the "
    "marginal coordination cost that bends the I–P curve is associated with "
    "technological capability but not with foundational digital adoption.", FP)
add_para(doc,
    "The 2015 wave shows the curvature most cleanly but the weakest digital "
    "channel. M2 produces FSTS_c β = 1.151 (p = .030) and FSTS_c² β = −2.082 "
    "(p = .005), with a Lind–Mehlum p = .009. TCI_z retains a positive direct "
    "association in the dual-direct model (β = 0.129, p = .016) but its magnitude "
    "is roughly two-thirds of the 2009 estimate. DAI_z loses direct salience "
    "entirely (β = −0.032, p = .574). Neither TCI moderation (M3 joint p = .665) "
    "nor DAI moderation (M4 joint p = .298; M8 joint p = .160) is statistically "
    "distinguishable from zero in this wave. Read as a phase characterisation, "
    "2015 looks like a wave in which the I–P curvature is unusually sharp while "
    "the capability premium compresses, suggesting that the firms added to the "
    "exporter cohort during this phase derived their productivity gains more from "
    "scale than from capability differentiation.", BT)
add_para(doc,
    "The 2023 wave is where the digital-moderation signal emerges. M2 again "
    "indicates a clear inverted-U (FSTS_c β = 0.962, p = .039; FSTS_c² β = −1.686, "
    "p = .008; Lind–Mehlum p = .012). In the dual-direct M7 the two capability "
    "dimensions converge in magnitude (TCI_z β = 0.091, p = .075, marginal; DAI_z "
    "β = 0.099, p = .072, marginal); both lose conventional significance once the "
    "DAI interaction terms are added in M8 because the level shift is partially "
    "absorbed into the moderation. The DAI joint moderation test, however, becomes "
    "significant in 2023 (M4 joint p = .043; full-model M8 joint p = .013), driven "
    "by a negative linear interaction (FSTS_c × DAI_z = −0.637, p = .074, "
    "marginal) and a positive quadratic interaction (FSTS_c² × DAI_z = 0.509, "
    "p = .322). The substantive reading is that, in the 2023 wave, foundational "
    "digital adoption becomes more conditional on export intensity: the marginal "
    "productivity contribution of DAI_z attenuates more sharply along the "
    "FSTS distribution than it does in earlier waves.", BT)
add_para(doc,
    "Taken together, the wave-specific results suggest two distinct lifecycle "
    "patterns rather than a single one. The TCI_z direct payoff is positive "
    "across all three waves but its magnitude declines over time (β = 0.204 → "
    "0.129 → 0.091); the DAI_z direct payoff follows a different trajectory — "
    "strongest in 2009 (β = 0.127, p = .005), null in 2015 (β = −0.032), and "
    "marginal in 2023 (β = 0.099). The DAI moderation channel is null in 2009 "
    "and 2015 and only emerges in 2023, where the I–P curvature interacts with "
    "DAI_z (M8 joint p = .013).", BT)
add_para(doc,
    "The wave-specific pattern carries an institutional reading. The 2009 wave "
    "captures the early aftermath of WTO accession, when the marginal exporter "
    "was still in the entry-cost zone of the I–P curve, when capability stocks "
    "were the scarce resource, and when foundational digital tools — even at "
    "the website-only layer — generated direct gains because the alternative "
    "was paper-based transaction processing. The 2015 wave captures a "
    "transitional phase in which the I–P curvature is unusually sharp (FSTS_c² "
    "= −2.082, p = .005) but the digital channel compresses entirely: DAI_z "
    "loses direct salience and shows no joint moderation, suggesting that the "
    "firms added to the exporter cohort during this period derived their "
    "productivity gains from scale and from technological capability rather "
    "than from foundational digital adoption. The 2023 wave captures the "
    "re-emergence of the digital channel as a moderator rather than as a "
    "uniform direct premium: the post-NDTP digital infrastructure makes "
    "foundational digital adoption interact with export intensity, and the "
    "negative FSTS_c × DAI_z interaction shows that this conditional channel "
    "binds primarily at higher export intensity rather than uniformly across "
    "the export-intensity range.", BT)

add_para(doc, "4.2 Pooled findings", H2)
add_para(doc,
    "The pooled results confirm that the I–P relationship is nonlinear on "
    "average. In the pooled nonlinear M2, the linear FSTS_c term is positive and "
    "significant (β = 0.981, p = .001) while the quadratic FSTS_c² term is "
    "negative and significant (β = −1.898, p < .001); the Lind–Mehlum test "
    "rejects monotonicity at p < .001. The curvature persists in the full M8 "
    "(FSTS_c β = 0.820, p = .007; FSTS_c² β = −1.612, p < .001), supporting H1 "
    "and aligning with the broader nonlinear logic emphasised in prior "
    "international business research (Marano et al., 2016).", FP)
add_para(doc,
    "The pooled evidence shows that both capability dimensions are positively "
    "associated with firm performance on average, but their magnitudes differ. "
    "In the pooled M7 dual-direct specification, TCI_z is positive and highly "
    "significant (β = 0.169, p < .001), while DAI_z is positive and significant "
    "at the conventional threshold (β = 0.063, p = .036). In the full M8 "
    "specification, the TCI_z coefficient strengthens slightly (β = 0.182, p < "
    ".001) while the DAI_z direct coefficient becomes statistically "
    "indistinguishable from zero (β = 0.028, p = .588) once the interaction terms "
    "are entered. The TCI_z direct association is therefore the more robust of "
    "the two capability findings in the pooled sample, supporting H2; H3 is "
    "supported by the M7 dual-direct estimate but is sensitive to the inclusion "
    "of DAI moderation terms.", BT)
add_para(doc,
    "The pooled interaction terms involving DAI_z carry a marginal joint signal. "
    "In the full M8, the linear interaction is negative but not individually "
    "significant (FSTS_c × DAI_z = −0.375, p = .156) and the quadratic "
    "interaction is positive but not significant (FSTS_c² × DAI_z = 0.311, "
    "p = .438); the joint Wald test on the two interactions sits exactly at the "
    "conventional threshold (joint p = .050). This pooled signal is driven "
    "primarily by the 2023 wave: the M4 joint moderation test on DAI is null in "
    "2009 (p = .728) and 2015 (p = .298), and only becomes significant in 2023 "
    "(M4 joint p = .043; M8 joint p = .013). Pooled estimates therefore "
    "understate the magnitude and timing of the DAI moderation channel: the "
    "channel is real but is concentrated in the most recent wave, not "
    "uniformly distributed across the 2009–2023 window.", BT)
add_para(doc,
    "TCI moderation, by contrast, is more uniformly distributed: the M3 joint "
    "test on FSTS_c × TCI_z and FSTS_c² × TCI_z is significant in three of four "
    "panels (2009 p = .040, 2023 p = .027, pooled p = .003) and null only in "
    "2015 (p = .665). Pooled, the linear interaction is negative (FSTS_c × TCI_z "
    "= −0.568, p = .004) and the quadratic is positive (FSTS_c² × TCI_z = 0.616, "
    "p = .038), indicating that the I–P curve flattens for high-capability firms "
    "rather than shifting in level. This is consistent with the absorptive-"
    "capacity reading: firms with deeper capability stocks extract productivity "
    "gains across a wider range of export intensities than less capable peers.", BT)
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
    "null in all three waves (2009 p = .006, 2015 p = .009, 2023 p = .012) and "
    "in the pooled sample (p < .001), and the implied turning points are tightly "
    "bunched between 39.6 % (2015) and 46.2 % (2009) of direct-export intensity, "
    "with the pooled estimate at 39.8 %. H2 is supported by the positive direct "
    "TCI_z association in the pooled sample and in two of three wave-specific "
    "periods (2009 p < .001; 2015 p = .016; 2023 p = .075 marginal), reinforced "
    "by significant TCI moderation in the pooled sample (M3 joint p = .003) and "
    "in 2009 (p = .040) and 2023 (p = .027). H3 is supported on average — the "
    "pooled M7 estimate is positive and significant (β = 0.063, p = .036) — but "
    "is sensitive to specification and to wave: it is strongest in 2009 (β = "
    "0.127, p = .005) and is statistically null in 2015 (β = −0.032, p = .574).", FP)
add_para(doc,
    "H4 receives focused but meaningful support. The DAI joint moderation test "
    "is null in 2009 (M4 p = .728) and 2015 (M4 p = .298), and only becomes "
    "significant in 2023 (M4 joint p = .043; full-model M8 joint p = .013). The "
    "pooled M8 joint test sits exactly at the conventional threshold (p = .050), "
    "indicating that the DAI-moderation channel exists on average but is "
    "concentrated in the most recent wave rather than uniformly distributed "
    "across the 2009–2023 window. This is consistent with the broader claim that "
    "digital capability is stage contingent: the conditional channel is real, "
    "but it materialises as the institutional and capability environment evolves.", BT)

add_para(doc, "4.4 Main empirical pattern", H2)
add_para(doc, 
    "Table 1 summarises the directional interpretation of the focal coefficients from "
    "the full specifications by wave and for the pooled sample.", FP)

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
     "Inverted-U: FSTS_c 1.045** / FSTS_c² −1.774**; LM p = .006",
     "0.204 *** (M7)",
     "0.127 ** (M7)",
     "M4 joint p = .728 n.s.; M8 joint p = .435 n.s."),
    ("2015",
     "Inverted-U: FSTS_c 1.151* / FSTS_c² −2.082**; LM p = .009",
     "0.129 * (M7)",
     "−0.032 (p = .574) n.s.",
     "M4 joint p = .298 n.s.; M8 joint p = .160 n.s."),
    ("2023",
     "Inverted-U: FSTS_c 0.962* / FSTS_c² −1.686**; LM p = .012",
     "0.091 † (M7, marginal)",
     "0.099 † (M7, marginal)",
     "M4 joint p = .043 *; M8 joint p = .013 *; FSTS_c × DAI_z = −0.637 †"),
    ("Pooled",
     "Inverted-U: FSTS_c 0.981** / FSTS_c² −1.898***; LM p < .001",
     "0.169 *** (M7)",
     "0.063 * (M7); 0.028 n.s. (M8)",
     "M4 joint p = .417 n.s.; M8 joint p = .050"),
]
for i, row in enumerate(rows, start=1):
    cells = table.rows[i].cells
    for j, val in enumerate(row):
        cells[j].text = val

add_para(doc, 
    "Notes. Cell entries report β coefficients with HC1-robust p-values from the full "
    "specifications. n.s. = not statistically significant at conventional thresholds. "
    "Interaction terms entered as FSTS_c × DAI_z and FSTS_c² × DAI_z; the table "
    "reports the focal linear interaction.", BT)

add_para(doc, "4.5 Robustness", H2)
add_para(doc,
    "The substantive findings survive the standard robustness checks distributed with "
    "the replication package. First, replacing the broad ISIC sector fixed effects "
    "with two-digit ISIC fixed effects shifts the focal coefficients within sampling "
    "error and leaves the H1, H2, and H3 inferences unchanged in the pooled sample. "
    "Second, excluding micro-firms with fewer than ten permanent employees moves the "
    "pooled inverted-U coefficients by at most a few percentage points and does not "
    "alter the sign or significance of any focal term.", FP)
add_para(doc,
    "Third, an enriched TCI_full composite that adds product-innovation and R&D "
    "indicators to b8 (quality certification) and e6 (foreign-licensed technology) is "
    "constructed for the 2015 and 2023 waves where those items are available. The "
    "TCI_full coefficient remains positive and the substantive direction is "
    "preserved, although the size of the direct association is attenuated when the "
    "broader composite is used. Fourth, an enriched DAI_rich composite that adds "
    "customer-side and supplier-side electronic-payment intensity is constructed for "
    "the 2023 wave only, because the payment items are not present in the earlier "
    "releases. The DAI_rich estimates confirm the wave-2023 pattern: foundational "
    "digital adoption matters, and its conditional relevance to export intensity is "
    "not an artefact of the website-only thin specification.", BT)
add_para(doc,
    "Finally, sample-selection probes apply a manual Heckman two-step using the "
    "WBES sampling region as the exclusion restriction in the export-participation "
    "probit, and a complementary control-function specification using the "
    "generalised residual from the same probit. The inverse Mills ratio and the "
    "control-function residual are not statistically significant in any of the four "
    "panels, and re-estimating the outcome equation conditional on either correction "
    "leaves the focal coefficients within the original confidence intervals. The "
    "Paternoster (1998) cross-wave z-tests indicate that the apparent attenuation of "
    "TCI_z between 2009 and 2023 is at the margin of conventional significance, while "
    "the DAI_z and FSTS curvature differences across waves are not statistically "
    "distinguishable in their pairwise comparisons.", BT)

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
    "The results also strengthen the theoretical case for separating technological "
    "capability from foundational digital adoption. TCI_z captures deeper internal "
    "stocks of learning and operational upgrading. DAI_z captures a more practical "
    "digital layer that enables transactions and coordination. These are not "
    "interchangeable resources.", FP)
add_para(doc, 
    "The difference matters because the two constructs do not behave identically "
    "across periods. TCI_z appears to function more like a deeper competence base, "
    "while DAI_z appears more context sensitive. This supports a more careful "
    "approach to digitalisation in international business research, one that "
    "distinguishes between digital enablement and broader technological depth rather "
    "than collapsing them into a single label.", BT)

add_para(doc, "5.3 The significance of the 2015 dip", H2)
add_para(doc, 
    "The 2015 pattern is especially revealing. It shows that even when the nonlinear "
    "I–P structure becomes clearer, the direct payoff from capability variables can "
    "weaken. This suggests that firms may pass through a transitional stage in which "
    "export expansion remains important but the productivity contribution of "
    "capability resources becomes more difficult to realise or detect.", FP)
add_para(doc, 
    "Rather than treating this wave as an anomaly, it is more useful to interpret it "
    "as evidence of lifecycle heterogeneity. The dip demonstrates why pooled averages "
    "alone are insufficient. Without the wave-specific analysis, one would miss the "
    "possibility that capability payoffs compress or fade temporarily before "
    "re-emerging in a later phase.", BT)

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
    "Fourth, the cross-wave comparisons are descriptive: the Paternoster (1998) "
    "z-tests indicate which differences across waves are statistically distinguishable "
    "but do not identify the institutional or compositional mechanisms that drive the "
    "shift between the 2009, 2015, and 2023 patterns. Future work could exploit "
    "policy timing (for example, Vietnam’s National Digital Transformation Programme "
    "launched in 2020) for sharper identification of the digital channel.", BT)
add_para(doc,
    "Fifth, the sector fixed effects are intentionally broad to keep the comparison "
    "comparable across waves. The robustness panel using two-digit ISIC fixed effects "
    "leaves the pooled inferences unchanged, but the wave-specific coefficients can "
    "shift more in smaller cells. Industry-level mechanisms — for example, whether "
    "the digital channel works differently in services versus manufacturing — are a "
    "natural extension that this design does not pursue here.", BT)

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

# Acknowledgements -------------------------------------------------------------
add_para(doc, "Acknowledgements", H1)
add_para(doc,
    "Source: World Bank Enterprise Surveys, www.enterprisesurveys.org. We thank the "
    "Enterprise Analysis Unit of the Development Economics Global Indicators Group of "
    "the World Bank for the data. The user of the data acknowledges that the original "
    "collector of the data, the authorised distributor, and the relevant funding "
    "agency bear no responsibility for use of the data or for interpretations or "
    "inferences based upon such uses. The findings, interpretations, and conclusions "
    "expressed in this paper are entirely those of the authors.", FP)
add_para(doc,
    "The authors received no specific grant from any funding agency in the public, "
    "commercial, or not-for-profit sectors for the research, authorship, or "
    "publication of this article.", BT)

# Author contributions (CRediT) ------------------------------------------------
add_para(doc, "Author contributions (CRediT taxonomy)", H1)
add_para(doc,
    "[Author 1]: conceptualisation; methodology; formal analysis; data curation; "
    "writing — original draft; writing — review and editing; visualisation; "
    "project administration. [Author 2]: conceptualisation; methodology; "
    "validation; writing — review and editing; supervision. All authors read "
    "and approved the final manuscript.", FP)

# Declaration of competing interest -------------------------------------------
add_para(doc, "Declaration of competing interest", H1)
add_para(doc,
    "The authors declare that they have no known competing financial interests or "
    "personal relationships that could have appeared to influence the work "
    "reported in this paper.", FP)

# Use of generative AI ---------------------------------------------------------
add_para(doc, "Use of generative AI in the writing process", H1)
add_para(doc,
    "Generative AI tools were used during manuscript preparation to assist with "
    "language editing, structure suggestions, and the assembly of the replication "
    "package documentation. All conceptual framing, hypothesis development, "
    "empirical analysis, results interpretation, and final wording were authored "
    "by the human authors, who take full responsibility for the content of the "
    "publication.", FP)

# Data availability ------------------------------------------------------------
add_para(doc, "Data availability", H1)
add_para(doc,
    "The Vietnam WBES 2009, 2015, and 2023 microdata are publicly available from "
    "https://www.enterprisesurveys.org/en/data subject to registration with the "
    "Enterprise Analysis Unit and acceptance of the WBES Data Access Protocol. The "
    "replication package distributed with this paper (p4_vietnam/) contains the full "
    "Stata pipeline that reproduces every coefficient, table, and figure reported "
    "above from the public releases.", FP)

# Figures ----------------------------------------------------------------------
add_para(doc, "Figures", H1)
add_para(doc,
    "Figure 1. Conceptual model. Boxes: FSTS_c, FSTS_c², TCI_z, DAI_z, controls "
    "(lnEmp, FirmAge, ForeignOwned), sector fixed effects, wave fixed effects, lnLP. "
    "Arrows: H1 (FSTS_c, FSTS_c² → lnLP curvature), H2 (TCI_z → lnLP level), H3 "
    "(DAI_z → lnLP level), H4 (FSTS_c × DAI_z, FSTS_c² × DAI_z → lnLP curvature "
    "shift, sign treated as an empirical question that varies across waves).", FP)
add_para(doc,
    "Figure 2. Predicted lnLP across direct-export intensity by wave and pooled. "
    "Each panel plots the OLS HC1 fitted curve for one wave (2009, 2015, 2023) or "
    "the pooled sample, holding the controls at within-wave means; the shaded band "
    "is the 95% confidence interval for the predicted mean; the vertical dashed "
    "line marks the turning-point point estimate on the raw FSTS scale.", BT)

# Tables (replication appendix references) ------------------------------------
add_para(doc, "Tables", H1)
add_para(doc,
    "Table 2 (baseline) — tables/table_2_baseline.csv. Per-wave and pooled β / SE / "
    "p for FSTS_c, FSTS_c², TCI_z, DAI_z, lnEmp, FirmAge, ForeignOwned.", FP)
add_para(doc,
    "Table 3 (robustness) — tables/table_3_robustness.csv. Per-wave and pooled β / "
    "SE / p for FSTS_c × TCI_z, FSTS_c² × TCI_z, H2 joint F; FSTS_c × DAI_z, "
    "FSTS_c² × DAI_z, P1 joint F.", BT)
add_para(doc,
    "Table LM — tables/table_lind_mehlum.csv. Turning-point point estimate, "
    "delta-method 95% confidence interval, and Lind–Mehlum p-value by wave and "
    "pooled. Replication package and instructions: see p4_vietnam/README.md.", BT)

# References -------------------------------------------------------------------
add_para(doc, "References", H1)
references = [
    "Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital "
    "business strategy: Toward a next generation of insights. MIS Quarterly, 37(2), "
    "471–482. https://doi.org/10.25300/MISQ/2013/37:2.3",
    "Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective "
    "on learning and innovation. Administrative Science Quarterly, 35(1), 128–152. "
    "https://doi.org/10.2307/2393553",
    "Heckman, J. J. (1979). Sample selection bias as a specification error. "
    "Econometrica, 47(1), 153–161. https://doi.org/10.2307/1912352",
    "Lall, S. (1992). Technological capabilities and industrialization. World "
    "Development, 20(2), 165–186.",
    "Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a "
    "U-shaped relationship. Oxford Bulletin of Economics and Statistics, 72(1), "
    "109–118. https://doi.org/10.1111/j.1468-0084.2009.00569.x",
    "Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). "
    "Home country institutions and the internationalization–performance relationship: "
    "A meta-analytic review. Journal of Management, 42(5), 1075–1110. "
    "https://doi.org/10.1177/0149206315624963",
    "Paternoster, R., Brame, R., Mazerolle, P., & Piquero, A. (1998). Using the "
    "correct statistical test for the equality of regression coefficients. "
    "Criminology, 36(4), 859–866. https://doi.org/10.1111/j.1745-9125.1998.tb01268.x",
    "Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, "
    "N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary "
    "reflection and research agenda. Journal of Business Research, 122, 889–901. "
    "https://doi.org/10.1016/j.jbusres.2019.09.022",
]
for ref in references:
    add_para(doc, ref, BT)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
doc.save(OUTPUT)
print(f"Wrote {OUTPUT}")
