# -*- coding: utf-8 -*-
"""Pass 1 -- brute force straight from each statement.
No hand method is reused: equations are solved by sign-change scanning +
bisection, integer conditions by exhaustive search, nested radicals by
iteration. Then: the computed value must equal the bank value, and exactly one
printed option must match it (and it must be the keyed one)."""
import math
import numpy as np
from math import sqrt, log
import bank

TOL = 1e-7


def lg(x, b):
    return log(x) / log(b)


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


def int_quadratic_for(s, R=60):
    hits = [(p, q) for p in range(-R, R + 1) for q in range(-R, R + 1)
            if abs(s * s + p * s + q) < 1e-9]
    assert len(hits) == 1, hits
    return hits[0]


V = {}

# Q1
s = (sqrt(3 - 2 * sqrt(2)) + sqrt(5 - 2 * sqrt(6)) + sqrt(7 - 4 * sqrt(3))
     + sqrt(9 - 4 * sqrt(5)) + sqrt(11 - 2 * sqrt(30)))
p, q = int_quadratic_for(s)
V[1] = 2 * q - p

# Q2 -- positive base: solve g(x)*ln(base)=0 by scanning; negative base: integer
# exponents only, test every grid point where the exponent is an integer.
def base(x): return x * x - 5 * x + 5
def ex(x): return x * x - 9 * x + 20
sols = set()
# positive base region: h(x)=ex*ln(base)
h = lambda x: ex(x) * log(base(x))
for r in roots(h, -50, 50, 400001):
    sols.add(round(r, 9))
# also exact zeros of h on intervals where it touches without sign change:
for r in roots(lambda x: ex(x), -50, 50) + roots(lambda x: base(x) - 1, -50, 50):
    if base(r) > 0:
        sols.add(round(r, 9))
# negative base: exponent must be an integer; base^int must be 1 => |base|=1 & even
for r in roots(lambda x: base(x) + 1, -50, 50):
    e = ex(r)
    if abs(e - round(e)) < 1e-9 and round(e) % 2 == 0:
        sols.add(round(r, 9))
# sanity: other negative-base points with integer exponent cannot give 1 unless |base|=1
S = sum(sols)
n = (S - 3) / 4 + 1
assert abs(n - round(n)) < 1e-9
V[2] = log(S + 1, 2) + round(n)

# Q3
a3, b3 = sqrt(3) + sqrt(2), sqrt(3) - sqrt(2)
r3 = roots(lambda x: lg(x, a3) * lg(x, b3) + 4, 1e-6, 1e6, 400000, True)
assert len(r3) == 2, r3
x1, x2 = max(r3), min(r3)
V[3] = x1 + x2 + sqrt(x1 * x2)

# Q4
a4, b4 = sqrt(5) + 2, sqrt(5) - 2
r4 = [r for r in roots(lambda x: lg(x, a4) + lg(x, b4) - 4, 1e-9, 1e9, 400000, True)
      if abs(r - 1) > 1e-9]
N4 = len(r4)
V[4] = (12 - N4) / 4

# Q5
r5 = roots(lambda x: 2 * lg(x + 2, 2) - lg(x, 2) - lg(3 * x + 2, 2), 1e-9, 1e6, 400000, True)
assert len(r5) == 1, r5
x5 = r5[0]
V[5] = (x5 / 0.25) ** (1 / 3)

# Q6
S6 = sum(2 * (1 / sqrt(2)) ** k for k in range(400))
p, q = int_quadratic_for(S6)
V[6] = p + q

# Q7
r7 = roots(lambda x: lg(x, 10) ** 2 - lg(100 * x * x, 10), 1e-6, 1e6, 400000, True)
P7 = 1.0
for r in r7: P7 *= r
V[7] = (lg(P7, 10) + 8) / 2

# Q8
al, be = sorted(np.roots([1, -2, -1]).real, reverse=True)
V[8] = 2 * 20 * sqrt(2) - (al ** 3 - be ** 3)

# Q9 -- every integer pair (t1,t2) gives k=t1+t2-2 and must satisfy t1t2=2k+1
ks = sorted({t1 + t2 - 2 for t1 in range(-300, 301) for t2 in range(t1, 301)
             if t1 * t2 == 2 * (t1 + t2 - 2) + 1})
assert len(ks) == 2, ks
V[9] = (ks[0] + ks[1]) / 2

# Q10 -- scan ratio r (b=ar, c=ar^2) for 4b-a-3c=0
r10 = [r for r in roots(lambda r: 4 * r - 1 - 3 * r * r, -10, 10, 400001)
       if abs(r - 1) > 1e-9 and abs(r) > 1e-12]
assert len(r10) == 1, r10
V[10] = sqrt(2) / (1 - r10[0])

# Q11
r11 = roots(lambda x: lg(x, 3) + lg(3, x) - 2.5, 1e-6, 1e6, 400000, True)
r11 = [r for r in r11 if abs(r - 1) > 1e-6]
assert len(r11) == 2, r11
V[11] = (lg(r11[0] * r11[1], 3) + 10) / 2

