# Năng lực công nghệ, mức độ áp dụng số và quan hệ giữa quốc tế hóa với hiệu quả hoạt động kinh doanh: Bằng chứng cấp doanh nghiệp tại Singapore

*Bản tiếng Việt học thuật của bản thảo Singapore (P4 theo plan, file gốc `01_Manuscript_4.docx`).*

*Tác giả: Đỗ Thùy Hương; Người hướng dẫn: PGS.TS. Phan Anh Tú, Trường Đại học Cần Thơ.*

*Ngữ cảnh: bằng chứng country-level ASEAN benchmark trong nền kinh tế đã hoàn thiện hạ tầng số (Chương 4 Mục 4.2 luận án).*

---

## Tóm tắt

Nghiên cứu này khảo sát mối quan hệ giữa quốc tế hóa (internationalization) và hiệu quả hoạt động kinh doanh (firm performance) trong bối cảnh nền kinh tế đã đạt mức số hóa cao, đồng thời phân biệt rõ vai trò của *năng lực công nghệ* (Technological Capability Index – TCI) và *mức độ áp dụng số* (Digital Adoption Index – DAI) như hai cấu trúc khái niệm độc lập. Sử dụng dữ liệu vi mô từ Khảo sát doanh nghiệp World Bank Enterprise Survey (WBES) Singapore 2023 với 623 doanh nghiệp, nghiên cứu áp dụng mô hình hồi quy bình phương nhỏ nhất (OLS) với sai số chuẩn vững HC1, đặc tả đa thức bậc hai cho cường độ xuất khẩu (FSTS) và các dạng tương tác moderation.

Ba phát hiện chính nổi lên: (i) trong phạm vi cường độ xuất khẩu quan sát được, quan hệ giữa quốc tế hóa và năng suất lao động được đặc tả tốt nhất dưới dạng *chủ yếu dương với độ cong nhẹ* hơn là một đường chữ U ngược được nhận dạng chính thức — kiểm định Lind–Mehlum không bác bỏ tính đơn điệu (p = 0,303) và điểm uốn ước lượng (~82% FSTS) nằm trong vùng có rất ít quan sát; (ii) TCI có quan hệ dương đáng kể với năng suất lao động (β = 0,168, p < 0,001), trong khi không phát hiện vai trò moderation rõ rệt của TCI lên độ cong; (iii) DAI không cho thấy phần thưởng năng suất đồng nhất giữa các doanh nghiệp; thay vào đó, mối liên hệ DAI–năng suất trở nên dương rõ hơn ở các mức cường độ xuất khẩu cao, với tín hiệu rõ nhất tập trung ở đuôi xuất khẩu cao (β tương tác bậc hai FSTS² × DAI = 3,118; p = 0,005).

Kết hợp các phát hiện trên, nghiên cứu cung cấp bằng chứng nội bộ từ Singapore khẳng định cần phân biệt rõ ràng năng lực công nghệ (chiều sâu nội tại) khỏi áp dụng số nền tảng (giao diện và cơ chế giao dịch số), đồng thời cho thấy áp dụng số có thể vận hành như một *nguồn lực mở rộng quy mô có điều kiện* (conditional scaling resource) hơn là một lợi thế năng suất phổ quát.

**Từ khóa**: quan hệ quốc tế hóa–hiệu quả; áp dụng số; năng lực công nghệ; cường độ xuất khẩu; năng suất lao động; Singapore.

---

## 1. Giới thiệu

### 1.1 Bối cảnh và động cơ nghiên cứu

