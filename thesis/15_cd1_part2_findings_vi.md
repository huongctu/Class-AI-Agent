# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> **Phiên bản 2.1 (cập nhật ngày 04/05/2026 — sau bổ sung Myanmar 2014/2016 + Mongolia 2019)**: Pool tăng từ 81.957 lên **83.778 doanh nghiệp** ở **36 nền kinh tế** với **87 cặp quốc gia × năm**.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2007–2024

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi pool**. Sau hòa hợp 88 file WBES, pool dữ liệu bao gồm **83.778 doanh nghiệp** thuộc **36 nền kinh tế** châu Á và 1 nền kinh tế đảo nhỏ Thái Bình Dương (Vanuatu — đại diện SIDS), trải khắp **87 đơn vị quốc gia × năm khảo sát** trong giai đoạn 2009–2025. Phân bố theo regime ICRV: Emerging 36.723 (44%), Frontier 25.115 (30%), Upper-middle 16.693 (20%), Advanced 5.008 (6%), SIDS 239 (0,3%). So với phiên bản 2.0 đã thêm Myanmar 2014 (632 doanh nghiệp), Myanmar 2016 (607 doanh nghiệp) và Mongolia 2019 (582 doanh nghiệp từ panel). Coverage chi tiết: xem **Phụ lục A**.

**Ba thế hệ schema**. Dữ liệu WBES qua giai đoạn 2009–2025 có ba thế hệ schema không hoàn toàn trùng tên biến: (i) Thế hệ 1 (2007–2012) với schema PICS3 và BREADY ban đầu; (ii) Thế hệ 2 (2013–2017) với WBES Standardized chính thức; (iii) Thế hệ 3 (2018–2025) với Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, TGS Followup, EAP Core. Mặc dù ba thế hệ khác nhau, các biến cốt lõi (`d2` doanh thu, `l1` số lao động thường xuyên, `d3b`/`d3c` cường độ xuất khẩu, `b5` năm thành lập, `b2b` tỷ trọng sở hữu nước ngoài, `h1`/`h8` đổi mới và R&D, `b8` chứng nhận ISO, `c22b` website) duy trì tính nhất quán đủ tốt cho phân tích so sánh xuyên thế hệ.

**Hòa hợp**. Giao thức hòa hợp được mô tả chi tiết ở `thesis/08_p7_data_harmonization_protocol_vi.md` và thực thi qua pipeline Python (`wbes/02_harmonize.py`). Quy trình gồm: (i) đọc 88 file `.dta` với fallback mã hoá Latin-1/CP1252 cho file lỗi UTF-8; (ii) crosswalk biến; (iii) loại các giá trị WBES "missing-by-design" ({-9,…,-1}); (iv) tính FSTS = `d3b + d3c` (xuất khẩu gián tiếp + trực tiếp); (v) winsorize log năng suất lao động trong từng cặp quốc gia × năm ở mức 1%/99%; (vi) loại doanh nghiệp có lao động ≤ 0 hoặc doanh thu ≤ 0. Mongolia panel 2009/2013/2019 được tách thành ba lát cross-section bằng filter `year == YYYY`.

**Sai số đo lường và caveat đơn vị tiền tệ**. Trong phiên bản hiện tại, doanh thu (`d2`) chưa được chuyển sang USD PPP — tỷ giá PPP từng quốc gia × năm cần lấy từ World Development Indicators. Vì vậy, các bảng so sánh năng suất xuyên quốc gia chỉ trình bày các **thước đo dispersion** (sd của log năng suất, tỷ số P90/P10, P75/P25) – tất cả bất biến với đơn vị tiền tệ.

### 4.2 Thực trạng năng suất lao động — dispersion trong từng quốc gia

Năng suất lao động được đo bằng `log(d2/l1)` cho từng doanh nghiệp; sau đó tính các thước đo dispersion trong từng cặp quốc gia × năm; cuối cùng tính bình quân có trọng số (theo số doanh nghiệp) trong từng nhóm regime ICRV.

**Bảng 4.1**. *Dispersion năng suất lao động theo regime, bình quân có trọng số (n=87 cặp quốc gia × năm).*

| Nhóm regime | Số cặp quốc gia × năm | Số doanh nghiệp | sd log năng suất | Tỷ số P90/P10 | Tỷ số P75/P25 |
|---|---|---|---|---|---|
| Advanced | 10 | 4.289 | 1,00 | 13,3 | 3,6 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 18 | 34.344 | 1,37 | 37,4 | 5,7 |
| Frontier | 34 | 15.676 | 1,36 | 38,8 | 6,0 |
| SIDS | 2 | 196 | 1,35 | 42,1 | 5,6 |

