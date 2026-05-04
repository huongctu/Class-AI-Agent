# Thiết kế chi tiết P8 — Pacific SIDS Forced Internationalization Penalty

File này định vị P8 Pacific SIDS paper trong kiến trúc dissertation. Manuscript gốc (`P9_SIDS_v2_REVISED.docx`, `Paper7_v7_COMPLETE.md`) đã hoàn thiện và submit World Development. File này là **dissertation chapter view** — cách P8 đóng vai trò trong cumulative thesis.

## 1. Định vị trong dissertation

### 1.1 Vai trò — Extreme boundary case

P8 đóng vai trò **extreme boundary case** trong **institutional gradient narrative** của dissertation:

| Cluster | Paper | Functional form | Institutional regime |
|---|---|---|---|
| High-quality institutions | P3 Singapore | Inverted-U classic, optimum ~71% FSTS | Regime I |
| Transitional | P4 Vietnam | Resource Diversion Trap, optimum ~37–44% | Regime II |
| Evolving | P5 China 2012–2024 | Vanishing inverted-U over time | Regime II→I |
| Multi-country mainland | P7 Asian capstone (25–36 countries) | Heterogeneous w/ moderation | Regimes I–III |
| **Extreme institutional voids** | **P8 Pacific SIDS** | **REVERSED slope (Forced Penalty)** | **Regime IV/V** |

→ P8 cung cấp **biên ngoài** của institutional spectrum, hoàn thiện buức tranh inverted-U lyà **conditional relationship**, không phải universal law.

### 1.2 Vị trí trong cấu trúc 5 chương

P8 đi vào **Ch.4.4 — Boundary condition test** sau khi trình bày P3-P5 country-level (Ch.4.2) và P7 multi-country (Ch.4.3). Ch.5 (Thảo luận) duùng P8 luàm extreme case đyể demonstrate institutional gradient.

### 1.3 Differentiation từ các paper khác trong dissertation

| Paper | Sample | Theoretical contribution | DV |
|---|---|---|---|
| P3 Singapore | 1 country, ASEAN benchmark | Inverted-U classic confirmation | $\ln(LP)$ |
| P4 Vietnam | 1 country, transitional | Resource Diversion Trap | ROS / $\ln(LP)$ |
| P5 China | 1 country, 2 waves | Temporal evolution of nonlinearity | $\ln(LP)$ |
| P7 Asian capstone | 25–36 countries mainland | Three-way moderation in mainland | $\ln(LP)$ |
| **P8 Pacific SIDS** | **8 Pacific countries, 12 waves** | **Forced Penalty as boundary condition** | **$\ln(LP)$ + domestic-sales productivity** |

P8 không trùng với P3–P5 (single mainland Asian) và với P7 (mainland multi-country) vì:
- **Sample**: Pacific SIDS, **không** mainland Asia
- **Functional form**: REVERSED slope, **không** inverted-U
- **Theoretical mechanism**: Forced Penalty (3 violated assumptions), **không** Resource Diversion hoặc temporal evolution

## 2. Theoretical positioning

### 2.1 Forced Internationalization Penalty — named contribution

Khái niệm **Forced Internationalization Penalty** là **named theoretical contribution** của P8, giống như:
- Lu & Beamish (2004) với "S-curve"
- Contractor et al. (2003) với "three-stage theory"
- Bartlett & Ghoshal (1989) với "transnational solution"

Forced Penalty xảy ra khi 3 prerequisites của inverted-U đều **không được đáp ứng**:

1. **Viable domestic market** — Tonga 104K people, Micronesia 94K people: thị trường nội địa không sủc support firm growth
2. **Manageable trade costs** — Winters & Martins (2004): cost amplification 30–210% trong remote economies
3. **Functional institutions** — Khanna & Palepu (2010): institutional voids comprehensive trong SIDS

### 2.2 Kết nối với khung 4 tầng + digital lens

P8 áp dụng khung 4 tầng nhưng với **outcome ngược**:

