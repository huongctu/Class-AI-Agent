# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 3: CHƯƠNG 5–7 + TÀI LIỆU THAM KHẢO + PHỤ LỤC)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md` và `thesis/15_cd1_part2_findings_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> Tổng hợp Asia context: `thesis/_asia_context_synthesis_2026.md`.
> Hình minh họa: `thesis/figures/` (11 hình; chạy `python3 generate_figures.py`).
> **Phiên bản 2.5–3.1d**: xem commit history.
> **Phiên bản 3.2 (06/05/2026 — Asia context v2 integration)**: 4 substantive enhancements (§5.5 India + §7.1 (5) GVC + §7.3.1 (3)(e) AIPI + §7.3.3 (6) GVC partnership VN).
> **Phiên bản 3.3 (07/05/2026 — Phase 2 NotebookLM Đợt 3 ripple-effects)**: §6 thêm cảnh báo schema BREADY 2025 + Xu (2024) lý giải; §7.3.2 mở rộng anchor model #6 + panel hậu đại dịch #7; §7.3.4 nâng 5 → 8 robustness checks.
> **Phiên bản 3.4 (07/05/2026 — ADB Vietnam Economic Outlook 2026 integration)**: §5.3 Vietnam case study mở rộng với ADB Vietnam Outlook 2026 — GDP 7,2% (2026) / 7,0% (2027) cao hơn ADO April 2026 (7,0%); FDI commitment $2,4 tỷ / 18 dự án chiến lược; năng suất lao động +5,1% 2026-2027; ADB Policy-Based Loans $2,4B target SME nội địa — củng cố two-tier non-convergence framing. Liên kết file 04 v2.5 (commit a3c1769).

---

## CHƯƠNG 5 — BẢY TIỂU CẢNH ĐIỂN HÌNH

### 5.1 Singapore (Advanced đổi mới sáng tạo dẫn dắt — innovation-driven, n=623, đợt 2023)

FSTS 7,1%; doanh nghiệp xuất khẩu 17,8%; website 66,1%; ISO 23,3%; R&D 7,5%; FDI 31,5%. Độ lệch chuẩn log năng suất (sd log) 1,03. **Biên trên (upper boundary)** của nhóm Advanced đổi mới sáng tạo dẫn dắt. Theo bài báo P3 (Singapore — MIR): mô hình M8 cho R² hiệu chỉnh = 0,196; tương tác FSTS² × DAI = 3,119; điểm uốn (turning point) ở mức ~85%.

### 5.2 Saudi Arabia, Qatar và Kuwait (Advanced tài nguyên dẫn dắt — resource-driven, n=1.632, 3 đợt năm 2025)

| Chỉ số | Saudi Arabia | Qatar | Kuwait | Singapore |
|---|---|---|---|---|
| FSTS (%) | 2,7 | 2,3 | **0,4** | 7,1 |
| FDI ≥10% (%) | 9,5 | 19,4 | 0,0 | **31,5** |
| R&D dương (%) | 1,7 | 0,6 | **20,7** | 7,5 |
| sd log năng suất | **0,47** | **0,31** | 1,15 | 1,03 |

Năm phát hiện: (1) **nhà nước tô (rentier state)** — Beblawi (1987); Hertog (2010); Hvidt (2013); (2) **phân bổ sai nguồn lực đảo chiều** so với Hsieh & Klenow (2009); (3) Kuwait Vision 2035 với R&D 20,7%; (4) **thiên lệch của DAI đơn thành phần**; (5) **phân nhóm con (sub-grouping) Advanced** — innovation-driven so với resource-driven là một dạng biến thể chế kiểu Varieties of Capitalism (Hall & Soskice, 2001). **Bối cảnh xung đột Trung Đông 2026**: IMF (2026, April) điều chỉnh giảm tăng trưởng Saudi Arabia mạnh từ ~4,5% xuống 3,1% do giảm sản lượng dầu; ADB (2026, April) — báo cáo *Asian Development Outlook April 2026: The Middle East Conflict Challenges Resilience in Asia and the Pacific* — dự báo Pacific 3,4%, Đông Nam Á 4,7%, Việt Nam 7,0% — củng cố luận điểm về dị biệt Advanced innovation vs resource.

