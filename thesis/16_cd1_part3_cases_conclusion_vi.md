# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 3: CHƯƠNG 5–7 + TÀI LIỆU THAM KHẢO + PHỤ LỤC)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md` và `thesis/15_cd1_part2_findings_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> Tổng hợp Asia context: `thesis/_asia_context_synthesis_2026.md`.
> Hình minh họa: `thesis/figures/` (11 hình; chạy `python3 generate_figures.py`).
> **Phiên bản 2.5–3.1d**: xem commit history.
> **Phiên bản 3.2 (06/05/2026 — Asia context v2 integration)**: 4 substantive enhancements.
> **Phiên bản 3.3 (07/05/2026 — Phase 2 NotebookLM Đợt 3 ripple-effects)**: §6 cảnh báo schema; §7.3.2 anchor model; §7.3.4 8 robustness checks.
> **Phiên bản 3.4 (07/05/2026 — ADB Vietnam Outlook 2026 integration)**: §5.3 4 động lực 2026.
> **Phiên bản 3.5a (07/05/2026 — Phase 4 Đợt 3 sub-commit 3A)**: §5.7.5 PICs macro context (4 trụ cột MIRAB).
> **Phiên bản 3.5b (07/05/2026 — Phase 4 Đợt 3 sub-commit 3B)**: §6.1 Gender + §6.2 Innovation U-curve digital.
> **Phiên bản 3.5c (07/05/2026 cuối phiên — Phase 4 Đợt 3 sub-commit 3C)**: §7.3.3 mở rộng từ 6 → 8 hàm ý — (7) **Migration labor partnership Pacific** cho Việt Nam dựa trên mô hình PLMS Australia + RSE New Zealand; (8) **NEW Chính sách số hóa Asia** cho SME Việt Nam — học từ Singapore/Korea AI full-stack, Japan 60% DN dùng AI back-office, Trung Quốc smart manufacturing, model thanh toán digital + social commerce. **Hoàn thành Đợt 3 Phase 4.**

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

**Cập nhật bối cảnh 2026 — ADB Vietnam Economic Outlook 2026 (mới v3.4)**: Theo ADB (2026, April — *Vietnam Economic Outlook 2026: Navigating the Crosscurrents*), Việt Nam dự phóng GDP **7,2% (2026) / 7,0% (2027)** — vượt mức bình quân ASEAN 4,6% và Đông Nam Á 4,7%. Bốn động lực chính: (a) FDI commitment $2,4 tỷ qua 18 dự án chiến lược; (b) Năng suất lao động tăng 5,1% giai đoạn 2026-2027; (c) Hai-tầng kinh tế tiếp tục phân kỳ + ADB Policy-Based Loans $2,4B target SME nội địa; (d) GVC re-positioning từ assembly downstream → mid-stream design/R&D theo 3 trụ cột "Resilience + Environmental Sustainability + Inclusiveness".

**Hàm ý cho CĐ2** *(mới v3.4)*: bổ sung **biến `Vietnam_HighValue_FDI_2026`** đo bước chuyển từ assembly → higher-value của FDI manufacturing như test cho **H7 industry × institutional dynamism interaction** (Kafouros et al., 2023).

### 5.4 Trung Quốc (n=4.889)

FSTS 10,9% → 8,8%; FDI ≥10% chiếm 6,0%. Quan hệ FSTS – năng suất là hàm bậc ba (cubic) với điểm uốn ~47,8% (Đỗ & Phan, 2026 — JFAR). **Cập nhật v3.1c**: Wang, Huang và Hong (2024 — *IRFA*) phân tích 80% bank risk models ở PRC phụ thuộc dominant tech providers — **concentration risk** trong digital ecosystem PRC.

### 5.5 Tổng hợp Emerging Asia (n=42.278) — bổ sung India case (v3.2)

FSTS 7,6%; FDI ≥10% chiếm 4,4%; tỷ lệ doanh nghiệp R&D dương 16%. Phân tán nội bộ lớn (sd log 2,18) — phản ánh dị biệt rộng xuyên 7 nước Emerging.

**Trường hợp Ấn Độ — chứng cứ technology spillovers (NEW v3.2)**: Theo Sikdar và Mukhopadhyay (2026 — *Asian Development Review, 43*(1), pp.37-75), nghiên cứu panel **4.293 doanh nghiệp Ấn Độ giai đoạn 2006-2019**. Phát hiện: FDI là kênh horizontal spillover quan trọng nhất; doanh nghiệp lớn và hiệu quả cao capture spillovers nhiều nhất; FDI inflows tăng từ $1,705M (1990-2000) → $42,396M (2012-2022); R&D stagnant ở 0,7% GDP; patent applications resident filing +11,9%/năm 2012-2022.

