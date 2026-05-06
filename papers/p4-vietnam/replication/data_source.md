# P4 Vietnam — Data source mapping

## WBES Vietnam 3 waves

| Wave | Year | N | Methodology |
|---|---|---|---|
| Wave 1 | 2009 | 989 | PICS3 schema |
| Wave 2 | 2015 | 956 | Standardized schema |
| Wave 3 | 2023 | 1,013 | BREADY/BEE schema (B-READY) |
| **Pooled** | **2009 + 2015 + 2023** | **2,958** | Wave-specific + pooled estimation |

## Variables (WBES question codes)

### Dependent variable
- **lnLP** = ln(d2 / l1)
  - `d2` = total annual sales (Vietnamese dong)
  - `l1` = number of permanent full-time employees

### Focal independent variable
- **FSTS** = `d3c / 100` (proportion of annual sales from direct exports)
- **FSTS_c** = mean-centred within wave
- **FSTS_c²** = squared

### TCI — Foreign-technology / standards capability
- **TCI_thin (primary)**: mean of {b8, e6 recoded}
  - `b8` = internationally recognised quality certification
  - `e6` = foreign-licensed technology
- **TCI_full (robustness)**: TCI_thin + h1 + h8 (2015, 2023 only)
  - `h1` = product innovation
  - `h8` = R&D activity

### DAI — Website-based digital presence (Tier 1 baseline)
- **DAI (primary)**: c22b own-website indicator (binary)
- **DAI_rich (2023 robustness)**: c22b + k33 + k38
  - `k33` = customer-side electronic-payment intensity
  - `k38` = supplier-side electronic-payment intensity
  - Available only in B-READY 2023 wave

### Controls
- `lnEmp` = ln(l1) firm size
- `FirmAge` = year - b5 (year established)
- `ForeignOwned` = 1 if b2b > 0 (any foreign equity)
- Sector FE: a4b 1-digit ISIC (2009, 2015) hoặc a4a 1-digit (2023)

## Listwise deletion rules

1. Treat WBES non-response codes (`-9`) as missing
2. Listwise delete on focal set: `{lnLP, lnEmp, FirmAge, ForeignOwned, FSTS, TCI_thin, DAI_thin, sector1}`
3. Result: N = 989 (2009), 956 (2015), 1,013 (2023) → pooled 2,958

## Data location trong repo

Raw WBES data: see [`../../../wbes/`](../../../wbes/) pipeline.

Specific Vietnam files:
- `wbes/raw/VNM/2009/Vietnam-2009-WBES.dta` (PICS3)
- `wbes/raw/VNM/2015/Vietnam-2015-WBES.dta` (Standardized)
- `wbes/raw/VNM/2023/Vietnam-2023-WBES-B-READY.dta` (B-READY)

Note: Raw WBES data is licensed by World Bank and not redistributed.

## Citation chain

- **Paper P4** — this folder
- **WBES microdata**:
  - World Bank (2010). *Vietnam Enterprise Survey 2009* [Data set]
  - World Bank (2016). *Vietnam Enterprise Survey 2015* [Data set]
  - World Bank (2024). *Vietnam Enterprise Survey 2023* [Data set]
- **Pipeline harmonisation** — `wbes/02_harmonize.py` xuyên 3 thế hệ schema
- **Thesis cross-reference** — [`thesis/16_cd1_part3_cases_conclusion_vi.md`](../../../thesis/16_cd1_part3_cases_conclusion_vi.md) §5.3 Việt Nam tiểu cảnh
