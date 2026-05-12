# Kết quả chính của P2 — Đỗ & Phan (2026, JFAR): Unveiling the impact of Chinese manufacturing SMEs' internationalization on performance

*Nguồn*: Đỗ Thùy Hương & Phan Anh Tú (2026). "Unveiling the impact of Chinese manufacturing SMEs' internationalization on performance". *Journal of Finance & Accounting Research*, No. 02 (39) - 2026, pp. 287-291. (đã xuất bản).

*Mục đích file này*: lưu trữ kết quả chính để trích dẫn trong luận án và CĐ1/CĐ2. **Không chỉnh sửa format của P2 — bản gốc đã xuất bản.**

---

## 1. Thông tin xuất bản

- **Tạp chí**: Journal of Finance & Accounting Research (JFAR), No. 02 (39) - 2026
- **Trang**: 287-291 (5 trang)
- **Tác giả**: PhD Candidate Đỗ Thùy Hương và Assoc.Prof.PhD Phan Anh Tú (corresponding author)
- **Đơn vị**: School of Economics, Can Tho University, Vietnam
- **Ngày nhận**: 27/01/2026; ngày phê duyệt: 28/03/2026
- **Từ khóa**: internationalization; export intensity; SME performance; working capital constraints; inverted-U relationship; Chinese manufacturing; emerging markets

## 2. Khung lý thuyết

P2 đóng góp **kết hợp lý thuyết mới**:

- **Resource-Based View (RBV)** (Barney, 1991): SMEs internationalization khai thác underutilized resources và đạt economies of scale
- **Working Capital Management (WCM) theory**: cơ chế đóng góp độc đáo của P2 — "Working Capital Trap"
- **Inverted-U logic** (Hitt et al., 1997; Qian et al., 2013)

### Phát hiện lý thuyết mới: "Working Capital Trap"

- Exporting mở rộng Cash Conversion Cycle (CCC) từ 30-45 ngày lên 75-90 ngày
- Manufacturing SMEs phải finance sản xuất, packaging, shipping trước khi receive foreign receivables
- Trong China với institutional voids và imperfect credit markets, SMEs không thể bridge liquidity gap
- Khi export intensity vượt critical threshold, firm đi vào **"Working Capital Trap"** — financial strain vượt qua scale benefits

## 3. Khung dữ liệu

- **Nguồn**: World Bank Enterprise Survey (WBES) China
- **Đợt**: 2 đợt — 2012 và 2024
- **Lọc**: manufacturing firms (ISIC codes 15-37)
- **Mẫu cuối**: **4.290 firm-year observations**
- **Schema**: cross-sectional analysis (không panel) với 2 cross-sections

## 4. Đặc tả mô hình

```
Productivity_i = β_0 + β_1·ExportIntensity_i + β_2·ExportIntensity²_i + γ·X_i + θ_j + τ_y + ε_i
```

Trong đó:
- `Productivity_i` = labour productivity (000 RMB/employee)
- `ExportIntensity_i` = % doanh thu xuất khẩu
- `X_i` = firm-specific controls (firm size, age, manager experience, digital capabilities, access to credit)
- `θ_j` = industry fixed effects (2-digit ISIC)
- `τ_y` = year fixed effect
- Standard errors clustered theo 2-digit ISIC industry classification
- **Inverted-U xác định khi**: β_1 > 0 và β_2 < 0
- **Optimal threshold**: ExportIntensity* = -β_1 / (2·β_2)

## 5. **Thống kê mô tả (Bảng 1)**

| Biến | Mean | SD | Min | Max |
|---|---|---|---|---|
| Labour Productivity (000 RMB) | **437,6** | 389,2 | 12,4 | 2.847,5 |
| Export Intensity (FSTS, %) | **23,7** | 28,4 | 0 | 100 |
| Firm Size (employees) | 284,5 | 512,8 | 5 | 5.823 |
| Firm Age (years) | 15,3 | 11,2 | 1 | 67 |
| Manager Experience (years) | 18,5 | 10,5 | 0 | 45 |
| Digital Capabilities (Index 0-1) | 0,673 | 0,469 | 0 | 1 |
| Access to Credit (Dummy) | 0,615 | 0,487 | 0 | 1 |

*Source: WBES China 2012, 2024*

- Trung bình export intensity 23,7% — SMEs chủ yếu nội địa; **18% có FSTS > 50%**
- Phân phối đầy đủ phổ từ thuần nội địa đến export-oriented

