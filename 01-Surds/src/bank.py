# -*- coding: utf-8 -*-
"""Surds question bank, retyped from the Sri Chaitanya source sheet (101 Q).
Every entry carries a numeric self-check so the printed key is verified,
not trusted."""
from math import sqrt

def cbrt(x):
    return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))

def rt(x, n):
    return x ** (1.0 / n) if x >= 0 else -((-x) ** (1.0 / n))

R2, R3, R5, R6, R7 = sqrt(2), sqrt(3), sqrt(5), sqrt(6), sqrt(7)

Q = {}

def add(qid, lv, q, opts, ans, truth=None, optvals=None, chk=None, note=""):
    assert qid not in Q, qid
    assert len(opts) == 4, qid
    assert 0 <= ans <= 3, qid
    Q[qid] = dict(id=qid, lv=lv, q=q, o=opts, ans=ans,
                  truth=truth, optvals=optvals, chk=chk, note=note)

# ------------------------------------------------------------------ page 1
add(1, 'L1',
    r"$\sqrt[3]{\,9\sqrt3+11\sqrt2\,}=$",
    [r"$\sqrt3+\sqrt2$", r"$\sqrt3+1$", r"$1+\sqrt2$", r"$\sqrt3-\sqrt2$"], 0,
    truth=lambda: cbrt(9 * R3 + 11 * R2),
    optvals=[lambda: R3 + R2, lambda: R3 + 1, lambda: 1 + R2, lambda: R3 - R2])

add(2, 'L1',
    r"$\sqrt[3]{\,11\sqrt5+17\sqrt2\,}=$",
    [r"$\sqrt2+\sqrt3$", r"$\sqrt3+1$", r"$\sqrt5+\sqrt2$", r"none of these"], 2,
    truth=lambda: cbrt(11 * R5 + 17 * R2),
    optvals=[lambda: R2 + R3, lambda: R3 + 1, lambda: R5 + R2, None])

add(3, 'L1',
    r"$\sqrt[4]{\,97+56\sqrt3\,}=$",
    [r"$1+\sqrt3$", r"$2+\sqrt3$", r"$1+2\sqrt3$", r"$4+\sqrt3$"], 1,
    truth=lambda: rt(97 + 56 * R3, 4),
    optvals=[lambda: 1 + R3, lambda: 2 + R3, lambda: 1 + 2 * R3, lambda: 4 + R3])

add(4, 'L1',
    r"$\sqrt{37+12\sqrt7}-\sqrt{37-12\sqrt7}=$",
    [r"$2\sqrt7$", r"$4\sqrt7$", r"$3$", r"$6$"], 3,
    truth=lambda: sqrt(37 + 12 * R7) - sqrt(37 - 12 * R7),
    optvals=[lambda: 2 * R7, lambda: 4 * R7, lambda: 3, lambda: 6])

add(5, 'L2',
    r"$\dfrac{\sqrt2}{\sqrt{3+\sqrt5}-\sqrt{3-\sqrt5}}=$",
    [r"$1$", r"$\sqrt2$", r"$\sqrt5$", r"$2\sqrt5$"], 0,
    truth=lambda: R2 / (sqrt(3 + R5) - sqrt(3 - R5)),
    optvals=[lambda: 1, lambda: R2, lambda: R5, lambda: 2 * R5])

add(6, 'L3',
    r"$\dfrac{\sqrt{26-15\sqrt3}}{5\sqrt2-\sqrt{38+5\sqrt3}}=$",
    [r"$1$", r"$\sqrt3$", r"$\dfrac{1}{\sqrt3}$", r"$-\sqrt3$"], 2,
    truth=lambda: sqrt(26 - 15 * R3) / (5 * R2 - sqrt(38 + 5 * R3)),
    optvals=[lambda: 1, lambda: R3, lambda: 1 / R3, lambda: -R3])

add(7, 'L2',
    r"$\dfrac{3+\sqrt6}{5\sqrt3-2\sqrt{12}-\sqrt{32}+\sqrt{50}}=$",
    [r"$3$", r"$\sqrt3$", r"$\dfrac13$", r"$-\sqrt3$"], 1,
    truth=lambda: (3 + R6) / (5 * R3 - 2 * sqrt(12) - sqrt(32) + sqrt(50)),
    optvals=[lambda: 3, lambda: R3, lambda: 1 / 3, lambda: -R3])

add(8, 'L3',
    r"$\sqrt[3]{16+8\sqrt5}+\sqrt[3]{16-8\sqrt5}=$",
    [r"$1$", r"$2$", r"$\sqrt5$", r"$2\sqrt5$"], 1,
    truth=lambda: cbrt(16 + 8 * R5) + cbrt(16 - 8 * R5),
    optvals=[lambda: 1, lambda: 2, lambda: R5, lambda: 2 * R5])

add(9, 'L2',
    r"$\sqrt[3]{20+14\sqrt2}-\sqrt[3]{-20+14\sqrt2}=$",
    [r"$2$", r"$4$", r"$\sqrt2$", r"$2\sqrt2$"], 1,
    truth=lambda: cbrt(20 + 14 * R2) - cbrt(-20 + 14 * R2),
    optvals=[lambda: 2, lambda: 4, lambda: R2, lambda: 2 * R2])

# ------------------------------------------------------------------ page 2
add(10, 'L3',
    r"$\left[\sqrt[6]{13-4\sqrt3}+\sqrt[3]{\dfrac18-\dfrac{\sqrt3}{4}}\right]\sqrt[3]{1+2\sqrt3}=$",
    [r"$1$", r"$-1$", r"$\sqrt[3]{11}$", r"$\dfrac12\sqrt[3]{11}$"], 3,
    truth=lambda: (rt(13 - 4 * R3, 6) + cbrt(1 / 8 - R3 / 4)) * cbrt(1 + 2 * R3),
    optvals=[lambda: 1, lambda: -1, lambda: cbrt(11), lambda: cbrt(11) / 2])

add(11, 'L3',
    r"$\sqrt{\;\sqrt[4]{193-132\sqrt2}+\sqrt{3+2\sqrt2}\;}=$",
    [r"$0$", r"$1$", r"$2$", r"$4$"], 2,
    truth=lambda: sqrt(rt(193 - 132 * R2, 4) + sqrt(3 + 2 * R2)),
    optvals=[lambda: 0, lambda: 1, lambda: 2, lambda: 4])

add(12, 'L3',
    r"$\dfrac{1}{\sqrt{12-\sqrt{140}}}-\dfrac{1}{\sqrt{8-\sqrt{60}}}-\dfrac{2}{\sqrt{10+\sqrt{84}}}=$",
    [r"$0$", r"$1$", r"$-1$", r"$\sqrt7+\sqrt5+\sqrt2$"], 0,
    truth=lambda: 1 / sqrt(12 - sqrt(140)) - 1 / sqrt(8 - sqrt(60)) - 2 / sqrt(10 + sqrt(84)),
    optvals=[lambda: 0, lambda: 1, lambda: -1, lambda: R7 + R5 + R2])

