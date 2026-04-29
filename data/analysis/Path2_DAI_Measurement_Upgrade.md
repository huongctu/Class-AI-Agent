# Path 2: DAI Measurement Upgrade — From Tier 1-2 to Tier 3-4

**Date**: 29 April 2026
**Source**: 16 strategy PDFs (Verhoef framework, Orbis linkage, FAT survey)
**Applies to**: P3 (Singapore), P4 (Vietnam), P5 (China), Dissertation

---

## 1. Current State: DAI = Tier 1-2 Only

| Tier | What it measures | Current WBES indicators | Status |
|------|-----------------|----------------------|--------|
| **1. Digital infrastructure** | Basic connectivity + presence | c22b website | ✓ In DAI |
| **2. Digital transactions** | E-payment adoption | k33, k38 e-payment % | ✓ In DAI |
| **3. Digital integration** | ERP, CRM, SCM embedded in processes | — | ✗ Not in WBES |
| **4. Digital dynamic capability** | AI, cloud, platform orchestration | — | ✗ Not in WBES |

**Honest label**: "Digital Adoption Index" (DAI) — correctly names Tier 1-2.
**Cannot claim**: "Digital Capability" — that requires Tier 3-4 measurement.

---

## 2. Verhoef et al. (2021) Framework — 4-Tier Hierarchy

### Tier 1: Digitization (converting analog → digital)
- Website presence (c22b)
- Email communication (c22a — legacy, dropped post-2017)
- Broadband connection (c23 — legacy)

### Tier 2: Digitalization (using digital tools in transactions)
- E-payment received (k33)
- E-payment to suppliers (k38)
- E-tax filing (j37)
- Digital exports (d35 — exporters only)

### Tier 3: Digital Transformation (integrating digital into business model)
- ERP/CRM software adoption
- Data analytics for decision-making
- Digital supply chain management
- Online platform sales channels
**Source**: FAT survey (Cirera, Comin & Cruz, 2022), NOT in WBES core

### Tier 4: Digital Dynamic Capability (sensing-seizing-reconfiguring)
- AI/ML deployment
- Cloud-native infrastructure
- Platform ecosystem orchestration
- Digital innovation culture
**Source**: Custom survey / case studies

---

## 3. Upgrade Options — Ranked by Feasibility

### Option A: WBES B-READY Module Expansion (Feasibility: HIGH)

The 2022/2023 B-READY revision added items that push toward Tier 2+:

| Item | Description | Available in | Tier |
|------|------------|-------------|------|
| c36 | Broadband application filed | SGP23, VNM23, CHN24 | 1+ |
| c39 | Broadband presence | SGP23, VNM23, CHN24 | 1 |
| c40a | Days without broadband | SGP23, VNM23, CHN24 | 1 |
| j36 | Electronic tax filing | SGP23, VNM23, CHN24 | 2 |
| j37 | Electronic tax payment | SGP23, VNM23, CHN24 | 2 |
| d35 | Digital exports (exporters) | SGP23, VNM23, CHN24 | 2+ |
| k33 | E-payment % received | SGP23, VNM23, CHN24 | 2 |
| k38 | E-payment % to suppliers | SGP23, VNM23, CHN24 | 2 |
| n2l | Annual broadband cost | SGP23, VNM23, CHN24 | 1 |

**Action**: Build DAI_extended = z(website + k33/100 + k38/100 + j37 + d35)
- j37: binary (e-tax payment) — but 99%+ ceiling in SGP/CHN → drop
- d35: continuous (digital export %) — exporters only → conditional
- Net gain: modest (still Tier 2 ceiling)

### Option B: WBES × Orbis Linkage (Feasibility: LOW-MEDIUM)

**Goal**: Link WBES firm-level data with Orbis financial data to get:
- IT spending / total assets
- Software & intangible assets
- Patent filings (digital-related IPC codes)
- R&D intensity (continuous, not binary)

**Barriers**:
1. WBES public data is **anonymized** — no firm identifiers
2. Need WBES **confidential microdata** access from World Bank
3. Orbis coverage for developing countries (VNM, CHN) is spotty
4. Fuzzy matching by name/location/sector requires significant effort

**Steps if pursuing**:
1. Apply for WBES confidential data: worldbank.org/en/about/unit/unit-dec
2. Match on: country + city + sector (ISIC) + firm size + year
3. Validate match rate (target >60%)
4. Extract: intangible_assets, IT_spending, patent_count

**Timeline**: 3-6 months minimum. Not for current P3 submission.

### Option C: FAT Survey Integration (Feasibility: LOW)

