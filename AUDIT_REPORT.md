# Initial repository audit

The target repository had been renamed from `Bilingual` to `Cognitive-Model`, but its tracked content was still **Advanced Communication Networks** (16 lecture PDFs and TeX files, network-specific templates, `references/acn.bib`, and Vazirmatn fonts). This is the course mismatch reported in the earlier conversation. The user explicitly requested removal of that unrelated material and replacement with the supplied Cognitive Modeling course.

The 20 supplied Markdown files contain the syllabus, course blueprint, glossary, reading list, and 16 paired English/Persian weekly lessons. English paragraphs and `<div dir="rtl">` Persian paragraphs are paired; tables, display equations, code blocks, Mermaid diagrams, lab tasks, and assignment references also occur. Companion `code/` and `assessments/` files are referenced but were not supplied. The source Markdown is copied unchanged into `source/` and the four course reference files are also copied at repository root.

The 16 weekly files were subsequently replaced byte-for-byte with the user's revised `bilingual(1)` set. The revision adds plain-language explanations, mathematical walkthroughs, engineering connections, and examples across all 16 weeks. The four reference Markdown files continue to come from the original supplied set. Generated LaTeX and PDFs use this latest source set.

One source expression in Week 14 literally reads `$1 - $` in the Persian parameter explanation. The converter preserves those dollar signs as printed text rather than guessing the intended mathematical notation. It remains an authoring item to clarify in the Markdown source.

`ProbAndStats` was inspected as the structural reference. It uses a shared package/style layer, per-topic `content.tex`, standalone topic PDFs, and separate full English/Persian books. Its syllabus, course-specific art, content, university branding, and blue/gold palette are not reused. The new green design and six Cognitive Modeling chapters are specific to this course.

## Problems found in the first LaTeX conversion

- Raw mixed-script text in tables reversed Persian words in English PDFs and English multiword terms in Persian PDFs. Semantic Pandoc bidi spans now generate `\RL{}` and `\LR{}`.
- The initially selected STIX English font has no Persian glyphs; English RTL spans now select the requested B Nazanin font. Unicode mathematical symbols outside math mode are mapped to native LaTeX commands. Vazirmatn remains an open fallback for direct manual compilation.
- Long verbatim lines overflowed; `fvextra` now wraps lines without changing their source text.
- The seven-column blueprint table needs landscape pages. Wide lecture tables receive separate review in quality assurance.
- There was no Cognitive Modeling bibliography database. The supplied reading list is preserved as a dedicated book section; BibTeX entries are not fabricated.
- The supplied Week 1 Mermaid pipeline is rendered as a vector TikZ figure in the PDF; its original code remains in Markdown. No experimental results were invented.

The engine is Tectonic's XeTeX implementation, equivalent to running XeLaTeX for this project. Installed tools: `tectonic`, `pandoc`, `pdfinfo`, and `pdftoppm`. `xelatex`, `latexmk`, and `biber` were unavailable in the working environment at audit time.
