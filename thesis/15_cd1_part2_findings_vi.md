# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> **Phiên bản 2 (cập nhật ngày 04/05/2026)**: Tất cả số liệu trong các bảng đã được tính trực tiếp từ pool 81.957 doanh nghiệp WBES sau hòa hợp, dùng `wbes/04_describe.py` (xem `thesis/17_cd1_data_pipeline.md`). Số liệu cũ (indicative) đã được thay bằng số thực tế.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2007–2024

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi pool**. Sau hòa hợp 85 file WBES, pool dữ liệu bao gồm **81.957 doanh nghiệp** thuộc **35 nền kinh tế** châu Á và 1 nền kinh tế đảo nhỏ Thái Bình Dương (Vanuatu — đại diện SIDS), trải khắp **84 đơn vị quốc gia × năm khảo sát** trong giai đoạn 2009–2025. Phân bố theo regime ICRV: Emerging 36.141 (44%), Frontier 23.876 (29%), Upper-middle 15.174 (19%), Advanced 4.289 (5%), SIDS 196 (0,2%). Coverage chi tiết quốc gia × năm: xem **Phụ lục A**.

**Ba thế hệ schema**. Dữ liệu WBES qua giai đoạn 2009–2025 có ba thế hệ schema không hoàn toàn trùng tên biến: (i) Thế hệ 1 (2007–2012) với schema PICS3 và BREADY ban đầu; (ii) Thế hệ 2 (2013–2017) với WBES Standardized chính thức; (iii) Thế hệ 3 (2018–2025) với Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, TGS Followup, EAP Core. Mặc dù ba thế hệ khác nhau, các biến cốt lõi (`d2` doanh thu, `l1` số lao động thường xuyên, `d3b`/`d3c` cường độ xuất khẩu, `b5` năm thành lập, `b2b` tỷ trọng sở hữu nước ngoài, `h1`/`h8` đổi mới và R&D, `b8` chứng nhận ISO, `c22b` website) duy trì tính nhất quán đủ tốt cho phân tích so sánh xuyên thế hệ.

**Hòa hợp**. Giao thức hòa hợp được mô tả chi tiết ở `thesis/08_p7_data_harmonization_protocol_vi.md` và thực thi qua pipeline Python (`wbes/03b_harmonize.py`). Quy trình gồm: (i) đọc 85 file `.dta` với fallback mã hoá Latin-1/CP1252 cho file lỗi UTF-8; (ii) crosswalk biến; (iii) loại các giá trị WBES "missing-by-design" ({-9,…,-1}); (iv) tính FSTS = `d3b + d3c` (xuất khẩu gián tiếp + trực tiếp); (v) winsorize log năng suất lao động trong từng cặp quốc gia × năm ở mức 1%/99%; (vi) loại doanh nghiệp có lao động ≤ 0 hoặc doanh thu ≤ 0.

**Sai số đo lường và caveat đơn vị tiền tệ**. Trong phiên bản hiện tại của pipeline, doanh thu (`d2`) chưa được chuyển sang USD PPP — nguyên nhân là tỷ giá PPP từng quốc gia × năm cần lấy từ World Development Indicators và tích hợp ở bước hậu xử lý (sẽ bổ sung ở phiên bản tiếp theo). Vì vậy, các bảng so sánh năng suất xuyên quốc gia trong chuyên đề này chỉ trình bày các **thước đo dispersion** (sd của log năng suất, tỷ số P90/P10, tỷ số P75/P25) – tất cả đều bất biến với đơn vị tiền tệ. Các thước đo cấu trúc và đổi mới sáng tạo là tỷ lệ phần trăm nên không bị ảnh hưởng bởi vấn đề đơn vị.

### 4.2 Thực trạng năng suất lao động — dispersion trong từng quốc gia

Năng suất lao động được đo bằng `log(d2/l1)` cho từng doanh nghiệp; sau đó tính các thước đo dispersion (độ lệch chuẩn của log, tỷ số P90/P10, tỷ số P75/P25) trong từng cặp quốc gia × năm; cuối cùng tính bình quân có trọng số (theo số doanh nghiệp) trong từng nhóm regime ICRV. Cách tiếp cận này tách bạch **dispersion nội bộ trong nước** (mức độ phân tán hiệu quả giữa các doanh nghiệp trong cùng quốc gia) khỏi hiệu ứng cross-country do đơn vị tiền tệ.

**Bảng 4.1**. *Dispersion năng suất lao động theo regime, bình quân có trọng số (n=84 cặp quốc gia × năm).*