The **Firm-level Adoption of Technology (FAT) Survey** (Cirera, Comin & Cruz, 2022) measures:
- Technology sophistication at business-function level (1-5 ladder)
- MAX score (frontier function) and MOST score (modal function)
- Covers: management, production, marketing, quality, logistics

**Vietnam 2019 FAT pilot exists** — could supplement P4.
**Singapore and China: no FAT survey** — cannot use for P3/P5.

### Option D: Composite Index with Theory Grading (Feasibility: HIGH)

Without new data, strengthen the theoretical defense of existing DAI:

1. **Explicitly grade** each indicator on Verhoef hierarchy in manuscript
2. **Report** that DAI captures Tier 1-2 and honestly cannot capture Tier 3-4
3. **Frame** as: "digital adoption is a necessary but not sufficient condition for digital capability; our DAI measures the foundational layer upon which Tier 3-4 capabilities are built"
4. **Cite** Cirera et al. (2022) to show that Tier 1-2 is the measurable frontier for cross-country WBES research

---

## 4. Implementation Plan

### Phase 1: For P3 MIR Submission (NOW)
- ✅ Already done: DAI labeled "digital adoption" not "digital capability"
- ✅ Already done: §3.2.3 explains formative construction
- ✅ Already done: §6 Limitations acknowledges Tier 1-2 constraint
- **Add to §6**: "Future research should link WBES microdata with proprietary databases such as Bureau van Dijk's Orbis to capture Tier 3 integration indicators (ERP adoption, digital supply chain management) and Tier 4 dynamic capability indicators (AI deployment, platform orchestration), following the progression hierarchy of Verhoef et al. (2021)."

### Phase 2: For R&R or Next Paper (3-6 months)
- Build DAI_extended with B-READY items (c36, d35, n2l) — Option A
- Compute polychoric PCA on mixed binary/continuous DAI items
- Report robustness: DAI_rich vs DAI_extended vs individual items
- Add Heckman selection model (Path 1 synergy)

### Phase 3: For Dissertation Chapter 6 (6-12 months)
- Apply for WBES confidential microdata access — Option B
- Explore Orbis linkage feasibility for Singapore firms
- If FAT Vietnam 2019 available, integrate into P4 analysis — Option C
- Document all linkage attempts (successful or not) transparently

### Phase 4: Post-Dissertation Research Agenda
- Design multi-tier DAI measurement framework
- Custom survey instrument for Tier 3-4 in ASEAN firms
- Propose to World Bank: add Tier 3 items to next WBES round

---

## 5. Text Blocks Ready for Manuscript

### §6 Limitations — Tier paragraph (paste-ready)

> A second limitation concerns the depth of our digital adoption measure. The DAI composite captures Tier 1 (digital presence) and Tier 2 (digital transactions) of the Verhoef et al. (2021) digitalization hierarchy, but cannot reach Tier 3 (process integration through ERP, CRM, and digital supply chain systems) or Tier 4 (digital dynamic capabilities such as AI deployment and platform orchestration). This constraint is inherent to the WBES instrument, which was designed to capture broad adoption patterns across developing and emerging economies rather than the fine-grained digital sophistication that distinguishes firms within a digital-frontier economy. Future research should link WBES microdata with proprietary firm-level databases (e.g., Bureau van Dijk's Orbis) or purpose-built surveys modelled on the World Bank's Firm-level Adoption of Technology (FAT) framework (Cirera, Comin & Cruz, 2022) to construct multi-tier digital capability indices that can discriminate between adoption and capability proper.

### §2.2 — Tier grading paragraph (paste-ready)

> We grade each DAI indicator on the Verhoef et al. (2021) hierarchy: website presence (c22b) captures Tier 1 digitization, while electronic-payment intensity (k33, k38) captures Tier 2 digitalization. Our composite therefore measures the foundational digital layer — the necessary infrastructure upon which higher-order digital capabilities (Tier 3 process integration, Tier 4 dynamic capability) are constructed. We deliberately label this construct "digital adoption" rather than "digital capability" to respect the content-domain boundary of the available indicators.

---

## 6. References to Add

- Cirera, X., Comin, D., & Cruz, M. (2022). *Bridging the Technological Divide*. World Bank. DOI: 10.1596/978-1-4648-1826-4
- Verhoef, P. C., et al. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research*, 122, 889-901. DOI: 10.1016/j.jbusres.2019.09.022
- Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy. *MIS Quarterly*, 37(2), 471-482. DOI: 10.25300/MISQ/2013/37:2.3
