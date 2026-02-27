#!/usr/bin/env bash
set -euo pipefail

URL="${URL:-http://localhost:8000/predict}"
DURATION="${DURATION:-30}"        # seconds
CONCURRENCY="${CONCURRENCY:-10}"  # workers
SLEEP="${SLEEP:-0.1}"             # delay between requests per worker

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

echo "Generating traffic: duration=${DURATION}s concurrency=${CONCURRENCY} sleep=${SLEEP}s"

end_time=$((SECONDS + DURATION))

worker () {
  local ok=0
  local fail=0
  while [ $SECONDS -lt $end_time ]; do
    if curl -sS -o /dev/null -w "%{http_code}" -X POST "$URL" \
      -H "Content-Type: application/json" \
      -d "$payload" | grep -q "^200$"; then
      ok=$((ok+1))
    else
      fail=$((fail+1))
    fi
    sleep "$SLEEP"
  done
  echo "worker ok=${ok} fail=${fail}"
}

pids=()
for i in $(seq 1 "$CONCURRENCY"); do
  worker &
  pids+=($!)
done

for pid in "${pids[@]}"; do
  wait "$pid"
done

echo "Done. Grafana: http://localhost:3000 (admin/admin)"