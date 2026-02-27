#!/usr/bin/env bash
set -euo pipefail

URL="http://localhost:8000/predict"

payload='{
  "cement": 540.0,
  "blast_furnace_slag": 0.0,
  "fly_ash": 0.0,
  "water": 162.0,
  "superplasticizer": 2.5,
  "coarse_aggregate": 1040.0,
  "fine_aggregate": 676.0,
  "age": 28.0
}'

echo "Generating traffic..."

for i in $(seq 1 200); do
  curl -s -X POST "$URL" \
    -H "Content-Type: application/json" \
    -d "$payload" > /dev/null
  sleep 0.2
done

echo "Done. Open Grafana at http://localhost:3000 (admin/admin)"
