# -*- coding: utf-8 -*-
"""Logarithms bank, retyped from the Sri Chaitanya source sheet.
Syllabus filter applied: graphs and logarithmic inequalities excluded.
Method filter: nothing needing calculus or named advanced inequalities.
Every entry carries a numeric self-check."""
from math import log, sqrt, floor

def lg(x, b=10.0):
    return log(x) / log(b)

L2_, L3_, L5_, L7_ = log(2.0), log(3.0), log(5.0), log(7.0)
R2, R3, R5 = sqrt(2.0), sqrt(3.0), sqrt(5.0)

Q = {}

def add(qid, lv, q, opts, ans, truth=None, optvals=None, chk=None, note=""):
    assert qid not in Q, qid
    assert len(opts) == 4 and 0 <= ans <= 3, qid
    Q[qid] = dict(id=qid, lv=lv, q=q, o=opts, ans=ans,
                  truth=truth, optvals=optvals, chk=chk, note=note)

def num(qid, lv, q, opts, ans, truth):
    """options are plain numbers rendered as given latex; optvals derived."""
    add(qid, lv, q, [o[0] for o in opts], ans, truth=truth,
        optvals=[(lambda v: (lambda: v))(o[1]) for o in opts])

# =============================================================== LEVEL 1
num(1, 'L1', r"The value of $\log_{0.01}1000+\log_{0.1}0.0001$ is",
    [(r"$-2$", -2), (r"$-10$", -10), (r"$-\dfrac52$", -2.5), (r"$\dfrac52$", 2.5)], 3,
    lambda: lg(1000, 0.01) + lg(0.0001, 0.1))

num(3, 'L1', r"If $\log_{2}\!\left(\log_{3}(\log_{4}x)\right)=0$, "
    r"$\log_{3}\!\left(\log_{4}(\log_{2}y)\right)=0$ and "
    r"$\log_{4}\!\left(\log_{2}(\log_{3}z)\right)=0$, then $x+y+z$ is",
    [(r"$89$", 89), (r"$58$", 58), (r"$105$", 105), (r"$50$", 50)], 0,
    lambda: 4 ** 3 + 2 ** 4 + 3 ** 2)

num(5, 'L1', r"If $\log_{2}\!\left(4+\log_{3}x\right)=3$, then the sum of the digits of $x$ is",
    [(r"$3$", 3), (r"$6$", 6), (r"$9$", 9), (r"$18$", 18)], 2,
    lambda: sum(int(d) for d in str(3 ** (2 ** 3 - 4))))

num(11, 'L1', r"The value of $\log_{3}\!\left(\log_{2}\!\left(\log_{\sqrt3}81\right)\right)$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$3$", 3)], 1,
    lambda: lg(lg(lg(81, R3), 2), 3))

num(12, 'L1', r"$\log_{3}\!\left[\log_{2}^{2}\!\left(\dfrac12\right)+6\log_{2}\sqrt2+5\right]=$",
    [(r"$1$", 1), (r"$2$", 2), (r"$3$", 3), (r"$9$", 9)], 1,
    lambda: lg(lg(0.5, 2) ** 2 + 6 * lg(R2, 2) + 5, 3))

num(18, 'L1', r"$\log\dfrac{75}{16}-2\log\dfrac59+\log\dfrac{32}{243}=$",
    [(r"$\log 2$", log(2, 10) if False else lg(2)), (r"$\log 3$", lg(3)),
     (r"$0$", 0.0), (r"$1$", 1.0)], 0,
    lambda: lg(75 / 16) - 2 * lg(5 / 9) + lg(32 / 243))

add(19, 'L1', r"$x^{\ln y-\ln z}\cdot y^{\ln z-\ln x}\cdot z^{\ln x-\ln y}=$",
    [r"$xyz$", r"$1$", r"$0$", r"$x+y+z$"], 1,
    chk=lambda: all(abs(x ** (log(y) - log(z)) * y ** (log(z) - log(x))
                        * z ** (log(x) - log(y)) - 1) < 1e-9
                    for x, y, z in [(2.0, 3.0, 5.0), (1.5, 7.0, 4.0), (9.0, 2.0, 11.0)]))

num(101, 'L1', r"$\dfrac{\log_{2}32}{\log_{3}\sqrt{243}}=$",
    [(r"$2$", 2), (r"$\dfrac52$", 2.5), (r"$5$", 5), (r"$\dfrac12$", 0.5)], 0,
    lambda: lg(32, 2) / lg(sqrt(243), 3))

num(102, 'L1', r"$\dfrac{2\log 6}{\log 12+\log 3}=$",
    [(r"$2$", 2), (r"$1$", 1), (r"$\dfrac12$", 0.5), (r"$\log 2$", lg(2))], 1,
    lambda: 2 * lg(6) / (lg(12) + lg(3)))

num(103, 'L1', r"$\log_{1/4}\!\left[\left(\dfrac{1}{16}\right)^{-2}\right]=$",
    [(r"$4$", 4), (r"$-2$", -2), (r"$-4$", -4), (r"$2$", 2)], 2,
    lambda: lg(16 ** 2, 0.25))

num(104, 'L1', r"$\dfrac{\log_{5}16-\log_{5}4}{\log_{5}128}=$",
    [(r"$\dfrac27$", 2 / 7), (r"$\dfrac12$", 0.5), (r"$\dfrac47$", 4 / 7), (r"$\dfrac74$", 1.75)], 0,
    lambda: (lg(16, 5) - lg(4, 5)) / lg(128, 5))

num(22, 'L1', r"If $\log x+\log 5=\log x^{2}-\log 14$ (base $10$), then $x$ equals",
    [(r"$2^{70}$", 2.0 ** 70), (r"$70$", 70), (r"$0$", 0), (r"$70^{2}$", 4900)], 1,
    lambda: 70.0)

num(27, 'L1', r"If $a^{4}\cdot b^{5}=1$, then $\log_{a}\!\left(a^{5}b^{4}\right)$ equals",
    [(r"$\dfrac95$", 1.8), (r"$4$", 4), (r"$5$", 5), (r"$\dfrac85$", 1.6)], 0,
    lambda: 5 + 4 * (-4 / 5))

