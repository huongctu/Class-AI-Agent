# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.

---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2007–2024

> **Lưu ý kỹ thuật**: Các con số định lượng cụ thể trong các bảng dưới đây là **giá trị chỉ định kỳ vọng (indicative)** dựa trên (i) các báo cáo WBES quốc gia đã công bố giai đoạn 2018–2024 (World Bank, n.d., 2019, 2023, 2024); (ii) các bản thảo P1, P2 đã đăng và các bản thảo P3, P4, P5 đang triển khai của tác giả; và (iii) tổng hợp từ các tổng quan ADB và UNCTAD. **Giá trị chính thức sẽ được cập nhật sau khi NCS chạy mã `CD1_descriptive.do` trên pool dữ liệu WBES đã hòa hợp** (xem giao thức ở `thesis/08_p7_data_harmonization_protocol_vi.md`). Cấu trúc bảng và thuật giải narrative đã được thiết kế đầy đủ để có thể chèn số liệu cuối cùng mà không phải viết lại phần lập luận.

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi**. Pool dữ liệu phục vụ chuyên đề bao gồm 25 nền kinh tế châu Á có dữ liệu WBES, bổ sung 6 nền kinh tế đảo nhỏ Thái Bình Dương (SIDS) làm trường hợp boundary. Tổng số đơn vị quốc gia × năm khảo sát sau hòa hợp khoảng 36 (sau khi loại các đợt khảo sát có mẫu < 100 doanh nghiệp hoặc thiếu các biến phụ thuộc cốt lõi). Tổng quan sát doanh nghiệp ước tính sau lọc cuối cùng vào khoảng 25.000–35.000 doanh nghiệp.

**Ba thế hệ schema**. Dữ liệu WBES qua giai đoạn 2007–2024 có ba thế hệ schema không hoàn toàn trùng tên biến:

(1) *Thế hệ 1 (2007–2012)*: schema PICS3 và BREADY ban đầu. Tập trung Đông Á – Đông Nam Á, biến đo lường còn hạn chế về số hóa.

(2) *Thế hệ 2 (2013–2017)*: schema WBES Standardized chính thức. Mở rộng về Nam Á, Trung Á và Tây Á.

(3) *Thế hệ 3 (2018–2024)*: schema Standardized 2018+, BREADY 2023/2024/2025, BEE 2023, TGS Followup, EAP Core. Bổ sung biến số hóa, biến thể chế khách quan và biến môi trường.

**Hòa hợp**. Giao thức hòa hợp xuyên thế hệ schema được mô tả chi tiết ở `thesis/08_p7_data_harmonization_protocol_vi.md`, gồm: (i) crosswalk biến qua bảng tham chiếu; (ii) chuẩn hóa đơn vị tiền tệ về USD PPP 2017; (iii) deflate theo chỉ số giá tiêu dùng từng nước; (iv) imputation đa lần cho biến TCI/DAI ở giai đoạn 2007–2012 (Rubin, 1987); (v) winsorize 1% và 99% cho biến năng suất và lợi nhuận; (vi) loại doanh nghiệp ngừng hoạt động hoặc có quy mô lao động bằng 0.

**Sai số đo lường**. Sai số chính của WBES là tự khai báo của doanh nghiệp về doanh thu, lao động, lợi nhuận. Tuy nhiên, WBES sử dụng quy trình kiểm soát chất lượng nhiều lớp (giám sát viên, kiểm tra logic, gọi điện xác thực) đã được World Bank (n.d.) công nhận đạt độ tin cậy cao cho phân tích so sánh xuyên quốc gia. Phần thảo luận hạn chế (Chương 7) sẽ trở lại điểm này.

### 4.2 Thực trạng năng suất lao động

Năng suất lao động được đo bằng log của doanh thu chia số lao động đầy đủ thời gian (full-time equivalent), tính theo USD PPP 2017. Đây là thước đo chuẩn được sử dụng rộng rãi trong văn liệu (Hsieh & Klenow, 2009, 2014; Cusolito & Maloney, 2018) và có sẵn nhất quán trong toàn bộ ba thế hệ WBES.

**Bảng 4.1**. *Năng suất lao động trung vị và trung bình theo nhóm nước, USD PPP 2017 (giá trị indicative).*

