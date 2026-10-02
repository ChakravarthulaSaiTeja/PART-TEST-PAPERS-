# -*- coding: utf-8 -*-
"""Integrated Paper I (JEE Main pattern) -- PRAGYA G8 Achievers.
Retyped from Hell_Paper_I_MAIN.pdf (27 Sep 2026); 'Hell' tag removed.
Every question's key is re-derived in verify.py (brute force straight from the
statement) and verify2.py (exact arithmetic along the hand method)."""
from math import sqrt

SU, LO, SS, QE = 'Surds', 'Logarithms', r'Seq.\ \& Series', 'Quadratic Eqns'

Q = []          # in paper order


def mcq(q, opts, ans, val, ch, concept, level, work, fix=""):
    """opts: [(latex, numeric value)]; ans: keyed index; val: true value."""
    assert len(opts) == 4 and 0 <= ans <= 3
    Q.append(dict(sec='A', q=q, o=[o[0] for o in opts], ov=[o[1] for o in opts],
                  ans=ans, val=val, ch=ch, concept=concept, level=level,
                  work=work, fix=fix))


def nva(q, val, ch, concept, level, work, fix=""):
    Q.append(dict(sec='B', q=q, o=None, ov=None, ans=None, val=val, ch=ch,
                  concept=concept, level=level, work=work, fix=fix))


R2, R6 = sqrt(2), sqrt(6)

# ------------------------------------------------------------- SECTION A
mcq(r"Let \[s=\sqrt{3-2\sqrt2}+\sqrt{5-2\sqrt6}+\sqrt{7-4\sqrt3}+\sqrt{9-4\sqrt5}"
    r"+\sqrt{11-2\sqrt{30}}.\] If $s$ is a root of ${x^2+px+q=0}$ where $p,q\in\mathbb{Z}$, "
    r"and $p,\,q,\,r$ are in arithmetic progression, then $r$ equals",
    [(r"$-7$", -7), (r"$-12$", -12), (r"$-3$", -3), (r"$12$", 12)], 1, -12,
    [SU, QE, SS], "Denesting $\\sqrt{a-2\\sqrt b}$; conjugate root; AP", "M",
    r"$s=\sqrt6-1\Rightarrow x^2+2x-5=0\Rightarrow p=2,\ q=-5,\ r=2q-p=-12$")

mcq(r"Let $S$ be the sum of all real values of $x$ satisfying "
    r"$\left(x^2-5x+5\right)^{x^2-9x+20}=1$. If $S$ is the $n$th term of the arithmetic "
    r"progression $3,7,11,\ldots$, then $\log_2(S+1)+n$ equals",
    [(r"$6$", 6), (r"$9$", 9), (r"$7$", 7), (r"$8$", 8)], 3, 8,
    [QE, SS, LO], "$f^{g}=1$: base $1$ / index $0$ / base $-1$ with even index", "M",
    r"base $1$: $x=1,4$; index $0$: $x=4,5$; base $-1$: $x=2,3$ (index $6,2$ even). "
    r"$S=15=a_4\Rightarrow\log_2 16+4=8$")

mcq(r"Let $x_1>x_2$ be the real numbers satisfying "
    r"$\log_{(\sqrt3+\sqrt2)}x\cdot\log_{(\sqrt3-\sqrt2)}x=-4$. "
    r"Then $x_1+x_2+\sqrt{x_1x_2}$ equals",
    [(r"$9$", 9), (r"$12$", 12), (r"$10$", 10), (r"$11$", 11)], 3, 11,
    [LO, SU, QE], "Reciprocal bases: $\\log_{1/a}x=-\\log_a x$", "M",
    r"$t=\log_{\sqrt3+\sqrt2}x\Rightarrow -t^2=-4,\ t=\pm2$; $x=5\pm2\sqrt6$; "
    r"$10+1=11$")

