# P3 Singapore — Data source mapping

## WBES Singapore 2023 (B-READY)

| Item | Value |
|---|---|
| **Country** | Singapore (SGP) |
| **Wave** | 2023 (only wave with B-READY methodology) |
| **Methodology** | B-READY (Business Ready) — expanded digital-adoption module including electronic-payment penetration |
| **N (full)** | 623 firms |
| **N (DAI sample)** | 617 firms (6 firms missing DAI items) |
| **Sectors** | Manufacturing 31%, retail+services 50%, other 19% |
| **Currency** | 2023 Singapore dollars (nominal) |

## Variables (WBES question codes)

### Dependent variable

- **lnLP** = ln(d2 / l1)
  - `d2` = total annual sales (Singapore dollars)
  - `l1` = number of permanent full-time employees
  - Winsorised at 1st and 99th percentiles within country-year

### Focal independent variable

- **FSTS** = `d3c / 100` (proportion of annual sales from direct exports, [0, 1])
- **FSTS_c** = mean-centred within wave
- **FSTS_c²** = squared mean-centred FSTS

### TCI — Technological Capability Index (formative composite)

Indicators (binary):
- `b8` = internationally recognised quality certification
- `e6` = foreign-licensed technology
- `h1` = introduced new or significantly improved product (TCI_full only)
- `h8` = R&D activity (TCI_full only)

Primary spec: `TCI_z` = z-standardised mean of {b8, e6}
Enriched spec: `TCI_full_z` = z-standardised mean of {b8, e6, h1, h8} (used in robustness)

### DAI — Digital Adoption Index (Tier 1–2)

Indicators (binary or proportion):
- `c22b` = own-website presence (Tier 1, primary)
- `k33` = customer-side electronic-payment intensity (Tier 2, B-READY 2023 only)
- `k38` = supplier-side electronic-payment intensity (Tier 2, B-READY 2023 only)

Primary spec: `DAI_z` = z-standardised mean of {c22b, k33, k38}
Thin spec: `DAI_thin_z` = c22b only (used in robustness R1)

### Controls

- `lnEmp` = ln(l1) firm size
- `FirmAge` = 2023 - b5 (year established)
- `ForeignOwned` = 1 if b2b > 10% foreign equity
- Sector FE: a4b 1-digit ISIC — manufacturing / retail / other services

## Listwise deletion rules

1. Remove obs with missing on focal variable set: `{lnLP, lnEmp, FirmAge, ForeignOwned, FSTS, TCI_z, DAI_z, sector1}`
2. Treat WBES non-response codes (`-9`) as missing before composite construction
3. Result: N = 623 (full) → N = 617 (with DAI items)

## Data location trong repo

Raw WBES data: see [`../../../wbes/`](../../../wbes/) pipeline.

Specific Singapore 2023 file: `wbes/raw/SGP/2023/Singapore-2023-WBES-B-READY.dta` (or equivalent)

Note: Raw WBES data is licensed by World Bank and not redistributed in this repo. Researchers must register at [enterprisesurveys.org](https://www.enterprisesurveys.org) and follow the World Bank Enterprise Surveys Data Access Protocol.

## Citation chain

- **Paper P3** — this folder
- **WBES microdata** — World Bank (2024). *World Bank Enterprise Surveys: Singapore 2023* [Data set]. https://www.enterprisesurveys.org
- **Pipeline harmonisation** — see `wbes/02_harmonize.py` (in thesis branch)
- **Thesis cross-reference** — [`thesis/01_chapter_outline_vi.md`](../../../thesis/01_chapter_outline_vi.md) Ch.4.2 ASEAN benchmark; [`thesis/16_cd1_part3_cases_conclusion_vi.md`](../../../thesis/16_cd1_part3_cases_conclusion_vi.md) §5.1 Singapore tiểu cảnh

## Reproducibility note

WBES Singapore 2023 raw `.dta` file không được commit vào repo (license restriction). Để reproduce khận cấp, NCS có file local tại `~/Documents/Research/wbes/raw/SGP/2023/`. Pipeline `wbes/02_harmonize.py` xử lý encoding fallback (Latin-1 → CP1252) và winsorize log productivity 1/99 trong country-year.
