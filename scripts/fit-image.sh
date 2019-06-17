#!/usr/bin/env bash
set -e

DSTDIR=${1:-.}

cd ${DSTDIR}
echo "${DSTDIR}"

FILES=$(git ls-files --exclude-standard --others *.jpg)

mogrify \
  -verbose \
  -resize '1920>' \
  ${FILES}

cd -