mcq(r"Let $N$ be the number of reals $x>0$, $x\neq1$, satisfying "
    r"$\log_{(\sqrt5+2)}x+\log_{(\sqrt5-2)}x=4$. If $N$ is the first term of an "
    r"arithmetic progression whose fifth term is $12$, then its common difference is",
    [(r"$12$", 12), (r"$4$", 4), (r"$3$", 3), (r"$2$", 2)], 2, 3,
    [LO, SU, SS], "Reciprocal bases give LHS $\\equiv0$; $N=0$", "M",
    r"$\sqrt5-2=(\sqrt5+2)^{-1}\Rightarrow$ LHS $=t-t=0\neq4$, so $N=0$; "
    r"$0+4d=12\Rightarrow d=3$")

mcq(r"If $\log_2 x$, $\log_2(x+2)$ and $\log_2(3x+2)$ are in arithmetic progression, and "
    r"$x$ is the fourth term of a geometric progression whose first term is $\dfrac14$, "
    r"then its common ratio is",
    [(r"$\dfrac12$", 0.5), (r"$4$", 4), (r"$\sqrt2$", R2), (r"$2$", 2)], 3, 2,
    [LO, QE, SS], "Logs in AP $\\Rightarrow$ arguments in GP; domain check", "E",
    r"$(x+2)^2=x(3x+2)\Rightarrow x^2-x-2=0\Rightarrow x=2$ ($x=-1$ rejected); "
    r"$\tfrac14r^3=2\Rightarrow r=2$")

mcq(r"Let $S$ be the sum to infinity of the geometric progression "
    r"$2,\ \sqrt2,\ 1,\ \dfrac{1}{\sqrt2},\ \ldots$. If $S$ is a root of ${x^2+px+q=0}$ "
    r"where $p,q\in\mathbb{Z}$, then $p+q$ equals",
    [(r"$-16$", -16), (r"$8$", 8), (r"$0$", 0), (r"$-8$", -8)], 2, 0,
    [SS, SU, QE], "Infinite GP; rationalising; conjugate root", "M",
    r"$S=\dfrac{2}{1-1/\sqrt2}=4+2\sqrt2\Rightarrow x^2-8x+8=0\Rightarrow p+q=0$")

mcq(r"Let $P$ be the product of all real values of $x$ satisfying "
    r"$x^{\log_{10}x}=100x^2$. If $\log_{10}P$, $k$ and $8$ are in arithmetic progression, "
    r"then $k$ equals",
    [(r"$6$", 6), (r"$\dfrac{11}{2}$", 5.5), (r"$4$", 4), (r"$5$", 5)], 3, 5,
    [LO, QE, SS], "Take logs; product of roots via sum of $\\log$ roots", "M",
    r"$t=\log x$: $t^2-2t-2=0$, $t_1+t_2=2\Rightarrow P=10^2$; $2,k,8$ in AP $\Rightarrow k=5$")

mcq(r"Let $\alpha>\beta$ be the roots of $x^2-2x-1=0$. If $\alpha^3-\beta^3$, "
    r"$20\sqrt2$ and $k$ are in arithmetic progression, then $k$ equals",
    [(r"$24\sqrt2$", 24 * R2), (r"$32\sqrt2$", 32 * R2), (r"$28\sqrt2$", 28 * R2),
     (r"$30\sqrt2$", 30 * R2)], 3, 30 * R2,
    [QE, SU, SS], "$\\alpha^3-\\beta^3=(\\alpha-\\beta)(\\alpha^2+\\alpha\\beta+\\beta^2)$", "E",
    r"$\alpha-\beta=2\sqrt2$, $\alpha^2+\alpha\beta+\beta^2=4+1=5\Rightarrow10\sqrt2$; "
    r"$k=40\sqrt2-10\sqrt2=30\sqrt2$")