add(13, 'L2',
    r"$\left(28-10\sqrt3\right)^{1/2}-\left(7+4\sqrt3\right)^{-1/2}=$",
    [r"$3$", r"$\sqrt3$", r"$\dfrac13$", r"$\dfrac{1}{\sqrt3}$"], 0,
    truth=lambda: (28 - 10 * R3) ** 0.5 - (7 + 4 * R3) ** -0.5,
    optvals=[lambda: 3, lambda: R3, lambda: 1 / 3, lambda: 1 / R3])

add(14, 'L3',
    r"$\sqrt{\dfrac{6+2\sqrt3}{33-19\sqrt3}}=$",
    [r"$5+\sqrt3$", r"$5+2\sqrt3$", r"$5+3\sqrt3$", r"$5+4\sqrt3$"], 2,
    truth=lambda: sqrt((6 + 2 * R3) / (33 - 19 * R3)),
    optvals=[lambda: 5 + R3, lambda: 5 + 2 * R3, lambda: 5 + 3 * R3, lambda: 5 + 4 * R3])

add(15, 'L2',
    r"$\dfrac{15}{\sqrt{10}+\sqrt{20}+\sqrt{40}-\sqrt5-\sqrt{80}}=$",
    [r"$10+\sqrt5$", r"$\sqrt{10}+5$", r"$\sqrt{10}+\sqrt5$", r"none of these"], 2,
    truth=lambda: 15 / (sqrt(10) + sqrt(20) + sqrt(40) - R5 - sqrt(80)),
    optvals=[lambda: 10 + R5, lambda: sqrt(10) + 5, lambda: sqrt(10) + R5, None])

add(16, 'L1',
    r"A rationalising factor of $\sqrt[3]{81}$ is",
    [r"$\sqrt{81}$", r"$\sqrt9$", r"$\sqrt[3]{3}$", r"$\sqrt[3]{9}$"], 3,
    chk=lambda: abs(cbrt(81) * cbrt(9) - 9.0) < 1e-9)

add(17, 'L1',
    r"A rationalising factor of $5\sqrt3-3\sqrt2$ is",
    [r"$5\sqrt3+3\sqrt2$", r"$3\sqrt2-5\sqrt3$", r"$3\sqrt5-2\sqrt3$", r"$3\sqrt5+2\sqrt3$"], 0,
    chk=lambda: abs((5 * R3 - 3 * R2) * (5 * R3 + 3 * R2) - 57.0) < 1e-9)

add(18, 'L1',
    r"A rationalising factor of $\sqrt[3]{2}+1$ is",
    [r"$\sqrt[3]{2}-1$", r"$\sqrt2-1$", r"$\sqrt[3]{4}+\sqrt[3]{2}+1$", r"$\sqrt[3]{4}-\sqrt[3]{2}+1$"], 3,
    chk=lambda: abs((cbrt(2) + 1) * (cbrt(4) - cbrt(2) + 1) - 3.0) < 1e-9)

add(19, 'L1',
    r"A rationalising factor of $\sqrt[3]{3}-1$ is",
    [r"$\sqrt[3]{3}+1$", r"$\sqrt{3+1}$", r"$\sqrt[3]{9}+\sqrt[3]{3}+1$", r"$\sqrt[3]{9}-\sqrt[3]{3}+1$"], 2,
    chk=lambda: abs((cbrt(3) - 1) * (cbrt(9) + cbrt(3) + 1) - 2.0) < 1e-9)

add(21, 'L2',
    r"A rationalising factor of $\sqrt[4]{3}+\sqrt[4]{2}$ is",
    [r"$\left(\sqrt[4]{3}-\sqrt[4]{2}\right)\left(\sqrt3-\sqrt2\right)$",
     r"$\left(\sqrt[4]{3}-\sqrt[4]{2}\right)\left(\sqrt3+\sqrt2\right)$",
     r"$\left(\sqrt[4]{3}-\sqrt[4]{2}\right)\left(\sqrt2-\sqrt3\right)$",
     r"$\left(\sqrt[4]{3}+\sqrt[4]{2}\right)\left(\sqrt3-\sqrt2\right)$"], 1,
    chk=lambda: abs((rt(3, 4) + rt(2, 4)) * (rt(3, 4) - rt(2, 4)) * (R3 + R2) - 1.0) < 1e-9)

# ------------------------------------------------------------------ page 3
add(22, 'L3',
    r"If $\left(1-\sqrt2-\sqrt3\right)^{-1}=a+b\sqrt2+c\sqrt6$, then $a+b+c=$",
    [r"$2$", r"$1$", r"$\sqrt2$", r"$0$"], 3,
    chk=lambda: abs((0.5 - 0.25 * R2 - 0.25 * R6) - 1 / (1 - R2 - R3)) < 1e-12
                and abs(0.5 - 0.25 - 0.25) < 1e-12)

add(23, 'L2',
    r"The greatest number among $\sqrt2,\ \sqrt[3]{3},\ \sqrt[5]{5}$ is",
    [r"$\sqrt2$", r"$\sqrt[3]{3}$", r"$\sqrt[5]{5}$", r"not determined"], 1,
    chk=lambda: max([R2, cbrt(3), rt(5, 5)]) == cbrt(3))

add(24, 'L2',
    r"The smallest number among $\sqrt{10}-\sqrt5,\ \sqrt{19}-\sqrt{14},\ \sqrt{22}-\sqrt{17}$ is",
    [r"$\sqrt{10}-\sqrt5$", r"$\sqrt{19}-\sqrt{14}$", r"$\sqrt{22}-\sqrt{17}$", r"not determined"], 2,
    chk=lambda: min([sqrt(10) - sqrt(5), sqrt(19) - sqrt(14), sqrt(22) - sqrt(17)])
                == sqrt(22) - sqrt(17))

add(25, 'L2',
    r"The greatest number among $\sqrt{22}+\sqrt{21},\ \sqrt{23}+\sqrt{20},\ \sqrt{24}+\sqrt{19}$ is",
    [r"$\sqrt{22}+\sqrt{21}$", r"$\sqrt{23}+\sqrt{20}$", r"$\sqrt{24}+\sqrt{19}$", r"not determined"], 0,
    chk=lambda: max([sqrt(22) + sqrt(21), sqrt(23) + sqrt(20), sqrt(24) + sqrt(19)])
                == sqrt(22) + sqrt(21))

add(26, 'L3',
    r"$\dfrac{2}{\sqrt[3]{9}-\sqrt[3]{3}+1}-\dfrac{1}{\sqrt[3]{9}+\sqrt[3]{3}+1}=$",
    [r"$1$", r"$-1$", r"$\sqrt[3]{3}$", r"$-\sqrt[3]{3}$"], 0,
    truth=lambda: 2 / (cbrt(9) - cbrt(3) + 1) - 1 / (cbrt(9) + cbrt(3) + 1),
    optvals=[lambda: 1, lambda: -1, lambda: cbrt(3), lambda: -cbrt(3)])

add(27, 'L1',
    r"If $\sqrt{20+x\sqrt6}=\sqrt{12}+\sqrt8$, then $x=$",
    [r"$4$", r"$6$", r"$8$", r"$16$"], 2,
    chk=lambda: abs(sqrt(20 + 8 * R6) - (sqrt(12) + sqrt(8))) < 1e-12)

