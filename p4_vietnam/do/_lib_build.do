*! _lib_build.do — wave-build helper macros
*! Sourced by 01–03_build_*.do so that the three wave scripts stay short and
*! the missing-code / composite logic lives in exactly one place.

cap program drop p4_clean_missing
program define p4_clean_missing
    * WBES codes "don't know" / "refused" as -9. Listwise treats them as missing.
    foreach v of varlist `0' {
        cap confirm numeric variable `v'
        if !_rc replace `v' = . if `v' == -9
    }
end

cap program drop p4_recode01
program define p4_recode01
    * WBES binary items use 1 = yes, 2 = no. Recode to 1/0.
    syntax varlist
    foreach v of local varlist {
        cap drop `v'_r
        recode `v' (1=1) (2=0) (else=.), gen(`v'_r)
    }
end

cap program drop p4_zwithin
program define p4_zwithin
    * z-standardise within the current sample (which is wave at build time).
    syntax varname, gen(name)
    qui sum `varlist'
    gen `gen' = (`varlist' - r(mean)) / r(sd)
end