Singapore là bối cảnh có giá trị phân tích cao để xem xét lại quan hệ giữa quốc tế hóa và hiệu quả hoạt động kinh doanh (I–P relationship), bởi nền kinh tế này kết hợp mức độ trưởng thành số rất cao với sự không đồng nhất ở cấp doanh nghiệp về cường độ xuất khẩu. Văn liệu I–P kinh điển giải thích tính phi tuyến thông qua sự đánh đổi giữa lợi ích quy mô và học hỏi từ mở rộng quốc tế và chi phí điều phối tăng dần khi doanh nghiệp hoạt động trên nhiều thị trường, với chữ U ngược là dạng thực nghiệm phổ biến nhất (Marano và cộng sự, 2016). Tuy nhiên, phần lớn văn liệu này được phát triển trong các bối cảnh tiền số hoặc số chuyển tiếp, nơi điều kiện thể chế và hạ tầng khác biệt đáng kể so với các nền kinh tế đã hoàn thiện hạ tầng số (Peng, 2003; Peng và cộng sự, 2008).

Trong bối cảnh số trưởng thành, câu hỏi liên quan không đơn thuần là liệu các doanh nghiệp vẫn thể hiện chữ U ngược cổ điển hay không, mà là liệu mức độ trưởng thành số có làm thay đổi *phạm vi xuất khẩu* mà tại đó phần suy giảm bên phải của đường cong trở nên khả quan sát thực nghiệm hay không. Nếu hạ tầng số trưởng thành làm giảm ma sát giao tiếp, giao dịch và xử lý thông tin, thì cơ chế chi phí điều phối làm cơ sở cho chữ U ngược cổ điển có thể bị suy yếu, dịch chuyển hoặc đẩy về vùng có rất ít quan sát (Bharadwaj và cộng sự, 2013; Verhoef và cộng sự, 2021).

Động cơ thứ hai liên quan đến tính rõ ràng của khái niệm. Trong các bối cảnh số trưởng thành, doanh nghiệp có thể khác biệt không chỉ ở chiều sâu năng lực công nghệ nội tại bắt nguồn từ học hỏi, đổi mới và năng lực hấp thụ, mà còn ở mức độ áp dụng các giao diện số nền tảng và hệ thống cho phép giao dịch. Hai chiều này không nên gộp lại thành một cấu trúc khái niệm chung, bởi năng lực công nghệ phản ánh chiều sâu năng lực nội tại của doanh nghiệp dựa trên logic resource-based và absorptive-capacity (Barney, 1991; Cohen và Levinthal, 1990; Lall, 1992), trong khi mức độ áp dụng số phản ánh sự tham gia vào các giao dịch và giao diện được hỗ trợ bởi công nghệ số có thể phụ thuộc nhiều hơn vào hệ sinh thái số xung quanh (Bharadwaj và cộng sự, 2013; Verhoef và cộng sự, 2021).

### 1.2 Khoảng trống nghiên cứu

Ba khoảng trống thúc đẩy nghiên cứu này. *Thứ nhất*, các nghiên cứu trước thường gộp các đặc tính doanh nghiệp liên quan đến số hóa thành các cấu trúc khái niệm chung, làm khó phân biệt năng lực công nghệ nội tại của doanh nghiệp với các hình thức áp dụng số cơ bản hơn. Điều này quan trọng vì hai chiều ám chỉ các cơ chế lợi thế khác nhau: năng lực công nghệ liên quan đến học hỏi, đổi mới và chiều sâu hấp thụ trong nội bộ doanh nghiệp, trong khi áp dụng số nền tảng liên quan đến việc sử dụng các giao diện số và hệ thống cho phép giao dịch.

*Thứ hai*, mặc dù nghiên cứu về quốc tế hóa số đã tạo ra các tiến bộ khái niệm quan trọng, bằng chứng cấp doanh nghiệp vẫn còn hạn chế về cách áp dụng số cơ bản liên quan với cường độ xuất khẩu trong một môi trường thể chế đã đạt mức số hóa cao.

*Thứ ba*, mặc dù văn liệu phi tuyến I–P đã ghi nhận các pattern chữ U ngược rộng rãi, việc diễn giải các pattern như vậy trong bối cảnh số trưởng thành vẫn chưa được đặc tả đầy đủ.

### 1.3 Đóng góp của nghiên cứu