add(28, 'L3',
    r"If $\left(4+\sqrt{15}\right)^{3/2}+\left(4-\sqrt{15}\right)^{3/2}=x\sqrt{10}$, then $x=$",
    [r"$4$", r"$5$", r"$7$", r"$10$"], 2,
    truth=lambda: ((4 + sqrt(15)) ** 1.5 + (4 - sqrt(15)) ** 1.5) / sqrt(10),
    optvals=[lambda: 4, lambda: 5, lambda: 7, lambda: 10])

add(29, 'L3',
    r"If $\left(6+\sqrt{35}\right)^{3/2}+\left(6-\sqrt{35}\right)^{3/2}=x\sqrt{14}$, then $x=$",
    [r"$6$", r"$9$", r"$11$", r"$13$"], 2,
    truth=lambda: ((6 + sqrt(35)) ** 1.5 + (6 - sqrt(35)) ** 1.5) / sqrt(14),
    optvals=[lambda: 6, lambda: 9, lambda: 11, lambda: 13])

add(30, 'L3',
    r"If $\sqrt[3]{a+\sqrt b}=7+4\sqrt3$, then $\sqrt[3]{a^{2}-b}=$",
    [r"$0$", r"$1$", r"$-1$", r"$7$"], 1,
    chk=lambda: abs(cbrt(((7 + 4 * R3) ** 3 + (7 - 4 * R3) ** 3) ** 2 / 4
                         - ((7 + 4 * R3) ** 3 - (7 - 4 * R3) ** 3) ** 2 / 4) - 1.0) < 1e-6)

add(31, 'L1',
    r"If $x=\dfrac{2}{3+\sqrt7}$, then $(x-3)^{2}=$",
    [r"$1$", r"$3$", r"$7$", r"$6$"], 2,
    truth=lambda: (2 / (3 + R7) - 3) ** 2,
    optvals=[lambda: 1, lambda: 3, lambda: 7, lambda: 6])

add(32, 'L1',
    r"If $x=4-\sqrt{15}$, then $x^{2}-8x+5=$",
    [r"$0$", r"$1$", r"$4$", r"$6$"], 2,
    truth=lambda: (4 - sqrt(15)) ** 2 - 8 * (4 - sqrt(15)) + 5,
    optvals=[lambda: 0, lambda: 1, lambda: 4, lambda: 6])

add(33, 'L1',
    r"If $x=2\sqrt2+\sqrt7$, then $x-\sqrt7=$",
    [r"$2\sqrt2$", r"$4\sqrt2$", r"$8$", r"$\sqrt7$"], 0,
    truth=lambda: 2 * R2 + R7 - R7,
    optvals=[lambda: 2 * R2, lambda: 4 * R2, lambda: 8, lambda: R7])

add(34, 'L2',
    r"If $x=\dfrac{\sqrt2+1}{\sqrt2-1}$, then $x^{3}+\dfrac{1}{x^{3}}=$",
    [r"$112$", r"$192$", r"$198$", r"$216$"], 2,
    truth=lambda: (lambda x: x ** 3 + 1 / x ** 3)((R2 + 1) / (R2 - 1)),
    optvals=[lambda: 112, lambda: 192, lambda: 198, lambda: 216])

# ------------------------------------------------------------------ page 4
add(35, 'L2',
    r"If $x=\dfrac{\sqrt3-\sqrt2}{\sqrt3+\sqrt2}$, then $x^{4}+\dfrac{1}{x^{4}}=$",
    [r"$8642$", r"$9602$", r"$10104$", r"$11132$"], 1,
    truth=lambda: (lambda x: x ** 4 + 1 / x ** 4)((R3 - R2) / (R3 + R2)),
    optvals=[lambda: 8642, lambda: 9602, lambda: 10104, lambda: 11132])

add(36, 'L2',
    r"If $x=2-\sqrt3$, then $x^{4}-4x^{3}+2x^{2}-4x+5=$",
    [r"$0$", r"$4$", r"$-4$", r"$6$"], 1,
    truth=lambda: (lambda x: x ** 4 - 4 * x ** 3 + 2 * x ** 2 - 4 * x + 5)(2 - R3),
    optvals=[lambda: 0, lambda: 4, lambda: -4, lambda: 6],
    note="source printed '-5', which matches no option; reconstructed as '+5'")

add(37, 'L3',
    r"If $x=3^{2/3}+3^{-2/3}$, then $9x^{3}-27x=$",
    [r"$82$", r"$73$", r"$63$", r"$56$"], 0,
    truth=lambda: (lambda x: 9 * x ** 3 - 27 * x)(3 ** (2 / 3) + 3 ** (-2 / 3)),
    optvals=[lambda: 82, lambda: 73, lambda: 63, lambda: 56])

add(38, 'L3',
    r"If $x=\sqrt2+\sqrt3$, then $x^{4}-10x^{2}+1=$",
    [r"$0$", r"$1$", r"$-1$", r"$2$"], 0,
    truth=lambda: (lambda x: x ** 4 - 10 * x ** 2 + 1)(R2 + R3),
    optvals=[lambda: 0, lambda: 1, lambda: -1, lambda: 2],
    note="replaces the source Cardano-formula item, which needs machinery "
         "beyond the class-8 toolkit")

add(39, 'L1',
    r"If $x=\sqrt{7+4\sqrt3}$, then $x+\dfrac1x=$",
    [r"$4$", r"$6$", r"$3$", r"$2$"], 0,
    truth=lambda: (lambda x: x + 1 / x)(sqrt(7 + 4 * R3)),
    optvals=[lambda: 4, lambda: 6, lambda: 3, lambda: 2])

add(40, 'L2',
    r"If $x=\dfrac{\sqrt5+\sqrt2}{\sqrt5-\sqrt2}$ and $y=\dfrac{\sqrt5-\sqrt2}{\sqrt5+\sqrt2}$, "
    r"then $3x^{2}-4xy+3y^{2}=$",
    [r"$0$", r"$\dfrac{196}{3}$", r"$\dfrac{166}{3}$", r"$\dfrac{133}{3}$"], 2,
    truth=lambda: (lambda x, y: 3 * x * x - 4 * x * y + 3 * y * y)(
        (R5 + R2) / (R5 - R2), (R5 - R2) / (R5 + R2)),
    optvals=[lambda: 0, lambda: 196 / 3, lambda: 166 / 3, lambda: 133 / 3])

add(41, 'L2',
    r"If $x=\dfrac{\sqrt7-\sqrt5}{\sqrt7+\sqrt5}$ and $y=\dfrac{\sqrt7+\sqrt5}{\sqrt7-\sqrt5}$, "
    r"then $x^{3}+y^{3}=$",
    [r"$142$", r"$1456$", r"$1692$", r"$1894$"], 2,
    truth=lambda: (lambda x, y: x ** 3 + y ** 3)(
        (R7 - R5) / (R7 + R5), (R7 + R5) / (R7 - R5)),
    optvals=[lambda: 142, lambda: 1456, lambda: 1692, lambda: 1894])

add(42, 'L1',
    r"If $x=\dfrac{3}{\sqrt5-\sqrt2}$ and $y=\dfrac{3}{\sqrt5+\sqrt2}$, then $x^{2}-2xy+y^{2}=$",
    [r"$2\sqrt2$", r"$2\sqrt5$", r"$20$", r"$8$"], 3,
    truth=lambda: (3 / (R5 - R2) - 3 / (R5 + R2)) ** 2,
    optvals=[lambda: 2 * R2, lambda: 2 * R5, lambda: 20, lambda: 8])

