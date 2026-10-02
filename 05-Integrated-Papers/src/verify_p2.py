# -*- coding: utf-8 -*-
"""Paper II, pass 1 -- brute force straight from each statement.
Equations: sign-change scan + bisection. Integer conditions: exhaustive search.
One-or-more-correct items: every option statement evaluated numerically; for the
general statement (Q14) each option is tested on 2000 random distinct GPs."""
import random
from math import sqrt, log, floor, isclose
import numpy as np
from numsolve import roots
import bank_p2 as bank

TOL = 1e-7
lg = lambda x, b: log(x) / log(b)
cbrt = lambda t: np.cbrt(t)
close = lambda a, b: abs(a - b) < TOL * max(1, abs(a), abs(b))

V = {}

# Q1
u, v = cbrt(7 + 5 * sqrt(2)), cbrt(7 - 5 * sqrt(2))
r1, r2 = u + v, u * v
p, q = -(r1 + r2), r1 * r2
V[1] = abs(q * q / p)

# Q2 -- scan c > 0, everything else forced
def f2(c):
    a, e = 1.0, 25.0
    b = 2 * c - a if False else (a + c) / 2      # a,b,c AP
    d = c * c / b                                 # b,c,d GP
    return 2 / d - (1 / c + 1 / e)                # c,d,e HP
r = roots(f2, 1e-6, 1e4, 400000, True)
r = [c for c in r if (1 + c) / 2 > 0]
assert len(r) == 1, r
V[2] = r[0]

# Q3
x = y = 0.0
for _ in range(300):
    x, y = sqrt(12 + x), sqrt(72 + y)
g = sqrt(x * y)
V[3] = lg(x * y, g)

# Q4 -- exact integers, and the given 4-figure logs must agree
big = 6 ** 10
d = len(str(big))
z = d - 1                       # 1/N, N not a power of 10, has digits(N)-1 leading zeros
assert big % 10 != 0
from fractions import Fraction
s, zz = Fraction(1, big), 0
while s * 10 < 1:
    s *= 10; zz += 1
assert zz == z
lg6 = 0.3010 + 0.4771
assert floor(10 * lg6) + 1 == d and -floor(-10 * lg6) - 1 == z
V[4] = d - z

# Q5
B5 = sqrt(9 + 4 * sqrt(5))
al, be = sorted(np.roots([1, -B5, sqrt(5)]).real, reverse=True)
V[5] = (al - be) / (1 / 3)

# Q6
r6 = roots(lambda x: lg(x, 5) ** 2 - lg(x ** 3, 5) + 2, 1e-6, 1e6, 400000, True)
assert len(r6) == 2
x1, x2 = r6
V[6] = lg(x2 * x2 / x1, 5) + 4

# Q7 -- scan ratio > 0
rr = roots(lambda t: sqrt(2) * t ** 6 - 8 * sqrt(2), 1e-6, 100, 400000, True)
assert len(rr) == 1
terms = [sqrt(2) * rr[0] ** n for n in range(7)]
a4 = terms[3]
k = (a4 * a4 + 8) / a4
other = k - a4
assert any(close(other, t) for t in terms)
V[7] = k

# Q8
base = lambda x: x * x - 7 * x + 11
ex = lambda x: x * x - 13 * x + 42
sols = set()
for rt in roots(lambda x: ex(x) * log(base(x)), -60, 60, 400001):
    sols.add(round(rt, 9))
for rt in roots(ex, -60, 60) + roots(lambda x: base(x) - 1, -60, 60):
    if base(rt) > 0: sols.add(round(rt, 9))
for rt in roots(lambda x: base(x) + 1, -60, 60):
    e = ex(rt)
    if abs(e - round(e)) < 1e-9 and round(e) % 2 == 0: sols.add(round(rt, 9))
T = sum(sols)
rT = sqrt(T / 3)
V[8] = lg(T, rT)

# ---------------- Section II: compute truth of each option
TR = {}
a, b = sqrt(8 + 2 * sqrt(15)), sqrt(8 - 2 * sqrt(15))
TR[9] = [close(a + b, 2 * sqrt(5)), close(a * b, 2),
         close(a * a - 2 * sqrt(5) * a + 2, 0) and close(b * b - 2 * sqrt(5) * b + 2, 0),
         close(a + b, 4)]

# Q10 -- scan r in (-1,1) for the two sum conditions
def f10(r):
    a = 5 * (1 - r)
    return a * a / (1 - r * r) - 15