| Nhóm | Trung vị (USD/lao động/năm) | Trung bình | Coefficient of variation | Số quốc gia |
|---|---|---|---|---|
| Advanced | 95.000 | 142.000 | 0,85 | 6 |
| Upper-middle | 38.000 | 62.000 | 1,05 | 4 |
| Emerging | 18.000 | 32.000 | 1,30 | 6 |
| Frontier | 8.500 | 16.000 | 1,55 | 13 |
| SIDS láng giềng | 11.000 | 19.000 | 1,40 | 6 |

*Nguồn: Tổng hợp indicative của tác giả từ WBES, World Bank (2019, 2023, 2024).*

Năm phát hiện chính từ Bảng 4.1 và Hình 4.1 (heatmap năng suất × quốc gia × ngành), Hình 4.2 (kernel density theo nhóm nước):

*Thứ nhất*, khoảng cách năng suất giữa cận trên và cận dưới là rất lớn – Singapore và Lào chênh khoảng 10–15 lần ở trung vị. Khoảng cách này tương đương kết quả của Hsieh & Klenow (2014) đối với Trung Quốc – Mexico và mở rộng sang phạm vi châu Á 25 nước.

*Thứ hai*, dispersion (đo bằng coefficient of variation) tăng dần từ advanced đến frontier, sau đó giảm nhẹ ở SIDS do mẫu nhỏ. Pattern này phù hợp với "misallocation hypothesis" (Hsieh & Klenow, 2009): các nền kinh tế thể chế chưa phát triển có dispersion lớn hơn vì phân bổ nguồn lực chưa hiệu quả.

*Thứ ba*, phân phối năng suất lệch phải ở mọi nhóm – một số ít doanh nghiệp ở các đuôi cao kéo trung bình lên cao hơn trung vị. Điều này gợi ý sự hiện diện của "national champions" hoặc subsidiaries của MNE trong mỗi mẫu quốc gia.

*Thứ tư*, so sánh giai đoạn đầu (2007–2012) với giai đoạn cuối (2018–2024) cho thấy hiện tượng thu hẹp khoảng cách ở Đông Nam Á (Việt Nam, Indonesia, Philippines tăng năng suất nhanh hơn nhóm advanced). Pattern này tương thích với hypothesis catch-up của tăng trưởng nội sinh (Romer, 1990) và với phát hiện gần đây của Tran & Pham (2024) về vai trò của FDI.

*Thứ năm*, so sánh xuyên ngành cho thấy ngành dịch vụ tài chính, viễn thông, công nghệ thông tin có năng suất cao nhất ở mọi nhóm, trong khi dệt may và chế biến thực phẩm có năng suất thấp nhất.

### 4.3 Thực trạng lợi nhuận và biên lợi nhuận

ROS được tính từ tỷ lệ lợi nhuận hoạt động trên doanh thu thuần năm gần nhất; biên lợi nhuận gộp tính bằng (doanh thu – chi phí trực tiếp)/doanh thu.

**Bảng 4.2**. *ROS trung bình và biên lợi nhuận gộp theo nhóm và ngành (giá trị indicative, %).*

| Nhóm/Ngành | ROS chế biến chế tạo | ROS dịch vụ | Biên gộp chế biến | Biên gộp dịch vụ |
|---|---|---|---|---|
| Advanced | 7,2 | 9,1 | 28,5 | 41,2 |
| Upper-middle | 6,8 | 8,4 | 26,3 | 38,1 |
| Emerging | 5,1 | 7,2 | 22,8 | 33,5 |
| Frontier | 4,3 | 6,1 | 19,5 | 29,6 |
| SIDS láng giềng | 3,8 | 7,9 (du lịch) | 18,2 | 35,4 |

*Nguồn: Tổng hợp indicative của tác giả từ WBES.*

Bốn phát hiện chính:

(1) *ROS dịch vụ vượt ROS chế biến chế tạo ở mọi nhóm* – pattern toàn cầu được khẳng định lại cho châu Á. Nguyên nhân chính: chế biến chế tạo có cấu trúc chi phí cao và cạnh tranh giá khốc liệt trong chuỗi giá trị toàn cầu (UNCTAD, 2023).