add(43, 'L2',
    r"If $x=7+4\sqrt3$ and $xy=1$, then $\dfrac{1}{x^{2}}+\dfrac{1}{y^{2}}=$",
    [r"$64$", r"$134$", r"$194$", r"$\dfrac{1}{49}$"], 2,
    truth=lambda: (lambda x, y: 1 / x ** 2 + 1 / y ** 2)(7 + 4 * R3, 1 / (7 + 4 * R3)),
    optvals=[lambda: 64, lambda: 134, lambda: 194, lambda: 1 / 49])

add(44, 'L3',
    r"If $\sqrt[3]{a}+\sqrt[3]{b}+\sqrt[3]{c}=0$, then $(a+b+c)^{3}=$",
    [r"$abc$", r"$3abc$", r"$9abc$", r"$27abc$"], 3,
    chk=lambda: all(abs((a + b + c) ** 3 - 27 * a * b * c) < 1e-6
        for a, b, c in [(1.0, 8.0, -(cbrt(1) + cbrt(8)) ** 3),
                        (27.0, 1.0, -(3 + 1) ** 3),
                        (8.0, 64.0, -(2 + 4) ** 3)]))

add(45, 'L3',
    r"If $0<a<1$, then $\left[\dfrac{\sqrt{1+a}}{\sqrt{1+a}-\sqrt{1-a}}"
    r"+\dfrac{1-a}{\sqrt{1-a^{2}}-1+a}\right]-\left[\sqrt{\dfrac{1}{a^{2}}-1}-\dfrac1a\right]=$",
    [r"$\dfrac2a$", r"$2a$", r"$3a$", r"$\dfrac3a$"], 0,
    chk=lambda: all(abs((sqrt(1 + a) / (sqrt(1 + a) - sqrt(1 - a))
                         + (1 - a) / (sqrt(1 - a * a) - 1 + a))
                        - (sqrt(1 / a ** 2 - 1) - 1 / a) - 2 / a) < 1e-9
                    for a in (0.2, 0.5, 0.8)))

# ------------------------------------------------------------------ page 5
add(46, 'L2',
    r"If $x>2$, then $\sqrt{x+2\sqrt{x-1}}+\sqrt{x-2\sqrt{x-1}}=$",
    [r"$1$", r"$\sqrt{x-1}$", r"$2$", r"$2\sqrt{x-1}$"], 3,
    chk=lambda: all(abs(sqrt(x + 2 * sqrt(x - 1)) + sqrt(x - 2 * sqrt(x - 1))
                        - 2 * sqrt(x - 1)) < 1e-9 for x in (2.5, 5.0, 10.0)))

add(47, 'L2',
    r"If $1\le x\le 2$, then $\sqrt{x+2\sqrt{x-1}}+\sqrt{x-2\sqrt{x-1}}=$",
    [r"$1$", r"$\sqrt{x-1}$", r"$2$", r"$2\sqrt{x-1}$"], 2,
    chk=lambda: all(abs(sqrt(x + 2 * sqrt(x - 1)) + sqrt(x - 2 * sqrt(x - 1)) - 2) < 1e-9
                    for x in (1.0, 1.4, 2.0)))

add(48, 'L1',
    r"The positive square root of $11+\sqrt{112}$ is",
    [r"$\sqrt7+\sqrt2$", r"$\sqrt7-\sqrt2$", r"$\sqrt7+2$", r"$7+\sqrt2$"], 2,
    truth=lambda: sqrt(11 + sqrt(112)),
    optvals=[lambda: R7 + R2, lambda: R7 - R2, lambda: R7 + 2, lambda: 7 + R2])

add(49, 'L1',
    r"The square root of $49+20\sqrt6$ is",
    [r"$3+3\sqrt5$", r"$5+3\sqrt6$", r"$5+2\sqrt6$", r"$2+5\sqrt6$"], 2,
    truth=lambda: sqrt(49 + 20 * R6),
    optvals=[lambda: 3 + 3 * R5, lambda: 5 + 3 * R6, lambda: 5 + 2 * R6, lambda: 2 + 5 * R6])

add(50, 'L2',
    r"The square root of $134-\sqrt{6292}$ is",
    [r"$11+\sqrt{13}$", r"$11-\sqrt{13}$", r"$12-\sqrt{13}$", r"$12+\sqrt{13}$"], 1,
    truth=lambda: sqrt(134 - sqrt(6292)),
    optvals=[lambda: 11 + sqrt(13), lambda: 11 - sqrt(13),
             lambda: 12 - sqrt(13), lambda: 12 + sqrt(13)])

add(51, 'L2',
    r"The positive square root of $12\sqrt5+2\sqrt{55}$ is",
    [r"$\sqrt[4]{3}\left(\sqrt{13}+1\right)$", r"$\sqrt[4]{5}\left(\sqrt{11}+1\right)$",
     r"$\sqrt[4]{2}\left(\sqrt{14}+1\right)$", r"$\sqrt[4]{5}\left(\sqrt{12}+1\right)$"], 1,
    truth=lambda: sqrt(12 * R5 + 2 * sqrt(55)),
    optvals=[lambda: rt(3, 4) * (sqrt(13) + 1), lambda: rt(5, 4) * (sqrt(11) + 1),
             lambda: rt(2, 4) * (sqrt(14) + 1), lambda: rt(5, 4) * (sqrt(12) + 1)])

add(52, 'L2',
    r"The positive square root of $5\sqrt2+4\sqrt3$ is",
    [r"$\sqrt[4]{7}\left(\sqrt3+\sqrt2\right)$", r"$\sqrt[4]{7}\left(\sqrt5+\sqrt2\right)$",
     r"$\sqrt[4]{2}\left(\sqrt5+\sqrt2\right)$", r"$\sqrt[4]{2}\left(\sqrt3+\sqrt2\right)$"], 3,
    truth=lambda: sqrt(5 * R2 + 4 * R3),
    optvals=[lambda: rt(7, 4) * (R3 + R2), lambda: rt(7, 4) * (R5 + R2),
             lambda: rt(2, 4) * (R5 + R2), lambda: rt(2, 4) * (R3 + R2)])

add(53, 'L2',
    r"The positive square root of $\sqrt{32}-\sqrt{24}$ is",
    [r"$\sqrt[4]{2}\left(\sqrt3-1\right)$", r"$\sqrt[4]{2}\left(\sqrt2-1\right)$",
     r"$\sqrt[4]{2}\left(\sqrt3-\sqrt2\right)$", r"$\sqrt[4]{2}\left(\sqrt2-\sqrt3\right)$"], 0,
    truth=lambda: sqrt(sqrt(32) - sqrt(24)),
    optvals=[lambda: rt(2, 4) * (R3 - 1), lambda: rt(2, 4) * (R2 - 1),
             lambda: rt(2, 4) * (R3 - R2), lambda: rt(2, 4) * (R2 - R3)])

