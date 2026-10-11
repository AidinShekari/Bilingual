#!/usr/bin/env python3
"""Build language editions, green reading pages, and complete course PDFs.

The original bilingual Markdown in source/ is the source of truth. English and
Persian editions are extracted from its paired paragraphs and RTL divs.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.request



ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
READER = "markdown+raw_html+tex_math_dollars+pipe_tables+fenced_code_blocks"
SECTIONS = [
    ("01-foundations", "Foundations", "مبانی مدل‌سازی شناختی", [1, 2]),
    ("02-parameter-estimation", "Parameter estimation", "برآورد پارامتر", [3, 4, 5]),
    ("03-model-evaluation", "Model evaluation", "ارزیابی مدل", [6, 7, 8]),
    ("04-bayesian-modeling", "Bayesian modeling", "مدل‌سازی بیزی", [9, 10]),
    ("05-monte-carlo", "Monte Carlo and MCMC", "مونت‌کارلو و MCMC", [11, 12, 13]),
    ("06-applications", "Cognitive applications", "کاربردها در علوم شناختی", [14, 15, 16]),
]
COURSE_FILES = [
    ("syllabus.md", "syllabus", "Syllabus", "طرح درس"),
    ("00_course_blueprint.md", "blueprint", "Course blueprint", "نقشه‌ی دوره"),
    ("glossary.md", "glossary", "Glossary", "واژه‌نامه"),
    ("reading_list.md", "readings", "Reading list", "فهرست مطالعه"),
]


def run(args: list[str], **kwargs):
    return subprocess.run(args, check=True, **kwargs)


def sanitize(markdown: str) -> str:
    """Flatten interactive answers so Pandoc doesn't swallow later RTL divs."""
    markdown = re.sub(r"<details(?:\s+[^>]*)?>", "", markdown)
    markdown = markdown.replace("</details>", "")
    markdown = re.sub(r"<summary>(.*?)</summary>", r"**\1**", markdown, flags=re.S)
    return markdown


def read_ast(path: Path) -> dict:
    source = sanitize(path.read_text(encoding="utf-8"))
    result = run(["pandoc", "-f", READER, "-t", "json"], input=source, text=True, capture_output=True)
    return json.loads(result.stdout)


def is_rtl_div(block: dict) -> bool:
    return block["t"] == "Div" and ["dir", "rtl"] in block["c"][0][2]


def split_header(block: dict, lang: str) -> dict:
    block = copy.deepcopy(block)
    inlines = block["c"][2]
    for index, inline in enumerate(inlines):
        if inline["t"] == "Str" and inline["c"] == "·":
            selected = inlines[:index] if lang == "en" else inlines[index + 1:]
            while selected and selected[0]["t"] in ("Space", "SoftBreak"):
                selected.pop(0)
            while selected and selected[-1]["t"] in ("Space", "SoftBreak"):
                selected.pop()
            block["c"][1] = ["", [], []]
            block["c"][2] = selected
            return block
    raise ValueError("A heading is missing its English/Persian separator")


def only_display_math(block: dict) -> bool:
    return block["t"] in ("Para", "Plain") and bool(block["c"]) and all(
        inline["t"] in ("Space", "SoftBreak") or
        (inline["t"] == "Math" and inline["c"][0]["t"] == "DisplayMath")
        for inline in block["c"]
    )


def rewrite_links(node):
    if isinstance(node, list):
        return [rewrite_links(item) for item in node]
    if not isinstance(node, dict):
        return node
    if node.get("t") == "Link":
        target = node["c"][2][0]
        if target.startswith(("code/", "assessments/")):
            return {"t": "Code", "c": [["", [], []], target]}
    return {key: rewrite_links(value) for key, value in node.items()}


def directionalize(node, lang: str):
    """Add semantic bidi spans to source inlines without changing their words."""
    if isinstance(node, list):
        return [directionalize(item, lang) for item in node]
    if not isinstance(node, dict):
        return node
    node = copy.deepcopy(node)
    if node.get("t") in ("Para", "Plain", "Strong", "Emph", "Strikeout"):
        inlines = [directionalize(item, lang) for item in node["c"]]
        node["c"] = bidi_runs(inlines, lang)
        return node
    if node.get("t") == "Header":
        node["c"][2] = bidi_runs([directionalize(i, lang) for i in node["c"][2]], lang)
        return node
    if node.get("t") == "Code" and lang == "fa":
        return {"t": "Span", "c": [["", [], [["dir", "ltr"]]], [node]]}
    if "c" in node:
        node["c"] = directionalize(node["c"], lang)
    return node


