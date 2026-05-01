*! 05_main_models.do — M0–M8 by wave + pooled
*! Stores estimates as VNM`wave'_M`k' for wave-specific and VNMpooled_M`k' for
*! pooled. Joint F-tests for H2 (TCI moderation) and P1 (DAI moderation) are
*! captured into r-class scalars and dumped to long-format CSVs that the table
*! exporter consumes in step 10.

clear all
use "$work/vnm_pooled_clean.dta", clear

global base_controls   "c.lnEmp c.FirmAge i.ForeignOwned i.sector1"
global pooled_controls "c.lnEmp c.FirmAge i.ForeignOwned i.sector1 i.wave"

tempfile coefs jointF
postfile pcoef str12 sample str4 model str40 term double(b se p ci_lo ci_hi) ///
    int nobs double r2 using `coefs', replace
postfile pjoint str12 sample str4 model str8 test double(F p) ///
    using `jointF', replace

cap program drop p4_save_eb
program define p4_save_eb
    syntax , sample(string) model(string)
    qui matrix b = e(b)
    qui matrix V = e(V)
    local k = colsof(b)
    local terms : colnames b
    forval i = 1/`k' {
        local term : word `i' of `terms'
        if "`term'" == "_cons" continue
        scalar _b  = b[1, `i']
        scalar _se = sqrt(V[`i', `i'])
        scalar _t  = _b / _se
        scalar _p  = 2 * ttail(e(df_r), abs(_t))
        scalar _lo = _b - 1.96 * _se
        scalar _hi = _b + 1.96 * _se
        post pcoef ("`sample'") ("`model'") ("`term'") ///
            (_b) (_se) (_p) (_lo) (_hi) (e(N)) (e(r2))
    }
end

cap program drop p4_save_joint
program define p4_save_joint
    syntax , sample(string) model(string) test(string)
    post pjoint ("`sample'") ("`model'") ("`test'") (r(F)) (r(p))
end

* ============================================================================
* A. WAVE-SPECIFIC MODELS
* ============================================================================
levelsof wave, local(waves)
foreach w of local waves {
    di as txt "==> wave `w'"

    qui regress lnLP $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M0")

    qui regress lnLP c.FSTSc $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M1")

    qui regress lnLP c.FSTSc c.FSTSc2 $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M2")

    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z ///
        c.FSTSc#c.TCI_z c.FSTSc2#c.TCI_z $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M3")
    qui test c.FSTSc#c.TCI_z c.FSTSc2#c.TCI_z
    p4_save_joint, sample("VNM`w'") model("M3") test("H2")

    qui regress lnLP c.FSTSc c.FSTSc2 c.DAI_z ///
        c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M4")
    qui test c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z
    p4_save_joint, sample("VNM`w'") model("M4") test("P1")

    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M5")

    qui regress lnLP c.FSTSc c.FSTSc2 c.DAI_z $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M6")

    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z ///
        $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M7")

    qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z ///
        c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z $base_controls if wave==`w', vce(robust)
    p4_save_eb, sample("VNM`w'") model("M8")
    qui test c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z
    p4_save_joint, sample("VNM`w'") model("M8") test("P1")
}

* ============================================================================
* B. POOLED MODELS
* ============================================================================
di as txt "==> pooled"

qui regress lnLP $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M0")

qui regress lnLP c.FSTSc $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M1")

qui regress lnLP c.FSTSc c.FSTSc2 $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M2")

qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z ///
    c.FSTSc#c.TCI_z c.FSTSc2#c.TCI_z $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M3")
qui test c.FSTSc#c.TCI_z c.FSTSc2#c.TCI_z
p4_save_joint, sample("VNMpooled") model("M3") test("H2")

qui regress lnLP c.FSTSc c.FSTSc2 c.DAI_z ///
    c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M4")
qui test c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z
p4_save_joint, sample("VNMpooled") model("M4") test("P1")

qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M5")

qui regress lnLP c.FSTSc c.FSTSc2 c.DAI_z $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M6")

qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M7")

qui regress lnLP c.FSTSc c.FSTSc2 c.TCI_z c.DAI_z ///
    c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z $pooled_controls, vce(robust)
p4_save_eb, sample("VNMpooled") model("M8")
qui test c.FSTSc#c.DAI_z c.FSTSc2#c.DAI_z
p4_save_joint, sample("VNMpooled") model("M8") test("P1")

postclose pcoef
postclose pjoint

preserve
use `coefs', clear
export delimited using "$tables/coefs_main_models.csv", replace
restore
preserve
use `jointF', clear
export delimited using "$tables/joint_tests_main_models.csv", replace
restore

di as txt "[05] coefs_main_models.csv and joint_tests_main_models.csv written"
