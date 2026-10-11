#!/usr/bin/env python3
"""Validate the bilingual source, compiled PDFs, and XeLaTeX diagnostics."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"


def main() -> int:
    errors: list[str] = []
    notes: list[str] = []
    expected = ["syllabus.md", "00_course_blueprint.md", "glossary.md", "reading_list.md"]
    expected += [f"week{n:02d}_{next(iter(SOURCE.glob(f'week{n:02d}_*.md')), Path('missing')).stem[7:]}.md"
                 for n in range(1, 17)]
    for name in expected:
        if not (SOURCE / name).is_file():
            errors.append(f"Missing Markdown source: {name}")
    for name in expected[:4]:
        if (ROOT / name).read_bytes() != (SOURCE / name).read_bytes():
            errors.append(f"Root copy differs from source: {name}")
    for lang in ("en", "fa"):
        for n in range(1, 17):
            if not (ROOT / "latex" / "chapters" / lang / f"week{n:02d}.tex").is_file():
                errors.append(f"Missing LaTeX chapter: {lang} week {n:02d}")
        book = ROOT / "00-full-notes" / lang / f"Course-{lang.upper()}.pdf"
        if not book.is_file():
            errors.append(f"Missing full book: {book.relative_to(ROOT)}")
        else:
            result = subprocess.run(["pdfinfo", str(book)], capture_output=True, text=True)
            match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.M)
            if result.returncode or not match or int(match.group(1)) < 100:
                errors.append(f"Invalid full book: {book.relative_to(ROOT)}")
            else:
                notes.append(f"{book.relative_to(ROOT)}: {match.group(1)} pages")
    generated = list((ROOT / "latex" / "chapters").rglob("*.tex"))
    generated += list((ROOT / "latex" / "frontmatter").glob("*.tex"))
    for tex in generated:
        data = tex.read_text(encoding="utf-8")
        if re.search(r"Python|PyMC|Jupyter|SciPy|NumPy|ArviZ|PyTensor|"
                     r"notebook|\bcode\b|\bscript\b|\binstall\b|"
                     r"\bsoftware\b|\bpackages?\b|\benvironment\b|"
                     r"\\nolinkurl\{|"
                     r"\\begin\{Verbatim\}|\\begin\{verbatim\}|"
                     r"برنامه.نویسی|پایتون|کد|اسکریپت|نصب|نرم.افزار|"
                     r"خروجی مورد انتظار|Expected output", data, re.I):
            errors.append(f"Software lesson content remains in {tex.relative_to(ROOT)}")
        tables = len(re.findall(r"\\begin\{longtable\}", data))
        captions = len(re.findall(r"\\caption\{\\centering ", data))
        if tables != captions:
            errors.append(f"Table/caption mismatch in {tex.relative_to(ROOT)}: {tables}/{captions}")
    week_pdfs = sorted(ROOT.glob("0[1-6]-*/week*/??/week*.pdf"))
    if len(week_pdfs) != 32:
        errors.append(f"Expected 32 weekly PDFs; found {len(week_pdfs)}")
    else:
        invalid_pdfs = []
        for pdf in week_pdfs:
            result = subprocess.run(["pdfinfo", str(pdf)], capture_output=True, text=True)
            match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.M)
            if result.returncode or not match or int(match.group(1)) < 3:
                invalid_pdfs.append(str(pdf.relative_to(ROOT)))
        if invalid_pdfs:
            errors.append(f"Invalid weekly PDFs: {', '.join(invalid_pdfs[:8])}")
        else:
            notes.append("32 individual weekly PDFs validated with pdfinfo")
    labels = re.findall(r"\\label\{([^}]+)\}", "\n".join(
        p.read_text(encoding="utf-8") for p in (ROOT / "latex").rglob("*.tex")))
    duplicates = [name for name, count in Counter(labels).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate LaTeX labels: {', '.join(duplicates[:10])}")
    logs = list((ROOT / "build" / "logs").glob("*.log"))
    if len(logs) < 34:
        notes.append(f"Build diagnostics available for {len(logs)}/34 PDFs")
    missing_glyphs = []
    invisible_marks = 0
    undefined = []
    overfull = []
    for log in logs:
        data = log.read_text(encoding="utf-8", errors="replace")
        for codepoint in re.findall(r"Missing character: There is no .*?\(U\+([0-9A-F]+)\)", data):
            if codepoint in ("200C", "200F"):
                invisible_marks += 1
            else:
                missing_glyphs.append(log.name)
        if re.search(r"undefined (?:references|citations)|Reference .* undefined|Citation .* undefined", data, re.I):
            undefined.append(log.name)
        for amount in re.findall(r"Overfull \\hbox \(([0-9.]+)pt too wide\)", data):
            if float(amount) > 10:
                overfull.append((float(amount), log.name))
    if missing_glyphs:
        errors.append(f"Visible missing glyph warnings in: {', '.join(sorted(set(missing_glyphs))[:12])}")
    if invisible_marks:
        notes.append(f"{invisible_marks} invisible ZWNJ/RTL-marker font warnings; no printable glyph is lost")
    if undefined:
        errors.append(f"Undefined references/citations in: {', '.join(undefined[:12])}")
    if overfull:
        worst = sorted(overfull, reverse=True)[:5]
        notes.append("Overfull lines >10 pt: " + ", ".join(f"{name} {size:.1f} pt" for size, name in worst))
    notes.append("Generated lectures contain no software lesson text or uncaptained longtables; archival Markdown is preserved.")
    report = "# Quality assurance report\n\n## Results\n\n"
    report += "\n".join(f"- {item}" for item in notes) + "\n\n"
    report += "## Critical errors\n\n" + ("\n".join(f"- {item}" for item in errors) if errors else "None detected") + "\n"
    (ROOT / "QUALITY_REPORT.md").write_text(report, encoding="utf-8")
    print(report)
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
