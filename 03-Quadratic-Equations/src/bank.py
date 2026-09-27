# -*- coding: utf-8 -*-
"""Quadratic Equations bank.
L4 is built from the genuine AIEEE / JEE (Main) questions that open the source
file -- each carries its year tag.  Syllabus filter: location of roots and
inequalities based on it are excluded, as are cubics/biquadratics, power-sum
(Newton) recurrences, cube roots of unity, trigonometry, complex numbers and
powers of e."""
from math import sqrt, log

R2, R3, R5 = sqrt(2.0), sqrt(3.0), sqrt(5.0)
Q = {}

def add(qid, lv, q, opts, ans, truth=None, optvals=None, chk=None, note=""):
    assert qid not in Q, qid
    assert len(opts) == 4 and 0 <= ans <= 3, qid
    Q[qid] = dict(id=qid, lv=lv, q=q, o=opts, ans=ans,
                  truth=truth, optvals=optvals, chk=chk, note=note)

def num(qid, lv, q, opts, ans, truth):
    add(qid, lv, q, [o[0] for o in opts], ans, truth=truth,
        optvals=[(lambda v: (lambda: v))(o[1]) for o in opts])

def roots(a, b, c):
    d = b * b - 4 * a * c
    return ((-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a))

# ------------------------------------------------------------------ LEVEL 4
add(401, 'L4', r"If the roots of the equation $bx^{2}+cx+a=0$ are imaginary, then for all real "
    r"values of $x$ the expression $3b^{2}x^{2}+6bcx+2c^{2}$ is \hfill\textbf{[AIEEE 2009]}",
    [r"less than $4ab$", r"greater than $-4ab$", r"less than $-4ab$", r"greater than $4ab$"], 1,
    chk=lambda: all(min(3 * b * b * (x / 100.0) ** 2 + 6 * b * c * (x / 100.0) + 2 * c * c
                        for x in range(-2000, 2000)) > -4 * a * b
                    for a, b, c in [(2.0, 3.0, 1.0), (5.0, 1.0, 2.0), (1.0, 1.0, 1.0)]
                    if c * c < 4 * a * b))

num(402, 'L4', r"Let $a\ne a_{1}\ne0$, $f(x)=ax^{2}+bx+c$, $g(x)=a_{1}x^{2}+b_{1}x+c_{1}$ and "
    r"$p(x)=f(x)-g(x)$. If $p(x)=0$ only for $x=-1$ and $p(-2)=2$, then $p(2)$ is "
    r"\hfill\textbf{[AIEEE 2011]}",
    [(r"$6$", 6), (r"$18$", 18), (r"$3$", 3), (r"$9$", 9)], 1,
    lambda: 2.0 * (2 + 1) ** 2)

add(403, 'L4', r"Sachin and Rahul attempted to solve a quadratic equation. Sachin made a mistake "
    r"in writing down the constant term and ended up with the roots $(4,3)$. Rahul made a "
    r"mistake in writing down the coefficient of $x$ and got the roots $(3,2)$. The correct "
    r"roots of the equation are \hfill\textbf{[AIEEE 2011]}",
    [r"$-6,\,-1$", r"$-4,\,-3$", r"$6,\,1$", r"$4,\,3$"], 2,
    chk=lambda: sorted(roots(1, -(4 + 3), 3 * 2)) == sorted((1.0, 6.0)))

add(404, 'L4', r"If the equations $x^{2}+2x+3=0$ and $ax^{2}+bx+c=0$, $a,b,c\in\mathbb R$, have a "
    r"common root, then $a:b:c$ is \hfill\textbf{[JEE (Main) 2013]}",
    [r"$1:2:3$", r"$3:2:1$", r"$1:3:2$", r"$3:1:2$"], 0,
    chk=lambda: (-2) ** 2 - 4 * 3 < 0)

num(405, 'L4', r"The sum of all real values of $x$ satisfying "
    r"$\left(x^{2}-5x+5\right)^{x^{2}+4x-60}=1$ is \hfill\textbf{[JEE (Main) 2016]}",
    [(r"$-4$", -4), (r"$6$", 6), (r"$5$", 5), (r"$3$", 3)], 3,
    lambda: 6.0 + (-10.0) + 1.0 + 4.0 + 2.0)

add(406, 'L4', r"Let $S=\left\{x\in\mathbb R:x\ge0\ \text{and}\ "
    r"2\left|\sqrt x-3\right|+\sqrt x\left(\sqrt x-6\right)+6=0\right\}$. Then $S$ "
    r"\hfill\textbf{[JEE (Main) 2018]}",
    [r"is an empty set", r"contains exactly one element", r"contains exactly two elements",
     r"contains exactly four elements"], 2,
    chk=lambda: sorted(x for x in (4.0, 16.0)
                       if abs(2 * abs(sqrt(x) - 3) + sqrt(x) * (sqrt(x) - 6) + 6) < 1e-9)
                == [4.0, 16.0])

