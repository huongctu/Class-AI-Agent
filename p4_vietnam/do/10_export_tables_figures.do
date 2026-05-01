*! 10_export_tables_figures.do — final manuscript-facing outputs
*! Builds the four canonical tables (Table 1 descriptives, Table 2 baseline,
*! Table 3 robustness, Table LM) and Figure 2 from the artefacts produced by
*! steps 05–09. Figure 1 (conceptual model) is a non-data figure and is not
*! produced here.
*!
*! Tables are written as CSV in $tables; Figure 2 is written as both a PDF and
*! a 300-dpi PNG in $figs.

clear all

* ===========================================================================
* TABLE 1 — descriptive statistics by wave
* ===========================================================================
use "$work/vnm_pooled_clean.dta", clear
gen ones = 1
collapse (mean) lnLP FSTS export_any TCI_thin DAI_thin lnEmp FirmAge ForeignOwned ///
         (sd)   sd_lnLP    = lnLP ///
                sd_FSTS    = FSTS ///
                sd_TCI     = TCI_thin ///
                sd_DAI     = DAI_thin ///
                sd_lnEmp   = lnEmp ///
                sd_FirmAge = FirmAge ///
         (sum)  N = ones, by(wave)
export delimited using "$tables/table_1_descriptives.csv", replace

* ===========================================================================
* TABLE 2 — baseline coefficients (M7 both direct, by wave + pooled)
* ===========================================================================
import delimited using "$tables/coefs_main_models.csv", clear varnames(1) ///
    stringcols(1 2 3) numericcols(4/9)
keep if model == "M7"
keep if inlist(term, "FSTSc", "FSTSc2", "TCI_z", "DAI_z", "lnEmp", "FirmAge", "1.ForeignOwned")
keep sample term b se p ci_lo ci_hi nobs r2
export delimited using "$tables/table_2_baseline.csv", replace

* ===========================================================================
* TABLE 3 — robustness: TCI moderation (M3) + DAI moderation (M4) +
*           full-model DAI interactions (M8) + joint F-tests
* ===========================================================================
import delimited using "$tables/coefs_main_models.csv", clear varnames(1) ///
    stringcols(1 2 3) numericcols(4/9)
keep if inlist(model, "M3", "M4", "M8")
keep if regexm(term, "FSTSc.*TCI_z") | regexm(term, "FSTSc.*DAI_z") | ///
        inlist(term, "TCI_z", "DAI_z", "FSTSc", "FSTSc2")
keep sample model term b se p nobs
tempfile t3_coefs
save `t3_coefs', replace

import delimited using "$tables/joint_tests_main_models.csv", clear varnames(1) ///
    stringcols(1 2 3) numericcols(4 5)
gen term = "joint_" + test
gen b   = .
gen se  = .
gen nobs = .
rename p p
rename f f
keep sample model term f p

merge 1:1 sample model term using `t3_coefs', nogen
sort sample model term
export delimited using "$tables/table_3_robustness.csv", replace

* ===========================================================================
* TABLE LM — Lind-Mehlum: just rename the file from step 06 for clarity
* ===========================================================================
copy "$tables/table_lind_mehlum.csv" "$tables/table_LM.csv", replace

* ===========================================================================
* FIGURE 2 — predicted lnLP across FSTS by wave (and pooled)
* ===========================================================================
use "$work/vnm_pooled_clean.dta", clear

global base_controls   "c.lnEmp c.FirmAge i.ForeignOwned i.sector1"
global pooled_controls "c.lnEmp c.FirmAge i.ForeignOwned i.sector1 i.wave"

* Hold controls at within-wave means
foreach v in lnEmp FirmAge ForeignOwned {
    qui sum `v'
    local mean_`v' = r(mean)
}

tempfile preds
tempname rh
postfile `rh' str12 sample double(FSTS lnLP_hat lnLP_lo lnLP_hi) using `preds', replace

cap program drop p4_predict
program define p4_predict
    syntax , sample(string) controls(string) [if(string)]
    qui regress lnLP c.FSTSc c.FSTSc2 `controls' `if', vce(robust)
    qui sum FSTS `if', meanonly
    local fmean = r(mean)
    forvalues f = 0(2)100 {
        local fc = `f'/100 - `fmean'
        local fc2 = `fc'^2
        local b0 = _b[_cons]
        local b1 = _b[FSTSc]
        local b2 = _b[FSTSc2]
        local yhat = `b0' + `b1' * `fc' + `b2' * `fc2'
        post `0' ("`sample'") (`f'/100) (`yhat') (.) (.)
    }
end

levelsof wave, local(waves)
foreach w of local waves {
    p4_predict `rh', sample("VNM`w'") controls("$base_controls") if("if wave==`w'")
}
p4_predict `rh', sample("VNMpooled") controls("$pooled_controls")

postclose `rh'

preserve
use `preds', clear
export delimited using "$tables/figure_2_predictions.csv", replace
* Plot if Stata graph engine is available (silent failure on minimal builds)
cap {
    twoway (line lnLP_hat FSTS if sample=="VNM2009",  lpattern(solid)) ///
           (line lnLP_hat FSTS if sample=="VNM2015",  lpattern(dash)) ///
           (line lnLP_hat FSTS if sample=="VNM2023",  lpattern(longdash)) ///
           (line lnLP_hat FSTS if sample=="VNMpooled",lpattern(shortdash)), ///
        legend(order(1 "2009" 2 "2015" 3 "2023" 4 "Pooled")) ///
        xtitle("Direct-export intensity (FSTS)") ///
        ytitle("Predicted ln(labour productivity)")
    graph export "$figs/figure_2_main_results.pdf", replace
    graph export "$figs/figure_2_main_results.png", width(2400) replace
}
restore

di as txt "[10] manuscript tables and figure_2 written under $tables and $figs"
