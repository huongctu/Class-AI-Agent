# Kết quả chính của P1 — Đỗ & Phan (2026, VEFR): Firm Performance Heterogeneity in Emerging Asia

*Nguồn*: Đỗ Thùy Hương & Phan Anh Tú (2026). "Firm Performance Heterogeneity in Emerging Asia: Evidence from World Bank Enterprise Surveys". *Vietnam Economic and Financial Review*. (đã xuất bản).

*Mục đích file này*: lưu trữ kết quả chính để trích dẫn trong luận án và CĐ1/CĐ2. **Không chỉnh sửa format của P1 — bản gốc đã xuất bản.**

---

## 1. Thông tin xuất bản

- **Tạp chí**: Vietnam Economic and Financial Review (VEFR)
- **Tác giả**: Đỗ Thùy Hương (NCS) và PGS.TS. Phan Anh Tú (corresponding author)
- **Đơn vị**: Trường Kinh tế, Đại học Cần Thơ
- **Trường khóa**: internationalization strategy; emerging markets

## 2. Khung dữ liệu

- **Pool**: 40.633 doanh nghiệp × 17 nền kinh tế châu Á mới nổi × giai đoạn 2009–2024
- **Nguồn**: World Bank Enterprise Surveys (WBES)
- **Phân nhóm vùng**:
  - **Greater China** (n=5.251): Trung Quốc, Hong Kong SAR, Mông Cổ (gồm cả Đông Á)
  - **ASEAN** (n=12.068): Việt Nam, Indonesia, Philippines, Malaysia, Thái Lan, Lào, Campuchia, Myanmar
  - **South Asia** (n=23.314): Ấn Độ, Bangladesh, Pakistan, Sri Lanka, Nepal, Bhutan

## 3. Khung lý thuyết

- **Resource-Based View** (Barney, 1991) — cho vấn đề firm capabilities
- **Institutional Theory** (North, 1990; Khanna & Palepu, 2010) — cho institutional voids
- **Substitution view** (Khanna & Palepu, 2010) — capability bù đắp institutional voids

## 4. Phương pháp

- **Phương pháp ước lượng**: OLS với sai số chuẩn vững HC3
- **5 mô hình lồng nhau** (M1 → M5):
  - M1: chỉ regional dummies
  - M2: thêm capability variables (technology adoption, quality certification, log employment)
  - M3: thêm obstacle index
  - M4: thêm SME × region interactions
  - M5: thêm capability × obstacle interactions (tested H5 substitution view)
- **Kiểm soát**: export intensity, survey year
- **Reference category**: ASEAN

## 5. **Thống kê mô tả theo vùng (Bảng 1)**

| Biến | Greater China | ASEAN | South Asia | Tổng |
|---|---|---|---|---|
| Năng suất TB (USD PPP/lao động) | **167.139** | 89.220 | 122.267 | 118.251 |
| Năng suất trung vị | 86.580 | 30.488 | 52.175 | 47.893 |
| Lao động (TB) | 109,7 | 69,7 | 83,9 | 83,0 |
| Technology adoption (%) | **62,0** | 46,2 | 52,5 | 51,9 |
| Quality certification (%) | **49,3** | 17,1 | 30,6 | 29,0 |
| Obstacle index (0–4) | 0,37 | 0,80 | **1,32** | 1,04 |
| **N** | **5.251** | **12.068** | **23.314** | **40.633** |

- Greater China premium so với ASEAN: **87%**; South Asia premium so với ASEAN: **37%**
- Phân phối năng suất lệch phải (typical của firm-level data)
- One-way ANOVA: F = 1.149,28; p < 0,001; η² = 0,054 (region giải thích 5,4% biến thiên)

## 6. **Kết quả hồi quy chính (Bảng 2)**

| Biến | M1 | M2 | M3 | M4 | M5 |
|---|---|---|---|---|---|
| Greater China | 0,990*** | 0,780*** | 0,745*** | 0,761*** | 0,769*** |
| South Asia | 0,506*** | 0,407*** | 0,445*** | 0,770*** | 0,459*** |
| Technology adoption | — | **0,409***** | 0,409*** | 0,426*** | 0,297*** |
| Quality certification | — | **0,322***** | 0,322*** | 0,357*** | 0,323*** |
| Log employment | — | 0,046*** | 0,046*** | — | 0,068*** |
| Obstacle index | — | — | **−0,076***** | −0,074*** | −0,133*** |
| SME × South Asia | — | — | — | **−0,390***** | — |
| **Obstacle × Technology** | — | — | — | — | **+0,110*** (DIGITAL SHIELD)** |
| **R²** | 0,054 | 0,105 | 0,107 | 0,113 | 0,113 |
| **N** | 40.633 | 40.633 | 40.633 | 40.633 | 40.633 |

*Note: \*\*\*p < 0,001. Reference: ASEAN. HC3 robust SE. Controls: export intensity, survey year.*

## 7. **6 phát hiện then chốt**

### H1 (Regional hierarchy): Được ủng hộ mạnh

