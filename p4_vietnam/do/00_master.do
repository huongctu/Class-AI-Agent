*! 00_master.do — P4 Vietnam: master orchestrator
*! Drives the full P4 rerun pipeline end-to-end. Set $root once below; every
*! downstream do-file resolves all paths from the globals defined here so no
*! manual edits should be needed inside the per-step scripts.
*!
*! Expected raw inputs in $raw:
*!   vietnam_2009.dta   (WBES Vietnam 2009 full release)
*!   vietnam_2015.dta   (WBES Vietnam 2015 full release)
*!   vietnam_2023.dta   (WBES Vietnam 2023 full release)
*! Drop the World Bank releases here unrenamed, then this master script
*! applies a thin rename layer at build time (01–03_build_*.do).

clear all
set more off
set varabbrev off
version 17

* ---------------------------------------------------------------------------
* Edit only this line to point at your local working copy of the project.
* All other paths are derived.
* ---------------------------------------------------------------------------
global root  "`c(pwd)'"

global do      "$root/do"
global raw     "$root/raw"
global work    "$root/work"
global out     "$root/output"
global tables  "$out/tables"
global figs    "$out/figures"
global logs    "$out/logs"

cap mkdir "$work"
cap mkdir "$out"
cap mkdir "$tables"
cap mkdir "$figs"
cap mkdir "$logs"

* ---------------------------------------------------------------------------
* Required user-written commands. Install once on a fresh machine.
* ---------------------------------------------------------------------------
foreach pkg in estout utest parmest ftools reghdfe {
    cap which `pkg'
    if _rc ssc install `pkg', replace
}

cap log close _all
log using "$logs/00_master.log", replace text

di as txt "==> P4 Vietnam pipeline starting at $S_DATE $S_TIME"
di as txt "    root  = $root"

do "$do/01_build_2009.do"
do "$do/02_build_2015.do"
do "$do/03_build_2023.do"
do "$do/04_append_pooled.do"
do "$do/05_main_models.do"
do "$do/06_lind_mehlum.do"
do "$do/07_selection_checks.do"
do "$do/08_crosswave_tests.do"
do "$do/09_robustness.do"
do "$do/10_export_tables_figures.do"

di as txt "==> P4 Vietnam pipeline finished at $S_DATE $S_TIME"
log close
