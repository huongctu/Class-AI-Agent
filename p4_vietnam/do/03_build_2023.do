*! 03_build_2023.do — Vietnam WBES 2023 analytic file
*! Variables present in the 2023 release (verified):
*!   d2 l1 d3c b8 e6 c22b b2b b5 a2 a4a h1 h8 k33 k38
*! Variables not present:
*!   a4b   (so sector1 must come from a4a in this wave)

clear all
do "$do/_lib_build.do"

use "$raw/vietnam_2023.dta", clear
gen wave = 2023

p4_clean_missing d2 l1 d3c b8 e6 c22b b2b b5 a2 a4a h1 h8 k33 k38

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

* DAI_rich: continuous (k33/100, k38/100) and binary (k33>0, k38>0) versions ---
gen k33c = k33 / 100 if k33 >= 0 & !missing(k33)
gen k38c = k38 / 100 if k38 >= 0 & !missing(k38)
gen k33b = (k33 > 0)  if !missing(k33)
gen k38b = (k38 > 0)  if !missing(k38)

egen DAI_rich_cont = rowmean(c22b_r e6_r k33c k38c)
egen DAI_rich_bin  = rowmean(c22b_r e6_r k33b k38b)

* Sector FE — 2023 release ships a4a only ------------------------------------
gen sector1 = real(substr(a4a, 1, 1)) if !missing(a4a)

egen miss_focal = rowmiss(lnLP lnEmp FirmAge ForeignOwned FSTS TCI_thin DAI_thin sector1)
keep if miss_focal == 0
drop miss_focal

qui sum FSTS
gen FSTSc  = FSTS - r(mean)
gen FSTSc2 = FSTSc^2

p4_zwithin TCI_thin,        gen(TCI_z)
p4_zwithin DAI_thin,        gen(DAI_z)
p4_zwithin TCI_full,        gen(TCI_full_z)
p4_zwithin DAI_rich_cont,   gen(DAI_rich_cont_z)
p4_zwithin DAI_rich_bin,    gen(DAI_rich_bin_z)

label var DAI_rich_cont_z "DAI_rich continuous (z within wave, 2023)"
label var DAI_rich_bin_z  "DAI_rich binary (z within wave, 2023)"

keep wave lnLP lnEmp FirmAge ForeignOwned FSTS FSTSc FSTSc2 export_any ///
     TCI_thin DAI_thin TCI_z DAI_z ///
     TCI_full TCI_full_z ///
     DAI_rich_cont DAI_rich_bin DAI_rich_cont_z DAI_rich_bin_z ///
     sector1 a2

compress
save "$work/vnm2023_clean.dta", replace
di as txt "[03] vnm2023_clean.dta saved with N = " _N
