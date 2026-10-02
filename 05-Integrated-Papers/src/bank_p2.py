# -*- coding: utf-8 -*-
"""Integrated Paper II (JEE Advanced pattern) -- PRAGYA G8 Achievers.
Retyped from Hell_Paper_II_ADVANCED.pdf (27 Sep 2026); 'Hell' tag removed.
Sections: I integer (0-9), II one-or-more correct, III single correct.
Keys re-derived in verify_p2.py (brute force from the statement) and
verify2_p2.py (exact arithmetic along the hand method)."""
from bank import SU, LO, SS, QE

Q = []


def intq(q, val, ch, concept, level, work, fix=""):
    Q.append(dict(sec='I', q=q, o=None, ans=val, val=val, ch=ch, concept=concept,
                  level=level, work=work, fix=fix))


def multi(q, opts, ans, ch, concept, level, work, fix=""):
    """ans: set of correct indices"""
    Q.append(dict(sec='II', q=q, o=opts, ans=sorted(ans), val=None, ch=ch,
                  concept=concept, level=level, work=work, fix=fix))


def single(q, opts, ans, val, ov, ch, concept, level, work, fix=""):
    Q.append(dict(sec='III', q=q, o=opts, ov=ov, ans=ans, val=val, ch=ch,
                  concept=concept, level=level, work=work, fix=fix))


# ------------------------------------------------------------ SECTION I
intq(r"Let $u=\sqrt[3]{7+5\sqrt2}$ and $v=\sqrt[3]{7-5\sqrt2}$. If $u+v$ and $uv$ are the roots "
     r"of ${x^2+px+q=0}$, and $p,\,q,\,r$ are in geometric progression, then $|r|$ is",
     4, [SU, QE, SS], "Cube root of $a+b\\sqrt2$ as a binomial surd", "M",
     r"$7\pm5\sqrt2=(1\pm\sqrt2)^3\Rightarrow u+v=2,\ uv=-1$; roots $2,-1\Rightarrow p=-1,\ q=-2$; "
     r"$r=q^2/p=-4$, $|r|=4$")

intq(r"Let $a,b,c$ be in arithmetic progression, $b,c,d$ in geometric progression and $c,d,e$ in "
     r"harmonic progression, where $a=1$, $e=25$ and all of $a,b,c,d,e$ are positive. Then $c$ is",
     5, [SS], "AP--GP--HP chain $\\Rightarrow c^2=ae$", "D",
     r"$b=\tfrac{a+c}{2}$, $d=\tfrac{c^2}{b}=\tfrac{2ce}{c+e}\Rightarrow c(c+e)=(a+c)e\Rightarrow c^2=ae=25$, $c=5$")

intq(r"Let $x=\sqrt{12+\sqrt{12+\sqrt{12+\cdots\infty}}}$ and "
     r"$y=\sqrt{72+\sqrt{72+\sqrt{72+\cdots\infty}}}$. If $x,\,g,\,y$ are in geometric progression "
     r"with $g>0$, then $\log_g(xy)$ is",
     2, [SU, QE, SS, LO], "Infinite nested radical $\\Rightarrow$ quadratic", "E",
     r"$x^2=x+12\Rightarrow x=4$; $y^2=y+72\Rightarrow y=9$; $g=6$; $\log_6 36=2$")

intq(r"Given $\log_{10}2=0.3010$ and $\log_{10}3=0.4771$, let $d$ be the number of digits in "
     r"$\left(\sqrt6\right)^{20}$ and let $z$ be the number of zeros after the decimal point and "
     r"before the first significant digit of $\left(\sqrt6\right)^{-20}$. Then $d-z$ is",
     1, [LO, SU], "Characteristic; digits and leading zeros", "M",
     r"$\log 6^{10}=7.781\Rightarrow d=8$; $\log 6^{-10}=\overline{8}.219\Rightarrow z=7$; $d-z=1$")

intq(r"Let $\alpha>\beta$ be the roots of $x^2-x\sqrt{9+4\sqrt5}+\sqrt5=0$. If $\alpha-\beta$ is the "
     r"second term of a geometric progression whose first term is $\dfrac13$, then its positive "
     r"common ratio is",
     9, [QE, SU, SS], "$(\\alpha-\\beta)^2=(\\alpha+\\beta)^2-4\\alpha\\beta$", "M",
     r"$(\alpha-\beta)^2=9+4\sqrt5-4\sqrt5=9\Rightarrow\alpha-\beta=3$; $\tfrac13r=3\Rightarrow r=9$")

intq(r"Let $x_1<x_2$ be the real values satisfying $\left(\log_5 x\right)^2-\log_5\!\left(x^3\right)+2=0$. "
     r"If $x_1,\ x_2,\ y$ are in geometric progression, then $\log_5 y+4$ is",
     7, [LO, QE, SS], "Quadratic in $\\log_5 x$", "E",
     r"$t^2-3t+2=0\Rightarrow x=5,25$; $y=25^2/5=125$; $3+4=7$")