add(54, 'L2',
    r"The positive square root of $8\sqrt3-6\sqrt5$ is",
    [r"$\sqrt5-\sqrt3$", r"$\sqrt3\left(\sqrt5-\sqrt3\right)$",
     r"$\sqrt[3]{3}\left(\sqrt5-\sqrt3\right)$", r"$\sqrt[4]{3}\left(\sqrt5-\sqrt3\right)$"], 3,
    truth=lambda: sqrt(8 * R3 - 6 * R5),
    optvals=[lambda: R5 - R3, lambda: R3 * (R5 - R3),
             lambda: cbrt(3) * (R5 - R3), lambda: rt(3, 4) * (R5 - R3)])

add(55, 'L2',
    r"The positive square root of $11\sqrt7+28$ is",
    [r"$\sqrt[4]{7}\left(\sqrt5+2\right)$", r"$\sqrt[4]{7}\left(\sqrt7+2\right)$",
     r"$\sqrt[4]{7}\left(\sqrt3+2\right)$", r"$\sqrt[4]{7}\left(\sqrt6+2\right)$"], 1,
    truth=lambda: sqrt(11 * R7 + 28),
    optvals=[lambda: rt(7, 4) * (R5 + 2), lambda: rt(7, 4) * (R7 + 2),
             lambda: rt(7, 4) * (R3 + 2), lambda: rt(7, 4) * (R6 + 2)])

add(56, 'L2',
    r"The positive square root of $7\sqrt3-12$ is",
    [r"$2-\sqrt3$", r"$\sqrt3\left(2-\sqrt3\right)$",
     r"$\sqrt[4]{3}\left(2-\sqrt3\right)$", r"$\sqrt[4]{3}\left(3-\sqrt2\right)$"], 2,
    truth=lambda: sqrt(7 * R3 - 12),
    optvals=[lambda: 2 - R3, lambda: R3 * (2 - R3),
             lambda: rt(3, 4) * (2 - R3), lambda: rt(3, 4) * (3 - R2)])

add(57, 'L2',
    r"The positive square root of $14\sqrt5-30$ is",
    [r"$\sqrt[4]{2}\left(\sqrt3-2\right)$", r"$\sqrt[4]{5}\left(\sqrt3-5\right)$",
     r"$\sqrt[4]{5}\left(\sqrt3-\sqrt2\right)$", r"$\sqrt[4]{5}\left(3-\sqrt5\right)$"], 3,
    truth=lambda: sqrt(14 * R5 - 30),
    optvals=[lambda: rt(2, 4) * (R3 - 2), lambda: rt(5, 4) * (R3 - 5),
             lambda: rt(5, 4) * (R3 - R2), lambda: rt(5, 4) * (3 - R5)],
    note="source option (d) printed 3-sqrt2, which matches nothing; corrected to 3-sqrt5")

add(58, 'L3',
    r"$\sqrt{4+\sqrt5+\sqrt{17-4\sqrt{15}}}=$",
    [r"$\sqrt2+1$", r"$\sqrt3+1$", r"$\sqrt3-1$", r"$\sqrt2-1$"], 1,
    truth=lambda: sqrt(4 + R5 + sqrt(17 - 4 * sqrt(15))),
    optvals=[lambda: R2 + 1, lambda: R3 + 1, lambda: R3 - 1, lambda: R2 - 1])

# ------------------------------------------------------------------ page 6
add(59, 'L3',
    r"$\sqrt{3+\sqrt3-\sqrt{13+\sqrt{48}}}=$",
    [r"$\dfrac{\sqrt3+2}{\sqrt2}$", r"$\dfrac{\sqrt3-1}{\sqrt2}$",
     r"$\dfrac{\sqrt3+1}{\sqrt2}$", r"$\dfrac{\sqrt3-2\sqrt2}{\sqrt2}$"], 1,
    truth=lambda: sqrt(3 + R3 - sqrt(13 + sqrt(48))),
    optvals=[lambda: (R3 + 2) / R2, lambda: (R3 - 1) / R2,
             lambda: (R3 + 1) / R2, lambda: (R3 - 2 * R2) / R2])

add(60, 'L3',
    r"$\sqrt{\sqrt{27}-\sqrt8+\sqrt{17+12\sqrt2}-\sqrt{28-6\sqrt3}}=$",
    [r"$1$", r"$2$", r"$3$", r"$4$"], 1,
    truth=lambda: sqrt(sqrt(27) - sqrt(8) + sqrt(17 + 12 * R2) - sqrt(28 - 6 * R3)),
    optvals=[lambda: 1, lambda: 2, lambda: 3, lambda: 4])

add(61, 'L3',
    r"$\sqrt{39-4\sqrt{21}-4\sqrt{35}+8\sqrt{15}}=$",
    [r"$3\sqrt2-2\sqrt3+\sqrt5$", r"$2\sqrt5+2\sqrt3-\sqrt7$",
     r"$2\sqrt2-2\sqrt3-\sqrt5$", r"$2\sqrt7+2\sqrt3-\sqrt5$"], 1,
    truth=lambda: sqrt(39 - 4 * sqrt(21) - 4 * sqrt(35) + 8 * sqrt(15)),
    optvals=[lambda: 3 * R2 - 2 * R3 + R5, lambda: 2 * R5 + 2 * R3 - R7,
             lambda: 2 * R2 - 2 * R3 - R5, lambda: 2 * R7 + 2 * R3 - R5])

add(62, 'L3',
    r"$2\sqrt{3+\sqrt{5-\sqrt{13+\sqrt{48}}}}=$",
    [r"$\sqrt6+\sqrt2$", r"$\sqrt6-\sqrt2$", r"$\sqrt3+\sqrt2$", r"$\sqrt3-\sqrt2$"], 0,
    truth=lambda: 2 * sqrt(3 + sqrt(5 - sqrt(13 + sqrt(48)))),
    optvals=[lambda: R6 + R2, lambda: R6 - R2, lambda: R3 + R2, lambda: R3 - R2])

add(63, 'L3',
    r"$\sqrt{12+2\sqrt{15}+4\sqrt5+4\sqrt3}=$",
    [r"$2+\sqrt3+\sqrt2$", r"$5+\sqrt3+\sqrt2$", r"$2+\sqrt5+\sqrt3$", r"$2+\sqrt5+\sqrt2$"], 2,
    truth=lambda: sqrt(12 + 2 * sqrt(15) + 4 * R5 + 4 * R3),
    optvals=[lambda: 2 + R3 + R2, lambda: 5 + R3 + R2,
             lambda: 2 + R5 + R3, lambda: 2 + R5 + R2])

add(64, 'L3',
    r"$\sqrt{\dfrac{21}{2}-\sqrt{70}+\sqrt{10}-2\sqrt7}=$",
    [r"$\dfrac{\sqrt{12}+\sqrt5-\sqrt2}{\sqrt2}$", r"$\dfrac{\sqrt{14}-\sqrt5-\sqrt2}{\sqrt2}$",
     r"$\dfrac{\sqrt{14}-\sqrt5+\sqrt2}{\sqrt2}$", r"$\dfrac{\sqrt{12}-\sqrt5-\sqrt2}{\sqrt2}$"], 1,
    truth=lambda: sqrt(21 / 2 - sqrt(70) + sqrt(10) - 2 * R7),
    optvals=[lambda: (sqrt(12) + R5 - R2) / R2, lambda: (sqrt(14) - R5 - R2) / R2,
             lambda: (sqrt(14) - R5 + R2) / R2, lambda: (sqrt(12) - R5 - R2) / R2])

