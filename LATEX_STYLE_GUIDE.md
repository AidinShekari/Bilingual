# LaTeX style guide

The architecture follows the reusable pattern observed in `ProbAndStats`: a shared preamble and style layer, separate weekly content, independently compilable lectures, and complete books. The visual design, green palette, and all educational content belong to Cognitive Modeling.

The book class uses A4 paper, 11 pt body, 28 mm inner / 22 mm outer margins, and 25 mm top / bottom margins. Chapter headings use forest green `#164A36`, section headings emerald `#247A56`, accents sage `#A8C9B0`, callout backgrounds pale green `#F1F7F2`, and body text dark `#24332A`. Page background is white. `latex/styles/layout.sty` sets running headers, rules, page numbers and section sizes. `latex/styles/environments.sty` provides numbered definition, theorem and exercise boxes plus examples, notes, warnings, labs, solutions and summaries.

Use `booktabs` for rules and `longtable` for multipage tables. Wide tables may be placed in landscape pages; do not shrink all table text. Week 1's modeling pipeline is a vector TikZ figure generated from the supplied Mermaid logic. Other Mermaid definitions remain in the authoritative Markdown where applicable. New figures should have a caption and unique `fig:` label; do not invent data.

The shared typography style configures framed, breakable `fvextra` code listings at `\small` with a DejaVu Sans Mono font and visible wrap indicators. Short listings reserve enough space to avoid awkward splits; listings longer than a page break naturally. `needspace` keeps headings with their opening content, while moderate widow and orphan penalties reduce isolated lines. Green `tcolorbox` examples and notes remain breakable. The source converter does not alter code bytes to fit a page.

Each source week maps to `latex/chapters/{en,fa}/weekNN.tex`. A standalone wrapper `latex/weekNN-{en,fa}.tex` imports the same content. Full books use `latex/main-{en,fa}.tex`. Avoid editing generated chapter files directly because `make source` regenerates them.
