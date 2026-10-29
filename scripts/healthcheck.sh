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
while read -r url; do
  [[ -z "$url" ]] && continue   # skip blank lines

  code=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$url" || true)

  if (( code >= 200 && code < 400 )); then
    echo "OK   $code  $url"
  else
    echo "FAIL $code  $url"
    STATUS=1
  fi
done < "$(dirname "$0")/urls.txt"
exit "$STATUS"