add(65, 'L3',
    r"$\sqrt{2(a+b)+2\sqrt{a^{2}+ab}-2\sqrt{ab}-2\sqrt{ab+b^{2}}}=$",
    [r"$\sqrt{a+b}+\sqrt a+\sqrt b$", r"$\sqrt{a-b}+\sqrt a+\sqrt b$",
     r"$\sqrt{a+b}+\sqrt a-\sqrt b$", r"$\sqrt{a-b}+\sqrt a-\sqrt b$"], 2,
    chk=lambda: all(abs(sqrt(2 * (a + b) + 2 * sqrt(a * a + a * b) - 2 * sqrt(a * b)
                             - 2 * sqrt(a * b + b * b))
                        - (sqrt(a + b) + sqrt(a) - sqrt(b))) < 1e-9
                    for a, b in [(1.0, 1.0), (4.0, 1.0), (2.0, 3.0), (9.0, 5.0)]))

add(66, 'L1',
    r"$\sqrt[3]{38+17\sqrt5}=$",
    [r"$1+\sqrt5$", r"$2+\sqrt5$", r"$1+2\sqrt5$", r"$3+\sqrt5$"], 1,
    truth=lambda: cbrt(38 + 17 * R5),
    optvals=[lambda: 1 + R5, lambda: 2 + R5, lambda: 1 + 2 * R5, lambda: 3 + R5])

add(67, 'L1',
    r"$\sqrt[3]{72+32\sqrt5}=$",
    [r"$3+\sqrt5$", r"$2+\sqrt5$", r"$3+2\sqrt5$", r"$2+3\sqrt5$"], 0,
    truth=lambda: cbrt(72 + 32 * R5),
    optvals=[lambda: 3 + R5, lambda: 2 + R5, lambda: 3 + 2 * R5, lambda: 2 + 3 * R5])

add(68, 'L1',
    r"$\sqrt[3]{20-14\sqrt2}=$",
    [r"$2+2\sqrt2$", r"$1-2\sqrt2$", r"$2-\sqrt2$", r"$3-\sqrt2$"], 2,
    truth=lambda: cbrt(20 - 14 * R2),
    optvals=[lambda: 2 + 2 * R2, lambda: 1 - 2 * R2, lambda: 2 - R2, lambda: 3 - R2])

add(69, 'L1',
    r"$\sqrt[3]{22-10\sqrt7}=$",
    [r"$1-3\sqrt2$", r"$1-2\sqrt2$", r"$1-\sqrt2$", r"$1-\sqrt7$"], 3,
    truth=lambda: cbrt(22 - 10 * R7),
    optvals=[lambda: 1 - 3 * R2, lambda: 1 - 2 * R2, lambda: 1 - R2, lambda: 1 - R7])

add(70, 'L1',
    r"$\sqrt[3]{-38+17\sqrt5}=$",
    [r"$-3+\sqrt5$", r"$-2+\sqrt3$", r"$-1$", r"$-2+\sqrt5$"], 3,
    truth=lambda: cbrt(-38 + 17 * R5),
    optvals=[lambda: -3 + R5, lambda: -2 + R3, lambda: -1, lambda: -2 + R5])

# ------------------------------------------------------------------ page 7
add(71, 'L3',
    r"The cube root of $9ab^{2}+\left(b^{2}+24a^{2}\right)\sqrt{b^{2}-3a^{2}}$ is",
    [r"$3a+\sqrt{b^{2}-3a^{2}}$", r"$3a-\sqrt{b^{2}-3a^{2}}$",
     r"$2a+\sqrt{b^{2}-3a^{2}}$", r"$2a-\sqrt{b^{2}-3a^{2}}$"], 0,
    chk=lambda: all(abs(cbrt(9 * a * b * b + (b * b + 24 * a * a) * sqrt(b * b - 3 * a * a))
                        - (3 * a + sqrt(b * b - 3 * a * a))) < 1e-9
                    for a, b in [(1.0, 2.0), (1.0, 5.0), (2.0, 7.0)]))

add(72, 'L2',
    r"$\sqrt[4]{124+32\sqrt{15}}=$",
    [r"$\sqrt5+\sqrt3$", r"$\sqrt5+\sqrt2$", r"$\sqrt3+\sqrt2$", r"$\sqrt5+2$"], 0,
    truth=lambda: rt(124 + 32 * sqrt(15), 4),
    optvals=[lambda: R5 + R3, lambda: R5 + R2, lambda: R3 + R2, lambda: R5 + 2],
    note="source printed 32*sqrt5 (OCR loss of the 1); reconstructed as 32*sqrt15")

add(73, 'L2',
    r"$\sqrt[4]{49-20\sqrt6}=$",
    [r"$\sqrt3-\sqrt2$", r"$\sqrt7-\sqrt3$", r"$\sqrt7-\sqrt2$", r"$\sqrt5-\sqrt2$"], 0,
    truth=lambda: rt(49 - 20 * R6, 4),
    optvals=[lambda: R3 - R2, lambda: R7 - R3, lambda: R7 - R2, lambda: R5 - R2])

add(74, 'L2',
    r"$\sqrt[4]{137-36\sqrt{14}}=$",
    [r"$5-\sqrt3$", r"$6-\sqrt3$", r"$\sqrt7-\sqrt2$", r"$\sqrt2-\sqrt3$"], 2,
    truth=lambda: rt(137 - 36 * sqrt(14), 4),
    optvals=[lambda: 5 - R3, lambda: 6 - R3, lambda: R7 - R2, lambda: R2 - R3])

add(75, 'L2',
    r"$\sqrt[4]{\dfrac{7+4\sqrt3}{4}}=$",
    [r"$\sqrt3+1$", r"$\sqrt3-1$", r"$\dfrac{\sqrt3+1}{2}$", r"$\dfrac{\sqrt3+1}{\sqrt2}$"], 2,
    truth=lambda: rt((7 + 4 * R3) / 4, 4),
    optvals=[lambda: R3 + 1, lambda: R3 - 1, lambda: (R3 + 1) / 2, lambda: (R3 + 1) / R2])

add(76, 'L1',
    r"$\sqrt{14+6\sqrt5}+\sqrt{14-6\sqrt5}=$",
    [r"$3$", r"$6$", r"$\sqrt5$", r"$2\sqrt5$"], 1,
    truth=lambda: sqrt(14 + 6 * R5) + sqrt(14 - 6 * R5),
    optvals=[lambda: 3, lambda: 6, lambda: R5, lambda: 2 * R5])

add(77, 'L1',
    r"$\sqrt{28+10\sqrt3}-\sqrt{7+4\sqrt3}=$",
    [r"$1$", r"$2$", r"$3$", r"$4$"], 2,
    truth=lambda: sqrt(28 + 10 * R3) - sqrt(7 + 4 * R3),
    optvals=[lambda: 1, lambda: 2, lambda: 3, lambda: 4])

add(78, 'L2',
    r"$\sqrt{7-3\sqrt5}+\sqrt{3+\sqrt5}=$",
    [r"$3\sqrt3$", r"$2\sqrt2$", r"$2\sqrt5$", r"$3\sqrt5$"], 1,
    truth=lambda: sqrt(7 - 3 * R5) + sqrt(3 + R5),
    optvals=[lambda: 3 * R3, lambda: 2 * R2, lambda: 2 * R5, lambda: 3 * R5])