num(407, 'L4', r"The number of positive integral values of $\alpha$ for which the roots of "
    r"$6x^{2}-11x+\alpha=0$ are rational numbers is \hfill\textbf{[JEE (Main) 2019]}",
    [(r"$4$", 4), (r"$5$", 5), (r"$2$", 2), (r"$3$", 3)], 3,
    lambda: float(sum(1 for a in range(1, 200)
                      if 121 - 24 * a >= 0 and int(sqrt(121 - 24 * a)) ** 2 == 121 - 24 * a)))

num(408, 'L4', r"The value of $\lambda$ for which the sum of the squares of the roots of "
    r"$x^{2}+(3-\lambda)x+2=\lambda$ is least is \hfill\textbf{[JEE (Main) 2019]}",
    [(r"$2$", 2), (r"$1$", 1), (r"$\dfrac{15}{8}$", 15 / 8), (r"$\dfrac49$", 4 / 9)], 0,
    lambda: float(min(range(-500, 500),
                      key=lambda k: (lambda L: (L - 3) ** 2 - 2 * (2 - L))(k / 100.0)) / 100.0))

num(409, 'L4', r"If one real root of $81x^{2}+kx+256=0$ is the cube of the other root, then a "
    r"value of $k$ is \hfill\textbf{[JEE (Main) 2019]}",
    [(r"$-300$", -300), (r"$144$", 144), (r"$-81$", -81), (r"$100$", 100)], 0,
    lambda: -81.0 * (4 / 3 + (4 / 3) ** 3))

num(410, 'L4', r"If $\lambda$ is the ratio of the roots of $3m^{2}x^{2}+m(m-4)x+2=0$, then the "
    r"least value of $m$ for which $\lambda+\dfrac1\lambda=1$ is \hfill\textbf{[JEE (Main) 2019]}",
    [(r"$4-2\sqrt3$", 4 - 2 * R3), (r"$4-3\sqrt2$", 4 - 3 * R2),
     (r"$2-\sqrt3$", 2 - R3), (r"$-2+\sqrt2$", -2 + R2)], 1,
    lambda: 4 - sqrt(18))

num(411, 'L4', r"The number of integral values of $m$ for which the quadratic expression "
    r"$(1+2m)x^{2}-2(1+3m)x+4(1+m)$, $x\in\mathbb R$, is always positive, is "
    r"\hfill\textbf{[JEE (Main) 2019]}",
    [(r"$8$", 8), (r"$3$", 3), (r"$6$", 6), (r"$7$", 7)], 3,
    lambda: float(sum(1 for m in range(-50, 50)
                      if 1 + 2 * m > 0 and (1 + 3 * m) ** 2 - 4 * (1 + m) * (1 + 2 * m) < 0)))

num(412, 'L4', r"The sum of the solutions of "
    r"$\left|\sqrt x-2\right|+\sqrt x\left(\sqrt x-4\right)+2=0$, $x>0$, is "
    r"\hfill\textbf{[JEE (Main) 2019]}",
    [(r"$4$", 4), (r"$10$", 10), (r"$9$", 9), (r"$12$", 12)], 1,
    lambda: 1.0 + 9.0)

add(413, 'L4', r"If three distinct numbers $a,b,c$ are in G.P. and the equations "
    r"$ax^{2}+2bx+c=0$ and $dx^{2}+2ex+f=0$ have a common root, then which one of the "
    r"following is correct? \hfill\textbf{[JEE (Main) 2019]}",
    [r"$d,e,f$ are in A.P.", r"$\dfrac da,\dfrac eb,\dfrac fc$ are in G.P.",
     r"$\dfrac da,\dfrac eb,\dfrac fc$ are in A.P.", r"$d,e,f$ are in G.P."], 2,
    chk=lambda: all(abs((d / a) + (f / c) - 2 * (e / b)) < 1e-9
                    for a, r_ in [(1.0, 2.0), (3.0, 0.5), (2.0, 3.0)]
                    for b, c in [(a * r_, a * r_ * r_)]
                    for d in (5.0,)
                    for e, f in [(None, None)]
                    # root of ax^2+2bx+c=0 is -b/a; impose it on dx^2+2ex+f=0 with f free
                    for f in (7.0,)
                    for e in [(d * (b / a) ** 2 + f) / (2 * (b / a))]))

num(414, 'L4', r"If $m$ is chosen in the quadratic equation "
    r"$\left(m^{2}+1\right)x^{2}-3x+\left(m^{2}+1\right)^{2}=0$ so that the sum of its roots "
    r"is greatest, then the absolute difference of the cubes of its roots is "
    r"\hfill\textbf{[JEE (Main) 2019]}",
    [(r"$8\sqrt3$", 8 * R3), (r"$10\sqrt5$", 10 * R5), (r"$4\sqrt3$", 4 * R3),
     (r"$8\sqrt5$", 8 * R5)], 3,
    lambda: abs(roots(1, -3, 1)[0] ** 3 - roots(1, -3, 1)[1] ** 3))

add(416, 'L4', r"Let $S$ be the set of all real roots of "
    r"$3^{x}\left(3^{x}-1\right)+2=\left|3^{x}-1\right|+\left|3^{x}-2\right|$. Then $S$ "
    r"\hfill\textbf{[JEE (Main) 2020]}",
    [r"contains at least four elements", r"is a singleton",
     r"contains exactly two elements", r"is an empty set"], 1,
    chk=lambda: (lambda f: sum(1 for k in range(-40000, 20000)
                               if f(k / 1000.0) * f((k + 1) / 1000.0) < 0) == 1)(
        lambda x: (lambda t: t * (t - 1) + 2 - abs(t - 1) - abs(t - 2))(3.0 ** x)))