mcq(r"Suppose $(\log_2 x)^2-(k+2)\log_2 x+(2k+1)=0$ has both of its roots (as values of "
    r"$\log_2 x$) integers, not necessarily distinct. The two admissible values of $k$, in "
    r"increasing order, are the first and third terms of an arithmetic progression. "
    r"Its second term is",
    [(r"$4$", 4), (r"$1$", 1), (r"$2$", 2), (r"$0$", 0)], 2, 2,
    [LO, QE, SS], "Integer roots: eliminate $k$, factorise", "D",
    r"$t_1t_2=2(t_1+t_2)-3\Rightarrow(t_1-2)(t_2-2)=1\Rightarrow t_1=t_2=3$ or $1$; "
    r"$k=4$ or $0$; middle term $2$")

mcq(r"Three distinct non-zero reals $a,b,c$ are in geometric progression and "
    r"$a,\,2b,\,3c$ are in arithmetic progression. If $a=\sqrt2$, then the sum to infinity "
    r"of the geometric progression $a,b,c,\ldots$ is",
    [(r"$\dfrac{3\sqrt2}{2}$", 1.5 * R2), (r"$\dfrac{\sqrt2}{2}$", R2 / 2),
     (r"$\dfrac{2\sqrt2}{3}$", 2 * R2 / 3), (r"$3\sqrt2$", 3 * R2)], 0, 1.5 * R2,
    [SS, QE, SU], "GP ratio from AP condition; distinctness rejects $r=1$", "M",
    r"$4ar=a+3ar^2\Rightarrow3r^2-4r+1=0\Rightarrow r=\tfrac13$; "
    r"$S_\infty=\sqrt2\big/\tfrac23=\tfrac{3\sqrt2}{2}$",
    fix="Wording: ``the geometric progression'' now names it as $a,b,c,\\ldots$")

mcq(r"Let $x_1$ and $x_2$ be the roots of $\log_3 x+\log_x 3=\dfrac52$. If "
    r"$\log_3(x_1x_2)$, $k$ and $10$ are in arithmetic progression, then $k$ equals",
    [(r"$\dfrac{21}{4}$", 5.25), (r"$\dfrac{25}{4}$", 6.25), (r"$\dfrac{27}{4}$", 6.75),
     (r"$\dfrac{23}{4}$", 5.75)], 1, 6.25,
    [LO, QE, SS], "$t+1/t=5/2$; base-change reciprocal", "E",
    r"$t=2,\tfrac12\Rightarrow x=9,\sqrt3$; $\log_3(9\sqrt3)=\tfrac52$; "
    r"$k=\tfrac12\!\left(\tfrac52+10\right)=\tfrac{25}{4}$")

mcq(r"Let $A=\sqrt{2+\sqrt{2+\sqrt{2+\cdots\infty}}}$ and "
    r"$B=\sqrt{6+\sqrt{6+\sqrt{6+\cdots\infty}}}$. If $A,\,G,\,B$ are in geometric "
    r"progression with $G>0$, then $\log_2\!\left(A+B+G^2-3\right)$ equals",
    [(r"$4$", 4), (r"$3$", 3), (r"$2$", 2), (r"$\log_2 11$", 3.4594316186372973)], 1, 3,
    [SU, QE, SS, LO], "Infinite nested radical $\\Rightarrow$ quadratic", "E",
    r"$A^2=A+2\Rightarrow A=2$; $B^2=B+6\Rightarrow B=3$; $G^2=6$; $\log_2 8=3$")

mcq(r"Let $\alpha=\sqrt{19+6\sqrt2}$ and $\beta=\sqrt{19-6\sqrt2}$. If $\alpha-\beta$, "
    r"$4$ and $k$ are in geometric progression, then $k$ equals",
    [(r"$8$", 8), (r"$12$", 12), (r"$6$", 6), (r"$10$", 10)], 0, 8,
    [SU, SS], "Denesting $\\sqrt{a\\pm b\\sqrt c}$", "M",
    r"$19\pm6\sqrt2=(3\sqrt2\pm1)^2\Rightarrow\alpha-\beta=2$; $k=16/2=8$")

