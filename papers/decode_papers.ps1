# decode_papers.ps1 — Decode 6 papers from base64 chunks to .docx (Windows PowerShell)
# Usage: Mở PowerShell → cd <thư mục muốn lưu> → .\decode_papers.ps1
# Hoặc: irm <URL_này> | iex

$BASE = "https://raw.githubusercontent.com/huongctu/Class-AI-Agent/refs/heads/claude/asia-internationalization-performance-2cYgO"
$OUT = "papers_decoded"
New-Item -Path $OUT -ItemType Directory -Force | Out-Null
Set-Location $OUT

function Decode-Chunked {
    param($name, $url_path, $chunks)
    Write-Host "=== $name ===" -ForegroundColor Cyan
    $b64 = ""
    foreach ($i in $chunks) {
        $idx = "{0:D2}" -f $i
        Invoke-WebRequest -Uri "$BASE/$url_path.b64.part$idx" -OutFile "tmp_$idx.b64" -UseBasicParsing
        $b64 += (Get-Content "tmp_$idx.b64" -Raw).TrimEnd("`r","`n")
        Remove-Item "tmp_$idx.b64"
    }
    $bytes = [Convert]::FromBase64String($b64)
    $filename = $url_path.Split("/")[-1]
    [IO.File]::WriteAllBytes($filename, $bytes)
    Write-Host "  OK $filename ($($bytes.Length) bytes)" -ForegroundColor Green
}

function Decode-Single {
    param($name, $url_path)
    Write-Host "=== $name ===" -ForegroundColor Cyan
    Invoke-WebRequest -Uri "$BASE/$url_path.b64" -OutFile "tmp.b64" -UseBasicParsing
    $b64 = (Get-Content "tmp.b64" -Raw).TrimEnd("`r","`n")
    Remove-Item "tmp.b64"
    $bytes = [Convert]::FromBase64String($b64)
    $filename = $url_path.Split("/")[-1]
    [IO.File]::WriteAllBytes($filename, $bytes)
    Write-Host "  OK $filename ($($bytes.Length) bytes)" -ForegroundColor Green
}

Decode-Chunked "P3 Singapore (1.18 MB)" "papers/p3-singapore/manuscript/Manuscript_Blinded_MIR_2_revised.docx" 0..1
Decode-Chunked "P4 Vietnam BLINDED (2.0 MB)" "papers/p4-vietnam/manuscript/manuscript_blinded.docx" 0..3
Decode-Chunked "P4 Vietnam FULL (2.0 MB)" "papers/p4-vietnam/manuscript/manuscript_full_with_authors.docx" 0..3
Decode-Single "P5 China (45 KB)" "papers/p5-china/manuscript/manuscript_v1_8_blinded.docx"
Decode-Single "Luận án 5 chương (75 KB)" "dist/luan_an_5_chuong_v1.docx"
Decode-Single "P6 So sánh ICBEF vs UPDATED (17 KB)" "dist/p6_comparison_icbef_vs_updated.docx"

Write-Host ""
Write-Host "Done — 6 files ready in: $(Get-Location)" -ForegroundColor Yellow
Get-ChildItem *.docx | Format-Table Name, Length