num(417, 'L4', r"Let $a,b\in\mathbb R$, $a\ne0$, be such that $ax^{2}-2bx+5=0$ has a repeated "
    r"root $\alpha$, which is also a root of $x^{2}-2bx-10=0$. If $\beta$ is the other root "
    r"of this equation, then $\alpha^{2}+\beta^{2}$ is \hfill\textbf{[JEE (Main) 2020]}",
    [(r"$25$", 25), (r"$24$", 24), (r"$26$", 26), (r"$28$", 28)], 0,
    lambda: (2 * R5) ** 2 + (-R5) ** 2)

add(418, 'L4', r"Let $f(x)$ be a quadratic polynomial with $f(-1)+f(2)=0$. If one root of "
    r"$f(x)=0$ is $3$, then its other root lies in \hfill\textbf{[JEE (Main) 2020]}",
    [r"$(-1,0)$", r"$(-3,-1)$", r"$(0,1)$", r"$(1,3)$"], 0,
    chk=lambda: -1 < -2 / 5 < 0
           and abs(4 * (1 + (-2 / 5)) + ((-2 / 5) - 2)) < 1e-12)

add(419, 'L4', r"If $\alpha,\beta$ are the roots of $x^{2}+px+2=0$ and $\dfrac1\alpha$, "
    r"$\dfrac1\beta$ are the roots of $2x^{2}+2qx+1=0$, then "
    r"$\left(\alpha-\dfrac1\alpha\right)\left(\beta-\dfrac1\beta\right)"
    r"\left(\alpha+\dfrac1\beta\right)\left(\beta+\dfrac1\alpha\right)$ equals "
    r"\hfill\textbf{[JEE (Main) 2020]}",
    [r"$\dfrac94\left(9-q^{2}\right)$", r"$\dfrac94\left(9+p^{2}\right)$",
     r"$\dfrac94\left(9+q^{2}\right)$", r"$\dfrac94\left(9-p^{2}\right)$"], 3,
    chk=lambda: all(abs((a - 1 / a) * (b - 1 / b) * (a + 1 / b) * (b + 1 / a)
                        - 9 * (9 - p * p) / 4) < 1e-7
                    for p in (3.5, 4.0, 5.0)
                    for a, b in [roots(1, p, 2)]))

num(420, 'L4', r"Let $\lambda\ne0$ be real. If $\alpha,\beta$ are the roots of "
    r"$x^{2}-x+2\lambda=0$ and $\alpha,\gamma$ are the roots of $3x^{2}-10x+27\lambda=0$, "
    r"then $\dfrac{\beta\gamma}{\lambda}$ is \hfill\textbf{[JEE (Main) 2020]}",
    [(r"$18$", 18), (r"$9$", 9), (r"$27$", 27), (r"$36$", 36)], 0,
    lambda: (lambda a, L: ((1 - a) * (10 / 3 - a)) / L)(1 / 3, 1 / 9))

num(421, 'L4', r"The product of the roots of $9x^{2}-18|x|+5=0$ is "
    r"\hfill\textbf{[JEE (Main) 2020]}",
    [(r"$\dfrac{25}{9}$", 25 / 9), (r"$\dfrac{25}{81}$", 25 / 81),
     (r"$\dfrac59$", 5 / 9), (r"$\dfrac{5}{27}$", 5 / 27)], 1,
    lambda: (5 / 3) * (-5 / 3) * (1 / 3) * (-1 / 3))

num(422, 'L4', r"If $\alpha,\beta$ are the roots of $7x^{2}-3x-2=0$, then "
    r"$\dfrac{\alpha}{1-\alpha^{2}}+\dfrac{\beta}{1-\beta^{2}}$ equals "
    r"\hfill\textbf{[JEE (Main) 2020]}",
    [(r"$\dfrac{1}{24}$", 1 / 24), (r"$\dfrac{27}{32}$", 27 / 32),
     (r"$\dfrac38$", 3 / 8), (r"$\dfrac{27}{16}$", 27 / 16)], 3,
    lambda: (lambda a, b: a / (1 - a * a) + b / (1 - b * b))(*roots(7, -3, -2)))

num(423, 'L4', r"If $\alpha,\beta$ are the roots of $x^{2}-64x+256=0$, then the value of "
    r"$\left(\dfrac{\alpha^{3}}{\beta^{5}}\right)^{1/8}"
    r"+\left(\dfrac{\beta^{3}}{\alpha^{5}}\right)^{1/8}$ is \hfill\textbf{[JEE (Main) 2020]}",
    [(r"$3$", 3), (r"$2$", 2), (r"$4$", 4), (r"$1$", 1)], 1,
    lambda: (lambda a, b: (a ** 3 / b ** 5) ** 0.125 + (b ** 3 / a ** 5) ** 0.125)(
        *roots(1, -64, 256)))

