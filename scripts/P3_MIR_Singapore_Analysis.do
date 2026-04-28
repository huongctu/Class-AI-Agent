/*==============================================================================
  P3_MIR_Singapore_Analysis.do
  ============================
  Reproduces ALL results for P3 MIR manuscript:
    - Table 1: Descriptive statistics + correlation matrix
    - Table 2: Hierarchical OLS regression M0-M8
    - Table 3: Robustness checks (4 specifications)
    - Table 4: Marginal effects of DAI across FSTS
    - Figure 1: DAI marginal effects plot with 95% CI
    - Figure 2: I-P curve with scatter
    - Lind-Mehlum U-test
    - Cohen's f² effect sizes
    - VIF diagnostics
    - Breusch-Pagan heteroskedasticity test

  Input:  data/analysis/pooled_wbes_6waves.csv
          (built by scripts/build-pooled-dataset.py with CNo3 fix)

  Specs:  Controls = ln_empl firm_age foreign_dummy
          manager_exp DROPPED (VIF = 5.85 with ln_empl)
          HC1 robust standard errors
          FSTS = d3c / 100 (direct exports, 0-1 proportion)
          TCI/DAI z-standardized within sample

  Author: Do Thuy Huong
  Date:   April 2026
==============================================================================*/

clear all
set more off
set scheme s2color

* ─── EDIT THIS PATH ───
global datadir "data/analysis"
global outdir  "data/analysis/stata_output"
capture mkdir "$outdir"

* =====================================================================
* 1. LOAD DATA
* =====================================================================
import delimited "$datadir/pooled_wbes_6waves.csv", clear
describe
keep if country == "SGP" & year == 2023
count
* Should be N = 623

* =====================================================================
* 2. BUILD COMPOSITES
* =====================================================================

* TCI_full: mean of 4 items, require >=3 non-missing
egen tci_n = rownonmiss(foreign_tech product_innov rd_spending quality_cert)
egen tci_raw = rowmean(foreign_tech product_innov rd_spending quality_cert)
replace tci_raw = . if tci_n < 3

* DAI_rich: mean of website + epayment/100 + epay_supp/100, require >=2
gen epay_norm = epayment_pct / 100
gen epay_supp_norm = epay_supp_pct / 100
egen dai_n = rownonmiss(website epay_norm epay_supp_norm)
egen dai_raw = rowmean(website epay_norm epay_supp_norm)
replace dai_raw = . if dai_n < 2

* DAI_thin: mean of website + foreign_tech (for robustness)
egen dai_thin_n = rownonmiss(website foreign_tech)
egen dai_thin_raw = rowmean(website foreign_tech)
replace dai_thin_raw = . if dai_thin_n < 1

* Z-standardize within sample
foreach var in tci_raw dai_raw dai_thin_raw {
    sum `var'
    gen `var'_z = (`var' - r(mean)) / r(sd)
}
rename tci_raw_z tci_z
rename dai_raw_z dai_z
rename dai_thin_raw_z dai_thin_z

* Interaction terms
gen fsts_x_tci = fsts * tci_z
gen fsts_sq_x_tci = fsts_sq * tci_z
gen fsts_x_dai = fsts * dai_z
gen fsts_sq_x_dai = fsts_sq * dai_z
gen fsts_x_dai_thin = fsts * dai_thin_z
gen fsts_sq_x_dai_thin = fsts_sq * dai_thin_z

* Labels
label var ln_lp        "Ln(Labor productivity)"
label var fsts         "FSTS (direct export intensity)"
label var fsts_sq      "FSTS squared"
label var tci_z        "TCI (z-standardized)"
label var dai_z        "DAI-rich (z-standardized)"
label var dai_thin_z   "DAI-thin (z-standardized)"
label var ln_empl      "Firm size (ln employees)"
label var firm_age     "Firm age (years)"
label var foreign_dummy "Foreign-owned"
label var fsts_x_dai   "FSTS × DAI"
label var fsts_sq_x_dai "FSTS² × DAI"

