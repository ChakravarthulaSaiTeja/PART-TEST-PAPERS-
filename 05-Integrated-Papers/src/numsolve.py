# -*- coding: utf-8 -*-
"""Sign-change root scanner shared by the brute-force passes."""
import numpy as np


def roots(f, lo, hi, n=400000, logscale=False):
    """all simple roots of f on [lo,hi] by sign change + bisection, plus exact-zero
    grid hits; returns sorted, de-duplicated list."""
    xs = np.geomspace(lo, hi, n) if logscale else np.linspace(lo, hi, n)
    out = []
    prev_x, prev_v = None, None
    for x in xs:
        try:
            v = f(x)
        except (ValueError, ZeroDivisionError, OverflowError):
            prev_x, prev_v = None, None
            continue
        if v == 0:
            out.append(x)
        elif prev_v is not None and prev_v * v < 0:
            a, b = prev_x, x
            try:
                for _ in range(200):
                    m = (a + b) / 2
                    fm = f(m)
                    if fm == 0:
                        a = b = m; break
                    if (f(a) < 0) == (fm < 0):
                        a = m
                    else:
                        b = m
                r = (a + b) / 2
                if abs(f(r)) < 1e-6:      # reject poles
                    out.append(r)
            except (ValueError, ZeroDivisionError, OverflowError):
                pass                      # bracket straddles a pole
        prev_x, prev_v = x, v
    out.sort()
    ded = []
    for r in out:
        if not ded or abs(r - ded[-1]) > 1e-6 * max(1, abs(r)):
            ded.append(r)
    return ded


