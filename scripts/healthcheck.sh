#!/usr/bin/env bash
# Health check: reports disk, memory, load, and URL status.
# Exit 0 = healthy, 1 = something is wrong.
set -euo pipefail

DISK_LIMIT=80
STATUS=0

echo "== Disk =="
disk_used=$(df / --output=pcent | tail -1 | tr -dc '0-9')
echo "Root disk: ${disk_used}% used"
if (( disk_used > DISK_LIMIT )); then
  echo "FAIL: disk above ${DISK_LIMIT}%"
  STATUS=1
fi

echo "== Memory =="
free -m | awk 'NR==2 {printf "Used: %s MB / %s MB\n", $3, $2}'

echo "== Load =="
uptime

echo "== URLs =="
# TODO: read each line of urls.txt, curl it,
# print OK or FAIL with the HTTP code, and set STATUS=1 on failure.
# Hint: curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$url"

exit "$STATUS"