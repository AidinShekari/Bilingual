#!/usr/bin/env python3
"""Quality gate for the LaTeX build logs.

Usage:  python3 scripts/check_logs.py [build-dir]

For every build/<name>/<name>.log it reports
  * undefined references / citations, multiply defined labels
  * undefined control sequences and other LaTeX errors
  * missing glyphs (U+200F/U+200E directional marks are ignored: they are
    invisible marks inserted by bidi and have no glyph by design)
  * overfull boxes wider than 1 pt
  * undefined font shapes
Exit status is 1 if any document has a blocking problem.
"""
import glob
import os
import re
import sys

IGNORED_GLYPHS = {"U+200F", "U+200E", "U+200C", "U+200D"}

def scan(path):
    text = open(path, encoding="utf-8", errors="replace").read()
    res = {}
    res["undef_ref"] = len(re.findall(r"LaTeX Warning: (?:Reference|Citation) `[^']*' .*undefined", text)) \
        + len(re.findall(r"Package biblatex Warning: The following entry could not be found", text))
    res["multi_label"] = len(re.findall(r"multiply defined", text))
    res["errors"] = len(re.findall(r"^! ", text, flags=re.M)) + len(re.findall(r"^[^\s:]+\.tex:\d+: ", text, flags=re.M))
    glyphs = re.findall(r"Missing character: There is no .*? \((U\+[0-9A-F]+)\)", text)
    res["missing_glyph"] = len([g for g in glyphs if g not in IGNORED_GLYPHS])
    over = re.findall(r"Overfull \\[hv]box \(([\d.]+)pt too", text)
    res["overfull>1pt"] = len([o for o in over if float(o) > 1.0])
    res["font_shape"] = len(re.findall(r"Font shape `[^']*' undefined", text))
    res["rerun"] = len(re.findall(r"Rerun to get|Please rerun", text))
    return res

def main():
    build = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", "build")
    logs = sorted(glob.glob(os.path.join(build, "*", "*.log")))
    logs = [l for l in logs if os.path.basename(os.path.dirname(l)) + ".log" == os.path.basename(l)]
    if not logs:
        print("no logs found in", build)
        return 1
    keys = ["undef_ref", "multi_label", "errors", "missing_glyph", "overfull>1pt", "font_shape", "rerun"]
    blocking = {"undef_ref", "multi_label", "errors", "missing_glyph"}
    print(f"{'document':<18}" + "".join(f"{k:>14}" for k in keys))
    bad = 0
    for log in logs:
        name = os.path.basename(log)[:-4]
        r = scan(log)
        flag = any(r[k] for k in blocking)
        bad += flag
        print(f"{name:<18}" + "".join(f"{r[k]:>14}" for k in keys) + ("   FAIL" if flag else ""))
    print(f"\n{len(logs)} documents checked, {bad} with blocking problems")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