* =====================================================================
* 3. TABLE 1: DESCRIPTIVE STATISTICS
* =====================================================================
di _n "============================================================"
di    "  TABLE 1: DESCRIPTIVE STATISTICS"
di    "============================================================"

sum ln_lp fsts tci_raw dai_raw ///
    foreign_tech product_innov rd_spending quality_cert ///
    website epayment_pct ln_empl firm_age foreign_dummy, detail

tabstat ln_lp fsts tci_raw dai_raw ///
    foreign_tech product_innov rd_spending quality_cert ///
    website epayment_pct ln_empl firm_age foreign_dummy, ///
    stat(n mean sd min max) columns(statistics) format(%9.3f)

* Correlation matrix
di _n "============================================================"
di    "  TABLE 1B: CORRELATION MATRIX"
di    "============================================================"

pwcorr ln_lp fsts tci_raw dai_raw ln_empl firm_age foreign_dummy, ///
    star(0.05) sig

* =====================================================================
* 4. TABLE 2: HIERARCHICAL OLS REGRESSION (M0 - M8)
* =====================================================================
di _n "============================================================"
di    "  TABLE 2: HIERARCHICAL OLS REGRESSION"
di    "============================================================"

* M0: Controls only
eststo m0: reg ln_lp ln_empl firm_age foreign_dummy, vce(robust)

* M1: + FSTS linear
eststo m1: reg ln_lp fsts ln_empl firm_age foreign_dummy, vce(robust)

* M2: + FSTS² (inverted-U)
eststo m2: reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)

* M3: + TCI direct + TCI moderation
eststo m3: reg ln_lp fsts fsts_sq tci_z fsts_x_tci fsts_sq_x_tci ///
    ln_empl firm_age foreign_dummy, vce(robust)

* M4: + DAI direct + DAI moderation
eststo m4: reg ln_lp fsts fsts_sq dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)

* M5: TCI direct only (no moderation)
eststo m5: reg ln_lp fsts fsts_sq tci_z ///
    ln_empl firm_age foreign_dummy, vce(robust)

* M6: DAI direct only (no moderation)
eststo m6: reg ln_lp fsts fsts_sq dai_z ///
    ln_empl firm_age foreign_dummy, vce(robust)

* M7: TCI + DAI both direct (no moderation)
eststo m7: reg ln_lp fsts fsts_sq tci_z dai_z ///
    ln_empl firm_age foreign_dummy, vce(robust)

* M8: FULL — TCI direct + DAI direct + DAI moderation
eststo m8: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)

* Export table
esttab m0 m2 m5 m6 m7 m4 m8 using "$outdir/Table2_regression.rtf", ///
    replace b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "Adj. R²")) ///
    title("Table 2. Hierarchical OLS Regression — Singapore 2023") ///
    mtitles("(1)" "(2)" "(3)" "(4)" "(5)" "(6)" "(7)") ///
    note("HC1 robust SE. TP=83.0%. LM p=.301. DAI mod joint F(2,607)=3.38, p=.035.")

* Also display in console
esttab m0 m2 m5 m6 m7 m4 m8, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f))

* =====================================================================
* 5. LIND-MEHLUM U-TEST
* =====================================================================
di _n "============================================================"
di    "  LIND-MEHLUM U-TEST (from M2)"
di    "============================================================"

quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)

* Turning point
local b1 = _b[fsts]
local b2 = _b[fsts_sq]
local tp = -`b1' / (2 * `b2')
di "Turning point = " `tp' * 100 "%"

* Slope at FSTS = 0 (lower bound)
nlcom _b[fsts], post
local slope_lo = r(b)[1,1]
local se_lo = sqrt(r(V)[1,1])
local t_lo = `slope_lo' / `se_lo'
local p_lo = 1 - normal(`t_lo')
di "Slope at FSTS=0: " `slope_lo' " (SE=" `se_lo' ", t=" `t_lo' ", p_one=" `p_lo' ")"

* Slope at FSTS = 1 (upper bound)
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)
nlcom _b[fsts] + 2*_b[fsts_sq], post
local slope_hi = r(b)[1,1]
local se_hi = sqrt(r(V)[1,1])
local t_hi = `slope_hi' / `se_hi'
local p_hi = normal(`t_hi')
di "Slope at FSTS=1: " `slope_hi' " (SE=" `se_hi' ", t=" `t_hi' ", p_one=" `p_hi' ")"

local p_lm = max(`p_lo', `p_hi')
di _n "Lind-Mehlum joint p = " `p_lm'
di "Status: " cond(`p_lm' < 0.05, "CONFIRMED", cond(`p_lm' < 0.10, "MARGINAL", "NOT CONFIRMED"))