| Nhóm regime | Số cặp quốc gia × năm | Số doanh nghiệp | sd log năng suất | Tỷ số P90/P10 | Tỷ số P75/P25 |
|---|---|---|---|---|---|
| Advanced | 10 | 4.289 | 1,00 | 13,3 | 3,6 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 17 | 33.986 | 1,37 | 37,6 | 5,7 |
| Frontier | 32 | 14.541 | 1,38 | 40,4 | 6,2 |
| SIDS | 2 | 196 | 1,35 | 42,1 | 5,6 |

*Nguồn: Tính toán của tác giả từ pool WBES 81.957 doanh nghiệp, 84 cặp quốc gia × năm.*

Bốn phát hiện chính từ Bảng 4.1:

*Thứ nhất*, dispersion năng suất **tăng đơn điệu** từ Advanced (sd=1,00) đến Frontier (sd=1,38), hơn 38 điểm phần trăm khi đo qua sd của log. Tỷ số P90/P10 — nghĩa là doanh nghiệp ở phân vị 90% có năng suất gấp bao nhiêu lần doanh nghiệp ở phân vị 10% trong cùng quốc gia — tăng từ 13,3 lần ở Advanced lên 40,4 lần ở Frontier. Pattern này khẳng định mạnh **hypothesis misallocation** của Hsieh & Klenow (2009, 2014): các nền kinh tế có thể chế chưa hoàn thiện không phân bổ vốn và lao động hiệu quả tới những doanh nghiệp năng suất cao, dẫn đến dispersion lớn ngay trong cùng quốc gia.

*Thứ hai*, SIDS (Vanuatu) có dispersion gần với Frontier (sd=1,35; P90/P10=42,1) — phù hợp với đặc tính thể chế hạn chế của các nền kinh tế đảo nhỏ. Tuy nhiên, mẫu nhỏ (n=196 doanh nghiệp, 2 cặp quốc gia × năm) khiến phát hiện này cần thận trọng và cần bổ sung dữ liệu của Fiji, Samoa, Tonga, Solomon Islands, PNG ở phiên bản tiếp theo.

*Thứ ba*, tỷ số P75/P25 (đo dispersion ở phần trung tâm phân phối) cũng tăng đơn điệu từ 3,6 (Advanced) lên 6,2 (Frontier) — chứng tỏ dị biệt năng suất KHÔNG chỉ là chuyện đuôi (tail effects) mà là pattern hệ thống xuyên toàn bộ phân phối.

*Thứ tư*, sự đơn điệu đẹp đẽ của dispersion theo regime cung cấp **bằng chứng thực tiễn ban đầu cho hệ giả thuyết H5** (institutional moderation) trong Chuyên đề 2: chất lượng thể chế có gradient tác động lên dispersion hiệu quả, gợi ý rằng cùng mức quốc tế hóa có thể tạo ra các kết quả hiệu quả khác nhau trong các regime khác nhau.

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

Cường độ quốc tế hóa được đo bằng FSTS = (% xuất khẩu gián tiếp `d3b` + % xuất khẩu trực tiếp `d3c`) trên tổng doanh thu, theo định nghĩa chuẩn của Hsu et al. (2013). Doanh nghiệp được coi là "exporter" nếu FSTS > 0%. Tăng trưởng việc làm 3 năm tính bằng CAGR từ `l1` (lao động hiện tại) và `l2` (lao động 3 năm trước).

**Bảng 4.3**. *Cường độ quốc tế hóa, tỷ trọng exporter, tăng trưởng việc làm theo regime.*

| Nhóm regime | FSTS trung bình (%) | FSTS trung vị (%) | Exporter share (% doanh nghiệp) | Tăng trưởng việc làm CAGR 3 năm (%) |
|---|---|---|---|---|
| Advanced | 12,8 | 0,0 | 27,6 | 3,15 |
| Upper-middle | 10,3 | 0,0 | 21,7 | 4,25 |
| Emerging | 10,5 | 0,0 | 18,2 | 2,60 |
| Frontier | 10,3 | 0,0 | 15,7 | 3,73 |
| SIDS | 4,1 | 0,0 | 9,7 | 8,51 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng doanh nghiệp xuất khẩu giảm tuyến tính theo regime*: từ 27,6% ở Advanced xuống 9,7% ở SIDS (Vanuatu). Tuy nhiên, ngay cả ở Advanced, **chỉ một phần tư doanh nghiệp tham gia xuất khẩu** — điều này khẳng định stylized fact rằng quốc tế hóa là một hành vi phân cực (bipolar) ở mọi nhóm: phần lớn doanh nghiệp hoạt động thuần nội địa, một thiểu số tham gia thương mại quốc tế.

