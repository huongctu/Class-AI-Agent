/*==============================================================================
  P5_APJM_China_Analysis.do
  =========================
  Reproduces ALL results for P5 APJM manuscript:
    China 2012 / 2024 (2 waves) + pooled

  Output:
    - Table 1: Descriptive statistics by wave
    - Table 2: Correlation matrix
    - Table 3: Hierarchical OLS regression by wave + pooled
    - Table 4: Robustness checks
    - Table 5: Paternoster z-tests (2012 vs 2024)
    - Figure 1: TCI/DAI temporal evolution
    - Figure 2: I-P curves overlay (2 waves)
    - Lind-Mehlum U-test per wave
    - Cohen's f²

  Specs:
    TCI = TCI_full (e6 + h1 + h8 + b8), require >=3 items
          CHN 2012: h1=CNo1, h8=CNo3 (FIXED — not CNo8)
    DAI = DAI_thin (c22b + e6) — cross-wave
    DAI_rich robustness for CHN 2024
    Controls = ln_empl firm_age foreign_dummy + wave_2024 (pooled)
    HC1 robust SE
    FSTS = d3c / 100

  Author: Do Thuy Huong
  Date:   April 2026
==============================================================================*/

clear all
set more off
set scheme s2color

global datadir "data/analysis"
global outdir  "data/analysis/stata_output"
capture mkdir "$outdir"

* =====================================================================
* 1. LOAD & PREPARE
* =====================================================================
import delimited "$datadir/pooled_wbes_6waves.csv", clear
keep if country == "CHN"
count
tab year

* ── Build composites ──
* TCI_full: require >=3 of 4 items
egen tci_full_n = rownonmiss(foreign_tech product_innov rd_spending quality_cert)
egen tci_full = rowmean(foreign_tech product_innov rd_spending quality_cert)
replace tci_full = . if tci_full_n < 3

* DAI_thin: cross-wave
egen dai_thin_n = rownonmiss(website foreign_tech)
egen dai_thin = rowmean(website foreign_tech)
replace dai_thin = . if dai_thin_n < 1

* DAI_rich: 2024 robustness only
gen epay_norm = epayment_pct / 100
gen epay_supp_norm = epay_supp_pct / 100
egen dai_rich_n = rownonmiss(website epay_norm epay_supp_norm)
egen dai_rich = rowmean(website epay_norm epay_supp_norm)
replace dai_rich = . if dai_rich_n < 2

* Z-standardize within each wave
foreach yr in 2012 2024 {
    foreach var in tci_full dai_thin {
        sum `var' if year == `yr'
        gen `var'_z_`yr' = (`var' - r(mean)) / r(sd) if year == `yr'
    }
}
gen tci_z = .
gen dai_z = .
foreach yr in 2012 2024 {
    replace tci_z = tci_full_z_`yr' if year == `yr'
    replace dai_z = dai_thin_z_`yr' if year == `yr'
}

* Pooled z-scores
sum tci_full
gen tci_z_pooled = (tci_full - r(mean)) / r(sd)
sum dai_thin
gen dai_z_pooled = (dai_thin - r(mean)) / r(sd)

* DAI_rich z for 2024
sum dai_rich if year == 2024
gen dai_rich_z = (dai_rich - r(mean)) / r(sd) if year == 2024

* Interaction terms (within-wave z)
gen fsts_x_tci = fsts * tci_z
gen fsts_sq_x_tci = fsts_sq * tci_z
gen fsts_x_dai = fsts * dai_z
gen fsts_sq_x_dai = fsts_sq * dai_z

* Pooled interactions
gen fsts_x_tci_p = fsts * tci_z_pooled
gen fsts_sq_x_tci_p = fsts_sq * tci_z_pooled
gen fsts_x_dai_p = fsts * dai_z_pooled
gen fsts_sq_x_dai_p = fsts_sq * dai_z_pooled

* DAI_rich interactions for 2024
gen fsts_x_dair = fsts * dai_rich_z
gen fsts_sq_x_dair = fsts_sq * dai_rich_z

* Wave dummy
gen wave_2024 = (year == 2024)

* Labels
label var tci_z        "TCI (z, within-wave)"
label var dai_z        "DAI-thin (z, within-wave)"
label var dai_rich_z   "DAI-rich (z, 2024 only)"
label var wave_2024    "Wave 2024"