Greater China vượt ASEAN **169,1%** (β = 0,990; p < 0,001); South Asia vượt ASEAN **65,9%** (β = 0,506; p < 0,001).

### H2 (Technology adoption → productivity): Được ủng hộ mạnh

Technology adoption liên quan với **+50,5%** năng suất (β = 0,409; p < 0,001). Sau khi thêm capability variables, R² tăng từ 0,054 → 0,105 (gần gấp đôi sức mạnh giải thích).

### H2a (Quality certification → productivity): Được ủng hộ mạnh

Quality certification liên quan với **+38,0%** năng suất (β = 0,322; p < 0,001).

### H3 (Business obstacles → productivity âm): Được ủng hộ

Mỗi đơn vị tăng obstacle giảm **7,3%** năng suất (β = −0,076; p < 0,001).

### H4 (Regional heterogeneity in SME gaps): Được ủng hộ

- South Asia SME × Region: **β = −0,390** (p < 0,001) — SME bất lợi lớn (33,3% gap)
- Greater China SME × Region: **β = +0,043** (n.s.) — SME gần như ngang bằng với large firms (6,9% gap, không có ý nghĩa)
- ASEAN: trung bình

### H5 (Digital shield effect): Được ủng hộ mạnh

**Technology × Obstacle interaction = +0,110 (p < 0,001)**

Cơ chế:
- Cho non-adopters: mỗi đơn vị obstacle giảm **−12,5%** năng suất
- Cho adopters: net penalty chỉ **−2,3%** năng suất
- **Technology adoption giảm 83% obstacle penalty**

Đây là bằng chứng ủng hộ substitution view (Khanna & Palepu, 2010): firm-level capabilities có thể bù đắp institutional voids.

## 8. Cơ chế hoạt động của digital shield

Theo thảo luận trong P1, technology adoption giúp firms bù đắp institutional weaknesses qua nhiều kênh:

1. **Digital communication tools** giúp firms ứng phó với hạ tầng viễn thông yếu kém
2. **Online platforms** giúp vượt qua information asymmetries trong các thị trường có weak contract enforcement
3. **Digital documentation systems** tiện cho navigation các quy định phức tạp

## 9. Hàm ý chính sách

### Đối với nhà hoạch định chính sách

- **Dual-track strategy**: đồng thời nâng cao firm capabilities + cải cách thể chế
- **Technology adoption programs**: digital literacy training, broadband infrastructure, e-government, ICT tax incentives
- **Institutional reforms**: để giảm obstacle index từ 1,32 (South Asia) về 0,37 (Greater China) → tăng ~7,3% năng suất/mỗi đơn vị obstacle giảm
- **Comprehensive SME support** (học từ Trung Quốc): SME financing, technology assistance, regulatory simplification, training

### Đối với nhà quản trị

- Technology adoption không phải chỉ là operational improvement mà là strategic resource
- Quality certification đặc biệt quan trọng cho firms tham gia GVC

## 10. Hạn chế chính (theo P1 tự thừa nhận)

1. Cross-sectional design → không xác định nhân quả
2. Technology measure bản cơ bản: chỉ đo email use — không capture ERP, cloud, big data
3. Obstacle measure dựa trên managers' subjective perceptions
4. Endogeneity concerns: high-productivity firms có thể self-select vào technology adoption (reverse causality)

---

## 11. Ánh xạ vào luận án và CĐ

### Vị trí tham chiếu trong CĐ1

- **§2.5 Khung lý thuyết**: trích dẫn "digital shield effect" từ P1 (Đỗ & Phan, 2026 — VEFR; β interaction = +0,110, p < 0,001)
- **§4.1 Pool data**: "P1 đã sử dụng pool 17 nước châu Á mới nổi với 40.633 firms; CD1 v2.6 mở rộng lên 47 nước/101.035 firms"
- **§5.4 Trung Quốc case**: tham chiếu Greater China premium 87% (P1, Bảng 1)
- **§7.1 Khoảng trống**: P1 là baseline, CĐ1 mở rộng coverage

### Vị trí tham chiếu trong CĐ2

- **§3.3 Bằng chứng cho châu Á**: "Châu Á mở rộng (17 nước → 47 nước): Đỗ & Phan (2026 — VEFR) — pattern 'digital shield effect'"
- **§5.5 H5 (institutional moderation)**: P1 là motivating evidence — technology adoption giảm 83% obstacle penalty
- **Bảng 4.2 (so sánh khung tham chiếu)**: P1 được đưa vào như một khung tham chiếu

### Vị trí tham chiếu trong luận án

- **Ch.2.4 Bối cảnh emerging Asia**: trích dẫn P1 với citation đầy đủ
- **Ch.4.1 Meta-analysis subgroup**: dùng P1 làm benchmark cho 17 nước
- **Ch.4.4 Boundary case**: trích dẫn digital shield effect khi thảo luận DAI moderation

---

## 12. Citation APA 7th

Đỗ, T. H., & Phan, A. T. (2026). Firm performance heterogeneity in emerging Asia: Evidence from World Bank Enterprise Surveys. *Vietnam Economic and Financial Review*. School of Economics, Can Tho University.