(2) *Trung vị FSTS bằng 0 ở mọi nhóm* — hơn 50% doanh nghiệp KHÔNG xuất khẩu gì. Trung bình FSTS ở Advanced (12,8%) cao hơn các nhóm khác chủ yếu do mức độ xuất khẩu cao của thiểu số doanh nghiệp xuất khẩu, không phải do nhiều doanh nghiệp tham gia xuất khẩu.

(3) *SIDS có exporter share thấp nhất (9,7%) bất chấp đặc điểm "kinh tế nhỏ và mở"* — phù hợp với phát hiện của tác giả về **forced internationalization penalty** ở Pacific SIDS (Đỗ & Phan, 2026 — P8 manuscript): doanh nghiệp xuất khẩu vì bắt buộc khi không có thị trường nội địa đủ lớn, không phải do lợi thế cạnh tranh; do đó tỷ trọng xuất khẩu thấp.

(4) *Tăng trưởng việc làm cao nhất ở SIDS (8,51%)* — bất ngờ; phản ánh đặc điểm tái thiết hậu COVID-19 của ngành du lịch Vanuatu (mẫu 2023) cùng với mở rộng dịch vụ địa phương. Pattern này không phản ánh động lực dài hạn mà mang tính cyclical.

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

Năm thước đo: tỷ lệ doanh nghiệp giới thiệu sản phẩm mới (`h1`), giới thiệu quy trình mới (`h2`), có chi R&D dương (`h8`), có chứng nhận ISO quốc tế (`b8`), có website riêng (`c22b`).

**Bảng 4.4**. *Tỷ lệ doanh nghiệp đổi mới sáng tạo và áp dụng số theo regime (% doanh nghiệp).*

| Nhóm regime | Sản phẩm mới (h1) | Quy trình mới (h2) | R&D dương (h8) | Chứng nhận ISO (b8) | Có website (c22b) |
|---|---|---|---|---|---|
| Advanced | 26,2 | 57,0 | 21,3 | 36,8 | 64,4 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 21,3 | 68,9 | 21,9 | 27,5 | 51,1 |
| Frontier | 22,1 | 69,1 | 13,6 | 23,2 | 37,5 |
| SIDS | 35,8 | 67,6 | 7,2 | 16,3 | 43,3 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Năm phát hiện:

(1) *Tỷ lệ chứng nhận ISO và có website giảm tuyến tính theo regime* — từ 36,8% ISO ở Advanced xuống 16,3% ở SIDS; từ 64,4% website ở Advanced xuống 37,5% ở Frontier. Hai chỉ số này phản ánh trực tiếp **năng lực thể chế hoá chất lượng và áp dụng số** — gợi ý mạnh sự cần thiết tách bạch TCI (chất lượng) và DAI (số hoá) trong mô hình của Chuyên đề 2.

(2) *Tỷ lệ R&D dương ổn định ở 21–22% xuyên Advanced – Upper-middle – Emerging* nhưng **sụt mạnh ở Frontier (13,6%) và SIDS (7,2%)**. Đây là chứng cứ thực tiễn cho **discontinuity** ở năng lực đổi mới giữa các nhóm thu nhập trung bình thấp và trung bình cao — phù hợp với hypothesis "absorptive capacity threshold" của Cohen & Levinthal (1990).

(3) *Tỷ lệ giới thiệu sản phẩm mới ở SIDS cao nhất (35,8%)* — bất ngờ; có thể phản ánh tính linh hoạt của doanh nghiệp nhỏ ở thị trường nội địa hẹp, nơi đổi mới sản phẩm là cách duy nhất để giành thị phần. Tuy nhiên, mẫu SIDS rất nhỏ (n=196 doanh nghiệp, chỉ Vanuatu) nên cần thận trọng diễn giải.

(4) *Tỷ lệ giới thiệu quy trình mới (h2) trên 65% ở mọi nhóm trừ Advanced (57%)* — pattern này phản ánh thực tế rằng **đổi mới quy trình là phổ biến** (incremental process change) ở các nền kinh tế đang phát triển, dễ thực hiện hơn đổi mới sản phẩm.

(5) *Khoảng cách Advanced – SIDS ở R&D là 14 điểm phần trăm; ở ISO là 21 điểm phần trăm; ở website là 21 điểm phần trăm* — gợi ý ba kênh khác nhau qua đó năng lực thể chế tác động lên hiệu quả: kênh R&D, kênh chứng nhận chất lượng, kênh hạ tầng số. Đây là cơ sở thực tiễn cho phân tích moderation của TCI vs DAI ở Chuyên đề 2.

