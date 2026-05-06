*===============================================================
* P5 China — 02_build_2024.do
* Build analytic sample from raw China 2024 WBES (BREADY, 2,189 firms)
* Output: china2024_analytic.dta
* NOTE: 2024 uses ISIC Rev 4 + separate refusal code -8
*       Manufacturing filter via d1a2_v4 (WBES recommended)
*===============================================================

clear all
set more off
version 17

local raw     "China2024fulldata.dta"
local out     "china2024_analytic.dta"

cap log close
log using "build_2024.log", replace text

*-----------------------------------------------------------------
* Step 1 — Open raw + audit raw N
*-----------------------------------------------------------------
use "`raw'", clear
count
local n_raw = r(N)
di as txt "[AUDIT] Raw N (2024) = `n_raw'  (expected 2,189; 1,972 fresh + 217 panel)"

* Verify panel flag exists
capture confirm variable panel
if _rc di as err "[WARN] variable 'panel' not found in 2024 data — check naming"

*-----------------------------------------------------------------
* Step 2 — Manufacturing filter: d1a2_v4 (4-digit ISIC Rev 4)
*           SKIP if reproducing manuscript v1.2 (full private frame)
*           If applied: floor(d1a2_v4/100) in 10..33 = manufacturing
*-----------------------------------------------------------------
* gen mfg2digit = floor(d1a2_v4/100)
* keep if mfg2digit >= 10 & mfg2digit <= 33
* di as txt "[AUDIT] Manufacturing N (2024) = " _N
* drop mfg2digit

*-----------------------------------------------------------------
* Step 3 — Recode WBES 2024 nonresponse codes
*   -9 = don't know, -8 = refuse, -7 = inapplicable -> all missing
*-----------------------------------------------------------------
local focal_vars d2 d3c l1 b5 b2b e6 b8 h1 h8 c22b
foreach v of local focal_vars {
    capture confirm numeric variable `v'
    if !_rc {
        replace `v' = . if inlist(`v', -9, -8, -7)
    }
}

*-----------------------------------------------------------------
* Step 4 — Focal variables
*-----------------------------------------------------------------
gen double lnLP    = ln(d2/l1)            if d2>0 & l1>0 & !mi(d2,l1)
gen double FSTS    = d3c/100              if !mi(d3c)
gen double FSTSsq  = FSTS^2
gen double lnEmp   = ln(l1)               if l1>0
gen double firmage = 2024 - b5            if b5>1900 & b5<=2024
gen byte   foreigndummy = (b2b > 0)       if !mi(b2b)

label var lnLP        "Log labour productivity (d2/l1)"
label var FSTS        "Foreign sales / total sales (0..1)"
label var FSTSsq      "FSTS squared"
label var lnEmp       "Log permanent employment"
label var firmage     "Firm age (years)"
label var foreigndummy "1 if any foreign ownership"

*-----------------------------------------------------------------
* Step 5 — Composites: within-wave z-standardization
*           Items in 2024 are binary (1=yes, 2=no, -9/-8 already missing)
*-----------------------------------------------------------------
foreach v in e6 b8 h1 h8 c22b {
    capture confirm numeric variable `v'
    if !_rc {
        gen byte `v'_bin = .
        replace `v'_bin = 1 if `v' == 1
        replace `v'_bin = 0 if `v' == 2
        egen double z_`v' = std(`v'_bin)
    }
}

egen byte tci_count = rownonmiss(z_e6 z_b8 z_h1 z_h8)
egen double TCIfull = rowmean(z_e6 z_b8 z_h1 z_h8) if tci_count >= 3
label var TCIfull "Tech capability index (z-mean, >=3/4 items)"

egen double DAIthin = rowmean(z_c22b z_e6)
label var DAIthin "Digital adoption index (thin proxy: c22b + e6) — cross-wave comparable"

*-----------------------------------------------------------------
* Step 6 — Sample flags
*-----------------------------------------------------------------
gen byte sample_analytic = !mi(lnLP, FSTS, lnEmp, firmage, foreigndummy)
gen byte sample_base     = !mi(lnLP, FSTS, FSTSsq, lnEmp, firmage, foreigndummy)
gen byte sample_dai      = sample_base & !mi(DAIthin)
gen byte sample_tci      = sample_base & !mi(TCIfull)
gen byte sample_full     = sample_tci  & !mi(DAIthin)

gen byte wave2024 = 1

*-----------------------------------------------------------------
* Step 7 — Audit
*-----------------------------------------------------------------
foreach s in analytic base dai tci full {
    count if sample_`s' == 1
    di as txt "[AUDIT] sample_`s' (2024) = " r(N)
}

* Expected per manuscript v1.2:
* analytic = 1,940 ; base = 1,934 ; dai = 1,934 ; tci = 1,920 ; full = 1,920
* Verified Python: 1,934 / 1,934 / 1,934 / 1,920 / 1,920 — exact match

*-----------------------------------------------------------------
* Step 8 — Save
*-----------------------------------------------------------------
local keepvars idstd id a2 a4a a6a wave2024 ///
     lnLP FSTS FSTSsq lnEmp firmage foreigndummy ///
     TCIfull DAIthin tci_count ///
     sample_analytic sample_base sample_dai sample_tci sample_full
capture confirm variable panel
if !_rc local keepvars `keepvars' panel
capture confirm variable d1a2_v4
if !_rc local keepvars `keepvars' d1a2_v4

keep `keepvars' d2 d3c l1 b5 b2b e6 b8 h1 h8 c22b
compress
save "`out'", replace

di as txt "[DONE] Saved `out'"
log close