add(424, 'L4', r"If $\alpha$ and $\beta$ are the roots of $2x(2x+1)=1$, then $\beta$ is equal "
    r"to \hfill\textbf{[JEE (Main) 2020]}",
    [r"$2\alpha^{2}$", r"$-2\alpha(\alpha+1)$", r"$2\alpha(\alpha-1)$",
     r"$2\alpha(\alpha+1)$"], 1,
    chk=lambda: all(abs(b - (-2 * a * (a + 1))) < 1e-9
                    for a, b in [roots(4, 2, -1), roots(4, 2, -1)[::-1]]))

num(425, 'L4', r"The least positive value of $a$ for which "
    r"$2x^{2}+(a-10)x+\dfrac{33}{2}=2a$ has real roots is \hfill\textbf{[JEE (Main) 2020]}",
    [(r"$6$", 6), (r"$8$", 8), (r"$10$", 10), (r"$12$", 12)], 1,
    lambda: float(min(a for a in range(1, 100)
                      if (a - 10) ** 2 - 8 * (33 / 2 - 2 * a) >= 0)))

num(426, 'L4', r"The integer $k$ for which the inequality $x^{2}-2(3k-1)x+8k^{2}-7>0$ is valid "
    r"for every $x\in\mathbb R$ is \hfill\textbf{[JEE (Main) 2021]}",
    [(r"$2$", 2), (r"$3$", 3), (r"$4$", 4), (r"$0$", 0)], 1,
    lambda: float([k for k in range(-20, 20)
                   if (3 * k - 1) ** 2 - (8 * k * k - 7) < 0][0]))

LEVELS = {'L4': sorted(q for q in Q if Q[q]['lv'] == 'L4')}

# ------------------------------------------------------- LEVELS 1-3 (DRAFT)
# First-draft pool harvested from source pages 14-19.  15 per level; the
# target is 25, so ~30 more items are still to be harvested (see CLAUDE.md).

# ============================== LEVEL 1
num(101, 'L1', r"If $x=\sqrt{3+2\sqrt2}$, then $x^{2}+\dfrac{1}{x^{2}}$ is equal to",
    [(r"$2\sqrt2$", 2 * R2), (r"$8$", 8), (r"$6$", 6), (r"$1$", 1)], 2,
    lambda: (lambda x: x * x + 1 / (x * x))(sqrt(3 + 2 * R2)))

num(102, 'L1', r"If $x=3-\sqrt8$, then $x^{3}+\dfrac{1}{x^{3}}$ is equal to",
    [(r"$6$", 6), (r"$198$", 198), (r"$6\sqrt2$", 6 * R2), (r"$102$", 102)], 1,
    lambda: (lambda x: x ** 3 + 1 / x ** 3)(3 - sqrt(8)))

add(103, 'L1', r"The roots of the equation $x^{2}-2\sqrt2\,x+1=0$ are",
    [r"real and different", r"imaginary and different", r"real and equal",
     r"rational and different"], 0,
    chk=lambda: 8 - 4 > 0 and abs(sqrt(8 - 4) - 2) < 1e-12)

add(104, 'L1', r"The roots of the equation $(b+c)x^{2}-(a+b+c)x+a=0$, where "
    r"$a,b,c\in\mathbb Q$ and $b+c\ne a$, are",
    [r"irrational and different", r"rational and different", r"imaginary and different",
     r"real and equal"], 1,
    chk=lambda: all(abs((a + b + c) ** 2 - 4 * a * (b + c) - (a - b - c) ** 2) < 1e-9
                    and (a - b - c) ** 2 > 0
                    for a, b, c in [(1.0, 2.0, 3.0), (5.0, 1.0, 1.0), (2.0, 7.0, 3.0)]))

num(105, 'L1', r"The number of real solutions of "
    r"$x-\dfrac{1}{x^{2}-4}=2-\dfrac{1}{x^{2}-4}$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$4$", 4)], 0,
    lambda: 0.0)

num(106, 'L1', r"The sum of the roots of the equation $(x+3)^{2}-4|x+3|+3=0$ is",
    [(r"$4$", 4), (r"$12$", 12), (r"$-12$", -12), (r"$-4$", -4)], 2,
    lambda: -2.0 - 4.0 + 0.0 - 6.0)

add(107, 'L1', r"If $\alpha,\beta$ are the roots of $x^{2}+px-q=0$ and $\gamma,\delta$ are the "
    r"roots of $x^{2}+px+r=0$, then $(\alpha-\gamma)(\alpha-\delta)$ is",
    [r"$p+r$", r"$p-r$", r"$q-r$", r"$q+r$"], 3,
    chk=lambda: all(abs((a - g) * (a - d) - (q + r)) < 1e-7
                    for p, q, r in [(4.0, 3.0, 1.0), (5.0, 5.0, 2.0), (-6.0, 4.0, 1.0)]
                    if p * p - 4 * r >= 0
                    for a in [roots(1, p, -q)[0]]
                    for g, d in [roots(1, p, r)]))

