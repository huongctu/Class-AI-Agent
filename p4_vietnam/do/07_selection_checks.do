*! 07_selection_checks.do — Heckman two-step + control-function probe
*! Selection equation: probit on export_any with sampling region a2 as the
*! exclusion restriction (manuscript identification argument: a2 affects the
*! export selection probability through logistical access but not the
*! productivity outcome conditional on observable controls).
*! Two complementary corrections:
*!   (a) Two-step Heckman: estimate IMR (lambda) from selection probit and
*!       enter it in the outcome equation, retest focal coefficients.
*!   (b) Control function: enter the generalised residual from the selection
*!       probit instead of the IMR.
*! Output: tables/selection_checks.csv

clear all
use "$work/vnm_pooled_clean.dta", clear

* Per the manuscript Heckman is run by wave and pooled. We also restrict the
* outcome sample to exporters (FSTS > 0) before adding lambda, matching the
* standard Heckman two-step interpretation.
global base_controls   "c.lnEmp c.FirmAge i.ForeignOwned i.sector1"
global pooled_controls "c.lnEmp c.FirmAge i.ForeignOwned i.sector1 i.wave"

tempname rh
tempfile sel
postfile `rh' str12 sample str12 method str20 term double(b se p) int nobs ///
    using `sel', replace

cap program drop p4_save_imr
program define p4_save_imr
    syntax , sample(string) method(string) terms(string)
    foreach t of local terms {
        cap scalar drop _b _se _p
        cap scalar _b  = _b[`t']
        cap scalar _se = _se[`t']
        if !_rc {
            scalar _t  = _b / _se
            scalar _p  = 2 * ttail(e(df_r), abs(_t))
            post `0' ("`sample'") ("`method'") ("`t'") (_b) (_se) (_p) (e(N))
        }
    }
end

cap program drop p4_selection_one
program define p4_selection_one
    syntax , sample(string) ifclause(string) controls(string) post(string)

    * (a) Heckman two-step manual ----------------------------------------------
    qui probit export_any `controls' i.a2 `ifclause'
    qui predict double xb_sel `ifclause', xb
    qui gen double imr = normalden(xb_sel) / normal(xb_sel) `ifclause'

    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z imr `controls' ///
        `ifclause' & FSTS > 0, vce(robust)
    p4_save_imr `post', sample("`sample'") method("Heckman2step") ///
        terms("FSTSc FSTSc2 TCI_z DAI_z imr")

    * (b) Control-function: generalised residual instead of IMR ---------------
    cap drop gres
    qui gen double gres = export_any * (normalden(xb_sel) / normal(xb_sel)) ///
                          - (1 - export_any) * (normalden(xb_sel) / normal(-xb_sel)) ///
                          `ifclause'

    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z gres `controls' ///
        `ifclause', vce(robust)
    p4_save_imr `post', sample("`sample'") method("ControlFunction") ///
        terms("FSTSc FSTSc2 TCI_z DAI_z gres")

    cap drop xb_sel imr gres
end

levelsof wave, local(waves)
foreach w of local waves {
    p4_selection_one, sample("VNM`w'") ifclause("if wave==`w'") ///
        controls("$base_controls") post("`rh'")
}
p4_selection_one, sample("VNMpooled") ifclause("") ///
    controls("$pooled_controls") post("`rh'")

postclose `rh'

preserve
use `sel', clear
export delimited using "$tables/selection_checks.csv", replace
restore

di as txt "[07] selection_checks.csv written"
