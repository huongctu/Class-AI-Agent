/******************************************************************************
 * P4_Vietnam_FullAnalysis.do
 * ===========================
 * Stata mirror of the verified Python pipeline for the v4.4 manuscript.
 *
 * NOT EXECUTED BY THE AUTHORS — provided for third-party verification.
 * Implements exactly the same specification as `code/p4_python_check.py`:
 *   - Listwise deletion on focal vars + first available sector code
 *   - WBES non-response code -9 treated as missing
 *   - TCI_thin = mean(b8 dummy, e6 dummy)  / DAI_thin = mean(c22b dummy, e6 dummy)
 *   - Within-wave z-standardisation of TCI / DAI
 *   - OLS with HC1 robust SE
 *
 * Usage
 * -----
 *   cd "<repo>/manuscripts/p4-jwb-vietnam/"
 *   stata -b do code/P4_Vietnam_FullAnalysis.do
 *
 * Tested on Stata 18; should also run on 17.
 *****************************************************************************/

version 17
clear all
set more off

local datadir  "../../wbes_dta"   // user-supplied path to .dta files
local outdir   "output"
capture mkdir  "`outdir'"

* ---- 1. Append three waves into a long file --------------------------------
tempfile vn_pool
foreach yr in 2009 2015 2023 {
    use "`datadir'/Vietnam`yr'fulldata.dta", clear
    gen wave        = "`yr'"
    gen survey_year = `yr'
    save `vn_pool'_`yr', replace
}
use `vn_pool'_2009, clear
append using `vn_pool'_2015 `vn_pool'_2023, force

* ---- 2. WBES -9 to missing -------------------------------------------------
ds, has(type numeric)
foreach v of varlist `r(varlist)' {
    qui replace `v' = . if `v' == -9
}

* ---- 3. Listwise on focal set ---------------------------------------------
* Sector code: a4b for 2009/2015, a4a for 2023
gen sector_src = a4b if a4b != .
replace sector_src = a4a if missing(sector_src) & a4a != .
keep if !missing(d2, l1, d3c, b8, e6, c22b, b5, b2b, sector_src)
keep if d2 > 0 & l1 > 0

* ---- 4. Variable construction ---------------------------------------------
gen lnLP        = ln(d2 / l1)
gen fsts        = d3c / 100
bysort wave: egen mean_fsts_w = mean(fsts)
gen fsts_c      = fsts - mean_fsts_w
gen fsts_c2     = fsts_c^2
gen b8_dum      = (b8 == 1)
gen e6_dum      = (e6 == 1)
gen c22b_dum    = (c22b == 1)
gen tci_thin    = (b8_dum + e6_dum) / 2
gen dai_thin    = (c22b_dum + e6_dum) / 2

* Within-wave z-standardisation
bysort wave: egen mean_tci_w = mean(tci_thin)
bysort wave: egen sd_tci_w   = sd(tci_thin)
gen tci_z = (tci_thin - mean_tci_w) / sd_tci_w
bysort wave: egen mean_dai_w = mean(dai_thin)
bysort wave: egen sd_dai_w   = sd(dai_thin)
gen dai_z = (dai_thin - mean_dai_w) / sd_dai_w

gen lnemp        = ln(l1)
gen firmage      = survey_year - b5
gen foreign_owned = (b2b > 0)
gen sector_broad = real(substr(string(sector_src), 1, 1))

* ---- 5. Baseline OLS-HC1 by wave ------------------------------------------
foreach w in 2009 2015 2023 {
    di as result _newline "*** Wave `w' baseline ***"
    regress lnLP fsts_c fsts_c2 tci_z dai_z lnemp firmage foreign_owned i.sector_broad ///
        if wave == "`w'", robust
    estimates store base_`w'
}

di as result _newline "*** Pooled (with wave FE) ***"
regress lnLP fsts_c fsts_c2 tci_z dai_z lnemp firmage foreign_owned i.sector_broad i.wave, robust
estimates store base_pool

* ---- 6. H2 moderation -----------------------------------------------------
gen fsts_c_x_tci_z   = fsts_c * tci_z
gen fsts_c2_x_tci_z  = fsts_c2 * tci_z
foreach w in 2009 2015 2023 {
    di as result _newline "*** H2 moderation wave `w' ***"
    regress lnLP fsts_c fsts_c2 tci_z dai_z fsts_c_x_tci_z fsts_c2_x_tci_z ///
        lnemp firmage foreign_owned i.sector_broad if wave == "`w'", robust
    test fsts_c_x_tci_z fsts_c2_x_tci_z
}
regress lnLP fsts_c fsts_c2 tci_z dai_z fsts_c_x_tci_z fsts_c2_x_tci_z ///
    lnemp firmage foreign_owned i.sector_broad i.wave, robust
test fsts_c_x_tci_z fsts_c2_x_tci_z

* ---- 7. H4 moderation -----------------------------------------------------
gen fsts_c_x_dai_z   = fsts_c * dai_z
gen fsts_c2_x_dai_z  = fsts_c2 * dai_z
foreach w in 2009 2015 2023 {
    di as result _newline "*** H4 moderation wave `w' ***"
    regress lnLP fsts_c fsts_c2 tci_z dai_z fsts_c_x_dai_z fsts_c2_x_dai_z ///
        lnemp firmage foreign_owned i.sector_broad if wave == "`w'", robust
    test fsts_c_x_dai_z fsts_c2_x_dai_z
}
regress lnLP fsts_c fsts_c2 tci_z dai_z fsts_c_x_dai_z fsts_c2_x_dai_z ///
    lnemp firmage foreign_owned i.sector_broad i.wave, robust
test fsts_c_x_dai_z fsts_c2_x_dai_z

* ---- 8. Lind-Mehlum U-test (utest) ----------------------------------------
* Requires the user-contributed `utest` package (Lind & Mehlum 2010)
* ssc install utest, replace
foreach w in 2009 2015 2023 {
    di as result _newline "*** Lind-Mehlum wave `w' ***"
    regress lnLP fsts_c fsts_c2 tci_z dai_z lnemp firmage foreign_owned i.sector_broad ///
        if wave == "`w'", robust
    capture utest fsts_c fsts_c2
}
regress lnLP fsts_c fsts_c2 tci_z dai_z lnemp firmage foreign_owned i.sector_broad i.wave, robust
capture utest fsts_c fsts_c2

* End of do-file.
