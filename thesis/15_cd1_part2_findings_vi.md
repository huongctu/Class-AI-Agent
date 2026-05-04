# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> **Phiên bản 2.3 (cập nhật ngày 04/05/2026)**: Pool **95.689 doanh nghiệp** ở **36 nền kinh tế** với **91 cặp quốc gia × năm** giai đoạn **2009–2025** (bao gồm 6 đợt khảo sát năm 2025: Brunei, Thái Lan, Sri Lanka, Afghanistan, Nepal, **Ấn Độ**). Bổ sung mới: India 2025 (10.479 doanh nghiệp) và Nepal panel 2009/2013/2023 (1.432 doanh nghiệp).

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi pool**. Sau hòa hợp 92 file WBES, pool dữ liệu bao gồm **95.689 doanh nghiệp** thuộc **36 nền kinh tế** châu Á và 1 nền kinh tế đảo nhỏ Thái Bình Dương (Vanuatu — đại diện SIDS), trải khắp **91 đơn vị quốc gia × năm khảo sát** trong giai đoạn **2009–2025**. Phân bố theo regime ICRV: Emerging 47.202 (49%), Frontier 26.547 (28%), Upper-middle 16.693 (17%), Advanced 5.008 (5%), SIDS 239 (0,2%). Đặc biệt, pool đã bao gồm **6 đợt khảo sát năm 2025** với 14.215 doanh nghiệp: Ấn Độ (n=10.479), Nepal (n=1.740), Thái Lan (n=813), Sri Lanka (n=607), Afghanistan (n=426), Brunei (n=150) — đặt chuyên đề ở vị trí cập nhật nhất so với các tổng quan IB hiện hành. Coverage chi tiết: xem **Phụ lục A**.

**Phân bố thời gian**. Pool có 12 mốc khảo sát từ 2009 đến 2025: 2009 (n=9.249), 2011 (n=1.366), 2012 (n=3.079), 2013 (n=7.701), 2014 (n=10.323), 2015 (n=3.695), 2016 (n=2.348), 2018 (n=332), 2019 (n=6.983), 2020 (n=546), 2021 (n=238), 2022 (n=12.693), 2023 (n=8.364), 2024 (n=14.557), **2025 (n=14.215)**. Phân bố theo ba giai đoạn schema: 2009–2012 (16.307 doanh nghiệp), 2013–2017 (24.067 doanh nghiệp), **2018–2025 (55.315 doanh nghiệp — chiếm 58% pool)**.

**Ba thế hệ schema**. Dữ liệu WBES qua giai đoạn 2009–2025 có ba thế hệ schema không hoàn toàn trùng tên biến: (i) Thế hệ 1 (2007–2012) với schema PICS3 và BREADY ban đầu; (ii) Thế hệ 2 (2013–2017) với WBES Standardized chính thức; (iii) Thế hệ 3 (**2018–2025**) với Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, TGS Followup, EAP Core. Mặc dù ba thế hệ khác nhau, các biến cốt lõi (`d2` doanh thu, `l1` số lao động thường xuyên, `d3b`/`d3c` cường độ xuất khẩu, `b5` năm thành lập, `b2b` tỷ trọng sở hữu nước ngoài, `h1`/`h8` đổi mới và R&D, `b8` chứng nhận ISO, `c22b` website) duy trì tính nhất quán đủ tốt cho phân tích so sánh xuyên thế hệ.

**Hòa hợp**. Giao thức hòa hợp được mô tả chi tiết ở `thesis/08_p7_data_harmonization_protocol_vi.md` và thực thi qua pipeline Python (`wbes/02_harmonize.py`). Quy trình gồm: (i) đọc 92 file `.dta` với fallback mã hoá Latin-1/CP1252; (ii) crosswalk biến; (iii) loại các giá trị WBES "missing-by-design" ({-9,…,-1}); (iv) tính FSTS = `d3b + d3c`; (v) winsorize log năng suất lao động trong từng cặp quốc gia × năm ở mức 1%/99%; (vi) loại doanh nghiệp có lao động ≤ 0 hoặc doanh thu ≤ 0. Mongolia panel 2009/2013/2019 và Nepal panel 2009/2013/2023 được tách thành các lát cross-section bằng filter `year == YYYY`.

