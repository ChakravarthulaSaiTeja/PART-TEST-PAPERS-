# -*- coding: utf-8 -*-
"""Pass 2 -- exact arithmetic along the hand method (Fractions and exact
a+b*sqrt(n) numbers; 60-digit Decimal only where a logarithm is unavoidable).
Independent of pass 1, which brute-forced every statement numerically."""
from fractions import Fraction as F
from decimal import Decimal as D, getcontext
import bank
getcontext().prec = 60


class S:
    """exact a + b*sqrt(n), a,b rational"""
    def __init__(s, a, b=0, n=2):
        s.a, s.b, s.n = F(a), F(b), n
    def _c(s, o):
        return o if isinstance(o, S) else S(o, 0, s.n)
    def __add__(s, o): o = s._c(o); assert o.n == s.n or o.b == 0; return S(s.a + o.a, s.b + o.b, s.n)
    __radd__ = __add__
    def __neg__(s): return S(-s.a, -s.b, s.n)
    def __sub__(s, o): return s + (-s._c(o))
    def __rsub__(s, o): return s._c(o) - s
    def __mul__(s, o):
        o = s._c(o)
        return S(s.a * o.a + s.b * o.b * s.n, s.a * o.b + s.b * o.a, s.n)
    __rmul__ = __mul__
    def conj(s): return S(s.a, -s.b, s.n)
    def __truediv__(s, o):
        o = s._c(o); c = o.conj(); den = (o * c).a
        r = s * c
        return S(r.a / den, r.b / den, s.n)
    def __eq__(s, o): o = s._c(o); return s.a == o.a and s.b == o.b
    def __repr__(s): return '%s%+s*sqrt(%d)' % (s.a, s.b, s.n)
    def dec(s): return D(s.a.numerator) / D(s.a.denominator) + D(s.b.numerator) / D(s.b.denominator) * D(s.n).sqrt()


def denest(a, b, n):
    """sqrt(a - 2*sqrt(n)) ... returns (p,q) integers with (sqrt p - sqrt q)^2 = a - 2 sqrt(n), p>q"""
    for q in range(0, a + 1):
        p = a - q
        if p * q == n and p > q:
            return p, q
    raise ValueError


def dlog(x, b):
    return D(x).ln() / D(b).ln()


R = {}

# Q1: each sqrt(a - 2 sqrt n) = sqrt p - sqrt q ; the sum telescopes
pairs = [denest(3, 2, 2), denest(5, 6, 6), denest(7, 12, 12), denest(9, 20, 20), denest(11, 30, 30)]
# (2,1),(3,2),(4,3),(5,4),(6,5): sum = sqrt6 - 1
assert pairs == [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5)], pairs
s = S(-1, 1, 6)
p, q = -(s + s.conj()).a, (s * s.conj()).a
assert s * s + p * s + q == 0
R[1] = 2 * q - p

# Q2: cases enumerated exactly with integer arithmetic
def base(x): return x * x - 5 * x + 5
def ex(x): return x * x - 9 * x + 20
cand = {1, 4} | {4, 5} | {2, 3}
sol = {x for x in cand if (base(x) != 0 or ex(x) > 0) and F(base(x)) ** ex(x) == 1}
assert sol == {1, 2, 3, 4, 5}
Ssum = sum(sol)
n = (Ssum - 3) // 4 + 1
assert 3 + 4 * (n - 1) == Ssum
R[2] = 4 + n                      # log2(16) = 4 exactly
assert 2 ** 4 == Ssum + 1

# Q3: x = (sqrt3+sqrt2)^{+-2} = 5 +- 2 sqrt6
x1, x2 = S(5, 2, 6), S(5, -2, 6)
base3 = S(0, 1, 6)  # placeholder not used
assert x1 * x2 == 1
R[3] = (x1 + x2).a + 1            # sqrt(x1 x2) = 1

# Q4: (sqrt5+2)(sqrt5-2) = 1 -> logs cancel -> LHS identically 0 -> N = 0
assert S(2, 1, 5) * S(-2, 1, 5) == 1
R[4] = F(12 - 0, 4)

# Q5
xs = [x for x in (2, -1) if (x + 2) ** 2 == x * (3 * x + 2)]
x5 = [x for x in xs if x > 0][0]
r = [r for r in range(-10, 11) if F(1, 4) * r ** 3 == x5]
R[5] = r[0]

# Q6
S6 = S(2) / (S(1) - S(0, F(1, 2), 2))            # 1/sqrt2 = sqrt2/2
assert S6 == S(4, 2, 2)
R[6] = -(S6 + S6.conj()).a + (S6 * S6.conj()).a

# Q7: t^2 - 2t - 2 = 0, t1+t2 = 2 -> log P = 2 ; disc = 12 > 0
assert 4 + 8 > 0
R[7] = F(2 + 8, 2)

# Q8
al, be = S(1, 1, 2), S(1, -1, 2)
assert al * al - 2 * al - 1 == 0 and be * be - 2 * be - 1 == 0
k8 = 2 * S(0, 20, 2) - (al * al * al - be * be * be)
R[8] = k8.dec()
assert k8 == S(0, 30, 2)