### 5.3 Việt Nam (n=3.077, 3 đợt khảo sát) — cập nhật v3.4 với ADB Vietnam Outlook 2026

FSTS 23,2% → 17,9% → 16,1% (suy giảm); doanh nghiệp xuất khẩu 37,1% → 23,8%; ISO 17–23%; R&D 6,1% (đợt 2023). Pattern **kinh tế hai tầng (two-tier economy)** — doanh nghiệp FDI hướng xuất khẩu hiệu quả cao đan xen với doanh nghiệp nội địa năng suất thấp (CIEM, 2023; Tran & Pham, 2024).

**Cập nhật bối cảnh 2026 — ADB Vietnam Economic Outlook 2026 (mới v3.4)**: Theo ADB (2026, April — *Vietnam Economic Outlook 2026: Navigating the Crosscurrents*), Việt Nam dự phóng GDP **7,2% (2026) / 7,0% (2027)** — vượt mức bình quân ASEAN 4,6% và Đông Nam Á 4,7%, **cao hơn dự báo ADO April 2026 chung (7,0%)** do động lực FDI và xuất khẩu mạnh hơn dự đoán tổng quát. Bốn động lực chính:

(a) **FDI commitment $2,4 tỷ qua 18 dự án chiến lược** — fintech, năng lượng sạch, logistics; tập trung vào CPTPP-compliance và xuyên biên giới (cross-border payments, fintech innovation).

(b) **Năng suất lao động tăng 5,1% giai đoạn 2026-2027** — FDI manufacturing tiến vào "higher-value" stage, chuyển từ assembly downstream sang mid-stream design/R&D. Đây là chứng cứ thực nghiệm cho **giai đoạn chuyển đổi quan trọng** của doanh nghiệp Việt Nam, vượt qua mô hình "factory of the world" sang "designer of the region".

(c) **Hai-tầng kinh tế tiếp tục phân kỳ — không hội tụ**: FDI-sector đóng góp 18% global solution với automation export-oriented; SME nội địa cần fintech và capacity support — ADB Policy-Based Loans **$2,4 tỷ target nhóm này** (cùng FDI commitment $2,4B nhưng đối tượng đối lập). Pattern này **củng cố luận điểm two-tier không hội tụ** trong §7.3.3 (1) hàm ý chính sách CĐ1; tỷ lệ FDI inflow tiếp tục cao nhưng spillover lan truyền tới SME nội địa vẫn hạn chế.

(d) **GVC re-positioning**: từ assembly downstream → mid-stream design/R&D theo 3 trụ cột **"Resilience + Environmental Sustainability + Inclusiveness"** — phù hợp khoảng trống §7.1 (5) ADPR 2026 GVC participation. Lạm phát dự phóng 4,0%; rủi ro chính từ giá dầu Brent + tỷ giá USD/VND.

**Hàm ý cho CĐ2** *(mới v3.4)*: bổ sung **biến `Vietnam_HighValue_FDI_2026`** đo bước chuyển từ assembly → higher-value của FDI manufacturing như test cho **H7 industry × institutional dynamism interaction** (Kafouros et al., 2023) trong context Việt Nam — kỳ vọng tương tác `tech_dynamism_industry × FDI_higher_value` dương và significant ở Việt Nam Manufacturing high-tech subsample (theo Bảng 4.8.1 file 15).

### 5.4 Trung Quốc (n=4.889)

FSTS 10,9% → 8,8%; FDI ≥10% chiếm 6,0%. Quan hệ FSTS – năng suất là hàm bậc ba (cubic) với điểm uốn ~47,8% (Đỗ & Phan, 2026 — JFAR). **Cập nhật v3.1c**: Wang, Huang và Hong (2024 — *IRFA*) phân tích 80% bank risk models ở PRC phụ thuộc dominant tech providers — **concentration risk** trong digital ecosystem PRC.

