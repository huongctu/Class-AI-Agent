# WBES Asia Dataset

Pooled World Bank Enterprise Surveys (WBES) microdata for **41 Asian economies**, 5 UN M.49 regions.

## Contents

```
data/asia/
├── README.md                 # this file
├── manifest.csv              # 1 row per file: country, year, n_obs, n_vars, size, md5
├── schema.json               # per-file variable list (first 50 vars + core hits)
├── raw/                      # 110 deduplicated country-year .dta files
│   ├── Afghanistan/
│   ├── Armenia/
│   ├── ...
│   └── Yemen/
├── pooled/
│   ├── asia_pooled_core.dta  # 122,858 firm-obs × 41 cols, core WBES variables only
│   └── asia_pooled_core.csv  # same data, CSV format
└── scripts/
    ├── build_asia_dta.py     # dedupe + canonicalize raw files
    └── pool_asia_dta.py      # enrich manifest + build pooled file
```

## Coverage

- **110 country-year files** (deduplicated from 298 raw uploads — many duplicates from re-uploads)
- **122,858 firm-observations** total
- **41 economies** across 5 regions:

| Region          | Files | Economies                                                                                              |
| --------------- | ----- | ------------------------------------------------------------------------------------------------------ |
| East Asia       | 12    | China, HongKong, Korea, Mongolia, Taiwan                                                               |
| Southeast Asia  | 33    | Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, TimorLeste, Vietnam |
| South Asia      | 24    | Afghanistan, Bangladesh, Bhutan, India, Maldives, Nepal, Pakistan, SriLanka                            |
| Central Asia    | 16    | Kazakhstan, KyrgyzRepublic, Tajikistan, Turkmenistan, Uzbekistan                                       |
| West Asia       | 25    | Armenia, Bahrain, Cyprus, Georgia, Iraq, Israel, Jordan, Kuwait, Lebanon, Oman, Qatar, SaudiArabia, Yemen |

Pacific islands (Fiji, Samoa, Kiribati, Tonga, Solomon Islands, PNG, Vanuatu) are excluded — Oceania, not Asia per UN M.49.

## Pooled file: variable set

`asia_pooled_core.dta` keeps only WBES variables that appear consistently across waves (Enterprise Surveys Indicator Descriptions, World Bank). Per-row coverage shown below.

| Var      | Meaning                              | Coverage |
| -------- | ------------------------------------ | -------- |
| src_country, src_year, src_region, src_file | metadata (added) | 100%     |
| idstd    | Standard firm ID                     | 95.6%    |
| a1       | Country name                         | 99.4%    |
| a2       | City/region                          | 86.9%    |
| a6a      | ISIC sector                          | 77.1%    |
| b1       | Legal status                         | 99.0%    |
| b2a      | Sector                               | 97.3%    |
| b3       | Year of operation                    | 64.4%    |
| b4       | Female ownership share               | 98.8%    |
| b6a      | Foreign ownership %                  | 52.3%    |
| b7       | Top manager experience               | 83.7%    |
| d2       | Total annual sales                   | 83.7%    |
| n3       | Sales last fiscal year               | 95.9%    |
| l1       | Full-time permanent workers          | 83.7%    |
| l2       | Full-time temporary workers          | 99.0%    |
| d3a/b/c  | Direct/indirect exports, domestic %  | 83.7%    |
| h1       | New product/service introduced       | 66.8%    |
| h5       | R&D spending                         | 66.0%    |
| k3a/k3bc | Working capital financing            | 80%      |
| wstrict, wmedian | Sample weights               | 90/94%   |

For variables NOT in the core list, load the raw country-year `.dta` directly.

## Caveats

1. **Variable harmonization is partial.** WBES question wording, value labels, and code definitions shift across waves (especially 2009→2013→2019 vs. 2022→2025 redesign). Pooled comparisons require additional cleaning per variable.
2. **Encoding.** 22 files required `latin1`/`cp1252` fallback (legacy waves); column labels may contain non-ASCII residue.
3. **Survey weights.** `wstrict` / `wmedian` are within-country weights — NOT comparable across countries without re-stratification.
4. **Year semantics.** `src_year` is the survey wave year (filename), not necessarily the firm's reporting year. The WBES `year` variable (present in 9.6% of rows) is the firm's reporting year.
5. **Panel files.** `Pakistan_panel_2007-2013-2022.dta`, `Mongolia_panel_2009-2013-2019.dta`, etc. stack multiple waves with a panel ID — treat separately from cross-section.

## Reproducibility

```bash
# 1. Place all raw .dta uploads in /tmp/*/ or /root/.claude/uploads/
# 2. Run inventory
python3 data/asia/scripts/build_asia_dta.py
# 3. Build pooled file
python3 data/asia/scripts/pool_asia_dta.py
```

Requires: `python3.9+`, `pyreadstat>=1.3`, `pandas>=2.0`.

## Source

World Bank Enterprise Surveys, https://www.enterprisesurveys.org. Microdata access subject to WBES terms (free academic use, attribution required).
