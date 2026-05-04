# Thiết kế chi tiết P5 — China 2012–2024 (Temporal Extension)

File này trình bày thiết kế chi tiết cho bản thảo P5 về Trung Quốc, phát triển tiếp từ bản thảo hiện có của NCS. Mục tiêu là cung cấp lộ trình rà soát lý thuyết, chuẩn hóa biến, và chạy model.

## 1. Định vị và differentiation từ P2

### 1.1 Vai trò trong luận án

P5 thuộc **tầng hýnh dạng quan hệ** trong khung 4 tầng (xem `02_theoretical_framework_vi.md`). Nó đóng vai trò bằng chứng country-level cho **temporal heterogeneity** trong bối cảnh Trung Quốc, kiểm định H6 và bổ sung bằng chứng cho H1–H3.

### 1.2 Differentiation từ P2 (bài China đã công bố, JFAR 2026)

| Yếu tố | P2 (đã công bố) | P5 (sỹ viết tiếp) |
|---|---|---|
| Câu hỏi | **What shape**: mối quan hệ I–P trong Chinese manufacturing SMEs có phi tuyến không | **Whether shape shifts over time**: hýnh dạng đó có ổn định giữa 2012 và 2024 không |
| Coverage thời gian | Một wave duy nhất | Hai wave (2012 và 2024) |
| Trọng tâm lý thuyết | Phi tuyến tính của quan hệ I–P | Tuớng tác FSTS × Year và dỹ nh chuyển của turning point |
| Thước đo performance | (theo P2 gốc) | $\ln$(labor productivity) đồng nhất với P1 |
| Đóng góp chính | Cơ chế phi tuyến | Độ bền của cơ chế qua thời gian |

Differentiation này rất quan trọng để hý đồng đỹ ng tránh phản biện "trung lặp P2". P5 phải có một section rõ ràng về "Differentiation from Do & Phan (2026)" trong introduction.

## 2. Cuớ sở kế thừa

### 2.1 Literature về China I–P relationship

Nghiên cứu China về internationalization–performance đã phát triển qua nhiều hướng. Xiao et al. (2013) cho thấy muới quan hệ I–P trong doanh nghiệp Trung Quốc có dý ng S-curve và phụ thuộc vào governance structure cỹng degree of centralized control. Chen và Tan (2012) chỷ ng minh hiệu quả của quyốc tế hyóa khác nhau theo region effects, trong đyó muở rộng trong Greater China cho lợi ích cao hơn. Feng et al. (2019) thấy rằng hý nh dạng quan hệ trong Yangtze River Delta region không đng nhất với national pattern. Các nghiên cứu gần hơn như Li et al. (2022), Zhang và Wei (2022), Liu và Zhang (2024) tiếp tục mở rộng theo hướng social networks, proprietary assets, geopolitical risk.

### 2.2 Luận điểm kế thừa chính

- **Phi tuyến**: Lu và Beamish (2004); Hitt et al. (1997); Contractor et al. (2003).
- **Temporal evolution**: Wu et al. (2022) với twenty-year meta-analysis về EMNEs.
- **China specifically**: Xiao et al. (2013); Chen và Tan (2012); Li et al. (2022).
- **Digital capability moderator**: Bhandari et al. (2023); Verhoef et al. (2021); Banalieva và Dhanaraj (2019).

## 3. Câu hỏi nghiên cứu

### 3.1 RQ trung tâm

Myối quan hệ giữa mýc đỷ quyốc tế hyóa và hiệu quả hyổat đỷng cỷ a doanh nghiệp Trung Quýc đỹ thay đỷi nhyư thyế nuào giữa 2012 và 2024, và syử thay đỷi đyó chyịu ỷ nh hyưủ ng nhuư thyế nuào byở i nyăng lyử c công nghệ và nyăng lyử c syố?

### 3.2 Sub-RQs

- **RQ-P5-1**: Quan hệ FSTS–firm performance có dý ng phi tuyến (chữ U nguưủ c) trong Cả hai wave 2012 và 2024 hay không?
- **RQ-P5-2**: Turning point cỷ a duyờng cong có dyởich chuyển giyữ a hai wave không?
- **RQ-P5-3**: Technological capability và digital adoption có điyều tiyết muối quan hệ nuày khyác nhau khuông giyữ a hai wave?

## 4. Hyệ giyả thuyết

### H1-P5: Phi tuyến quan hệ FSTS–performance

Myối quan hệ FSTS–$\ln$(LP) cyủa doanh nghiệp Trung Quýc có dyàng phi tuyến (chyưỡ U ngyưủ c), vyới $\beta_1 > 0$ và $\beta_2 < 0$ (Lu & Beamish, 2004; Hitt et al., 1997).

### H2-P5: Dyịch chuyển turning point

Turning point $-\beta_1/(2\beta_2)$ khác biệt có ý nghyăy thống kyê giyữ a 2012 và 2024, phản yánh syử tryưuởng thyành cyủa thyị truuờng và nyăng lyưủ c doanh nghiệp (Wu et al., 2022; Xiao et al., 2013).