### 5.5 Tổng hợp Emerging Asia (n=42.278) — bổ sung India case (v3.2)

FSTS 7,6%; FDI ≥10% chiếm 4,4%; tỷ lệ doanh nghiệp R&D dương 16%. Phân tán nội bộ lớn (sd log 2,18) — phản ánh dị biệt rộng xuyên 7 nước Emerging.

**Trường hợp Ấn Độ — chứng cứ technology spillovers (NEW v3.2)**: Theo Sikdar và Mukhopadhyay (2026 — *Asian Development Review, 43*(1), pp.37-75), nghiên cứu panel **4.293 doanh nghiệp Ấn Độ giai đoạn 2006-2019**, áp dụng mô hình TFP với bốn kênh horizontal spillovers (imported intermediate/capital goods, license fee technology purchases, foreign-owned firm presence, skill diffusion qua lao động) và hai kênh vertical spillovers (downstream/upstream FDI, downstream/upstream import inputs). Phát hiện chính:

- **FDI là kênh horizontal spillover quan trọng nhất** ở Ấn Độ
- Doanh nghiệp **lớn và hiệu quả cao** capture spillovers nhiều nhất
- FDI inflows Ấn Độ tăng từ **$1,705M (1990-2000) → $20,077M (2001-2011) → $42,396M (2012-2022)**; chi trả IP tăng tương ứng $138M → $1,195M → $6,530M
- R&D **stagnant ở 0,7% GDP** từ 1996; patent applications resident filing **+11,9%/năm 2012-2022** (vs 0,3% nonresident)

**Hàm ý so sánh**: Pattern Ấn Độ (FDI là kênh chính, large/efficient firms hấp thụ tốt nhất) **đối lập với Việt Nam two-tier kinh tế** — nơi FDI hiệu quả cao nhưng spillover hạn chế cho khối nội địa do absorptive capacity yếu (CIEM, 2023). Khi Ấn Độ FSTS sụt 7,7→2,7% trong đợt 2025 (§4.10), pattern này gợi ý không chỉ là schema effect mà còn phản ánh chuyển hướng Atmanirbhar Bharat (self-reliance) — giảm phụ thuộc nhập khẩu công nghệ. Bằng chứng từ Sikdar & Mukhopadhyay (2026) củng cố **H2 (TCI điều tiết)** trong CĐ2: tác động FSTS → năng suất phụ thuộc vào năng lực hấp thụ (absorptive capacity, Cohen & Levinthal, 1990) và năng lực công nghệ tích lũy (Lall, 1992).

### 5.6 Mongolia — từ lời nguyền tài nguyên đến chuyển đổi critical minerals (n=1.905, 4 đợt 2009–2025)

> **REVAMP v3.1c** (06/05/2026): Tích hợp ADB (2026, May) *Market Assessment of Critical Minerals in Mongolia* + IEA Global Critical Minerals Outlook 2025.

**Số liệu lịch sử lời nguyền tài nguyên (2009-2025)**: FSTS đình trệ 4-6%; FDI ≥10% giảm rõ **7,2% → 3,2%**; tỷ lệ website tăng 39% → 65% (digital leapfrog đơn lẻ). Pattern **lời nguyền tài nguyên** (Auty, 1993; Sachs & Warner, 2001; Gerelmaa & Kotani, 2016).

![Hình 5.6.1 — Mongolia: Evolution 2009–2025 (4 đợt khảo sát WBES)](figures/fig_5_6_mongolia_evolution.png)

*Hình 5.6.1. 4-panel chart: (A) FSTS đình trệ 4-6%; (B) FDI ≥10% giảm 7,2%→3,2%; (C) Website tăng 39%→65%; (D) sd log productivity dispersion 1,33→0,98→1,27→1,20.*

