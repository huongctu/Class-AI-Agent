# Protocol harmonization dữ liệu P7 — WBES Asian + Middle East + Pacific

File này là protocol để chuẩn hóa tất cả country-wave WBES files thành một pooled dataset cho P7. Đi kèm với `scripts/P7_harmonize_pool.do` (Stata) để chạy tự động trên local.

## 1. Khung lý thuyết

P7 kiểm định mối quan hệ **internationalization → firm performance** với 3 nhóm moderator:

1. **Digital capability**: technological capability (TCI) và digital adoption (DAI) — hai construct non-overlapping
2. **Top manager**: experience (năm) và gender (b1.1/b7 tùy wave)
3. **Institutional context**: ICRV regime (theo WGI Rule of Law) + business obstacles index

Bối cảnh: Asian + Middle East + Pacific (~36 country-units). Variable WBES đồng nhất toàn cầu theo *Notes on Standardized Dataset* (World Bank).

## 2. Inventory 36 country-units

| Cluster | Quyốc gia (số waves) |
|---|---|
| **East Asia (4)** | China (2), Hong Kong (1), Korea (1), Taiwan (1) |
| **Southeast Asia (10)** | Brunei (1), Cambodia (3), Indonesia (3), Lao PDR (4), Malaysia (3), Myanmar (?), Philippines (3), Singapore (1), Thailand (2), Timor-Leste (3), Vietnam (3) |
| **South Asia (7)** | Afghanistan (2), Bangladesh (2), Bhutan (3), India (2), Nepal (2-3), Pakistan (2), Sri Lanka (2) |
| **Central Asia (6)** | Kazakhstan (4), Kyrgyz (4), Mongolia (2), Tajikistan (3), Turkmenistan (1), Uzbekistan (3) |
| **Western Asia (7)** | Armenia (4), Bahrain (1), Cyprus (2), Georgia (3), Iraq (2), Israel (2), Jordan (3) |
| **Pacific (1)** | Vanuatu (2) |

Tổng: ~87 standard WBES cross-section files + 10 panels (sau dedup).

## 3. Schema crosswalk WBES theo thời gian

WBES đã thay đổi schema 3 lần. Protocol harmonization xử lý cả 3:

| Concept | Schema 2007–2010 | Schema 2013–2017 | Schema 2018+ |
|---|---|---|---|
| Annual sales (current) | `d2` | `d2` | `d2` |
| Annual sales 3y ago | `n3` hoặc `d2a` | `n3` | `n3` |
| Permanent FT employees current | `l1` | `l1` | `l1` |
| Permanent FT employees 3y ago | `l2` | `l2` | `l2` |
| Direct exports % | `d3a` | `d3c` | `d3c` |
| Indirect exports % | `d3b` | `d3d` | `d3d` |
| Email use | `c30b` | `c22a` | `c22a` |
| Website | (không có phiên bản sớm) | `c22b` | `c22b` |
| Quality certification | `b8` | `e6` | `e6` |
| Foreign tech license | (option) | `h1` | `h1` |
| Foreign ownership % | `b2b` | `b5` | `b5` |
| Establishment year | `b6` | `b1` hoặc `b6a` | `b6a` |
| Industry sector | `a4a` hoặc `a4b` | `a4a` | `a4a` |
| Top manager experience | `b7` | `b7` | `b7` |
| Top manager gender | `b7a` | `b7a` | `b7a` |

Lưu ý: standardized dataset của World Bank đã rename hai chiều về schema 2013–2017 để đồng nhất. Protocol này theo schema standardized.

## 4. Biến dẫn xuất (derived variables)

Từ raw variables, tạo các biến phân tích sau:

### 4.1 Performance variables

```
ln_lp     = ln(d2 / l1)                       /* labor productivity, primary DV */
ln_sales  = ln(d2)                             /* sales level */
sales_g   = (d2 - n3) / n3                     /* sales growth (raw) */
ln_sales_g = ln(d2/n3) / 3                     /* annualized log growth */
emp_g     = (l1 - l2) / l2                     /* employment growth */
```

### 4.2 Internationalization variables

```
fsts       = d3c / 100                         /* foreign sales / total sales */
fsts_sq    = fsts^2                            /* binh phuong cho phi tuyen */
is_exporter = (fsts > 0)                       /* dummy */
exp_indirect = (d3d > 0) if !missing(d3d)
```

### 4.3 Digital constructs (non-overlapping)

```
* Technological Capability Index (TCI) - chieu sau
tci_n  = rownonmiss(h1 e6)
tci    = rowmean(h1 e6)
replace tci = . if tci_n < 1

* Digital Adoption Index (DAI) - be mat
dai_n  = rownonmiss(c22a c22b)
dai    = rowmean(c22a c22b)
replace dai = . if dai_n < 1
```