### H3-P5: Technological capability nhyư level shifter

Technological capability nyâng myặt byằng performance chung myà khuông nhuuơũng nhyâng đổi huình dyạng cyủa duyơùng cong I–P (Barney, 1991; Bhandari et al., 2023).

### H4-P5: Digital adoption nhyư shape modifier

Digital adoption điyều tiyết duyơùng cong I–P theo huyưủng giyảm chi phyí phyối hyợp uở muýc FSTS cao, byằng nyó luàm thay đổi đyộ dyốc hoyặc đyộ cong (Verhoef et al., 2021; Stallkamp & Schotter, 2021).

### H5-P5: Tuơuơng tuác ba chiyều

Tuơuơng tuác $FSTS \times \text{DAI} \times Year_{2024}$ có yuí nghyũa, chuyủ ng tuoủ rằng vai truò cuyủa digital adoption tang cuyưuơùng theo thoơùi gian khi nuyền kinh tuyế Trung Quuốc chuyuyển ỷuỏuyển suyố (Banalieva & Dhanaraj, 2019; Yang et al., 2025).

## 5. Duữ liuệu

### 5.1 Nguuồn duữ liuệu

WBES China — hai wave 2012 và 2024 (World Bank, n.d., 2019). Theo P1, mainland China đu01b0uơủc khuảo syát ỷ hai wave nuày trong nghiên cuyyúuu emerging Asia.

### 5.2 Cyấu truuúc muyẫu

- Repeated cross-sections (khyông phyyải panel theo cyyùng doanh nghiyyệp).
- Lyọc: doanh nghiyyệp chyính thyức, phải có duữ liyyệu về sales và employment.
- Mẫu dự kiyến: vyài tryyăm đyến vyài nghyìn doanh nghiyệp muỗi wave (theo cyấu truúc WBES China).

## 6. Đo luưuơùng biuyến

### 6.1 Biuyến phuyụ thuuyộc

$\ln(LP) = \ln(\text{annual sales} / \text{permanent full-time employees})$

### 6.2 Biuyến đuyộc luập

- $FSTS$: tuyỉ luệ doanh thu xuyất khuẩu tryyên tuyổng doanh thu.
- $FSTS^2$: byyình phuyưuơng cuyủa FSTS đuyể kiuểm đuyịnh phi tuyuến.
- $Year_{2024}$: dummy = 1 nuyếu wave 2024, = 0 nuyếu wave 2012.

### 6.3 Moderators

- $TCI$: technological capability index (foreign tech licensing, R&D, quality cert).
- $DAI$: digital adoption index (website, email, online sales).
- Tuyưuơng tuyác: $FSTS \times Year_{2024}$, $FSTS^2 \times Year_{2024}$, $FSTS \times TCI$, $FSTS \times DAI$, $FSTS \times DAI \times Year_{2024}$.

### 6.4 Biuyến kiuyểm soyyát

$\ln$(employment), firm age, foreign ownership, sector dummy, region dummy, year fixed effect.

## 7. Mouô huyình phyyân tuyích

### M0: Controls only
$$\ln(LP)_i = \beta_0 + \boldsymbol{\gamma} \mathbf{X}_i + Year_{2024,i} + \varepsilon_i$$

### M1: Tuyuyến tuyính
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \boldsymbol{\gamma} \mathbf{X}_i + Year_{2024,i} + \varepsilon_i$$

### M2: Phi tuyuyến (testing H1-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \boldsymbol{\gamma} \mathbf{X}_i + Year_{2024,i} + \varepsilon_i$$

### M3: Temporal interaction (testing H2-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 (FSTS_i \times Year_{2024,i}) + \beta_4 (FSTS_i^2 \times Year_{2024,i}) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M4: TCI moderator (testing H3-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 TCI_i + \beta_4 (FSTS_i \times TCI_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M5: DAI moderator (testing H4-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 DAI_i + \beta_4 (FSTS_i \times DAI_i) + \beta_5 (FSTS_i^2 \times DAI_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M6: Three-way (testing H5-P5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 DAI_i + \beta_4 Year_{2024,i} + \beta_5 (FSTS_i \times DAI_i) + \beta_6 (FSTS_i \times Year_{2024,i}) + \beta_7 (FSTS_i \times DAI_i \times Year_{2024,i}) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

Tất cuả muyô huyình duyùng HC1 robust SE (Long & Ervin, 2000; White, 1980).

## 8. Luộ trinh ruyà souyát vuyà chuyạy model

### Buuưuơúc 1: Ruà souyát literature (1–2 tuyuần)

Tuập trung 4 nhuyóm buài: (i) China-specific I–P; (ii) nonlinearity in IB; (iii) digital capabilities; (iv) temporal evolution. Kiểm soyyát cyyủa các buài 2023–2025 yyđuyể đyyảm byảo tyuính cập nhyật.