* Alternative: use utest command if installed
capture which utest
if _rc == 0 {
    quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)
    utest fsts fsts_sq
}
else {
    di "Note: Install utest for formal Lind-Mehlum test: ssc install utest"
}

* =====================================================================
* 6. DAI MODERATION JOINT F-TEST
* =====================================================================
di _n "============================================================"
di    "  DAI MODERATION JOINT F-TEST"
di    "============================================================"

* M7 (restricted: no DAI interactions)
quietly reg ln_lp fsts fsts_sq tci_z dai_z ///
    ln_empl firm_age foreign_dummy, vce(robust)
estimates store m7_r

* M8 (full: with DAI interactions)
quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)
estimates store m8_f

* Joint test
test fsts_x_dai fsts_sq_x_dai
di "Joint F = " r(F) ", p = " r(p)

* =====================================================================
* 7. TABLE 4: MARGINAL EFFECTS OF DAI ACROSS FSTS
* =====================================================================
di _n "============================================================"
di    "  TABLE 4: MARGINAL EFFECTS"
di    "============================================================"

quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)

* Marginal effect = b_dai + b_fsts_x_dai * FSTS + b_fsts_sq_x_dai * FSTS²
foreach pct in 0 5 10 15 20 30 50 70 100 {
    local x = `pct' / 100
    nlcom _b[dai_z] + _b[fsts_x_dai]*`x' + _b[fsts_sq_x_dai]*`x'^2, post
    local me = r(b)[1,1]
    local se = sqrt(r(V)[1,1])
    local t  = `me' / `se'
    local p  = 2 * (1 - normal(abs(`t')))
    local ci_lo = `me' - 1.96 * `se'
    local ci_hi = `me' + 1.96 * `se'
    di "FSTS = " %3.0f `pct' "%:  ME = " %7.3f `me' "  SE = " %7.3f `se' ///
       "  p = " %7.4f `p' "  [" %7.3f `ci_lo' ", " %7.3f `ci_hi' "]"
    quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
        ln_empl firm_age foreign_dummy, vce(robust)
}

* =====================================================================
* 8. FIGURE 1: DAI MARGINAL EFFECTS PLOT
* =====================================================================
di _n "============================================================"
di    "  FIGURE 1: DAI MARGINAL EFFECTS PLOT"
di    "============================================================"

quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)

* Generate marginal effects across FSTS range
preserve
    clear
    set obs 101
    gen fsts_plot = (_n - 1) / 100
    gen me = .
    gen me_se = .
    gen me_lo = .
    gen me_hi = .
restore

* Use margins command (cleaner)
quietly reg ln_lp c.fsts##c.fsts##c.dai_z tci_z ln_empl firm_age foreign_dummy, vce(robust)

margins, dydx(dai_z) at(fsts=(0(0.05)1)) post
marginsplot, ///
    recast(line) recastci(rarea) ///
    ciopt(color(gs12%50)) ///
    plotopts(lcolor(black) lwidth(medthick)) ///
    yline(0, lcolor(red) lpattern(dash)) ///
    title("Figure 1. Marginal Effect of DAI on Productivity" ///
          "across Export Intensity — Singapore 2023", size(medium)) ///
    ytitle("Marginal Effect of DAI (z) on Ln(LP)") ///
    xtitle("Export Intensity (FSTS)") ///
    xlabel(0 "0%" 0.2 "20%" 0.4 "40%" 0.6 "60%" 0.8 "80%" 1.0 "100%") ///
    name(fig1_dai_margins, replace)

graph export "$outdir/Figure1_DAI_Marginal_Effects.png", replace width(2400)
graph export "$outdir/Figure1_DAI_Marginal_Effects.pdf", replace

* =====================================================================
* 9. FIGURE 2: I-P CURVE
* =====================================================================
di _n "============================================================"
di    "  FIGURE 2: I-P CURVE"
di    "============================================================"

quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)

* Predicted values at means of controls
sum ln_empl, meanonly
local m_empl = r(mean)
sum firm_age, meanonly
local m_age = r(mean)
sum foreign_dummy, meanonly
local m_foreign = r(mean)

gen yhat_ip = _b[_cons] + _b[fsts]*fsts + _b[fsts_sq]*fsts_sq ///
    + _b[ln_empl]*`m_empl' + _b[firm_age]*`m_age' + _b[foreign_dummy]*`m_foreign'

local tp_pct = (-_b[fsts] / (2*_b[fsts_sq])) * 100

twoway (scatter ln_lp fsts, mcolor(gs12) msize(vsmall) msymbol(circle)) ///
       (line yhat_ip fsts, sort lcolor(black) lwidth(thick)), ///
    xline(`=`tp_pct'/100', lcolor(red) lpattern(dash)) ///
    title("Figure 2. Internationalization–Performance Relationship" ///
          "Singapore 2023 (N = 623)", size(medium)) ///
    ytitle("Ln(Labor Productivity)") ///
    xtitle("Export Intensity (FSTS)") ///
    xlabel(0 "0%" 0.2 "20%" 0.4 "40%" 0.6 "60%" 0.8 "80%" 1.0 "100%") ///
    text(12.7 `=`tp_pct'/100+0.03' "TP = `=round(`tp_pct',1)'%", color(red) size(small)) ///
    legend(order(1 "Observed" 2 "Predicted") ring(0) pos(2)) ///
    name(fig2_ip_curve, replace)

graph export "$outdir/Figure2_IP_Curve.png", replace width(2400)
graph export "$outdir/Figure2_IP_Curve.pdf", replace

* =====================================================================
* 10. TABLE 3: ROBUSTNESS CHECKS
* =====================================================================
di _n "============================================================"
di    "  TABLE 3: ROBUSTNESS CHECKS"
di    "============================================================"

* R0: Baseline (already run as m8)
eststo r0: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)

