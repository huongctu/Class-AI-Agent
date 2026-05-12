# Thiết kế chi tiết P5 — China 2012–2024 (Temporal Extension)

File này trình bày thiết kế chi tiết cho bản thảo P5 về Trung Quốc, phát triển tiếp từ bản thảo hiện có của NCS. Mục tiêu là cung cấp lộ trình rà soát lý thuyết, chuẩn hóa biến, và chạy model.

## 1. Định vị và differentiation từ P2

### 1.1 Vai trò trong luận án

P5 thuộc **tầng hình dạng quan hệ** trong khung 4 tầng (xem `02_theoretical_framework_vi.md`). Nó đóng vai trò bằng chứng country-level cho **temporal heterogeneity** trong bối cảnh Trung Quốc, kiểm định H6 và bổ sung bằng chứng cho H1–H3.

### 1.2 Differentiation từ P2 (bài China đã công bố, JFAR 2026)

| Yếu tố | P2 (đã công bố) | P5 (sẽ viết tiếp) |
|---|---|---|
| Câu hỏi | **What shape**: mối quan hệ I–P trong Chinese manufacturing SMEs có phi tuyến không | **Whether shape shifts over time**: hình dạng đó có ổn định giữa 2012 và 2024 không |
| Coverage thời gian | Một wave duy nhất | Hai wave (2012 và 2024) |
| Trọng tâm lý thuyết | Phi tuyến tính của quan hệ I–P | Tương tác FSTS × Year và dịch chuyển của turning point |
| Thước đo performance | (theo P2 gốc) | $\ln$(labor productivity) đồng nhất với P1 |
| Đóng góp chính | Cơ chế phi tuyến | Độ bền của cơ chế qua thời gian |

Differentiation này rất quan trọng để hội đồng tránh phản biện "trùng lặp P2". P5 phải có một section rõ ràng về "Differentiation from Do & Phan (2026)" trong introduction.

## 2. Cơ sở kế thừa

### 2.1 Literature về China I–P relationship

Nghiên cứu China về internationalization–performance đã phát triển qua nhiều hướng. Xiao et al. (2013) cho thấy mối quan hệ I–P trong doanh nghiệp Trung Quốc có dạng S-curve và phụ thuộc vào governance structure cùng degree of centralized control. Chen và Tan (2012) chứng minh hiệu quả của quốc tế hóa khác nhau theo region effects, trong đó mở rộng trong Greater China cho lợi ích cao hơn. Feng et al. (2019) thấy rằng hình dạng quan hệ trong Yangtze River Delta region không đồng nhất với national pattern. Các nghiên cứu gần hơn như Li et al. (2022), Zhang và Wei (2022), Liu và Zhang (2024) tiếp tục mở rộng theo hướng social networks, proprietary assets, geopolitical risk.

### 2.2 Luận điểm kế thừa chính

- **Phi tuyến**: Lu và Beamish (2004); Hitt et al. (1997); Contractor et al. (2003).
- **Temporal evolution**: Wu et al. (2022) với twenty-year meta-analysis về EMNEs.
- **China specifically**: Xiao et al. (2013); Chen và Tan (2012); Li et al. (2022).
- **Digital capability moderator**: Bhandari et al. (2023); Verhoef et al. (2021); Banalieva và Dhanaraj (2019).

## 3. Câu hỏi nghiên cứu

### 3.1 RQ trung tâm

Mối quan hệ giữa mức độ quốc tế hóa và hiệu quả hoạt động của doanh nghiệp Trung Quốc đã thay đổi như thế nào giữa 2012 và 2024, và sự thay đổi đó chịu ảnh hưởng như thế nào bởi năng lực công nghệ và năng lực số?

### 3.2 Sub-RQs

- **RQ-P5-1**: Quan hệ FSTS–firm performance có dạng phi tuyến (chữ U ngược) trong cả hai wave 2012 và 2024 hay không?
- **RQ-P5-2**: Turning point của đường cong có dịch chuyển giữa hai wave không?
- **RQ-P5-3**: Technological capability và digital adoption có điều tiết mối quan hệ này khác nhau giữa hai wave không?

## 4. Hệ giả thuyết

### H1-P5: Phi tuyến quan hệ FSTS–performance