Nghiên cứu này có một đóng góp chính và hai đóng góp bổ trợ. Đóng góp chính là cung cấp bằng chứng cấp doanh nghiệp, nội bộ bối cảnh từ Singapore cho thấy phần suy giảm bên phải kinh điển của đường cong I–P *không được nhận dạng rõ ràng* trong phạm vi cường độ xuất khẩu mà phần lớn doanh nghiệp trong mẫu hoạt động. Theo nghĩa này, nghiên cứu *bổ sung điều kiện* hơn là phủ nhận văn liệu phi tuyến cổ điển: trong bối cảnh này, phương trình bậc hai khớp được diễn giải tốt hơn dưới dạng chủ yếu dương với độ cong nhẹ hơn là một chữ U ngược được thiết lập chính thức.

Đóng góp bổ trợ thứ nhất là làm rõ cấu trúc khái niệm: tách biệt năng lực công nghệ khỏi áp dụng số nền tảng, qua đó tách biệt chiều sâu năng lực nội tại của doanh nghiệp khỏi các giao diện và cơ chế giao dịch số nền tảng. Đóng góp bổ trợ thứ hai là về mặt thực chất: mối liên hệ DAI–năng suất là yếu trên phần lớn phân phối cường độ xuất khẩu và chỉ trở nên dương rõ ràng ở đuôi xuất khẩu cao, do đó áp dụng số nền tảng nên được hiểu như một *nguồn lực mở rộng quy mô có điều kiện* hơn là một phần thưởng năng suất đồng nhất.

---

## 2. Cơ sở lý thuyết và giả thuyết

### 2.1 Quan hệ giữa quốc tế hóa và hiệu quả

Văn liệu I–P đã sản sinh nhiều bằng chứng về các quan hệ phi tuyến giữa mức độ quốc tế hóa và hiệu quả doanh nghiệp. Hitt và cộng sự (1997) giới thiệu logic chữ U ngược: quốc tế hóa ban đầu mang lại lợi ích quy mô và học hỏi, nhưng ở các mức cường độ xuất khẩu cao, doanh nghiệp gặp giới hạn nhận thức và điều phối làm xói mòn lợi nhuận từ việc mở rộng tiếp. Contractor và cộng sự (2003) mở rộng logic này thành đường cong S ba giai đoạn, và Lu và Beamish (2004) tinh chỉnh chữ U ngược với chú ý đến quy mô doanh nghiệp và tuổi. Pattern phổ biến nhất trong văn liệu này là chữ U ngược với điểm uốn trong khoảng 30–60% tỷ lệ doanh thu xuất khẩu trên tổng doanh thu (FSTS) (Marano và cộng sự, 2016).

### 2.2 Hai cấu trúc khái niệm độc lập: TCI và DAI

Nghiên cứu này phân biệt rõ ràng *Technological Capability Index* (TCI) — neo trong truyền thống năng lực Lall–Cohen-Levinthal (Cohen và Levinthal, 1990; Lall, 1992) — với *Digital Adoption Index* (DAI) — neo trong truyền thống số hóa Bharadwaj–Verhoef (Bharadwaj và cộng sự, 2013; Verhoef và cộng sự, 2021).

Sự phân biệt này là cần thiết về lý thuyết vì hai cấu trúc khái niệm tham chiếu các lĩnh vực lợi thế doanh nghiệp khác nhau. TCI nắm bắt các kho năng lực nội tại liên quan đến đổi mới, học hỏi và hấp thụ công nghệ. DAI, ngược lại, nắm bắt việc tiếp nhận các giao diện số và cơ chế hỗ trợ giao dịch của doanh nghiệp, phản ánh một dạng lợi thế phụ thuộc vào hệ sinh thái số xung quanh nhiều hơn. Trong phân loại bốn cấp của Verhoef và cộng sự (2021), website (c22b) tương ứng nhất với Tier 1 (digitization), trong khi cường độ thanh toán điện tử bên khách hàng và bên nhà cung cấp (k33, k38) tương ứng với Tier 2 (digitalization). Chỉ số DAI tổng hợp do đó nắm bắt lớp số nền tảng làm cơ sở cho các năng lực số bậc cao hơn, nhưng không thể quan sát trực tiếp Tier 3 (tích hợp quy trình như ERP, CRM, chuỗi cung ứng số) hay Tier 4 (năng lực động số như triển khai AI, điều phối nền tảng).