intq(r"Let $a_1,a_2,\ldots,a_7$ be in geometric progression with $a_1=\sqrt2$, $a_7=8\sqrt2$ and "
     r"positive common ratio. If $a_4$ is a root of ${x^2-kx+8=0}$ whose other root is also a term "
     r"of this progression, then $k$ is",
     6, [SS, SU, QE], "GP terms; product of roots", "E",
     r"$r^6=8\Rightarrow r=\sqrt2$, $a_4=4$; other root $8/4=2=a_2$; $k=6$")

intq(r"Let $T$ be the sum of all real values of $x$ satisfying "
     r"$\left(x^2-7x+11\right)^{x^2-13x+42}=1$. If $T$ is the third term of a geometric progression "
     r"whose first term is $3$ and whose common ratio $r$ is positive, then $\log_r T$ is",
     3, [QE, SS, LO], "$f^{g}=1$: base $1$ / index $0$ / base $-1$ with even index", "M",
     r"base $1$: $x=2,5$; index $0$: $x=6,7$; base $-1$: $x=3,4$ (index $12,6$ even); "
     r"$T=27$; $3r^2=27\Rightarrow r=3$; $\log_3 27=3$")

# ------------------------------------------------------------ SECTION II
multi(r"Let $a=\sqrt{8+2\sqrt{15}}$ and $b=\sqrt{8-2\sqrt{15}}$. Then",
      [r"$a+b=2\sqrt5$", r"$ab=2$",
       r"$a$ and $b$ are the roots of $x^2-2\sqrt5\,x+2=0$",
       r"$a,\ 2,\ b$ are in arithmetic progression"], {0, 1, 2},
      [SU, QE, SS], "Denesting; sum/product; AP test", "E",
      r"$a=\sqrt5+\sqrt3$, $b=\sqrt5-\sqrt3$; $a+b=2\sqrt5$, $ab=2$; AP needs $a+b=4$ -- false")

multi(r"An infinite geometric progression has sum $5$ and the sum of the squares of its terms is "
      r"$15$. Then",
      [r"its common ratio is $\dfrac14$", r"its first term is $\dfrac{15}{4}$",
       r"the sum of the cubes of its terms is $\dfrac{375}{13}$",
       r"its third term is $\dfrac{15}{64}$"], {0, 1, 3},
      [SS], "Infinite GP of squares and cubes", "M",
      r"$\tfrac{1+r}{1-r}=\tfrac{25}{15}\Rightarrow r=\tfrac14$, $a=\tfrac{15}{4}$; "
      r"cubes: $\tfrac{a^3}{1-r^3}=\tfrac{375}{7}\neq\tfrac{375}{13}$; $ar^2=\tfrac{15}{64}$")

multi(r"Let $x_1>x_2$ be the real numbers satisfying $\left(\log_3 x\right)^2-4\log_3 x+3=0$. Then",
      [r"$\log_3 x_1+\log_3 x_2=3$", r"$x_1x_2=81$",
       r"$x_1,\ 9,\ x_2$ are in geometric progression", r"$x_1-x_2=24$"], {1, 2, 3},
      [LO, QE, SS], "Quadratic in $\\log_3 x$", "E",
      r"$t=1,3\Rightarrow x=3,27$; $\log$ sum $=4$ (A false); $x_1x_2=81=9^2$; $27-3=24$")

multi(r"Let $p=\sqrt{14+6\sqrt5}$ and $q=\sqrt{14-6\sqrt5}$. Then",
      [r"$p+q=6$", r"$pq=2$", r"$p,\ 2,\ q$ are in geometric progression",
       r"$p$ and $q$ are the roots of $x^2-6x+4=0$"], {0, 2, 3},
      [SU, QE, SS], "Denesting; sum/product; GP test", "E",
      r"$p=3+\sqrt5$, $q=3-\sqrt5$; $p+q=6$, $pq=4$ (B false); $2^2=pq$; $x^2-6x+4=0$")

multi(r"Let $\alpha>\beta$ be the roots of $x^2-6x+7=0$. Then",
      [r"$\alpha-\beta=2\sqrt2$", r"$\alpha\beta=7$",
       r"$\alpha+\beta,\ \alpha\beta,\ \alpha-\beta$ are in arithmetic progression",
       r"$\log_\alpha\beta=-1$"], {0, 1},
      [QE, SU, SS, LO], "Roots $3\\pm\\sqrt2$; AP and log tests", "E",
      r"$\alpha,\beta=3\pm\sqrt2$; $\alpha-\beta=2\sqrt2$, $\alpha\beta=7$; "
      r"$14\neq6+2\sqrt2$; $\log_\alpha\beta=-1\iff\alpha\beta=1$ -- false")