add(79, 'L2',
    r"$\left(\sqrt{12+2\sqrt6}+\sqrt{12-2\sqrt6}\right)^{2}=$",
    [r"$24+4\sqrt{30}$", r"$24-4\sqrt{30}$", r"$4\sqrt{30}$", r"$24$"], 0,
    truth=lambda: (sqrt(12 + 2 * R6) + sqrt(12 - 2 * R6)) ** 2,
    optvals=[lambda: 24 + 4 * sqrt(30), lambda: 24 - 4 * sqrt(30),
             lambda: 4 * sqrt(30), lambda: 24])

add(80, 'L1',
    r"$\dfrac{\sqrt2}{\sqrt{2+\sqrt3}-\sqrt{2-\sqrt3}}=$",
    [r"$1$", r"$2$", r"$3$", r"$4$"], 0,
    truth=lambda: R2 / (sqrt(2 + R3) - sqrt(2 - R3)),
    optvals=[lambda: 1, lambda: 2, lambda: 3, lambda: 4])

add(81, 'L2',
    r"$\dfrac{\sqrt7}{\sqrt{16+6\sqrt7}-\sqrt{16-6\sqrt7}}$ is",
    [r"a rational number", r"an irrational number", r"a complex number", r"none of these"], 0,
    chk=lambda: abs(R7 / (sqrt(16 + 6 * R7) - sqrt(16 - 6 * R7)) - 0.5) < 1e-12)

# ------------------------------------------------------------------ page 8
add(83, 'L3',
    r"$\dfrac{\sqrt{5/2}+\sqrt{7-3\sqrt5}}{\sqrt{7/2}+\sqrt{16-5\sqrt7}}$ is",
    [r"a rational number", r"an irrational number", r"a complex number", r"none of these"], 0,
    chk=lambda: abs((sqrt(2.5) + sqrt(7 - 3 * R5)) / (sqrt(3.5) + sqrt(16 - 5 * R7)) - 0.6) < 1e-12)

add(84, 'L2',
    r"$\dfrac{\sqrt{8+\sqrt{28}}+\sqrt{8-\sqrt{28}}}{\sqrt{8+\sqrt{28}}-\sqrt{8-\sqrt{28}}}=$",
    [r"$2$", r"$7$", r"$\sqrt7$", r"$\sqrt2$"], 2,
    truth=lambda: (sqrt(8 + sqrt(28)) + sqrt(8 - sqrt(28))) / (sqrt(8 + sqrt(28)) - sqrt(8 - sqrt(28))),
    optvals=[lambda: 2, lambda: 7, lambda: R7, lambda: R2])

add(85, 'L3',
    r"$\dfrac{\sqrt{15-5\sqrt5}}{\sqrt2+\sqrt{7-3\sqrt5}}=$",
    [r"$1$", r"$5$", r"$\sqrt5$", r"$\sqrt2$"], 0,
    truth=lambda: sqrt(15 - 5 * R5) / (R2 + sqrt(7 - 3 * R5)),
    optvals=[lambda: 1, lambda: 5, lambda: R5, lambda: R2])

add(86, 'L1',
    r"$\dfrac{\left(\sqrt{45}-\sqrt{20}\right)\left(\sqrt{12}+\sqrt{75}\right)}{\sqrt5+\sqrt{180}}=$",
    [r"$1$", r"$-1$", r"$\sqrt3$", r"$-\sqrt3$"], 2,
    truth=lambda: (sqrt(45) - sqrt(20)) * (sqrt(12) + sqrt(75)) / (R5 + sqrt(180)),
    optvals=[lambda: 1, lambda: -1, lambda: R3, lambda: -R3])

add(87, 'L2',
    r"If $x=\dfrac{1}{12}$, then $\sqrt{\dfrac34-x}+\sqrt{2x}-\dfrac32\sqrt{1-4x}=$",
    [r"$0$", r"$1$", r"$-1$", r"none of these"], 0,
    chk=lambda: abs(sqrt(0.75 - 1 / 12) + sqrt(2 / 12) - 1.5 * sqrt(1 - 4 / 12)) < 1e-12)

add(89, 'L2',
    r"A rationalising factor of $a^{1/3}+a^{-1/3}$ is",
    [r"$a^{1/3}-a^{-1/3}$", r"$a^{1/3}+a^{-1/3}$",
     r"$a^{2/3}-a^{-2/3}$", r"$a^{2/3}+a^{-2/3}-1$"], 3,
    chk=lambda: all(abs((a ** (1 / 3) + a ** (-1 / 3)) * (a ** (2 / 3) + a ** (-2 / 3) - 1)
                        - (a + 1 / a)) < 1e-9 for a in (2.0, 5.0, 11.0)))

add(90, 'L2',
    r"A rationalising factor of $\sqrt[3]{16}+\sqrt[3]{4}+1$ is",
    [r"$4^{1/3}+1$", r"$4^{1/3}-1$", r"$2^{1/3}+1$", r"$2^{1/3}-1$"], 1,
    chk=lambda: abs((cbrt(16) + cbrt(4) + 1) * (cbrt(4) - 1) - 3.0) < 1e-9)

add(91, 'L3',
    r"A rationalising factor of $2+\sqrt[4]{12}+\sqrt3$ is",
    [r"$\left(2-\sqrt[4]{12}+\sqrt3\right)\left(7-2\sqrt3\right)$",
     r"$\left(2-\sqrt[4]{12}+\sqrt3\right)\left(7+2\sqrt3\right)$",
     r"$\left(2+\sqrt[4]{12}-\sqrt3\right)\left(7+2\sqrt3\right)$",
     r"$\left(2-\sqrt[4]{12}+\sqrt3\right)\left(7+4\sqrt3\right)$"], 0,
    chk=lambda: abs((2 + rt(12, 4) + R3) * (2 - rt(12, 4) + R3) * (7 - 2 * R3) - 37.0) < 1e-9)

# ------------------------------------------------------------------ page 9
add(93, 'L2',
    r"$\dfrac{3\sqrt2}{\sqrt6+\sqrt3}-\dfrac{4\sqrt3}{\sqrt6+\sqrt2}+\dfrac{\sqrt6}{\sqrt3+\sqrt2}=$",
    [r"$0$", r"$1$", r"$2$", r"$4$"], 0,
    truth=lambda: 3 * R2 / (R6 + R3) - 4 * R3 / (R6 + R2) + R6 / (R3 + R2),
    optvals=[lambda: 0, lambda: 1, lambda: 2, lambda: 4])

add(94, 'L2',
    r"$\dfrac{1}{1+\sqrt3}+\dfrac{1}{\sqrt3+\sqrt5}+\dfrac{1}{\sqrt5+\sqrt7}+\cdots$ to $40$ terms $=$",
    [r"$0$", r"$1$", r"$4$", r"$\dfrac{\sqrt{41}-1}{2}$"], 2,
    truth=lambda: sum(1 / (sqrt(2 * k - 1) + sqrt(2 * k + 1)) for k in range(1, 41)),
    optvals=[lambda: 0, lambda: 1, lambda: 4, lambda: (sqrt(41) - 1) / 2])

