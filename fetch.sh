#!/usr/bin/env bash

# USAGE: ./fetch.sh 1 (or any other number up to 25).
# Place the session token in manually, do not commit.
# This is runnable without prefacing with sh or bash because of having run chmod +x fetch.sh

# strict mode: exit on error, error on unset vars, fail on any pipe command failure
set -euo pipefail

# Day: first arg; must be 1..25
DAY="${1:-}"
if [[ -z "$DAY" ]]; then
  echo "Usage: $0 <day 1-25> [out-file]" >&2
  exit 2
fi
if ! [[ "$DAY" =~ ^([1-9]|1[0-9]|2[0-5])$ ]]; then
  echo "Day must be an integer 1-25" >&2
  exit 2
fi

SESSION_TOKEN="none" # insert manually. this sucks, use the python script
UA="elbertvw (github.com/elbertvw) AoC2025 fetcher"
URL="https://adventofcode.com/2025/day/${DAY}/input"

# Zero‑pad day to two digits: %02d → width 2, pad with 0s on the left (1→01, 9→09)
DAY_PADDED=$(printf '%02d' "$DAY")

# Default output: DD/input (e.g., 01/input, 15/input). You can override with arg2.
OUT="${2:-${DAY_PADDED}/input}"
OUT_DIR=$(dirname -- "$OUT")

# Create the directory only if it does not already exist
if [[ ! -d "$OUT_DIR" ]]; then
  mkdir -p -- "$OUT_DIR"
fi

curl --fail --silent --show-error --compressed \
  -H "Cookie: session=$SESSION_TOKEN" \
  -A "$UA" \
  -o "$OUT" \
  "$URL"

echo "Saved to $OUT"