def bidi_runs(inlines: list, lang: str) -> list:
    target = re.compile(r"[\u0600-\u06ff]" if lang == "en" else r"[A-Za-z]")
    direction = "rtl" if lang == "en" else "ltr"
    out, run = [], []
    def split_script(item):
        if item.get("t") != "Str":
            return [item]
        value = item["c"]
        if not (re.search(r"[A-Za-z]", value) and re.search(r"[\u0600-\u06ff]", value)):
            return [item]
        pieces, current, script = [], "", None
        for char in value:
            char_script = ("fa" if re.match(r"[\u0600-\u06ff]", char) else
                           "en" if re.match(r"[A-Za-z]", char) else None)
            if char_script and script and char_script != script:
                pieces.append({"t": "Str", "c": current})
                current = ""
            current += char
            if char_script:
                script = char_script
        if current:
            pieces.append({"t": "Str", "c": current})
        return pieces
    def flush():
        trailing = []
        while run and run[-1].get("t") in ("Space", "SoftBreak"):
            trailing.insert(0, run.pop())
        if any(item.get("t") == "Str" and target.search(item["c"]) for item in run):
            out.append({"t": "Span", "c": [["", [], [["dir", direction]]], run.copy()]})
        else:
            out.extend(run)
        out.extend(trailing)
        run.clear()
    for item in (piece for inline in inlines for piece in split_script(inline)):
        typ = item.get("t")
        if typ == "Str" and target.search(item["c"]):
            run.append(item)
        elif typ in ("Space", "SoftBreak") and run:
            run.append(item)
        else:
            flush()
            out.append(item)
    flush()
    return out


def flexible_inline_code(node):
    """Render inline code as breakable TeX URL text without changing bytes."""
    if isinstance(node, list):
        return [flexible_inline_code(item) for item in node]
    if not isinstance(node, dict):
        return node
    if node.get("t") == "Code":
        value = node["c"][1]
        if "{" not in value and "}" not in value:
            return {"t": "RawInline", "c": ["latex", f"\\nolinkurl{{{value}}}"]}
    return {key: flexible_inline_code(value) for key, value in node.items()}


def extract(ast: dict, lang: str) -> dict:
    blocks = ast["blocks"]
    selected = []
    def paired_later(index: int, kind: str) -> bool:
        for following in blocks[index + 1:]:
            if following["t"] == "Header":
                break
            if is_rtl_div(following):
                return any(child["t"] == kind for child in following["c"][1])
        return False
    for index, block in enumerate(blocks):
        next_rtl = index + 1 < len(blocks) and is_rtl_div(blocks[index + 1])
        if is_rtl_div(block):
            if lang == "fa":
                selected.extend(copy.deepcopy(block["c"][1]))
        elif block["t"] == "Header":
            selected.append(split_header(block, lang))
        elif lang == "en":
            selected.append(copy.deepcopy(block))
        elif block["t"] == "HorizontalRule":
            selected.append(copy.deepcopy(block))
        elif block["t"] == "Table" and not paired_later(index, "Table"):
            selected.append(copy.deepcopy(block))
        elif block["t"] == "CodeBlock":
            paired_code = (next_rtl and any(
                child["t"] == "CodeBlock" and child["c"][0][1] == block["c"][0][1]
                for child in blocks[index + 1]["c"][1]))
            if not paired_code:
                selected.append(copy.deepcopy(block))
        elif only_display_math(block):
            selected.append(copy.deepcopy(block))
        elif block["t"] == "BlockQuote" and not next_rtl:
            # Bilingual code-cell references are shared between editions.
            selected.append(copy.deepcopy(block))
    output = copy.deepcopy(ast)
    output["blocks"] = flexible_inline_code(directionalize(rewrite_links(selected), lang))
    return output


def ast_to(ast: dict, format_name: str) -> str:
    args = ["pandoc", "-f", "json", "-t", format_name]
    if format_name == "html5":
        args.append("--mathjax")
    return run(args,
               input=json.dumps(ast, ensure_ascii=False), text=True, capture_output=True).stdout


def extract_title(ast: dict, lang: str) -> str:
    first = next(block for block in ast["blocks"] if block["t"] == "Header")
    plain = ast_to({**ast, "blocks": [split_header(first, lang)]}, "plain").strip()
    return plain


def week_source(number: int) -> Path:
    matches = list(SOURCE.glob(f"week{number:02d}_*.md"))
    if len(matches) != 1:
        raise ValueError(f"Expected one source for week {number:02d}, found {len(matches)}")
    return matches[0]