**Bước ngoặt 2026 — chuyển đổi critical minerals (ADB, 2026, May)**: Mongolia ở giao điểm chiến lược của **11 critical minerals** cho energy transition: Cu, C (graphite), Li, Mo, Mn, Co, Fluorspar, Pt, Ni, W, REE. Cu exports **1,69 Mt (2024)** = **3,3 tỷ USD** = **22,1% tổng xuất khẩu**. Trữ lượng 61,4 Mt. Oyu Tolgoi target **500.000 tấn/năm 2028-2036**. Lithium 8-13× by 2050; supply shortfall 2040: 35% Li, 59% Cu. PRC processing dominance: 100% graphite, 90% Mn, 70% Co, 60% Li, 40% Cu. Indonesia precedent nickel ban 2020 → 40% global processing. Korea-Mongolia Mineral Resources Cooperation Center (2023) precedent. **Hàm ý**: Mongolia chuyển đổi resource curse → critical minerals economy. CĐ2 thêm biến `Critical_Minerals_Exposure` cho 4 nước (Mongolia + Indonesia + Vùng Vịnh + Australia).

### 5.7 SIDS Thái Bình Dương (7 nước — cập nhật v3.1, n=1.371)

**Bảy nước**: Fiji (FJI), Papua New Guinea (PNG), Solomon Islands (SLB), Tonga (TON), Vanuatu (VUT), Samoa (WSM), **Kiribati (KIR — bổ sung 2025)**. Tổng n=1.371.

**Số liệu gộp 6 nước cũ**: FSTS 6,3%; FDI ≥10% **23,5%**; đổi mới sản phẩm **41,5%**; website **58,9%**. Pattern **thích nghi trong điều kiện ràng buộc (adaptation under constraint)**.

**Kiribati 2025 — trường hợp biên CỰC ĐOAN nhất**: FSTS 1,03%, FDI 0,7%, website 18,7% (LOW vs Fiji 74,8%), ISO 1,3%, sd log 1,48, SME 93,3%. GDP/đầu người ~1.700 USD, viện trợ AUS/NZ ~30% GDP.

![Hình 5.7.1 — Dị biệt nội bộ SIDS Thái Bình Dương: Kiribati vs Fiji vs Singapore](figures/fig_5_7_sids_comparison.png)

*Hình 5.7.1. 3-way comparison cho 6 chỉ số. Kiribati gần ZERO trên mọi chỉ số kết nối quốc tế. Phát hiện cốt lõi: cần 9 phân nhóm con thay vì 8 trong CĐ2.*

**Phát hiện cốt lõi v3.1**: Dị biệt nội bộ SIDS — "high-digital SIDS" (Fiji, Maldives) vs "isolated SIDS" (Kiribati). ADB (2026, April) Pacific 3,4% năm 2026 — bối cảnh nghiệt ngã cho "isolated SIDS".

### 5.8 So sánh tổng hợp

**Bảng 5.1**. *Ma trận so sánh đa chiều bảy tiểu cảnh điển hình.*

| Chỉ số | Singapore | Việt Nam | Trung Quốc | Em Asia | Mongolia | SIDS Thái Bình Dương¹ | Saudi+Qatar+Kuwait |
|---|---|---|---|---|---|---|---|
| n_firms | 623 | 3.077 | 4.889 | 42.278 | 1.905 | **1.371 (v3.1)** | 1.632 |
| FSTS (%) | 7,1 | 19,1 | 9,9 | 7,6 | **5,0** | 6,3 | **2,4** |
| FDI ≥10% (%) | **31,5** | 11,4 | 6,0 | 4,4 | **4,7** | 23,5 | **11,5** |
| R&D dương (%) | 7,5 | **3,1** | **39,4** | 16 | **20,8** | 11,8 | **3,1** |
| Website (%) | 66,1 | **47,0** | **58,7** | **48,0** | **50,1** | 58,9 | **43,6** |
| sd log năng suất | 1,03 | 1,38 | 1,20 | 2,18 | **1,16** | 1,32 | **0,49** |

*¹SIDS Thái Bình Dương cập nhật v3.1 với Kiribati 2025: tổng n=1.371; sd log 1,32.*