### 5.6 Mongolia — từ lời nguyền tài nguyên đến chuyển đổi critical minerals (n=1.905, 4 đợt 2009–2025)

FSTS đình trệ 4-6%; FDI ≥10% giảm rõ **7,2% → 3,2%**; tỷ lệ website tăng 39% → 65%. Pattern **lời nguyền tài nguyên** (Auty, 1993; Sachs & Warner, 2001).

**Bước ngoặt 2026 — chuyển đổi critical minerals (ADB, 2026, May)**: Mongolia ở giao điểm chiến lược của **11 critical minerals** (Cu, Li, Mo, Mn, Co, Ni, W, REE, etc.). Cu exports 1,69 Mt (2024) = 22,1% tổng xuất khẩu. Oyu Tolgoi target 500.000 tấn/năm 2028-2036. PRC processing dominance: 100% graphite, 90% Mn, 70% Co. CĐ2 thêm biến `Critical_Minerals_Exposure`.

![Hình 5.6.1 — Mongolia: Evolution 2009–2025 (4 đợt khảo sát WBES)](figures/fig_5_6_mongolia_evolution.png)

### 5.7 SIDS Thái Bình Dương (7 nước — cập nhật v3.1, n=1.371)

**Bảy nước**: Fiji (FJI), Papua New Guinea (PNG), Solomon Islands (SLB), Tonga (TON), Vanuatu (VUT), Samoa (WSM), **Kiribati (KIR — bổ sung 2025)**. Tổng n=1.371. FSTS 6,3%; FDI ≥10% **23,5%**; đổi mới sản phẩm **41,5%**; website **58,9%**. Pattern **thích nghi trong điều kiện ràng buộc (adaptation under constraint)**.

**Kiribati 2025 — trường hợp biên CỰC ĐOAN nhất**: FSTS 1,03%, FDI 0,7%, website 18,7%, ISO 1,3%, sd log 1,48, SME 93,3%. GDP/đầu người ~1.700 USD, viện trợ AUS/NZ ~30% GDP.

#### 5.7.5 Bối cảnh kinh tế vĩ mô PICs Pacific *(mới v3.5a)*

PICs có 4 trụ cột MIRAB (Bertram, 2006): (1) khu vực công chủ đạo (30-50% việc làm chính thức); (2) phụ thuộc 4 nguồn ngoại sinh — nông nghiệp tự cấp + ODA 30% GDP + remittances 25-40% GDP + khai thác tài nguyên; (3) thanh niên thất nghiệp 15-30% + dân số <25 tuổi >50%; (4) migration labor PLMS Australia + RSE New Zealand như channel sinh tồn (Vanuatu RSE 15-20% GDP). Liên kết: Fiji website 74,8% > Singapore (PLMS+remittance corridors); Kiribati 18,7% (outer islands no internet); SIDS innovation 41,5% (bricolage Baker & Nelson 2005). CĐ2: 3 control variables PICs-specific (`aid_share_GDP_pct`, `remittance_share_GDP_pct`, `seasonal_worker_outflow_pct`).

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

---

## CHƯƠNG 6 — CÁC YẾU TỐ GIẢI THÍCH SƠ BỘ

**Bảng 6.1**. *Hệ số tương quan Pearson (n=101.185 — v3.1).*

| Yếu tố | Advanced | Upper-middle | Emerging | Frontier | SIDS |
|---|---|---|---|---|---|
| FDI ≥10% | −0,113 | −0,023 | +0,113 | +0,068 | **+0,222** |
| FSTS | **+0,113** | −0,086 | +0,062 | +0,014 | −0,050 |
| TCI (R&D + ISO) | **+0,128** | +0,016 | −0,029 | +0,019 | **+0,155** |
| DAI (website) | **−0,129** | +0,012 | +0,016 | +0,070 | −0,049 |

**Sáu phát hiện chính**: (1) FDI dương mạnh SIDS (+0,222); (2) FDI âm Advanced; (3) FSTS dương Advanced — Uppsala+OLI; (4) TCI dương SIDS+Advanced; (5) DAI âm Advanced — Tier-1 saturation; (6) Đảo dấu cross-regime — institutional moderation.

**Cảnh báo schema BREADY 2025 (v3.3)**: bảng 6.1 có thể bị nhiễu schema effect — kiểm chứng qua "triple-defense" §4.11 file 15.

