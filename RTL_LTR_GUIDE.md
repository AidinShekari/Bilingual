# RTL and LTR guide

Persian documents load `xepersian`; English documents load `fontspec` and `bidi`. The source converter splits mixed-script tokens and applies semantic Pandoc `dir` spans. In the Persian output, Latin runs use `\lr{}` so that both direction and font change; Persian runs in the English output use `\RL{\CMfa ...}`. It never inserts invisible directional Unicode markers into the generated text.

Shared robust commands are `\EN{English phrase}`, `\FA{عبارت فارسی}`, `\Term{English term}{اصطلاح فارسی}`, `\Acronym{MCMC}` and `\Code{file.py}`. Use them in authored front matter, captions and tables. Keep equations in native LaTeX math mode; do not reverse mathematical expressions. Persian assignments are generated from the Persian RTL source blocks and should remain inside the Persian document flow.

For mixed-language headings, inspect the PDF bookmark as well as the page. Prefer a simple text-only alternative with `\texorpdfstring` if a heading uses complex macros. Do not put raw URLs in unbreakable table cells.

Literal code and command output in Persian PDFs use xepersian's `latin` environment around `fvextra` Verbatim. This is necessary for decimal numbers such as `0.674` to appear in source order; a bare `LTR` environment reverses their digits in these listings. Listings remain selectable text and can break across pages.
