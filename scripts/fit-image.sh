#!/usr/bin/env bash
set -e

function resize () {
  FILE=$1
  mogrify \
    -verbose \
    -quality 80 \
    -resize '1920>' \
    ${FILE}
}

DSTDIR=${1:-.}
echo "${DSTDIR}"

pushd ${DSTDIR}

# FILES=$(git ls-files --exclude-standard --others *.jpg)
FILE_LIST=($(find . -type f -name *.jpg -o -name *.png -o -name *.gif))

for FILE in "${FILE_LIST[@]}"; do
  WIDTH=$(identify -ping -format '%w' "$FILE")
  if [ $WIDTH -gt 1920 ]; then
    echo "$FILE $WIDTH"
    resize $FILE
  fi
done

popd

