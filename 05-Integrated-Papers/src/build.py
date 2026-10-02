# -*- coding: utf-8 -*-
"""Build Paper I (JEE Main pattern) and its Zero Report in Sri Chaitanya house style.
Pass 3 lives here: after the option letters are rebalanced, the keyed option is
re-checked against the true value and the build refuses to run if it is wrong."""
import os, subprocess, sys, datetime
import bank

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'build')
os.makedirs(OUT, exist_ok=True)
LET = 'ABCD'

# Letter rebalancing. The source paper had 5/5/5/5 overall but D on five of the
# first eight questions and none after Q8, plus five back-to-back repeats.
# Each entry moves the correct option to a new letter by a single swap.
MOVE = {3: 0, 8: 1, 12: 3, 14: 2, 19: 3, 20: 0}

TOL = 1e-9


def final_questions():
    rows = []
    for i, e in enumerate(bank.Q, 1):
        e = dict(e)
        e['old'] = e['ans']
        if e['sec'] == 'A' and i in MOVE:
            o, ov, a, t = list(e['o']), list(e['ov']), e['ans'], MOVE[i]
            o[a], o[t] = o[t], o[a]
            ov[a], ov[t] = ov[t], ov[a]
            e['o'], e['ov'], e['ans'] = o, ov, t
        # ---- pass 3
        if e['sec'] == 'A':
            hits = [j for j, v in enumerate(e['ov']) if abs(v - e['val']) < TOL * max(1, abs(v))]
            assert hits == [e['ans']], ('Q%d' % i, hits, e['ans'])
            assert len({round(v, 9) for v in e['ov']}) == 4, 'Q%d duplicate options' % i
        rows.append(e)
    seq = [r['ans'] for r in rows if r['sec'] == 'A']
    counts = [seq.count(k) for k in range(4)]
    assert counts == [5, 5, 5, 5], counts
    assert all(seq[k] != seq[k + 1] for k in range(len(seq) - 1)), 'back-to-back letters'
    return rows


PRE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[a4paper,left=18mm,right=16mm,top=26mm,bottom=27mm,headsep=7mm,footskip=10mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{mathpazo}
\usepackage{amsmath,amssymb}
\usepackage{booktabs,longtable,array}
\usepackage{enumitem}
\usepackage{eso-pic}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage[most]{tcolorbox}
\usepackage{fancyhdr}
\usepackage{needspace}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}
\fancyhead[L]{\small\itshape Sri Chaitanya IIT Academy}
\fancyhead[R]{\small\itshape __RH__}
\fancyfoot[C]{\small\bfseries Page \thepage}

\AddToShipoutPictureBG{%
  \begin{tikzpicture}[overlay,remember picture]
    \draw[line width=1.1pt]
      ($(current page.north west)+(9mm,-9mm)$) rectangle ($(current page.south east)+(-9mm,9mm)$);
    \draw[line width=0.4pt]
      ($(current page.north west)+(11mm,-11mm)$) rectangle ($(current page.south east)+(-11mm,11mm)$);
  \end{tikzpicture}}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}
\sloppy
\emergencystretch=3.5em
\hbadness=10000
\newcommand{\rqq}{\textquotedblright}
\thickmuskip=5mu plus 1.5mu
\medmuskip=4mu plus 1mu minus 2mu