### 4.5 Thực trạng cấu trúc doanh nghiệp

Cấu trúc doanh nghiệp được đo qua: tỷ trọng SME (định nghĩa < 100 lao động thường xuyên), tỷ trọng doanh nghiệp xuất khẩu (FSTS > 0), tỷ trọng doanh nghiệp có sở hữu nước ngoài ≥ 10% (`b2b ≥ 10`).

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo regime (%).*

| Nhóm regime | SME (<100 LĐ) | Exporter (>0%) | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,9 | 27,6 | 10,9 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 75,2 | 18,2 | 5,6 |
| Frontier | 84,4 | 15,7 | 6,6 |
| SIDS | 99,2 | 9,7 | 30,6 |

*Nguồn: Tính toán của tác giả từ pool WBES.*

Bốn phát hiện:

(1) *Tỷ trọng SME 75–99% ở mọi nhóm* — khẳng định stylized fact rằng SME chi phối tuyệt đại đa số số lượng doanh nghiệp châu Á (CIEM, 2023; ADB, 2024). SIDS có tỷ trọng SME 99,2% — gần như tất cả doanh nghiệp đều dưới 100 lao động.

(2) *Tỷ trọng doanh nghiệp xuất khẩu giảm tuyến tính từ Advanced (27,6%) xuống SIDS (9,7%)* — đã phân tích ở Mục 4.3.

(3) *Tỷ trọng FDI ≥ 10% có pattern phi tuyến đáng chú ý*: cao ở Advanced (10,9%) và Frontier (6,6%) — nhưng **cao bất thường ở SIDS (30,6%)**. Pattern SIDS phản ánh hai thực tế: (i) các doanh nghiệp lớn nhất ở Vanuatu (du lịch, viễn thông, vận tải biển) thường có vốn nước ngoài; (ii) khu vực doanh nghiệp tổng thể của SIDS rất nhỏ nên các doanh nghiệp FDI chiếm tỷ trọng tương đối lớn. Đây không phải dấu hiệu hấp dẫn FDI mạnh mà là đặc thù cấu trúc.

(4) *Tỷ trọng FDI ở Emerging (5,6%) thấp hơn Frontier (6,6%)* — bất ngờ so với kỳ vọng. Có thể do mẫu Emerging chứa Ấn Độ (n=18.657 doanh nghiệp, chiếm hơn nửa Emerging) với tỷ lệ FDI thấp do thị trường nội địa lớn; trong khi Frontier chứa các nước nhỏ phụ thuộc đầu tư khu vực (Cambodia, Lào nhận FDI Trung Quốc; Bangladesh nhận FDI dệt may).

### 4.6 Bức tranh thay đổi theo thời gian — so sánh ba giai đoạn

Pool dữ liệu được phân thành ba giai đoạn theo thế hệ schema: 2007–2012 (n=10.523 doanh nghiệp, chủ yếu Frontier và Emerging), 2013–2017 (n=20.215), 2018–2024 (n=51.219). Tính trung bình từng chỉ số trong từng giai đoạn và regime, sau đó tính độ chênh giữa giai đoạn cuối và giai đoạn đầu (Δ = giai đoạn 2018-2024 − giai đoạn 2007-2012, đơn vị điểm phần trăm).

**Bảng 4.6**. *Δ điểm phần trăm các chỉ số khi so sánh 2018–2024 với 2007–2012.*

| Nhóm regime | Δ Website | Δ Exporter | Δ FDI ≥10% | Δ R&D | Δ ISO | Δ Innov product |
|---|---|---|---|---|---|---|
| Advanced | n/a* | n/a* | n/a* | n/a* | n/a* | n/a* |
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5** | -25,4 | n/a* |
| Emerging | +20,6 | -6,6 | -10,3 | -39,2 | +2,4 | -23,8 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 | n/a* |
| SIDS | +42,9 | +11,3 | -10,0 | n/a* | -24,3 | n/a* |

*Nguồn: Tính toán của tác giả từ pool WBES.*

\* n/a: thiếu dữ liệu giai đoạn 2007–2012 cho regime đó (Advanced chưa có khảo sát WBES trước 2013; một số chỉ số như `h1` chưa được đo nhất quán ở schema cũ).

