"""
wbes/00_config.py
=================
47-country WBES catalogue for thesis: "Internationalization & Firm Performance
Across Institutional Regimes" (Đỗ Thùy Hương, 2026).

Each entry in COUNTRY_WAVES lists the WBES survey rounds available per economy.
Waves are identified by the integer survey year that appears in the .dta filename.

WBES filename convention (World Bank Microdata portal):
  <ISO3>_<year>_wbes.dta          e.g. VNM_2015_wbes.dta
  <ISO3>_<year>_Enterprise-Survey.dta

Place all raw .dta files under:  raw/<ISO3>/

ICRV regime assignment follows thesis §3.3.6.
"""

# ------------------------------------------------------------------
# 47-economy catalogue  (ISO-3 → list of survey years available)
# ------------------------------------------------------------------
COUNTRY_WAVES: dict[str, list[int]] = {
    # ── R1  Advanced Innovation-driven ────────────────────────────
    "SGP": [2015, 2023],
    "HKG": [2018],
    "KOR": [2016],
    "TWN": [],                      # Taiwan not in standard WBES
    "ISR": [2024],
    "CYP": [2019],

    # ── R1' Advanced Resource-driven ──────────────────────────────
    "SAU": [2013],
    "QAT": [2019],
    "KWT": [2019],
    "BHR": [2019],
    "BRN": [2015],

    # ── R2  Upper-Middle ───────────────────────────────────────────
    "CHN": [2012, 2024],
    "MYS": [2015],
    "THA": [2016],
    "KAZ": [2019],
    "ARM": [2020],
    "GEO": [2020],

    # ── R3  Emerging ──────────────────────────────────────────────
    "IND": [2014, 2022],
    "IDN": [2015],
    "PHL": [2015],
    "VNM": [2009, 2015, 2023],
    "LKA": [2011],
    "JOR": [2019],
    "MNG": [2019],

    # ── R4  Frontier ──────────────────────────────────────────────
    "BGD": [2013, 2022],
    "PAK": [2013],
    "LAO": [2016],
    "KHM": [2016],
    "MMR": [2016],
    "NPL": [2013],
    "BTN": [2015],
    "MDV": [2019],
    "UZB": [2019],
    "TJK": [2019],
    "KGZ": [2019],
    "TKM": [],                      # Turkmenistan: no public WBES
    "AFG": [2014],
    "TLS": [2015],
    "IRQ": [2011],
    "LBN": [2019],
    "YEM": [2013],

    # ── R5  SIDS / Pacific ─────────────────────────────────────────
    "FJI": [2019],
    "PNG": [2015],
    "SLB": [2015],
    "TON": [2015],
    "VUT": [2019],
    "WSM": [2019],
}

ICRV: dict[str, str] = {
    # R1
    "SGP": "R1_Adv_Innovation", "HKG": "R1_Adv_Innovation",
    "KOR": "R1_Adv_Innovation", "TWN": "R1_Adv_Innovation",
    "ISR": "R1_Adv_Innovation", "CYP": "R1_Adv_Innovation",
    # R1'
    "SAU": "R1p_Adv_Resource", "QAT": "R1p_Adv_Resource",
    "KWT": "R1p_Adv_Resource", "BHR": "R1p_Adv_Resource",
    "BRN": "R1p_Adv_Resource",
    # R2
    "CHN": "R2_Upper_Middle", "MYS": "R2_Upper_Middle",
    "THA": "R2_Upper_Middle", "KAZ": "R2_Upper_Middle",
    "ARM": "R2_Upper_Middle", "GEO": "R2_Upper_Middle",
    # R3
    "IND": "R3_Emerging", "IDN": "R3_Emerging", "PHL": "R3_Emerging",
    "VNM": "R3_Emerging", "LKA": "R3_Emerging", "JOR": "R3_Emerging",
    "MNG": "R3_Emerging",
    # R4
    "BGD": "R4_Frontier", "PAK": "R4_Frontier", "LAO": "R4_Frontier",
    "KHM": "R4_Frontier", "MMR": "R4_Frontier", "NPL": "R4_Frontier",
    "BTN": "R4_Frontier", "MDV": "R4_Frontier", "UZB": "R4_Frontier",
    "TJK": "R4_Frontier", "KGZ": "R4_Frontier", "TKM": "R4_Frontier",
    "AFG": "R4_Frontier", "TLS": "R4_Frontier", "IRQ": "R4_Frontier",
    "LBN": "R4_Frontier", "YEM": "R4_Frontier",
    # R5
    "FJI": "R5_SIDS", "PNG": "R5_SIDS", "SLB": "R5_SIDS",
    "TON": "R5_SIDS", "VUT": "R5_SIDS", "WSM": "R5_SIDS",
}

