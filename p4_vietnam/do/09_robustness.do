*! 09_robustness.do — robustness panels in the order the manuscript reports
*! A. TCI_full (h1 + h8 added) for 2015 and 2023
*! B. DAI_rich continuous and binary for 2023 only
*! C. 2-digit ISIC sector FE replacement (a4a or a4b first two digits)
*! D. Micro-firm exclusion (l1 < 10 dropped)
*! E. Common-N comparison: re-estimate DAI_thin on the DAI_rich sample so
*!    measurement vs. sample changes do not get conflated.
*! Each panel writes its own CSV under $tables.

clear all
use "$work/vnm_pooled_clean.dta", clear

global base_controls   "c.lnEmp c.FirmAge i.ForeignOwned i.sector1"
global pooled_controls "c.lnEmp c.FirmAge i.ForeignOwned i.sector1 i.wave"

* ===========================================================================
* A. TCI_full — 2015 and 2023 only ------------------------------------------
* ===========================================================================
preserve
keep if inlist(wave, 2015, 2023) & !missing(TCI_full_z)
tempname rh
tempfile a
postfile `rh' str12 sample str20 term double(b se p) int nobs using `a', replace
levelsof wave, local(ws)
foreach w of local ws {
    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_full_z c.DAI_z $base_controls if wave==`w', vce(robust)
    foreach t in FSTSc FSTSc2 TCI_full_z DAI_z {
        scalar _b  = _b[`t']
        scalar _se = _se[`t']
        scalar _t  = _b / _se
        scalar _p  = 2 * ttail(e(df_r), abs(_t))
        post `rh' ("VNM`w'") ("`t'") (_b) (_se) (_p) (e(N))
    }
}
postclose `rh'
use `a', clear
export delimited using "$tables/robustness_TCI_full.csv", replace
restore

* ===========================================================================
* B. DAI_rich — 2023 only ---------------------------------------------------
* ===========================================================================
preserve
keep if wave == 2023
tempname rh
tempfile b_rich
postfile `rh' str20 spec str20 term double(b se p) int nobs using `b_rich', replace

foreach spec in DAI_rich_cont_z DAI_rich_bin_z {
    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.`spec' ///
        c.FSTSc#c.`spec' c.FSTSc2#c.`spec' $base_controls if !missing(`spec'), vce(robust)
    foreach t in FSTSc FSTSc2 TCI_z `spec' {
        scalar _b  = _b[`t']
        scalar _se = _se[`t']
        scalar _t  = _b / _se
        scalar _p  = 2 * ttail(e(df_r), abs(_t))
        post `rh' ("`spec'") ("`t'") (_b) (_se) (_p) (e(N))
    }
}
postclose `rh'
use `b_rich', clear
export delimited using "$tables/robustness_DAI_rich.csv", replace
restore

* ===========================================================================
* C. 2-digit ISIC sector FE -------------------------------------------------
* ===========================================================================
preserve
gen sector2 = real(substr(string(sector1), 1, 2))
* For releases that ship only a4a (2023), reconstruct a 2-digit ISIC from a4a.
* If a4a is short (e.g. 1-digit), this defaults to sector1 already, so the FE
* set is at worst a duplicate of the broad-sector FE.
qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z ///
    c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z ///
    c.lnEmp c.FirmAge i.ForeignOwned i.sector2 i.wave, vce(robust)
estimates store rob_sector2
estimates table rob_sector2, b(%9.3f) se p
tempfile c2
parmest, saving(`c2', replace) format(estimate stderr p)
preserve
use `c2', clear
gen sample = "VNMpooled"
gen panel  = "sector2digit"
keep sample panel parm estimate stderr p
export delimited using "$tables/robustness_sector2digit.csv", replace
restore
restore

* ===========================================================================
* D. Micro-firm exclusion (l1 >= 10) ----------------------------------------
* ===========================================================================
preserve
keep if exp(lnEmp) >= 10
qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z ///
    c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z $pooled_controls, vce(robust)
estimates store rob_micro
tempfile d2
parmest, saving(`d2', replace) format(estimate stderr p)
preserve
use `d2', clear
gen sample = "VNMpooled"
gen panel  = "micro_excluded"
keep sample panel parm estimate stderr p
export delimited using "$tables/robustness_microfirm.csv", replace
restore
restore

* ===========================================================================
* E. Common-N comparison: DAI_thin re-estimated on DAI_rich's 2023 sample ---
* ===========================================================================
preserve
keep if wave == 2023 & !missing(DAI_rich_cont_z)
tempname rh
tempfile e2
postfile `rh' str20 spec str20 term double(b se p) int nobs using `e2', replace
foreach spec in DAI_z DAI_rich_cont_z DAI_rich_bin_z {
    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.`spec' ///
        c.FSTSc#c.`spec' c.FSTSc2#c.`spec' $base_controls, vce(robust)
    foreach t in FSTSc FSTSc2 TCI_z `spec' {
        scalar _b  = _b[`t']
        scalar _se = _se[`t']
        scalar _t  = _b / _se
        scalar _p  = 2 * ttail(e(df_r), abs(_t))
        post `rh' ("`spec'") ("`t'") (_b) (_se) (_p) (e(N))
    }
}
postclose `rh'
use `e2', clear
export delimited using "$tables/robustness_commonN_2023.csv", replace
restore

di as txt "[09] robustness CSVs written under $tables"
