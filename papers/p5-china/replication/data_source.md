# P5 China — Data source mapping

## WBES China 2 waves

| Wave | Year | N | Methodology |
|---|---|---|---|
| Wave 1 | 2012 | 2,619 | Standardized schema (post-PICS3) |
| Wave 2 | 2024 | 1,940 | Standardized 2018+ / BREADY enhancements |
| **Pooled** | **2012 + 2024** | **4,559** | Wave-specific + pooled estimation |
| Panel subset | Common firms 2012 + 2024 | 217 | Optional 2-period panel for future work |

## Variables (WBES question codes)

### Dependent variable
- **lnLP** = ln(d2 / l1)
  - `d2` = total annual sales (Chinese yuan, then deflated to 2012 RMB or 2024 RMB)
  - `l1` = number of permanent full-time employees

### Focal independent variable
- **FSTS** = `d3c / 100` (proportion of annual sales from direct exports)
- **FSTS²** = squared
- For pooled: wave_2024 = 1 if wave=2024 else 0

### TCI_full (formative, 4 binary indicators)
- `e6` = foreign-licensed technology
- `b8` = quality certification (ISO etc.)
- `h1` = product innovation in past 3 years
- `h8` = R&D activity past 3 years
- TCI_full_z = z-standardized mean

### DAI_core (deliberately Tier-1 only, for cross-wave comparability)
- `c22b` = own-website presence (binary)
- DAI_core_z = z-standardized
- Note: 2024 BREADY has richer items (e-payment, ERP) but 2012 lacks them; using only c22b ensures cross-wave comparability

### Controls
- `lnEmp` = ln(l1) firm size
- `FirmAge` = year - b5
- `ForeignOwned` = 1 if b2b > 0
- Sector FE: a4b 1-digit ISIC
- Region FE: a3 (provinces)

### Working-capital proxies (supplementary, §4.5)
- `k4` = bank loan as percent of working capital
- `k7` = days inventory
- `k8/k82` = days receivables (2012 only)
- `k1c, k2c` = purchases / sales on credit (2012 only)
- `k14` = access-to-finance obstacle (binary)
- `k30` = applied for credit

## Listwise deletion

1. Remove WBES non-response codes (`-9`, `-8`, etc.) before composite construction
2. Listwise delete on focal set: `{lnLP, FSTS, TCI_full_z, DAI_core_z, lnEmp, FirmAge, ForeignOwned, sector1, region1}`
3. Result: N = 2,619 (2012) + 1,940 (2024) → pooled 4,559

## Data location trong repo

Raw WBES data: see [`../../../wbes/`](../../../wbes/) pipeline.

Specific China files:
- `wbes/raw/CHN/2012/China-2012-WBES.dta` (Standardized)
- `wbes/raw/CHN/2024/China-2024-WBES-BREADY.dta` (Standardized 2018+)

Note: Raw WBES data is licensed by World Bank.

## Citation chain

- **Paper P5** — this folder
- **WBES microdata**:
  - World Bank (2013). *China Enterprise Survey 2012* [Data file]
  - World Bank (2025). *China Enterprise Survey 2024* [Data file]
- **Pipeline harmonisation** — `wbes/02_harmonize.py` (single-country, 2 waves)
- **Thesis cross-reference**:
  - [`thesis/05_p5_china_design_vi.md`](../../../thesis/05_p5_china_design_vi.md) — full P5 design
  - [`thesis/01_chapter_outline_vi.md`](../../../thesis/01_chapter_outline_vi.md) Ch.4.5 temporal heterogeneity
  - [`thesis/16_cd1_part3_cases_conclusion_vi.md`](../../../thesis/16_cd1_part3_cases_conclusion_vi.md) §5.4 Trung Quốc tiểu cảnh

## P2 published predecessor

P5 builds on the China cubic specification published in P2 (Đỗ & Phan, 2026 — JFAR), which used WBES China 2012 alone with N = 4,290 SMEs and identified turning point ~47.8% FSTS. P5 extends this to include 2024 wave + tests for cross-wave shift (the central novel contribution).