\** Upper-middle ở giai đoạn 2013–2017 chỉ có Trung Quốc 2012 (xếp vào 2007–2012) và Trung Quốc 2024 (xếp vào 2018–2024), nên các giá trị trung gian có biến động lớn do sự thay đổi mẫu chứ không phải biến động thực.

Năm phát hiện chính:

(1) *Số hoá tăng vọt ở Frontier, Emerging và SIDS*: tỷ lệ doanh nghiệp có website tăng 20–43 điểm phần trăm trong vòng 12 năm. Đây là hiện tượng "leapfrog" — các nền kinh tế chậm phát triển nhảy thẳng vào hạ tầng số (Banalieva & Dhanaraj, 2019; Verhoef et al., 2021). Pattern này KHÔNG xảy ra ở Upper-middle (Trung Quốc) nơi website đã phổ biến trước 2012.

(2) *R&D giảm mạnh ở Emerging và Frontier* (Δ = −39 và −19 điểm phần trăm). Bằng chứng này gây ngạc nhiên và cần được diễn giải thận trọng: phần lớn là do sự thay đổi cấu trúc mẫu (giai đoạn 2007–2012 chủ yếu là các nước có nhiều R&D như Indonesia, Mongolia; giai đoạn 2018–2024 mở rộng sang Ấn Độ với R&D thấp hơn). Khi NCS bổ sung weighting theo dân số doanh nghiệp ở phiên bản tiếp theo, pattern này có thể đảo dấu.

(3) *Tỷ trọng exporter giảm 6,6 điểm phần trăm ở Emerging* — phản ánh hiện tượng chuyển dịch về thị trường nội địa giai đoạn 2018–2024 (chiến tranh thương mại, COVID-19, đứt gãy chuỗi cung ứng). Pattern này có thể là tạm thời, cần theo dõi tiếp với dữ liệu 2025+.

(4) *Tăng tỷ lệ ISO ở Frontier (+18,5 điểm phần trăm)* — bằng chứng quá trình chính thức hoá doanh nghiệp ở các nước thu nhập thấp, có thể nhờ áp lực chuỗi giá trị toàn cầu yêu cầu chứng nhận chất lượng để được tham gia.

(5) *SIDS tăng exporter (+11,3 điểm phần trăm) và website (+42,9 điểm phần trăm) song hành với giảm ISO (−24,3 điểm phần trăm)* — pattern phức tạp, có thể phản ánh tái cấu trúc kinh tế Vanuatu hậu COVID với nhiều doanh nghiệp dịch vụ số mới gia nhập và một số doanh nghiệp công nghiệp truyền thống có ISO thoái lui.

### 4.7 Tổng hợp Chương 4

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **81.957 doanh nghiệp ở 35 nền kinh tế châu Á (84 cặp quốc gia × năm) trong giai đoạn 2009–2025** từ pool WBES sau hòa hợp. Bốn kết luận chính cho Chương 5 và 6:

(i) *Dispersion năng suất nội bộ trong nước tăng đơn điệu theo regime* (Advanced sd=1,00; Frontier sd=1,38; P90/P10 từ 13,3 lên 40,4 lần) — bằng chứng misallocation ở các nền kinh tế thể chế chưa hoàn thiện và là cơ sở thực tiễn cho hypothesis institutional moderation H5.

(ii) *Quốc tế hóa là hiện tượng phân cực ở mọi nhóm*: hơn 50% doanh nghiệp KHÔNG xuất khẩu (FSTS_median=0% xuyên năm regime); chỉ 10–28% doanh nghiệp tham gia xuất khẩu. SIDS có tỷ trọng exporter thấp nhất (9,7%) phù hợp với forced internationalization penalty.

(iii) *Năng lực thể chế hoá (ISO), năng lực số (website) và năng lực R&D có pattern khác nhau theo regime* — Advanced cao nhất về cả 3, Frontier có discontinuity ở R&D, SIDS cao bất thường về innovation sản phẩm. Ba pattern khác nhau khẳng định sự cần thiết tách bạch TCI và DAI trong mô hình Chuyên đề 2.

(iv) *Số hoá tăng vọt trong giai đoạn 2018–2024 ở Frontier, Emerging và SIDS* (+20–43 điểm phần trăm tỷ lệ website) — bằng chứng "leapfrog" hỗ trợ luận điểm tái định vị Uppsala cho kỷ nguyên số (Banalieva & Dhanaraj, 2019).

---

*Tiếp tục ở Phần 3 (Chương 5 — bốn tiểu cảnh điển hình; Chương 6 — yếu tố giải thích sơ bộ; Chương 7 — kết luận; Tài liệu tham khảo) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*
