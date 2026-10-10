"""Shared numerical helpers used to validate worked examples (stdlib only)."""
import math

def erlang_b(A, m):
    """Blocking probability of an M/M/m/m loss system, stable recursion."""
    B = 1.0
    for k in range(1, m + 1):
        B = A * B / (k + A * B)
    return B

def erlang_b_traffic(m, target, lo=0.0, hi=None):
    """Offered traffic A [E] such that erlang_b(A, m) == target (bisection)."""
    hi = hi or 2.0 * m + 10
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if erlang_b(mid, m) > target:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)

def erlang_c(A, m):
    """Probability of waiting in an M/M/m queue (A < m)."""
    b = erlang_b(A, m)
    return m * b / (m - A * (1 - b))

def db(x):
    return 10 * math.log10(x)

def lin(x_db):
    return 10 ** (x_db / 10)

def shannon(B, snr_lin):
    return B * math.log2(1 + snr_lin)

def fspl_db(d_m, f_hz):
    c = 299792458.0
    return 20 * math.log10(4 * math.pi * d_m * f_hz / c)

def thermal_noise_dbm(B_hz, T=290.0):
    k = 1.380649e-23
    return 10 * math.log10(k * T * B_hz / 1e-3)
