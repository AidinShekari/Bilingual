# Build instructions

## Requirements

- Python 3.9 or newer
- Pandoc
- Tectonic 0.16 or newer, using its XeTeX engine
- Poppler `pdfinfo` and `pdftoppm` for validation and visual review

Tectonic downloads LaTeX packages on first use; allow network access for that first compilation. The build also fetches the requested B Nazanin font from a pinned revision of the user's `ProbAndStats` repository into an ignored local file, verifies its checksum, and embeds it in the Persian PDFs. The bundled DejaVu Sans Mono handles code. If STIX Two Text is installed, it is used for Latin text; otherwise bundled Vazirmatn is the fallback.

On macOS, install Pandoc, Tectonic and Poppler with Homebrew. On Linux, use the distribution packages or official Pandoc/Tectonic releases. On Windows, install the three tools and run the commands below in a shell with `make` and Python available.

```sh
make all                 # both full books and all 32 weekly PDFs
make english             # English book and 16 weekly PDFs
make persian             # Persian book and 16 weekly PDFs
make books               # two complete books only
make lecture WEEK=08     # one week in both languages
make source              # regenerate TeX without compiling PDFs
make check               # source/PDF/log validation and QA report
make clean               # remove temporary diagnostics only
```

The converter reads the 20 files in `source/`. It does not change them. Run commands from the repository root. Generated PDFs are stored in `00-full-notes/{en,fa}/` and in the corresponding six section folders. The TeX project is under `latex/`; edit shared design files there, then rebuild.

To compile manually from `latex/`, run `tectonic -o ../00-full-notes/en main-en.tex`. The project uses XeTeX through Tectonic because `xelatex` and `latexmk` were not installed on the working host.