def week_folder(number: int) -> Path:
    section = next(slug for slug, _, _, weeks in SECTIONS if number in weeks)
    return ROOT / section / f"week{number:02d}"




LATEX = ROOT / "latex"
BN_FONT = LATEX / "fonts" / "BNazanin.ttf"
BN_SHA256 = "d088c489473040c556ae804359aad61e5e6a6cec34f49e8e176da9e2e100bf4c"
BN_URL = ("https://raw.githubusercontent.com/AidinShekari/ProbAndStats/"
          "c5c0cdf503625ab0574e7c3d4f825517470b2ec7/template/fonts/BNazanin.ttf")
CHAPTERS = [
    ("Fundamentals of Cognitive Modeling", "مبانی مدل‌سازی شناختی", [1, 2]),
    ("Parameter Estimation Methods", "روش‌های برآورد پارامتر", [3, 4, 5]),
    ("Evaluation of Cognitive Models", "ارزیابی مدل‌های شناختی", [6, 7, 8]),
    ("Bayesian Modeling", "مدل‌سازی بیزی", [9, 10]),
    ("Parameter Estimation with MCMC", "برآورد پارامتر با MCMC", [11, 12, 13]),
    ("Applications in Cognitive Science", "کاربردها در علوم شناختی", [14, 15, 16]),
]


def latex_body(ast: dict, lang: str, landscape_wide: bool = True) -> str:
    result = run(["pandoc", "-f", "json", "-t", "latex", "--syntax-highlighting=none"],
                 input=json.dumps(ast, ensure_ascii=False), text=True, capture_output=True)
    body = result.stdout
    # Pandoc uses bidi's \RL for semantic RTL spans. Select the bundled
    # Persian font locally in English documents; STIX body lacks Arabic glyphs.
    if lang == "en":
        body = body.replace(r"\RL{", r"\RL{\CMfa ")
    else:
        # Pandoc's bidi macro changes direction only; xepersian's \lr also
        # selects the configured Latin font, required by B Nazanin.
        body = body.replace(r"\LR{", r"\lr{")
    # These symbols are outside the body font's coverage. Keep mathematics
    # native rather than silently dropping glyphs from the PDF.
    parts = re.split(r"(\\begin\{verbatim\}.*?\\end\{verbatim\})", body, flags=re.S)
    symbols = {"←": r"\ensuremath{\leftarrow}", "→": r"\ensuremath{\rightarrow}",
               "★": r"\ensuremath{\star}", "β": r"\ensuremath{\beta}",
               "≈": r"\ensuremath{\approx}", "≥": r"\ensuremath{\geq}",
               "≤": r"\ensuremath{\leq}", "≠": r"\ensuremath{\neq}",
               "↔": r"\ensuremath{\leftrightarrow}", "√": r"\ensuremath{\surd}",
               "∞": r"\ensuremath{\infty}", "∝": r"\ensuremath{\propto}",
               "≫": r"\ensuremath{\gg}", "✓": r"\ensuremath{\checkmark}",
               "η": r"\ensuremath{\eta}", "λ": r"\ensuremath{\lambda}",
               "α": r"\ensuremath{\alpha}", "±": r"\ensuremath{\pm}",
               "…": r"\ensuremath{\ldots}"}
    for index in range(0, len(parts), 2):
        if lang == "fa":
            # Keep literal command fragments inside inline code untouched.
            chunks = re.split(r"(\\nolinkurl\{[^{}]*\})", parts[index])
            for chunk_index in range(0, len(chunks), 2):
                chunk = chunks[chunk_index]
                chunk = re.sub(r"\\text\{([^{}]*)\}",
                               lambda match: (r"\text{\lr{" + match.group(1) + "}}")
                               if re.search(r"[A-Za-z]", match.group(1)) and not re.search(r"[\u0600-\u06ff]", match.group(1))
                               else match.group(0), chunk)
                chunk = chunk.replace("---", "\ue000").replace("--", "\ue001")
                chunk = chunk.replace("\ue000", r"\lr{---}").replace("\ue001", r"\lr{--}")
                chunk = re.sub(r"\\ldots(?:\{\})?", lambda _: r"\ensuremath{\ldots}", chunk)
                chunk = re.sub(r"\\(textless|textgreater|textbar|textasciitilde)(?:\{\})?",
                               lambda match: "\\lr{\\" + match.group(1) + "}", chunk)
                chunk = chunk.replace(r"\$", r"\lr{\$}")
                chunks[chunk_index] = chunk.replace(r"\&", r"\lr{\&}")
            parts[index] = "".join(chunks)
        for char, macro in symbols.items():
            parts[index] = parts[index].replace(char, macro)
        if lang == "fa":
            parts[index] = parts[index].replace("−", r"\ensuremath{-}")
    for index in range(1, len(parts), 2):
        opener = r"\begin{latin}" + "\n" + r"\begin{Verbatim}" if lang == "fa" else r"\begin{Verbatim}"
        closer = r"\end{Verbatim}" + "\n" + r"\end{latin}" if lang == "fa" else r"\end{Verbatim}"
        parts[index] = parts[index].replace(r"\begin{verbatim}", opener)
        parts[index] = parts[index].replace(r"\end{verbatim}", closer)
    if lang == "fa":
        def break_long_inline_math(match):
            expression = match.group(1)
            if len(expression) > 34 and "," in expression and r"\text{" not in expression:
                expression = re.sub(r"(?<!\\),(\s+)", lambda comma: r",\allowbreak" + comma.group(1), expression)
            return r"\(" + expression + r"\)"
        for index in range(0, len(parts), 2):
            parts[index] = re.sub(r"\\\((.*?)\\\)", break_long_inline_math, parts[index], flags=re.S)
    body = "".join(parts)
    def prepare_listing(match):
        listing = match.group(0)
        lines = listing.count("\n") - 1
        reserved = min(lines + 3, 28) if lines <= 28 else 4
        return f"\\Needspace{{{reserved}\\baselineskip}}\n" + listing
    body = re.sub(r"(?:\\begin\{latin\}\s*)?\\begin\{Verbatim\}.*?\\end\{Verbatim\}(?:\s*\\end\{latin\})?",
                  prepare_listing, body, flags=re.S)
    # The only Mermaid blocks supplied are the paired Week 1 pipeline.
    body = re.sub(r"(?:\\begin\{latin\}\s*)?\\begin\{Verbatim\}\s*flowchart LR.*?\\end\{Verbatim\}(?:\s*\\end\{latin\})?",
                  r"\\input{figures/modeling-pipeline}", body, count=1, flags=re.S)
    if landscape_wide:
        def wrap_wide(match):
            table = match.group(0)
            head = table.split(r"\midrule", 1)[0]
            return (r"\begin{landscape}\small" + "\n" + table + "\n" + r"\end{landscape}") if head.count("&") >= 6 else table
        body = re.sub(r"\\begin\{longtable\}.*?\\end\{longtable\}", wrap_wide, body, flags=re.S)
    return body