mcq(r"Let $N$ be the number of real solutions of $2\log_3 x-\log_3(x+6)=1$ and let "
    r"$x_0$ be their sum. Then $N+x_0$ equals",
    [(r"$7$", 7), (r"$9$", 9), (r"$5$", 5), (r"$6$", 6)], 0, 7,
    [LO, QE], "Log equation with domain rejection", "E",
    r"$x^2=3(x+6)\Rightarrow(x-6)(x+3)=0$; $x>0\Rightarrow x=6$; $N+x_0=1+6=7$")

mcq(r"Three reals $a<b<c$ are in arithmetic progression with $a+b+c=15$ and "
    r"$a^2+b^2+c^2=83$. If $a,\,g,\,c$ are in geometric progression with $g>0$, "
    r"then $g$ equals",
    [(r"$\sqrt{35}$", sqrt(35)), (r"$\sqrt{21}$", sqrt(21)), (r"$\sqrt{15}$", sqrt(15)),
     (r"$5$", 5)], 1, sqrt(21),
    [SS, SU], "AP as $b-d,b,b+d$; GM of extremes", "E",
    r"$b=5$, $75+2d^2=83\Rightarrow d=2$; $a,c=3,7$; $g=\sqrt{21}$")

mcq(r"The number of integral values of $x$ satisfying "
    r"$\sqrt{x+3-4\sqrt{x-1}}+\sqrt{x+8-6\sqrt{x-1}}=1$ is the third term of a geometric "
    r"progression whose first term is $\dfrac23$. Its positive common ratio is",
    [(r"$\dfrac32$", 1.5), (r"$\sqrt6$", R6), (r"$3$", 3), (r"$2$", 2)], 2, 3,
    [SU, SS], "Perfect squares under root $\\Rightarrow|u-2|+|u-3|=1$", "D",
    r"$u=\sqrt{x-1}$: $|u-2|+|u-3|=1\Rightarrow2\le u\le3\Rightarrow5\le x\le10$, "
    r"$6$ integers; $\tfrac23r^2=6\Rightarrow r=3$")

mcq(r"Let the sum of all real solutions of $4^x-3\cdot2^{x+1}+8=0$ be the second term of "
    r"an arithmetic progression whose first term is $1$. Its fifth term is",
    [(r"$11$", 11), (r"$9$", 9), (r"$13$", 13), (r"$7$", 7)], 1, 9,
    [QE, SS], "Quadratic in $2^x$", "E",
    r"$y=2^x$: $y^2-6y+8=0\Rightarrow y=2,4\Rightarrow x=1,2$; sum $3\Rightarrow d=2$; "
    r"$T_5=1+8=9$")

mcq(r"Let $G$ and $H$ be the geometric mean and the harmonic mean of $3+2\sqrt2$ and "
    r"$3-2\sqrt2$. If $\dfrac{G}{H},\ k,\ 27$ are in geometric progression with $k>0$, "
    r"then $\log_3 k$ equals",
    [(r"$2$", 2), (r"$\dfrac32$", 1.5), (r"$3$", 3), (r"$1$", 1)], 0, 2,
    [SU, SS, LO], "GM, HM of conjugate surds", "M",
    r"product $1\Rightarrow G=1$; $H=\tfrac{2\cdot1}{6}=\tfrac13$; $G/H=3$; "
    r"$k^2=81\Rightarrow k=9$; $\log_3 9=2$")

mcq(r"Let $\alpha,\beta$ be the roots of $x^2-4x+2=0$. If $\log_2(\alpha\beta)$, "
    r"$\log_2\!\big[(\alpha-\beta)^2\big]$ and $k$ are in arithmetic progression, then "
    r"$k$ equals",
    [(r"$5$", 5), (r"$6$", 6), (r"$7$", 7), (r"$4$", 4)], 0, 5,
    [QE, LO, SS], "$(\\alpha-\\beta)^2=(\\alpha+\\beta)^2-4\\alpha\\beta$", "E",
    r"$\alpha\beta=2$, $(\alpha-\beta)^2=16-8=8$; $1,3,k$ in AP $\Rightarrow k=5$",
    fix=r"Notation: $\log_2(\alpha-\beta)^2$ (could be read as $[\log_2(\alpha-\beta)]^2$) "
        r"rewritten as $\log_2\big[(\alpha-\beta)^2\big]$")

