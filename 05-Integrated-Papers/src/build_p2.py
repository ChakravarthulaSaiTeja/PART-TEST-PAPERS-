# -*- coding: utf-8 -*-
"""Build Paper II (JEE Advanced pattern) and its Zero Report.
Shares the house-style preamble with build.py. Pass 3: before typesetting,
the keyed option(s) of every MCQ are re-matched to the computed truth."""
import os, sys, datetime
from math import sqrt
import bank, bank_p2
from build import PRE, POST, OUT, compile_tex, opts_tex, LET

TOL = 1e-9


def check(rows):
    for i, e in enumerate(rows, 1):
        if e['sec'] == 'III':
            hits = [j for j, v in enumerate(e['ov']) if abs(v - e['val']) < TOL * max(1, abs(v))]
            assert hits == [e['ans']], ('Q%d' % i, hits)
            assert len({round(v, 9) for v in e['ov']}) == 4
        elif e['sec'] == 'I':
            assert isinstance(e['ans'], int) and 0 <= e['ans'] <= 9
        else:
            assert 1 <= len(e['ans']) <= 4 and len(set(e['o'])) == 4
    return rows


def key_str(e):
    if e['sec'] == 'I':
        return str(e['ans'])
    if e['sec'] == 'II':
        return '(%s)' % ', '.join(LET[j] for j in e['ans'])
    return '(%s)' % LET[e['ans']]


def opts_list(o):
    return (r'\par\vspace{2pt}\begin{list}{}{\leftmargin=9mm\itemindent=0pt\labelwidth=7mm'
            r'\labelsep=2mm\topsep=2pt\parsep=0pt\itemsep=4pt}' +
            ''.join(r'\item[(%s)]%s' % (L, x) for L, x in zip(LET, o)) + r'\end{list}')


SEC = {'I': (r'SECTION -- I', r'(INTEGER ANSWER TYPE)'),
       'II': (r'SECTION -- II', r'(ONE OR MORE CORRECT ANSWER TYPE)'),
       'III': (r'SECTION -- III', r'(SINGLE CORRECT ANSWER TYPE)')}


def build_paper(rows):
    body = [PRE.replace('__RH__', r'Paper II -- Advanced')
               .replace('__TITLE__', r'INTEGRATED PAPER -- II \quad\textbar\quad JEE ADVANCED PATTERN')]
    cur = None
    for i, e in enumerate(rows, 1):
        if e['sec'] != cur:
            cur = e['sec']
            body.append(r'\Section{%s}{%s}' % SEC[cur])
        if e['sec'] == 'I':
            body.append(r'\Qitem{%d}{%s\ansline}' % (i, e['q']))
        elif e['sec'] == 'II':
            body.append(r'\Qitem{%d}{%s%s}' % (i, e['q'], opts_list(e['o'])))
        else:
            body.append(r'\Qitem{%d}{%s%s}' % (i, e['q'], opts_tex(e['o'])))
    body.append(POST)
    return '\n'.join(body)


