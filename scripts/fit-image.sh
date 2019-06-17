#!/usr/bin/env bash
set -e

DSTDIR=${1:-.}
echo "${DSTDIR}"

push ${DSTDIR}

# FILES=$(git ls-files --exclude-standard --others *.jpg)
FILES=$(find . -type f -name *.jpg -o -name *.png -o -name *.gif)

echo $FILES
mogrify \
  -verbose \
  -resize '1920>' \
  ${FILES}

popd