Quy tắc non-overlapping: `e6` (quality cert) và `h1` (foreign tech) thuộc TCI; `c22a` (email) và `c22b` (website) thuộc DAI — không share component.

### 4.4 Top manager variables

```
mgr_exp    = b7                                /* years of experience */
mgr_female = (b7a == 1)                        /* female top manager dummy */
ln_mgr_exp = ln(b7 + 1)                        /* log to handle zeros */
```

### 4.5 Institutional / control variables

```
firm_age   = wave - b6a                        /* firm age */
ln_emp     = ln(l1)                            /* size control */
foreign    = (b5 >= 10)                        /* foreign-owned dummy */
sector_mfg = inrange(a4a, 15, 39)              /* manufacturing dummy ISIC */

* Business obstacle index (b1nh quan obstacles 1-5 scale)
egen obstacle_idx = rowmean(b30a b30b b30c c30a c30b /* etc. */)
```

### 4.6 ICRV regime classification

Cần một lần cho mỗi country-year. Theo WGI Rule of Law:
- `icrv_regime = 1` (Regime I) nếu WGI RoL > +0.80
- `icrv_regime = 2` (Regime II) nếu WGI RoL trong [-0.50, +0.80]
- `icrv_regime = 3` (Regime III) nếu WGI RoL < -0.50
- `icrv_regime = 4` (SIDS) nếu Vanuatu, Maldives, Timor-Leste
- `icrv_regime = 5` (Frontier) nếu Afghanistan, Myanmar (nếu có)

Mã hóa manual từ bảng country-year x WGI RoL.

## 5. Stata script: `scripts/P7_harmonize_pool.do`

Xem file rên riêng trong nhánh này. Cấu trúc:

```stata
* P7_harmonize_pool.do
* Pool 36 country-wave WBES files into one harmonized dataset

clear all
set more off
set linesize 200

global RAW   "data/raw_wbes"
global OUT   "data/p7_pooled"
cap mkdir "$OUT"

* ----------------------------------------
* 1. Manifest of files: country, wave, filename
* ----------------------------------------
tempfile manifest
file open mf using "`manifest'", write replace
file write mf "country|wave|file" _n
file write mf "Afghanistan|2014|Afghanistan2014fulldata.dta" _n
file write mf "Afghanistan|2025|Afghanistan2025fulldata.dta" _n
file write mf "Bangladesh|2013|Bangladesh2013fulldata.dta" _n
file write mf "Bangladesh|2022|Bangladesh2022fulldata.dta" _n
file write mf "Bhutan|2009|Bhutan2009fulldata.dta" _n
file write mf "Bhutan|2015|Bhutan2015fulldata.dta" _n
file write mf "Bhutan|2024|Bhutan2024fulldata.dta" _n
* ... (full list cua 87 files)
file close mf

* ----------------------------------------
* 2. Loop over each file and harmonize
* ----------------------------------------
tempfile master
save `master', replace emptyok

import delimited "`manifest'", delimiter("|") clear
local n_files = _N