*Nguồn: Tính toán của tác giả từ pool WBES 83.778 doanh nghiệp, 87 cặp quốc gia × năm.*

Bốn phát hiện chính từ Bảng 4.1:

*Thứ nhất*, dispersion năng suất tăng từ Advanced (sd=1,00) lên 1,29 ở Upper-middle, rồi đạt **plateau ở mức 1,35–1,37** xuyên ba regime cuối (Emerging, Frontier, SIDS). Pattern này khẳng định **hypothesis misallocation** của Hsieh & Klenow (2009, 2014): các nền kinh tế có thể chế chưa hoàn thiện không phân bổ vốn và lao động hiệu quả tới những doanh nghiệp năng suất cao, dẫn đến dispersion lớn ngay trong cùng quốc gia. Tuy nhiên, sự "bão hòa" của dispersion ở mức ~1,36 cho thấy có **trần dispersion** (dispersion ceiling) — vượt qua đó các doanh nghiệp năng suất cực thấp sẽ phá sản, giữ phân phối ổn định ở cận trên này.

*Thứ hai*, tỷ số P90/P10 — nghĩa là doanh nghiệp ở phân vị 90% có năng suất gấp bao nhiêu lần doanh nghiệp ở phân vị 10% trong cùng quốc gia — tăng từ 13,3 lần ở Advanced lên 42,1 lần ở SIDS. SIDS có P90/P10 cao nhất bất chấp sd log thấp, do mẫu rất nhỏ (Vanuatu, n=196) khiến đuôi phân phối có ảnh hưởng lớn.

*Thứ ba*, tỷ số P75/P25 (đo dispersion ở phần trung tâm phân phối) tăng đơn điệu từ 3,6 (Advanced) lên 6,0 (Frontier) — chứng tỏ dị biệt năng suất KHÔNG chỉ là chuyện đuôi (tail effects) mà là pattern hệ thống xuyên toàn bộ phân phối.

*Thứ tư*, sự đơn điệu của dispersion theo regime cung cấp **bằng chứng thực tiễn cho hệ giả thuyết H5** (institutional moderation) trong Chuyên đề 2: chất lượng thể chế có gradient tác động lên dispersion hiệu quả, gợi ý rằng cùng mức quốc tế hóa có thể tạo ra các kết quả hiệu quả khác nhau trong các regime khác nhau.

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

Cường độ quốc tế hóa được đo bằng FSTS = (% xuất khẩu gián tiếp `d3b` + % xuất khẩu trực tiếp `d3c`) trên tổng doanh thu. Doanh nghiệp được coi là "exporter" nếu FSTS > 0%.

**Bảng 4.3**. *Cường độ quốc tế hóa, tỷ trọng exporter, tăng trưởng việc làm theo regime.*

| Nhóm regime | FSTS trung bình (%) | FSTS trung vị (%) | Exporter share (% doanh nghiệp) | Tăng trưởng việc làm CAGR 3 năm (%) |
|---|---|---|---|---|
| Advanced | 12,8 | 0,0 | 27,6 | 3,15 |
| Upper-middle | 10,3 | 0,0 | 21,7 | 4,25 |
| Emerging | 10,4 | 0,0 | 18,1 | 2,60 |
| Frontier | 10,2 | 0,0 | 15,4 | 3,67 |
| SIDS | 4,1 | 0,0 | 9,7 | 8,51 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng doanh nghiệp xuất khẩu giảm tuyến tính theo regime*: từ 27,6% ở Advanced xuống 9,7% ở SIDS. Ngay cả ở Advanced, **chỉ một phần tư doanh nghiệp tham gia xuất khẩu** — khẳng định stylized fact rằng quốc tế hóa là một hành vi phân cực ở mọi nhóm.

(2) *Trung vị FSTS bằng 0 ở mọi nhóm* — hơn 50% doanh nghiệp KHÔNG xuất khẩu gì. Trung bình FSTS ở Advanced (12,8%) cao chủ yếu do mức xuất khẩu cao của thiểu số doanh nghiệp xuất khẩu, không phải do nhiều doanh nghiệp tham gia.

(3) *SIDS có exporter share thấp nhất (9,7%) bất chấp đặc điểm "kinh tế nhỏ và mở"* — phù hợp với phát hiện về **forced internationalization penalty** ở Pacific SIDS (Đỗ & Phan, 2026 — P8 manuscript).