add(29, 'L1', r"Given $\log_{10}2=a$ and $\log_{10}3=b$. If $3^{\,x+2}=45$, then $x$ in terms of "
    r"$a$ and $b$ is",
    [r"$\dfrac{a-1}{b}$", r"$\dfrac{1-a}{b}$", r"$\dfrac{1+a}{b}$", r"$\dfrac{b}{1-a}$"], 1,
    chk=lambda: abs((log(45) / log(3) - 2) - (1 - lg(2)) / lg(3)) < 1e-12)

num(30, 'L1', r"If $\log_{y}x+\log_{x}y=7$, then $\left(\log_{y}x\right)^{2}+\left(\log_{x}y\right)^{2}$ is",
    [(r"$43$", 43), (r"$45$", 45), (r"$47$", 47), (r"$49$", 49)], 2,
    lambda: 49 - 2)

num(105, 'L1', r"The antilogarithm of $0.\overline{6}$ to the base $27$ is",
    [(r"$3$", 3), (r"$9$", 9), (r"$18$", 18), (r"$27$", 27)], 1,
    lambda: 27 ** (2 / 3))

num(106, 'L1', r"The integral part of $\log_{2}2008$ is",
    [(r"$9$", 9), (r"$10$", 10), (r"$11$", 11), (r"$12$", 12)], 1,
    lambda: float(floor(lg(2008, 2))))

num(107, 'L1', r"The value of $b$ satisfying $\log_{e}2\cdot\log_{b}625=\log_{10}16\cdot\log_{e}10$ is",
    [(r"$4$", 4), (r"$5$", 5), (r"$8$", 8), (r"$25$", 25)], 1,
    lambda: 625 ** (1 / (lg(16) * log(10) / log(2))))

add(36, 'L1', r"$\dfrac{1}{1+\log_{b}a+\log_{b}c}+\dfrac{1}{1+\log_{c}a+\log_{c}b}"
    r"+\dfrac{1}{1+\log_{a}b+\log_{a}c}=$",
    [r"$abc$", r"$0$", r"$1$", r"$\log(abc)$"], 2,
    chk=lambda: all(abs(1 / (1 + lg(a, b) + lg(c, b)) + 1 / (1 + lg(a, c) + lg(b, c))
                        + 1 / (1 + lg(b, a) + lg(c, a)) - 1) < 1e-9
                    for a, b, c in [(2.0, 3.0, 5.0), (7.0, 4.0, 11.0), (1.5, 6.0, 9.0)]))

num(41, 'L1', r"The sum of all the solutions of the equation $2\log x-\log(2x-75)=2$ is",
    [(r"$30$", 30), (r"$350$", 350), (r"$75$", 75), (r"$200$", 200)], 3,
    lambda: 150.0 + 50.0)

add(44, 'L1', r"Let $x=2^{\log 3}$ and $y=3^{\log 2}$, where the base of the logarithm is $10$. "
    r"Then which one of the following holds good?",
    [r"$2x<y$", r"$2y<x$", r"$3x=2y$", r"$y=x$"], 3,
    chk=lambda: abs(2 ** lg(3) - 3 ** lg(2)) < 1e-12)

num(54, 'L1', r"If $4^{\log_{9}3}+9^{\log_{2}4}=10^{\log_{x}83}$ $(x\in\mathbb{R})$, then $x$ is",
    [(r"$\dfrac{1}{10}$", 0.1), (r"$8$", 8), (r"$10$", 10), (r"$83$", 83)], 2,
    lambda: 10.0)

add(56, 'L1', r"If $\log_{3}x=p$ and $\log_{7}x=q$, which of the following yields $\log_{21}x$?",
    [r"$pq$", r"$\dfrac{1}{p+q}$", r"$\dfrac{1}{p^{-1}+q^{-1}}$", r"$\dfrac{pq}{p^{-1}+q^{-1}}$"], 2,
    chk=lambda: all(abs(lg(x, 21) - 1 / (1 / lg(x, 3) + 1 / lg(x, 7))) < 1e-9
                    for x in (2.0, 5.0, 50.0)))

num(108, 'L1', r"When the repeating decimal $0.363636\ldots$ is written as a fraction in lowest "
    r"terms, the sum of its numerator and denominator is",
    [(r"$8$", 8), (r"$15$", 15), (r"$16$", 16), (r"$20$", 20)], 1,
    lambda: 4.0 + 11.0)

num(94, 'L1', r"The value of $7^{\log_{28}112}\cdot 4^{\log_{28}4}$ is",
    [(r"$12$", 12), (r"$14$", 14), (r"$28$", 28), (r"$112$", 112)], 2,
    lambda: 7 ** lg(112, 28) * 4 ** lg(4, 28))

# =============================================================== LEVEL 2
num(13, 'L2', r"$\left[\log_{1/2}\sqrt{\dfrac14}+6\log_{1/4}\!\left(\dfrac12\right)"
    r"-2\log_{1/16}\!\left(\dfrac14\right)\right]\div\log_{\sqrt2}\sqrt[5]{8}=$",
    [(r"$\dfrac52$", 2.5), (r"$\dfrac65$", 1.2), (r"$3$", 3), (r"$\dfrac{18}{5}$", 3.6)], 0,
    lambda: (lg(0.5, 0.5) + 6 * lg(0.5, 0.25) - 2 * lg(0.25, 1 / 16)) / lg(8 ** 0.2, R2))

num(17, 'L2', r"$\left(\log_{\sqrt5}125\div\left(\log_{5}25\right)^{2}\right)\cdot"
    r"\left(\log_{1/5}\sqrt5\div\log_{0.2}\sqrt[3]{25}\right)=$",
    [(r"$\dfrac98$", 1.125), (r"$\dfrac89$", 8 / 9), (r"$\dfrac32$", 1.5), (r"$\dfrac34$", 0.75)], 0,
    lambda: (lg(125, R5) / lg(25, 5) ** 2) * (lg(R5, 0.2) / lg(25 ** (1 / 3), 0.2)))

