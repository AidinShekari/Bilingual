# =====================================================================
#  Advanced Communication Networks -- build system
#  Requires: XeLaTeX, latexmk, biber, xepersian (see README for packages)
#
#    make all                  every lecture (en + fa) and both syllabi
#    make english              all English lectures
#    make persian              all Persian lectures
#    make lecture LECTURE=01   one lecture, both languages
#    make syllabus             syllabus-en.pdf and syllabus-fa.pdf
#    make check                scan build logs (scripts/check_logs.py)
#    make validate             numerical checks of worked examples
#    make clean                remove build/ (keeps pdf/)
#    make distclean            remove build/ and pdf/
#  Parallel builds are safe:   make -j4 all
# =====================================================================
ROOT     := $(abspath .)
BUILD    := $(ROOT)/build
PDFDIR   := pdf
LATEXMK  := latexmk -r $(ROOT)/latexmkrc
PYTHON   ?= python3
# shared bibliography for biber and latexmk (\addbibresource{acn.bib})
export BIBINPUTS := $(ROOT)/references//:$(BIBINPUTS)

LECTURE_DIRS := $(sort $(wildcard lectures/lecture-[0-9][0-9]))
NUMS         := $(patsubst lectures/lecture-%,%,$(LECTURE_DIRS))
EN_PDFS      := $(foreach n,$(NUMS),$(PDFDIR)/lecture-$(n)-en.pdf)
FA_PDFS      := $(foreach n,$(NUMS),$(PDFDIR)/lecture-$(n)-fa.pdf)
SYL_PDFS     := $(PDFDIR)/syllabus-en.pdf $(PDFDIR)/syllabus-fa.pdf
SHARED       := $(wildcard templates/*) references/acn.bib latexmkrc
FIGS         := $(wildcard figures/*/*.tex)

.PHONY: all english persian lecture syllabus check validate clean distclean list

all: english persian syllabus

english: $(EN_PDFS)
persian: $(FA_PDFS)
syllabus: $(SYL_PDFS)

list:
	@echo "Lectures found: $(NUMS)"

lecture:
ifndef LECTURE
	$(error Usage: make lecture LECTURE=01)
endif
	@$(MAKE) --no-print-directory $(PDFDIR)/lecture-$(LECTURE)-en.pdf $(PDFDIR)/lecture-$(LECTURE)-fa.pdf

# One rule per lecture and language (generated; GNU make substitutes only one
# '%' per prerequisite, so pattern rules cannot express lecture-NN/lecture-NN).
define LECTURE_RULE
$(PDFDIR)/lecture-$(1)-$(2).pdf: lectures/lecture-$(1)/lecture-$(1)-$(2).tex $(SHARED) $(FIGS)
	@mkdir -p $(BUILD)/lecture-$(1)-$(2) $(PDFDIR)
	@echo "  XELATEX  lecture-$(1)-$(2)"
	@$(LATEXMK) -cd -outdir=$(BUILD)/lecture-$(1)-$(2) $$< > $(BUILD)/lecture-$(1)-$(2).stdout 2>&1 \
	  || { tail -40 $(BUILD)/lecture-$(1)-$(2).stdout; exit 1; }
	@cp $(BUILD)/lecture-$(1)-$(2)/lecture-$(1)-$(2).pdf $$@
endef
$(foreach n,$(NUMS),$(foreach l,en fa,$(eval $(call LECTURE_RULE,$(n),$(l)))))

$(PDFDIR)/syllabus-%.pdf: syllabus/syllabus-%.tex $(SHARED)
	@mkdir -p $(BUILD)/syllabus-$* $(PDFDIR)
	@echo "  XELATEX  syllabus-$*"
	@$(LATEXMK) -cd -outdir=$(BUILD)/syllabus-$* $< > $(BUILD)/syllabus-$*.stdout 2>&1 \
	  || { tail -40 $(BUILD)/syllabus-$*.stdout; exit 1; }
	@cp $(BUILD)/syllabus-$*/syllabus-$*.pdf $@

check:
	@$(PYTHON) scripts/check_logs.py $(BUILD)

validate:
	@$(PYTHON) scripts/validate_examples.py

clean:
	rm -rf $(BUILD)

distclean: clean
	rm -rf $(PDFDIR)