| Tầng | Mainland Asia (P3-P7) | Pacific SIDS (P8) |
|---|---|---|
| **Thể chế** | Voids selective, moderates I-P | Voids comprehensive, **disables** I-P benefits |
| **Năng lực doanh nghiệp** | Capabilities shift inverted-U up | Capabilities raise productivity but **không moderate** I-P |
| **Top manager** | Gender + experience moderate I-P | (Limited variation in small SIDS samples) |
| **Huình dyạng quan hệ** | Inverted-U / S-curve / vanishing | **Reversed slope** |

### 2.3 Theoretical contribution — boundary conditions

P8 chuứng minh inverted-U paradigm cyó **structural prerequisites**, mu1edf ruộng tu1eeb "institutional moderation" (Marano et al. 2016) sang "institutional dependency":

- **Marano et al. (2016)**: institutional quality **moderates** I-P relationship intensity
- **P8 (Forced Penalty)**: institutional regime **determines** existence and **sign** of I-P relationship

→ Move from variation in **degree** to variation in **kind**.

## 3. Empirical summary (để người đọc dissertation hiểu nhanh)

### 3.1 Sample

- 1,207 firms
- 8 Pacific Island nations: Fiji, Kiribati, Federated States of Micronesia, Papua New Guinea, Samoa, Solomon Islands, Tonga, Vanuatu
- 12 country-year datasets, 2009–2025
- 172 exporters (14.3%)

### 3.2 Key findings

| Finding | Coefficient | p-value | Implication |
|---|---|---|---|
| DOI × productivity (exporters only) | $\beta = -0.033$ | $p = .035$ | **Forced Penalty confirmed** |
| DOI (no fixed effects) | $\beta = -0.028$ | $p = .012$ | Negative across full sample |
| DOI² (domestic-sales productivity) | $\beta = -0.021$ | $p = .071$ | Deeper internationalization erodes domestic efficiency |
| Quality certification (signaling) | $\beta = 0.372$ | $p = .003$ | Strongest capability predictor |
| Foreign technology licensing (seizing) | $\beta = 0.214$ | $p = .030$ | Production efficiency channel |
| Website ownership (sensing) | $\beta = 0.149$ | $p = .062$ | Modest sensing channel |
| Foreign ownership | exp(0.500)−1 | (45-65% premium) | Institutional substitution |

### 3.3 R-squared decomposition

- Country fixed effects alone: 62.3%
- Firm-level variables alone: 14.0%
- Full model: 65.7%
- **95% of explained variance is between-country**

→ Methodological insight: cross-country WBES regressions cuần carefully interpret country-level vs firm-level effects.

## 4. Methodological contributions

### 4.1 Formative measurement decomposition

Thay vì composite digital capability index với Cronbach's $\alpha = 0.23$, P8 dùng **3 formative indicators**:

- **Website (c22b)** — sensing
- **Foreign tech licensing (j6a)** — seizing
- **International quality certification (b8)** — signaling

Theo Hair et al. (2022) + Diamantopoulos & Winklhofer (2001) + Jarvis et al. (2003). Low inter-item correlation ($r = 0.07-0.13$) **theoretically expected** in formative model.

### 4.2 Two-part model

- Extensive margin: Probit cho export participation ($N = 1,207$)
- Intensive margin: OLS exporters only ($N = 172$)

→ Tách biệt **selection effect** và **conditional intensity effect**.

### 4.3 Multiple robustness

- Quantile regression at median
- Drop-one-country (8 iterations)
- Heckman two-step selection correction
- Post-2020 wave interaction
- Domestic-sales productivity (addresses simultaneity)
- Employment growth (sales-independent DV)

## 5. Submission status

