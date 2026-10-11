PYTHON ?= python3
WEEK ?= 01

.PHONY: all english persian books lecture check clean source regression

all:
	$(PYTHON) tools/build.py

english:
	$(PYTHON) tools/build.py --only en

persian:
	$(PYTHON) tools/build.py --only fa

books:
	$(PYTHON) tools/build.py --books-only

lecture:
	$(PYTHON) tools/build.py --week $(WEEK)

source:
	$(PYTHON) tools/build.py --no-pdf

check:
	$(PYTHON) tools/check.py

regression:
	mkdir -p build/regression
	cd latex && tectonic -o ../build/regression regression-en.tex
	cd latex && tectonic -o ../build/regression regression-fa.tex

clean:
	$(PYTHON) tools/clean.py