(4) *Tăng trưởng việc làm cao nhất ở SIDS (8,51%)* — phản ánh đặc điểm tái thiết hậu COVID-19 của ngành du lịch Vanuatu.

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

Năm thước đo: tỷ lệ doanh nghiệp giới thiệu sản phẩm mới (`h1`), giới thiệu quy trình mới (`h2`), có chi R&D dương (`h8`), có chứng nhận ISO quốc tế (`b8`), có website riêng (`c22b`).

**Bảng 4.4**. *Tỷ lệ doanh nghiệp đổi mới sáng tạo và áp dụng số theo regime (% doanh nghiệp).*

| Nhóm regime | Sản phẩm mới (h1) | Quy trình mới (h2) | R&D dương (h8) | Chứng nhận ISO (b8) | Có website (c22b) |
|---|---|---|---|---|---|
| Advanced | 26,2 | 57,0 | 21,3 | 36,8 | 64,4 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 21,7 | 68,9 | 21,9 | 27,3 | 51,0 |
| Frontier | 22,1 | 69,7 | 13,0 | 22,0 | 35,9 |
| SIDS | 35,8 | 67,6 | 7,2 | 16,3 | 43,3 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Năm phát hiện:

(1) *Tỷ lệ chứng nhận ISO và có website giảm tuyến tính theo regime* — từ 36,8% ISO ở Advanced xuống 16,3% ở SIDS; từ 64,4% website ở Advanced xuống 35,9% ở Frontier. Hai chỉ số này phản ánh trực tiếp **năng lực thể chế hoá chất lượng và áp dụng số** — gợi ý sự cần thiết tách bạch TCI (chất lượng) và DAI (số hoá) trong mô hình của Chuyên đề 2.

(2) *Tỷ lệ R&D dương ổn định ở 21–22% xuyên Advanced – Upper-middle – Emerging* nhưng **sụt mạnh ở Frontier (13,0%) và SIDS (7,2%)**. Đây là chứng cứ thực tiễn cho **discontinuity** ở năng lực đổi mới giữa các nhóm thu nhập trung bình thấp và trung bình cao — phù hợp với hypothesis "absorptive capacity threshold" (Cohen & Levinthal, 1990).

(3) *Tỷ lệ giới thiệu sản phẩm mới ở SIDS cao nhất (35,8%)* — bất ngờ; có thể phản ánh tính linh hoạt của doanh nghiệp nhỏ ở thị trường nội địa hẹp (Vanuatu).

(4) *Tỷ lệ giới thiệu quy trình mới (h2) trên 65% ở mọi nhóm trừ Advanced (57%)* — đổi mới quy trình là incremental change phổ biến ở các nền kinh tế đang phát triển.

(5) *Khoảng cách Advanced – SIDS ở R&D là 14 điểm phần trăm; ở ISO là 21 điểm phần trăm; ở website là 21–28 điểm phần trăm* — gợi ý ba kênh khác nhau qua đó năng lực thể chế tác động lên hiệu quả: kênh R&D, kênh chứng nhận chất lượng, kênh hạ tầng số. Đây là cơ sở cho phân tích moderation của TCI vs DAI ở Chuyên đề 2.

### 4.5 Thực trạng cấu trúc doanh nghiệp

Cấu trúc doanh nghiệp được đo qua: tỷ trọng SME (< 100 lao động), tỷ trọng exporter, tỷ trọng FDI ≥ 10%.

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo regime (%).*

| Nhóm regime | SME (<100 LĐ) | Exporter (>0%) | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,9 | 27,6 | 10,9 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 75,3 | 18,1 | 5,6 |
| Frontier | 84,5 | 15,4 | 6,4 |
| SIDS | 99,2 | 9,7 | 30,6 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng SME 75–99% ở mọi nhóm* — khẳng định stylized fact rằng SME chi phối tuyệt đại đa số doanh nghiệp châu Á. SIDS có 99,2%.

(2) *Tỷ trọng exporter giảm tuyến tính từ Advanced (27,6%) xuống SIDS (9,7%)* — đã phân tích ở Mục 4.3.

(3) *Tỷ trọng FDI ≥ 10% có pattern phi tuyến đáng chú ý*: cao ở Advanced (10,9%) và Frontier (6,4%), nhưng **cao bất thường ở SIDS (30,6%)** do mẫu nhỏ và đặc thù du lịch + viễn thông Vanuatu thường có vốn nước ngoài.

