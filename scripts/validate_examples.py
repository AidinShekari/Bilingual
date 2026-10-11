#!/usr/bin/env python3
"""Recompute selected worked-example and solution values of the lectures.

Each check compares a value printed in the lecture notes with an independent
computation (stdlib only). Run: make validate   (exit code 1 on any mismatch).
"""
import cmath
import math
import sys

sys.path.insert(0, __import__("os").path.dirname(__file__))
from acnmath import erlang_b, fspl_db  # noqa: E402

FAILS = []
COUNT = 0


def check(name, value, expected, rel=0.01, abs_tol=0.0):
    global COUNT
    COUNT += 1
    ok = math.isclose(value, expected, rel_tol=rel, abs_tol=abs_tol)
    print(f"{'ok  ' if ok else 'FAIL'} {name:58s} {value:.6g} (notes: {expected:g})")
    if not ok:
        FAILS.append(name)


# ---- Lecture 4: two-class location-area optimisation ---------------------
def la_cost(v, lam, N, a=500.0, cu=1.0, cp=0.1):
    """Per-user cost per hour: updates 4 cu v/(pi a sqrt N) + paging cp lam N."""
    return 3600 * (4 * cu * v / (math.pi * a * math.sqrt(N)) + cp * lam / 3600 * N)


def la_opt(v, lam, a=500.0, cp=0.1):
    return (2 * v / (math.pi * a * cp * lam / 3600)) ** (2 / 3)


vbar, lbar = 0.7 * 1.5 + 0.3 * 15, 0.7 * 1 + 0.3 * 3
check("L04 mean speed [m/s]", vbar, 5.55)
check("L04 N* (average class)", la_opt(vbar, lbar), 29.3)
check("L04 N* pedestrians", la_opt(1.5, 1), 16.8)
check("L04 N* vehicles", la_opt(15, 3), 37.5)

# ---- Lecture 8: Zadoff-Chu properties ------------------------------------
NZC = 839


def zc(u):
    return [cmath.exp(-1j * math.pi * u * n * (n + 1) / NZC) for n in range(NZC)]


def corr(a, b, s):
    return abs(sum(a[n] * b[(n + s) % NZC].conjugate() for n in range(NZC))) / NZC


x25, x29 = zc(25), zc(29)
check("L08 ZC u=25 constant amplitude (max |x|)", max(abs(v) for v in x25), 1.0, rel=1e-12)
check("L08 ZC u=25 max autocorrelation, shift != 0",
      max(corr(x25, x25, s) for s in (1, 13, 100, 419)), 0.0, abs_tol=1e-9)
check("L08 ZC cross-correlation u=25/29 = 1/sqrt(N)", corr(x25, x29, 0), 1 / math.sqrt(NZC), rel=1e-6)

# ---- Lecture 21: Erlang-B values -----------------------------------------
check("L21 B(40, 52)", erlang_b(40, 52), 0.011, rel=0.05)
check("L21 B(40, 53)", erlang_b(40, 53), 0.0082, rel=0.05)
check("L21 B(45, 53)", erlang_b(45, 53), 0.031, rel=0.05)

# ---- Lecture 23: user plane ----------------------------------------------
check("L23 efficiency 1500 B", 1500 / 1510, 0.993, rel=1e-3)
check("L23 option-8 fronthaul 4 ant [Gbit/s]", 2 * 122.88e6 * 16 * 4 * 66 / 64 / 1e9, 16.2)
check("L23 option-7.2 fronthaul 16 layers [Gbit/s]", 273 * 12 * 28000 * 16 * 18 / 1e9, 26.4)
check("L23 12-bit SN window at 2 Gbit/s [ms]", 2048 / (2e9 / 12000) * 1e3, 12.3)
check("L23 UPF distance bound [km]", 1.6e-3 / 5e-6, 320)

# ---- Lecture 24: control plane -------------------------------------------
check("L24 AMF load [msg/s]", 2e6 * 116 / 3600, 64444, rel=1e-4)
check("L24 load with INACTIVE [msg/s]", 2e6 * 52 / 3600, 28889, rel=1e-4)
check("L24 transitions/h, T=10 s", 60 * math.exp(-10 / 60), 50.8)
check("L24 tail fraction, T=30 s", 1 - math.exp(-0.5), 0.393)
a_opt = (2 * 10 * 20 * 1 / (math.pi * 5)) ** (1 / 3)
check("L24 optimal area side a* [km]", a_opt, 2.94)
check("L24 update cost at optimum", 10 * 4 * 20 / (math.pi * a_opt), 86.6)
check("L24 timer for 20 % tail [s]", -60 * math.log(0.8), 13.4)

# ---- Lecture 25: evolution -----------------------------------------------
k = math.log(20e9 / 9.6e3) / 27
check("L25 growth constant k [1/yr]", k, 0.539)
check("L25 doubling time [yr]", math.log(2) / k, 1.29)
check("L25 cost halving time g=30 % [yr]", math.log(2) / math.log(1.3), 2.64)
check("L25 cells per km2 for 10 Tbit/s/km2", 1e13 / (400e6 * 10), 2500)

# ---- Lecture 26: 6G -------------------------------------------------------
check("L26 FSPL 140 GHz, 100 m [dB]", fspl_db(100, 140e9), 115.4, rel=2e-3)
check("L26 FSPL 300 GHz, 10 m [dB]", fspl_db(10, 300e9), 102.0, rel=2e-3)
check("L26 capacity 10 GHz [Gbit/s]", 10 * math.log2(1 + 10), 34.6)
check("L26 RIS gain N=1024 [dB]", 20 * math.log10(1024), 60.2)
R, h, e = 6371.0, 600.0, math.radians(10)
d = math.sqrt((R + h) ** 2 - (R * math.cos(e)) ** 2) - R * math.sin(e)
check("L26 LEO slant range at 10 deg [km]", d, 1932)

print(f"\n{COUNT - len(FAILS)}/{COUNT} checks passed")
sys.exit(1 if FAILS else 0)