def metadata_title(value: str, lang: str) -> str:
    if lang != "fa":
        return value
    return re.sub(r"[A-Za-z][A-Za-z0-9]*(?:[ \-–/][A-Za-z][A-Za-z0-9]*)*",
                  lambda match: r"\lr{" + match.group(0) + "}", value)


def standalone(lang: str, content: str, detail: str = "") -> str:
    flag = "true" if lang == "fa" else "false"
    if not detail:
        detail = "۱۶ هفته · ۶ فصل" if lang == "fa" else "16 weeks · 6 chapters"
    detail = metadata_title(detail, lang)
    return ("% !TEX program = xelatex\n"
            "\\documentclass[11pt,a4paper,openany]{book}\n"
            f"\\newif\\ifCMpersian\\CMpersian{flag}\n"
            "\\input{preamble}\n"
            f"\\def\\CMcoverdetail{{{detail}}}\n"
            "\\begin{document}\n"
            "\\frontmatter\\input{frontmatter/cover}\\tableofcontents\n"
            "\\mainmatter\n" + content + "\n\\end{document}\n")


def write_all() -> None:
    for lang in ("en", "fa"):
        front = []
        for source_name, stem, en, fa in COURSE_FILES:
            ast = extract(read_ast(SOURCE / source_name), lang)
            # The frontmatter title is supplied by the book's chapter heading.
            if ast["blocks"] and ast["blocks"][0]["t"] == "Header":
                ast["blocks"] = ast["blocks"][1:]
            title = metadata_title(fa if lang == "fa" else en, lang)
            content = latex_body(ast, lang, landscape_wide=False)
            if stem == "blueprint":
                content = "\\begin{landscape}\n" + content + "\n\\end{landscape}\n"
            out = LATEX / "frontmatter" / f"{stem}-{lang}.tex"
            out.write_text(content, encoding="utf-8")
            front.append((title, stem))
        main = []
        for title, stem in front[:2]:
            main.append(f"\\chapter*{{{title}}}\\addcontentsline{{toc}}{{chapter}}{{{title}}}\\input{{frontmatter/{stem}-{lang}}}\n")
        for en, fa, weeks in CHAPTERS:
            title = metadata_title(fa if lang == "fa" else en, lang)
            main.append(f"\\chapter{{{title}}}\n")
            for week in weeks:
                main.append(f"\\input{{chapters/{lang}/week{week:02d}}}\n")
        for title, stem in front[2:]:
            main.append(f"\\chapter*{{{title}}}\\addcontentsline{{toc}}{{chapter}}{{{title}}}\\input{{frontmatter/{stem}-{lang}}}\n")
        (LATEX / f"main-{lang}.tex").write_text(standalone(lang, "".join(main)), encoding="utf-8")
        for en, fa, weeks in CHAPTERS:
            for week in weeks:
                ast = extract(read_ast(week_source(week)), lang)
                body = latex_body(ast, lang)
                (LATEX / "chapters" / lang / f"week{week:02d}.tex").write_text(body, encoding="utf-8")
                title = metadata_title(fa if lang == "fa" else en, lang)
                week_title = extract_title(read_ast(week_source(week)), lang)
                wrapper = standalone(lang, f"\\chapter{{{title}}}\\input{{chapters/{lang}/week{week:02d}}}", week_title)
                (LATEX / f"week{week:02d}-{lang}.tex").write_text(wrapper, encoding="utf-8")