### 2.3 Phát triển giả thuyết

**H1**. Năng lực công nghệ (TCI) có quan hệ dương với hiệu quả hoạt động doanh nghiệp tại Singapore.

**H2 (câu hỏi mở)**. Liệu TCI có làm thay đổi hình dạng của quan hệ I–P hay không được xử lý như một câu hỏi thực nghiệm mở và đánh giá trong đặc tả bổ sung, không được giả định trước.

**H3**. Mối liên hệ năng suất của áp dụng số (DAI) tại Singapore có điều kiện chứ không đồng nhất giữa các doanh nghiệp.

**H4**. Mối liên hệ giữa áp dụng số (DAI) và hiệu quả doanh nghiệp trở nên dương hơn ở các mức cường độ xuất khẩu cao tại Singapore.

---

## 3. Phương pháp nghiên cứu

### 3.1 Dữ liệu

Nghiên cứu sử dụng đợt khảo sát WBES Singapore 2023, là dữ liệu vi mô cấp doanh nghiệp gần nhất hiện có cho Singapore. Đợt 2023 áp dụng phương pháp luận B-READY, mở rộng module áp dụng số để bao gồm các mục về cường độ thanh toán điện tử. Sau khi loại bỏ các quan sát thiếu giá trị ở các biến trọng yếu, mẫu phân tích bao gồm 623 doanh nghiệp trên các ngành chính của nền kinh tế Singapore. Sản xuất chế tạo chiếm khoảng 31%, bán lẻ và dịch vụ khác 50%, và các ngành khác 19%. Mẫu chủ yếu định hướng nội địa: 18% doanh nghiệp báo cáo có xuất khẩu khác 0, và chỉ 3% vượt 50% FSTS.

### 3.2 Đo lường biến

*Biến phụ thuộc*: Hiệu quả doanh nghiệp được vận hành hóa như năng suất lao động, đo bằng logarit tự nhiên của doanh thu hằng năm chia cho số lao động toàn thời gian. Để giảm nhạy cảm với giá trị ngoại lai, biến phụ thuộc được winsorize tại bách phân vị 1 và 99.

*Biến độc lập trọng yếu*: FSTS được định nghĩa là tỷ lệ doanh thu hằng năm từ xuất khẩu trực tiếp, chuẩn hóa về khoảng [0,1]. FSTS được trung tâm hóa (mean-centered) trước khi bình phương để giảm đa cộng tuyến giữa hạng tử tuyến tính và bậc hai (Aiken và West, 1991).

*Tổ hợp TCI và DAI*: TCI và DAI được mô hình hóa như hai tổ hợp formative riêng biệt. TCI nắm bắt chiều sâu năng lực công nghệ nội tại thông qua liên kết công nghệ ngoài, đổi mới sản phẩm, nỗ lực R&D và chứng nhận chất lượng. DAI nắm bắt việc tiếp nhận giao diện số nền tảng và cơ chế hỗ trợ giao dịch thông qua hiện diện website, cường độ thanh toán điện tử bên khách hàng và bên nhà cung cấp.

*Biến kiểm soát*: Quy mô doanh nghiệp (logarit số lao động toàn thời gian), tuổi doanh nghiệp, sở hữu nước ngoài (≥10% vốn nước ngoài), và hiệu ứng cố định ngành rộng.

### 3.3 Chiến lược ước lượng

