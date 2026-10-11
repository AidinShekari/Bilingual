# PDF layout QA

## Final build

- `make all` produced 34 PDFs: two complete books and 32 weekly editions.
- The English book has 246 pages; the Persian book has 224 pages. Each book has 91 centered table captions above its tables. Long tables repeat their column headers on continuation pages.
- `make check` passed. Generated lectures contain no software lessons, executable code, installation steps, notebook instructions, or code output. The supplied Markdown remains unchanged in `source/`.
- The Persian PDF embeds B Nazanin; Latin text and mathematics use the configured companion fonts.

## Pagination and visual review

- Automated page inspection of all 34 PDFs found no blank content pages, low or off-center captions, or detached section headings. All 182 complete-book table captions were detected.
- Rendered and inspected the English and Persian landscape course-plan tables and Week 2 assignment rubric. The table text stays within the page, the Persian assignment reads in RTL order, and its heading shares a page with the instructions.
- The mathematical model descriptions, formulas, lab analyses, and conceptual assignments remain in both languages. The Week 2 rubric now assesses theoretical predictions in place of the removed programming task.
- `make regression` compiled both layout stress PDFs. Its synthetic samples retain minor TeX warnings (an underfull line, a 2.68 pt vertical overrun in Persian, and duplicate table anchors in the regression fixture); these are not critical errors in the course PDFs.

## Reproducibility note

The build uses the pinned B Nazanin font and the locally available STIX Two Text font. Tectonic reported no printable missing glyphs, undefined references, or overfull course lines above 10 pt in the final checks.
