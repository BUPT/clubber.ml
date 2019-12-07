#!/usr/bin/env bash
set -e

function resize () {
  FILE=$1
  mogrify \
    -verbose \
    -quality 90 \
    -resize '1920>' \
    "${FILE}"
}

DST=${1:-.}

if [ -f "$DST" ]; then
  echo "fit-image: $DST is file"
  resize "$DST"
  exit 0
fi

echo "fit-image: $DST is directory"
pushd "${DST}"

# FILES=$(git ls-files --exclude-standard --others *.jpg)
FILE_LIST=($(find . -type f -name '*.jpg' -o -name '*.jpeg' -o -name '*.png' -o -name '*.gif'))

for FILE in "${FILE_LIST[@]}"; do
  size=$(stat -f"%z" "$FILE")
  if [ "$size" -lt 1024 ]; then
    continue
  fi

  WIDTH=$(identify -ping -format '%w' "$FILE")
  if [ "$WIDTH" -gt 1920 ]; then
    resize "$FILE"
  fi
done

popd