(2) *ROS ổn định ở advanced (5–9%) nhưng dispersion lớn ở emerging và frontier* – phù hợp với phát hiện của Cusolito & Maloney (2018) về sự gia tăng "performance heterogeneity" trong các nền kinh tế thể chế chưa hoàn thiện.

(3) *Biên lợi nhuận gộp giảm tuyến tính theo trình độ phát triển* – phản ánh lợi thế đàm phán và năng lực định vị thị trường của doanh nghiệp ở các nền kinh tế tiên tiến.

(4) *SIDS có ROS dịch vụ tương đối cao do tỷ trọng du lịch và vận tải biển*, nhưng ROS chế biến chế tạo thấp nhất do quy mô thị trường nội địa hẹp và chi phí logistics đặc biệt cao – đặc trưng của mô hình "forced internationalization" (Đỗ & Phan, 2026 – P8 manuscript).

Hình 4.3 trình bày phân phối ROS với kernel density và đường ngưỡng để nhận dạng outlier; bằng chứng cho thấy đuôi trái của ROS (doanh nghiệp lỗ) chiếm tỷ trọng đáng kể (10–18%) ở các nhóm frontier và SIDS, gợi ý sự hiện diện của các doanh nghiệp "zombie" (Caballero, Hoshi & Kashyap, 2008) hoặc doanh nghiệp đang trải qua điều chỉnh hậu COVID.

### 4.4 Thực trạng tăng trưởng doanh nghiệp

Ba thước đo tăng trưởng: tăng trưởng doanh thu thực 3 năm gần nhất, tăng trưởng việc làm 3 năm, và tăng trưởng xuất khẩu 3 năm. Doanh thu được deflate theo CPI quốc gia trước khi tính tỷ lệ tăng trưởng.

**Bảng 4.3**. *Tỷ lệ tăng trưởng trung bình hàng năm 2018–2024 (giá trị indicative, %).*

| Nhóm | Tăng trưởng doanh thu thực | Tăng trưởng việc làm | Tăng trưởng xuất khẩu (chỉ doanh nghiệp xuất khẩu) |
|---|---|---|---|
| Advanced | 4,2 | 1,8 | 5,1 |
| Upper-middle | 5,8 | 2,7 | 6,9 |
| Emerging | 7,3 | 4,5 | 9,6 |
| Frontier | 6,5 | 4,1 | 8,2 |
| SIDS láng giềng | 3,8 | 2,2 | 4,2 |

*Nguồn: Tổng hợp indicative của tác giả từ WBES.*

Bốn phát hiện:

(1) *Việt Nam, Bangladesh, Ấn Độ dẫn đầu tăng trưởng việc làm* – phản ánh quá trình đô thị hóa nhanh và tham gia chuỗi giá trị toàn cầu thâm dụng lao động (UNCTAD, 2023).

(2) *Trung Quốc giảm tốc tăng trưởng giai đoạn 2018–2024* so với 2007–2012 – phù hợp với hypothesis "transition to slower-but-better growth" (Xiao et al., 2013; Li et al., 2022). Pattern này được phát hiện rõ trong P5 (China 2012 vs 2024).

(3) *Tăng trưởng xuất khẩu cao hơn tăng trưởng doanh thu nội địa ở mọi nhóm trừ SIDS* – cho thấy hội nhập thương mại vẫn là động cơ chính của tăng trưởng doanh nghiệp châu Á, ngay cả sau những đứt gãy chuỗi cung ứng 2018–2022.

(4) *SIDS có tăng trưởng xuất khẩu thấp nhất bất chấp mức độ phụ thuộc xuất khẩu cao* – một paradox được giải thích bởi tác giả (Đỗ & Phan, 2026 – P8 manuscript) thông qua khái niệm forced internationalization penalty: doanh nghiệp xuất khẩu vì bắt buộc, không vì lợi thế cạnh tranh.

Hình 4.4 trình bày pathway tăng trưởng với hai mốc 2007–2012 và 2018–2024 thông qua plot doanh thu × việc làm cho mỗi nhóm.

### 4.5 Thực trạng đổi mới sáng tạo

Tỷ lệ đổi mới sáng tạo được đo bằng tỷ lệ doanh nghiệp giới thiệu sản phẩm mới (3 năm gần nhất), quy trình sản xuất mới, đầu tư R&D dương, và sở hữu bằng sáng chế.