multi(r"Let $a,b,c$ be distinct positive reals, none equal to $1$, in geometric progression, and let "
      r"$N>0$, $N\neq1$. Then",
      [r"$\log_a N,\ \log_b N,\ \log_c N$ are in harmonic progression",
       r"$a,\ b,\ c$ are in arithmetic progression",
       r"$a^2,\ b^2,\ c^2$ are in geometric progression",
       r"$\log_a N,\ \log_b N,\ \log_c N$ are in arithmetic progression"], {0, 2},
      [LO, SS], "$\\log_N a,\\log_N b,\\log_N c$ in AP $\\Rightarrow$ reciprocals in HP", "M",
      r"$b^2=ac\Rightarrow\log_N a,\log_N b,\log_N c$ in AP, so $\log_a N,\dots$ in HP; "
      r"$(b^2)^2=a^2c^2$; distinct terms cannot be in AP and HP together, nor a GP in AP",
      fix="``distinct'' added")

# ------------------------------------------------------------ SECTION III
from math import sqrt
single(r"Let $a,b>0$ with $a\neq1$, $b\neq1$. If the equations \[x^2+(\log_a b)\,x+\log_b a=0\quad\text{and}\quad "
       r"x^2+(\log_b a)\,x+\log_a b=0\] have both roots common and real, and $\alpha>\beta$ are those "
       r"common roots, then $(\alpha-\beta)+ab$ equals",
       [r"$2$", r"$\sqrt5-1$", r"$2\sqrt5$", r"$\sqrt5+1$"], 3, sqrt(5) + 1,
       [2, sqrt(5) - 1, 2 * sqrt(5), sqrt(5) + 1],
       [LO, QE, SU], "Identical equations $\\Rightarrow\\log_a b=\\log_b a=\\pm1$", "D",
       r"$t=1/t\Rightarrow t=\pm1$; $t=1$: $x^2+x+1$ (not real); $t=-1$: $b=1/a$, "
       r"$x^2-x-1=0$, $\alpha-\beta=\sqrt5$, $ab=1$")

single(r"Let $a,b,c$ be in harmonic progression with $a=7+4\sqrt3$ and $c=7-4\sqrt3$. If $b$, $k$ "
       r"and $\log_{(2+\sqrt3)}a$ are in arithmetic progression, then $k$ equals",
       [r"$\dfrac{15}{14}$", r"$\dfrac97$", r"$\dfrac{13}{14}$", r"$\dfrac87$"], 0, 15 / 14,
       [15 / 14, 9 / 7, 13 / 14, 8 / 7],
       [SS, SU, LO], "HM of conjugate surds; $7+4\\sqrt3=(2+\\sqrt3)^2$", "M",
       r"$b=\tfrac{2ac}{a+c}=\tfrac{2}{14}=\tfrac17$; $\log_{2+\sqrt3}(2+\sqrt3)^2=2$; "
       r"$k=\tfrac12\!\left(\tfrac17+2\right)=\tfrac{15}{14}$")

single(r"The harmonic mean of the roots of $x^2-\left(\sqrt5+\sqrt3\right)x+\sqrt{15}=0$ is",
       [r"$\sqrt{15}$", r"$5\sqrt3-3\sqrt5$", r"$\dfrac{\sqrt5+\sqrt3}{2}$", r"$3\sqrt5-5\sqrt3$"],
       1, 5 * sqrt(3) - 3 * sqrt(5),
       [sqrt(15), 5 * sqrt(3) - 3 * sqrt(5), (sqrt(5) + sqrt(3)) / 2, 3 * sqrt(5) - 5 * sqrt(3)],
       [QE, SU, SS], "HM $=2\\alpha\\beta/(\\alpha+\\beta)$; rationalising", "E",
       r"roots $\sqrt5,\sqrt3$; $\tfrac{2\sqrt{15}}{\sqrt5+\sqrt3}=\sqrt{15}(\sqrt5-\sqrt3)=5\sqrt3-3\sqrt5$")

single(r"Let $x_1>x_2$ be the real numbers satisfying $\left(\log_2 x\right)^2=\log_2\!\left(x^2\right)+8$. "
       r"If $x_1,\ g,\ x_2$ are in geometric progression with $g>0$, then $g$ equals",
       [r"$1$", r"$8$", r"$2$", r"$4$"], 2, 2, [1, 8, 2, 4],
       [LO, QE, SS], "Quadratic in $\\log_2 x$; GM", "E",
       r"$t^2-2t-8=0\Rightarrow t=4,-2\Rightarrow x=16,\tfrac14$; $g=\sqrt{4}=2$")

assert len(Q) == 18