**Lý giải dị biệt cross-regime qua Xu (2024) de jure-de facto (v3.3)**: gap formal-enforcement explains FDI sign reversal Emerging vs Advanced.

### 6.1 Pattern giới tính trong quản lý + sở hữu — bằng chứng EAP châu Á dẫn đầu *(mới v3.5b)*

**Bảng 6.1.1**. *Pattern giới tính trong TMT + ownership — phân tầng theo khu vực địa lý.*

| Khu vực | % nữ TMT (cấp cao) | % nữ ownership majority | Khoảng cách (TMT – Owner) |
|---|---|---|---|
| **East Asia & Pacific (EAP)** | **33,4%** *(dẫn đầu globally)* | **25,7%** *(dẫn đầu globally)* | +7,7 đpt |
| Latin America & Caribbean | 27,8% | 18,3% | +9,5 đpt |
| Sub-Saharan Africa | 21,3% | 14,9% | +6,4 đpt |
| Europe & Central Asia | 19,8% | 12,1% | +7,7 đpt |
| South Asia | 9,2% | 8,5% | +0,7 đpt |
| **Middle East & North Africa (MENA)** | **3,3%** *(thấp nhất globally)* | **1,7%** *(thấp nhất globally)* | +1,6 đpt |

Bốn quan sát: (a) EAP dẫn đầu — Asian gender paradox; (b) MENA thấp nhất — structural barriers; (c) 43/50 economies có ownership ceiling cao hơn management; (d) Boundary references: Mardones-Ibáñez (2025) Chile + Al-Najjar et al. (2025) S&P 500 U-shaped.

### 6.2 Đường cong U của innovation digital tech *(mới v3.5b)*

**Giai đoạn 1 (chi phí đầu tư cao)**: 1-3 năm đầu, giảm hiệu quả tài chính ngắn hạn — phù hợp DAI âm -0,129 Advanced + "digital theatre" (Verhoef et al., 2021). **Giai đoạn 2 (productivity payoff)**: vượt threshold ~3% revenue/năm × 3-5 năm sustained → tăng năng suất + cạnh tranh quốc tế + profit margin. Liên kết Tier-1/Tier-2 §4.4.5 file 15. Bằng chứng: Trung Quốc R&D 39,4% late-stage Tier-2; Vùng Vịnh transition phase; Việt Nam R&D 6,1% early Tier-2.

---

## CHƯƠNG 7 — KHOẢNG TRỐNG THỰC TIỄN VÀ KẾT LUẬN

### 7.1 Khoảng trống nghiên cứu thực tiễn (5 khoảng trống — v3.2)

(Giữ nguyên — xem commit 7738953 + b3306e1.)

### 7.2 Kết luận chính (8 kết luận)

(Giữ nguyên — xem commit b3306e1.)

### 7.3 Hàm ý cho luận án và Chuyên đề 2

#### 7.3.1 Hàm ý lý thuyết

(Giữ nguyên từ v3.3 — 5 evidence; AIPI; digital theatre warning. Xem commit cc33ed4.)

#### 7.3.2 Hàm ý phương pháp luận (mở rộng v3.3)

(Giữ nguyên từ v3.3 — 5 hàm ý + triple-defense system. Xem commit cc33ed4.)

#### 7.3.3 Hàm ý chính sách cho doanh nghiệp Việt Nam và khu vực (mở rộng v3.5c từ 6 lên **8 hàm ý**)

> **Cập nhật v3.5c**: Mở rộng (7) Migration labor partnership Pacific + (8) NEW Chính sách số hóa Asia.
> **Hàm ý (1)-(6)** giữ nguyên từ v3.2 — 6 hàm ý chính sách + 4 đề xuất GVC cho Việt Nam (commit 7738953).

**(7) Migration labor partnership Pacific cho Việt Nam — bài học từ PLMS Australia + RSE New Zealand** *(mới v3.5c — Phase 4 Đợt 3 sub-commit 3C)*

> **Bằng chứng nền tảng**: §5.7.5 file 16 v3.5a (PICs macro context); Bertram (2006) MIRAB model — file 04 v2.5 Section N.

Bốn đề xuất cụ thể cho doanh nghiệp + nhà hoạch định chính sách Việt Nam:

(a) **Học mô hình PLMS** *(Australia Pacific Labour Mobility Scheme)*: Australia chương trình PLMS gần 30.000 lao động PICs/năm, làm việc 1-3 năm trong nông nghiệp, chế biến thực phẩm, du lịch. Việt Nam có thể ký song phương MoU với Australia để chương trình tương tự **Vietnamese Skilled Worker Mobility Scheme** — tập trung vào nông nghiệp công nghệ cao + chế biến + healthcare aged-care (Australia có nhu cầu cao, dân số già hóa).

