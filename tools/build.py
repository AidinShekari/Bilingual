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
        if target.endswith(".md") and not target.startswith(("http://", "https://")):
            return {"t": "Span", "c": [["", [], []], node["c"][1]]}
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


# The source transcripts remain archival.  The lecture editions omit their
# software instructions while retaining mathematical and conceptual material.
CODE_TOPIC = re.compile(
    r"\b(?:python|pymc|jupyter(?:lab)?|notebook|colab|conda|pip|numpy|"
    r"matplotlib|arviz|scipy|script|code|install|environment|software|packages|api|"
    r"source.code|code.cell|code.block|code/|"
    r"check_install|\.py\b|\.ipynb\b|\.yml\b|programming|coding|"
    r"np\.\w+|pm\.\w+|az\.\w+|minimize_scalar|logpmf|default_rng|"
    r"expected output|run the code|execute the code)\b|"
    r"کدنویسی|کد|پایتون|نوت.?بوک|برنامه.?نویسی|خروجی مورد انتظار|"
    r"محیط نرم.?افزاری|نصب|نرم.?افزار|بسته‌ها|اسکریپت|سلول",
    re.I,
)
CODE_ONLY_HEADING = re.compile(
    r"environment setup|python warm.up|self.study.*code|code reading|"
    r"probabilistic programming with pymc|"
    r"نصب محیط نرم.?افزاری|گرم کردن با python|مطالعه.*کد|"
    r"برنامه.?نویسی احتمالاتی با pymc",
    re.I,
)


def plain_node(node) -> str:
    if isinstance(node, list):
        return " ".join(part for item in node if (part := plain_node(item)).strip())
    if isinstance(node, dict):
        kind = node.get("t")
        if kind == "Str":
            return node["c"]
        if kind in ("Code", "Math"):
            return plain_node(node["c"])
        return plain_node(node.get("c", []))
    return str(node) if node is not None else ""


def has_code(node) -> bool:
    if isinstance(node, list):
        return any(has_code(item) for item in node)
    return isinstance(node, dict) and (node.get("t") == "Code" or has_code(node.get("c", [])))


def clean_inlines(inlines: list) -> list:
    """Remove only software-specific sentences from mixed prose blocks."""
    # Bibliographies in the source sometimes use hard lines inside a single
    # paragraph.  Remove a software-only entry as a whole, not its title only.
    lines, line = [], []
    for item in inlines:
        if item.get("t") == "SoftBreak":
            lines.append(line)
            line = []
        else:
            line.append(item)
    lines.append(line)
    inlines = []
    for part in lines:
        value = plain_node(part)
        if "Martin, O." in value and "Python" in value:
            continue
        if inlines:
            inlines.append({"t": "SoftBreak"})
        inlines.extend(part)
    sentences, sentence = [], []
    for item in inlines:
        sentence.append(item)
        if item.get("t") == "Str" and re.search(r"[.!?؟؛]$", item["c"]):
            sentences.append(sentence)
            sentence = []
    if sentence:
        sentences.append(sentence)
    kept = []
    for part in sentences:
        if CODE_TOPIC.search(plain_node(part)) or has_code(part):
            formulas = math_nodes(part)
            if formulas:
                kept.append(spaced_math(formulas))
        else:
            kept.append(part)
    return [item for part in kept for item in part]


def has_math(node) -> bool:
    if isinstance(node, list):
        return any(has_math(item) for item in node)
    return isinstance(node, dict) and (node.get("t") == "Math" or has_math(node.get("c", [])))


def math_nodes(node) -> list:
    if isinstance(node, list):
        return [formula for item in node for formula in math_nodes(item)]
    if isinstance(node, dict):
        if node.get("t") == "Math":
            expression = node["c"][1]
            substantive = (node["c"][0]["t"] == "DisplayMath" or
                           bool(re.search(r"=|<|>|\\sim|\\frac|\\propto|\\leq|\\geq", expression)) or
                           len(expression) > 18)
            return [copy.deepcopy(node)] if substantive else []
        return math_nodes(node.get("c", []))
    return []


def spaced_math(formulas: list) -> list:
    result = [{"t": "Space"}]
    for formula in formulas:
        if len(result) > 1:
            result.extend([{"t": "Space"}, {"t": "Str", "c": "·"}, {"t": "Space"}])
        result.append(formula)
    result.append({"t": "Space"})
    return result


