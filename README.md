# Advanced Communication Networks — bilingual lecture notes

[فارسی](README.fa.md)

A complete course on mobile communication networks from 2G to 6G, written in
LaTeX with **an English and a Persian edition of every document**. Both editions
share the same structure, equations, figures, labels and numbering.

The 26 lectures follow the syllabus of
[AdvancedCommNetworks2026](https://github.com/AidinShekari/AdvancedCommNetworks2026).
All text, figures and exercises in this repository are original.

## Contents

| Part | Lectures |
|------|----------|
| I — 2G/3G foundations | 01 GSM, GPRS and EDGE · 02 2G circuit switching · 03 2G/3G core networks · 04 Mobility and handover |
| II — 4G access and core | 05 LTE architecture · 06 E-UTRAN · 07 LTE scheduling · 08 Random access · 09 EPC · 10 Diameter · 11 HSS · 12 MME · 13 S-GW and P-GW |
| III — Software-driven architectures | 15 SDN · 16 NFV · 17 3GPP standardisation · 18 5G service-based architecture |
| IV — 5G system and procedures | 14 5G introduction · 19 5G core · 20 5G procedures · 21 Network slicing · 22 QoS |
| V — Planes and outlook | 23 User plane · 24 Control plane · 25 Network evolution · 26 6G technologies |

Every lecture has the same 14 sections: learning objectives, prerequisites,
introduction, fundamentals, technical detail, mathematical models, architecture,
step-by-step procedures, worked examples, technology comparison, key takeaways,
exercises (three levels), solutions and further reading with references.

Compiled PDFs are in [`pdf/`](pdf): `lecture-NN-en.pdf`, `lecture-NN-fa.pdf`,
`syllabus-en.pdf` and `syllabus-fa.pdf`.

## Repository layout

```
lectures/lecture-NN/lecture-NN-{en,fa}.tex   lecture sources
figures/lecture-NN/*.tex                     TikZ / PGFPlots figures (shared by both editions)
syllabus/syllabus-{en,fa}.tex                course syllabus
templates/                                   preambles, cover, macros, strings, shared style
references/acn.bib                           bibliography (biblatex, IEEE style)
fonts/                                       Vazirmatn (SIL OFL 1.1)
scripts/                                     QA and validation scripts (Python 3, stdlib only)
pdf/                                         compiled PDFs
Makefile, latexmkrc                          build system
.github/workflows/build.yml                  continuous integration
```

## Building

Requirements: TeX Live 2022 or later with XeLaTeX, `xepersian`, `bidi`,
`biblatex` + `biber`, TikZ/PGFPlots and `latexmk`; Python 3.

```sh
make all                    # every lecture in both languages + syllabus
make english                # English editions only
make persian                # Persian editions only
make lecture LECTURE=07     # one lecture, both languages
make syllabus
make check                  # scan logs: errors, undefined refs, missing glyphs, overfull boxes
make validate               # recompute worked-example values
make clean                  # remove build/
```

On Debian/Ubuntu:

```sh
sudo apt-get install texlive-xetex texlive-lang-arabic texlive-latex-extra \
  texlive-pictures texlive-science texlive-bibtex-extra texlive-fonts-recommended \
  biber latexmk python3
```

Use `make -j4 all` for a parallel build.

## Quality checks

* `scripts/check_logs.py` — reports errors, undefined references and citations,
  missing glyphs, overfull boxes and RTL/LTR problems for every built document.
* `scripts/lint_sources.py [--fix]` — checks EN/FA parity (labels, equations,
  figures, citations), the 14-section structure, syllabus coverage and Persian
  figure labels; `--fix` applies safe automatic corrections.
* `scripts/validate_examples.py` — recomputes selected numbers from worked
  examples and solutions.

The GitHub Actions workflow runs the full build and all three checks on every
push and uploads the PDFs as an artifact.

## Conventions

Italic scalars, bold vectors and matrices, upright units and operators, SI units.
Technical abbreviations stay in Latin script in the Persian edition; numbers in
Persian prose use Persian digits, while equations use the same notation as the
English edition.

## License

Text and figures: CC BY-SA 4.0. Code (scripts, build files, templates): MIT.
Vazirmatn font: SIL Open Font License 1.1. See [LICENSE](LICENSE).

## Limitations

* Quantitative examples use stated, often illustrative, assumptions; they are
  teaching values, not measurements of a specific network.
* 3GPP specifications evolve with each release; check the current version of a
  cited specification before relying on a detail.
* Lecture 26 describes 6G as of 2026: the IMT-2030 framework is agreed, most
  technologies are still research.
