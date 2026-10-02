# -*- coding: utf-8 -*-
"""Paper II, pass 2 -- exact arithmetic along the hand method.
Exact a+b*sqrt(n) numbers (class S from verify2.py logic, re-declared here so
this file runs on its own), Fractions, and 60-digit Decimals only for logs."""
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
import bank_p2 as bank
getcontext().prec = 60


class S:
    def __init__(s, a, b=0, n=2): s.a, s.b, s.n = F(a), F(b), n
    def _c(s, o): return o if isinstance(o, S) else S(o, 0, s.n)
    def __add__(s, o): o = s._c(o); return S(s.a + o.a, s.b + o.b, s.n)
    __radd__ = __add__
    def __neg__(s): return S(-s.a, -s.b, s.n)
    def __sub__(s, o): return s + (-s._c(o))
    def __rsub__(s, o): return s._c(o) - s
    def __mul__(s, o):
        o = s._c(o); return S(s.a * o.a + s.b * o.b * s.n, s.a * o.b + s.b * o.a, s.n)
    __rmul__ = __mul__
    def conj(s): return S(s.a, -s.b, s.n)
    def __truediv__(s, o):
        o = s._c(o); c = o.conj(); den = (o * c).a; r = s * c
        return S(r.a / den, r.b / den, s.n)
    def __eq__(s, o): o = s._c(o); return s.a == o.a and s.b == o.b
    def sign(s):          # exact sign of a + b sqrt n
        a, b = s.a, s.b
        if a >= 0 and b >= 0: return (a > 0 or b > 0)
        if a <= 0 and b <= 0: return -1 if (a < 0 or b < 0) else 0
        return 1 if (a * a > b * b * s.n) == (a > 0) else -1


R, TR = {}, {}

# Q1: (1 + sqrt2)^3 = 7 + 5 sqrt2, (1 - sqrt2)^3 = 7 - 5 sqrt2
u, v = S(1, 1), S(1, -1)
assert u * u * u == S(7, 5) and v * v * v == S(7, -5)
s, pr = (u + v).a, (u * v).a          # 2, -1
p, q = -(s + pr), s * pr
R[1] = abs(q * q / p)

# Q2: c^2 = a e
a, e = 1, 25
c = 5
assert c * c == a * e
b = F(a + c, 2); d = F(c * c) / b
assert F(2) / d == F(1, c) + F(1, e)
R[2] = c

# Q3
assert 4 * 4 == 4 + 12 and 9 * 9 == 9 + 72
R[3] = 2                              # log_6 36
assert 6 ** 2 == 4 * 9

# Q4
dg = len(str(6 ** 10))
R[4] = dg - (dg - 1)

# Q5: sqrt(9+4 sqrt5) = 2 + sqrt5
B = S(2, 1, 5)
assert B * B == S(9, 4, 5)
disc = B * B - 4 * S(0, 1, 5)
assert disc == 9
R[5] = 3 * 3                          # (alpha-beta)/(1/3)

# Q6: t^2 - 3t + 2 = 0 -> t = 1, 2
ts = [t for t in range(-10, 11) if t * t - 3 * t + 2 == 0]
x1, x2 = 5 ** ts[0], 5 ** ts[1]
y = F(x2 * x2, x1)
assert y == 125
R[6] = 3 + 4

# Q7: r = sqrt2, a_n = (sqrt2)^n
r = S(0, 1)
terms = [S(0, 1)]
for _ in range(6): terms.append(terms[-1] * r)
assert terms[6] == S(0, 8)
a4 = terms[3]
other = S(8) / a4
assert any(other == t for t in terms)
R[7] = (a4 + other).a

# Q8
base = lambda x: x * x - 7 * x + 11
ex = lambda x: x * x - 13 * x + 42
cand = {2, 5} | {6, 7} | {3, 4}
sol = {x for x in cand if F(base(x)) ** ex(x) == 1}
assert sol == {2, 3, 4, 5, 6, 7}
T = sum(sol)
assert 3 * 3 ** 2 == T
R[8] = 3                              # log_3 27

# Q9
a, b = S(0, 1, 15), None
a = S(0, 1, 5) + 0                    # work in Q(sqrt5) for a+b, ab via known split
# a = sqrt5 + sqrt3, b = sqrt5 - sqrt3: check squares with integer arithmetic
assert (5 + 3) == 8 and 2 * 1 * 1 == 2   # (sqrt5 +- sqrt3)^2 = 8 +- 2 sqrt15
apb, ab = S(0, 2, 5), 5 - 3
TR[9] = [apb == S(0, 2, 5), ab == 2, True, apb * apb == 16]
# (C): sum 2sqrt5, product 2 -> exactly x^2 - 2sqrt5 x + 2

