#!/usr/bin/env python3
"""Source-level checks for the bilingual lecture files.

  * bilingual parity: the English and Persian edition of each lecture must
    define the same \\label keys, include the same figures, and contain the
    same number of equations, exercises, solutions, examples and procedures;
  * Persian-specific pitfalls: Persian comma inside \\lr{...} (no glyph in the
    Latin font), line breaks inside \\bil{...}{...} in figures;
  * syllabus alignment: every lecture directory 01..26 exists with both files
    and the expected lecture number.

Usage: python3 scripts/lint_sources.py [--fix]   (exit status 1 on any problem)
  --fix  replaces Persian commas inside \\lr{...} by Latin commas, and Latin decimal
         points in Persian running text by the Persian decimal separator, before checking.
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

COUNTED = {
    "equations": r"\\begin\{(?:equation|align|gather|multline)\*?\}",
    "exercises": r"\\begin\{exercisebox\}",
    "solutions": r"\\begin\{solutionbox\}",
    "examples": r"\\begin\{examplebox\}",
    "procedures": r"\\begin\{procedurebox\}",
    "definitions": r"\\begin\{definitionbox\}",
    "tables": r"\\begin\{table\}",
    "sections": r"\\section\{",
}

def strip_comments(text):
    return re.sub(r"(?<!\\)%.*", "", text)

def facts(path):
    t = strip_comments(open(path, encoding="utf-8").read())
    f = {k: len(re.findall(p, t)) for k, p in COUNTED.items()}
    f["labels"] = sorted(set(re.findall(r"\\label\{([^}]*)\}", t)))
    f["figures"] = sorted(re.findall(r"\\acnfig\{([^}]*)\}", t))
    f["number"] = (re.findall(r"\\ACNset\{number\}\{(\d+)\}", t) or ["?"])[0]
    return f, t

PROTECTED_CMDS = ("lr", "acro", "msg", "iface", "spec", "qty", "qtyrange", "num", "SI", "ang",
                  "cite", "cref", "Cref", "ref", "label", "acnfig", "texttt", "url", "resizebox",
                  "nocite", "includegraphics", "hspace", "vspace", "rule", "addbibresource")
MATH_ENVS = ("equation", "equation*", "align", "align*", "gather", "gather*", "multline",
             "subequations", "tikzpicture", "axis")

def _mask(text):
    """Replace math and protected command arguments by placeholders."""
    keep = []
    def stash(frag):
        keep.append(frag)
        return "\x00%d\x00" % (len(keep) - 1)
    out, i, n = [], 0, len(text)
    while i < n:
        c = text[i]
        if c == "%" and (i == 0 or text[i - 1] != "\\"):            # comment
            j = text.find("\n", i)
            j = n if j < 0 else j
            out.append(stash(text[i:j])); i = j; continue
        if c == "$":                                                 # inline/display math
            dbl = text.startswith("$$", i)
            end = text.find("$$" if dbl else "$", i + (2 if dbl else 1))
            end = n if end < 0 else end + (2 if dbl else 1)
            out.append(stash(text[i:end])); i = end; continue
        if text.startswith("\\begin{", i):
            m = re.match(r"\\begin\{([^}]*)\}", text[i:])
            if m and m.group(1) in MATH_ENVS:
                endtag = "\\end{%s}" % m.group(1)
                end = text.find(endtag, i)
                end = n if end < 0 else end + len(endtag)
                out.append(stash(text[i:end])); i = end; continue
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+)\*?", text[i:])
            if m and m.group(1) in PROTECTED_CMDS:
                j = i + m.end()
                while j < n and text[j] in "[{":                     # all following arguments
                    close = "]" if text[j] == "[" else "}"
                    depth, k = 0, j
                    while k < n:
                        if text[k] in "[{" and text[k] == text[j]: depth += 1
                        elif text[k] == close:
                            depth -= 1
                            if depth == 0: break
                        k += 1
                    j = k + 1
                out.append(stash(text[i:j])); i = j; continue
        out.append(c); i += 1
    return "".join(out), keep

def _unmask(text, keep):
    return re.sub("\x00(\\d+)\x00", lambda m: keep[int(m.group(1))], text)

DEC = re.compile(r"(?<![\w.\\])(\d+)\.(\d+)(?![\w.]|\\linewidth|\\textwidth|cm|pt|em\b|ex\b)")

LATDIG = re.compile(r"(?<![\\\w])([A-Za-z][\w./-]*\d[\w./-]*|\d+[A-Za-z][\w./-]*)")
BIL = re.compile(r"\\bil\{([^{}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}")

def _fa_arg_fix(arg):
    """Wrap Latin tokens that contain digits (S4, P4Runtime, GTPv2-C) in \\lr so
    that their digits are not shaped as Persian digits inside the RTL label."""
    keep = []
    def stash(m):
        keep.append(m.group(0))
        return "\x00%d\x00" % (len(keep) - 1)
    masked = re.sub(r"\$[^$]*\$|\\lr\{[^{}]*\}|\\[A-Za-z]+", stash, arg)
    masked = LATDIG.sub(lambda m: "\\lr{" + m.group(1) + "}", masked)
    return _unmask(masked, keep)

PERSIAN_LETTER = re.compile("[\u0621-\u064a\u067e\u0686\u0698\u06a9\u06af\u06cc]")

def _bil_fix(m):
    en, fa = m.group(1), m.group(2)
    if not PERSIAN_LETTER.search(fa) and not re.fullmatch(r"\\[A-Za-z]+", fa.strip()):
        # nothing Persian to show: use the English label, kept left-to-right
        return "\\ACNlatin{%s}" % en
    return "\\bil{%s}{%s}" % (en, _fa_arg_fix(fa))

def fix_figures():
    for p in glob.glob(os.path.join(ROOT, "figures", "*", "*.tex")):
        s = open(p, encoding="utf-8").read()
        t = BIL.sub(_bil_fix, s)
        if t != s:
            open(p, "w", encoding="utf-8").write(t)
            print("autofixed", os.path.relpath(p, ROOT))

def autofix():
    fix_figures()
    for p in glob.glob(os.path.join(ROOT, "lectures", "*", "*-fa.tex")) + \
             glob.glob(os.path.join(ROOT, "syllabus", "*-fa.tex")):
        s = open(p, encoding="utf-8").read()
        t = re.sub(r"\\lr\{([^{}]*)\}", lambda m: "\\lr{" + m.group(1).replace("\u060c", ",") + "}", s)
        head, body = t.split("\\begin{document}", 1) if "\\begin{document}" in t else ("", t)
        masked, keep = _mask(body)
        masked = DEC.sub("\\1\u066b\\2", masked)
        t = head + ("\\begin{document}" if head else "") + _unmask(masked, keep)
        if t != s:
            open(p, "w", encoding="utf-8").write(t)
            print("autofixed", os.path.relpath(p, ROOT))

def main():
    if "--fix" in sys.argv:
        autofix()
    problems = []
    dirs = sorted(glob.glob(os.path.join(ROOT, "lectures", "lecture-[0-9][0-9]")))
    present = {os.path.basename(d)[-2:] for d in dirs}
    for n in range(1, 27):
        if "%02d" % n not in present:
            problems.append("lecture-%02d: directory missing" % n)
    for d in dirs:
        num = os.path.basename(d)[-2:]
        en = os.path.join(d, "lecture-%s-en.tex" % num)
        fa = os.path.join(d, "lecture-%s-fa.tex" % num)
        if not (os.path.exists(en) and os.path.exists(fa)):
            problems.append("lecture-%s: missing %s" % (num, "EN" if not os.path.exists(en) else "FA"))
            continue
        fe, _ = facts(en)
        ff, tfa = facts(fa)
        for f, lang in ((fe, "EN"), (ff, "FA")):
            if f["number"] != num:
                problems.append("lecture-%s %s: \\ACNset{number} is %s" % (num, lang, f["number"]))
        for k in list(COUNTED) + ["labels", "figures"]:
            if fe[k] != ff[k]:
                if isinstance(fe[k], list):
                    a, b = set(fe[k]), set(ff[k])
                    problems.append("lecture-%s parity %s: only EN %s, only FA %s"
                                    % (num, k, sorted(a - b), sorted(b - a)))
                else:
                    problems.append("lecture-%s parity %s: EN %d vs FA %d" % (num, k, fe[k], ff[k]))
        body = tfa.split("\\begin{document}", 1)[-1]
        masked, _ = _mask(body)
        for m in DEC.findall(masked):
            problems.append("lecture-%s FA: Latin decimal point in RTL text: %s.%s" % (num, m[0], m[1]))
        for m in re.findall(r"\\lr\{([^{}]*)\}", tfa):
            if PERSIAN_LETTER.search(m):
                problems.append("lecture-%s FA: Persian letters inside \\lr (no glyphs): %s" % (num, m[:60]))
        for m in re.findall(r"\\lr\{[^{}]*\u060c[^{}]*\}", tfa):
            problems.append("lecture-%s FA: Persian comma inside \\lr: %s" % (num, m[:60]))
        for fig in fe["figures"]:
            p = os.path.join(ROOT, "figures", fig + ".tex")
            if not os.path.exists(p):
                problems.append("lecture-%s: figure file missing: %s" % (num, fig))
    for p in glob.glob(os.path.join(ROOT, "figures", "*", "*.tex")):
        t = open(p, encoding="utf-8").read()
        for m in re.finditer(r"\\bil\{([^{}]*)\}\{([^{}]*)\}", t):
            if "\\\\" in m.group(0):
                problems.append("%s: line break inside \\bil (breaks in RTL)" % os.path.relpath(p, ROOT))
        for m in BIL.finditer(t):
            if not PERSIAN_LETTER.search(m.group(2)) and not re.fullmatch(r"\\[A-Za-z]+", m.group(2).strip()):
                problems.append("%s: Persian label without Persian text: %s"
                                % (os.path.relpath(p, ROOT), m.group(2)[:50]))
            elif _fa_arg_fix(m.group(2)) != m.group(2):
                problems.append("%s: Latin token with digits not wrapped in \\lr: %s"
                                % (os.path.relpath(p, ROOT), m.group(2)[:50]))
    for p in problems:
        print("PROBLEM:", p)
    print("%d lecture directories checked, %d problems" % (len(dirs), len(problems)))
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