Phân tích thực nghiệm sử dụng OLS với sai số chuẩn vững HC1 cho heteroscedasticity (Long và Ervin, 2000). Các mô hình được ước lượng tuần tự: bắt đầu với đặc tả chỉ kiểm soát (M0), tiếp đến mô hình tuyến tính (M1), mô hình bậc hai (M2), mô hình tác động trực tiếp cho TCI (M5) và DAI (M6), mô hình kép (M7), và đặc tả đầy đủ với các hạng tử tương tác (M8). Theo khuyến nghị của Haans và cộng sự (2016), kiểm định Lind và Mehlum (2010) được áp dụng để đánh giá hình dạng bậc hai một cách chính thức.

---

## 4. Kết quả

### 4.1 Quan hệ I–P: chủ yếu đơn điệu với độ cong nhẹ

Trong đặc tả bậc hai cơ sở (M2), hạng tử tuyến tính FSTS dương và có ý nghĩa thống kê (β = 2,652, p < 0,001), trong khi hạng tử bậc hai âm và chỉ có ý nghĩa biên (β = −1,705, p < 0,1). Đường cong khớp ngụ ý điểm uốn ở đuôi trên của phân phối cường độ xuất khẩu, gần FSTS = 82% trên thang gốc, nhưng điểm này được xác định không chính xác và nằm trong vùng có rất ít quan sát. Bootstrap 5.000 lần lặp khôi phục hình dạng chữ U ngược trong 96,3% lần, nhưng khoảng tin cậy 95% percentile cho điểm uốn rộng [53%, 253%], và kiểm định Lind–Mehlum không bác bỏ tính đơn điệu (p = 0,303). Diễn giải phù hợp nhất là quan hệ toàn mẫu *chủ yếu dương với độ cong bậc hai nhẹ* trong phạm vi cường độ xuất khẩu quan sát được.

### 4.2 Kết quả TCI

Mô hình tác động trực tiếp cho TCI (M5) cho thấy TCI có quan hệ dương với năng suất lao động (β = 0,168, SE = 0,040, p < 0,001), với độ vừa khớp mô hình tăng từ R² = 0,178 (M2) lên R² = 0,199 (M5). Trong đặc tả TCI moderation bổ sung (M3), hệ số TCI trực tiếp vẫn dương và có ý nghĩa (β = 0,188, p < 0,001), nhưng các hạng tử tương tác với FSTS và FSTS² *không có ý nghĩa kết hợp*. Bằng chứng này phù hợp với cách diễn giải *intercept-dominant* về vai trò của TCI hơn là một kênh moderation rõ ràng đã được nhận dạng.

### 4.3 Kết quả DAI

Trong mô hình tác động trực tiếp cho DAI (M6), DAI có quan hệ dương với năng suất lao động (β = 0,104, SE = 0,038, p = 0,007). Tuy nhiên, khi TCI được bao gồm cùng DAI trong M7, hệ số DAI giảm xuống β = 0,077 và chỉ ở mức biên (p = 0,048). Sự suy giảm này quan trọng về mặt thực chất vì gợi ý rằng DAI không nên được diễn giải như một phần thưởng năng suất phổ quát lớn cho mọi doanh nghiệp.

Bằng chứng mạnh nhất cho DAI xuất hiện trong các đặc tả moderation. Trong mô hình đầy đủ (M8), hạng tử DAI trực tiếp nhỏ và không có ý nghĩa (β = 0,019, p = 0,705); tương tác tuyến tính với FSTS âm và biên (β = −1,177, p = 0,083); và **tương tác bậc hai dương và có ý nghĩa thống kê (β = 3,118, SE = 1,117, p = 0,005)**. M8 cũng tạo ra sức mạnh giải thích cao nhất trong các đặc tả chính, với R² = 0,211 và R² hiệu chỉnh = 0,196.

Diễn giải về mặt thực chất, các ước lượng này chỉ ra rằng *mối liên hệ năng suất của áp dụng số trở nên dương hơn ở các mức cường độ xuất khẩu cao*, với tín hiệu rõ nhất tập trung ở đuôi xuất khẩu cao thay vì phân bổ đồng nhất trên toàn mẫu.

