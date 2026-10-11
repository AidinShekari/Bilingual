# Font configuration

The repository bundles **Vazirmatn Regular/Bold** under the SIL Open Font License and **DejaVu Sans Mono Regular/Bold** under the DejaVu font license. License files are in `latex/fonts/`. B Nazanin is used for the Persian book and Persian spans in the English book. Its font file is fetched from the pinned `ProbAndStats` revision into ignored `latex/fonts/BNazanin.ttf` and is not committed.

Persian body and headings use B Nazanin with simulated bold, matching the requested reference. English body uses STIX Two Text when installed and falls back to bundled Vazirmatn. Mathematical expressions use the XeTeX/LaTeX math font supplied by Tectonic. Code uses bundled DejaVu Sans Mono, including Persian characters inside literal blocks. This keeps code aligned and avoids missing Arabic glyphs in code samples.

The build script checks the B Nazanin file against a pinned SHA-256 checksum. The preamble falls back to Vazirmatn only for direct manual compilation when B Nazanin has not been fetched; `make all` fetches it before compiling. The preamble checks for STIX Two Text with `\IfFontExistsTF`. If a different Latin font is desired, update both `\setmainfont` and `\setlatintextfont` branches in `latex/preamble.tex`, then rebuild and inspect mixed-language tables.