def scrub_software_words(node):
    if isinstance(node, list):
        return [scrub_software_words(item) for item in node]
    if not isinstance(node, dict):
        return node
    if node.get("t") == "Code":
        return {"t": "Str", "c": ""}
    if node.get("t") == "Str":
        return {"t": "Str", "c": re.sub(r"(?i)python|pymc|arviz|scipy|programming", "", node["c"])}
    return {key: scrub_software_words(value) for key, value in node.items()}


def clean_blocks(blocks: list) -> list:
    cleaned, skip_level = [], None
    for block in blocks:
        kind = block["t"]
        if kind == "Header":
            level = block["c"][0]
            if skip_level is not None and level > skip_level:
                continue
            skip_level = None
            title = plain_node(block["c"][2])
            if CODE_ONLY_HEADING.search(title):
                skip_level = level
                continue
            block = copy.deepcopy(block)
            if "Probabilistic Programming and Hierarchical Models" in title:
                block["c"][2] = [{"t": "Str", "c": "Week 13: Hierarchical Models"}]
            elif "برنامه‌نویسی احتمالاتی و مدل‌های سلسله‌مراتبی" in title:
                block["c"][2] = [{"t": "Str", "c": "هفته‌ی ۱۳: مدل‌های سلسله‌مراتبی"}]
            elif "written report and code" in title:
                block["c"][2] = [{"t": "Str", "c": "Final project: written report"}]
            elif "گزارش کتبی و کد" in title:
                block["c"][2] = [{"t": "Str", "c": "پروژه‌ی پایانی: گزارش کتبی"}]
            elif "the model in PyMC" in title:
                block["c"][2] = [{"t": "Str", "c": "Part B: prior predictive check"}]
            elif "مدل در PyMC" in title:
                block["c"][2] = [{"t": "Str", "c": "بخش B: بررسی پیش‌بینی پیشین"}]
            elif "Setup and verbal theory audit" in title:
                block["c"][2] = [{"t": "Str", "c": "A0: Verbal theory audit"}]
            elif "نصب و «ممیزی نظریه‌ی کلامی»" in title:
                block["c"][2] = [{"t": "Str", "c": "A0: ممیزی نظریه‌ی کلامی"}]
            elif "checked against ArviZ" in title:
                block["c"][2] = [{"t": "Str", "c": "Part C: R-hat and ESS diagnostics (30 min)"}]
            elif "بررسی‌شده با ArviZ" in title:
                block["c"][2] = [{"t": "Str", "c": "بخش C: تشخیص همگرایی با R-hat و ESS (۳۰ دقیقه)"}]
            elif "assessments/project_brief.md" in title:
                block["c"][2] = [{"t": "Str", "c": "پروژه‌ی پایانی: نمای کلی"}]
            cleaned.append(block)
            continue
        if skip_level is not None:
            formulas = [] if kind == "Table" else math_nodes(block)
            if formulas:
                cleaned.append({"t": "Para", "c": spaced_math(formulas)})
            continue
        if kind == "CodeBlock":
            # Mermaid is the source for an actual explanatory figure.
            if "mermaid" in block["c"][0][1]:
                cleaned.append(block)
            continue
        if kind in ("Para", "Plain"):
            block = copy.deepcopy(block)
            block["c"] = clean_inlines(block["c"])
            if block["c"] and plain_node(block["c"]).strip():
                cleaned.append(block)
            continue
        if kind == "BlockQuote":
            inner = clean_blocks(block["c"])
            if inner:
                cleaned.append({"t": kind, "c": inner})
            continue
        if kind == "BulletList":
            items = []
            for source_item in block["c"]:
                item = clean_blocks(source_item)
                if item and not (CODE_TOPIC.search(plain_node(source_item)) and
                                 len(plain_node(item).split()) < 12):
                    items.append(item)
            if items:
                cleaned.append({"t": kind, "c": items})
            continue
        if kind == "OrderedList":
            attrs, source_items = block["c"]
            items = []
            for source_item in source_items:
                source_text = plain_node(source_item)
                if re.search(r"^Implement\.?\s+Write Python functions", source_text, re.I):
                    item = [{"t": "Para", "c": [{"t": "Str", "c": "Analyze the predicted recall probabilities and binomial variability at selected retention intervals; explain how the two models differ."}]}]
                elif re.search(r"^پیاده.?سازی\.?\s+توابع Python", source_text):
                    item = [{"t": "Para", "c": [{"t": "Str", "c": "احتمال‌های پیش‌بینی‌شده‌ی یادآوری و تغییرپذیری دوجمله‌ای را در چند فاصله‌ی نگهداری تحلیل کنید و تفاوت دو مدل را توضیح دهید."}]}]
                else:
                    item = clean_blocks(source_item)
                if item and not (CODE_TOPIC.search(plain_node(source_item)) and
                                 len(plain_node(item).split()) < 12):
                    items.append(item)
            if items:
                cleaned.append({"t": kind, "c": [attrs, items]})
            continue
        if kind == "Table":
            table = copy.deepcopy(block)
            if CODE_TOPIC.search(plain_node(table["c"][3])):
                continue  # a software-mapping table has a software header
            for body in table["c"][4]:
                rows = []
                for row in body[3]:
                    row_text = plain_node(row)
                    if re.search(r"\bEnvironment\b.*\bpackages\b|محیط نرم.?افزاری.*بسته‌ها", row_text, re.I):
                        continue
                    if re.search(r"probabilistic programming.*برنامه.?نویسی احتمالاتی|Bayesian modeling and computation in Python", row_text, re.I):
                        continue
                    if re.search(r"Code \(Task 2\)|کد \(کار 2\)", row_text):
                        replacement = ("Predictions (Task 2)", "Clear quantitative comparison of model predictions and binomial variability") if "Code (Task 2)" in row_text else ("پیش‌بینی‌ها (کار 2)", "مقایسه‌ی کمی و روشن پیش‌بینی‌های دو مدل و تغییرپذیری دوجمله‌ای")
                        row[1][0][4] = [{"t": "Plain", "c": [{"t": "Str", "c": replacement[0]}]}]
                        row[1][-1][4] = [{"t": "Plain", "c": [{"t": "Str", "c": replacement[1]}]}]
                    for cell in row[1]:
                        cell_blocks = cell[4]
                        if (CODE_TOPIC.search(plain_node(cell_blocks)) or has_code(cell_blocks) or
                                re.search(r"\bimplement\b|پیاده.?سازی", plain_node(cell_blocks), re.I)):
                            if has_math(cell_blocks):
                                cell[4] = scrub_software_words(cell_blocks)
                                continue
                            value = plain_node(scrub_software_words(cell_blocks))
                            if "Laptop setup" in value:
                                value = "Simulate a random walk and compare its predictions with observations"
                            elif "نصب روی لپ‌تاپ" in value:
                                value = "شبیه‌سازی گام تصادفی و مقایسه‌ی پیش‌بینی‌های مدل با مشاهده‌ها"
                            value = re.sub(r"(?i)install(?: the)? course environment;?", "", value)
                            value = re.sub(r"نصب محیط نرم.?افزاری درس؛?", "", value)
                            value = re.sub(r"(?i)install check plus a\s*", "", value)
                            value = re.sub(r"بررسی نصب\s*\+\s*", "", value)
                            value = re.sub(r"(?i)probabilistic programming\s*(?:and|&|;)?\s*", "", value)
                            value = re.sub(r"(?i)report\s*\+\s*code", "report", value)
                            value = re.sub(r"(?i)code reading/interpretation", "model interpretation", value)
                            value = re.sub(r"(?i),?\s*then with\s*;", ";", value)
                            value = re.sub(r"و سپس با\s*؛", "؛", value)
                            value = re.sub(r"(?i)implement an LS fit from scratch", "derive and evaluate an LS fit", value)
                            value = re.sub(r"(?i)implement NLL minimization", "analyze NLL minimization", value)
                            value = re.sub(r"(?i)\bimplement\b", "analyze", value)
                            value = re.sub(r"پیاده‌سازی برازش LS از صفر", "استخراج و ارزیابی برازش LS", value)
                            value = re.sub(r"پیاده‌سازی کمینه‌سازی NLL", "تحلیل کمینه‌سازی NLL", value)
                            value = re.sub(r"پیاده.?سازی", "تحلیل", value)
                            value = re.sub(r"(?i)(?:python|pymc|arviz|jupyter(?:lab)?|notebook|colab|numpy|matplotlib|scipy|miniforge|conda|\bcode\b|\bscript\b|\bsoftware\b|\binstall\b|\benvironment\b|\bpackages\b)", "", value)
                            value = re.sub(r"برنامه.?نویسی|پایتون|نوت.?بوک|کد|اسکریپت|نصب|نرم.?افزار|محیط نرم.?افزاری|بسته‌ها", "", value)
                            value = re.sub(r"\s+", " ", value).strip(" ;:,()،")
                            cell[4] = [{"t": "Plain", "c": [{"t": "Str", "c": value or "Conceptual discussion"}]}]
                    rows.append(row)
                body[3][:] = rows
            if any(body[3] for body in table["c"][4]):
                cleaned.append(table)
            continue
        cleaned.append(block)
    # A removed example can leave its heading empty; remove such headings.
    for index in range(len(cleaned) - 1, -1, -1):
        block = cleaned[index]
        if block["t"] == "Header":
            level = block["c"][0]
            following = index + 1
            while following < len(cleaned) and cleaned[following]["t"] == "HorizontalRule":
                following += 1
            if following == len(cleaned) or (cleaned[following]["t"] == "Header" and cleaned[following]["c"][0] <= level):
                del cleaned[index]
    return cleaned


