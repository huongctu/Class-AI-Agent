/*==============================================================================
  P3_MIR_Refine_AI_Reruns.do
  ==========================
  Addresses 4 Refine AI critiques:
    #1 Sector FE: add broad sector dummies (a0: manufacturing/retail/services)
    #2 Demote nonlinear: text edits only (no rerun needed)
    #3 DAI_thin redefine: website (c22b) ONLY — remove foreign_tech overlap
    #4 H2/H3 alignment: text edits only (no rerun needed)

  Run AFTER P3_MIR_Singapore_Analysis.do
  Uses same pooled CSV as input.
==============================================================================*/

clear all
set more off
set scheme s2color

global datadir "data/analysis"
global outdir  "data/analysis/stata_output"
capture mkdir "$outdir"

import delimited "$datadir/pooled_wbes_6waves.csv", clear
keep if country == "SGP" & year == 2023

* ── Rebuild composites (same as main do-file) ──
egen tci_n = rownonmiss(foreign_tech product_innov rd_spending quality_cert)
egen tci_raw = rowmean(foreign_tech product_innov rd_spending quality_cert)
replace tci_raw = . if tci_n < 3

gen epay_norm = epayment_pct / 100
gen epay_supp_norm = epay_supp_pct / 100
egen dai_n = rownonmiss(website epay_norm epay_supp_norm)
egen dai_raw = rowmean(website epay_norm epay_supp_norm)
replace dai_raw = . if dai_n < 2

* Z-standardize
foreach var in tci_raw dai_raw {
    sum `var'
    gen `var'_z = (`var' - r(mean)) / r(sd)
}
rename tci_raw_z tci_z
rename dai_raw_z dai_z