![Hình 5.1 — Định vị 7 tiểu cảnh điển hình trên hệ trục Phân tán (sd log) × FDI ≥10%](figures/fig_5_1_seven_scenes.png)

*Hình 5.1. Scatter bubble chart, kích thước √n_firms.*

---

## CHƯƠNG 6 — CÁC YẾU TỐ GIẢI THÍCH SƠ BỘ

Chương này phân tích tương quan **hai biến (bivariate)** giữa bốn yếu tố giải thích sơ bộ — FDI ≥10%, FSTS, TCI, DAI — và log năng suất lao động, theo từng phân nhóm con thể chế.

**Bảng 6.1**. *Hệ số tương quan Pearson (n=101.185 — v3.1).*

| Yếu tố | Advanced | Upper-middle | Emerging | Frontier | SIDS |
|---|---|---|---|---|---|
| FDI ≥10% | −0,113 | −0,023 | +0,113 | +0,068 | **+0,222** |
| FSTS | **+0,113** | −0,086 | +0,062 | +0,014 | −0,050 |
| TCI (R&D + ISO) | **+0,128** | +0,016 | −0,029 | +0,019 | **+0,155** |
| DAI (website) | **−0,129** | +0,012 | +0,016 | +0,070 | −0,049 |

**Sáu phát hiện chính**:

**(1)** FDI ≥10% dương rất mạnh ở SIDS (+0,222) — kênh truyền tải năng suất chính.

**(2)** FDI ≥10% âm ở Advanced (−0,113) — FDI tài chính/dầu khí năng suất tự thân thấp.

**(3)** FSTS dương ở Advanced (+0,113) — phù hợp Uppsala (Johanson & Vahlne, 1977) + OLI (Dunning, 1988); cơ sở H1.

**(4)** TCI dương mạnh ở SIDS (+0,155) + Advanced (+0,128) — TCI then chốt ở **hai cực** phổ phát triển. Học hỏi tự thân vs FDI-induced learning (Cohen & Levinthal, 1990; Lall, 1992).

**(5)** DAI âm Advanced (−0,129) — Tier-1 Digital Presence saturation; ICT artifact; digital theatre (Verhoef et al., 2021). Cần multi-component DAI ở CĐ2.

**(6)** Đảo dấu xuyên phân nhóm con — bằng chứng cho **điều tiết thể chế (institutional moderation)**. Cơ sở H4.

**Cảnh báo schema BREADY 2025 (mới v3.3 — Phase 2 NotebookLM HĐ3)**: Đợt 2025 (n=16.979, 16,8% pool) sử dụng schema mới gây thay đổi đo lường tại nhiều nước (đặc biệt IND FSTS 7,7%→2,7%, R&D nhiều nước tăng vọt do hiệu ứng bảng hỏi). Vì vậy bảng 6.1 trên có thể bị nhiễu schema effect — **cần kiểm chứng qua hệ thống "triple-defense" §4.11 file 15**: (a) biến giả `Post_BREADY_2024`; (b) anchor model so sánh hệ số 2009-2024 vs 2009-2025; (c) tách 2025 thành panel hậu đại dịch độc lập. Đặc biệt với DAI âm Advanced (-0,129): kết hợp với ICT exclusion test §4.4.5 và Tier-1 saturation framing để minh bạch hóa artifact.

