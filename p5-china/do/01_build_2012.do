*===============================================================
* P5 China — 01_build_2012.do
* Build analytic sample from raw China 2012 WBES (2,700 private firms)
* Output: china2012_analytic.dta with focal vars, composites, sample flags
*===============================================================

clear all
set more off
version 17

* --- Paths (adjust to RA local machine) --------------------------
local raw     "China2012fullESN2700data.dta"
local out     "china2012_analytic.dta"
local audit   "audit_2012.txt"

cap log close
log using "build_2012.log", replace text

*-----------------------------------------------------------------
* Step 1 — Open raw + audit raw N
*-----------------------------------------------------------------
use "`raw'", clear
count
local n_raw = r(N)
di as txt "[AUDIT] Raw N (2012) = `n_raw'  (expected 2,700)"

*-----------------------------------------------------------------
* Step 2 — Manufacturing filter: a4a 15..38 (ISIC Rev 3.1, incl Other Mfg)
*           SKIP this step if reproducing manuscript v1.2 (uses full private frame)
*-----------------------------------------------------------------
* keep if a4a >= 15 & a4a <= 38
* count
* local n_mfg = r(N)
* di as txt "[AUDIT] Manufacturing N (2012) = `n_mfg'"

*-----------------------------------------------------------------
* Step 3 — Recode WBES nonresponse codes -9 / -7 -> missing
*           on every numeric variable that will enter focal set
*-----------------------------------------------------------------
local focal_vars d2 d3c l1 b5 b2b e6 b8 h1 h8 c22b CNo1 CNo3
foreach v of local focal_vars {
    capture confirm numeric variable `v'
    if !_rc {
        replace `v' = . if inlist(`v', -9, -7)
    }
    else {
        di as err "[WARN] variable `v' not numeric or not found"
    }
}

*-----------------------------------------------------------------
* Step 4 — Focal variables
*-----------------------------------------------------------------
gen double lnLP    = ln(d2/l1)            if d2>0 & l1>0 & !mi(d2,l1)
gen double FSTS    = d3c/100              if !mi(d3c)
gen double FSTSsq  = FSTS^2
gen double lnEmp   = ln(l1)               if l1>0
gen double firmage = 2012 - b5            if b5>1900 & b5<=2012
gen byte   foreigndummy = (b2b > 0)       if !mi(b2b)

label var lnLP        "Log labour productivity (d2/l1)"
label var FSTS        "Foreign sales / total sales (0..1)"
label var FSTSsq      "FSTS squared"
label var lnEmp       "Log permanent employment"
label var firmage     "Firm age (years, 2012 - founded)"
label var foreigndummy "1 if any foreign ownership"

*-----------------------------------------------------------------
* Step 5 — Composites: TCIfull (>=3/4 nonmissing), DAIthin
*           Within-wave z-standardization (do BEFORE pooling)
*           NOTE: items in 2012 are binary (1=yes, 2=no, -9=missing)
*           Recode to 0/1 before standardization for cleaner interpretation
*-----------------------------------------------------------------
* TCI items: e6, b8, CNo1 (h1 in 2024), CNo3 (h8 in 2024)
foreach v in e6 b8 CNo1 CNo3 c22b {
    capture confirm numeric variable `v'
    if !_rc {
        gen byte `v'_bin = .
        replace `v'_bin = 1 if `v' == 1
        replace `v'_bin = 0 if `v' == 2
        egen double z_`v' = std(`v'_bin)
    }
}

egen byte tci_count = rownonmiss(z_e6 z_b8 z_CNo1 z_CNo3)
egen double TCIfull = rowmean(z_e6 z_b8 z_CNo1 z_CNo3) if tci_count >= 3
label var TCIfull "Tech capability index (z-mean, >=3/4 items)"

egen double DAIthin = rowmean(z_c22b z_e6)
label var DAIthin "Digital adoption index (thin proxy: c22b + e6)"

*-----------------------------------------------------------------
* Step 6 — Sample flags (model-specific estimation samples)
*-----------------------------------------------------------------
gen byte sample_analytic = !mi(lnLP, FSTS, lnEmp, firmage, foreigndummy)
gen byte sample_base     = !mi(lnLP, FSTS, FSTSsq, lnEmp, firmage, foreigndummy)
gen byte sample_dai      = sample_base & !mi(DAIthin)
gen byte sample_tci      = sample_base & !mi(TCIfull)
gen byte sample_full     = sample_tci  & !mi(DAIthin)

gen byte wave2024 = 0

*-----------------------------------------------------------------
* Step 7 — Audit table
*-----------------------------------------------------------------
foreach s in analytic base dai tci full {
    count if sample_`s' == 1
    local n_`s' = r(N)
    di as txt "[AUDIT] sample_`s' (2012) = `n_`s''"
}

* Expected per manuscript v1.2 (full private frame):
* analytic = 2,619 ; base = 2,612 ; dai = 2,612 ; tci = 1,613 ; full = 1,613
* Verified Python: 2,610 / 2,610 / 2,610 / 1,639 / 1,639 (within 2 firms; TCI gap larger)

*-----------------------------------------------------------------
* Step 8 — Save
*-----------------------------------------------------------------
keep idstd id a2 a4a a6a wave2024 ///
     lnLP FSTS FSTSsq lnEmp firmage foreigndummy ///
     TCIfull DAIthin tci_count ///
     sample_analytic sample_base sample_dai sample_tci sample_full ///
     d2 d3c l1 b5 b2b e6 b8 c22b CNo1 CNo3
compress
save "`out'", replace

di as txt "[DONE] Saved `out'"
log close