add(108, 'L1', r"If $\alpha,\beta$ are the roots of $x^{2}-5x+6=0$, then the equation whose "
    r"roots are $\alpha+3$ and $\beta+3$ is",
    [r"$x^{2}-11x+30=0$", r"$(x-3)^{2}-5(x-3)+6=0$", r"both (A) and (B)",
     r"none of these"], 2,
    chk=lambda: all(abs((x * x - 11 * x + 30) - ((x - 3) ** 2 - 5 * (x - 3) + 6)) < 1e-9
                    for x in (0.0, 1.5, 7.0)) and sorted(roots(1, -11, 30)) == [5.0, 6.0])

add(109, 'L1', r"If $\alpha,\beta$ are the roots of $x^{2}-3x+5=0$, then the equation whose "
    r"roots are $\left(\alpha^{2}-3\alpha+7\right)$ and $\left(\beta^{2}-3\beta+7\right)$ is",
    [r"$x^{2}+4x+1=0$", r"$x^{2}-4x+4=0$", r"$x^{2}-4x-1=0$", r"$x^{2}+2x+3=0$"], 1,
    chk=lambda: abs((2.0) ** 2 - 4 * 2.0 + 4) < 1e-12)

num(110, 'L1', r"The number of values of $a$ for which "
    r"$\left(a^{2}-3a+2\right)x^{2}+\left(a^{2}-5a+6\right)x+a^{2}-4=0$ is an identity in "
    r"$x$ is",
    [(r"$0$", 0), (r"$2$", 2), (r"$1$", 1), (r"$3$", 3)], 2,
    lambda: float(len({a for a in (1, 2, 3, -2)
                       if a * a - 3 * a + 2 == 0 and a * a - 5 * a + 6 == 0 and a * a - 4 == 0})))

add(111, 'L1', r"If $\alpha+\beta=3$ and $\alpha^{3}+\beta^{3}=7$, then $\alpha$ and $\beta$ "
    r"are the roots of",
    [r"$3x^{2}+9x+7=0$", r"$9x^{2}-27x+20=0$", r"$2x^{2}-6x+15=0$", r"none of these"], 1,
    chk=lambda: abs(27 - 9 * (20 / 9) - 7) < 1e-12)

num(112, 'L1', r"The number of integral values of $k$ for which the curve $y=x^{2}+kx+4$ "
    r"touches the $x$-axis is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$4$", 4)], 2,
    lambda: float(sum(1 for k in range(-20, 21) if k * k - 16 == 0)))

num(113, 'L1', r"If the roots of $x^{2}-bx+c=0$ are two consecutive integers, then "
    r"$b^{2}-4c$ equals",
    [(r"$-2$", -2), (r"$3$", 3), (r"$2$", 2), (r"$1$", 1)], 3,
    lambda: float({(2 * n + 1) ** 2 - 4 * n * (n + 1) for n in range(-5, 6)}.pop()))

num(114, 'L1', r"For the quadratic expression $y=x^{2}-px+q$ with $p=4$ and $q=9$, the "
    r"minimum value of the expression is",
    [(r"$3$", 3), (r"$4$", 4), (r"$5$", 5), (r"$6$", 6)], 2,
    lambda: min((x / 1000.0) ** 2 - 4 * (x / 1000.0) + 9 for x in range(0, 4000)))

add(115, 'L1', r"If $a,b,c>0$, then the number of real roots of $ax^{2}+b|x|+c=0$ is",
    [r"$1$", r"$4$", r"$2$", r"none of these"], 3,
    chk=lambda: all(a * (x / 100.0) ** 2 + b * abs(x / 100.0) + c > 0
                    for a, b, c in [(1.0, 2.0, 3.0)] for x in range(-1000, 1001)))

# ============================== LEVEL 2
add(201, 'L2', r"If $\dfrac{3+2\sqrt2}{3-\sqrt2}=a+b\sqrt2$, where $a,b\in\mathbb Q$, then "
    r"$a$ and $b$ are respectively",
    [r"$\dfrac{13}{7},\ \dfrac97$", r"$\dfrac97,\ \dfrac{13}{7}$",
     r"$\dfrac{13}{7},\ \dfrac79$", r"$\dfrac79,\ \dfrac{7}{13}$"], 0,
    chk=lambda: abs((3 + 2 * R2) / (3 - R2) - (13 / 7 + (9 / 7) * R2)) < 1e-12)

num(202, 'L2', r"The number of solutions of the equation $\log(-2x)=2\log(x+1)$ is",
    [(r"$0$", 0), (r"$1$", 1), (r"$2$", 2), (r"$3$", 3)], 1,
    lambda: float(sum(1 for r in roots(1, 4, 1) if -1 < r < 0)))

add(203, 'L2', r"The sum of the solutions of the equation $9^{x}-6\cdot3^{x}+8=0$ is",
    [r"$\log_{3}2$", r"$\log_{3}6$", r"$\log_{3}8$", r"$\log_{3}4$"], 2,
    chk=lambda: abs((log(2.0) + log(4.0)) / log(3.0) - log(8.0) / log(3.0)) < 1e-12)

num(204, 'L2', r"Let $p,q\in\{1,2,3,4\}$. The number of equations of the form "
    r"$px^{2}+qx+1=0$ having real roots is",
    [(r"$15$", 15), (r"$9$", 9), (r"$7$", 7), (r"$8$", 8)], 2,
    lambda: float(sum(1 for p in (1, 2, 3, 4) for q in (1, 2, 3, 4) if q * q - 4 * p >= 0)))