* =====================================================================
* 2. TABLE 1: DESCRIPTIVE STATISTICS BY WAVE
* =====================================================================
di _n "============================================================"
di    "  TABLE 1: DESCRIPTIVE STATISTICS BY WAVE"
di    "============================================================"

foreach yr in 2012 2024 {
    di _n "--- China `yr' ---"
    tabstat ln_lp fsts tci_full dai_thin ///
        foreign_tech product_innov rd_spending quality_cert ///
        website epayment_pct ln_empl firm_age foreign_dummy ///
        if year == `yr', ///
        stat(n mean sd min max) columns(statistics) format(%9.3f)

    count if fsts == 0 & year == `yr'
    count if fsts > 0 & fsts <= 0.25 & year == `yr'
    count if fsts > 0.25 & fsts <= 0.75 & year == `yr'
    count if fsts > 0.75 & year == `yr'
}

* =====================================================================
* 3. TABLE 2: CORRELATION MATRIX
* =====================================================================
di _n "============================================================"
di    "  TABLE 2: CORRELATION MATRIX (POOLED)"
di    "============================================================"

pwcorr ln_lp fsts tci_full dai_thin ln_empl firm_age foreign_dummy, ///
    star(0.05) sig

* =====================================================================
* 4. TABLE 3: HIERARCHICAL REGRESSION — BY WAVE + POOLED
* =====================================================================
di _n "============================================================"
di    "  TABLE 3: REGRESSION BY WAVE"
di    "============================================================"

foreach yr in 2012 2024 {
    di _n "{'='*60}"
    di    "  CHINA `yr'"
    di    "{'='*60}"

    eststo `yr'_m0: reg ln_lp ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)

    eststo `yr'_m2: reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)

    eststo `yr'_m5: reg ln_lp fsts fsts_sq tci_z ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    eststo `yr'_m6: reg ln_lp fsts fsts_sq dai_z ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    eststo `yr'_m7: reg ln_lp fsts fsts_sq tci_z dai_z ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    eststo `yr'_m8: reg ln_lp fsts fsts_sq tci_z dai_z ///
        fsts_x_dai fsts_sq_x_dai ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    esttab `yr'_m0 `yr'_m2 `yr'_m5 `yr'_m6 `yr'_m7 `yr'_m8, ///
        b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
        stats(N r2_a, fmt(%9.0f %9.4f)) ///
        mtitles("Controls" "Inv-U" "+TCI" "+DAI" "Both" "Full") ///
        title("China `yr'")
}

* ── POOLED ──
di _n "{'='*60}"
di    "  CHINA POOLED (2012+2024)"
di    "{'='*60}"

eststo p_m0: reg ln_lp ln_empl firm_age foreign_dummy wave_2024, vce(robust)
eststo p_m2: reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy wave_2024, vce(robust)
eststo p_m5: reg ln_lp fsts fsts_sq tci_z_pooled ln_empl firm_age foreign_dummy wave_2024, vce(robust)
eststo p_m6: reg ln_lp fsts fsts_sq dai_z_pooled ln_empl firm_age foreign_dummy wave_2024, vce(robust)
eststo p_m7: reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ln_empl firm_age foreign_dummy wave_2024, vce(robust)
eststo p_m8: reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    fsts_x_dai_p fsts_sq_x_dai_p ///
    ln_empl firm_age foreign_dummy wave_2024, vce(robust)

esttab p_m0 p_m2 p_m5 p_m6 p_m7 p_m8, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("Controls" "Inv-U" "+TCI" "+DAI" "Both" "Full") ///
    title("China Pooled")

* Export
esttab 2012_m7 2024_m7 p_m7 ///
    using "$outdir/P5_Table3_TCI_DAI.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("2012" "2024" "Pooled")

* =====================================================================
* 5. LIND-MEHLUM U-TEST
* =====================================================================
di _n "============================================================"
di    "  LIND-MEHLUM U-TESTS"
di    "============================================================"