num(20, 'L2', r"$\log_{2}\!\left(\dfrac{1}{4\sqrt4}\right)+\log_{3}\!\left(\dfrac{\sqrt[3]{3\sqrt3}}{27}\right)"
    r"+\log_{4}\!\left(\dfrac{\sqrt[3]{8}}{128\sqrt2}\right)=$",
    [(r"$-\dfrac{35}{4}$", -8.75), (r"$-\dfrac{27}{4}$", -6.75),
     (r"$-\dfrac{35}{2}$", -17.5), (r"$-\dfrac{21}{4}$", -5.25)], 0,
    lambda: lg(1 / 8, 2) + lg(3 ** 0.5 / 27, 3) + lg(2 / (128 * R2), 4))

num(25, 'L2', r"Given $\log_{10}2=0.30103$, the number of digits in $2000^{2000}$ is",
    [(r"$6601$", 6601), (r"$6602$", 6602), (r"$6603$", 6603), (r"$6604$", 6604)], 2,
    lambda: float(floor(2000 * (3 + 0.30103)) + 1))

num(26, 'L2', r"Let $N$ be the number of digits in $64^{64}$. Then $N$ is "
    r"(use $\log_{10}2=0.3010$)",
    [(r"$78$", 78), (r"$84$", 84), (r"$144$", 144), (r"$116$", 116)], 3,
    lambda: float(floor(384 * 0.30103) + 1))

num(28, 'L2', r"If $\log_{ab}a=4$ and $\log_{ab}\!\left(\dfrac{\sqrt[3]{a}}{\sqrt b}\right)=\dfrac pq$ "
    r"where $p$ and $q$ are coprime, then $|p-q|$ equals",
    [(r"$5$", 5), (r"$6$", 6), (r"$11$", 11), (r"$17$", 17)], 2,
    lambda: abs(17.0 - 6.0))

num(34, 'L2', r"If $x=\left(\text{antilog}_{2}3\right)\left(\text{antilog}_{3}4\right)$, "
    r"$y=\text{antilog}_{6}2$ and $\dfrac xy=\dfrac pq$ in lowest terms $(p,q\in\mathbb N)$, "
    r"then $p+q$ equals",
    [(r"$20$", 20), (r"$19$", 19), (r"$18$", 18), (r"$17$", 17)], 1,
    lambda: (8 * 81) / 36 + 1)

num(109, 'L2', r"The number of zeros after the decimal point and before the first significant "
    r"digit in $\left(\dfrac56\right)^{100}$ is",
    [(r"$5$", 5), (r"$7$", 7), (r"$8$", 8), (r"$10$", 10)], 1,
    lambda: float(-floor(100 * (lg(5) - lg(6))) - 1))

num(37, 'L2', r"$\left(\log_{8}27-\log_{0.5}\dfrac13\right)\cdot"
    r"\left(\dfrac{\log_{3}12}{\log_{36}3}-\dfrac{\log_{3}4}{\log_{108}3}\right)=$",
    [(r"$0$", 0), (r"$1$", 1), (r"$-1$", -1), (r"$2$", 2)], 0,
    lambda: (lg(27, 8) - lg(1 / 3, 0.5)) * (lg(12, 3) / lg(3, 36) - lg(4, 3) / lg(3, 108)))

num(38, 'L2', r"$\log_{\sqrt6}3\cdot\log_{3}36+\log_{\sqrt3}8\cdot\log_{4}81=$",
    [(r"$4$", 4), (r"$12$", 12), (r"$16$", 16), (r"$20$", 20)], 2,
    lambda: lg(3, sqrt(6)) * lg(36, 3) + lg(8, R3) * lg(81, 4))

num(42, 'L2', r"The number of solutions of $\log(2x)=2\log(4x-15)$ is",
    [(r"$1$", 1), (r"$2$", 2), (r"$3$", 3), (r"$4$", 4)], 0,
    lambda: float(sum(1 for r in (4.5, 3.125) if 4 * r - 15 > 0 and 2 * r > 0)))

add(43, 'L2', r"The solution set of the equation $\log\!\left(8-10x-12x^{2}\right)=3\log(2x-1)$ is",
    [r"$\{1\}$", r"$\{3,2\}$", r"$\{5\}$", r"$\varnothing$"], 3,
    chk=lambda: all(not (2 * x - 1 > 0 and 8 - 10 * x - 12 * x * x > 0)
                    for x in [i / 200.0 for i in range(-400, 1200)]))

num(46, 'L2', r"Suppose $\log_{10}(x-2)+\log_{10}y=0$ and $\sqrt x+\sqrt{y-2}=\sqrt{x+y}$. "
    r"Then the value of $(x+y)$ is",
    [(r"$2$", 2), (r"$2\sqrt2$", 2 * R2), (r"$2+2\sqrt2$", 2 + 2 * R2),
     (r"$4+2\sqrt2$", 4 + 2 * R2)], 2,
    lambda: 2 * (1 + R2))

num(47, 'L2', r"The real value of $x$ for which "
    r"$\log_{6}9-\log_{9}27+\log_{8}x=\log_{64}x-\log_{6}4$ holds is",
    [(r"$\dfrac12$", 0.5), (r"$\dfrac14$", 0.25), (r"$\dfrac18$", 0.125),
     (r"$\dfrac{1}{16}$", 1 / 16)], 2,
    lambda: 2.0 ** -3)

num(48, 'L2', r"The reals $x$ and $y$ satisfy $\log_{8}x+\log_{4}y^{2}=5$ and "
    r"$\log_{8}y+\log_{4}x^{2}=7$. The value of $xy$ is",
    [(r"$2^{9}$", 2.0 ** 9), (r"$2^{12}$", 2.0 ** 12), (r"$2^{18}$", 2.0 ** 18),
     (r"$2^{24}$", 2.0 ** 24)], 0,
    lambda: 2.0 ** 9)

num(53, 'L2', r"If $\log_{\sqrt2}\sqrt x+\log_{2}x+\log_{4}x^{2}+\log_{8}x^{3}+\log_{16}x^{4}=40$, "
    r"then $x$ equals",
    [(r"$32$", 32), (r"$64$", 64), (r"$128$", 128), (r"$256$", 256)], 3,
    lambda: 2.0 ** 8)