**Sai số đo lường và caveat đơn vị tiền tệ**. Trong phiên bản hiện tại, doanh thu (`d2`) chưa được chuyển sang USD PPP. Vì vậy, các bảng so sánh năng suất xuyên quốc gia chỉ trình bày các **thước đo dispersion** (sd của log năng suất, tỷ số P90/P10, P75/P25) – tất cả bất biến với đơn vị tiền tệ.

### 4.2 Thực trạng năng suất lao động — dispersion trong từng quốc gia

**Bảng 4.1**. *Dispersion năng suất lao động theo regime, bình quân có trọng số (n=91 cặp quốc gia × năm).*

| Nhóm regime | Số cặp quốc gia × năm | Số doanh nghiệp | sd log năng suất | Tỷ số P90/P10 | Tỷ số P75/P25 |
|---|---|---|---|---|---|
| Advanced | 10 | 4.289 | 1,00 | 13,3 | 3,6 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| **Emerging** | **19** | **44.823** | **1,24** | **30,8** | **5,1** |
| Frontier | 37 | 17.090 | 1,36 | 38,5 | 6,2 |
| SIDS | 2 | 196 | 1,35 | 42,1 | 5,6 |

*Nguồn: Tính toán của tác giả từ pool WBES 95.689 doanh nghiệp, 91 cặp quốc gia × năm.*

Bốn phát hiện chính:

*Thứ nhất*, dispersion năng suất tăng từ Advanced (sd=1,00) lên 1,29 ở Upper-middle, **giảm xuống 1,24 ở Emerging** (do bổ sung India 2025 với mẫu rất lớn n=10.479 và dispersion thấp), rồi tăng lại lên 1,36 ở Frontier và 1,35 ở SIDS. Pattern này khẳng định **hypothesis misallocation** của Hsieh & Klenow (2009, 2014) cho Frontier, nhưng cho thấy rằng các nền kinh tế Emerging có quy mô lớn (Ấn Độ) có thể có dispersion thấp hơn dự kiến nhờ cơ chế thị trường hoàn thiện hơn.

*Thứ hai*, tỷ số P90/P10 tăng từ 13,3 lần ở Advanced lên 42,1 lần ở SIDS, với một bước nhảy lớn giữa Upper-middle (27,7) và Frontier (38,5). Trong cùng quốc gia Frontier, doanh nghiệp ở phân vị 90 có năng suất cao gấp 38–42 lần doanh nghiệp ở phân vị 10 — bằng chứng misallocation cực mạnh.

*Thứ ba*, tỷ số P75/P25 (dispersion trung tâm phân phối) cũng cao nhất ở Frontier (6,2), thấp nhất ở Advanced (3,6) — cho thấy dị biệt năng suất là pattern hệ thống xuyên toàn bộ phân phối, không chỉ ở đuôi.

*Thứ tư*, sự đơn điệu của dispersion giữa Advanced – Upper-middle – Frontier (loại trừ Emerging do hiệu ứng Ấn Độ) cung cấp bằng chứng cho **hệ giả thuyết H5** (institutional moderation). Cần kiểm tra thêm bằng cách tách Emerging thành sub-groups (large vs small) ở Chuyên đề 2.

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *Cường độ quốc tế hóa, tỷ trọng exporter, tăng trưởng việc làm theo regime.*

| Nhóm regime | FSTS trung bình (%) | FSTS trung vị (%) | Exporter share (% doanh nghiệp) | Tăng trưởng việc làm CAGR 3 năm (%) |
|---|---|---|---|---|
| Advanced | 12,8 | 0,0 | 27,6 | 3,15 |
| Upper-middle | 10,3 | 0,0 | 21,7 | 4,25 |
| Emerging | 8,7 | 0,0 | 15,6 | 2,77 |
| Frontier | 10,1 | 0,0 | 15,6 | 3,64 |
| SIDS | 4,1 | 0,0 | 9,7 | 8,51 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng doanh nghiệp xuất khẩu giảm tuyến tính theo regime*: từ 27,6% ở Advanced xuống 9,7% ở SIDS. Sau khi bổ sung India 2025 (mẫu lớn với cường độ xuất khẩu thấp), Emerging có exporter share 15,6% — bằng Frontier.