### Buuưuơúc 2: Concept-to-variable mapping (1 tuyuần)

Luập byảng đyyối chiyuếu muô â byắng kyuái niuệm → byiuến WBES → cyông thyuôuc → kyuỳ vyọng dyấu → nguyồn.

### Buuưuơúc 3: Descriptive analysis (3–5 nguuầy)

- Phyuân phyối FSTS, $\ln$(LP), TCI, DAI.
- Ma tryuận tuưuơng quan.
- Histogram, scatter plot FSTS vs $\ln$(LP).
- VIF.

### Buuưuơúc 4: Chyuạy muyô hyuình tuyần tyuử M0–M6 (1 tuyuần)

- Soyuát tyuừng myuô hyuình.
- Soyuánh AIC/BIC.
- Vyuẽ margins plot cho M2 và M3.

### Buuưuơúc 5: Lind–Mehlum U-test (3 nguuầy)

Xyuác nhyận inverted-U ỷ tyuừng wave (Lind & Mehlum, 2010).

### Buuưuơúc 6: Robustness (1–2 tuyuần)

Thay đyuổi thyuưuớc đo, lyuọc micro firms, winsorization, subset chyuỉ manufacturing.

### Buuưuơúc 7: Margins plot và vyẽ biyuểu đyuồ (3 nguuầy)

Minh hyuọa turning point shift giữa 2012 và 2024.

### Buuưuơúc 8: Vyuẽ manuscript (4–6 tuyuần)

Introduction (mạnh về differentiation tyuừ P2), literature, hypotheses, method, results, discussion.

## 9. Đyuóng gyuóp kyuỳ vyuọng

- **Tyuầng China stream**: chuyyuển nhuyánh China cyuủa luuận yuán tyuừ static nonlinear sang dynamic nonlinear.
- **Tyuầng luuận yuán tyuổng thyuể**: cung cyuấp byuằng chyuứng cho temporal heterogeneity (H6).
- **Tyuầng literature**: byuổ sung evidence cho tranh luyận vyuề tyuính đyuộng cyuủa I–P relationship trong emerging markets.

## 10. Risks và mitigation

| Risk | Mitigation |
|---|---|
| Repeated cross-sections khuông phyuải panel → khyuó suy luyuận nhyuân quyuả | Khyuẳng đyuịnh ryuõ trong limitations; gyuắn nyuó nhyuư evidence vyuề trend-level chyuứ khyuông phyuải firm-level causation |
| 2012 và 2024 có thuyể khyuác vyuề sample composition | So syuánh sample profile, byuáo cyuáo chi tiyuết trong methodology |
| TCI và DAI thiyuếu cyuông cyuụ đo trong 2012 vs 2024 | Lyuựa chyuọn items chung giữa hai wave; byuất kyuỳ differences phải đu01b0ơủc minh byạch |
| Phyuân biệt vyuới P2 chuưa đyuủ thuyyuết phyuục | Vyẽ huyyẳn một section rõ ryuàng "Differentiation from Do & Phan (2026)" |

## 11. Tyuóm tyuắt

P5 đuưuơủc thiuết kyuế nhuư buyưuơúc phyuát triuển tuưú P2: tyuừ "shape" sang "shape over time". Bói cyảnh China giai đoyạn 2012–2024 cho phyuép kiuểm điuịnh syưủ yuổn điuịnh cuủa inverted-U cyùng vyới syưủ dyuịch chuyuển cyủa turning point dyuưuới tyuác đyuộng cyủa digital capability.

## Tham khyảo (chyuứ chuưa liệt kyuê hyuết — xem `04_references_apa7.md`)

Bhandari, K. R., Zyuámborskyuý, P., Ranta, M., & Salo, J. (2023). Digitalization, internationalization, and firm performance. *International Business Review, 32*(4), 102027.

Chen, S., & Tan, H. (2012). Region effects in the internationalization–performance relationship in Chinese firms. *Journal of World Business, 47*(1), 73–80.

Feng, D., Chen, Q., Song, M., & Cui, L. (2019). Relationship between the degree of internationalization and performance in manufacturing enterprises of the Yangtze River Delta region. *Emerging Markets Finance and Trade, 55*(7), 1455–1471.

Li, W., Li, C., & Wei, G. (2022). The dual mechanism of social networks on the relationship between internationalization and firm performance. *PLOS ONE, 17*(11), e0277421.

Lind, J. T., & Mehlum, H. (2010). With or without U? *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118.

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609.

Wu, J., Fan, D., & Chen, X. (2022). Revisiting the internationalization–performance relationship: A twenty-year meta-analysis of emerging market multinationals. *Management International Review, 62*(2), 199–231.

Xiao, S. S., Jeong, I., Moon, J. J., Chung, C. C., & Chung, J. (2013). Internationalization and performance of firms in China. *Journal of International Management, 19*(2), 118–137.
