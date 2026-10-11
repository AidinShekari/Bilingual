# Contributing

* Every change to a lecture must be made in **both** editions
  (`lecture-NN-en.tex` and `lecture-NN-fa.tex`) with the same labels,
  equations, figures, citations and exercise numbering.
* Figures live in `figures/lecture-NN/` and are shared by both editions; put
  translatable text in `\bil{english}{persian}` and Latin-only labels in
  `\ACNlatin{...}`.
* In the Persian edition wrap Latin words in `\lr{...}` (or `\acro{...}` for
  abbreviations); never put Persian letters inside `\lr`.
* Add references to `references/acn.bib`; cite only sources you have checked.
* Before opening a pull request run:

```sh
python3 scripts/lint_sources.py --fix
make -j4 all
make check
make validate
```

All four must finish without reported problems.