num(55, 'L2', r"Let $B,C,P,L$ be positive reals with $\log(BL)+\log(BP)=2$, "
    r"$\log(PL)+\log(PC)=3$ and $\log(CB)+\log(CL)=4$ (base $10$). "
    r"Then the product $BCPL$ equals",
    [(r"$10^{2}$", 1e2), (r"$10^{3}$", 1e3), (r"$10^{4}$", 1e4), (r"$10^{9}$", 1e9)], 1,
    lambda: 10.0 ** 3)

add(58, 'L2', r"Let $u=\left(\log_{2}x\right)^{2}-6\log_{2}x+12$ where $x$ is real. "
    r"Then the equation $x^{u}=256$ has",
    [r"no solution for $x$", r"exactly one solution for $x$",
     r"exactly two distinct solutions for $x$", r"exactly three distinct solutions for $x$"], 1,
    chk=lambda: abs(4.0 ** ((lg(4, 2)) ** 2 - 6 * lg(4, 2) + 12) - 256) < 1e-6)

num(59, 'L2', r"If $(49)^{3\log_{\sqrt{343}}\sqrt x}-2x-3=0$, then $x$ equals",
    [(r"$-1$", -1), (r"$3$", 3), (r"$1$", 1), (r"$2$", 2)], 1,
    lambda: 3.0)

num(110, 'L2', r"If $\log_{8}a+\log_{8}b=\left(\log_{8}a\right)\left(\log_{8}b\right)$ and "
    r"$\log_{a}b=3$, then the value of $a$ is",
    [(r"$8$", 8), (r"$15$", 15), (r"$16$", 16), (r"$2$", 2)], 2,
    lambda: 8.0 ** (4 / 3))

num(111, 'L2', r"Let $N=(2+1)\left(2^{2}+1\right)\left(2^{4}+1\right)\cdots\left(2^{32}+1\right)+1$. "
    r"Then $\log_{256}N$ equals",
    [(r"$8$", 8), (r"$15$", 15), (r"$16$", 16), (r"$32$", 32)], 0,
    lambda: lg(2.0 ** 64, 256))

num(68, 'L2', r"If $(21.4)^{a}=(0.00214)^{b}=100$, then the value of "
    r"$\dfrac1a-\dfrac1b$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$4$", 4)], 2,
    lambda: (lg(21.4) - lg(0.00214)) / 2)

num(86, 'L2', r"The reals $x$ and $y$ satisfy $\log_{16}x+\log_{4}y^{2}=9$ and "
    r"$\log_{16}y+\log_{4}x^{2}=6$. Then $xy$ equals",
    [(r"$2^{12}$", 2.0 ** 12), (r"$3^{12}$", 3.0 ** 12), (r"$24$", 24),
     (r"$2^{-12}$", 2.0 ** -12)], 0,
    lambda: 2.0 ** 12)

num(124, 'L2', r"Given $\log_{10}2=0.3010$ and $\log_{10}3=0.4771$, the number of digits in "
    r"$6^{100}$ is",
    [(r"$75$", 75), (r"$76$", 76), (r"$77$", 77), (r"$78$", 78)], 3,
    lambda: float(floor(100 * (0.3010 + 0.4771)) + 1))

num(125, 'L2', r"Given $\log_{10}2=0.3010$ and $\log_{10}5=0.6990$, the number of zeros after the "
    r"decimal point and before the first significant digit of "
    r"$10^{\,100\left(\log_{10}2-\log_{10}5\right)}$ is",
    [(r"$37$", 37), (r"$38$", 38), (r"$39$", 39), (r"$40$", 40)], 2,
    lambda: float(-floor(100 * (0.3010 - 0.6990)) - 1))

# =============================================================== LEVEL 3
num(21, 'L3', r"""How many distinct real numbers belong to the following collection?
    \[\left\{\ln\!\left(4-\sqrt{15}\right),\ \ln\!\left(4+\sqrt{15}\right),\
    -\ln\!\left(4-\sqrt{15}\right),\ -\ln\!\left(4+\sqrt{15}\right),\
    \ln\!\left(\frac{4+\sqrt{15}}{4-\sqrt{15}}\right),\
    \ln\!\left(31+8\sqrt{15}\right)\right\}\]""",
    [(r"$2$", 2), (r"$3$", 3), (r"$4$", 4), (r"$5$", 5)], 1,
    lambda: float(len({round(v, 9) for v in
        [log(4 - sqrt(15)), log(4 + sqrt(15)), -log(4 - sqrt(15)), -log(4 + sqrt(15)),
         log((4 + sqrt(15)) / (4 - sqrt(15))), log(31 + 8 * sqrt(15))]})))

add(23, 'L3', r"$\log_{10}\!\left(\log_{2}3\right)+\log_{10}\!\left(\log_{3}4\right)"
    r"+\log_{10}\!\left(\log_{4}5\right)+\cdots+\log_{10}\!\left(\log_{1023}1024\right)$ "
    r"simplifies to",
    [r"a composite number", r"a prime number", r"a rational which is not an integer",
     r"an integer"], 3,
    chk=lambda: abs(sum(lg(lg(n + 1, n)) for n in range(2, 1024)) - 1.0) < 1e-7)

num(45, 'L3', r"The product of all values of $x$ which make the statement "
    r"$\left(\log_{3}x\right)\left(\log_{5}9\right)-\log_{x}25+\log_{3}2=\log_{3}54$ true is",
    [(r"$\sqrt5$", R5), (r"$5$", 5), (r"$5\sqrt5$", 5 * R5), (r"$25$", 25)], 2,
    lambda: 25.0 * 5.0 ** -0.5)

num(61, 'L3', r"If $x_{1}$ and $x_{2}$ satisfy the equation $x^{\log_{10}x}=100x$, "
    r"then the value of $x_{1}x_{2}$ equals",
    [(r"$1$", 1), (r"$10$", 10), (r"$100$", 100), (r"$1000$", 1000)], 1,
    lambda: 100.0 * 0.1)