Mối quan hệ FSTS–$\ln$(LP) của doanh nghiệp Trung Quốc có dạng phi tuyến (chữ U ngược), với $\beta_1 > 0$ và $\beta_2 < 0$ (Lu & Beamish, 2004; Hitt et al., 1997).

### H2-P5: Dịch chuyển turning point

Turning point $-\beta_1/(2\beta_2)$ khác biệt có ý nghĩa thống kê giữa 2012 và 2024, phản ánh sự trưởng thành của thị trường và năng lực doanh nghiệp (Wu et al., 2022; Xiao et al., 2013).

### H3-P5: Technological capability như level shifter

Technological capability nâng mặt bằng performance chung mà không nhất thiết thay đổi hình dạng của đường cong I–P (Barney, 1991; Bhandari et al., 2023).

### H4-P5: Digital adoption như shape modifier

Digital adoption điều tiết đường cong I–P theo hướng giảm chi phí phối hợp ở mức FSTS cao, bằng cách làm thay đổi độ dốc hoặc độ cong (Verhoef et al., 2021; Stallkamp & Schotter, 2021).

### H5-P5: Tương tác ba chiều

Tương tác $FSTS \times \text{DAI} \times Year_{2024}$ có ý nghĩa, cho thấy vai trò của digital adoption tăng cường theo thời gian khi nền kinh tế Trung Quốc chuyển đổi số (Banalieva & Dhanaraj, 2019; Yang et al., 2025).

## 5. Dữ liệu

### 5.1 Nguồn dữ liệu

WBES China — hai wave 2012 và 2024 (World Bank, n.d., 2019). Theo P1, mainland China được khảo sát ở hai wave này trong nghiên cứu emerging Asia.

### 5.2 Cấu trúc mẫu

- Repeated cross-sections (không phải panel theo cùng doanh nghiệp).
- Lọc: doanh nghiệp chính thức, phải có dữ liệu về sales và employment.
- Mẫu dự kiến: vài trăm đến vài nghìn doanh nghiệp mỗi wave (theo cấu trúc WBES China).

## 6. Đo lường biến

### 6.1 Biến phụ thuộc

$\ln(LP) = \ln(\text{annual sales} / \text{permanent full-time employees})$

### 6.2 Biến độc lập

- $FSTS$: tỉ lệ doanh thu xuất khẩu trên tổng doanh thu.
- $FSTS^2$: bình phương của FSTS để kiểm định phi tuyến.
- $Year_{2024}$: dummy = 1 nếu wave 2024, = 0 nếu wave 2012.

### 6.3 Moderators

- $TCI$: technological capability index (foreign tech licensing, R&D, quality cert).
- $DAI$: digital adoption index (website, email, online sales).
- Tương tác: $FSTS \times Year_{2024}$, $FSTS^2 \times Year_{2024}$, $FSTS \times TCI$, $FSTS \times DAI$, $FSTS \times DAI \times Year_{2024}$.

### 6.4 Biến kiểm soát

$\ln$(employment), firm age, foreign ownership, sector dummy, region dummy, year fixed effect.

## 7. Mô hình phân tích

### M0: Controls only
$$\ln(LP)_i = \beta_0 + \boldsymbol{\gamma} \mathbf{X}_i + Year_{2024,i} + \varepsilon_i$$

### M1: Tuyến tính
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \boldsymbol{\gamma} \mathbf{X}_i + Year_{2024,i} + \varepsilon_i$$

### M2: Phi tuyến (testing H1-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \boldsymbol{\gamma} \mathbf{X}_i + Year_{2024,i} + \varepsilon_i$$

### M3: Temporal interaction (testing H2-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 (FSTS_i \times Year_{2024,i}) + \beta_4 (FSTS_i^2 \times Year_{2024,i}) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M4: TCI moderator (testing H3-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 TCI_i + \beta_4 (FSTS_i \times TCI_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M5: DAI moderator (testing H4-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 DAI_i + \beta_4 (FSTS_i \times DAI_i) + \beta_5 (FSTS_i^2 \times DAI_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M6: Three-way (testing H5-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 DAI_i + \beta_4 Year_{2024,i} + \beta_5 (FSTS_i \times DAI_i) + \beta_6 (FSTS_i \times Year_{2024,i}) + \beta_7 (FSTS_i \times DAI_i \times Year_{2024,i}) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

Tất cả mô hình dùng HC1 robust SE (Long & Ervin, 2000; White, 1980).