mcq(r"Let $x=\log_2 3\cdot\log_3 4\cdot\log_4 5\cdots\log_{63}64$. If $x,\ y$ and "
    r"$\sqrt{x^2+13}$ are in geometric progression with $y>0$, then $y^2$ equals",
    [(r"$36$", 36), (r"$\sqrt{42}$", sqrt(42)), (r"$42$", 42), (r"$49$", 49)], 2, 42,
    [LO, SS, SU], "Chain rule of logarithms", "E",
    r"$x=\log_2 64=6$; $\sqrt{49}=7$; $y^2=6\cdot7=42$")

# ------------------------------------------------------------- SECTION B
nva(r"Given $\log_{10}2=0.3010$ and $\log_{10}3=0.4771$, let $d$ be the number of digits in "
    r"$\left(\sqrt{18}\right)^{30}$ and let $z$ be the number of zeros after the decimal point "
    r"and before the first significant digit of $\left(\sqrt{18}\right)^{-30}$. If $d+z$ is "
    r"the $n$th term of the arithmetic progression $1,4,7,\ldots$, then $n$ is",
    13, [LO, SU, SS], "Characteristic; digits and leading zeros", "M",
    r"$\log18^{15}=15(1.2552)=18.828\Rightarrow d=19$; $\log18^{-15}=\overline{19}.172"
    r"\Rightarrow z=18$; $1+3(n-1)=37\Rightarrow n=13$")

nva(r"Let $\alpha>\beta$ be the roots of $x^2-6x+4=0$. If $\alpha^3-\beta^3=m\sqrt5$ and "
    r"$m$ is the $n$th term of the geometric progression $1,2,4,8,\ldots$, then $n$ is",
    7, [QE, SU, SS], "$\\alpha^3-\\beta^3$ via factorisation", "M",
    r"$\alpha-\beta=2\sqrt5$, $\alpha^2+\alpha\beta+\beta^2=36-4=32\Rightarrow m=64=2^{6}"
    r"\Rightarrow n=7$")

nva(r"Three positive reals $a,b,c$ are in geometric progression with $a+b+c=13$ and "
    r"$a^2+b^2+c^2=91$. If $M$ is the largest of them, then $\log_3 M$ is",
    2, [SS, QE, LO], "$1+r^2+r^4=(1+r+r^2)(1-r+r^2)$", "D",
    r"$a(1-r+r^2)=7$, $a(1+r+r^2)=13\Rightarrow b=ar=3$; $a+c=10,\ ac=9\Rightarrow M=9$; "
    r"$\log_3 9=2$")

nva(r"Let $\log_{12}18=a$ and $\log_{24}54=b$, and let $m=ab+5(a-b)$. If $m,\ m+d,\ m+2d$ "
    r"are in arithmetic progression with sum $12$, then $d$ is",
    3, [LO, SS], "Classical identity $ab+5(a-b)=1$", "D",
    r"with $x=\log2,\ y=\log3$: numerator and denominator both $6x^2+5xy+y^2\Rightarrow m=1$; "
    r"$3(m+d)=12\Rightarrow d=3$")

nva(r"The third and seventh terms of an arithmetic progression are $\sqrt2$ and $5\sqrt2$. "
    r"If these two terms are the roots of ${x^2+px+q=0}$ and the fifteenth term of the "
    r"progression is $k\sqrt2$, then $k+q$ is",
    23, [SS, SU, QE], "AP terms; product of roots", "E",
    r"$4d=4\sqrt2\Rightarrow d=\sqrt2,\ a=-\sqrt2$; $T_{15}=13\sqrt2$; $q=\sqrt2\cdot5\sqrt2=10$; "
    r"$13+10=23$")

assert len(Q) == 25