r10 = roots(f10, -0.999999, 0.999999, 400001)
assert len(r10) == 1, r10
r = r10[0]; a = 5 * (1 - r)
cubes = sum((a * r ** n) ** 3 for n in range(400))
TR[10] = [close(r, 0.25), close(a, 15 / 4), close(cubes, 375 / 13), close(a * r * r, 15 / 64)]

r11 = roots(lambda x: lg(x, 3) ** 2 - 4 * lg(x, 3) + 3, 1e-6, 1e6, 400000, True)
x2, x1 = r11
TR[11] = [close(lg(x1, 3) + lg(x2, 3), 3), close(x1 * x2, 81), close(81, x1 * x2), close(x1 - x2, 24)]

p, q = sqrt(14 + 6 * sqrt(5)), sqrt(14 - 6 * sqrt(5))
TR[12] = [close(p + q, 6), close(p * q, 2), close(4, p * q),
          close(p * p - 6 * p + 4, 0) and close(q * q - 6 * q + 4, 0)]

al, be = sorted(np.roots([1, -6, 7]).real, reverse=True)
TR[13] = [close(al - be, 2 * sqrt(2)), close(al * be, 7),
          close(2 * al * be, (al + be) + (al - be)), close(lg(be, al), -1)]

# Q14 -- general statement: an option is "correct" iff it holds in every trial
rnd = random.Random(7)
ok = [True] * 4
for _ in range(2000):
    while True:
        a, r, N = rnd.uniform(0.05, 9), rnd.uniform(0.05, 4), rnd.uniform(0.05, 50)
        b, c = a * r, a * r * r
        if min(abs(a - 1), abs(b - 1), abs(c - 1), abs(N - 1), abs(r - 1)) > 1e-3:
            break
    la, lb, lc = lg(N, a), lg(N, b), lg(N, c)
    ok[0] &= close(2 / lb, 1 / la + 1 / lc)
    ok[1] &= close(2 * b, a + c)
    ok[2] &= close(b ** 4, a * a * c * c)
    ok[3] &= close(2 * lb, la + lc)
TR[14] = ok

# ---------------- Section III
# Q15 -- search a, b>0 on a grid of log_a b = t: equations identical iff t = 1/t
cands = []
for t in np.linspace(-5, 5, 100001):
    if abs(t) < 1e-9: continue
    if abs(t - 1 / t) < 1e-9:                                # coefficients agree
        disc = t * t - 4 / t
        if disc >= 0:
            cands.append(t)
cands = sorted({round(c, 6) for c in cands})
assert cands == [-1.0], cands
a = 3.7; b = a ** cands[0]
al, be = sorted(np.roots([1, lg(b, a), lg(a, b)]).real, reverse=True)
V[15] = (al - be) + a * b

a, c = 7 + 4 * sqrt(3), 7 - 4 * sqrt(3)
b = 2 * a * c / (a + c)
V[16] = (b + lg(a, 2 + sqrt(3))) / 2

al, be = np.roots([1, -(sqrt(5) + sqrt(3)), sqrt(15)]).real
V[17] = 2 * al * be / (al + be)

r18 = roots(lambda x: lg(x, 2) ** 2 - lg(x * x, 2) - 8, 1e-9, 1e9, 400000, True)
assert len(r18) == 2
V[18] = sqrt(r18[0] * r18[1])

# ---------------- compare
bad = 0
for i, e in enumerate(bank.Q, 1):
    msg = ''
    if e['sec'] == 'I':
        t = V[i]
        if not close(t, e['ans']): msg = 'brute %r vs key %r' % (t, e['ans'])
        if not (abs(t - round(t)) < TOL and 0 <= round(t) <= 9): msg += ' not a digit'
        shown = '%.10g' % t
    elif e['sec'] == 'II':
        got = [j for j in range(4) if TR[i][j]]
        if got != e['ans']: msg = 'brute %s vs key %s' % (got, e['ans'])
        if not got: msg += ' NO CORRECT OPTION'
        shown = ''.join('ABCD'[j] for j in got)
    else:
        t = V[i]
        hits = [j for j, ov in enumerate(e['ov']) if close(ov, t)]
        if hits != [e['ans']]: msg = 'hits %s vs key %s' % (hits, e['ans'])
        if not close(t, e['val']): msg += ' bank value differs'
        if len({round(x, 9) for x in e['ov']}) != 4: msg += ' DUPLICATE OPTIONS'
        shown = '%.10g -> %s' % (t, 'ABCD'[hits[0]] if hits else '?')
    print('Q%-2d %-4s %-22s %s' % (i, e['sec'], shown, msg or 'OK'))
    bad += bool(msg)
print('\nPASS 1 (Paper II):', 'ALL 18 AGREE' if not bad else '%d PROBLEMS' % bad)
