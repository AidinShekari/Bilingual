# PDF layout QA

## Build and automated checks

- Final `make all`/`make persian` builds produced 2 complete books and 32 weekly PDFs from the revised 16-week Markdown set. The English book has 278 pages; the Persian book has 258 pages.
- `make check` passed: all expected PDFs and LaTeX chapters exist; no visible missing-glyph diagnostics, undefined references, or overfull lines above 10 pt remain in course PDF logs.
- `make regression` compiled both 10-page stress documents. The test covers a short listing, a listing longer than one page, a repeated-header longtable, mixed-script cells, equations, a vector figure, and short/long example boxes. The regression output still has minor warnings for an invisible ZWNJ in a synthetic Persian code comment, a 2.7 pt vertical overrun, and duplicate table anchors in the test itself; these do not occur as critical errors in the course PDFs.

## Visual review

Rendered with Poppler and inspected:

- Both complete-book covers: green hierarchy, margins, and B Nazanin Persian text are legible.
- Week 2 English mathematical explanation and engineering comparison table: columns wrap within margins.
- Week 2 Persian engineering comparison table: RTL column order is correct; the paired English source table no longer appears in the Persian edition.
- Week 2 Persian technical listings: ASCII decimals such as `0.674` and `1.67` retain source order; indentation and borders are readable.
- Week 2 Persian assignment: headings, numbered instructions, math, and page transition remain legible in RTL.
- Persian regression pages with a short and a multipage listing: framed code can continue across pages without clipping.

## Remaining source and environment limits

- The supplied weekly Markdown contains fenced `text`, `bash`, `yaml`, and Mermaid blocks, but no fenced Python implementation blocks. Actual lab Python files under `code/` and assessment files under `assessments/` were not supplied; references to them remain plain text.
- The synthetic regression's Persian comment inside an otherwise LTR verbatim listing is glyph-complete but visually ordered as literal code. A real Persian-commented Python source file would need a dedicated mixed-script code path before inclusion. None of the supplied course's rendered code listings contains a Persian Python comment.
- The Week 14 source literally contains `$1 - $` in a Persian parameter explanation; the converter retains the source text rather than guessing the intended formula.
- Tectonic emits a package-level `lineno.sty` UTF-8 warning, and STIX Two Text is read from the host installation. These did not prevent compilation or produce visible course glyph loss.
