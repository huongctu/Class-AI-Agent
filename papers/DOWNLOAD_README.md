# 3 Papers — Download Instructions

NCS Đỗ Thùy Hương — final manuscripts ready to print and submit.

## Quick Start (1 lệnh)

```bash
curl -sL https://raw.githubusercontent.com/huongctu/Class-AI-Agent/refs/heads/claude/asia-internationalization-performance-2cYgO/papers/decode_papers.sh | bash
```

Sau ~30 giây sẽ có thư mục `papers_decoded/` chứa 3 file Word:

| File | Paper | Size | Journal target |
|---|---|---|---|
| `Manuscript_R3_FIGFIXED.docx` | P3 Singapore (R3 final với Figure 1 fix) | 1.1 MB | Management International Review |
| `manuscript_v5_9_FIXED.docx` | P4 Vietnam (v5.9, 27 edits) | 2.0 MB | International Journal of Emerging Markets |
| `manuscript_v1_8_blinded.docx` | P5 China (v1.8) | 45 KB | Asia Pacific Journal of Management |

## Tại sao chia chunks?

GitHub MCP API có giới hạn payload ~1 MB/request. P3 (1.1 MB) và P4 (2.0 MB) lớn hơn → chia thành chunks base64 (P3: 2 chunks, P4: 4 chunks, P5: 1 chunk). Decoder script tự động fetch tất cả chunks và ghép lại thành file Word đầy đủ.

## Chi tiết các chunks

**P3 Singapore — `papers/p3-singapore/manuscript/`**:
- `Manuscript_R3_FIGFIXED.docx.b64.part00` (750 KB)
- `Manuscript_R3_FIGFIXED.docx.b64.part01` (735 KB)
- → ghép + base64 -d → `Manuscript_R3_FIGFIXED.docx` (1.1 MB)

**P4 Vietnam — `papers/p4-vietnam/manuscript/`**:
- `manuscript_v5_9_FIXED.docx.b64.part00` (900 KB)
- `manuscript_v5_9_FIXED.docx.b64.part01` (900 KB)
- `manuscript_v5_9_FIXED.docx.b64.part02` (900 KB)
- `manuscript_v5_9_FIXED.docx.b64.part03` (11 KB)
- → ghép + base64 -d → `manuscript_v5_9_FIXED.docx` (2.0 MB)

**P5 China — `papers/p5-china/manuscript/`**:
- `manuscript_v1_8_blinded.docx.b64` (60 KB)
- → base64 -d → `manuscript_v1_8_blinded.docx` (45 KB)

## Yêu cầu hệ thống

- `curl` (Linux/Mac có sẵn; Windows 10+ có sẵn từ 2018)
- `bash` (Linux/Mac có sẵn; Windows: dùng Git Bash hoặc WSL)
- `base64` (Linux/Mac có sẵn; Windows Git Bash có)

## Cách thủ công (nếu không có bash)

PowerShell trên Windows:

```powershell
$BASE = "https://raw.githubusercontent.com/huongctu/Class-AI-Agent/refs/heads/claude/asia-internationalization-performance-2cYgO"

# P3 Singapore
@("part00","part01") | ForEach-Object { Invoke-WebRequest "$BASE/papers/p3-singapore/manuscript/Manuscript_R3_FIGFIXED.docx.b64.$_" -OutFile "p3_$_.b64" }
Get-Content p3_part0*.b64 -Raw | Out-File -Encoding ASCII p3_combined.b64
[IO.File]::WriteAllBytes("Manuscript_R3_FIGFIXED.docx", [Convert]::FromBase64String((Get-Content p3_combined.b64 -Raw)))

# P4 Vietnam
@("part00","part01","part02","part03") | ForEach-Object { Invoke-WebRequest "$BASE/papers/p4-vietnam/manuscript/manuscript_v5_9_FIXED.docx.b64.$_" -OutFile "p4_$_.b64" }
Get-Content p4_part0*.b64 -Raw | Out-File -Encoding ASCII p4_combined.b64
[IO.File]::WriteAllBytes("manuscript_v5_9_FIXED.docx", [Convert]::FromBase64String((Get-Content p4_combined.b64 -Raw)))

# P5 China
Invoke-WebRequest "$BASE/papers/p5-china/manuscript/manuscript_v1_8_blinded.docx.b64" -OutFile "p5.b64"
[IO.File]::WriteAllBytes("manuscript_v1_8_blinded.docx", [Convert]::FromBase64String((Get-Content p5.b64 -Raw)))
```

## Verify integrity

Sau khi decode, kiểm tra:

```bash
file papers_decoded/*.docx
# Expected output: "Microsoft Word 2007+" cho cả 3 file
```

Nếu thấy "ASCII text" → decode failed → re-run script.

## Submission docs (cover letter, title page, response letters)

Ngoài manuscript, mỗi paper có thêm các file submission khác. Xem:
- P3: `papers/p3-singapore/` (Cover_Letter.docx, Title_Page.docx, P3_MIR_Submission_Package_20260502.zip)
- P4: source branch `claude/update-p4-draft-W6UKL/submission/` (cover_letter_ijoem.docx, response_letter_round2.docx)
- P5: `papers/p5-china/` (submission/00–05 markdown — compile bằng pandoc)