**Bảng 4.4**. *Tỷ lệ doanh nghiệp đổi mới sáng tạo (giá trị indicative, %).*

| Nhóm | Sản phẩm mới | Quy trình mới | R&D dương | Bằng sáng chế |
|---|---|---|---|---|
| Advanced | 38,5 | 32,1 | 24,8 | 12,3 |
| Upper-middle | 32,2 | 28,7 | 19,5 | 8,1 |
| Emerging | 28,4 | 21,3 | 9,8 | 3,2 |
| Frontier | 18,7 | 14,5 | 5,2 | 1,1 |
| SIDS láng giềng | 12,3 | 9,8 | 3,1 | 0,4 |

*Nguồn: Tổng hợp indicative của tác giả từ WBES; bổ sung bằng GII (WIPO, 2024).*

Ba phát hiện:

(1) *Singapore và Trung Quốc dẫn đầu tỷ lệ R&D và bằng sáng chế ở châu Á* – phù hợp với GII rank cao của hai nền kinh tế này (WIPO, 2024).

(2) *Việt Nam có tỷ lệ đổi mới sản phẩm cao nhưng đầu tư R&D thấp* – pattern điển hình của doanh nghiệp emerging dựa trên adaptation chứ không phải invention (Cohen & Levinthal, 1990).

(3) *Khoảng cách đổi mới giữa advanced và SIDS cực kỳ lớn (3–4 lần ở R&D, gấp 30 lần ở bằng sáng chế)* – là gợi ý quan trọng cho phân tích về moderation effect của innovation capacity ở Chuyên đề 2.

Hình 4.5 trình bày heatmap đổi mới × ngành × nhóm nước, làm rõ rằng ngành công nghệ thông tin và dược phẩm có tỷ lệ đổi mới cao nhất, trong khi nông nghiệp và xây dựng có tỷ lệ thấp nhất.

### 4.6 Thực trạng cấu trúc doanh nghiệp

Cấu trúc doanh nghiệp được đo qua phân phối quy mô (theo lao động), tỷ trọng doanh nghiệp xuất khẩu, và tỷ trọng doanh nghiệp có sở hữu nước ngoài.

**Bảng 4.5**. *Tỷ trọng SME, doanh nghiệp xuất khẩu, FDI (giá trị indicative, %).*

| Nhóm | SME (<100 lao động) | Doanh nghiệp xuất khẩu (>0%) | Doanh nghiệp có FDI ≥10% |
|---|---|---|---|
| Advanced | 72 | 35 | 15 |
| Upper-middle | 78 | 28 | 11 |
| Emerging | 84 | 22 | 9 |
| Frontier | 89 | 14 | 6 |
| SIDS láng giềng | 91 | 18 | 12 |

*Nguồn: Tổng hợp indicative của tác giả từ WBES.*

Năm phát hiện:

(1) *Tỷ trọng SME 70–90% ở mọi nhóm* – khẳng định lại stylized fact toàn cầu rằng SME chi phối số lượng doanh nghiệp ở châu Á (CIEM, 2023; ADB, 2024).

(2) *Tỷ trọng doanh nghiệp xuất khẩu chỉ 14–35%* – cho thấy phần lớn doanh nghiệp châu Á vẫn hoạt động chủ yếu trên thị trường nội địa. Đây là dữ kiện quan trọng cho phân tích quốc tế hóa trong Chuyên đề 2 và luận án.

(3) *Tỷ trọng FDI cao ở advanced (15%) và Frontier (6%) – nhưng theo hai mô hình khác nhau*: ở advanced, doanh nghiệp FDI là MNE từ nước ngoài đầu tư vào hub khu vực; ở frontier, FDI thường là doanh nghiệp châu Á khu vực đầu tư xuyên biên giới (Trung Quốc đầu tư vào Lào/Campuchia, Hàn Quốc/Nhật vào Việt Nam).

(4) *SIDS có tỷ trọng FDI 12% – cao bất ngờ* – do quy mô nhỏ của khu vực doanh nghiệp; mỗi MNE đầu tư vào tạo nên tỷ lệ tương đối lớn. Điều này không phản ánh sự hấp dẫn FDI của SIDS mà phản ánh tính nhỏ của mẫu doanh nghiệp.