(2) *Trung vị FSTS bằng 0 ở mọi nhóm* — hơn 50% doanh nghiệp KHÔNG xuất khẩu gì.

(3) *SIDS có exporter share thấp nhất (9,7%)* — phù hợp với forced internationalization penalty (Đỗ & Phan, 2026 — P8 manuscript).

(4) *Tăng trưởng việc làm cao nhất ở SIDS (8,51%)* — phản ánh tái thiết hậu COVID-19 của ngành du lịch Vanuatu.

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

**Bảng 4.4**. *Tỷ lệ doanh nghiệp đổi mới sáng tạo và áp dụng số theo regime (% doanh nghiệp).*

| Nhóm regime | Sản phẩm mới (h1) | Quy trình mới (h2) | R&D dương (h8) | Chứng nhận ISO (b8) | Có website (c22b) |
|---|---|---|---|---|---|
| Advanced | 26,2 | 57,0 | 21,3 | 36,8 | 64,4 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 17,2 | 65,0 | 16,3 | 25,0 | 49,0 |
| Frontier | 22,0 | 68,6 | 12,4 | 21,3 | 36,5 |
| SIDS | 35,8 | 67,6 | 7,2 | 16,3 | 43,3 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Năm phát hiện:

(1) *Tỷ lệ chứng nhận ISO và có website giảm tuyến tính theo regime* — từ 36,8% ISO ở Advanced xuống 16,3% ở SIDS; từ 64,4% website ở Advanced xuống 36,5% ở Frontier. Hai chỉ số này phản ánh trực tiếp **năng lực thể chế hoá chất lượng và áp dụng số**.

(2) *Tỷ lệ R&D dương giảm dần theo regime*: 21,3% Advanced → 21,0% Upper-middle → **16,3% Emerging** (giảm từ 21,9% sau khi bổ sung India 2025) → 12,4% Frontier → 7,2% SIDS. Bổ sung India 2025 làm rõ rằng Emerging có discontinuity với Upper-middle.

(3) *Tỷ lệ giới thiệu sản phẩm mới ở Emerging chỉ 17,2%* — thấp hơn Frontier (22,0%) sau khi bổ sung Ấn Độ với tỷ lệ đổi mới thấp.

(4) *Tỷ lệ giới thiệu quy trình mới (h2) trên 65% ở mọi nhóm trừ Advanced (57%)* — đổi mới quy trình là incremental change phổ biến.

(5) *Khoảng cách Advanced – SIDS ở R&D là 14 điểm phần trăm; ở ISO là 21 điểm phần trăm; ở website là 21–28 điểm phần trăm* — gợi ý ba kênh khác nhau qua đó năng lực thể chế tác động lên hiệu quả.

### 4.5 Thực trạng cấu trúc doanh nghiệp

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo regime (%).*

| Nhóm regime | SME (<100 LĐ) | Exporter (>0%) | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,9 | 27,6 | 10,9 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 74,2 | 15,6 | 4,7 |
| Frontier | 84,7 | 15,6 | 6,1 |
| SIDS | 99,2 | 9,7 | 30,6 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng SME 74–99% ở mọi nhóm* — SME chi phối tuyệt đại đa số doanh nghiệp châu Á.

(2) *Emerging và Frontier có tỷ trọng exporter giống nhau (15,6%)* — sau khi bổ sung India 2025, ranh giới giữa Emerging và Frontier về xuất khẩu đã mờ. Chỉ Advanced và Upper-middle giữ ưu thế xuất khẩu rõ rệt.

(3) *Tỷ trọng FDI ≥ 10% có pattern phi tuyến đáng chú ý*: cao ở Advanced (10,9%) và Upper-middle (8,4%), thấp ở Emerging (4,7%) và Frontier (6,1%), nhưng **cao bất thường ở SIDS (30,6%)** do mẫu nhỏ và đặc thù Vanuatu.

(4) *Tỷ trọng FDI ở Emerging (4,7%) thấp nhất trong tất cả non-SIDS* — Ấn Độ (n=29.136 trong Emerging, ~62%) có FDI thấp do thị trường nội địa lớn và khung pháp lý FDI hạn chế lịch sử.

### 4.6 Bức tranh thay đổi theo thời gian — so sánh ba giai đoạn 2009–2025

