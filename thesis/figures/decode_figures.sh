#!/usr/bin/env bash
# decode_figures.sh — Decode base64-encoded PNG figures back to PNG files
# Usage: bash decode_figures.sh
# Run from thesis/figures/ directory after pulling .b64 files
set -e
cd "$(dirname "$0")"
for f in *.png.b64; do
    [ -e "$f" ] || continue
    out="${f%.b64}"
    base64 -d "$f" > "$out"
    echo "Decoded: $out"
done
echo "Done. PNG files ready for embed in DOCX."
