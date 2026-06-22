*! 02_build_2015.do — Vietnam WBES 2015 analytic file
*! Variables present in the 2015 release (verified):
*!   d2 l1 d3c b8 e6 c22b b2b b5 a2 a4a a4b h1 h8
*! Variables not present:
*!   k33 k38   (so DAI_rich is still 2023-only)

clear all
do "$do/_lib_build.do"

use "$raw/vietnam_2015.dta", clear
gen wave = 2015

p4_clean_missing d2 l1 d3c b8 e6 c22b b2b b5 a2 a4b a4a h1 h8

gen lnLP = ln(d2 / l1)
gen lnEmp = ln(l1)
gen FirmAge = wave - b5
gen ForeignOwned = (b2b > 0) if !missing(b2b)

gen FSTS    = d3c / 100
gen export_any = (FSTS > 0) if !missing(FSTS)

p4_recode01 b8 e6 c22b h1 h8

egen TCI_thin = rowmean(b8_r e6_r)
egen DAI_thin = rowmean(c22b_r e6_r)
egen TCI_full = rowmean(b8_r e6_r h1_r h8_r)

gen sector1 = real(substr(a4b, 1, 1)) if !missing(a4b)
replace sector1 = real(substr(a4a, 1, 1)) if missing(sector1) & !missing(a4a)

egen miss_focal = rowmiss(lnLP lnEmp FirmAge ForeignOwned FSTS TCI_thin DAI_thin sector1)
keep if miss_focal == 0
drop miss_focal

qui sum FSTS
gen FSTSc  = FSTS - r(mean)
gen FSTSc2 = FSTSc^2

p4_zwithin TCI_thin, gen(TCI_z)
p4_zwithin DAI_thin, gen(DAI_z)
p4_zwithin TCI_full, gen(TCI_full_z)

label var lnLP        "log labour productivity"
label var FSTS        "direct-export intensity (share)"
label var FSTSc       "FSTS, mean-centred within wave"
label var FSTSc2      "FSTSc squared"
label var TCI_z       "TCI_thin (z within wave)"
label var DAI_z       "DAI_thin (z within wave)"
label var TCI_full_z  "TCI_full (z within wave, 2015/2023)"
label var lnEmp       "log permanent employees"
label var FirmAge     "firm age (years)"
label var ForeignOwned "foreign ownership > 0 (0/1)"
label var sector1     "broad ISIC sector (first digit)"

keep wave lnLP lnEmp FirmAge ForeignOwned FSTS FSTSc FSTSc2 export_any ///
     TCI_thin DAI_thin TCI_z DAI_z TCI_full TCI_full_z sector1 a2

compress
save "$work/vnm2015_clean.dta", replace
di as txt "[02] vnm2015_clean.dta saved with N = " _N