add(95, 'L3',
    r"If $f(x)=\dfrac{1}{\sqrt{x+2\sqrt{2x-4}}}+\dfrac{1}{\sqrt{x-2\sqrt{2x-4}}}$ for $x>2$, "
    r"then $f(11)=$",
    [r"$\dfrac76$", r"$\dfrac56$", r"$\dfrac67$", r"$\dfrac57$"], 2,
    truth=lambda: 1 / sqrt(11 + 2 * sqrt(18)) + 1 / sqrt(11 - 2 * sqrt(18)),
    optvals=[lambda: 7 / 6, lambda: 5 / 6, lambda: 6 / 7, lambda: 5 / 7])

add(98, 'L2',
    r"$\dfrac{2\left(\sqrt3-1\right)^{2}}{3\left(\sqrt3-1\right)^{2}-2}=$",
    [r"$-\left(\sqrt2+1\right)$", r"$\sqrt2+1$", r"$\sqrt3+1$", r"$-\left(\sqrt3+1\right)$"], 3,
    truth=lambda: 2 * (R3 - 1) ** 2 / (3 * (R3 - 1) ** 2 - 2),
    optvals=[lambda: -(R2 + 1), lambda: R2 + 1, lambda: R3 + 1, lambda: -(R3 + 1)])

# ------------------------------------------------------------------ page 10
add(100, 'L3',
    r"$\sqrt{6+2\sqrt3+2\sqrt2+2\sqrt6}-\dfrac{1}{\sqrt{5+2\sqrt6}}=$",
    [r"$1$", r"$-1$", r"$0$", r"none of these"], 3,
    chk=lambda: abs(sqrt(6 + 2 * R3 + 2 * R2 + 2 * R6) - 1 / sqrt(5 + 2 * R6)
                    - (1 + 2 * R2)) < 1e-12)

# ------------------------------------------------------------- deliberately dropped
DROPPED = {
    20: "RF of 2^(2/3)+2^(-2/3)-1: none of the four printed options rationalises it",
    82: "numerator of the fraction is missing from the source crop",
    88: "exact duplicate of Q18",
    92: "option crops overlap; two different option sets printed on top of each other",
    96: "options truncated mid-expression in the source",
    97: "value is 4*sqrt6; no printed option matches",
    99: "second term illegible; both plausible readings give different keys",
    101: "exact duplicate of Q13",
}

# ---------------------------------------------------------------- L4 additions
# The three PYQ books supplied contain no Surds chapter (verified against the
# Arihant contents, the MTG Class-XI contents and a full-text sweep), so the
# Level-4 paper is built from the hardest remaining source items plus these
# seven JEE-pattern questions written to the same standard.

add(201, 'L4',
    r"If $x=\dfrac{\sqrt5+1}{\sqrt5-1}$ and $y=\dfrac{\sqrt5-1}{\sqrt5+1}$, then $x^{2}+xy+y^{2}=$",
    [r"$6$", r"$7$", r"$8$", r"$9$"], 2,
    truth=lambda: (lambda x, y: x * x + x * y + y * y)((R5 + 1) / (R5 - 1), (R5 - 1) / (R5 + 1)),
    optvals=[lambda: 6, lambda: 7, lambda: 8, lambda: 9])

add(202, 'L4',
    r"$\dfrac{1}{1+\sqrt2}+\dfrac{1}{\sqrt2+\sqrt3}+\dfrac{1}{\sqrt3+\sqrt4}"
    r"+\cdots+\dfrac{1}{\sqrt{99}+\sqrt{100}}=$",
    [r"$8$", r"$9$", r"$10$", r"$11$"], 1,
    truth=lambda: sum(1 / (sqrt(k) + sqrt(k + 1)) for k in range(1, 100)),
    optvals=[lambda: 8, lambda: 9, lambda: 10, lambda: 11])

add(203, 'L4',
    r"If $a=\sqrt[3]{2}+\sqrt[3]{4}$, then $a^{3}-6a=$",
    [r"$2$", r"$4$", r"$6$", r"$8$"], 2,
    truth=lambda: (lambda a: a ** 3 - 6 * a)(cbrt(2) + cbrt(4)),
    optvals=[lambda: 2, lambda: 4, lambda: 6, lambda: 8])

add(204, 'L4',
    r"The set of all real $x$ satisfying "
    r"$\sqrt{x+3-4\sqrt{x-1}}+\sqrt{x+8-6\sqrt{x-1}}=1$ is",
    [r"$\{5\}$", r"$\{10\}$", r"$[5,10]$", r"$\varnothing$"], 2,
    chk=lambda: all(abs(sqrt(x + 3 - 4 * sqrt(x - 1)) + sqrt(x + 8 - 6 * sqrt(x - 1)) - 1) < 1e-9
                    for x in (5.0, 6.3, 8.0, 10.0))
           and all(abs(sqrt(x + 3 - 4 * sqrt(x - 1)) + sqrt(x + 8 - 6 * sqrt(x - 1)) - 1) > 1e-6
                    for x in (4.0, 11.0, 2.0)))

add(205, 'L4',
    r"$\left(7+4\sqrt3\right)^{1/2}-\left(7-4\sqrt3\right)^{1/2}=$",
    [r"$2$", r"$2\sqrt3$", r"$4$", r"$4\sqrt3$"], 1,
    truth=lambda: sqrt(7 + 4 * R3) - sqrt(7 - 4 * R3),
    optvals=[lambda: 2, lambda: 2 * R3, lambda: 4, lambda: 4 * R3])

add(206, 'L4',
    r"If $x=\dfrac{1}{2-\sqrt3}$, then $x^{3}-2x^{2}-7x+5=$",
    [r"$1$", r"$2$", r"$3$", r"$5$"], 2,
    truth=lambda: (lambda x: x ** 3 - 2 * x ** 2 - 7 * x + 5)(1 / (2 - R3)),
    optvals=[lambda: 1, lambda: 2, lambda: 3, lambda: 5])

add(207, 'L4',
    r"$\sqrt[3]{2+\sqrt5}+\sqrt[3]{2-\sqrt5}=$",
    [r"$-1$", r"$0$", r"$1$", r"$2$"], 2,
    truth=lambda: cbrt(2 + R5) + cbrt(2 - R5),
    optvals=[lambda: -1, lambda: 0, lambda: 1, lambda: 2])

# ---------------------------------------------------------------- final split
LEVELS = {
    'L1': [1, 2, 3, 4, 16, 17, 18, 19, 27, 31, 32, 33, 39, 42, 48, 49,
           66, 67, 68, 69, 70, 76, 77, 80, 86],
    'L2': [5, 7, 9, 15, 21, 34, 35, 36, 40, 41, 43, 50, 51, 52, 53, 54,
           55, 56, 57, 72, 73, 74, 75, 79, 84],
    'L3': [6, 8, 10, 11, 12, 14, 22, 26, 28, 29, 30, 37, 38, 44, 45, 58,
           59, 60, 61, 62, 63, 64, 65, 71, 91],
    'L4': [13, 23, 24, 25, 46, 47, 78, 81, 83, 85, 87, 89, 90, 93, 94, 95,
           98, 100, 201, 202, 203, 204, 205, 206, 207],
}