## 8. Lộ trình rà soát và chạy model

### Bước 1: Rà soát literature (1–2 tuần)

Tập trung 4 nhóm bài: (i) China-specific I–P; (ii) nonlinearity in IB; (iii) digital capabilities; (iv) temporal evolution. Kiểm soát các bài 2023–2025 để đảm bảo tính cập nhật.

### Bước 2: Concept-to-variable mapping (1 tuần)

Lập bảng đối chiếu: khái niệm → biến WBES → công thức → kỳ vọng dấu → nguồn.

### Bước 3: Descriptive analysis (3–5 ngày)

- Phân phối FSTS, $\ln$(LP), TCI, DAI.
- Ma trận tương quan.
- Histogram, scatter plot FSTS vs $\ln$(LP).
- VIF.

### Bước 4: Chạy mô hình tuần tự M0–M6 (1 tuần)

- Soát từng mô hình.
- So sánh AIC/BIC.
- Vẽ margins plot cho M2 và M3.

### Bước 5: Lind–Mehlum U-test (3 ngày)

Xác nhận inverted-U ở từng wave (Lind & Mehlum, 2010).

### Bước 6: Robustness (1–2 tuần)

Thay đổi thước đo, lọc micro firms, winsorization, subset chỉ manufacturing.

### Bước 7: Margins plot và vẽ biểu đồ (3 ngày)

Minh họa turning point shift giữa 2012 và 2024.

### Bước 8: Viết manuscript (4–6 tuần)

Introduction (mạnh về differentiation từ P2), literature, hypotheses, method, results, discussion.

## 9. Đóng góp kỳ vọng

- **Tầng China stream**: chuyển nhánh China của luận án từ static nonlinear sang dynamic nonlinear.
- **Tầng luận án tổng thể**: cung cấp bằng chứng cho temporal heterogeneity (H6).
- **Tầng literature**: bổ sung evidence cho tranh luận về tính động của I–P relationship trong emerging markets.

## 10. Risks và mitigation

| Risk | Mitigation |
|---|---|
| Repeated cross-sections không phải panel → khó suy luận nhân quả | Khẳng định rõ trong limitations; gắn nó như evidence về trend-level chứ không phải firm-level causation |
| 2012 và 2024 có thể khác về sample composition | So sánh sample profile, báo cáo chi tiết trong methodology |
| TCI và DAI thiếu công cụ đo trong 2012 vs 2024 | Lựa chọn items chung giữa hai wave; bất kỳ differences phải được minh bạch |
| Phân biệt với P2 chưa đủ thuyết phục | Viết hẳn một section rõ ràng "Differentiation from Do & Phan (2026)" |

## 11. Tóm tắt

P5 được thiết kế như bước phát triển tự P2: từ "shape" sang "shape over time". Bối cảnh China giai đoạn 2012–2024 cho phép kiểm định sự ổn định của inverted-U cùng với sự dịch chuyển của turning point dưới tác động của digital capability.

## Tham khảo (chứ chưa liệt kê hết — xem `04_references_apa7.md`)

Bhandari, K. R., Zámborský, P., Ranta, M., & Salo, J. (2023). Digitalization, internationalization, and firm performance. *International Business Review, 32*(4), 102027.

Chen, S., & Tan, H. (2012). Region effects in the internationalization–performance relationship in Chinese firms. *Journal of World Business, 47*(1), 73–80.

Feng, D., Chen, Q., Song, M., & Cui, L. (2019). Relationship between the degree of internationalization and performance in manufacturing enterprises of the Yangtze River Delta region. *Emerging Markets Finance and Trade, 55*(7), 1455–1471.

Li, W., Li, C., & Wei, G. (2022). The dual mechanism of social networks on the relationship between internationalization and firm performance. *PLOS ONE, 17*(11), e0277421.

Lind, J. T., & Mehlum, H. (2010). With or without U? *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118.

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609.

Wu, J., Fan, D., & Chen, X. (2022). Revisiting the internationalization–performance relationship: A twenty-year meta-analysis of emerging market multinationals. *Management International Review, 62*(2), 199–231.

Xiao, S. S., Jeong, I., Moon, J. J., Chung, C. C., & Chung, J. (2013). Internationalization and performance of firms in China. *Journal of International Management, 19*(2), 118–137.