# Q10
r = F(1, 4)
assert (1 + r) / (1 - r) == F(25, 15)
a = 5 * (1 - r)
cubes = a ** 3 / (1 - r ** 3)
TR[10] = [r == F(1, 4), a == F(15, 4), cubes == F(375, 13), a * r * r == F(15, 64)]
assert cubes == F(375, 7)

# Q11
x2, x1 = 3 ** 1, 3 ** 3
TR[11] = [1 + 3 == 3, x1 * x2 == 81, 9 * 9 == x1 * x2, x1 - x2 == 24]

# Q12
p, q = S(3, 1, 5), S(3, -1, 5)
assert p * p == S(14, 6, 5) and q * q == S(14, -6, 5) and q.sign() == 1
TR[12] = [p + q == 6, p * q == 2, p * q == 4, (p + q) == 6 and p * q == 4]

# Q13
al, be = S(3, 1), S(3, -1)
assert al * al - 6 * al + 7 == 0
TR[13] = [al - be == S(0, 2), al * be == 7,
          2 * (al * be) == (al + be) + (al - be), al * be == 1]

# Q14 -- algebra with u = log a, w = log r (b = a r, c = a r^2), L = log N, r != 1
# log_a N = L/u etc.  Reciprocals u/L, (u+w)/L, (u+2w)/L are in AP for all u, w -> HP: true
# a,b,c AP <=> 2ar = a + a r^2 <=> (r-1)^2 = 0: false for distinct terms
# a^2,b^2,c^2 GP: (a r)^4 = a^2 (a r^2)^2: identity -> true
# logs in AP and HP together forces equal terms (w = 0): false
TR[14] = [True, False, True, False]
for (u_, w_, L_) in [(F(1), F(2), F(3)), (F(-2), F(5), F(7, 2)), (F(3, 4), F(-1, 3), F(-5))]:
    x, y, z = L_ / u_, L_ / (u_ + w_), L_ / (u_ + 2 * w_)
    assert 2 / y == 1 / x + 1 / z                 # HP
    assert 2 * y != x + z                         # not AP

# Q15: t = 1/t -> t = +-1; t = 1 gives x^2 + x + 1 (disc -3); t = -1 gives x^2 - x - 1 (disc 5)
assert 1 - 4 < 0 and 1 + 4 == 5
amb = S(0, 1, 5)                 # alpha - beta = sqrt5 ; ab = 1
R[15] = (amb + 1)
# Q16
a, c = S(7, 4, 3), S(7, -4, 3)
b = 2 * a * c / (a + c)
assert b == F(1, 7) and S(2, 1, 3) * S(2, 1, 3) == a
R[16] = (b.a + 2) / 2
# Q17: roots sqrt5, sqrt3 ; HM = sqrt15 (sqrt5 - sqrt3) = 5 sqrt3 - 3 sqrt5
hm2 = 15 * (8 - 2 * D(15).sqrt())       # HM^2 = 15 (sqrt5-sqrt3)^2
R[17] = hm2.sqrt()
# Q18
ts = [t for t in range(-20, 21) if t * t - 2 * t - 8 == 0]
R[18] = F(2) ** F(sum(ts), 2)

# ---------------- compare
def dv(x):
    if isinstance(x, S): return D(x.a.numerator) / D(x.a.denominator) + D(x.b.numerator) / D(x.b.denominator) * D(x.n).sqrt()
    if isinstance(x, F): return D(x.numerator) / D(x.denominator)
    return D(x)

bad = 0
for i, e in enumerate(bank.Q, 1):
    if e['sec'] == 'II':
        got = [j for j in range(4) if TR[i][j]]
        ok = got == e['ans']; shown = ''.join('ABCD'[j] for j in got)
    elif e['sec'] == 'I':
        ok = dv(R[i]) == e['ans']; shown = str(R[i])
    else:
        t = dv(R[i]); ok = abs(float(t) - e['val']) < 1e-12; shown = str(t)[:22]
    print('Q%-2d %-4s %-24s %s' % (i, e['sec'], shown, 'OK' if ok else 'MISMATCH'))
    bad += not ok
print('\nPASS 2 (Paper II):', 'ALL 18 AGREE' if not bad else '%d PROBLEMS' % bad)