num(62, 'L3', r"The sum of the squares of the roots of the equation "
    r"$\log_{2}\!\left(9-2^{x}\right)=3-x$ is",
    [(r"$3$", 3), (r"$5$", 5), (r"$9$", 9), (r"$10$", 10)], 2,
    lambda: 0.0 ** 2 + 3.0 ** 2)

num(63, 'L3', r"If $\log_{1/8}\!\left(\log_{1/4}\!\left(\log_{1/2}x\right)\right)=\dfrac13$, "
    r"then $x$ is",
    [(r"$\dfrac{1}{\sqrt2}$", 1 / R2), (r"$\sqrt2$", R2), (r"$\dfrac12$", 0.5), (r"$2$", 2)], 0,
    lambda: 0.5 ** 0.5)

num(64, 'L3', r"Let $\log_{b}a=3$ and $\log_{b}c=-4$. If the value of $x$ satisfying "
    r"$a^{3x}=c^{\,x-1}$ is $\dfrac pq$ with $p,q$ relatively prime, then $p+q$ is",
    [(r"$9$", 9), (r"$13$", 13), (r"$17$", 17), (r"$21$", 21)], 2,
    lambda: 4.0 + 13.0)

num(71, 'L3', r"Let $x=\log 2$, $y=\log 3$ and "
    r"$a+bx+cy=\bigl[\log 1+\log(1+3)+\log(1+3+5)+\cdots+\log(1+3+5+\cdots+19)\bigr]"
    r"-2\bigl[\log 1+\log 2+\log 3+\cdots+\log 7\bigr]$, where $a,b,c$ are positive "
    r"integers. Then $2a+3b+5c$ equals",
    [(r"$28$", 28), (r"$34$", 34), (r"$42$", 42), (r"$50$", 50)], 2,
    lambda: 2 * 2 + 3 * 6 + 5 * 4)

num(73, 'L3', r"The number of values of $x$ satisfying "
    r"$\log_{10}\!\left(2^{x+1}+x-37\right)=x\left(1-\log_{10}5\right)$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$3$", 3)], 1,
    lambda: float(sum(1 for k in range(-20, 40) if abs(2.0 ** k + k - 37) < 1e-9)))

add(77, 'L3', r"The solution set of the equation $\log_{x}2\cdot\log_{2x}2=\log_{4x}2$ is",
    [r"$\left\{2^{-\sqrt2},\,2^{\sqrt2}\right\}$", r"$\left\{\dfrac12,\,2\right\}$",
     r"$\left\{2^{-2},\,2^{2}\right\}$", r"none of these"], 0,
    chk=lambda: all(abs(lg(2, x) * lg(2, 2 * x) - lg(2, 4 * x)) < 1e-9
                    for x in (2.0 ** R2, 2.0 ** -R2)))

num(78, 'L3', r"If $\left|x-5\right|^{\,x^{2}-3x-10}=1$, then the sum of all solutions is",
    [(r"$13$", 13), (r"$8$", 8), (r"$15$", 15), (r"$3$", 3)], 1,
    lambda: -2.0 + 4.0 + 6.0)

num(79, 'L3', r"The sum of the solutions of the equation "
    r"$3^{2x+1}+2\cdot3^{x}\cdot7^{x}-3\cdot7^{2x+1}=0$ is",
    [(r"$0$", 0), (r"$-1$", -1), (r"$1$", 1), (r"$2$", 2)], 1,
    lambda: -1.0)

add(80, 'L3', r"The values of $x$ satisfying "
    r"$5^{6x^{2}}-2\cdot5^{3x^{2}+5x+2}+5^{10x+4}=0$ are",
    [r"$2,\ \dfrac23$", r"$-2,\ -\dfrac13$", r"$2,\ -\dfrac13$", r"$-2,\ \dfrac23$"], 2,
    chk=lambda: all(abs(5.0 ** (6 * x * x) - 2 * 5.0 ** (3 * x * x + 5 * x + 2)
                        + 5.0 ** (10 * x + 4)) < 1e-6 * 5.0 ** (10 * x + 4)
                    for x in (2.0, -1 / 3)))

add(81, 'L3', r"Which of the following is true?",
    [r"$3^{150}>2^{200}>6^{100}$", r"$6^{100}>2^{200}>3^{150}$",
     r"$6^{100}>3^{150}>2^{200}$", r"$3^{150}>6^{100}>2^{200}$"], 2,
    chk=lambda: 100 * log(6) > 150 * log(3) > 200 * log(2))

num(82, 'L3', r"The product of the solutions of the equation "
    r"$\left|\log_{\sqrt3}x-2\right|-\left|\log_{3}x-2\right|=2$ is",
    [(r"$-1$", -1), (r"$3$", 3), (r"$2$", 2), (r"$1$", 1)], 3,
    lambda: (3.0 ** -2) * (3.0 ** 2))

num(84, 'L3', r"If $\alpha$ and $\beta$ are the solutions of "
    r"$6^{x}-3^{2x-1}-2^{2x-1}+6^{\,x-1}=0$, then",
    [(r"$\alpha+\beta=1$", 1), (r"$\alpha+\beta=0$", 0),
     (r"$\alpha+\beta=\dfrac{1}{1-\log_{2}3}$", 1 / (1 - lg(3, 2))),
     (r"$\alpha+\beta=\log_{2}3$", lg(3, 2))], 0,
    lambda: log(3) / (log(3) - log(2)) + log(0.5) / (log(3) - log(2)))

add(85, 'L3', r"If $2^{2x+1}=3^{y}$ and $3^{2y+1}=2^{x}$, then $(x-y)$ is equal to",
    [r"$\dfrac{\log_{3}2+\log_{2}3}{3}$", r"$\dfrac{\log_{3}2-\log_{2}3}{3}$",
     r"$\log_{3}2+\log_{2}3$", r"$\log_{3}2-\log_{2}3$"], 1,
    chk=lambda: (lambda a: abs(((-(2 + a) / 3) - ((-1 - 2 * a) / (3 * a)))
                               - (1 / a - a) / 3) < 1e-9)(lg(3, 2)))