foreach yr in 2012 2024 {
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local b1 = _b[fsts]
    local b2 = _b[fsts_sq]
    local tp = -`b1' / (2 * `b2')

    nlcom _b[fsts], post
    local p_lo = 1 - normal(r(b)[1,1]/sqrt(r(V)[1,1]))
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    nlcom _b[fsts] + 2*_b[fsts_sq], post
    local p_hi = normal(r(b)[1,1]/sqrt(r(V)[1,1]))
    local p_lm = max(`p_lo', `p_hi')

    di "CHN `yr': TP = " %5.1f `tp'*100 "%, LM p = " %7.4f `p_lm' ///
        " " cond(`p_lm'<0.05,"CONFIRMED",cond(`p_lm'<0.1,"MARGINAL","NOT CONFIRMED"))
}

* Pooled
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy wave_2024, vce(robust)
local tp = (-_b[fsts]/(2*_b[fsts_sq]))*100
nlcom _b[fsts], post
local p_lo = 1 - normal(r(b)[1,1]/sqrt(r(V)[1,1]))
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy wave_2024, vce(robust)
nlcom _b[fsts] + 2*_b[fsts_sq], post
local p_hi = normal(r(b)[1,1]/sqrt(r(V)[1,1]))
di "CHN Pooled: TP = " %5.1f `tp' "%, LM p = " %7.4f max(`p_lo',`p_hi')

* =====================================================================
* 6. PATERNOSTER Z-TESTS (2012 vs 2024)
* =====================================================================
di _n "============================================================"
di    "  PATERNOSTER Z-TESTS: 2012 vs 2024"
di    "============================================================"

* TCI direct
quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
    if year == 2012, vce(robust)
local b_tci_12 = _b[tci_z]
local se_tci_12 = _se[tci_z]

quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
    if year == 2024, vce(robust)
local b_tci_24 = _b[tci_z]
local se_tci_24 = _se[tci_z]

local z = (`b_tci_12' - `b_tci_24') / sqrt(`se_tci_12'^2 + `se_tci_24'^2)
local p = 2 * (1 - normal(abs(`z')))
di "TCI: b12=" %7.3f `b_tci_12' " b24=" %7.3f `b_tci_24' ///
   " z=" %7.3f `z' " p=" %7.4f `p'

* DAI direct
quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
    if year == 2012, vce(robust)
local b_dai_12 = _b[dai_z]
local se_dai_12 = _se[dai_z]

quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
    if year == 2024, vce(robust)
local b_dai_24 = _b[dai_z]
local se_dai_24 = _se[dai_z]

local z = (`b_dai_12' - `b_dai_24') / sqrt(`se_dai_12'^2 + `se_dai_24'^2)
local p = 2 * (1 - normal(abs(`z')))
di "DAI: b12=" %7.3f `b_dai_12' " b24=" %7.3f `b_dai_24' ///
   " z=" %7.3f `z' " p=" %7.4f `p'

* FSTS (I-P shape)
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy if year==2012, vce(robust)
local b_f12 = _b[fsts]
local se_f12 = _se[fsts]
local b_f2_12 = _b[fsts_sq]
local se_f2_12 = _se[fsts_sq]
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy if year==2024, vce(robust)
local z = (`b_f12' - _b[fsts]) / sqrt(`se_f12'^2 + _se[fsts]^2)
local p = 2*(1-normal(abs(`z')))
di "FSTS linear: z=" %7.3f `z' " p=" %7.4f `p'
local z = (`b_f2_12' - _b[fsts_sq]) / sqrt(`se_f2_12'^2 + _se[fsts_sq]^2)
local p = 2*(1-normal(abs(`z')))
di "FSTS quadratic: z=" %7.3f `z' " p=" %7.4f `p'

* =====================================================================
* 7. FIGURES
* =====================================================================

* ── Figure 1: Coefficient evolution ──
preserve
    clear
    input year tci_b dai_b
    2012 `b_tci_12' `b_dai_12'
    2024 `b_tci_24' `b_dai_24'
    end

    twoway (connected tci_b year, lcolor(navy) mcolor(navy) msymbol(circle) lwidth(thick)) ///
           (connected dai_b year, lcolor(cranberry) mcolor(cranberry) msymbol(diamond) lwidth(thick) lpattern(dash)), ///
        title("Figure 1. TCI and DAI Direct Effects" ///
              "China 2012 vs 2024 (z-standardized β)", size(medium)) ///
        ytitle("β (z-standardized)") xtitle("Survey Wave") ///
        xlabel(2012 2024) ///
        yline(0, lcolor(gs12) lpattern(dot)) ///
        legend(order(1 "TCI direct" 2 "DAI direct") ring(0) pos(11)) ///
        note("TCI: Paternoster z = -2.85, p = .004" ///
             "DAI: Paternoster z = -2.22, p = .027") ///
        name(fig1_coef, replace)

    graph export "$outdir/P5_Figure1_Coef_Evolution.png", replace width(2400)
    graph export "$outdir/P5_Figure1_Coef_Evolution.pdf", replace
restore

* ── Figure 2: I-P curves overlay ──
foreach yr in 2012 2024 {
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    sum ln_empl if year == `yr', meanonly
    local m_e = r(mean)
    sum firm_age if year == `yr', meanonly
    local m_a = r(mean)
    sum foreign_dummy if year == `yr', meanonly
    local m_f = r(mean)
    gen yhat_`yr' = _b[_cons] + _b[fsts]*fsts + _b[fsts_sq]*fsts_sq ///
        + _b[ln_empl]*`m_e' + _b[firm_age]*`m_a' + _b[foreign_dummy]*`m_f' ///
        if year == `yr'
}

twoway (line yhat_2012 fsts if year==2012, sort lcolor(navy) lwidth(thick)) ///
       (line yhat_2024 fsts if year==2024, sort lcolor(cranberry) lwidth(thick) lpattern(dash)), ///
    title("Figure 2. I-P Curves — China 2012 vs 2024", size(medium)) ///
    ytitle("Ln(Labor Productivity)") xtitle("Export Intensity (FSTS)") ///
    xlabel(0 "0%" 0.2 "20%" 0.4 "40%" 0.6 "60%" 0.8 "80%" 1.0 "100%") ///
    legend(order(1 "2012" 2 "2024") ring(0) pos(5)) ///
    name(fig2_ip, replace)

graph export "$outdir/P5_Figure2_IP_Curves.png", replace width(2400)
graph export "$outdir/P5_Figure2_IP_Curves.pdf", replace

* =====================================================================
* 8. ROBUSTNESS
* =====================================================================
di _n "============================================================"
di    "  TABLE 4: ROBUSTNESS"
di    "============================================================"

* R1: DAI_rich for 2024
eststo rob_dair: reg ln_lp fsts fsts_sq tci_z dai_rich_z ///
    fsts_x_dair fsts_sq_x_dair ///
    ln_empl firm_age foreign_dummy if year == 2024, vce(robust)

* R2: Exclude micro
eststo rob_nomicro: reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2024 ///
    if employees >= 10, vce(robust)

* R3: Exporters only (pooled)
eststo rob_exp: reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2024 ///
    if fsts > 0, vce(robust)

esttab rob_dair rob_nomicro rob_exp, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("2024 DAI-rich" "No micro" "Exporters")

esttab rob_dair rob_nomicro rob_exp ///
    using "$outdir/P5_Table4_Robustness.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f))

* =====================================================================
* 9. EFFECT SIZES
* =====================================================================
di _n "============================================================"
di    "  COHEN'S f²"
di    "============================================================"

foreach yr in 2012 2024 {
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local r2_m2 = e(r2)

    quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local r2_m5 = e(r2)
    local f2_tci = (`r2_m5' - `r2_m2') / (1 - `r2_m5')

    quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local r2_m6 = e(r2)
    local f2_dai = (`r2_m6' - `r2_m2') / (1 - `r2_m6')

    di "CHN `yr': TCI f² = " %7.4f `f2_tci' ", DAI f² = " %7.4f `f2_dai'
}

* =====================================================================
* 10. VIF + BREUSCH-PAGAN
* =====================================================================
quietly reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2024
estat vif
estat hettest

* =====================================================================
di _n "============================================================"
di    "  P5 ANALYSIS COMPLETE"
di    "============================================================"
di "Output: $outdir/P5_*.rtf, P5_*.png, P5_*.pdf"

drop tci_full_n dai_thin_n dai_rich_n epay_norm epay_supp_norm
drop tci_full_z_* dai_thin_z_*
drop yhat_*
