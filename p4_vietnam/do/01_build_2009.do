*! 01_build_2009.do — Vietnam WBES 2009 analytic file
*! Variables present in the 2009 release (verified):
*!   d2 l1 d3c b8 e6 c22b b2b b5 a2 a4a a4b
*! Variables not present (must remain undefined for this wave):
*!   h1 h8 k33 k38   (so TCI_full and DAI_rich do not exist for 2009)

clear all
do "$do/_lib_build.do"

use "$raw/vietnam_2009.dta", clear
gen wave = 2009

p4_clean_missing d2 l1 d3c b8 e6 c22b b2b b5 a2 a4b a4a

* Outcome and controls --------------------------------------------------------
gen lnLP = ln(d2 / l1)
gen lnEmp = ln(l1)
gen FirmAge = wave - b5
gen ForeignOwned = (b2b > 0) if !missing(b2b)

* Internationalisation --------------------------------------------------------
gen FSTS    = d3c / 100
gen export_any = (FSTS > 0) if !missing(FSTS)

* Capability composites -------------------------------------------------------
p4_recode01 b8 e6 c22b
egen TCI_thin = rowmean(b8_r e6_r)
egen DAI_thin = rowmean(c22b_r e6_r)

* (TCI_full and DAI_rich are not constructed for 2009 — items missing.)

* Sector fixed effects --------------------------------------------------------
gen sector1 = real(substr(a4b, 1, 1)) if !missing(a4b)
replace sector1 = real(substr(a4a, 1, 1)) if missing(sector1) & !missing(a4a)

* Listwise on the focal set ---------------------------------------------------
egen miss_focal = rowmiss(lnLP lnEmp FirmAge ForeignOwned FSTS TCI_thin DAI_thin sector1)
keep if miss_focal == 0
drop miss_focal

* Within-wave centering and standardisation -----------------------------------
qui sum FSTS
gen FSTSc  = FSTS - r(mean)
gen FSTSc2 = FSTSc^2

p4_zwithin TCI_thin, gen(TCI_z)
p4_zwithin DAI_thin, gen(DAI_z)

label var lnLP        "log labour productivity"
label var FSTS        "direct-export intensity (share)"
label var FSTSc       "FSTS, mean-centred within wave"
label var FSTSc2      "FSTSc squared"
label var TCI_z       "TCI_thin (z within wave)"
label var DAI_z       "DAI_thin (z within wave)"
label var lnEmp       "log permanent employees"
label var FirmAge     "firm age (years)"
label var ForeignOwned "foreign ownership > 0 (0/1)"
label var sector1     "broad ISIC sector (first digit)"

keep wave lnLP lnEmp FirmAge ForeignOwned FSTS FSTSc FSTSc2 export_any ///
     TCI_thin DAI_thin TCI_z DAI_z sector1 a2

compress
save "$work/vnm2009_clean.dta", replace
di as txt "[01] vnm2009_clean.dta saved with N = " _N