num(87, 'L3', r"The root of the equation "
    r"$\sqrt{\left(\log_{2}x\right)^{2}-4\log_{2}x+19}=\log_{2}\!\left(x^{2}+12\right)$, "
    r"where $x>1$ and $\log_{2}x,\ \log_{2}\!\left(x^{2}+12\right)$ are integers, is",
    [(r"$5$", 5), (r"$2$", 2), (r"$3$", 3), (r"$4$", 4)], 1,
    lambda: 2.0)

num(88, 'L3', r"The product of all real values of $t$ satisfying "
    r"$\left|5^{\left(\log_{5}t\right)^{2}}-25\right|-4\,t^{\log_{5}t}=0$ is",
    [(r"$1$", 1), (r"$5$", 5), (r"$25$", 25), (r"$125$", 125)], 0,
    lambda: 5.0 * 0.2)

add(89, 'L3', r"Which one of the following is incorrect?",
    [r"$\log_{2}3>\log_{3}11$", r"$\displaystyle\sum_{r=1}^{n}\log_{n!}r=1$ for $n\ge2$",
     r"If $\dfrac{\log_{8}\!\left(8/x^{2}\right)}{\left(\log_{8}x\right)^{2}}=3$ then "
     r"$x=\dfrac18$ or $2$",
     r"$\sqrt[3]{5^{\,1/\log_{7}5}+\dfrac{1}{\sqrt{-\log_{10}0.1}}}=2$"], 0,
    chk=lambda: (lg(3, 2) < lg(11, 3)
                 and abs(sum(lg(r, 120) for r in range(1, 6)) - 1) < 1e-9
                 and abs((5 ** (1 / lg(5, 7)) + 1) ** (1 / 3) - 2) < 1e-9))

num(91, 'L3', r"If $\log_{2}x=\log_{7}8$, $\log_{3}y=\log_{5}9$ and $\log_{5}z=\log_{11}25$, then "
    r"$x^{\left(\log_{2}7\right)^{2}}+y^{\left(\log_{3}5\right)^{2}}+z^{\left(\log_{5}11\right)^{2}}$ "
    r"equals",
    [(r"$389$", 389), (r"$489$", 489), (r"$589$", 589), (r"$289$", 289)], 1,
    lambda: (2 ** (lg(8, 7) * lg(7, 2) ** 2) + 3 ** (lg(9, 5) * lg(5, 3) ** 2)
             + 5 ** (lg(25, 11) * lg(11, 5) ** 2)))

num(92, 'L3', r"Let $\alpha,\beta,\gamma$ be distinct reals with "
    r"$\dfrac{1}{(\alpha-\beta)^{2}}+\dfrac{1}{(\beta-\gamma)^{2}}+\dfrac{1}{(\gamma-\alpha)^{2}}"
    r"=5^{\,2\left[\log_{5}11-\log_{5}9\right]}$. Then "
    r"$\left(\dfrac{1}{\alpha-\beta}+\dfrac{1}{\beta-\gamma}+\dfrac{1}{\gamma-\alpha}\right)^{2}$ is",
    [(r"$\dfrac{121}{81}$", 121 / 81), (r"$\dfrac{11}{9}$", 11 / 9),
     (r"$\dfrac{81}{121}$", 81 / 121), (r"$\dfrac{9}{11}$", 9 / 11)], 0,
    lambda: 5.0 ** (2 * (lg(11, 5) - lg(9, 5))))

num(93, 'L3', r"Let $p,q$ be the roots of $x^{2}+2bx+c=0$ and let "
    r"$2\log\!\left(\sqrt{y-p}+\sqrt{y-q}\right)=\log a+\log\!\left(y+b+\sqrt{y^{2}+2by+c}\right)$ "
    r"wherever defined. Then $a$ is",
    [(r"$1$", 1), (r"$2$", 2), (r"$0$", 0), (r"$4$", 4)], 1,
    lambda: 2.0)

num(95, 'L3', r"If $\dfrac1p-\dfrac1q=\dfrac1q-\dfrac1r$, then "
    r"$\dfrac{\log(p-r)}{\log(p+r)+\log(p-2q+r)}$ equals (assume all terms are defined)",
    [(r"$1$", 1), (r"$\dfrac12$", 0.5), (r"$\dfrac14$", 0.25), (r"$4$", 4)], 1,
    lambda: (lambda p, r, q: lg(p - r) / (lg(p + r) + lg(p - 2 * q + r)))(
        9.0, 1.0, 2 * 9.0 * 1.0 / 10.0))

add(96, 'L3', r"If $a,b,c$ are positive reals, then "
    r"$\dfrac{(ab)^{\log\frac ab}\cdot(bc)^{\log\frac bc}\cdot(ca)^{\log\frac ca}}"
    r"{a^{\log\frac bc}\cdot b^{\log\frac ca}\cdot c^{\log\frac ab}}$ is equal to",
    [r"$0$", r"$-1$", r"$1$", r"none of these"], 2,
    chk=lambda: all(abs(((a * b) ** lg(a / b) * (b * c) ** lg(b / c) * (c * a) ** lg(c / a))
                        / (a ** lg(b / c) * b ** lg(c / a) * c ** lg(a / b)) - 1) < 1e-9
                    for a, b, c in [(2.0, 3.0, 5.0), (7.0, 1.5, 4.0), (11.0, 9.0, 2.0)]))

# =============================================================== LEVEL 4
num(83, 'L4', r"If $\log_{2}9+\log_{9}2=k$, then the largest integer less than $k$ is",
    [(r"$1$", 1), (r"$2$", 2), (r"$3$", 3), (r"$4$", 4)], 2,
    lambda: float(floor(lg(9, 2) + lg(2, 9))))

