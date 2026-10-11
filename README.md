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
pdf/                                         compiled PDFs
```

## Compiling a document yourself

Requirements: TeX Live 2022 or later with XeLaTeX, `xepersian`, `bidi`,
`biblatex` + `biber` and TikZ/PGFPlots. From a lecture folder, for example:

```sh
cd lectures/lecture-07
xelatex lecture-07-en.tex && biber lecture-07-en && xelatex lecture-07-en.tex && xelatex lecture-07-en.tex
```

Run `biber` with `--input-directory ../../references` if it cannot find `acn.bib`.

## Conventions

Italic scalars, bold vectors and matrices, upright units and operators, SI units.
Technical abbreviations stay in Latin script in the Persian edition; numbers in
Persian prose use Persian digits, while equations use the same notation as the
English edition.

## License

Text, figures and PDFs: CC BY-SA 4.0. LaTeX templates: MIT.
Vazirmatn font: SIL Open Font License 1.1. See [LICENSE](LICENSE).

## Limitations

* Quantitative examples use stated, often illustrative, assumptions; they are
  teaching values, not measurements of a specific network.
* 3GPP specifications evolve with each release; check the current version of a
  cited specification before relying on a detail.
* Lecture 26 describes 6G as of 2026: the IMT-2030 framework is agreed, most
  technologies are still research.