* ============================================================
* SECTOR FIXED EFFECTS (Refine AI #1)
* ============================================================
* a0 = WBES sampling sector: 1=Manufacturing, 2=Retail, 3=Other Services
* Load from raw .dta or use sector column if available
* For now, load a0 from the raw Singapore file:
* merge 1:1 using "Singapore2023fulldata.dta", keepusing(a0) nogen
* OR if sector already in pooled CSV:

* Create broad sector dummies
* If a0 not in pooled CSV, load from raw:
capture confirm variable sector
if _rc != 0 {
    di "NOTE: 'sector' not in pooled CSV. Using a0 from raw .dta."
    di "Add this merge before running:"
    di "  merge 1:1 _n using raw_sgp.dta, keepusing(a0) nogen"
    di "  gen sector = a0"
    di "For now, creating placeholder dummies..."
    gen sector = .
}

tab sector, gen(sec_)

* ============================================================
* REDEFINED DAI_THIN (Refine AI #3)
* ============================================================
* OLD: DAI_thin = mean(website, foreign_tech) ← WRONG: foreign_tech is TCI item
* NEW: DAI_thin = website only (c22b) — single binary indicator
gen dai_thin_new = website
sum dai_thin_new
gen dai_thin_new_z = (dai_thin_new - r(mean)) / r(sd)

* Interactions
gen fsts_x_dai = fsts * dai_z
gen fsts_sq_x_dai = fsts_sq * dai_z
gen fsts_x_dai_t = fsts * dai_thin_new_z
gen fsts_sq_x_dai_t = fsts_sq * dai_thin_new_z

* ============================================================
* RERUN M2-M8 WITH SECTOR FE
* ============================================================
di _n "============================================================"
di    "  TABLE 2 RERUN: WITH SECTOR FE"
di    "============================================================"

local sector_fe "sec_2 sec_3"
local controls "ln_empl firm_age foreign_dummy `sector_fe'"

eststo sf_m0: reg ln_lp `controls', vce(robust)
eststo sf_m2: reg ln_lp fsts fsts_sq `controls', vce(robust)
eststo sf_m5: reg ln_lp fsts fsts_sq tci_z `controls', vce(robust)
eststo sf_m6: reg ln_lp fsts fsts_sq dai_z `controls', vce(robust)
eststo sf_m7: reg ln_lp fsts fsts_sq tci_z dai_z `controls', vce(robust)
eststo sf_m8: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai `controls', vce(robust)

esttab sf_m0 sf_m2 sf_m5 sf_m6 sf_m7 sf_m8, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    title("Table 2 with Sector FE")

esttab sf_m0 sf_m2 sf_m5 sf_m6 sf_m7 sf_m8 ///
    using "$outdir/P3_Table2_with_SectorFE.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f))

* Joint F for DAI moderation with sector FE
test fsts_x_dai fsts_sq_x_dai
di "DAI moderation joint F = " r(F) ", p = " r(p)

* Lind-Mehlum with sector FE
quietly reg ln_lp fsts fsts_sq `controls', vce(robust)
local tp = (-_b[fsts]/(2*_b[fsts_sq]))*100
di "TP (with sector FE) = " %5.1f `tp' "%"

* ============================================================
* RERUN R1: DAI_THIN = WEBSITE ONLY
* ============================================================
di _n "============================================================"
di    "  R1 RERUN: DAI = WEBSITE ONLY (no foreign_tech)"
di    "============================================================"

eststo r1_new: reg ln_lp fsts fsts_sq tci_z dai_thin_new_z ///
    fsts_x_dai_t fsts_sq_x_dai_t `controls', vce(robust)

esttab r1_new, b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) stats(N r2_a)
test fsts_x_dai_t fsts_sq_x_dai_t
di "R1-new DAI mod joint F = " r(F) ", p = " r(p)

* ============================================================
* FULL ROBUSTNESS TABLE (6 specs with sector FE)
* ============================================================
di _n "============================================================"
di    "  TABLE 3 FULL ROBUSTNESS (with sector FE)"
di    "============================================================"

* R0: Baseline + sector FE (already sf_m8)
* R1: DAI = website only + sector FE (already r1_new)
* R2: Exclude micro + sector FE
eststo r2_sf: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    `controls' if employees >= 10, vce(robust)

* R3: SMEs + sector FE
eststo r3_sf: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    `controls' if employees <= 200, vce(robust)

* R4: Exporters only + sector FE
eststo r4_sf: reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai ///
    `controls' if fsts > 0, vce(robust)

esttab sf_m8 r1_new r2_sf r3_sf r4_sf, ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    keep(tci_z dai_z dai_thin_new_z fsts_sq_x_dai fsts_sq_x_dai_t) ///
    stats(N r2_a, fmt(%9.0f %9.4f)) ///
    mtitles("Baseline+SF" "DAI=web" "No micro" "SMEs" "Exporters")

esttab sf_m8 r1_new r2_sf r3_sf r4_sf ///
    using "$outdir/P3_Table3_Robustness_SectorFE.rtf", replace ///
    b(3) se(3) star(* 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.4f))

* ============================================================
* TABLE 4: MARGINAL EFFECTS (with sector FE)
* ============================================================
di _n "============================================================"
di    "  TABLE 4: MARGINAL EFFECTS (with sector FE)"
di    "============================================================"

quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai `controls', vce(robust)
foreach pct in 0 5 10 15 20 30 50 70 100 {
    local x = `pct'/100
    nlcom _b[dai_z] + _b[fsts_x_dai]*`x' + _b[fsts_sq_x_dai]*`x'^2, post
    local me = r(b)[1,1]
    local se = sqrt(r(V)[1,1])
    local p = 2*(1-normal(abs(`me'/`se')))
    di "FSTS=" %3.0f `pct' "%:  ME=" %7.3f `me' "  SE=" %7.3f `se' "  p=" %7.4f `p'
    quietly reg ln_lp fsts fsts_sq tci_z dai_z fsts_x_dai fsts_sq_x_dai `controls', vce(robust)
}

* ============================================================
* FIGURE 2 RERUN (marginsplot with sector FE)
* ============================================================
quietly reg ln_lp c.fsts##c.fsts##c.dai_z tci_z `controls', vce(robust)
margins, dydx(dai_z) at(fsts=(0(0.05)1)) post
marginsplot, ///
    recast(line) recastci(rarea) ///
    ciopt(color(gs12%50)) plotopts(lcolor(black) lwidth(medthick)) ///
    yline(0, lcolor(red) lpattern(dash)) ///
    title("Figure 2. Marginal Effect of DAI (with sector FE)") ///
    ytitle("ME of DAI on Ln(LP)") xtitle("FSTS") ///
    name(fig2_sf, replace)

graph export "$outdir/P3_Figure2_DAI_Margins_SectorFE.png", replace width(2400)

di _n "============================================================"
di    "  REFINE AI RERUNS COMPLETE"
di    "  Compare with baseline: TCI/DAI/moderation should be stable"
di    "============================================================"