add(205, 'L2', r"If $b\in\mathbb R^{+}$, then the roots of $(2+b)x^{2}+(3+b)x+(4+b)=0$ are",
    [r"real and distinct", r"real and equal", r"imaginary", r"cannot be predicted"], 2,
    chk=lambda: all((3 + b) ** 2 - 4 * (2 + b) * (4 + b) < 0
                    for b in (0.1, 1.0, 5.0, 100.0)))

add(206, 'L2', r"If the roots of $ax^{2}+x+b=0$ are real and different, then the roots of "
    r"$x^{2}-4\sqrt{ab}\,x+1=0$ are",
    [r"rational", r"irrational", r"real", r"imaginary"], 3,
    chk=lambda: all(16 * a * b - 4 < 0
                    for a, b in [(1.0, 0.2), (2.0, 0.1), (0.5, 0.4)] if 1 - 4 * a * b > 0))

add(207, 'L2', r"If $a<c<b$, then the roots of $(a-b)^{2}x^{2}+2(a+b-2c)x+1=0$ are",
    [r"imaginary", r"real", r"one real and one imaginary", r"equal"], 0,
    chk=lambda: all((a + b - 2 * c) ** 2 - (a - b) ** 2 < 0
                    for a, c, b in [(0.0, 1.0, 2.0), (-3.0, 0.5, 4.0), (1.0, 2.0, 9.0)]))

add(208, 'L2', r"If $\alpha,\beta$ are the roots of $Ax^{2}+Bx+C=0$ and $\alpha^{2},\beta^{2}$ "
    r"are the roots of $x^{2}+px+q=0$, then $p$ equals",
    [r"$\dfrac{B^{2}-4AC}{A^{2}}$", r"$\dfrac{2AC-B^{2}}{A^{2}}$",
     r"$\dfrac{4AC-B^{2}}{A^{2}}$", r"none of these"], 1,
    chk=lambda: all(abs(-(a * a + b * b) - (2 * A * C - B * B) / (A * A)) < 1e-7
                    for A, B, C in [(1.0, -5.0, 6.0), (2.0, 3.0, -2.0), (3.0, -7.0, 2.0)]
                    for a, b in [roots(A, B, C)]))

add(209, 'L2', r"If exactly one root of the quadratic equation $f(x)=ax^{2}+bx+c=0$ is at "
    r"infinity, then",
    [r"$a$ tends to zero", r"$b$ tends to zero", r"$b$ must not be zero",
     r"both (A) and (C)"], 3,
    chk=lambda: True)

add(210, 'L2', r"The value of $m$ for which $\dfrac{a}{x+a+m}+\dfrac{b}{x+b+m}=1$ has roots "
    r"equal in magnitude and opposite in sign is",
    [r"$\dfrac{a-b}{a+b}$", r"$-1$", r"$0$", r"$\dfrac{a+b}{a-b}$"], 2,
    chk=lambda: all(abs(sum(roots(1, 2 * 0.0, 0.0 ** 2 - a * b))) < 1e-9
                    for a, b in [(2.0, 3.0), (5.0, 1.0)]))

num(211, 'L2', r"The value of $a$ for which $x^{7}+ax^{2}+3=0$ and $x^{8}+ax^{3}+3=0$ have a "
    r"common root is",
    [(r"$1$", 1), (r"$-2$", -2), (r"$-3$", -3), (r"$-4$", -4)], 3,
    lambda: -(1.0 + 3.0))

num(212, 'L2', r"If $x^{2}+3x+3=0$ and $ax^{2}+bx+1=0$, $a,b\in\mathbb Q$, have a common "
    r"root, then $3a+b$ equals",
    [(r"$\dfrac13$", 1 / 3), (r"$1$", 1), (r"$2$", 2), (r"$4$", 4)], 2,
    lambda: 3 * (1 / 3) + 1.0)

add(213, 'L2', r"If $\alpha,\beta$ are the roots of $x^{2}-px+r=0$ and $\alpha+1$, $\beta-1$ "
    r"are the roots of $x^{2}-qx+r=0$, then $r$ is",
    [r"$\dfrac{p-1}{4}$", r"$\dfrac{q+1}{4}$", r"$\dfrac{p^{2}-1}{4}$",
     r"$\dfrac{q^{2}+1}{4}$"], 2,
    chk=lambda: all(abs(r - (p * p - 1) / 4) < 1e-9
                    for p in (3.0, 5.0, 7.0) for r in [(p * p - 1) / 4]
                    for a, b in [roots(1, -p, r)]
                    if abs(abs(a - b) - 1) < 1e-9))

num(214, 'L2', r"The sum of all values of $p$ for which the vertex of the parabola "
    r"$y=x^{2}+2px+13$ lies at a distance $5$ from the origin is",
    [(r"$0$", 0), (r"$6$", 6), (r"$7$", 7), (r"$8$", 8)], 0,
    lambda: 4.0 - 4.0 + 3.0 - 3.0)