## 6. **Kết quả hồi quy chính (Bảng 2)**

| Biến | M1 (Linear) | M2 (Quadratic) | M3 (Full Controls) |
|---|---|---|---|
| Export Intensity (FSTS) | 0,952 (0,325) | **+1,704 (0,412)*** | +1,682 (0,418)*** |
| Export Intensity² (FSTS²) | — | **−1,781 (0,336)*** | −1,776 (0,339)*** |
| Digital Capabilities | 0,386 (0,078) | 0,384 (0,077) | 0,381 (0,078) |
| Manager Experience | 0,015 (0,005) | 0,015 (0,005) | 0,015 (0,005) |
| Firm Size (ln) | 0,108 (0,018) | 0,112 (0,018) | 0,113 (0,018) |
| **Observations** | 4.290 | 4.290 | 4.290 |
| **R²** | 0,062 | **0,079** | 0,081 |
| **Turning Point** | — | **47,8%** | 47,4% |

*Note: \*\*\*p < 0,001; \*\*p < 0,01; \*p < 0,05. Standard errors clustered by industry.*

## 7. **Phát hiện then chốt**

### H1 (Inverted-U cubic relationship): Được ủng hộ mạnh

- **β_1 = +1,704 (p < 0,001)** — export intensity tuyến tính dương
- **β_2 = −1,781 (p < 0,001)** — export intensity bình phương âm
- → **Inverted-U xác nhận**

**Optimal threshold = 47,8%** (95% CI: 40,9% — 54,1%)

### H1a (Upward Phase)

Ở mức export intensity thấp đến trung bình, internationalization tích cực với performance qua **economies of scale + learning by exporting**.

### H1b (Downward Phase)

Vượt qua threshold 47,8%, performance giảm do **"Working Capital Trap"** — chi phí financing extended cash cycle vượt qua scale benefits.

### "Safe Operating Zone" 30%-60% FSTS

Khuyến nghị chiến lược: SMEs nên targeting **40-50% export intensity** để maximize performance.

## 8. **Phân tích moderation (Bảng 3)**

| Biến | Main Effects | With Interactions |
|---|---|---|
| FSTS | 1,704 | 1,682 |
| FSTS² | −1,781 | −1,776 |
| Digital Capabilities (DDCI) | 0,384 | 0,381 |
| FSTS × DDCI | — | **0,021 (0,064) n.s.** |
| FSTS × Manager Exp | — | **0,003 (0,006) n.s.** |
| **R²** | 0,079 | 0,080 |
| **F-test for Interactions** | — | **0,34 (p = 0,89)** |

### Phát hiện quan trọng về moderation

Digital capabilities và manager experience đóng vai trò **"level-shifters"** chứ không **"slope-modifiers"**:
- Digital capabilities (DDCI): tăng productivity đồng đều (β = 0,384), không thay đổi 47,8% threshold
- Manager experience: tương tự
- Hàm ý: Digital tools enhance operational efficiency NHƯ 0không resolve structural credit-lag issues inherent in high-intensity exporting

## 9. **Robustness: Alternative performance metrics (Bảng 5)**

| Biến phụ thuộc | Turning Point | 95% CI | Inverted-U Confirmed? |
|---|---|---|---|
| **Labour Productivity** | **47,8%** | [40,9%; 54,1%] | YES |
| Return on Assets | 44,2% | [37,8%; 50,6%] | YES |
| Sales Growth | 50,1% | [43,5%; 56,8%] | YES |

Cả ba metrics đều tập trung trong dải 44%-50% — củng cố "Safe Zone" 30-60%.

## 10. **Temporal stability 2012 vs 2024 (Bảng 4)**

| Biến | 2012 Subsample | 2024 Subsample | Difference (p-value) |
|---|---|---|---|
| FSTS Coefficient | 1,598 (0,458) | 1,789 (0,472) | 0,412 (n.s.) |
| FSTS² Coefficient | −1,647 (0,381) | −1,933 (0,395) | 0,346 (n.s.) |
| **Optimal Threshold** | **48,6%** | **46,3%** | **0,327 (Stable)** |
| Mean Productivity | 261,3 | 439,8 | < 0,001 |
| Observations | 2.136 | 2.154 | — |

### Phát hiện then chốt về temporal stability