def compile_file(source: Path, output_dir: Path, pdf_name: str | None = None) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    # Compiling from latex/ makes all shared template paths deterministic.
    proc = subprocess.run(["tectonic", "--keep-logs", "-o", str(output_dir), str(source.relative_to(LATEX))],
                          cwd=LATEX, text=True, capture_output=True)
    log_dir = ROOT / "build" / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    (log_dir / f"{source.stem}.log").write_text(proc.stdout + proc.stderr, encoding="utf-8")
    if proc.returncode:
        log = ROOT / "build" / "compile-errors.log"
        log.parent.mkdir(exist_ok=True)
        log.write_text(proc.stdout + proc.stderr, encoding="utf-8")
        raise RuntimeError(f"XeLaTeX failed for {source.name}: {proc.stderr[-1500:]}")
    if pdf_name:
        (output_dir / f"{source.stem}.pdf").replace(output_dir / pdf_name)
    (output_dir / f"{source.stem}.log").unlink(missing_ok=True)
    print(f"Compiled {source.relative_to(ROOT)}")


def ensure_bnazanin() -> None:
    """Use the exact font already published in the user's reference repo.

    The local file is ignored by Git because the font's redistribution terms
    are not established here; final PDFs embed the selected glyphs.
    """
    if BN_FONT.is_file():
        data = BN_FONT.read_bytes()
    else:
        print("Fetching B Nazanin from pinned ProbAndStats revision", flush=True)
        with urllib.request.urlopen(BN_URL, timeout=30) as response:
            data = response.read()
        BN_FONT.parent.mkdir(parents=True, exist_ok=True)
        BN_FONT.write_bytes(data)
    if hashlib.sha256(data).hexdigest() != BN_SHA256:
        raise RuntimeError("B Nazanin font hash differs from the audited reference file")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-pdf", action="store_true", help="Generate LaTeX without compiling")
    parser.add_argument("--only", choices=["en", "fa"], help="Build only one language")
    parser.add_argument("--books-only", action="store_true", help="Compile complete books only")
    parser.add_argument("--week", type=int, help="Compile one week in both languages")
    args = parser.parse_args()
    if args.week is not None and not 1 <= args.week <= 16:
        parser.error("--week must be between 1 and 16")
    try:
        write_all()
        if not args.no_pdf:
            if not shutil.which("tectonic"):
                raise RuntimeError("tectonic XeLaTeX engine is required")
            ensure_bnazanin()
            for lang in ([args.only] if args.only else ["en", "fa"]):
                if args.week is None:
                    compile_file(LATEX / f"main-{lang}.tex", ROOT / "00-full-notes" / lang,
                                 f"Course-{lang.upper()}.pdf")
                if not args.books_only:
                    for week in ([args.week] if args.week is not None else range(1, 17)):
                        compile_file(LATEX / f"week{week:02d}-{lang}.tex",
                                     week_folder(week) / lang)
    except (ValueError, FileNotFoundError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