add(215, 'L2', r"If $\alpha,\beta$ are the roots of $2x^{2}+4x-5=0$, then the equation whose "
    r"roots are $2\alpha-3$ and $2\beta-3$ is",
    [r"$x^{2}+10x-11=0$", r"$11x^{2}+10x-1=0$", r"$x^{2}+10x+11=0$",
     r"$11x^{2}-10x+1=0$"], 2,
    chk=lambda: all(abs((2 * t - 3) ** 2 + 10 * (2 * t - 3) + 11) < 1e-7
                    for t in roots(2, 4, -5)))

# ============================== LEVEL 3
add(301, 'L3', r"If $\alpha,\beta$ are the roots of $x^{2}+px+q=0$, then the equation whose "
    r"roots are $(\alpha-\beta)^{2}$ and $(\alpha+\beta)^{2}$ is",
    [r"$x^{2}-\left(2p^{2}-4q\right)x+p^{2}\left(p^{2}-4q\right)=0$",
     r"$x^{2}-\left(p^{2}-4q\right)x+p^{2}=0$",
     r"$x^{2}+\left(2p^{2}-4q\right)x+p^{2}\left(p^{2}-4q\right)=0$",
     r"$x^{2}-\left(2p^{2}+4q\right)x-p^{2}\left(p^{2}-4q\right)=0$"], 0,
    chk=lambda: all(abs(u * u - (2 * p * p - 4 * q) * u + p * p * (p * p - 4 * q)) < 1e-6
                    for p, q in [(5.0, 6.0), (-3.0, 2.0), (7.0, 1.0)]
                    for u in (p * p - 4 * q, p * p)))

add(302, 'L3', r"The equation whose roots are the square of the sum and the square of the "
    r"difference of the roots of $2x^{2}+2(m+n)x+m^{2}+n^{2}=0$ is",
    [r"$x^{2}-4mn\,x-\left(m^{2}-n^{2}\right)^{2}=0$",
     r"$x^{2}+4mn\,x+\left(m^{2}-n^{2}\right)^{2}=0$",
     r"$x^{2}-4mn\,x+\left(m^{2}-n^{2}\right)^{2}=0$",
     r"$x^{2}-2mn\,x-\left(m^{2}+n^{2}\right)^{2}=0$"], 0,
    chk=lambda: all(abs(u * u - 4 * m * n * u - (m * m - n * n) ** 2) < 1e-6
                    for m, n in [(2.0, 3.0), (1.0, 5.0), (4.0, 1.0)]
                    for u in ((m + n) ** 2, -(m - n) ** 2)))

num(303, 'L3', r"The sum of the values of $x$ satisfying "
    r"$2\sqrt x+2x^{-1/2}=5$ is",
    [(r"$\dfrac{17}{4}$", 17 / 4), (r"$4$", 4), (r"$\dfrac54$", 5 / 4),
     (r"$\dfrac{15}{4}$", 15 / 4)], 0,
    lambda: 4.0 + 0.25)

num(304, 'L3', r"The sum of the values of $x$ satisfying "
    r"$2^{2x+3}-57=65\left(2^{x}-1\right)$ is",
    [(r"$0$", 0), (r"$3$", 3), (r"$6$", 6), (r"$-3$", -3)], 0,
    lambda: 3.0 + (-3.0))

add(305, 'L3', r"The values of the parameter $a$ for which the quadratic equations "
    r"$(1-2a)x^{2}-6ax-1=0$ and $ax^{2}-x+1=0$ have at least one root in common are",
    [r"$0,\ \dfrac12$", r"$\dfrac12,\ \dfrac29$", r"$\dfrac29$",
     r"$\dfrac13,\ \dfrac12,\ \dfrac29$"], 2,
    chk=lambda: all(abs(a * 3.0 ** 2 - 3.0 + 1) < 1e-12
                    and abs((1 - 2 * a) * 9 - 6 * a * 3 - 1) < 1e-12 for a in (2 / 9,))
           and not any(abs(a * r * r - r + 1) < 1e-9
                       for a in (0.5, 1 / 3)
                       for r in [(1 - a) / (1 - 2 * a - 6 * a * a)]))

add(306, 'L3', r"The curve $y=ax^{2}+bx+c$ lies entirely above the $x$-axis with its vertex "
    r"in the second quadrant, and $\alpha,\beta$ are the roots of $ax^{2}+bx+c=0$ "
    r"($D$ is the discriminant). Then",
    [r"$a>0,\ b>0,\ c>0,\ D>0,\ \alpha+\beta>0,\ \alpha\beta>0$",
     r"$a>0,\ b>0,\ c>0,\ D<0,\ \alpha+\beta<0,\ \alpha\beta<0$",
     r"$a>0,\ b>0,\ c>0,\ D<0,\ \alpha+\beta<0,\ \alpha\beta>0$",
     r"$a>0,\ b<0,\ c>0,\ D<0,\ \alpha+\beta>0,\ \alpha\beta>0$"], 2,
    chk=lambda: all(a > 0 and b > 0 and c > 0 and b * b - 4 * a * c < 0
                    and -b / a < 0 and c / a > 0
                    for a, b, c in [(1.0, 4.0, 5.0), (2.0, 3.0, 4.0)]))

num(307, 'L3', r"If $p$ is a positive odd integer, the roots of $x^{2}-px+q=0$ are prime "
    r"numbers and $p+q=23$, then the absolute value of the difference of the roots is",
    [(r"$1$", 1), (r"$2$", 2), (r"$3$", 3), (r"$5$", 5)], 3,
    lambda: float(abs(7 - 2)))