### 4.4 Tác động biên của DAI dọc cường độ xuất khẩu

| FSTS | Tác động biên DAI | SE | p-value | KTC 95% |
|---|---|---|---|---|
| 0% (nội địa) | +0,080 | 0,040 | 0,045* | [+0,002, +0,158] |
| 5% | +0,015 | 0,047 | 0,752 | [-0,077, +0,106] |
| 10% | -0,035 | 0,069 | 0,616 | [-0,170, +0,101] |
| 50% | +0,131 | 0,186 | 0,481 | [-0,234, +0,496] |
| 70% | +0,588 | 0,262 | 0,025* | [+0,074, +1,102] |
| 100% | +1,742 | 0,573 | 0,002** | [+0,618, +2,865] |

Tại FSTS = 0, tác động biên của DAI nhỏ nhưng dương và có ý nghĩa biên (+0,080, p = 0,045), chỉ ra một mối liên hệ baseline khiêm tốn ở các doanh nghiệp thuần nội địa. Trên phạm vi xuất khẩu thấp và trung bình, tác động biên không phân biệt được với 0 về mặt thống kê. Ngược lại, tác động biên trở nên dương và có ý nghĩa thống kê ở các nhà xuất khẩu cường độ cao, đạt 0,588 tại FSTS = 70% và 1,742 tại FSTS = 100%. Pattern này hỗ trợ diễn giải DAI như *bổ sung mở rộng quy mô* (scale-enabling complement) mà mối liên hệ năng suất trở nên rõ ràng hơn khi doanh nghiệp đối mặt với nhu cầu điều phối và giao dịch xuyên biên giới đậm đặc hơn.

### 4.5 Kiểm định độ vững

Phân tích độ vững cho thấy suy luận cốt lõi về DAI moderation ổn định rộng rãi qua sáu đặc tả, mặc dù sức mạnh thống kê thay đổi theo lựa chọn đo lường và hạn chế mẫu. Khi DAI được rút gọn về thước đo chỉ website, kết quả moderation suy yếu. Khi mẫu loại trừ doanh nghiệp siêu nhỏ hoặc giới hạn ở SMEs, pattern moderation bậc hai dương vẫn hiển thị và thậm chí mạnh hơn ở một số trường hợp. Đặc biệt, kiểm định item-swap khẳng định ranh giới khái niệm: khi chỉ báo website (c22b) được chuyển từ DAI sang TCI, ý nghĩa kết hợp của khối DAI moderation sụp đổ (joint F giảm từ 4,56 [p = 0,011] xuống 1,88 [p = 0,154]).

---

## 5. Thảo luận

### 5.1 Hàm ý lý thuyết

Ba hàm ý lý thuyết được rút ra. *Thứ nhất*, kết quả TCI hỗ trợ cách diễn giải *capability-depth* về hiệu quả doanh nghiệp ở các doanh nghiệp đang quốc tế hóa. TCI có quan hệ dương với năng suất lao động theo cách ổn định hơn bất kỳ pattern moderation nào được nhận dạng trong thiết kế hiện tại. Diễn giải này phù hợp với truyền thống absorptive-capacity và technological-capability bằng cách nhấn mạnh học hỏi, đổi mới và hấp thụ công nghệ như các nguồn năng suất khác biệt nội tại của doanh nghiệp.

*Thứ hai*, bằng chứng *bổ sung điều kiện* hơn là phủ nhận văn liệu phi tuyến I–P kinh điển. Trong mẫu Singapore, phương trình bậc hai khớp thể hiện độ cong nhẹ, nhưng phần suy giảm bên phải không được nhận dạng chính thức trong phạm vi cường độ xuất khẩu mà phần lớn doanh nghiệp hoạt động. Nghiên cứu *làm sắc bén* việc diễn giải văn liệu phi tuyến thay vì khẳng định rằng một mặt cắt một quốc gia có thể tách biệt cơ chế đặc trưng bối cảnh khỏi đặc điểm thể chế cụ thể của Singapore.