forvalues i = 1/`n_files' {
    local country = country[`i']
    local wave    = wave[`i']
    local file    = file[`i']
    
    use "$RAW/`file'", clear
    
    * Standardize variable names (handles 3 schema versions)
    capture rename d3a d3c
    capture rename b8 e6
    capture rename b2b b5
    capture rename b6 b6a
    capture rename c30b c22a
    
    * Compute derived variables
    capture drop ln_lp
    gen double sales_now = d2
    gen double emp_now = l1
    gen double ln_lp = ln(sales_now / emp_now) if sales_now > 0 & emp_now > 0
    
    capture gen double fsts = d3c / 100
    capture gen double fsts_sq = fsts^2
    
    capture gen byte uses_email = (c22a == 1)
    capture gen byte has_website = (c22b == 1)
    capture gen byte quality_cert = (e6 == 1)
    capture gen byte foreign_tech = (h1 == 1)
    
    egen dai_n = rownonmiss(uses_email has_website)
    egen dai = rowmean(uses_email has_website)
    replace dai = . if dai_n < 1
    
    egen tci_n = rownonmiss(quality_cert foreign_tech)
    egen tci = rowmean(quality_cert foreign_tech)
    replace tci = . if tci_n < 1
    
    capture gen double mgr_exp = b7
    capture gen byte mgr_female = (b7a == 1)
    
    capture gen double firm_age = `wave' - b6a
    capture gen double ln_emp = ln(l1)
    capture gen byte foreign = (b5 >= 10)
    
    * Add country and wave
    gen str20 country = "`country'"
    gen int wave = `wave'
    
    * Keep harmonized variables only
    keep country wave ln_lp fsts fsts_sq dai tci mgr_exp mgr_female ///
         firm_age ln_emp foreign quality_cert has_website uses_email ///
         foreign_tech a4a sales_now emp_now
    
    capture rename a4a sector
    
    * Append to master
    append using `master'
    save `master', replace
    
    di "Done: `country' `wave' — `file'"
}

* ----------------------------------------
* 3. Final cleaning and ICRV regime mapping
* ----------------------------------------
use `master', clear

* ICRV regime by country
gen byte icrv_regime = .
replace icrv_regime = 1 if inlist(country, "Singapore", "Hong Kong", "Taiwan", "Korea", "Brunei Darussalam", "Israel", "Bahrain", "Cyprus")
replace icrv_regime = 2 if inlist(country, "China", "Malaysia", "India", "Thailand", "Vietnam", "Indonesia", "Philippines", "Kazakhstan", "Georgia", "Armenia", "Mongolia")
replace icrv_regime = 3 if inlist(country, "Bangladesh", "Pakistan", "Nepal", "Sri Lanka", "Cambodia", "Lao PDR", "Kyrgyz Republic", "Tajikistan", "Uzbekistan", "Turkmenistan", "Bhutan", "Iraq", "Jordan")
replace icrv_regime = 4 if inlist(country, "Vanuatu", "Timor-Leste")
replace icrv_regime = 5 if inlist(country, "Afghanistan", "Myanmar")
label define ICRV 1 "I" 2 "II" 3 "III" 4 "SIDS" 5 "Frontier"
label values icrv_regime ICRV

* Save final pooled dataset
save "$OUT/wbes_p7_pool.dta", replace

* ----------------------------------------
* 4. Summary statistics by country-wave
* ----------------------------------------
preserve
    collapse (count) n=ln_lp ///
             (mean) m_ln_lp=ln_lp m_fsts=fsts m_dai=dai m_tci=tci ///
                    m_mgr_exp=mgr_exp m_mgr_female=mgr_female ///
             (sd) sd_ln_lp=ln_lp sd_fsts=fsts ///
             (min) min_ln_lp=ln_lp ///
             (max) max_ln_lp=ln_lp, by(country wave)
    export delimited "$OUT/wbes_p7_summary_country_wave.csv", replace
restore

preserve
    collapse (count) n=ln_lp ///
             (mean) m_ln_lp=ln_lp m_fsts=fsts m_dai=dai m_tci=tci, by(icrv_regime)
    export delimited "$OUT/wbes_p7_summary_icrv.csv", replace
restore

di "DONE: pooled dataset saved to $OUT/wbes_p7_pool.dta"
di "DONE: summaries saved to $OUT/wbes_p7_summary_*.csv"
```

## 6. Quality checks (NCS chạy sau khi pool)

1. **Sample size theo country-wave**: mỗi country-wave nên có ≥ 100 firms; nếu < 50 firms loyại ra robustness.
2. **Missingness**: kiyểm tra tỉ lệ missing cyủa các key variables (`ln_lp`, `fsts`, `dai`, `tci`, `mgr_exp`).
3. **Outliers**: Winsorize `ln_lp` tại 1% và 99% percentiles theo country-wave.
4. **ICRV regime distribution**: mỗi regime nên có ≥ 3 countries để subgroup analysis.
5. **WGI Rule of Law verification**: confirm ICRV mapping bằng bảng country-year data từ World Bank Governance Indicators.

## 7. Output spec

Sau khi chạy script, NCS sẽ có:

| File | Vai trò |
|---|---|
| `data/p7_pooled/wbes_p7_pool.dta` | Pooled dataset sẵn sàng phân tích |
| `data/p7_pooled/wbes_p7_summary_country_wave.csv` | Summary stat theo country-wave |
| `data/p7_pooled/wbes_p7_summary_icrv.csv` | Summary stat theo ICRV regime |
| Log file Stata | Quy tắc xử lý mỗi file (cho transparency) |

## 8. Bước tiếp theo

Sau khi NCS chạy script và có `wbes_p7_pool.dta`:

1. **Upload 2 file CSV summary** lên GitHub — em phân tích initial và đề xuất fixes
2. **Upload `wbes_p7_pool.dta`** hoặc export sang CSV — em bắt đầu chạy các mô hình M0–M7 của P7 design
3. **Iterate**: xử lý outliers, reconcile missingness, refine ICRV regime

## 9. Tham khảo

- World Bank. (n.d.). *Notes on Standardized Dataset*. World Bank Enterprise Surveys.
- World Bank. (2019). *Understanding the Questionnaire*. WBES Documentation.
- World Bank. (2026). *Indicator Descriptions*. WBES Documentation.
- Kaufmann, D., Kraay, A., & Mastruzzi, M. (2010). The worldwide governance indicators: Methodology and analytical issues. *Hague Journal on the Rule of Law, 3*(2), 220–246.
- Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets*. Harvard Business Press.
- Do, T. H., & Tu, P. A. (2025). Internationalization and firm performance of firms in India: The role of top management. IntechOpen.