# ------------------------------------------------------------------
# WBES raw variable → harmonised name  (with wave-year overrides)
# ------------------------------------------------------------------
# Primary mapping (most waves 2009-2024)
VAR_MAP_PRIMARY: dict[str, str] = {
    # Identity
    "idstd":   "firm_id",

    # Performance
    "d2":      "total_sales_raw",      # total sales last FY (local currency)
    "d2b":     "total_sales_raw",      # alt in some waves
    "l1":      "employees",            # full-time perm employees
    "l6":      "employees",            # alt in some waves

    # Internationalisation (FSTS)
    "a14b":    "export_pct",           # exports % of sales
    "a14":     "export_pct",           # alt name

    # Technology / TCI
    "b8":      "quality_cert",         # ISO/int'l quality cert (0/1)
    "e6":      "foreign_tech",         # tech licensed from foreign firm (0/1)
    "h7":      "foreign_tech",         # alt name some waves

    # Digital / DAI
    "c22b":    "website",              # uses email/website (0/1)
    "c22":     "website",              # alt

    # Innovation
    "h1":      "product_innov",        # new product last 3yr
    "h3":      "process_innov",        # new process last 3yr
    "h2":      "rd_spending",          # has R&D expenditure (0/1)

    # Ownership / FDI
    "b2b":     "foreign_own",          # % shares foreign-owned

    # E-payments
    "j7a":     "epayment_pct",         # % payments received electronically
    "j7b":     "epay_supp_pct",        # % payments to suppliers electronic

    # Firm characteristics
    "b5":      "yr_established",       # year firm established
    "b7":      "manager_exp",          # years manager experience

    # Sector / location
    "a3b":     "sector_isic4",         # primary activity ISIC4
    "a3b_2d":  "sector_isic4",
    "d1b2":    "sector_isic4",
    "a2":      "region_code",
}

# Wave-specific overrides (year → {raw_var: harmonised_name})
VAR_MAP_OVERRIDES: dict[int, dict[str, str]] = {
    2009: {"h7": "foreign_tech", "c22b": "website"},
    2012: {"l6": "employees", "d2b": "total_sales_raw"},
    2013: {},
    2014: {},
    2015: {},
    2016: {"h3a": "product_innov"},
    2018: {},
    2019: {"h1a": "product_innov", "c22a": "website"},
    2020: {},
    2022: {},
    2023: {"l1b": "employees"},
    2024: {},
}

# ISIC 2-digit → broad sector
SECTOR_LABELS: dict[int, str] = {
    10: "Food", 11: "Beverages", 13: "Textiles", 14: "Apparel",
    15: "Leather", 16: "Wood", 17: "Paper", 18: "Printing",
    19: "Coke/Petroleum", 20: "Chemicals", 21: "Pharma",
    22: "Rubber/Plastic", 23: "NonMetal", 24: "BasicMetal",
    25: "FabricatedMetal", 26: "Electronics", 27: "ElectricEq",
    28: "Machinery", 29: "MotorVehicle", 30: "OtherTransport",
    31: "Furniture", 32: "OtherMfg", 33: "Repair",
    45: "Retail/Wholesale", 46: "Retail/Wholesale", 47: "Retail/Wholesale",
    49: "Transport", 50: "Transport", 51: "Transport", 52: "Transport",
    55: "Hotels", 56: "Food/Bev_service",
    62: "ICT", 63: "ICT", 64: "Finance", 65: "Finance",
    68: "RealEstate", 69: "ProfServices", 70: "ProfServices",
    72: "R&D", 78: "AdminServices",
}
