*! 04_append_pooled.do — append the three Vietnam waves into a pooled file
*! After append the script re-centers FSTS by wave (so FSTSc is wave-demeaned
*! in the pooled sample, matching how the manuscript reports H1) and re-
*! z-standardises TCI_z / DAI_z within wave so cross-wave coefficients remain
*! comparable. TCI_full_z is preserved only for 2015/2023 (the wave dummy
*! absorbs its absence in 2009 when entered in robustness).

clear all
use "$work/vnm2009_clean.dta", clear
append using "$work/vnm2015_clean.dta"
append using "$work/vnm2023_clean.dta"

* Recompute FSTSc within wave (manuscript spec) ------------------------------
drop FSTSc FSTSc2
bysort wave: egen _fsts_mean = mean(FSTS)
gen FSTSc  = FSTS - _fsts_mean
gen FSTSc2 = FSTSc^2
drop _fsts_mean

* Re-z-standardise TCI / DAI within wave -------------------------------------
foreach v in TCI_thin DAI_thin {
    cap drop `v'_zw
    bysort wave: egen _m = mean(`v')
    bysort wave: egen _s = sd(`v')
    gen `v'_zw = (`v' - _m) / _s
    drop _m _s
}
drop TCI_z DAI_z
rename TCI_thin_zw TCI_z
rename DAI_thin_zw DAI_z

label var FSTSc  "FSTS, mean-centred within wave (pooled)"
label var FSTSc2 "FSTSc squared (pooled)"
label var TCI_z  "TCI_thin (z within wave, pooled)"
label var DAI_z  "DAI_thin (z within wave, pooled)"

compress
save "$work/vnm_pooled_clean.dta", replace
di as txt "[04] vnm_pooled_clean.dta saved with N = " _N
tab wave
