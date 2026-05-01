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
add_para(doc, "v4.5 — md-guided revision (Vietnam, three-wave lifecycle)", "Subtitle")
add_para(doc, "2026-05-01", "Date")

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
    "Using three waves of harmonised firm-level evidence from the World Bank Enterprise "
    "Survey for Vietnam (2009, 2015, 2023), we distinguish a Technological Capability "
    "Index (TCI_z) from a Digital Adoption Index (DAI_z) and evaluate their roles in "
    "both pooled and wave-specific OLS specifications with HC1 robust covariance. The "
    "findings indicate that the internationalisation–performance relationship is "
    "nonlinear in the pooled evidence and is especially visible in the later waves. In "
    "the pooled full model, both TCI_z and DAI_z are positively associated with firm "
    "performance, indicating that both deeper capability stocks and foundational digital "
    "adoption are beneficial on average. However, the wave-specific evidence reveals "
    "substantial temporal heterogeneity: both TCI and DAI are strongly positive in 2009, "
    "lose salience in 2015, and re-emerge in 2023, when digital adoption also becomes "
    "more tightly connected to export intensity.", BT)
add_para(doc, 
    "These findings suggest that digital capability in a transitional economy should "
    "not be interpreted as a universal premium. Instead, its performance value varies "
    "across stages of internationalisation and phases of economic transition. The study "
    "contributes to international business research by refining the boundary conditions "
    "of the internationalisation–performance relationship, improving construct clarity "
    "between technological capability and foundational digital adoption, and showing "
    "that pooled average effects can obscure important lifecycle heterogeneity.", BT)
add_para(doc, 
    "Keywords: internationalisation–performance relationship; digital adoption; "
    "technological capability; Vietnam; firm performance; lifecycle heterogeneity.", BT)

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
    "the usable samples are 977 observations for 2009, 964 for 2015, and 1,013 for "
    "2023. The pooled full model contains 2,954 observations. This structure provides "
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
    "The models also include standard firm-level controls: firm size (lnEmp), firm "
    "age (FirmAge), and foreign ownership (ForeignOwned). Sector fixed effects use the "
    "broad ISIC classification. In pooled specifications, wave fixed effects are "
    "added to absorb broad period differences. Listwise deletion is applied on the "
    "focal variable set, with WBES non-response codes treated as missing.", BT)

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

# 4. Results -------------------------------------------------------------------
add_para(doc, "4. Results", H1)

add_para(doc, "4.1 Wave-specific findings", H2)
add_para(doc, 
    "The wave-specific evidence reveals clear temporal heterogeneity. In 2009, both "
    "capability constructs are strongly and positively associated with performance. "
    "In the full 2009 model, TCI_z is positive and highly significant (β = 0.274, p < "
    ".001), and DAI_z is also positive and highly significant (β = 0.210, p < .001). "
    "However, the interaction terms involving DAI_z are not significant in that wave. "
    "This indicates that, in the earlier phase, both technological capability and "
    "foundational digital adoption operate primarily as direct "
    "performance-enhancing resources rather than as robust moderators of the I–P "
    "relationship.", FP)
add_para(doc, 
    "The 2015 wave shows a different configuration. The I–P relationship becomes more "
    "clearly nonlinear in that period: in the full model, the linear FSTS_c term is "
    "positive and significant (β = 1.653, p = .041), while the quadratic FSTS_c² term "
    "is negative and significant (β = −2.175, p = .010). At the same time, both "
    "capability measures lose direct salience. TCI_z becomes statistically "
    "insignificant (β = 0.071, p = .297), and DAI_z is likewise insignificant (β = "
    "0.006, p = .928). The interaction terms involving DAI_z also remain "
    "insignificant. This suggests a transitional phase in which export intensity "
    "matters, but the performance payoff from capability variables becomes more "
    "muted.", BT)
add_para(doc, 
    "The 2023 evidence reveals another shift. The nonlinear structure remains "
    "visible, with a positive linear FSTS_c term (β = 1.338, p = .112) and a negative "
    "quadratic FSTS_c² term that is statistically significant (β = −1.942, p = .023). "
    "More importantly, both capability measures regain direct significance: TCI_z is "
    "positive (β = 0.140, p = .013) and DAI_z is positive (β = 0.161, p = .012). In "
    "addition, the linear interaction between FSTS_c and DAI_z is negative and "
    "reaches the conventional significance threshold (β = −1.072, p = .050), "
    "suggesting that the performance relevance of digital adoption becomes more "
    "conditional on export intensity in the later wave.", BT)
add_para(doc, 
    "Taken together, the wave-specific results suggest a lifecycle pattern rather "
    "than a stable cross-period rule. The direct payoff from both TCI_z and DAI_z is "
    "strong in 2009, weak in 2015, and positive again in 2023, with digital adoption "
    "becoming more conditional in the later wave.", BT)

