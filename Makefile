# Makefile for awesome-chatboot
# Author: Huan LI <zixia@zixia.net> github.com/huan

SOURCE_GLOB=$(wildcard bin/*.py chit-chat/*.py tests/*.py)

.PHONY: all
all : clean lint

.PHONY: clean
clean:
	echo "TODO: clean what?"

.PHONY: lint
lint: pylint pycodestyle flake8 mypy

.PHONY: install
install:
	npm install
	(cd docs && bundle install && bundle update)

.PHONY: test
test:
	npm test

.PHONY: code
code:
	code .

.PHONY: build
build:
	(cd docs && JEKYLL_ENV=production bundle exec jekyll build)

.PHONY: serve
serve:
	(cd docs && JEKYLL_ENV=production bundle exec jekyll serve --incremental)

.PHONY: fit-image
fit-image:
	./scripts/fit-image.sh docs/assets/