(b) **Học mô hình RSE** *(New Zealand Recognised Seasonal Employer)*: New Zealand RSE chỉ áp dụng cho viticulture (vườn nho) + horticulture (vườn cây ăn quả) + fishing — work permits 7 tháng/năm. Việt Nam hợp tác với NZ để mở **Aquaculture + Coffee + Cashew Skills Exchange** — leveraging chuyên môn Việt Nam trong các ngành này.

(c) **Cơ chế remittance corridor digital**: Theo NotebookLM 06/05/2026, Vanuatu RSE remittances chiếm 15-20% GDP — chứng minh model "labor mobility + digital remittance" hiệu quả. Việt Nam có thể hợp tác với Wise/Western Union/MoMo để **giảm phí remittance từ ~7% xuống <3%** cho lao động Việt ở Aus/NZ — tiết kiệm hàng trăm triệu USD/năm. Liên kết §5.3 (a) FDI commitment $2,4B với fintech focus.

(d) **Skills upgrading approach để tránh brain drain**: Migration labor có nguy cơ brain drain nếu chỉ low-skilled. Việt Nam cần đầu tư technical education + ngoại ngữ trước khi gửi đi, theo mô hình Korea Employment Permit System (EPS) — tập trung vào ngành cao kỹ + đảm bảo lao động return có vốn + kỹ năng để khởi nghiệp tại Việt Nam (return migration channel).

**(8) Chính sách số hóa Asia cho SME Việt Nam — bài học từ Singapore/Korea/Japan/Trung Quốc** *(mới v3.5c — Phase 4 Đợt 3 sub-commit 3C)*

> **Bằng chứng nền tảng**: §6.2 Innovation U-curve digital (commit b3306e1); Bảng 4.4 file 15 (Website Việt Nam 47% < EAP average 58,9%); §5.4 Trung Quốc Wang/Huang/Hong (2024) concentration risk.

Bốn lộ trình số hóa cho SME Việt Nam tham khảo:

(a) **Mô hình Singapore + Korea — AI integration full-stack** *(Tier-3 transformation)*: Singapore SmartNation initiative + Korea Digital New Deal đã đạt mức tích hợp AI vào toàn bộ chuỗi value chain — từ marketing automation → CRM intelligence → supply chain optimization → financial forecasting. SME Việt Nam ở giai đoạn này còn xa, **không nên copy nguyên mẫu** mà nên target **Tier-2 first** (xem điểm (d) dưới đây).

(b) **Mô hình Japan — 60% DN dùng AI back-office** *(Tier-2 productive transformation)*: Japan đã đạt 60% doanh nghiệp dùng AI cho back-office tasks (accounting automation, HR scheduling, customer service chatbots). Đây là **realistic target cho SME Việt Nam 2026-2030** — không cần AI cutting-edge, chỉ cần AI applied cho efficiency gains. Khuyến nghị: chính phủ tài trợ **AI Adoption Voucher Program** cho SME (~50 triệu VND/firm) để mua off-the-shelf AI tools (Microsoft Copilot, Notion AI, Make.com).

(c) **Mô hình Trung Quốc — smart manufacturing + concentration risk warning** *(Tier-2/3 hybrid + cảnh báo)*: Trung Quốc dẫn đầu Asia trong smart manufacturing với Industry 4.0 standards — Foxconn Shenzhen, BYD, Geely. Tuy nhiên **80% bank risk models PRC phụ thuộc dominant tech providers** (Wang/Huang/Hong, 2024 — *IRFA*) → concentration risk cao. Việt Nam cần học positive (smart manufacturing roadmap) nhưng **TRÁNH** lock-in vào single foreign vendor — đẩy mạnh open standards + multi-vendor procurement cho FDI manufacturing.

(d) **Mô hình ưu tiên cho SME Việt Nam — digital payment + social commerce** *(Tier-1.5 Vietnamese-specific)*: Việt Nam có lợi thế đặc biệt — VietQR ecosystem + mobile payment (MoMo, ZaloPay, ViettelPay) + social commerce qua TikTok/Facebook (>200 triệu user trong khu vực). SME Việt Nam nên ưu tiên 4 layer:
   1. **Digital payment integration** — accept mọi loại payment qua VietQR (đã miễn phí 100%, không như credit card 2-3%)
   2. **Social commerce optimization** — Facebook Live + TikTok Shop là kênh bán hàng chính cho retail SME
   3. **Cross-border e-commerce** — Shopee Asia Pacific + Amazon Vietnam Sellers Program để xuất khẩu micro
   4. **Cloud + basic AI tools** — Google Workspace + Microsoft 365 + Make.com automation
   → Mức **Tier-1.5** — vượt website passive (Tier-1) nhưng chưa đến full-stack AI (Tier-2/3) — phù hợp với pattern thực tế Việt Nam và mức R&D 6,1%.