add_para(doc, "4.2 Pooled findings", H2)
add_para(doc, 
    "The pooled results confirm that the I–P relationship is nonlinear on average. In "
    "the pooled nonlinear model, the linear FSTS_c term is positive and significant "
    "(β = 1.207, p = .003), while the quadratic FSTS_c² term is negative and "
    "significant (β = −1.714, p < .001). This pattern remains in the pooled full "
    "model, where the linear term is positive (β = 1.036, p = .023) and the "
    "quadratic term remains negative and significant (β = −1.487, p = .002). This "
    "supports H1 and aligns with the broader nonlinear logic emphasised in prior "
    "international business research (Marano et al., 2016).", FP)
add_para(doc, 
    "The pooled evidence also shows that both capability dimensions are positively "
    "associated with firm performance on average. In the pooled full model, TCI_z is "
    "positive and statistically significant (β = 0.138, p < .001), and DAI_z is also "
    "positive and statistically significant (β = 0.125, p < .001). These estimates "
    "indicate that, when averaged across waves, both deeper technological capability "
    "and foundational digital adoption are performance enhancing, supporting H2 and "
    "H3.", BT)
add_para(doc, 
    "The pooled interaction terms involving DAI_z, however, are not statistically "
    "significant. The linear interaction between FSTS_c and DAI_z is negative but "
    "insignificant (β = −0.573, p = .170), and the quadratic interaction is positive "
    "but insignificant (β = 0.460, p = .298). This matters because it shows that the "
    "pooled average should not be interpreted as evidence of a stable moderation "
    "effect across time. Instead, the pooled model masks meaningful stage-specific "
    "heterogeneity.", BT)
add_para(doc, 
    "If the analysis stopped at pooled estimation, one might conclude that "
    "digitalisation provides a broadly positive but structurally simple performance "
    "premium. The wave-specific evidence shows that this conclusion would be "
    "incomplete. The positive pooled average coexists with substantial temporal "
    "heterogeneity, and the conditional role of digital adoption emerges more "
    "clearly only in the later wave.", BT)

add_para(doc, "4.3 Interpretation of the hypothesis tests", H2)
add_para(doc, 
    "H1 is supported because the pooled evidence indicates a nonlinear relationship "
    "between internationalisation and firm performance, and the later waves display "
    "the same logic more clearly. H2 is supported because TCI_z is positively "
    "associated with performance in the pooled evidence and in two of the three "
    "wave-specific periods. H3 is also supported because DAI_z is positively "
    "associated with performance on average and in two of the three waves.", FP)
add_para(doc, 
    "H4 receives partial but meaningful support. The pooled interaction terms do not "
    "indicate a stable conditional role for DAI_z across all periods. However, the "
    "wave-specific analysis shows that the role of DAI_z changes over time and "
    "becomes more conditionally linked to export intensity in 2023. This is "
    "consistent with the broader claim that digital capability is stage contingent "
    "rather than uniformly valuable in the same way across all phases.", BT)

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
    ("2009 full model",
     "Not clearly supported in full model",
     "0.274 (p < .001)",
     "0.210 (p < .001)",
     "Not significant"),
    ("2015 full model",
     "FSTS_c positive (1.653, p = .041); FSTS_c² negative (−2.175, p = .010)",
     "0.071 (p = .297) n.s.",
     "0.006 (p = .928) n.s.",
     "Not significant"),
    ("2023 full model",
     "FSTS_c² negative and significant (−1.942, p = .023)",
     "0.140 (p = .013)",
     "0.161 (p = .012)",
     "FSTS_c × DAI_z = −1.072 (p = .050)"),
    ("Pooled full model",
     "FSTS_c positive (1.036, p = .023); FSTS_c² negative (−1.487, p = .002)",
     "0.138 (p < .001)",
     "0.125 (p < .001)",
     "Not significant"),
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

# 6. Conclusion ----------------------------------------------------------------
add_para(doc, "6. Conclusion", H1)
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
add_para(doc, 
    "The study also has limitations. The analysis is observational, and the available "
    "digital measure captures a foundational layer of adoption rather than the full "
    "depth of digitally integrated organisational capability. Future research could "
    "extend this approach by using richer digital measures, more detailed industry "
    "differentiation, and stronger causal identification designs.", BT)

# References -------------------------------------------------------------------
add_para(doc, "References", H1)
references = [
    "Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital "
    "business strategy: Toward a next generation of insights. MIS Quarterly, 37(2), "
    "471–482. https://doi.org/10.25300/MISQ/2013/37:2.3",
    "Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective "
    "on learning and innovation. Administrative Science Quarterly, 35(1), 128–152. "
    "https://doi.org/10.2307/2393553",
    "Lall, S. (1992). Technological capabilities and industrialization. World "
    "Development, 20(2), 165–186.",
    "Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). "
    "Home country institutions and the internationalization–performance relationship: "
    "A meta-analytic review. Journal of Management, 42(5), 1075–1110. "
    "https://doi.org/10.1177/0149206315624963",
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