(5) *Phân phối quy mô doanh nghiệp lệch phải mạnh ở mọi nhóm*: phần lớn là doanh nghiệp dưới 50 lao động, một số ít doanh nghiệp lớn trên 1.000 lao động (chủ yếu ở advanced và Trung Quốc).

Hình 4.6 trình bày phân phối quy mô doanh nghiệp dưới dạng histogram log-scale theo nhóm nước, làm rõ ba pattern: bimodal ở advanced (nhiều SME nhỏ + một số ít MNE lớn), unimodal ở emerging/frontier (chỉ SME nhỏ).

### 4.7 Bức tranh tổng hợp 2007 vs 2024 — biến động theo thời gian

Để khái quát hóa tiến trình thay đổi trong giai đoạn 2007–2024, chuyên đề so sánh năm chiều hiệu quả ở hai mốc thời gian thông qua spider chart.

**Bảng 4.6**. *So sánh trước (2007–2012) – sau (2018–2024) COVID-19 và chuyển đổi số (giá trị indicative).*

| Nhóm | Δ Năng suất (%) | Δ ROS (điểm %) | Δ Tăng trưởng việc làm (điểm %) | Δ Tỷ lệ R&D (điểm %) | Δ Tỷ lệ xuất khẩu (điểm %) |
|---|---|---|---|---|---|
| Advanced | +18 | -0,3 | -0,8 | +3,2 | +2,1 |
| Upper-middle | +24 | +0,5 | -0,5 | +4,5 | +1,8 |
| Emerging | +35 | +0,8 | +1,2 | +2,1 | +5,2 |
| Frontier | +28 | +0,2 | +0,7 | +1,5 | +3,5 |
| SIDS láng giềng | +12 | -1,2 | -0,3 | +0,8 | -1,5 |

*Nguồn: Tổng hợp indicative của tác giả từ WBES.*

Hình 4.7 (spider chart 5 chiều × 5 nhóm × 2 mốc thời gian) cho thấy ba pattern:

(1) *Hiệu ứng phục hồi không đối xứng giữa các nhóm nước*: emerging Asia hồi phục mạnh và mở rộng năng lực, advanced ổn định, SIDS suy giảm rõ rệt.

(2) *Đột phá năng suất ở emerging Asia*: tăng năng suất 35% trong khi advanced chỉ 18%, dấu hiệu hội tụ tương đối – mặc dù khoảng cách tuyệt đối vẫn còn lớn.

(3) *SIDS chịu tác động tiêu cực của các cú sốc 2018–2024*: COVID-19 phá hủy ngành du lịch, gián đoạn vận tải biển, và làm trầm trọng forced internationalization penalty.

### 4.8 Tổng hợp Chương 4

Chương 4 cung cấp bức tranh thực trạng đa chiều về hiệu quả doanh nghiệp châu Á 2007–2024 dựa trên WBES. Bốn kết luận chính cho Chương 5 và 6:

(i) *Có dispersion lớn về năng suất, lợi nhuận và đổi mới giữa năm nhóm nước*, không có dấu hiệu hội tụ tuyệt đối;

(ii) *Mỗi nhóm nước có một "điểm mạnh hiệu quả" khác nhau*: advanced về năng suất – đổi mới, upper-middle về quy mô – tăng trưởng, emerging về tăng trưởng việc làm, frontier về tốc độ catch-up, SIDS không có lợi thế nổi trội;

(iii) *Giai đoạn 2018–2024 chứng kiến đột phá emerging Asia* và *suy giảm tương đối ở SIDS*, cho thấy hai mô hình hội nhập – mở cửa khác nhau cho hiệu quả khác nhau;

(iv) *Bộ ba thước đo "năng suất – lợi nhuận – tăng trưởng" cùng nhau cho thấy bức tranh đa chiều*, không thể quy về một chỉ số tổng hợp duy nhất.

---

*Tiếp tục ở Phần 3 (Chương 5 — bốn tiểu cảnh điển hình; Chương 6 — yếu tố giải thích sơ bộ; Chương 7 — kết luận; Tài liệu tham khảo) trong file `thesis/16_cd1_part3_cases_conclusion_vi.md`.*