*Thứ ba*, kết quả DAI gợi ý áp dụng số nền tảng được hiểu tốt hơn như *nguồn lực mở rộng quy mô có điều kiện* hơn là một phần thưởng năng suất doanh nghiệp đồng nhất. Trên phần lớn phân phối cường độ xuất khẩu quan sát được, mối liên hệ DAI yếu hoặc không phân biệt được về mặt thống kê, nhưng trở nên dương hơn ở đuôi xuất khẩu cao, nơi doanh nghiệp đối mặt với nhu cầu điều phối và giao dịch xuyên biên giới đậm đặc hơn. Pattern này phù hợp với ý tưởng rằng áp dụng số Tier 1–2 quan trọng nhất khi doanh nghiệp có đủ throughput quốc tế để sử dụng các giao diện số và hệ thống hỗ trợ giao dịch một cách thâm sâu.

### 5.2 Hàm ý quản trị

Đối với các doanh nghiệp tại Singapore và các bối cảnh hạ tầng số cao tương tự, các phát hiện gợi ý rằng đầu tư vào áp dụng số nền tảng có liên quan mạnh nhất với lợi thế năng suất khi doanh nghiệp đã hoạt động ở cường độ xuất khẩu tương đối cao. Trong các trường hợp như vậy, các giao diện số, hệ thống thanh toán và công cụ hỗ trợ giao dịch liên quan dường như vận hành như cơ chế mở rộng quy mô giúp doanh nghiệp điều phối khối lượng hoạt động xuyên biên giới lớn hơn một cách hiệu quả.

Đối với các doanh nghiệp tập trung ở thị trường nội địa hoặc cường độ xuất khẩu thấp, áp dụng số vẫn có thể có giá trị, nhưng các khác biệt năng suất dường như nhỏ hơn và ít đặc trưng hơn trong dữ liệu hiện tại. Quan trọng hơn, các phát hiện hàm ý nhà quản trị nên *tránh xem* năng lực công nghệ và áp dụng số như các hạng mục đầu tư có thể thay thế cho nhau. Đầu tư vào năng lực công nghệ dường như hỗ trợ một mặt bằng năng suất rộng hơn, trong khi đầu tư vào áp dụng số nền tảng trở nên liên quan hơn khi doanh nghiệp đối mặt với cường độ điều phối liên quan đến quốc tế hóa sâu hơn.

---

## 6. Kết luận

Nghiên cứu này xem xét lại quan hệ giữa quốc tế hóa và hiệu quả doanh nghiệp bằng cách phân biệt năng lực công nghệ khỏi áp dụng số nền tảng và khảo sát cách mỗi loại liên quan đến năng suất lao động ở các doanh nghiệp Singapore. Sử dụng dữ liệu vi mô WBES Singapore 2023, phân tích cho thấy năng lực công nghệ có quan hệ dương với năng suất, trong khi áp dụng số thể hiện mối liên hệ có điều kiện chỉ trở nên dương rõ hơn ở các mức cường độ xuất khẩu cao. Các phát hiện do đó hỗ trợ phân biệt giữa chiều sâu năng lực nội tại của doanh nghiệp và năng lực giao dịch số nền tảng, thay vì xem cả hai như các khía cạnh có thể thay thế của một cấu trúc khái niệm năng lực số duy nhất.

Nghiên cứu cũng *bổ sung điều kiện* cho việc diễn giải văn liệu phi tuyến I–P trong bối cảnh này. Trong phạm vi cường độ xuất khẩu quan sát được, pattern cơ sở được đặc tả tốt hơn dưới dạng chủ yếu dương với độ cong bậc hai nhẹ hơn là một chữ U ngược được nhận dạng chính thức. Đọc theo cách này, bằng chứng không phủ nhận văn liệu I–P đã thiết lập, cũng không thiết lập một điều kiện biên chung cho các nền kinh tế đã hoàn thiện hạ tầng số; thay vào đó, nó cung cấp bằng chứng nội bộ bối cảnh từ Singapore về cách logic phi tuyến kinh điển xuất hiện trong môi trường thể chế đã đạt mức số hóa cao, nơi phần lớn doanh nghiệp vẫn tập trung ở cường độ xuất khẩu thấp.