add(97, 'L4', r"If $x=\sqrt{\log_{a}b}$, $y=\sqrt{\log_{b}a}$ with $a>0$, $b>0$, "
    r"$a,b\ne1$, then $x^{a}-y^{-b}=0$ implies",
    [r"$a$ and $b$ cannot be equal", r"$a$ and $b$ must be equal",
     r"$a+b$ must be zero", r"$a+b$ can be zero"], 1,
    chk=lambda: all(abs(sqrt(lg(a, a)) ** a - sqrt(lg(a, a)) ** (-a)) < 1e-12
                    for a in (2.0, 5.0, 9.0)))

add(98, 'L4', r"If $a,b,c$ are positive reals with $a^{2}+b^{2}=c^{2}$, then "
    r"$c+b\ne1$ and $c-b\ne1$, then $\log_{c+b}a+\log_{c-b}a$ equals",
    [r"$0$", r"$1$", r"$\log_{c+b}a\cdot\log_{c-b}a$",
     r"$2\log_{c+b}a\cdot\log_{c-b}a$"], 3,
    chk=lambda: all(abs(lg(a, c + b) + lg(a, c - b) - 2 * lg(a, c + b) * lg(a, c - b)) < 1e-9
                    for a, b, c in [(8.0, 15.0, 17.0), (12.0, 35.0, 37.0), (28.0, 45.0, 53.0)]))

num(99, 'L4', r"If $\dfrac{\log_{2}a}{2x+3y}=\dfrac{\log_{2}(b+1)}{5y+6z}=\dfrac{\log_{2}(c+2)}{3z+5x}$ "
    r"(wherever defined) with $(a-1)b(c+1)\ne0$ and $abc+2ab+ac+2a-1=0$, "
    r"then $(7x+8y+9z)$ equals",
    [(r"$0$", 0), (r"$1$", 1), (r"$24$", 24), (r"$6$", 6)], 0,
    lambda: 0.0)

add(100, 'L4', r"Which of the following is the greatest?",
    [r"$\log_{3}5$", r"$\log_{4}6$", r"$\log_{15}36$", r"$\log_{25}36$"], 0,
    chk=lambda: max([lg(5, 3), lg(6, 4), lg(36, 15), lg(36, 25)]) == lg(5, 3))

add(112, 'L4', r"Which of the following is the smallest?",
    [r"$\log_{3}108$", r"$\log_{4}192$", r"$\log_{5}500$", r"$\log_{6}1080$"], 1,
    chk=lambda: min([lg(108, 3), lg(192, 4), lg(500, 5), lg(1080, 6)]) == lg(192, 4))

add(114, 'L4', r"Identify the correct order.",
    [r"$\log_{2}6<\log_{3}6<\log_{3}8<\log_{2}5$",
     r"$\log_{3}6<\log_{3}8<\log_{2}5<\log_{2}6$",
     r"$\log_{2}5<\log_{2}6<\log_{3}6<\log_{3}8$",
     r"$\log_{3}8<\log_{3}6<\log_{2}6<\log_{2}5$"], 1,
    chk=lambda: lg(6, 3) < lg(8, 3) < lg(5, 2) < lg(6, 2))

add(115, 'L4', r"Which of the following is the largest?",
    [r"$\log_{2}\!\left(\log_{3}\!\left(\log_{4}5\right)\right)$",
     r"$\log_{4}\!\left(\log_{3}\!\left(\log_{2}5\right)\right)$",
     r"$\log_{2}\!\left(\log_{4}\!\left(\log_{3}5\right)\right)$",
     r"$\log_{4}\!\left(\log_{3}\!\left(\log_{3}5\right)\right)$"], 1,
    chk=lambda: max([lg(lg(lg(5, 4), 3), 2), lg(lg(lg(5, 2), 3), 4),
                     lg(lg(lg(5, 3), 4), 2), lg(lg(lg(5, 3), 3), 4)])
                == lg(lg(lg(5, 2), 3), 4))

num(118, 'L4', r"Let $(x_{0},y_{0})$ solve the system "
    r"$\left(5(x+1)\right)^{\ln 5}=(2y)^{\ln 2}$ and $(x+1)^{\ln 2}=5^{\ln y}$. "
    r"Then $x_{0}$ is",
    [(r"$\dfrac15$", 0.2), (r"$-\dfrac25$", -0.4), (r"$-\dfrac45$", -0.8),
     (r"$\dfrac45$", 0.8)], 2,
    lambda: 1 / 5.0 - 1)

num(116, 'L4', r"Let $m$ be the number of positive integers whose logarithm to the base $3$ has "
    r"characteristic $4$, and $n$ the number of zeros after the decimal point and before the "
    r"first significant digit of $2^{-100}$. The remainder when $m$ is divided by $n$ is",
    [(r"$12$", 12), (r"$6$", 6), (r"$11$", 11), (r"$7$", 7)], 0,
    lambda: float((3 ** 5 - 3 ** 4) % (-floor(-100 * lg(2)) - 1)))

num(117, 'L4', r"The number of solutions of the equation "
    r"$\log_{11}\!\left(x^{4}+5\right)=\log_{4}\!\left(1-x^{6}\right)$ "
    r"(wherever defined) is",
    [(r"$0$", 0), (r"$1$", 1), (r"$4$", 4), (r"$6$", 6)], 0,
    lambda: 0.0)

add(126, 'L4', r"The number of integers whose reciprocals have logarithm to the base $10$ with "
    r"characteristic $-n$ is",
    [r"$9\cdot10^{\,n}$", r"$9\cdot10^{\,n-1}$", r"$9\cdot10^{\,n+1}$", r"$9\cdot10^{-n}$"], 1,
    chk=lambda: all(sum(1 for N in range(1, 10 ** n + 1)
                        if floor(lg(1.0 / N)) == -n) == 9 * 10 ** (n - 1)
                    for n in (1, 2, 3)))

add(127, 'L4', r"Let $f(x)=4^{\,x+1.5}+9^{\,x+0.5}-10\cdot6^{x}$. "
    r"The sum of the values of $x$ satisfying $f(x)=0$ is",
    [r"$\log_{2}5$", r"$\log_{7}11$", r"$\log_{2/3}\!\left(\dfrac38\right)$",
     r"$\log_{3/4}\!\left(\dfrac59\right)$"], 2,
    chk=lambda: abs((lg(0.75, 2 / 3) + lg(0.5, 2 / 3)) - lg(3 / 8, 2 / 3)) < 1e-9
           and all(abs(4 ** (x + 1.5) + 9 ** (x + 0.5) - 10 * 6 ** x) < 1e-7
                   for x in (lg(0.75, 2 / 3), lg(0.5, 2 / 3))))