* R1: DAI_thin (drop k33)
gen fsts_x_dai_t = fsts * dai_thin_z
gen fsts_sq_x_dai_t = fsts_sq * dai_thin_z
eststo r1: reg ln_lp fsts fsts_sq tci_z dai_thin_z fsts_x_dai_t fsts_sq_x_dai_t ///
    ln_empl firm_age foreign_dummy, vce(robust)

* R2: Exclude micro-firms (employees < 10)
eststo r2: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy if employees >= 10, vce(robust)

* R3: Exporters only (FSTS > 0)
eststo r3: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy if fsts > 0, vce(robust)

* Display
esttab r0 r1 r2 r3, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    keep(tci_z dai_z dai_thin_z fsts_sq_x_dai fsts_sq_x_dai_t) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("Baseline" "DAI-thin" "No micro" "Exporters")

* Export
esttab r0 r1 r2 r3 using "$outdir/Table3_robustness.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f) labels("N" "Adj. R²")) ///
    title("Table 3. Robustness Checks") ///
    mtitles("Baseline" "DAI-thin" "No micro" "Exporters") ///
    note("HC1 robust SE. All models include FSTS, FSTS², controls.")

* =====================================================================
* 11. EFFECT SIZES (Cohen's f²)
* =====================================================================
di _n "============================================================"
di    "  EFFECT SIZES (Cohen's f²)"
di    "============================================================"

* f² = (R²_full - R²_reduced) / (1 - R²_full)

* TCI direct: M2 → M5
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)
local r2_m2 = e(r2)
quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy, vce(robust)
local r2_m5 = e(r2)
local f2_tci = (`r2_m5' - `r2_m2') / (1 - `r2_m5')
di "TCI direct f² (M2→M5) = " %7.4f `f2_tci' ///
   " (" cond(`f2_tci'>=0.35,"large",cond(`f2_tci'>=0.15,"medium",cond(`f2_tci'>=0.02,"small","negligible"))) ")"

* DAI moderation: M7 → M8
quietly reg ln_lp fsts fsts_sq tci_z dai_z ln_empl firm_age foreign_dummy, vce(robust)
local r2_m7 = e(r2)
quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)
local r2_m8 = e(r2)
local f2_dai = (`r2_m8' - `r2_m7') / (1 - `r2_m8')
di "DAI moderation f² (M7→M8) = " %7.4f `f2_dai' ///
   " (" cond(`f2_dai'>=0.35,"large",cond(`f2_dai'>=0.15,"medium",cond(`f2_dai'>=0.02,"small","negligible"))) ")"

