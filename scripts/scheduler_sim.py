#!/usr/bin/env python3
"""Single-cell downlink scheduling simulation (Lecture 7).

Model (deliberately simple, reproducible with the standard library only):
  * one shared channel of B_eff = 9 MHz (50 LTE resource blocks of 180 kHz),
    allocated entirely to one user per 1-ms TTI;
  * N users with fixed mean SNRs and independent Rayleigh block fading per TTI
    (instantaneous SNR exponentially distributed around its mean);
  * link model: spectral efficiency = min(0.75*log2(1+SNR), 5.55) bit/s/Hz,
    an attenuated Shannon bound capped at the highest LTE CQI efficiency;
  * schedulers: round robin (RR), maximum C/I (MaxCI), proportional fair (PF)
    with exponentially weighted average throughput (time constant t_c TTIs).
Outputs per-user throughput [Mbit/s], cell throughput and Jain's fairness index.
Usage:  python3 scripts/scheduler_sim.py
"""
import math
import random

B_EFF = 9e6
MEAN_SNR_DB = [20.0, 12.0, 5.0, 0.0]
TTIS = 20000
TC = 100.0
SEED = 2026

def efficiency(snr_lin):
    return min(0.75 * math.log2(1.0 + snr_lin), 5.55)

def jain(x):
    return sum(x) ** 2 / (len(x) * sum(v * v for v in x))

def simulate(policy, seed=SEED, ttis=TTIS, mean_db=MEAN_SNR_DB, tc=TC):
    rng = random.Random(seed)
    n = len(mean_db)
    mean_lin = [10 ** (m / 10) for m in mean_db]
    served = [0.0] * n
    avg = [1e-6] * n
    for t in range(ttis):
        rates = [B_EFF * efficiency(rng.expovariate(1.0) * mean_lin[k]) for k in range(n)]
        if policy == "RR":
            k = t % n
        elif policy == "MaxCI":
            k = max(range(n), key=lambda i: rates[i])
        elif policy == "PF":
            k = max(range(n), key=lambda i: rates[i] / avg[i])
        else:
            raise ValueError(policy)
        for i in range(n):
            r = rates[i] if i == k else 0.0
            avg[i] = (1 - 1 / tc) * avg[i] + r / tc
        served[k] += rates[k]
    thr = [s / ttis / 1e6 for s in served]
    return thr, sum(thr), jain(thr)

def results():
    return {p: simulate(p) for p in ("RR", "PF", "MaxCI")}

if __name__ == "__main__":
    for p, (thr, tot, j) in results().items():
        print(f"{p:6s} users={['%.2f' % v for v in thr]} total={tot:.2f} Mbit/s Jain={j:.3f}")