Pool dữ liệu được phân thành ba giai đoạn theo thế hệ schema: **2009–2012** (n=16.307), **2013–2017** (n=24.067), **2018–2025** (n=55.315).

**Bảng 4.6**. *Δ điểm phần trăm các chỉ số khi so sánh giai đoạn 2018–2025 với 2009–2012.*

| Nhóm regime | Δ Website | Δ Exporter | Δ FDI ≥10% | Δ R&D | Δ ISO | Δ Innov product |
|---|---|---|---|---|---|---|
| Advanced | n/a* | n/a* | n/a* | n/a* | n/a* | n/a* |
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5** | -25,4 | n/a* |
| Emerging | +20,3 | -7,5 | -10,9 | -42,1 | +1,9 | -23,5 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 | n/a* |
| SIDS | +42,9 | +11,3 | -10,0 | n/a* | -24,3 | n/a* |

*Nguồn: Tính toán của tác giả từ pool WBES.*

\* n/a: thiếu dữ liệu giai đoạn 2009–2012 cho regime đó.

Năm phát hiện:

(1) *Số hoá tăng vọt ở Frontier, Emerging và SIDS*: tỷ lệ doanh nghiệp có website tăng 20–43 điểm phần trăm trong giai đoạn 2009–2025 — hiện tượng "leapfrog".

(2) *R&D giảm mạnh ở Emerging (Δ = −42)* — do thay đổi cấu trúc mẫu: 2009–2012 có Indonesia, Mongolia với R&D cao; 2018–2025 có Ấn Độ, Nepal với R&D thấp. Dữ liệu Ấn Độ 2025 (n=10.479) đặc biệt làm rõ pattern này.

(3) *Tỷ trọng exporter giảm 7,5 điểm phần trăm ở Emerging* — chuyển dịch về thị trường nội địa giai đoạn hậu chiến tranh thương mại Mỹ-Trung 2018+.

(4) *Tăng tỷ lệ ISO ở Frontier (+18,5 điểm phần trăm)* — bằng chứng quá trình chính thức hoá.

(5) *SIDS tăng exporter (+11,3 điểm phần trăm) và website (+42,9 điểm phần trăm) song hành với giảm ISO (−24,3 điểm phần trăm)* — pattern phức tạp phản ánh tái cấu trúc kinh tế Vanuatu hậu COVID.

### 4.7 Tổng hợp Chương 4

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **95.689 doanh nghiệp ở 36 nền kinh tế châu Á (91 cặp quốc gia × năm) trong giai đoạn 2009–2025**. Bốn kết luận chính:

(i) *Dispersion năng suất nội bộ theo pattern không hoàn toàn đơn điệu*: Advanced (sd=1,00) → Upper-middle (1,29) → Emerging (1,24) → Frontier (1,36) → SIDS (1,35). Việc dispersion Emerging GIẢM so với Upper-middle là phát hiện mới sau khi bổ sung India 2025 — gợi ý các nền kinh tế Emerging quy mô lớn có cơ chế thị trường giảm dispersion. Pattern này cần được kiểm tra ở Chuyên đề 2.

(ii) *Quốc tế hóa là hiện tượng phân cực ở mọi nhóm*: hơn 50% doanh nghiệp KHÔNG xuất khẩu; chỉ 10–28% tham gia xuất khẩu. SIDS có tỷ trọng exporter thấp nhất (9,7%) phù hợp với forced internationalization penalty.

(iii) *Năng lực thể chế hoá (ISO), năng lực số (website) và năng lực R&D có pattern khác nhau theo regime* — khẳng định cần tách bạch TCI và DAI trong mô hình Chuyên đề 2.

(iv) *Số hoá tăng vọt giai đoạn 2018–2025 ở Frontier, Emerging và SIDS* (+20–43 điểm phần trăm tỷ lệ website) — bằng chứng "leapfrog". Dữ liệu 2025 (Ấn Độ, Nepal, Brunei, Thái Lan, Sri Lanka, Afghanistan) củng cố thêm pattern này.

---

*Tiếp tục ở Phần 3 (Chương 5 — bốn tiểu cảnh điển hình; Chương 6 — yếu tố giải thích sơ bộ; Chương 7 — kết luận; Tài liệu tham khảo) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*