* I-P quadratic: M1 → M2
quietly reg ln_lp fsts ln_empl firm_age foreign_dummy, vce(robust)
local r2_m1 = e(r2)
local f2_ip = (`r2_m2' - `r2_m1') / (1 - `r2_m2')
di "I-P quadratic f² (M1→M2) = " %7.4f `f2_ip'

* =====================================================================
* 12. VIF DIAGNOSTICS
* =====================================================================
di _n "============================================================"
di    "  VIF DIAGNOSTICS"
di    "============================================================"

* M7 spec (without interactions — interpretable VIF)
quietly reg ln_lp fsts fsts_sq tci_z dai_z ln_empl firm_age foreign_dummy
estat vif

* Check manager_exp VIF
di _n "With manager_exp added:"
capture {
    quietly reg ln_lp fsts fsts_sq tci_z dai_z ln_empl firm_age foreign_dummy manager_exp
    estat vif
}

* =====================================================================
* 13. BREUSCH-PAGAN TEST
* =====================================================================
di _n "============================================================"
di    "  BREUSCH-PAGAN HETEROSKEDASTICITY TEST"
di    "============================================================"

quietly reg ln_lp fsts fsts_sq tci_z dai_z ln_empl firm_age foreign_dummy
estat hettest
di "→ HC1 robust SE justified if p < .05"

* =====================================================================
* 14. INCREMENTAL F-TESTS
* =====================================================================
di _n "============================================================"
di    "  INCREMENTAL F-TESTS (ΔR²)"
di    "============================================================"

* M0 → M2: Adding FSTS + FSTS²
quietly reg ln_lp ln_empl firm_age foreign_dummy, vce(robust)
estimates store inc_m0
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)
estimates store inc_m2
di "M0→M2 (FSTS + FSTS²):"
lrtest inc_m0 inc_m2, force

* M2 → M5: Adding TCI
quietly reg ln_lp fsts fsts_sq ln_empl firm_age foreign_dummy, vce(robust)
estimates store inc_m2b
quietly reg ln_lp fsts fsts_sq tci_z ln_empl firm_age foreign_dummy, vce(robust)
estimates store inc_m5
di "M2→M5 (TCI direct):"
test tci_z

* M5 → M3: Adding TCI moderation
quietly reg ln_lp fsts fsts_sq tci_z fsts_x_tci fsts_sq_x_tci ///
    ln_empl firm_age foreign_dummy, vce(robust)
di "M5→M3 (TCI moderation):"
test fsts_x_tci fsts_sq_x_tci

* M7 → M8: Adding DAI moderation
quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    ln_empl firm_age foreign_dummy, vce(robust)
di "M7→M8 (DAI moderation):"
test fsts_x_dai fsts_sq_x_dai

* =====================================================================
* 15. SAVE ALL RESULTS LOG
* =====================================================================
di _n "============================================================"
di    "  ALL TESTS COMPLETE"
di    "============================================================"
di "Output files saved to: $outdir/"
di "  Table2_regression.rtf"
di "  Table3_robustness.rtf"
di "  Figure1_DAI_Marginal_Effects.png/pdf"
di "  Figure2_IP_Curve.png/pdf"

* Clean up
drop yhat_ip epay_norm epay_supp_norm tci_n dai_n dai_thin_n
drop fsts_x_dai_t fsts_sq_x_dai_t

di _n "Done. Review results and paste into manuscript."