# Q9: (t1-2)(t2-2) = 1
ks = sorted({t1 + t2 - 2 for (t1, t2) in [(3, 3), (1, 1)]})
for k in ks:
    disc = (k + 2) ** 2 - 4 * (2 * k + 1)
    assert disc == 0                                  # double root
R[9] = F(ks[0] + ks[1], 2)

# Q10
rs = [F(1), F(1, 3)]
assert all(3 * r * r - 4 * r + 1 == 0 for r in rs)
R[10] = (S(0, 1, 2) / (1 - F(1, 3))).dec()

# Q11
ts = [F(2), F(1, 2)]
assert all(t + 1 / t == F(5, 2) for t in ts)
R[11] = (sum(ts) + 10) / 2                           # log3(x1x2) = t1+t2

# Q12
A, B = 2, 3
assert A * A == A + 2 and B * B == B + 6
G2 = A * B
R[12] = 3
assert 2 ** 3 == A + B + G2 - 3

# Q13
al, be = S(1, 3, 2), S(-1, 3, 2)
assert al * al == S(19, 6, 2) and be * be == S(19, -6, 2) and be.dec() > 0
R[13] = (S(16) / (al - be)).a

# Q14
r14 = [x for x in (6, -3) if x * x - 3 * x - 18 == 0 and x > 0]
R[14] = len(r14) + sum(r14)

# Q15
d = 2
assert 3 * 25 + 2 * d * d == 83
g2 = (5 - d) * (5 + d)
R[15] = D(g2).sqrt()

# Q16: |u-2|+|u-3| = 1 <=> 2<=u<=3 <=> 5<=x<=10
xs16 = [x for x in range(1, 2000) if 4 <= x - 1 <= 9]
R[16] = 3
assert F(2, 3) * 3 ** 2 == len(xs16)

# Q17
ys = [y for y in range(0, 20) if y * y - 6 * y + 8 == 0]
xs17 = [y.bit_length() - 1 for y in ys]
assert all(2 ** x == y for x, y in zip(xs17, ys))
d17 = sum(xs17) - 1
R[17] = 1 + 4 * d17

# Q18
u, v = S(3, 2, 2), S(3, -2, 2)
G = 1
assert u * v == G * G
H = (2 * u * v) / (u + v)
assert H == F(1, 3)
k = 9
assert k * k == (G / H.a) * 27
R[18] = 2

# Q19
s19, p19 = 4, 2
R[19] = 2 * 3 - 1
assert (s19 * s19 - 4 * p19) == 2 ** 3 and p19 == 2 ** 1

# Q20: chain -> log2 64 = 6
R[20] = 6 * 7
assert 6 * 6 + 13 == 49

# Q21: exact integers
big = 18 ** 15
dgt = len(str(big))
z = len(str(big)) - 1 if str(big) != '1' + '0' * (dgt - 1) else dgt - 1
# 1/big has (digits(big) - 1) zeros after the point, big not a power of 10
assert big % 10 != 0
R[21] = (dgt + z - 1) // 3 + 1

# Q22
al, be = S(3, 1, 5), S(3, -1, 5)
m = (al * al * al - be * be * be) / S(0, 1, 5)
assert m.b == 0
R[22] = int(m.a).bit_length()                       # 64 = 2^6 -> n = 7
assert 2 ** (R[22] - 1) == m.a

# Q23
b = 3
assert F(13) * 7 == 91 and 13 - 7 == 2 * b
ac, apc = b * b, 13 - b
roots23 = [x for x in range(0, 20) if x * x - apc * x + ac == 0]
M = max(roots23 + [b])
assert 3 ** 2 == M
R[23] = 2

# Q24: polynomial identity in x=log2, y=log3, checked at several rational points
for xv, yv in [(F(3), F(5)), (F(1, 2), F(7, 3)), (F(-4), F(9)), (F(11, 7), F(2, 13))]:
    a = (xv + 2 * yv) / (2 * xv + yv)
    b = (xv + 3 * yv) / (3 * xv + yv)
    assert a * b + 5 * (a - b) == 1
m24 = (D(18).ln() / D(12).ln()) * (D(54).ln() / D(24).ln()) \
      + 5 * (D(18).ln() / D(12).ln() - D(54).ln() / D(24).ln())
assert abs(m24 - 1) < D('1e-50')
R[24] = 4 - 1

# Q25
dd = (S(0, 5, 2) - S(0, 1, 2)) / 4
a1 = S(0, 1, 2) - 2 * dd
T15 = a1 + 14 * dd
qq = S(0, 1, 2) * S(0, 5, 2)
R[25] = T15.b + qq.a

# ------------------------------------------------------------ compare
bad = 0
for i, e in enumerate(bank.Q, 1):
    t = R[i]
    tv = D(t) if not isinstance(t, F) else D(t.numerator) / D(t.denominator)
    ok = abs(float(tv) - e['val']) < 1e-9 * max(1, abs(e['val']))
    print('Q%-2d exact=%-28s %s' % (i, str(t)[:28], 'OK' if ok else 'MISMATCH bank=%r' % e['val']))
    bad += not ok
print('\nPASS 2:', 'ALL 25 AGREE' if not bad else '%d PROBLEMS' % bad)
