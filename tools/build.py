#!/usr/bin/env python3
"""Compile bilingual lectures and assemble the complete course PDFs.

The default command only assembles the already published chapter PDFs, so it
needs pypdf but no TeX installation. Pass --compile to rebuild TeX sources.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
CHAPTERS = sorted(
    path for path in ROOT.iterdir() if path.is_dir() and re.fullmatch(r"\d{2}-[^/]+", path.name) and not path.name.startswith("00-")
)
LANGUAGES = ("en", "fa")


def source_and_pdf(folder: Path, lang: str) -> tuple[Path, Path]:
    stem = f"lecture-{folder.name[:2]}-{lang}"
    return folder / lang / f"{stem}.tex", folder / lang / f"{stem}.pdf"


def title_of(source: Path) -> str:
    content = source.read_text(encoding="utf-8")
    marker = r"\ACNset{title}{"
    start = content.find(marker)
    if start < 0:
        return source.parent.parent.name
    depth, chars = 1, []
    for char in content[start + len(marker):]:
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                break
        chars.append(char)
    title = "".join(chars).replace(r"\lr{", "").replace("}", "")
    return title.replace(r"\&", "&").replace("~", " ")


def check_inputs(languages: tuple[str, ...]) -> None:
    if len(CHAPTERS) != 26 or [p.name[:2] for p in CHAPTERS] != [f"{i:02d}" for i in range(1, 27)]:
        raise ValueError("Expected exactly 26 numbered lecture directories (01–26)")
    for lang in languages:
        syllabus = ROOT / "00-syllabus" / lang / f"syllabus-{lang}"
        for path in (syllabus.with_suffix(".tex"), syllabus.with_suffix(".pdf")):
            if not path.is_file():
                raise FileNotFoundError(path)
        for folder in CHAPTERS:
            source, pdf = source_and_pdf(folder, lang)
            for path in (source, pdf):
                if not path.is_file():
                    raise FileNotFoundError(path)
            if not PdfReader(pdf).pages:
                raise ValueError(f"Empty PDF: {pdf}")


def compile_document(source: Path) -> None:
    for executable in ("xelatex", "biber"):
        if not shutil.which(executable):
            raise RuntimeError(f"{executable} is required for --compile")
    build_dir = ROOT / "build" / source.stem
    build_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "references" / "acn.bib", build_dir / "acn.bib")
    env = os.environ.copy()
    env["BIBINPUTS"] = f"{build_dir}{os.pathsep}{ROOT / 'references'}{os.pathsep}{env.get('BIBINPUTS', '')}"
    latex = ["xelatex", "-interaction=nonstopmode", "-halt-on-error", f"-output-directory={build_dir}", source.name]
    subprocess.run(latex, cwd=source.parent, env=env, check=True)
    subprocess.run(["biber", source.stem], cwd=build_dir, env=env, check=True)
    subprocess.run(latex, cwd=source.parent, env=env, check=True)
    subprocess.run(latex, cwd=source.parent, env=env, check=True)
    shutil.copy2(build_dir / f"{source.stem}.pdf", source.with_suffix(".pdf"))


def assemble(lang: str) -> Path:
    if not shutil.which("pdfunite"):
        raise RuntimeError("pdfunite (Poppler) is required to preserve chapter PDF links")
    syllabus = ROOT / "00-syllabus" / lang / f"syllabus-{lang}.pdf"
    inputs = [syllabus]
    bookmarks = [("Syllabus" if lang == "en" else "سرفصل درس", 0)]
    offset = len(PdfReader(syllabus).pages)
    for folder in CHAPTERS:
        source, pdf = source_and_pdf(folder, lang)
        bookmarks.append((f"{folder.name[:2]} — {title_of(source)}", offset))
        offset += len(PdfReader(pdf).pages)
        inputs.append(pdf)
    (ROOT / "build").mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(dir=ROOT / "build") as temp_dir:
        merged = Path(temp_dir) / "merged.pdf"
        subprocess.run(["pdfunite", *(str(path) for path in inputs), str(merged)], check=True)
        writer = PdfWriter()
        writer.clone_document_from_reader(PdfReader(merged))
        for title, page_number in bookmarks:
            writer.add_outline_item(title, page_number)
        writer.add_metadata({
            "/Title": "Advanced Communication Networks — Complete Notes" if lang == "en" else "شبکه‌های ارتباطی پیشرفته — جزوهٔ کامل",
            "/Author": "Aidin Shekari",
            "/Language": lang,
        })
        output = ROOT / "00-full-notes" / lang / f"AdvancedCommunicationNetworks-{lang}.pdf"
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("wb") as stream:
            writer.write(stream)
    print(f"Built {output.relative_to(ROOT)} ({len(PdfReader(output).pages)} pages)")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--only", choices=LANGUAGES, help="Build one language")
    parser.add_argument("--compile", action="store_true", help="Recompile the lecture and syllabus TeX sources first")
    parser.add_argument("--chapter", help="With --compile, recompile only one lecture number (01–26)")
    parser.add_argument("--check", action="store_true", help="Check all source and chapter PDFs without writing books")
    args = parser.parse_args()
    if args.chapter and not args.compile:
        parser.error("--chapter requires --compile")
    languages = (args.only,) if args.only else LANGUAGES
    try:
        if args.compile:
            selected = [folder for folder in CHAPTERS if not args.chapter or folder.name[:2] == args.chapter.zfill(2)]
            if not selected:
                raise ValueError(f"Unknown chapter: {args.chapter}")
            for lang in languages:
                if not args.chapter:
                    compile_document(ROOT / "00-syllabus" / lang / f"syllabus-{lang}.tex")
                for folder in selected:
                    compile_document(source_and_pdf(folder, lang)[0])
        check_inputs(languages)
        if not args.check:
            for lang in languages:
                assemble(lang)
    except (FileNotFoundError, ValueError, RuntimeError, subprocess.CalledProcessError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