def caption_tables(blocks: list, lang: str) -> list:
    """Give each surviving table a source-derived, centered top caption."""
    heading = "Course information" if lang == "en" else "اطلاعات درس"
    for block in blocks:
        if block["t"] == "Header":
            heading = plain_node(block["c"][2]).strip()
        elif block["t"] == "Table" and not block["c"][1][1]:
            block["c"][1] = [None, [{"t": "Plain", "c": [{"t": "Str", "c": heading}]}]]
    return blocks


def keep_heading_families(blocks: list) -> list:
    """Reserve room when a parent heading is followed immediately by a child."""
    result = []
    for index, block in enumerate(blocks):
        if block["t"] == "Header" and index + 1 < len(blocks):
            following = blocks[index + 1]
            if following["t"] == "Header" and following["c"][0] > block["c"][0]:
                result.append({"t": "RawBlock", "c": ["latex", r"\Needspace{11\baselineskip}"]})
        result.append(block)
    return result


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
    selected = keep_heading_families(caption_tables(clean_blocks(selected), lang))
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
    # Keep the scientific examples while removing a package name embedded in
    # an otherwise useful discussion of hierarchical model applications.
    body = re.sub(r"\s*\(the HDDM\s+package\)", "", body)
    body = re.sub(r"\s*\(بسته‌ی\s*\\lr\{HDDM\)\}", "", body)
    # Labs describe mathematical procedures and model checks.  Rephrase
    # software-oriented verbs while preserving Marr's technical term.
    body = re.sub(r"\bImplement\b", "Formulate and evaluate", body)
    body = re.sub(r"\bimplement\b", "formulate and evaluate", body)
    body = body.replace("Formulate and evaluate, simulate and verify", "Formulate, simulate and verify")
    body = re.sub(r"(سطح(?:وح)?\s+)پیاده‌سازی", lambda match: match.group(1) + "\ue010", body)
    body = body.replace("پیاده‌سازی", "صورت‌بندی")
    body = body.replace("\ue010", "پیاده‌سازی")
    # The caption package prints a stray LT marker with xepersian/longtable in
    # this engine.  A local declaration centers even wrapped captions safely.
    body = body.replace(r"\caption{", r"\caption{\centering ")
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
            out = LATEX / "frontmatter" / f"{stem}-{lang}.tex"
            out.write_text(content, encoding="utf-8")
            front.append((title, stem))
        main = []
        for title, stem in front[:2]:
            chapter = f"\\chapter*{{{title}}}\\addcontentsline{{toc}}{{chapter}}{{{title}}}\\input{{frontmatter/{stem}-{lang}}}\n"
            if stem == "blueprint":
                chapter = "\\begin{landscape}\n" + chapter + "\\end{landscape}\n"
            main.append(chapter)
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
                week_title = plain_node(ast["blocks"][0]["c"][2]).strip()
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
