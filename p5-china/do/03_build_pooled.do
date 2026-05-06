*===============================================================
* P5 China — 03_build_pooled.do
* Append 2012 + 2024 analytic files into pooled panel
* Output: china_pooled.dta
*
* IMPORTANT: composites (TCIfull, DAIthin) are z-standardized
*            WITHIN each wave in 01/02 — DO NOT re-standardize here.
*===============================================================

clear all
set more off
version 17

cap log close
log using "build_pooled.log", replace text

*-----------------------------------------------------------------
* Step 1 — Append
*-----------------------------------------------------------------
use "china2012_analytic.dta", clear
local n_2012 = _N
append using "china2024_analytic.dta"
local n_pool = _N
local n_2024 = `n_pool' - `n_2012'

di as txt "[AUDIT] Pooled N = `n_pool'  (2012 = `n_2012'  + 2024 = `n_2024')"
di as txt "[AUDIT] Expected pooled = 4,559 per manuscript v1.2; verified Python = 4,544 sample_base"

*-----------------------------------------------------------------
* Step 2 — Wave dummy + interactions for cross-wave Paternoster z-test
*-----------------------------------------------------------------
gen double FSTS_w24    = FSTS    * wave2024
gen double FSTSsq_w24  = FSTSsq  * wave2024
gen double lnEmp_w24   = lnEmp   * wave2024
gen double firmage_w24 = firmage * wave2024

label var FSTS_w24    "FSTS x wave2024"
label var FSTSsq_w24  "FSTSsq x wave2024"
label var lnEmp_w24   "lnEmp x wave2024"
label var firmage_w24 "firmage x wave2024"

*-----------------------------------------------------------------
* Step 3 — Audit pooled sample sizes
*-----------------------------------------------------------------
foreach s in analytic base dai tci full {
    count if sample_`s' == 1
    di as txt "[AUDIT] pooled sample_`s' = " r(N)
}
* Expected: base = 4,546 ; dai = 4,546 ; tci = 3,533 ; full = 3,533

*-----------------------------------------------------------------
* Step 4 — Panel-firm flag for cluster sanity
*-----------------------------------------------------------------
duplicates tag idstd, gen(idstd_dup)
count if idstd_dup > 0
di as txt "[AUDIT] Obs with duplicate idstd (panel firms across waves) = " r(N)
di as txt "[INFO] Expected 2 x 217 = 434 if all 2024 panel firms also pass focal filters"
di as txt "[WARN] Verified Python found 0 duplicate idstd — investigate panel link mechanism"
drop idstd_dup

compress
save "china_pooled.dta", replace
di as txt "[DONE] Saved china_pooled.dta"
log close