- **Productivity tăng 68,3%** từ 2012 đến 2024 (mean 261,3 → 439,8)
- **Optimal threshold vẫn ổn định** ~47-48% qua 12 năm (48,6% → 46,3%, không có ý nghĩa thay đổi)
- **Inverted-U formation bảo toàn**

→ **47,8% threshold là cấu trúc structural feature của SME financial environment ở China, không phải transitory market phenomenon**

## 11. Gender parity (Hình 2)

- Female manager coefficient: **β = −0,070 (p > 0,10)** — không có ý nghĩa
- Mean productivity diff: −0,07 thousand RMB (variation 0,02%) — ngắtnghĩa
- Cả male và female managers đều peak ở 47-48% FSTS
- → **Gender parity in I-P trajectory được xác nhận**

## 12. Hàm ý chính sách

### Đối với nhà quản trị SMEs

- **Theo đuổi "balanced internationalization"** với target FSTS 40-50%
- Ưu tiên working capital management: thiết lập favourable payment terms với export buyers
- Phát triển trade finance: letters of credit, receivables factoring
- Leverage digital technologies để giảm operational inefficiencies

### Đối với nhà hoạch định chính sách

- Export promotion policies nên nhấn mạnh **financial infrastructure support**:
  - Trade finance facilities
  - Receivables factoring marketplaces
  - Supply chain finance platforms
- Target highly internationalized firms (>60% FSTS) — nơi working capital constraints ràng buộc mạnh nhất
- Digital infrastructure investment tăng productivity đồng đều nhưng KHÔNG resolve working capital constraints inherent trong cross-border transactions

## 13. Hạn chế chính (theo P2 tự thừa nhận)

1. Cross-sectional design → không xác định nhân quả đầy đủ
2. Mẫu chỉ manufacturing SMEs trong một quốc gia → hạn chế generalizability
3. Chỉ đo direct exports → underestimate firms' total international exposure (qua intermediaries)
4. Working capital mechanism còn somewhat indirect — thiếu direct measures of cash conversion cycles

---

## 14. Ánh xạ vào luận án và CĐ

### Vị trí tham chiếu trong CĐ1

- **§5.4 Trung Quốc (large emerging — chuyển đổi)**: trích dẫn cubic inverted-U với optimal threshold 47,8% FSTS (Đỗ & Phan, 2026 — JFAR)
- **§7.1 Khoảng trống**: P2 cung cấp baseline cubic cho temporal heterogeneity test

### Vị trí tham chiếu trong CĐ2

- **§3.1 Năm dạng hàm**: "S-curve / Cubic (Lu & Beamish, 2004; Contractor et al., 2003; Đỗ & Phan, 2026 — JFAR)— được xác nhận bằng cubic specification ở China với turning point ~47,8% FSTS"
- **§3.3 Trung Quoc evidence**: trích dẫn "Đỗ & Phan (2026 — JFAR) — cubic inverted-U với turning point ~47,8% FSTS"
- **§5.1 H1 (phi tuyến cubic)**: P2 là bằng chứng motivating cho hypothesis cubic
- **Bảng 4.2 (so sánh khung tham chiếu)**: thêm dòng cho P2

### Vị trí tham chiếu trong luận án

- **Ch.4.2 Trung Quốc (country-level)**: gắn citation đầy đủ đến số "~47,8% FSTS turning point" — (Đỗ & Phan, 2026 — JFAR)
- **Ch.4.5 Robustness — temporal heterogeneity**: P2 đã verify temporal stability 48,6% (2012) → 46,3% (2024) (n.s.) — cung cấp baseline cho China 2012–2024 evolution test

---

## 15. Đóng góp mới của P2 so với văn liệu

1. **WCM mechanism** thay vì traditional coordination cost mechanism (Hitt et al., 1997) — đóng góp lý thuyết mới
2. **Sharper threshold** 47,8% — cụ thể hơn "30-60% range" trong Marano et al. (2016)
3. **Temporal stability test** xác nhận 47,8% là structural feature
4. **Gender parity** — contradicts gender entrepreneurship literature
5. **Digital as level-shifter, not slope-modifier** — finding mới về digital capabilities
6. **Robustness across 3 metrics** — LP, ROA, Sales Growth all confirm

---

## 16. Citation APA 7th

Đỗ, T. H., & Phan, A. T. (2026). Unveiling the impact of Chinese manufacturing SMEs' internationalization on performance. *Journal of Finance & Accounting Research, No. 02 (39) - 2026*, 287–291. School of Economics, Can Tho University, Vietnam.