(4) *Tỷ trọng FDI ở Emerging (5,6%) thấp hơn Frontier (6,4%)* — Emerging chứa Ấn Độ (n=18.657) với FDI thấp do thị trường nội địa lớn; Frontier chứa các nước nhỏ phụ thuộc đầu tư khu vực.

### 4.6 Bức tranh thay đổi theo thời gian — so sánh ba giai đoạn

Pool dữ liệu được phân thành ba giai đoạn theo thế hệ schema: 2007–2012, 2013–2017, 2018–2024.

**Bảng 4.6**. *Δ điểm phần trăm các chỉ số khi so sánh 2018–2024 với 2007–2012.*

| Nhóm regime | Δ Website | Δ Exporter | Δ FDI ≥10% | Δ R&D | Δ ISO | Δ Innov product |
|---|---|---|---|---|---|---|
| Advanced | n/a* | n/a* | n/a* | n/a* | n/a* | n/a* |
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5** | -25,4 | n/a* |
| Emerging | +20,3 | -3,0 | -10,3 | -39,2 | +2,2 | -22,8 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 | n/a* |
| SIDS | +42,9 | +11,3 | -10,0 | n/a* | -24,3 | n/a* |

*Nguồn: Tính toán của tác giả từ pool WBES.*

\* n/a: thiếu dữ liệu giai đoạn 2007–2012 cho regime đó.
\** Upper-middle Δ R&D dựa trên Trung Quốc 2012 vs 2024 nên có biến động lớn do thay đổi mẫu chứ không phải biến động thực.

Năm phát hiện:

(1) *Số hoá tăng vọt ở Frontier, Emerging và SIDS*: tỷ lệ doanh nghiệp có website tăng 20–43 điểm phần trăm trong vòng 12 năm — hiện tượng "leapfrog" phù hợp với Banalieva & Dhanaraj (2019).

(2) *R&D giảm mạnh ở Emerging và Frontier* (Δ = −39 và −19 điểm phần trăm) — chủ yếu do thay đổi cấu trúc mẫu: giai đoạn 2007–2012 có Indonesia, Mongolia với R&D cao; giai đoạn 2018–2024 mở rộng sang Ấn Độ với R&D thấp hơn. Sau khi bổ sung Myanmar 2014/2016 và Mongolia 2019, pattern này dịu nhẹ một chút (Δ R&D Emerging từ −39,2 không thay đổi đáng kể).

(3) *Tỷ trọng exporter giảm 3 điểm phần trăm ở Emerging* — phản ánh chuyển dịch về thị trường nội địa.

(4) *Tăng tỷ lệ ISO ở Frontier (+18,5 điểm phần trăm)* — bằng chứng quá trình chính thức hoá doanh nghiệp.

(5) *SIDS tăng exporter (+11,3 điểm phần trăm) và website (+42,9 điểm phần trăm) song hành với giảm ISO (−24,3 điểm phần trăm)* — pattern phức tạp phản ánh tái cấu trúc kinh tế Vanuatu hậu COVID.

### 4.7 Tổng hợp Chương 4

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **83.778 doanh nghiệp ở 36 nền kinh tế châu Á (87 cặp quốc gia × năm) trong giai đoạn 2009–2025**. Bốn kết luận chính:

(i) *Dispersion năng suất nội bộ tăng từ Advanced (sd=1,00) lên plateau 1,35–1,37 ở Emerging/Frontier/SIDS*; P90/P10 từ 13,3 lên 42,1 lần. Pattern khẳng định mạnh hypothesis misallocation và là cơ sở thực tiễn cho hypothesis institutional moderation H5.

(ii) *Quốc tế hóa là hiện tượng phân cực ở mọi nhóm*: hơn 50% doanh nghiệp KHÔNG xuất khẩu; chỉ 10–28% tham gia xuất khẩu. SIDS có tỷ trọng exporter thấp nhất phù hợp với forced internationalization penalty.

(iii) *Năng lực thể chế hoá (ISO), năng lực số (website) và năng lực R&D có pattern khác nhau theo regime* — khẳng định cần tách bạch TCI và DAI trong mô hình Chuyên đề 2.

(iv) *Số hoá tăng vọt giai đoạn 2018–2024 ở Frontier, Emerging và SIDS* (+20–43 điểm phần trăm) — bằng chứng "leapfrog".

---

*Tiếp tục ở Phần 3 (Chương 5 — bốn tiểu cảnh điển hình; Chương 6 — yếu tố giải thích sơ bộ; Chương 7 — kết luận; Tài liệu tham khảo) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*
