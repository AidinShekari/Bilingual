#!/usr/bin/env python3
"""Source-level checks for the bilingual lecture files.

  * bilingual parity: the English and Persian edition of each lecture must
    define the same \\label keys, include the same figures, and contain the
    same number of equations, exercises, solutions, examples and procedures;
  * Persian-specific pitfalls: Persian comma inside \\lr{...} (no glyph in the
    Latin font), line breaks inside \\bil{...}{...} in figures;
  * syllabus alignment: every lecture directory 01..26 exists with both files
    and the expected lecture number.

Usage: python3 scripts/lint_sources.py      (exit status 1 on any problem)
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

def main():
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
    for p in problems:
        print("PROBLEM:", p)
    print("%d lecture directories checked, %d problems" % (len(dirs), len(problems)))
    return 1 if problems else 0

if __name__ == "__main__":
    sys.exit(main())