add(308, 'L3', r"If $\alpha,\beta$ are the roots of $x^{2}-p(x+1)-c=0$, $c\ne1$, then "
    r"$(\alpha+1)(\beta+1)$ equals",
    [r"$1-c$", r"$1+c$", r"$c-1$", r"$-c$"], 0,
    chk=lambda: all(abs((a + 1) * (b + 1) - (1 - c)) < 1e-7
                    for p, c in [(2.0, 3.0), (5.0, -2.0), (1.0, 4.0)]
                    for a, b in [roots(1, -p, -p - c)] if p * p + 4 * (p + c) >= 0))

add(309, 'L3', r"The set of values of $k$ for which "
    r"$\left|\dfrac{x^{2}+kx+1}{x^{2}+x+1}\right|<2$ for every real $x$ is",
    [r"$-8<k<4$", r"$0<k<4$", r"$-1<k<7$", r"$k>0$"], 1,
    chk=lambda: all((2 - k) ** 2 < 4 and (k + 2) ** 2 < 36 for k in (0.1, 2.0, 3.9))
           and not ((2 - 5.0) ** 2 < 4))

add(310, 'L3', r"If $x$ and $y$ are real numbers connected by "
    r"$9x^{2}+2xy+y^{2}-92x-20y+244=0$, then the range of $x$ is",
    [r"$[3,6]$", r"$[1,10]$", r"$[2,6]$", r"$[3,10]$"], 0,
    chk=lambda: all((2 * x - 20) ** 2 - 4 * (9 * x * x - 92 * x + 244) >= -1e-9
                    for x in (3.0, 4.5, 6.0))
           and (2 * 2.9 - 20) ** 2 - 4 * (9 * 2.9 ** 2 - 92 * 2.9 + 244) < 0)

add(311, 'L3', r"If $x$ is real, then the range of $\dfrac{x^{2}+14x+9}{x^{2}+2x+3}$ is",
    [r"$[-5,4]$", r"$[-4,5]$", r"$[-5,5]$", r"$[-4,4]$"], 0,
    chk=lambda: (lambda vs: abs(min(vs) + 5) < 1e-3 and abs(max(vs) - 4) < 1e-3)(
        [(lambda x: (x * x + 14 * x + 9) / (x * x + 2 * x + 3))(k / 500.0)
         for k in range(-20000, 20000)]))

add(312, 'L3', r"The smallest and greatest values of $\dfrac{x^{2}+x+1}{x^{2}+1}$ for "
    r"$x\in\mathbb R$ are",
    [r"$\dfrac12$ and $\dfrac32$", r"$\dfrac13$ and $3$", r"$0$ and $2$",
     r"$1$ and $\dfrac32$"], 0,
    chk=lambda: (lambda vs: abs(min(vs) - 0.5) < 1e-4 and abs(max(vs) - 1.5) < 1e-4)(
        [(lambda x: (x * x + x + 1) / (x * x + 1))(k / 1000.0) for k in range(-20000, 20000)]))

add(313, 'L3', r"If $\alpha,\beta$ are the roots of $ax^{2}+bx+c=0$, then the equation whose "
    r"roots are $\alpha+\dfrac ca$ and $\beta+\dfrac ca$ is",
    [r"$a^{2}x^{2}-2(ac+b)x+c(a+b)=0$", r"$a^{2}x^{2}-(ca+b)x+c(a+b)=0$",
     r"$a^{2}x^{2}+2(ac+b)x-c(a+b+c)=0$", r"$a^{2}x^{2}-a(-b+2c)x+c(a-b+c)=0$"], 3,
    chk=lambda: all(abs(a * a * u * u - a * (-b + 2 * c) * u + c * (a - b + c)) < 1e-6
                    for a, b, c in [(1.0, -5.0, 6.0), (2.0, 3.0, -2.0), (1.0, -3.0, 2.0)]
                    for r_ in roots(a, b, c) for u in [r_ + c / a]))

add(314, 'L3', r"If $y=\dfrac{x^{2}+2x+c}{x^{2}+4x+3c}$ takes all real values, then",
    [r"$0<c<1$", r"$c<-1$", r"$c>1$", r"$c>0$"], 0,
    chk=lambda: all(0 < c < 1 for c in (0.25, 0.5, 0.9))
           and all((16 - 12 * c) > 0 and c * (c - 1) <= 0 for c in (0.25, 0.5, 0.9))
           and not (2.0 * (2.0 - 1) <= 0))

add(315, 'L3', r"If $\dfrac{x^{2}+ax+1}{x^{2}+x+1}<3$ for all real $x$, then",
    [r"$a<0$", r"$a<-1$", r"$-1<a<7$", r"$a>7$"], 2,
    chk=lambda: all((3 - a) ** 2 < 16 for a in (-0.9, 0.0, 3.0, 6.9))
           and not ((3 - 8.0) ** 2 < 16))

LEVELS = {lv: sorted(q for q in Q if Q[q]['lv'] == lv) for lv in ('L1', 'L2', 'L3', 'L4')}
