# Quality assurance procedure

Run `make all` followed by `make check`. `tools/check.py` validates the 20 Markdown sources, four unchanged root copies, 32 weekly TeX files, 32 lecture PDFs, both full books, duplicate labels, missing glyph diagnostics, undefined references, and large overfull lines. Its report is written to `QUALITY_REPORT.md`.

Run `make regression` to compile the English and Persian layout stress tests. They include a short code block, a code listing that spans pages, a multi-page table with repeated headings, a mixed-script table, equations, a vector figure and short/long green example boxes. The tests live in `latex/tests/` and their PDFs are temporary build artifacts.

For visual review, render representative pages with `pdftoppm -f N -l N -png -r 130 book.pdf preview`. Inspect the cover, table of contents, mixed-language terminology tables, displayed mathematics, the Week 1 pipeline figure, code listings, a long table, assignments, and final project pages in both languages. Check margins, glyphs, table width, equation direction and link behavior. A successful XeLaTeX process alone does not establish visual correctness.

Source references to missing `code/` and `assessments/` files are rendered as text. They are not linked because those companion files were not provided. The reading list is preserved exactly; chapter pointers marked `[verify]` in the source remain unverified. Do not remove those caveats when distributing the course.