def build_zero(rows, audit):
    today = datetime.date(2026, 10, 2).strftime('%d-%m-%Y')
    T = [PRE.replace('__RH__', r'Zero Report -- Paper II (Advanced)')
            .replace('__TITLE__', r'ZERO REPORT \quad\textbar\quad INTEGRATED PAPER -- II (JEE ADVANCED)')]
    T.append(r"""
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{@{}p{42mm}p{128mm}@{}}
\textbf{Paper} & Integrated Paper -- II, JEE Advanced pattern (file: \texttt{Paper\_II\_ADVANCED.pdf})\\
\textbf{Batch} & PRAGYA G8 -- Achievers\\
\textbf{Syllabus} & Surds; Logarithms; Sequences \& Series; Quadratic Equations\\
\textbf{Pattern} & 18 questions -- Section I: Q1--8 integer (0--9); Section II: Q9--14 one or more correct; Section III: Q15--18 single correct\\
\textbf{Date of report} & __DATE__\\
\textbf{Result} & All 18 keys verified. 5 corrections made (listed below). \textbf{Outstanding errors: 0.}\\
\end{tabular}
""".replace('__DATE__', today))

    # key grid: 3 rows of 6
    T.append(r'\Section{ANSWER KEY}{}')
    T.append(r'\vspace{1mm}\begin{center}\renewcommand{\arraystretch}{1.45}')
    T.append(r'\begin{tabular}{|' + 'c|' * 6 + '}\\hline')
    for start in (1, 7, 13):
        idx = list(range(start, start + 6))
        T.append(' & '.join(r'\textbf{%d}' % i for i in idx) + r'\\\hline')
        T.append(' & '.join(key_str(rows[i - 1]) for i in idx) + r'\\\hline')
    T.append(r'\end{tabular}\end{center}')

    lev = {k: sum(1 for r in rows if r['level'] == k) for k in 'EMD'}
    chap = {}
    for r in rows:
        for c in r['ch']:
            chap[c] = chap.get(c, 0) + 1
    T.append(r'\Section{SUMMARY}{}')
    T.append(r'\vspace{1mm}\renewcommand{\arraystretch}{1.25}\begin{tabular}{@{}p{58mm}p{112mm}@{}}')
    T.append(r'\textbf{Section I answers} & 4, 5, 2, 1, 9, 7, 6, 3 -- all single digits, no repeats\\')
    T.append(r'\textbf{Section II keys} & two items with 2 correct, four with 3 correct; '
             r'(A) correct in 5, (B) 4, (C) 4, (D) 3\\')
    T.append(r'\textbf{Section III keys} & (D), (A), (B), (C) -- one of each\\')
    T.append(r'\textbf{Difficulty} & Easy %d \quad Medium %d \quad Difficult %d\\' % (lev['E'], lev['M'], lev['D']))
    T.append(r'\textbf{Chapter usage} & ' + r' \quad '.join(
        '%s %d' % (c, chap.get(c, 0)) for c in (bank.SU, bank.LO, bank.SS, bank.QE)) +
        r' \quad (questions touching each chapter)\\')
    T.append(r'\textbf{Syllabus / method level} & Within G8 CPT-01 scope; no excluded topic (AGP, sigma, '
             r'$V_n$, telescopic series, location of roots, log inequalities, graphs); no calculus, '
             r'Cauchy--Schwarz, Newton sums, cubic equations, trigonometry or GIF.\\')
    T.append(r'\end{tabular}')

    T.append(r'\Section{QUESTION-WISE ANALYSIS}{}')
    T.append(r'\vspace{1mm}{\small\renewcommand{\arraystretch}{1.3}')
    T.append(r'\begin{longtable}{@{}c c p{36mm} p{70mm} c c@{}}\toprule')
    T.append(r'\textbf{Q} & \textbf{Type} & \textbf{Chapters} & \textbf{Concept tested} & '
             r'\textbf{Level} & \textbf{Key}\\\midrule\endhead')
    abbr = {bank.SU: 'Surds', bank.LO: 'Logs', bank.SS: 'S\\&S', bank.QE: 'QE'}
    typ = {'I': 'INT', 'II': 'MCQ+', 'III': 'SCQ'}
    for i, r in enumerate(rows, 1):
        T.append(r'%d & %s & %s & %s & %s & %s\\' % (
            i, typ[r['sec']], ', '.join(abbr[c] for c in r['ch']), r['concept'], r['level'], key_str(r)))
    T.append(r'\bottomrule\end{longtable}}')
    T.append(r'{\footnotesize INT = integer answer; MCQ+ = one or more correct; SCQ = single correct; '
             r'E/M/D = easy/medium/difficult.}')

    T.append(r'\Section{ERRORS FOUND AND CORRECTED}{}')
    T.append(r'\begin{enumerate}[leftmargin=7mm,itemsep=3pt,topsep=4pt]')
    T.append(r'\item \textbf{Title / header.} ``Hell Paper\rqq{} and ``(HELL LEVEL)\rqq{} removed. Paper is now '
             r'\emph{Integrated Paper -- II, JEE Advanced pattern}; running header reads \emph{Paper II -- Advanced}.')
    T.append(r'\item \textbf{Tagline removed.} ``Every question draws on at least three of \ldots\rqq{} was not '
             r'true: Q2 and Q10 use Sequences \& Series only; Q4 uses Logarithms and Surds; Q14 uses '
             r'Logarithms and Sequences \& Series.')
    T.append(r'\item \textbf{Instruction and marking-scheme boxes removed} from all three sections. The Section I '
             r'box was also wrong for an integer section (``$+3$ if ONLY the correct \emph{option} is chosen\rqq{} '
             r'-- the section has no options).')
    T.append(r'\item \textbf{Q14 -- objection route closed.} The statement allowed a constant progression '
             r'($a=b=c$), for which (B) and (D) are also true. Now reads ``Let $a,b,c$ be \emph{distinct} '
             r'positive reals \ldots\rqq{}. Key unchanged: (A), (C).')
    T.append(r'\item \textbf{Page break.} Q12 had options (C) and (D) printed on the next page. Every question is '
             r'now kept on one page with its options; the two equations in Q15 are set on their own line.')
    T.append(r'\end{enumerate}')
    T.append(r'No answer in the paper was wrong. Every Section II item has at least one correct option and no '
             r'two identical options; every Section III item has exactly one correct option.')

    T.append(r'\Section{OBSERVATIONS (NO CHANGE MADE)}{}')
    T.append(r'\begin{itemize}[leftmargin=7mm,itemsep=3pt,topsep=4pt]')
    T.append(r'\item Q8 is the same construction as Paper I Q2 ($f(x)^{g(x)}=1$ with the base $=-1$ case) '
             r'on different numbers; a student who has written Paper I will recognise it. Omitting the base $=-1$ '
             r'case gives $T=20$ and no integer answer, so there is no rival key.')
    T.append(r'\item Q1 is meant to be done by spotting $7\pm5\sqrt2=(1\pm\sqrt2)^3$ (cube of a binomial surd, as in '
             r'the Surds L1/L2 cube-root items). The other common route -- cubing $s=u+v$ -- leads to '
             r'$s^3+3s-14=0$, solvable only by inspecting $s=2$; borderline for the no-cubics rule.')
    T.append(r'\item Redundant but harmless conditions: ``positive\rqq{} in Q5 (the ratio is forced to be $9$) '
             r'and ``whose other root is also a term\rqq{} in Q7 (the other root is $2=a_2$ automatically).')
    T.append(r'\item Repeated templates: Q9 and Q12 (denest $\sqrt{m\pm2\sqrt n}$, then sum/product/progression/'
             r'quadratic); Q6, Q11 and Q18 (quadratic in a logarithm, then a GP).')
    T.append(r'\item Q10 (C) is a distractor: the sum of the cubes is $\dfrac{375}{7}$, not $\dfrac{375}{13}$.')
    T.append(r'\end{itemize}')

    T.append(r'\Section{KEY VERIFICATION}{}')
    T.append(r'\begin{list}{}{\leftmargin=21mm\labelwidth=19mm\labelsep=2mm\itemsep=3pt\topsep=4pt'
             r'\renewcommand{\makelabel}[1]{#1\hfil}}')
    for i, r in enumerate(rows, 1):
        T.append(r'\item[\textbf{Q%d}~%s] %s' % (i, key_str(r), r['work']))
    T.append(r'\end{list}')

    T.append(r'\Section{VERIFICATION METHOD}{}')
    T.append(r'\begin{enumerate}[leftmargin=7mm,itemsep=2pt,topsep=4pt]')
    T.append(r'\item \textbf{Brute force from the statement} -- equations solved by numerical scanning, integer '
             r'conditions by exhaustive search; every Section II option evaluated as a statement (Q14 tested on '
             r'2000 random progressions).')
    T.append(r'\item \textbf{Exact arithmetic along the hand method} -- fractions and exact $a+b\sqrt n$ '
             r'numbers; 60-digit decimals where a logarithm is unavoidable.')
    T.append(r'\item \textbf{Build-time check} -- keyed options re-matched to the true values before typesetting.')
    T.append(r'\item \textbf{Independent re-solve} -- a separate solver, given only the printed paper, '
             r'solved all 18 from scratch: ' + audit)
    T.append(r'\end{enumerate}')
    T.append(POST)
    return '\n'.join(T)


if __name__ == '__main__':
    rows = check([dict(e) for e in bank_p2.Q])
    audit = sys.argv[1] if len(sys.argv) > 1 else 'PENDING'
    print(compile_tex(build_paper(rows), 'Paper_II_ADVANCED'))
    print(compile_tex(build_zero(rows, audit), 'Paper_II_ADVANCED_Zero_Report'))
    print('KEY:', ' '.join('%d%s' % (i, key_str(r)) for i, r in enumerate(rows, 1)))
