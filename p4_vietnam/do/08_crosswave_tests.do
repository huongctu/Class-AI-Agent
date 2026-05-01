*! 08_crosswave_tests.do — Paternoster (1998) z-tests across waves
*! Reads the wave-specific coefficient/SE pairs from coefs_main_models.csv,
*! computes z = (b_A − b_B) / sqrt(SE_A^2 + SE_B^2) for the focal terms in
*! M7 (FSTSc, FSTSc2, TCI_z, DAI_z) and the M2 curvature terms, then writes
*! tables/table_paternoster.csv.

clear all
import delimited using "$tables/coefs_main_models.csv", clear varnames(1) ///
    stringcols(1 2 3) numericcols(4/9)

* Restrict to the model specifications and terms we want pairwise z-tests for.
keep if inlist(model, "M2", "M7")
keep if inlist(term, "FSTSc", "FSTSc2", "TCI_z", "DAI_z")
keep if substr(sample, 1, 4) == "VNM2"     // wave-specific only

keep sample model term b se
duplicates drop
reshape wide b se, i(model term) j(sample) string

tempfile pat
tempname rh
postfile `rh' str4 model str20 term str16 pair double(b_a b_b se_a se_b z p) ///
    using `pat', replace

local pairs "VNM2009 VNM2015 | VNM2009 VNM2023 | VNM2015 VNM2023"
local i = 1
local pair_count = 0
foreach pair in `pairs' {
    local pair_count = `pair_count' + 1
}

forvalues k = 1/3 {
    if `k' == 1 {
        local A "VNM2009"
        local B "VNM2015"
    }
    else if `k' == 2 {
        local A "VNM2009"
        local B "VNM2023"
    }
    else {
        local A "VNM2015"
        local B "VNM2023"
    }
    qui count
    forvalues r = 1/`r(N)' {
        local mdl  = model[`r']
        local trm  = term[`r']
        local b_a  = b`A'[`r']
        local b_b  = b`B'[`r']
        local se_a = se`A'[`r']
        local se_b = se`B'[`r']
        if !missing(`b_a', `b_b', `se_a', `se_b') {
            local z = (`b_a' - `b_b') / sqrt(`se_a'^2 + `se_b'^2)
            local p = 2 * (1 - normal(abs(`z')))
            post `rh' ("`mdl'") ("`trm'") ("`A'_vs_`B'") ///
                (`b_a') (`b_b') (`se_a') (`se_b') (`z') (`p')
        }
    }
}
postclose `rh'

preserve
use `pat', clear
export delimited using "$tables/table_paternoster.csv", replace
restore

di as txt "[08] table_paternoster.csv written"
