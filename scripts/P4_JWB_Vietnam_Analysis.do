/*==============================================================================
  P4_JWB_Vietnam_Analysis.do
  ==========================
  Reproduces ALL results for P4 JWB manuscript:
    Vietnam 2009 / 2015 / 2023 (3 waves) + pooled

  Output:
    - Table 1: Descriptive statistics by wave
    - Table 2: Correlation matrix (pooled)
    - Table 3: Hierarchical OLS regression by wave + pooled
    - Table 4: Robustness checks
    - Table 5: Paternoster z-tests (cross-wave coefficient comparison)
    - Figure 1: TP stability across waves
    - Figure 2: TCI/DAI temporal evolution
    - Lind-Mehlum U-test per wave
    - Cohen's f²

  Specs:
    TCI = TCI_thin (e6 + b8) — VNM 2009 lacks h1/h8
    DAI = DAI_thin (c22b + e6) — cross-wave consistent
    Controls = ln_empl firm_age foreign_dummy + wave dummies (pooled)
    HC1 robust SE
    FSTS = d3c / 100 (0-1 proportion)

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
keep if country == "VNM"
count
tab year

* ── Build composites ──
* TCI_thin: mean(foreign_tech, quality_cert) — available all 3 waves
egen tci_n = rownonmiss(foreign_tech quality_cert)
egen tci_thin = rowmean(foreign_tech quality_cert)
replace tci_thin = . if tci_n < 1

* TCI_full: for robustness on 2015/2023 only
egen tci_full_n = rownonmiss(foreign_tech product_innov rd_spending quality_cert)
egen tci_full = rowmean(foreign_tech product_innov rd_spending quality_cert)
replace tci_full = . if tci_full_n < 3

* DAI_thin: mean(website, foreign_tech) — available all 3 waves
egen dai_thin_n = rownonmiss(website foreign_tech)
egen dai_thin = rowmean(website foreign_tech)
replace dai_thin = . if dai_thin_n < 1

* DAI_rich: for 2023 robustness only
gen epay_norm = epayment_pct / 100
gen epay_supp_norm = epay_supp_pct / 100
egen dai_rich_n = rownonmiss(website epay_norm epay_supp_norm)
egen dai_rich = rowmean(website epay_norm epay_supp_norm)
replace dai_rich = . if dai_rich_n < 2

* Z-standardize WITHIN each wave (important for cross-wave comparability)
foreach yr in 2009 2015 2023 {
    foreach var in tci_thin dai_thin {
        sum `var' if year == `yr'
        gen `var'_z_`yr' = (`var' - r(mean)) / r(sd) if year == `yr'
    }
}
* Combine wave-specific z-scores into single column
gen tci_z = .
gen dai_z = .
foreach yr in 2009 2015 2023 {
    replace tci_z = tci_thin_z_`yr' if year == `yr'
    replace dai_z = dai_thin_z_`yr' if year == `yr'
}

* For pooled: z-standardize across entire pooled sample
sum tci_thin
gen tci_z_pooled = (tci_thin - r(mean)) / r(sd)
sum dai_thin
gen dai_z_pooled = (dai_thin - r(mean)) / r(sd)

* Interaction terms
gen fsts_x_tci = fsts * tci_z
gen fsts_sq_x_tci = fsts_sq * tci_z
gen fsts_x_dai = fsts * dai_z
gen fsts_sq_x_dai = fsts_sq * dai_z

* Pooled interactions
gen fsts_x_tci_p = fsts * tci_z_pooled
gen fsts_sq_x_tci_p = fsts_sq * tci_z_pooled
gen fsts_x_dai_p = fsts * dai_z_pooled
gen fsts_sq_x_dai_p = fsts_sq * dai_z_pooled

* Wave dummies
gen wave_2015 = (year == 2015)
gen wave_2023 = (year == 2023)

* Labels
label var ln_lp         "Ln(Labor productivity)"
label var fsts          "FSTS"
label var fsts_sq       "FSTS²"
label var tci_z         "TCI (z, within-wave)"
label var dai_z         "DAI (z, within-wave)"
label var tci_z_pooled  "TCI (z, pooled)"
label var dai_z_pooled  "DAI (z, pooled)"
label var ln_empl       "Firm size (ln)"
label var firm_age      "Firm age"
label var foreign_dummy "Foreign-owned"
label var wave_2015     "Wave 2015"
label var wave_2023     "Wave 2023"

* =====================================================================
* 2. TABLE 1: DESCRIPTIVE STATISTICS BY WAVE
* =====================================================================
di _n "============================================================"
di    "  TABLE 1: DESCRIPTIVE STATISTICS BY WAVE"
di    "============================================================"

foreach yr in 2009 2015 2023 {
    di _n "--- Vietnam `yr' ---"
    tabstat ln_lp fsts tci_thin dai_thin ///
        foreign_tech quality_cert website ///
        ln_empl firm_age foreign_dummy ///
        if year == `yr', ///
        stat(n mean sd min max) columns(statistics) format(%9.3f)

    * Export distribution
    di "Export distribution:"
    count if fsts == 0 & year == `yr'
    count if fsts > 0 & fsts <= 0.25 & year == `yr'
    count if fsts > 0.25 & fsts <= 0.75 & year == `yr'
    count if fsts > 0.75 & year == `yr'
}

* =====================================================================
* 3. TABLE 2: CORRELATION MATRIX (pooled)
* =====================================================================
di _n "============================================================"
di    "  TABLE 2: CORRELATION MATRIX (POOLED)"
di    "============================================================"

pwcorr ln_lp fsts tci_thin dai_thin ln_empl firm_age foreign_dummy, ///
    star(0.05) sig

* =====================================================================
* 4. TABLE 3: HIERARCHICAL REGRESSION — BY WAVE
* =====================================================================
di _n "============================================================"
di    "  TABLE 3: REGRESSION BY WAVE"
di    "============================================================"

foreach yr in 2009 2015 2023 {
    di _n "{'='*60}"
    di    "  VIETNAM `yr'"
    di    "{'='*60}"

    * M0: Controls
    eststo `yr'_m0: reg ln_lp ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)

    * M2: Inverted-U
    eststo `yr'_m2: reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)

    * M5: + TCI direct
    eststo `yr'_m5: reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)

    * M6: + DAI direct
    eststo `yr'_m6: reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)

    * M7: TCI + DAI direct
    eststo `yr'_m7: reg ln_lp fsts fsts_sq tci_z dai_z ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    * M3: TCI + moderation
    eststo `yr'_m3: reg ln_lp fsts fsts_sq tci_z fsts_x_tci fsts_sq_x_tci ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    * M4: DAI + moderation
    eststo `yr'_m4: reg ln_lp fsts fsts_sq dai_z fsts_x_dai fsts_sq_x_dai ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    * M8: Full
    eststo `yr'_m8: reg ln_lp fsts fsts_sq tci_z dai_z ///
        fsts_x_dai fsts_sq_x_dai ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)

    * Display key models
    esttab `yr'_m0 `yr'_m2 `yr'_m5 `yr'_m6 `yr'_m7 `yr'_m8, ///
        b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
        stats(N r2_a, fmt(%9.0f %9.4f)) ///
        mtitles("Controls" "Inv-U" "+TCI" "+DAI" "Both" "Full") ///
        title("Vietnam `yr'")
}

* ── POOLED (3 waves + wave dummies) ──
di _n "{'='*60}"
di    "  VIETNAM POOLED (2009+2015+2023)"
di    "{'='*60}"

eststo p_m0: reg ln_lp ln_empl firm_age foreign_dummy ///
    wave_2015 wave_2023, vce(robust)

eststo p_m2: reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
    wave_2015 wave_2023, vce(robust)

eststo p_m5: reg ln_lp fsts fsts_sq tci_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2015 wave_2023, vce(robust)

eststo p_m6: reg ln_lp fsts fsts_sq dai_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2015 wave_2023, vce(robust)

eststo p_m7: reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2015 wave_2023, vce(robust)

eststo p_m8: reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    fsts_x_dai_p fsts_sq_x_dai_p ///
    ln_empl firm_age foreign_dummy wave_2015 wave_2023, vce(robust)

esttab p_m0 p_m2 p_m5 p_m6 p_m7 p_m8, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("Controls" "Inv-U" "+TCI" "+DAI" "Both" "Full") ///
    title("Vietnam Pooled")

* Export all to RTF
esttab 2009_m2 2015_m2 2023_m2 p_m2 ///
    using "$outdir/P4_Table3_InvU_bywave.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("2009" "2015" "2023" "Pooled") ///
    title("Table 3A. Inverted-U by Wave")

esttab 2009_m7 2015_m7 2023_m7 p_m7 ///
    using "$outdir/P4_Table3_TCI_DAI_bywave.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("2009" "2015" "2023" "Pooled") ///
    title("Table 3B. TCI + DAI Direct by Wave")

* =====================================================================
* 5. LIND-MEHLUM U-TEST — EACH WAVE + POOLED
* =====================================================================
di _n "============================================================"
di    "  LIND-MEHLUM U-TESTS"
di    "============================================================"

foreach yr in 2009 2015 2023 {
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)

    local b1 = _b[fsts]
    local b2 = _b[fsts_sq]
    local tp = -`b1' / (2 * `b2')

    nlcom _b[fsts], post
    local slope_lo = r(b)[1,1]
    local se_lo = sqrt(r(V)[1,1])
    local p_lo = 1 - normal(`slope_lo'/`se_lo')

    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    nlcom _b[fsts] + 2*_b[fsts_sq], post
    local slope_hi = r(b)[1,1]
    local se_hi = sqrt(r(V)[1,1])
    local p_hi = normal(`slope_hi'/`se_hi')

    local p_lm = max(`p_lo', `p_hi')
    di _n "VNM `yr': TP = " %5.1f `tp'*100 "%, LM p = " %7.4f `p_lm' ///
        " " cond(`p_lm'<0.05,"CONFIRMED",cond(`p_lm'<0.1,"MARGINAL","NOT CONFIRMED"))
}

* Pooled
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
    wave_2015 wave_2023, vce(robust)
local b1 = _b[fsts]
local b2 = _b[fsts_sq]
local tp = -`b1' / (2 * `b2')
nlcom _b[fsts], post
local p_lo = 1 - normal(r(b)[1,1]/sqrt(r(V)[1,1]))
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
    wave_2015 wave_2023, vce(robust)
nlcom _b[fsts] + 2*_b[fsts_sq], post
local p_hi = normal(r(b)[1,1]/sqrt(r(V)[1,1]))
local p_lm = max(`p_lo', `p_hi')
di _n "VNM Pooled: TP = " %5.1f `tp'*100 "%, LM p = " %7.4f `p_lm'

* =====================================================================
* 6. PATERNOSTER Z-TESTS (CROSS-WAVE COMPARISON)
* =====================================================================
di _n "============================================================"
di    "  PATERNOSTER Z-TESTS: CROSS-WAVE COMPARISONS"
di    "============================================================"

* TCI direct: 2009 vs 2023
quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
    if year == 2009, vce(robust)
local b_tci_09 = _b[tci_z]
local se_tci_09 = _se[tci_z]

quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
    if year == 2023, vce(robust)
local b_tci_23 = _b[tci_z]
local se_tci_23 = _se[tci_z]

local diff = `b_tci_09' - `b_tci_23'
local se_diff = sqrt(`se_tci_09'^2 + `se_tci_23'^2)
local z = `diff' / `se_diff'
local p = 2 * (1 - normal(abs(`z')))
di "TCI 2009 vs 2023: b09=" %7.3f `b_tci_09' " b23=" %7.3f `b_tci_23' ///
   " z=" %7.3f `z' " p=" %7.4f `p'

* DAI direct: 2009 vs 2023
quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
    if year == 2009, vce(robust)
local b_dai_09 = _b[dai_z]
local se_dai_09 = _se[dai_z]

quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
    if year == 2023, vce(robust)
local b_dai_23 = _b[dai_z]
local se_dai_23 = _se[dai_z]

local diff = `b_dai_09' - `b_dai_23'
local se_diff = sqrt(`se_dai_09'^2 + `se_dai_23'^2)
local z = `diff' / `se_diff'
local p = 2 * (1 - normal(abs(`z')))
di "DAI 2009 vs 2023: b09=" %7.3f `b_dai_09' " b23=" %7.3f `b_dai_23' ///
   " z=" %7.3f `z' " p=" %7.4f `p'

* TCI: 2009 vs 2015
quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
    if year == 2015, vce(robust)
local b_tci_15 = _b[tci_z]
local se_tci_15 = _se[tci_z]
local diff = `b_tci_09' - `b_tci_15'
local se_diff = sqrt(`se_tci_09'^2 + `se_tci_15'^2)
local z = `diff' / `se_diff'
local p = 2 * (1 - normal(abs(`z')))
di "TCI 2009 vs 2015: b09=" %7.3f `b_tci_09' " b15=" %7.3f `b_tci_15' ///
   " z=" %7.3f `z' " p=" %7.4f `p'

* DAI: 2009 vs 2015
quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
    if year == 2015, vce(robust)
local b_dai_15 = _b[dai_z]
local se_dai_15 = _se[dai_z]
local diff = `b_dai_09' - `b_dai_15'
local se_diff = sqrt(`se_dai_09'^2 + `se_dai_15'^2)
local z = `diff' / `se_diff'
local p = 2 * (1 - normal(abs(`z')))
di "DAI 2009 vs 2015: b09=" %7.3f `b_dai_09' " b15=" %7.3f `b_dai_15' ///
   " z=" %7.3f `z' " p=" %7.4f `p'

* =====================================================================
* 7. FIGURES
* =====================================================================
di _n "============================================================"
di    "  FIGURES"
di    "============================================================"

* ── Figure 1: TP across waves ──
* Collect TPs
local tp_09 = .
local tp_15 = .
local tp_23 = .

foreach yr in 2009 2015 2023 {
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local tp_`yr' = (-_b[fsts] / (2*_b[fsts_sq])) * 100
}

preserve
    clear
    input year tp
    2009 `tp_09'
    2015 `tp_15'
    2023 `tp_23'
    end

    twoway (connected tp year, lcolor(navy) mcolor(navy) msymbol(circle) lwidth(thick)), ///
        title("Figure 1. Turning Point Stability across Waves" ///
              "Vietnam 2009–2023", size(medium)) ///
        ytitle("Turning Point (%)") xtitle("Survey Wave") ///
        xlabel(2009 2015 2023) ylabel(25(5)45) ///
        yline(35, lcolor(gs12) lpattern(dash)) ///
        name(fig1_tp_waves, replace)

    graph export "$outdir/P4_Figure1_TP_Waves.png", replace width(2400)
    graph export "$outdir/P4_Figure1_TP_Waves.pdf", replace
restore

* ── Figure 2: TCI/DAI coefficient evolution ──
preserve
    clear
    input year tci_b dai_b
    2009 `b_tci_09' `b_dai_09'
    2015 `b_tci_15' `b_dai_15'
    2023 `b_tci_23' `b_dai_23'
    end

    twoway (connected tci_b year, lcolor(navy) mcolor(navy) msymbol(circle) lwidth(thick)) ///
           (connected dai_b year, lcolor(cranberry) mcolor(cranberry) msymbol(diamond) lwidth(thick) lpattern(dash)), ///
        title("Figure 2. TCI and DAI Direct Effects across Waves" ///
              "Vietnam 2009–2023 (z-standardized β)", size(medium)) ///
        ytitle("β (z-standardized)") xtitle("Survey Wave") ///
        xlabel(2009 2015 2023) ///
        yline(0, lcolor(gs12) lpattern(dot)) ///
        legend(order(1 "TCI direct" 2 "DAI direct") ring(0) pos(2) cols(1)) ///
        note("VNM 2015 attenuation consistent with WTO-transition institutional shock") ///
        name(fig2_coef_evolution, replace)

    graph export "$outdir/P4_Figure2_Coef_Evolution.png", replace width(2400)
    graph export "$outdir/P4_Figure2_Coef_Evolution.pdf", replace
restore

* ── Figure 3: I-P curve by wave (overlay) ──
foreach yr in 2009 2015 2023 {
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

twoway (line yhat_2009 fsts if year==2009, sort lcolor(navy) lwidth(thick)) ///
       (line yhat_2015 fsts if year==2015, sort lcolor(forest_green) lwidth(thick) lpattern(dash)) ///
       (line yhat_2023 fsts if year==2023, sort lcolor(cranberry) lwidth(thick) lpattern(longdash)), ///
    title("Figure 3. I-P Curves across Waves — Vietnam", size(medium)) ///
    ytitle("Ln(Labor Productivity)") xtitle("Export Intensity (FSTS)") ///
    xlabel(0 "0%" 0.2 "20%" 0.4 "40%" 0.6 "60%" 0.8 "80%" 1.0 "100%") ///
    legend(order(1 "2009" 2 "2015" 3 "2023") ring(0) pos(5) cols(1)) ///
    name(fig3_ip_waves, replace)

graph export "$outdir/P4_Figure3_IP_Waves.png", replace width(2400)
graph export "$outdir/P4_Figure3_IP_Waves.pdf", replace

* =====================================================================
* 8. ROBUSTNESS CHECKS
* =====================================================================
di _n "============================================================"
di    "  TABLE 4: ROBUSTNESS CHECKS"
di    "============================================================"

* R1: TCI_full for 2015 + 2023 (where h1/h8 available)
foreach yr in 2015 2023 {
    sum tci_full if year == `yr'
    gen tci_full_z_`yr' = (tci_full - r(mean)) / r(sd) if year == `yr'
}
gen tci_full_z = .
replace tci_full_z = tci_full_z_2015 if year == 2015
replace tci_full_z = tci_full_z_2023 if year == 2023

foreach yr in 2015 2023 {
    eststo rob_`yr': reg ln_lp fsts fsts_sq tci_full_z dai_z ///
        ln_empl firm_age foreign_dummy if year == `yr', vce(robust)
    di "R1 VNM `yr' TCI_full: b=" %7.3f _b[tci_full_z] " p=" %7.4f 2*ttail(e(df_r),abs(_b[tci_full_z]/_se[tci_full_z]))
}

* R2: DAI_rich for 2023
sum dai_rich if year == 2023
gen dai_rich_z_23 = (dai_rich - r(mean)) / r(sd) if year == 2023
gen fsts_x_dair = fsts * dai_rich_z_23
gen fsts_sq_x_dair = fsts_sq * dai_rich_z_23

eststo rob_2023r: reg ln_lp fsts fsts_sq tci_z dai_rich_z_23 ///
    fsts_x_dair fsts_sq_x_dair ///
    ln_empl firm_age foreign_dummy if year == 2023, vce(robust)

* R3: Exclude micro-firms
eststo rob_nomicro: reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2015 wave_2023 ///
    if employees >= 10, vce(robust)

esttab rob_2015 rob_2023 rob_2023r rob_nomicro, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("2015 TCI_full" "2023 TCI_full" "2023 DAI_rich" "No micro") ///
    title("Table 4. Robustness Checks")

esttab rob_2015 rob_2023 rob_2023r rob_nomicro ///
    using "$outdir/P4_Table4_Robustness.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f))

* =====================================================================
* 9. EFFECT SIZES
* =====================================================================
di _n "============================================================"
di    "  COHEN'S f² EFFECT SIZES"
di    "============================================================"

foreach yr in 2009 2015 2023 {
    * TCI direct: M2 → M5
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local r2_m2 = e(r2)
    quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local r2_m5 = e(r2)
    local f2_tci = (`r2_m5' - `r2_m2') / (1 - `r2_m5')
    di "VNM `yr' TCI f² = " %7.4f `f2_tci'

    * DAI direct: M2 → M6
    quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local r2_m6 = e(r2)
    local f2_dai = (`r2_m6' - `r2_m2') / (1 - `r2_m6')
    di "VNM `yr' DAI f² = " %7.4f `f2_dai'
}

* =====================================================================
* 10. CROSS-WAVE SUMMARY TABLE
* =====================================================================
di _n "============================================================"
di    "  CROSS-WAVE SUMMARY"
di    "============================================================"

di _n "Wave     N     TP      LM_p    TCI_b   TCI_p   DAI_b   DAI_p"
di    "─────────────────────────────────────────────────────────────"

foreach yr in 2009 2015 2023 {
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local n = e(N)
    local tp = (-_b[fsts]/(2*_b[fsts_sq]))*100

    quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local tci_b = _b[tci_z]
    local tci_p = 2*ttail(e(df_r),abs(_b[tci_z]/_se[tci_z]))

    quietly reg ln_lp fsts fsts_sq dai_z ln_empl firm_age foreign_dummy ///
        if year == `yr', vce(robust)
    local dai_b = _b[dai_z]
    local dai_p = 2*ttail(e(df_r),abs(_b[dai_z]/_se[dai_z]))

    di "`yr'   " %5.0f `n' "  " %5.1f `tp' "%  " ///
       "  " %7.3f `tci_b' "  " %7.4f `tci_p' ///
       "  " %7.3f `dai_b' "  " %7.4f `dai_p'
}

* =====================================================================
* 11. VIF + BREUSCH-PAGAN
* =====================================================================
di _n "============================================================"
di    "  DIAGNOSTICS: VIF + BREUSCH-PAGAN"
di    "============================================================"

quietly reg ln_lp fsts fsts_sq tci_z_pooled dai_z_pooled ///
    ln_empl firm_age foreign_dummy wave_2015 wave_2023
estat vif
estat hettest

* =====================================================================
di _n "============================================================"
di    "  P4 ANALYSIS COMPLETE"
di    "============================================================"
di "Output files in: $outdir/"

* Clean up temp vars
drop tci_n tci_full_n dai_thin_n dai_rich_n
drop epay_norm epay_supp_norm
drop tci_thin_z_* dai_thin_z_*
drop tci_full_z_* dai_rich_z_23 fsts_x_dair fsts_sq_x_dair
drop yhat_*