# Q12
A = B = 0.0
for _ in range(200):
    A, B = sqrt(2 + A), sqrt(6 + B)
G = sqrt(A * B)
V[12] = lg(A + B + G * G - 3, 2)

# Q13
d13 = sqrt(19 + 6 * sqrt(2)) - sqrt(19 - 6 * sqrt(2))
V[13] = 16 / d13

# Q14
r14 = roots(lambda x: 2 * lg(x, 3) - lg(x + 6, 3) - 1, 1e-9, 1e6, 400000, True)
V[14] = len(r14) + sum(r14)

# Q15 -- scan d>0 (a<b<c), b from the sum
def f15(d):
    b = 5.0
    return (b - d) ** 2 + b * b + (b + d) ** 2 - 83
r15 = roots(f15, 1e-9, 100, 400001)
assert len(r15) == 1
V[15] = sqrt((5 - r15[0]) * (5 + r15[0]))

# Q16 -- every integer x >= 1 up to 10^5
cnt = 0
for x in range(1, 100001):
    u = sqrt(x - 1)
    a, b = x + 3 - 4 * u, x + 8 - 6 * u
    a, b = max(a, 0.0), max(b, 0.0)      # rounding guard at perfect squares
    if abs(sqrt(a) + sqrt(b) - 1) < 1e-9:
        cnt += 1
V[16] = sqrt(cnt / (2 / 3))

# Q17
r17 = roots(lambda x: 4 ** x - 3 * 2 ** (x + 1) + 8, -30, 30, 400001)
assert len(r17) == 2, r17
d17 = sum(r17) - 1
V[17] = 1 + 4 * d17

# Q18
u, v = 3 + 2 * sqrt(2), 3 - 2 * sqrt(2)
Gm, Hm = sqrt(u * v), 2 * u * v / (u + v)
V[18] = lg(sqrt(Gm / Hm * 27), 3)

# Q19
al, be = np.roots([1, -4, 2]).real
V[19] = 2 * lg((al - be) ** 2, 2) - lg(al * be, 2)

# Q20
x20 = 1.0
for k in range(2, 64):
    x20 *= lg(k + 1, k)
V[20] = x20 * sqrt(x20 ** 2 + 13)

# Q21 -- exact big integers / fractions, then also with the given 4-figure logs
from fractions import Fraction
big = 18 ** 15
d = len(str(big))
small = Fraction(1, big)
z = 0
while small * 10 < 1:
    small *= 10; z += 1
lg18 = 0.3010 + 2 * 0.4771              # the values the question supplies
assert math.floor(15 * lg18) + 1 == d    # digits from the given logs agree
assert (-math.floor(-15 * lg18)) - 1 == z  # zeros = |characteristic| - 1
V[21] = (d + z - 1) / 3 + 1

# Q22
al, be = sorted(np.roots([1, -6, 4]).real, reverse=True)
m22 = (al ** 3 - be ** 3) / sqrt(5)
V[22] = log(m22, 2) + 1

# Q23 -- scan r>0 with a = 13/(1+r+r^2)
def f23(r):
    a = 13 / (1 + r + r * r)
    return a * a * (1 + r * r + r ** 4) - 91
r23 = roots(f23, 1e-6, 1e6, 400000, True)
Ms = []
for r in r23:
    a = 13 / (1 + r + r * r)
    Ms.append(max(a, a * r, a * r * r))
assert all(abs(M - Ms[0]) < 1e-9 for M in Ms), Ms
V[23] = lg(Ms[0], 3)

# Q24
a24, b24 = lg(18, 12), lg(54, 24)
m24 = a24 * b24 + 5 * (a24 - b24)
V[24] = 12 / 3 - m24

# Q25 -- terms T3, T7 given
d25 = (5 * sqrt(2) - sqrt(2)) / 4
a25 = sqrt(2) - 2 * d25
V[25] = (a25 + 14 * d25) / sqrt(2) + sqrt(2) * 5 * sqrt(2)

# ------------------------------------------------------------ compare
bad = 0
for i, e in enumerate(bank.Q, 1):
    t = V[i]
    ok_val = abs(t - e['val']) < TOL * max(1, abs(t))
    msg = ''
    if e['sec'] == 'A':
        hits = [j for j, ov in enumerate(e['ov']) if abs(ov - t) < TOL * max(1, abs(t))]
        if hits != [e['ans']]:
            msg = 'option hits %s, keyed %s' % (hits, e['ans'])
        if len(set(round(x, 9) for x in e['ov'])) != 4:
            msg += ' DUPLICATE OPTION VALUES'
    else:
        if abs(t - round(t)) > TOL:
            msg = 'non-integer numerical answer'
    if not ok_val:
        msg += ' bank value %r != brute %r' % (e['val'], t)
    print('Q%-2d  brute=%-14.10g %s' % (i, t, msg or 'OK'))
    bad += bool(msg)
print('\nPASS 1:', 'ALL 25 AGREE' if not bad else '%d PROBLEMS' % bad)