---

## 7. Hạn chế và hướng nghiên cứu tiếp theo

Ba hạn chế cảnh báo việc diễn giải các phát hiện. *Thứ nhất*, phân tích dựa trên một mặt cắt một quốc gia, do đó phạm vi nhận dạng là *liên kết* (associational) chứ không phải nhân quả. Các quan hệ quan sát được giữa năng lực công nghệ, áp dụng số, cường độ xuất khẩu và năng suất lao động có thể phản ánh nhân quả ngược, biến bị bỏ sót, hoặc lựa chọn theo năng suất vào xuất khẩu và áp dụng số.

*Thứ hai*, mẫu chứa đuôi phải mỏng của các nhà xuất khẩu cường độ cao. Phần lớn doanh nghiệp báo cáo không xuất khẩu, bách phân vị 75 của FSTS vẫn ở 0, và chỉ một phần nhỏ doanh nghiệp chiếm vùng xuất khẩu cao. Điểm uốn ngụ ý trong đặc tả bậc hai do đó nên được diễn giải như một đặc điểm mô tả hơn là một điểm uốn được nhận dạng cấu trúc.

*Thứ ba*, tác động áp dụng số ước lượng nên được diễn giải trong phạm vi đo lường của các chỉ báo có sẵn. DAI nắm bắt áp dụng số Tier 1–2 — hiện diện số và sử dụng giao dịch điện tử — chứ không phải năng lực tổ chức tích hợp số sâu hơn hay năng lực động số. Nghiên cứu tương lai nên khảo sát liệu pattern có điều kiện tương tự có xuất hiện ở các nền kinh tế số trưởng thành khác hay không và dưới các đo lường phong phú hơn nắm bắt tích hợp quy trình, số hóa tổ chức và năng lực số bậc cao trực tiếp hơn.

---

## Tài liệu tham khảo (chính)

- Aiken, L. S., & West, S. G. (1991). *Multiple regression: Testing and interpreting interactions*. Sage.
- Banalieva, E. R., & Dhanaraj, C. (2019). Internalization theory for the digital economy. *Journal of International Business Studies, 50*(8), 1372–1387.
- Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120.
- Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. *MIS Quarterly, 37*(2), 471–482.
- Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152.
- Contractor, F. J., Kundu, S. K., & Hsu, C.-C. (2003). A three-stage theory of international expansion. *Journal of International Business Studies, 34*(1), 5–18.
- Haans, R. F. J., Pieters, C., & He, Z.-L. (2016). Thinking about U: Theorizing and testing U- and inverted U-shaped relationships in strategy research. *Strategic Management Journal, 37*(7), 1177–1195.
- Hitt, M. A., Hoskisson, R. E., & Kim, H. (1997). International diversification: Effects on innovation and firm performance in product-diversified firms. *Academy of Management Journal, 40*(4), 767–798.
- Lall, S. (1992). Technological capabilities and industrialization. *World Development, 20*(2), 165–186.
- Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U-shaped relationship. *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118.
- Long, J. S., & Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. *American Statistician, 54*(3), 217–224.
- Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609.
- Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship: A meta-analytic review. *Journal of Management, 42*(5), 1075–1110.
- Peng, M. W. (2003). Institutional transitions and strategic choices. *Academy of Management Review, 28*(2), 275–296.
- Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.
- World Bank. (2024). *World Bank Enterprise Survey: Singapore 2023*. https://www.enterprisesurveys.org

*Danh mục đầy đủ tham khảo APA 7th xem trong bản tiếng Anh `p4_singapore_en_clean.md`.*