- **Manuscript**: Paper7_v7 / P9_SIDS_v2_REVISED — hoàn thiện REVISED v2
- **Target journal**: World Development
- **Cover letter**: đã có (`Paper7_v7_CoverLetter.md`)
- **Highlights**: 5 bullet points (`Paper7_v7_Highlights.md`)
- **Anonymous version**: có (`Paper7_v7_Anonymous_Manuscript.docx`)
- **Tables**: `P9_SIDS_Paper_Tables.xlsx`
- **Figures**: `Figure1_SIDS_TriPanel.png`, `Figure2_SIDS_FSTS.png`

## 6. Cách trình bày trong dissertation

### 6.1 Trong Chương 1 (Introduction)

Khi giới thiệu dissertation, nêu:
- Dissertation bảo quát **Asian + adjacent regions** (không strict Asia)
- Pacific SIDS là **extreme test** của institutional moderation thesis
- 4 paper mạch: P3 (regime I) → P4 (regime II) → P5 (regime II→I) → **P8 (regime IV/V)**

### 6.2 Trong Chương 2 (Theory)

- 2.5 Khung 4 tầng + digital lens áp dụng across institutional gradient
- 2.6 Forced Penalty là **boundary case** mu1edf ruộng theory

### 6.3 Trong Chương 4 (Results)

- 4.4 Pacific SIDS findings — contrast với mainland Asia
- 4.5 Synthesis: institutional gradient hypothesis confirmed

### 6.4 Trong Chương 5 (Discussion)

- 5.1 Theoretical implications: inverted-U **conditional**, không universal
- 5.2 Boundary conditions: 3 structural prerequisites
- 5.3 Policy: Antigua and Barbuda Agenda — implications cho SIDS
- 5.4 Limitations: scope expansion (Pacific in Asian dissertation)
- 5.5 Future research: panel dimension cho 4 SIDS countries có 2 waves

## 7. Tham khyảo chính (đyầy đyủ trong `04_references_apa7.md`)

- Briguglio, L. (1995). Small island developing states and their economic vulnerabilities. *World Development, 23*(9), 1615–1632.
- Briguglio, L., Cordina, G., Farrugia, N., & Vella, S. (2009). Economic vulnerability and resilience. *Oxford Development Studies, 37*(3), 229–247.
- Diamantopoulos, A., & Winklhofer, H. M. (2001). Index construction with formative indicators. *Journal of Marketing Research, 38*(2), 269–277.
- Doh, J. P., Rodrigues, S., Saka-Helmhout, A., & Makhija, M. (2017). International business responses to institutional voids. *Journal of International Business Studies, 48*(3), 293–307.
- Goedhuys, M., & Sleuwaegen, L. (2013). The impact of international standards certification. *World Development, 46*, 87–101.
- Hair, J. F., Hult, G. T. M., Ringle, C. M., & Sarstedt, M. (2022). *A primer on partial least squares structural equation modeling* (3rd ed.). Sage.
- Jarvis, C. B., MacKenzie, S. B., & Podsakoff, P. M. (2003). A critical review of construct indicators. *Journal of Consumer Research, 30*(2), 199–218.
- Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets*. Harvard Business Press.
- Read, R. (2004). The implications of increasing globalization. *World Development, 32*(2), 365–378.
- Teece, D. J. (2007). Explicating dynamic capabilities. *Strategic Management Journal, 28*(13), 1319–1350.
- Terlaak, A., & King, A. A. (2006). The effect of certification with the ISO 9000 Quality Management Standard. *Journal of Economic Behavior & Organization, 60*(4), 579–602.
- United Nations General Assembly. (2024). *The Antigua and Barbuda Agenda for Small Island Developing States* (A/RES/78/317).
- Vahlne, J.-E., & Johanson, J. (2020). The Uppsala model: Networks and micro-foundations. *Journal of International Business Studies, 51*(1), 4–10.
- Verbeke, A., & Brugman, M. (2018). Internationalization and performance. *Journal of International Business Studies, 49*(7).
- Winters, L. A., & Martins, P. M. G. (2004). When comparative advantage is not enough. *World Trade Review, 3*(3), 347–383.
- Xu, P., & Takase, K. (2025). *Financial constraints and firm performance in Small Island Developing States* [Working paper].
