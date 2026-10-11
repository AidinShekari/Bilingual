PYTHON ?= python3

.PHONY: all check compile english persian

all:
	$(PYTHON) tools/build.py

check:
	$(PYTHON) tools/build.py --check

compile:
	$(PYTHON) tools/build.py --compile

english:
	$(PYTHON) tools/build.py --only en

persian:
	$(PYTHON) tools/build.py --only fa