**Lý giải dị biệt cross-regime qua Xu (2024) de jure-de facto** *(mới v3.3)*: Đảo dấu giữa nhóm Emerging (FDI +0,113) và Advanced (FDI −0,113) một phần phản ánh **gap de jure–de facto enforcement**: ở Emerging (Việt Nam, Indonesia, Trung Quốc, Mongolia — trạng thái B của Bảng 2.6.1 file 14), thể chế formal có nhưng thực thi yếu, nên FDI capture được "premium" từ partnership identification (Kafouros et al. 2023 mechanism #1) chưa bão hòa. Ngược lại, ở Advanced (Singapore, Korea — trạng thái A), formal-de facto đã align, nên FDI thuần tài chính/dầu khí (Vùng Vịnh) không add productivity premium qua kênh thể chế.

---

## CHƯƠNG 7 — KHOẢNG TRỐNG THỰC TIỄN VÀ KẾT LUẬN

### 7.1 Khoảng trống nghiên cứu thực tiễn (mở rộng v3.2 từ 4 lên **5 khoảng trống**)

**(1) Hài hòa khung dữ liệu xuyên thế hệ WBES 2009–2025**. Pipeline tái lập được cho 4 thế hệ (PICS3, Standardized, BEE, BREADY) — thực hành mở (Page et al., 2021).

**(2) Phân nhóm con Advanced + boundary case Mongolia**. (a) Advanced sub-grouping innovation/resource — VoC + REE (Hall & Soskice, 2001; Hertog, 2010); (b) Mongolia chuyển đổi sang critical minerals economy 2026 (ADB, 2026, May).

**(3) Mô hình phi tuyến và điều tiết đa tầng** (Bausch & Krist, 2007; Marano et al., 2016). Đỗ & Phan (2026 — VEFR, JFAR) chỉ ra điểm uốn khác nhau; CĐ1 mở rộng lên 47 nước.

**(4) Trường hợp biên SIDS Thái Bình Dương** — 7 nước với Kiribati 2025. Đỗ & Phan (2026 — bản thảo P8) áp dụng forced internationalization penalty (Briguglio, 1995; Bertram, 2006).

**(5) Khung GVC participation và inclusive development cho 47 nước (NEW v3.2)** — Theo *Asian Development Policy Report 2026 — Global Value Chains and Inclusive Development* (ADB, 2026, May): Asia/Pacific chiếm ~1/3 GVC trade global; **GVC share Developing Asia tăng 9% → 18% giai đoạn 2000-2023** (gấp đôi). Bằng chứng định lượng macro: 10% increase trong GVC participation → +0,45% per capita income growth; 10% improvement in GVC centrality → +0,8% per capita income growth. Successfully upgraded economies grew 6%/năm (2000-2023) vs 3,9% peripheral. **Tuy nhiên**: small firms 25% less likely to participate in GVCs; within-economy Gini ↑6,7pp — nguy cơ dị biệt nội bộ.

Khoảng trống cho CĐ1: chưa có nghiên cứu firm-level WBES kết hợp với GVC participation cho 47 nước châu Á + Thái Bình Dương. Bằng chứng CĐ1 về **kinh tế hai tầng Việt Nam** (§5.3) và **dị biệt Em Asia** (§5.5) phù hợp với pattern ADPR 2026 — small firms khó tham gia GVC. CĐ2 nên có biến `GVC_participation_rate` (theo OECD TiVA hoặc ADB MRIO) ở cấp ngành × quốc gia × năm.

### 7.2 Kết luận chính

**(i)** Pool 101.185 doanh nghiệp · 47 nước · 108 cặp QG×năm — phạm vi rộng nhất.

**(ii)** Phân tán: Advanced (0,86) < Emerging (1,24) ≈ SIDS (1,32) < Frontier (1,36).

**(iii)** Bảy tiểu cảnh + 7 SIDS đa diện cùng tồn tại — không có hội tụ.

**(iv)** Dị biệt nội bộ Advanced (Singapore/Vùng Vịnh ≈ 2,1×).

**(v)** SIDS pattern thích nghi/leapfrog ở 6 nước cũ; Kiribati 2025 CỰC ĐOAN nhất.

**(vi)** FDI ≥10% dương mạnh SIDS (+0,222) — kênh năng suất chính.

**(vii)** Mongolia chuyển đổi sang critical minerals economy 2026.

**(viii)** Bằng chứng đảo dấu — phi tuyến + điều tiết đa tầng. Cơ sở H1-H6; **CĐ2 mở rộng 9 phân nhóm con**.

### 7.3 Hàm ý cho luận án và Chuyên đề 2

#### 7.3.1 Hàm ý lý thuyết

(Giữ nguyên từ v3.3 — 5 evidence; AIPI; digital theatre warning. Xem commit cc33ed4.)

#### 7.3.2 Hàm ý phương pháp luận (mở rộng v3.3 — bổ sung anchor model + panel hậu đại dịch)

(Giữ nguyên từ v3.3 — 5 hàm ý + triple-defense system. Xem commit cc33ed4.)

#### 7.3.3 Hàm ý chính sách cho doanh nghiệp Việt Nam và khu vực (mở rộng v3.2 từ 5 lên **6 hàm ý**)

(Giữ nguyên từ v3.2 — 6 hàm ý chính sách + 4 đề xuất GVC cho Việt Nam. Xem commit 7738953.)

#### 7.3.4 Hàm ý cho Chuyên đề 2 và luận án

(Giữ nguyên từ v3.3 — 8 robustness checks. Xem commit cc33ed4.)

### 7.4 Hạn chế của chuyên đề

(Giữ nguyên từ v3.2 — 7 hạn chế. Xem commit 7738953.)

### 7.5 Kế hoạch hoàn thiện

(Giữ nguyên từ v3.1a — 4 giai đoạn 6/2026 → 9/2026.)

---

## TÀI LIỆU THAM KHẢO

> Trích dẫn theo APA 7th. Danh mục đầy đủ ở `thesis/04_references_apa7.md` (v2.5 cập nhật với 4 references mới Vietnam Outlook 2026 + IFC + WB Vietnamese WBES sources).

**Cited references mới ở v3.4** (chi tiết APA full format trong `04_references_apa7.md` v2.5):

- **Asian Development Bank**. (2026, April). *Vietnam Economic Outlook 2026: Navigating the Crosscurrents*. ADB. (cited §5.3 — Vietnam case study v3.4)

---

## PHỤ LỤC

### Phụ lục A — Phạm vi thực tế của nhóm dữ liệu WBES

47 nước, 108 cặp QG×năm, 101.185 doanh nghiệp, 7 SIDS bao gồm Kiribati 2025.

### Phụ lục B – G

(Sẽ mở rộng giai đoạn 1–3 tháng 6–8/2026.)

---

*Phiên bản 3.0 (06/05/2026) — Biên tập tiếng Việt hoàn thiện.*
*Phiên bản 3.1c (06/05/2026) — §5.6 Mongolia REVAMP critical minerals.*
*Phiên bản 3.1d (06/05/2026) — 3 markdown image refs (5.6.1, 5.7.1, 5.1).*
*Phiên bản 3.2 (06/05/2026) — Asia context v2 integration: §5.5 India case + §7.1 (5) GVC + §7.3.1 (3)(e) AIPI + §7.3.3 (6) GVC partnership VN.*

*Phiên bản 3.3 (07/05/2026 — Phase 2 NotebookLM Đợt 3 ripple-effects) — §6 cảnh báo schema BREADY 2025 + Xu (2024) lý giải; §7.3.2 anchor model #6 + panel hậu đại dịch #7; §7.3.4 nâng 5 → 8 robustness checks.*

*Phiên bản 3.4 (07/05/2026 — ADB Vietnam Outlook 2026 integration) — §5.3 Vietnam case study mở rộng với 4 động lực 2026: (a) FDI commitment $2,4B / 18 dự án; (b) năng suất +5,1%; (c) two-tier không hội tụ + ADB Policy-Based Loans $2,4B target SME; (d) GVC re-positioning từ assembly → mid-stream design/R&D theo 3 trụ cột Resilience + Environmental Sustainability + Inclusiveness. Hàm ý CĐ2: bổ sung biến Vietnam_HighValue_FDI_2026 test H7 industry × institutional dynamism. Liên kết file 04 v2.5 (commit a3c1769).*

> **Sections §7.3.1, §7.3.2, §7.3.3, §7.3.4, §7.4 v3.4**: Giữ nguyên từ v3.3 (commit cc33ed4) và v3.2 (commit 7738953) để giảm size file v3.4 — full content vẫn truy cập qua git history.