\newcommand{\Qitem}[2]{%
  \par\medskip\noindent\begin{minipage}{\linewidth}%
  \begin{list}{}{\leftmargin=9mm\itemindent=0pt\labelwidth=7.5mm\labelsep=1.5mm\topsep=0pt\partopsep=0pt\parsep=2pt}
  \item[\textbf{#1.}]#2
  \end{list}\end{minipage}\par}

\newcommand{\optTwo}[4]{\par\vspace{3pt}%
  \noindent{\renewcommand{\arraystretch}{1.5}%
  \begin{tabular}{@{}p{0.45\linewidth}@{\hspace{4mm}}p{0.45\linewidth}@{}}
  (A)~#1 & (B)~#2\\[6pt]
  (C)~#3 & (D)~#4
  \end{tabular}}\par\vspace{2pt}}

\newcommand{\optTwoTall}[4]{\par\vspace{5pt}%
  \noindent{\renewcommand{\arraystretch}{2.2}%
  \begin{tabular}{@{}p{0.45\linewidth}@{\hspace{4mm}}p{0.45\linewidth}@{}}
  (A)~#1 & (B)~#2\\[10pt]
  (C)~#3 & (D)~#4
  \end{tabular}}\par\vspace{4pt}}

\newcommand{\ansline}{\par\vspace{6pt}\rule{40mm}{0.4pt}\par}

\newcommand{\Section}[2]{\par\bigskip\needspace{9\baselineskip}\begin{center}{\large\bfseries #1}\\[2pt]{\bfseries #2}\end{center}\vspace{-2mm}\rule{\textwidth}{0.4pt}\par}

\begin{document}
\thispagestyle{fancy}
\begin{center}
{\large\bfseries SRI CHAITANYA IIT ACADEMY, INDIA}\\[2pt]
{\small AP \textbullet\ TELANGANA \textbullet\ KARNATAKA \textbullet\ TAMILNADU \textbullet\ MAHARASHTRA \textbullet\ DELHI \textbullet\ RANCHI}\\[5pt]
\rule{\textwidth}{0.8pt}\\[4pt]
{\large\bfseries PRAGYA G8 -- ACHIEVERS \quad\textbar\quad MATHEMATICS}\\[3pt]
{\large\bfseries __TITLE__}\\[4pt]
\rule{\textwidth}{0.8pt}
\end{center}
"""
POST = "\n\\end{document}\n"


def opts_tex(o):
    cmd = r'\optTwoTall' if any('frac' in x for x in o) else r'\optTwo'
    return cmd + ''.join('{%s}' % x for x in o)


def build_paper(rows):
    body = [PRE.replace('__RH__', r'Paper I -- Main')
               .replace('__TITLE__', r'INTEGRATED PAPER -- I \quad\textbar\quad JEE MAIN PATTERN')]
    body.append(r'\Section{SECTION -- A}{(SINGLE CORRECT ANSWER TYPE)}')
    for i, e in enumerate(rows, 1):
        if i == 21:
            body.append(r'\Section{SECTION -- B}{(NUMERICAL VALUE ANSWER TYPE)}')
        if e['sec'] == 'A':
            body.append(r'\Qitem{%d}{%s%s}' % (i, e['q'], opts_tex(e['o'])))
        else:
            body.append(r'\Qitem{%d}{%s\ansline}' % (i, e['q']))
    body.append(POST)
    return '\n'.join(body)


def key_str(e):
    return '(%s)' % LET[e['ans']] if e['sec'] == 'A' else str(e['val'])


def build_zero(rows):
    today = datetime.date(2026, 10, 2).strftime('%d-%m-%Y')
    T = [PRE.replace('__RH__', r'Zero Report -- Paper I (Main)')
            .replace('__TITLE__', r'ZERO REPORT \quad\textbar\quad INTEGRATED PAPER -- I (JEE MAIN)')]

    # ---------------- particulars
    T.append(r"""
\renewcommand{\arraystretch}{1.25}
\begin{tabular}{@{}p{42mm}p{128mm}@{}}
\textbf{Paper} & Integrated Paper -- I, JEE Main pattern (file: \texttt{Paper\_I\_MAIN.pdf})\\
\textbf{Batch} & PRAGYA G8 -- Achievers\\
\textbf{Syllabus} & Surds; Logarithms; Sequences \& Series; Quadratic Equations\\
\textbf{Pattern} & 25 questions -- Section A: Q1--20 single correct; Section B: Q21--25 numerical value\\
\textbf{Date of report} & __DATE__\\
\textbf{Result} & All 25 keys verified. 7 corrections made (listed below). \textbf{Outstanding errors: 0.}\\
\end{tabular}
""".replace('__DATE__', today))

    # ---------------- key grid
    T.append(r'\Section{ANSWER KEY}{}')
    T.append(r'\vspace{1mm}\begin{center}\renewcommand{\arraystretch}{1.45}')
    T.append(r'\begin{tabular}{|' + 'c|' * 10 + '}\\hline')
    for start in (1, 11, 21):
        idx = list(range(start, min(start + 10, 26)))
        qs = ' & '.join(r'\textbf{%d}' % i for i in idx) + ' & ' * (10 - len(idx))
        ks = ' & '.join(key_str(rows[i - 1]) for i in idx) + ' & ' * (10 - len(idx))
        T.append(qs + r'\\\hline')
        T.append(ks + r'\\\hline')
    T.append(r'\end{tabular}\end{center}')

    # ---------------- summary counts
    seq = [r['ans'] for r in rows if r['sec'] == 'A']
    lc = {LET[k]: seq.count(k) for k in range(4)}
    lev = {k: sum(1 for r in rows if r['level'] == k) for k in 'EMD'}
    chap = {}
    for r in rows:
        for c in r['ch']:
            chap[c] = chap.get(c, 0) + 1
    T.append(r'\Section{SUMMARY}{}')
    T.append(r'\vspace{1mm}\renewcommand{\arraystretch}{1.25}\begin{tabular}{@{}p{58mm}p{112mm}@{}}')
    T.append(r'\textbf{Key distribution (Section A)} & (A) %d \quad (B) %d \quad (C) %d \quad (D) %d '
             r'\quad -- no two consecutive questions share a letter\\' % (lc['A'], lc['B'], lc['C'], lc['D']))
    T.append(r'\textbf{Section B answers} & all non-negative integers (13, 7, 2, 3, 23)\\')
    T.append(r'\textbf{Difficulty} & Easy %d \quad Medium %d \quad Difficult %d\\' % (lev['E'], lev['M'], lev['D']))
    T.append(r'\textbf{Chapter usage} & ' + r' \quad '.join(
        '%s %d' % (c, chap[c]) for c in (bank.SU, bank.LO, bank.SS, bank.QE)) +
        r' \quad (questions touching each chapter)\\')
    T.append(r'\textbf{Syllabus / method level} & Within G8 CPT-01 scope; no excluded topic (AGP, sigma, '
             r'$V_n$, telescopic series, location of roots, log inequalities, graphs); no calculus, '
             r'Cauchy--Schwarz, Newton sums, cubics, trigonometry or GIF.\\')
    T.append(r'\end{tabular}')

    # ---------------- question-wise analysis
    T.append(r'\Section{QUESTION-WISE ANALYSIS}{}')
    T.append(r'\vspace{1mm}{\small\renewcommand{\arraystretch}{1.3}')
    T.append(r'\begin{longtable}{@{}c c p{38mm} p{72mm} c c@{}}\toprule')
    T.append(r'\textbf{Q} & \textbf{Type} & \textbf{Chapters} & \textbf{Concept tested} & '
             r'\textbf{Level} & \textbf{Key}\\\midrule\endhead')
    abbr = {bank.SU: 'Surds', bank.LO: 'Logs', bank.SS: 'S\\&S', bank.QE: 'QE'}
    for i, r in enumerate(rows, 1):
        T.append(r'%d & %s & %s & %s & %s & %s\\' % (
            i, 'SCQ' if r['sec'] == 'A' else 'NVA', ', '.join(abbr[c] for c in r['ch']),
            r['concept'], r['level'], key_str(r)))
    T.append(r'\bottomrule\end{longtable}}')
    T.append(r'{\footnotesize SCQ = single correct; NVA = numerical value answer; '
             r'E/M/D = easy/medium/difficult.}')

    # ---------------- corrections log
    moved = ', '.join('Q%d (%s$\\to$%s)' % (i, LET[rows[i - 1]['old']], LET[rows[i - 1]['ans']])
                      for i in sorted(MOVE))
    T.append(r'\Section{ERRORS FOUND AND CORRECTED}{}')
    T.append(r'\begin{enumerate}[leftmargin=7mm,itemsep=3pt,topsep=4pt]')
    T.append(r'\item \textbf{Title / header.} ``Hell Paper\rqq{} and ``(HELL LEVEL)\rqq{} removed. Paper is now '
             r'\emph{Integrated Paper -- I, JEE Main pattern}; running header reads \emph{Paper I -- Main}.')
    T.append(r'\item \textbf{Tagline removed.} ``Every question draws on at least three of: Surds, Logarithms, '
             r'Sequences \& Series, Quadratic Equations\rqq{} was also not true -- Q13, Q14, Q15, Q16, Q17 '
             r'and Q24 each use two chapters (see analysis table).')
    T.append(r'\item \textbf{Instruction and marking-scheme boxes removed} from both sections. The Section B box '
             r'was also wrong for a numerical section (``$+4$ if the correct \emph{option} is chosen\rqq{}, '
             r'$-1$ negative marking).')
    T.append(r'\item \textbf{Q19 -- ambiguous notation.} $\log_2(\alpha-\beta)^2$ can be read as '
             r'$\big[\log_2(\alpha-\beta)\big]^2$; rewritten as $\log_2\big[(\alpha-\beta)^2\big]$. '
             r'Key unchanged.')
    T.append(r'\item \textbf{Q10 -- wording.} ``the sum to infinity of the geometric progression\rqq{} now names it: '
             r'``\ldots of the geometric progression $a,b,c,\ldots$\rqq{}. Key unchanged.')
    T.append(r'\item \textbf{Page breaks.} Q5 and Q19 had their options printed on the next page, away '
             r'from the stem. Every question is now kept on one page with its options; the long surd sum in Q1 is now set on its own line.')
    T.append(r'\item \textbf{Answer-letter clustering.} Overall 5/5/5/5, but (D) was the key for five of '
             r'Q2--Q8 and for none of Q9--Q20, with five back-to-back repeats. Options swapped in ' + moved +
             r'; same options, same answers, new letters.')
    T.append(r'\end{enumerate}')
    T.append(r'No answer in the paper was wrong, no question had zero or two correct options, '
             r'and no two options in any question were equal.')

    T.append(r'\Section{OBSERVATIONS (NO CHANGE MADE)}{}')
    T.append(r'\begin{itemize}[leftmargin=7mm,itemsep=3pt,topsep=4pt]')
    T.append(r'\item Q8 and Q22 test the same step ($\alpha^3-\beta^3=(\alpha-\beta)(\alpha^2+\alpha\beta+\beta^2)$) '
             r'on different quadratics; Q1 and Q6 share one template (a surd taken as a root of $x^2+px+q=0$ '
             r'with $p,q\in\mathbb Z$).')
    T.append(r'\item Q2 needs the base $=-1$ (even index) case. A student who omits it gets $S=10$, which is '
             r'not a term of $3,7,11,\ldots$ -- so there is no rival answer to object with.')
    T.append(r'\item Q4 rests on $N=0$ (the two logarithms cancel identically); that is the intended trap.')
    T.append(r'\end{itemize}')

    # ---------------- key verification
    T.append(r'\Section{KEY VERIFICATION}{}')
    T.append(r'\begin{list}{}{\leftmargin=19mm\labelwidth=17mm\labelsep=2mm\itemsep=3pt\topsep=4pt\renewcommand{\makelabel}[1]{#1\hfil}}')
    for i, r in enumerate(rows, 1):
        T.append(r'\item[\textbf{Q%d}~%s] %s' % (i, key_str(r), r['work']))
    T.append(r'\end{list}')

    T.append(r'\Section{VERIFICATION METHOD}{}')
    T.append(r'\begin{enumerate}[leftmargin=7mm,itemsep=2pt,topsep=4pt]')
    T.append(r'\item \textbf{Brute force from the statement} -- every equation solved by numerical scanning, '
             r'integer conditions by exhaustive search; exactly one option must match.')
    T.append(r'\item \textbf{Exact arithmetic along the hand method} -- fractions and exact $a+b\sqrt n$ '
             r'numbers; 60-digit decimals where a logarithm is unavoidable.')
    T.append(r'\item \textbf{Build-time check} -- after the option swaps, the keyed option is re-matched '
             r'to the true value before the paper is typeset.')
    T.append(r'\item \textbf{Independent re-solve} -- a separate solver, given only the printed paper, '
             r'solved all 25 from scratch: __AUDIT__')
    T.append(r'\end{enumerate}')
    T.append(POST)
    return '\n'.join(T)


def compile_tex(tex, name):
    p = os.path.join(OUT, name + '.tex')
    open(p, 'w').write(tex)
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error', name + '.tex'],
                           cwd=OUT, capture_output=True, text=True)
        if r.returncode:
            sys.exit(r.stdout[-3000:])
    log = open(os.path.join(OUT, name + '.log')).read()
    over = [l for l in log.splitlines() if l.startswith('Overfull')]
    if over:
        sys.exit('OVERFULL in %s:\n%s' % (name, '\n'.join(over)))
    return os.path.join(OUT, name + '.pdf')


if __name__ == '__main__':
    rows = final_questions()
    audit = sys.argv[1] if len(sys.argv) > 1 else 'PENDING'
    print(compile_tex(build_paper(rows), 'Paper_I_MAIN'))
    print(compile_tex(build_zero(rows).replace('__AUDIT__', audit), 'Paper_I_MAIN_Zero_Report'))
    print('KEY:', ' '.join('%d%s' % (i, key_str(r)) for i, r in enumerate(rows, 1)))