**Hàm ý cho CĐ2**: bổ sung **biến `Digital_Tier_Vietnam`** với 4 cấp (Tier-1 website, Tier-1.5 digital payment+social commerce, Tier-2 productive AI, Tier-3 full-stack AI) → test xem mỗi tier có productivity payoff khác nhau không. Kỳ vọng: Tier-1 không add productivity (saturated); Tier-1.5 add productivity ở SME-driven economies (VN, IDN, PHL); Tier-2 add productivity ở Manufacturing; Tier-3 add productivity ở ICT + Finance.

#### 7.3.4 Hàm ý cho Chuyên đề 2 và luận án

(Giữ nguyên từ v3.3 — 8 robustness checks. Xem commit cc33ed4.)

### 7.4 Hạn chế của chuyên đề

(Giữ nguyên từ v3.2 — 7 hạn chế.)

### 7.5 Kế hoạch hoàn thiện

(Giữ nguyên từ v3.1a — 4 giai đoạn 6/2026 → 9/2026.)

---

## TÀI LIỆU THAM KHẢO

> Trích dẫn theo APA 7th. Danh mục đầy đủ ở `thesis/04_references_apa7.md` (v2.5).

---

## PHỤ LỤC

### Phụ lục A — Phạm vi thực tế của nhóm dữ liệu WBES

47 nước, 108 cặp QG×năm, 101.185 doanh nghiệp, 7 SIDS bao gồm Kiribati 2025.

### Phụ lục B – G

(Sẽ mở rộng giai đoạn 1–3 tháng 6–8/2026.)

---

*Phiên bản 3.0 (06/05/2026) — Biên tập tiếng Việt hoàn thiện.*
*Phiên bản 3.1c (06/05/2026) — §5.6 Mongolia REVAMP critical minerals.*
*Phiên bản 3.1d (06/05/2026) — 3 markdown image refs.*
*Phiên bản 3.2 (06/05/2026) — Asia context v2 integration.*
*Phiên bản 3.3 (07/05/2026) — Phase 2 NotebookLM Đợt 3 ripple-effects.*
*Phiên bản 3.4 (07/05/2026) — ADB Vietnam Outlook 2026 §5.3 mở rộng.*
*Phiên bản 3.5a (07/05/2026 — Phase 4 Đợt 3 sub-commit 3A) — §5.7.5 PICs macro context.*
*Phiên bản 3.5b (07/05/2026 — Phase 4 Đợt 3 sub-commit 3B) — §6.1 Gender + §6.2 Innovation U-curve.*

*Phiên bản 3.5c (07/05/2026 cuối phiên — Phase 4 Đợt 3 sub-commit 3C) — Mở rộng §7.3.3 từ 6 → 8 hàm ý chính sách: **(7) Migration labor partnership Pacific cho Việt Nam** với 4 đề xuất (a) PLMS Australia agriculture+aged-care; (b) RSE New Zealand viticulture+horticulture; (c) remittance corridor digital fintech 7%→<3%; (d) skills upgrading return migration channel theo Korea EPS. **(8) NEW Chính sách số hóa Asia cho SME Việt Nam** với 4 lộ trình (a) Singapore/Korea AI full-stack Tier-3; (b) Japan 60% DN AI back-office Tier-2 + AI Adoption Voucher; (c) Trung Quốc smart manufacturing Tier-2/3 + concentration risk warning Wang/Huang/Hong (2024); (d) **Mô hình ưu tiên Việt Nam Tier-1.5 — digital payment VietQR + social commerce TikTok/Facebook + cross-border Shopee/Amazon + cloud Google/Microsoft**. Hàm ý CĐ2: biến `Digital_Tier_Vietnam` với 4 cấp test productivity payoff khác nhau. **HOÀN THÀNH ĐỢT 3 PHASE 4** — file 16 v3.5 với 3 sub-commits 3A/B/C all pushed.*

> **Sections §7.1, §7.2, §7.3.1, §7.3.2, §7.3.4, §7.4, §7.5 v3.5a-c**: Giữ nguyên từ v3.2 (commit 7738953) và v3.3 (commit cc33ed4) — full content vẫn truy cập qua git history.