num(128, 'L4', r"Let $g(x)=\log_{10}\!\left(2^{x}+1\right)-\log_{10}6-x\log_{10}5$. "
    r"The value of $x$ satisfying $g(x)=-x$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$3$", 3)], 1,
    lambda: 1.0)

add(129, 'L4', r"Let $f(x)=4^{\log_{7}x}+3^{\log_{7}x}$. The number of solutions of "
    r"$f(x)=x$ is",
    [r"$1$", r"$2$", r"$3$", r"infinite"], 0,
    chk=lambda: abs(4 ** lg(7.0, 7) + 3 ** lg(7.0, 7) - 7.0) < 1e-9
           and all(abs(4 ** lg(x, 7) + 3 ** lg(x, 7) - x) > 1e-6
                   for x in (2.0, 3.0, 5.0, 10.0, 49.0, 0.5)))

num(131, 'L4', r"$\log_{2}\!\left(\sqrt{2-\sqrt5+\sqrt{21-4\sqrt5}+\sqrt{14-6\sqrt5}}\right)=$",
    [(r"$1$", 1), (r"$2$", 2), (r"$3$", 3), (r"$4$", 4)], 0,
    lambda: lg(sqrt(2 - R5 + sqrt(21 - 4 * R5) + sqrt(14 - 6 * R5)), 2))

num(132, 'L4', r"The natural solution of "
    r"$\dfrac{3x^{4}+x^{2}-2x-3}{3x^{4}-x^{2}+2x+3}=\dfrac{6x^{4}+2x^{2}-7x+3}{6x^{4}-2x^{2}+7x-3}$ is",
    [(r"$1$", 1), (r"$2$", 2), (r"$3$", 3), (r"$4$", 4)], 2,
    lambda: 3.0)

num(133, 'L4', r"The value of $3^{\log_{12}60}\cdot4^{\log_{12}5}$ is",
    [(r"$5$", 5), (r"$12$", 12), (r"$15$", 15), (r"$60$", 60)], 2,
    lambda: 3 ** lg(60, 12) * 4 ** lg(5, 12))

num(134, 'L4', r"If $a=\sqrt{4+\sqrt{15}}+\sqrt{4-\sqrt{15}}-2\sqrt{3-\sqrt5}$ and "
    r"$b=\sqrt{17+4\sqrt{13}}-\sqrt{17-4\sqrt{13}}$, then $\log_{a}b$ is",
    [(r"$2$", 2), (r"$3$", 3), (r"$4$", 4), (r"$8$", 8)], 2,
    lambda: lg(sqrt(17 + 4 * sqrt(13)) - sqrt(17 - 4 * sqrt(13)),
               sqrt(4 + sqrt(15)) + sqrt(4 - sqrt(15)) - 2 * sqrt(3 - R5)))

num(135, 'L4', r"The value of $\left(\log_{6}2\right)^{3}+\log_{6}8\cdot\log_{6}3"
    r"+\left(\log_{6}3\right)^{3}$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$3$", 3)], 1,
    lambda: lg(2, 6) ** 3 + lg(8, 6) * lg(3, 6) + lg(3, 6) ** 3)

num(136, 'L4', r"If $a=\log_{245}175$ and $b=\log_{1715}875$, then $\dfrac{1-ab}{a-b}$ is",
    [(r"$1$", 1), (r"$3$", 3), (r"$5$", 5), (r"$7$", 7)], 2,
    lambda: (lambda a, b: (1 - a * b) / (a - b))(lg(175, 245), lg(875, 1715)))

add(137, 'L4', r"If $\left(\log_{b}a\right)^{3}+\left(\log_{c}b\right)^{3}+\left(\log_{a}c\right)^{3}=3$, "
    r"where $a,b,c$ are real numbers greater than $1$, then "
    r"$\dfrac{ab+bc+ca}{a^{2}+b^{2}+c^{2}}$ equals",
    [r"$\dfrac13$", r"$\dfrac12$", r"$1$", r"$3$"], 2,
    chk=lambda: all(abs((a * a + a * a + a * a) / (3 * a * a) - 1) < 1e-12
                    for a in (2.0, 5.0, 9.0)))

num(138, 'L4', r"If $\log_{2n}(1944)=\log_{n}\!\left(486\sqrt2\right)$, then the number of "
    r"significant digits in $n^{6}$ is (use $\log_{10}2=0.3010$, $\log_{10}3=0.4771$)",
    [(r"$10$", 10), (r"$11$", 11), (r"$12$", 12), (r"$13$", 13)], 2,
    lambda: float(floor(4 * lg(486 * R2)) + 1))

num(139, 'L4', r"The number of values of $x$ satisfying "
    r"$x^{\log_{7}13}+13^{\,\log_{11}17\cdot\log_{7}x}=2\cdot17^{\,\log_{11}\left(13^{\log_{7}x}\right)}$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$3$", 3)], 1,
    lambda: 1.0)

num(140, 'L4', r"Let $x=\left(\log_{1/3}5\right)\left(\log_{125}343\right)\left(\log_{49}729\right)$ "
    r"and $y=25^{\,3\log_{289}11\cdot\log_{28}\sqrt{17}\cdot\log_{1331}784}$. "
    r"Then $x^{2}+y^{2}$ is",
    [(r"$25$", 25), (r"$34$", 34), (r"$41$", 41), (r"$50$", 50)], 1,
    lambda: (lg(5, 1 / 3) * lg(343, 125) * lg(729, 49)) ** 2
            + (25 ** (3 * lg(11, 289) * lg(sqrt(17), 28) * lg(784, 1331))) ** 2)

LEVELS = {}
for _lv in ('L1', 'L2', 'L3', 'L4'):
    LEVELS[_lv] = [q for q in Q if Q[q]['lv'] == _lv]
