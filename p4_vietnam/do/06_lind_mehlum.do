*! 06_lind_mehlum.do — turning points + Lind–Mehlum U-test
*! Runs the M2 inverted-U specification per wave and pooled, applies utest on
*! the actual range of FSTSc, and writes a long-format CSV with the turning
*! point in raw FSTS units, delta-method 95% CI, and the U-test p-value.

clear all
use "$work/vnm_pooled_clean.dta", clear

global base_controls   "c.lnEmp c.FirmAge i.ForeignOwned i.sector1"
global pooled_controls "c.lnEmp c.FirmAge i.ForeignOwned i.sector1 i.wave"

tempname rh
tempfile lm
postfile `rh' str12 sample double(b_l b_q tp_c tp_lo tp_hi tp_raw tp_raw_lo tp_raw_hi) ///
    double(lm_p) int nobs using `lm', replace

cap program drop p4_lm_one
program define p4_lm_one
    syntax , sample(string) controls(string) [if(string)]
    qui regress lnLP c.FSTSc c.FSTSc2 `controls' `if', vce(robust)
    qui sum FSTSc `if', meanonly
    local lo = r(min)
    local hi = r(max)
    qui utest FSTSc FSTSc2, range(`lo' `hi')

    local b_l = _b[FSTSc]
    local b_q = _b[FSTSc2]
    local nobs = e(N)

    * turning point in centred space + delta-method CI
    qui nlcom (tp: -_b[FSTSc] / (2 * _b[FSTSc2]))
    matrix B = r(b)
    matrix V = r(V)
    local tp_c   = B[1,1]
    local tp_se  = sqrt(V[1,1])
    local tp_lo  = `tp_c' - 1.96 * `tp_se'
    local tp_hi  = `tp_c' + 1.96 * `tp_se'

    * back-transform to raw FSTS using the pre-centring mean of FSTS in this sample
    qui sum FSTS `if', meanonly
    local fmean = r(mean)
    local tp_raw    = `tp_c'  + `fmean'
    local tp_raw_lo = `tp_lo' + `fmean'
    local tp_raw_hi = `tp_hi' + `fmean'

    * Lind–Mehlum p-value: utest stores it in r(p_overall) on recent versions;
    * fall back to r(p) if the older signature is in use.
    local p = .
    cap local p = r(p_overall)
    if missing(`p') {
        cap local p = r(p)
    }

    post `0' ("`sample'") (`b_l') (`b_q') ///
        (`tp_c') (`tp_lo') (`tp_hi') (`tp_raw') (`tp_raw_lo') (`tp_raw_hi') ///
        (`p') (`nobs')
end

levelsof wave, local(waves)
foreach w of local waves {
    p4_lm_one `rh', sample("VNM`w'") controls("$base_controls") if("if wave==`w'")
}
p4_lm_one `rh', sample("VNMpooled") controls("$pooled_controls")

postclose `rh'

preserve
use `lm', clear
export delimited using "$tables/table_lind_mehlum.csv", replace
restore

di as txt "[06] table_lind_mehlum.csv written"
