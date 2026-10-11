#!/usr/bin/env python3
"""Remove temporary build diagnostics; published PDFs remain available."""
from pathlib import Path
import shutil

root = Path(__file__).resolve().parents[1]
shutil.rmtree(root / "build", ignore_errors=True)
