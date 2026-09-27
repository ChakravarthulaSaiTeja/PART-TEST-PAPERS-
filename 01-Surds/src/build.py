# -*- coding: utf-8 -*-
"""Build the four Sri Chaitanya house-style Surds papers (L1-L4) + key sheet."""
import os, random, subprocess, sys
sys.path.insert(0, '/home/claude/surds')
import bank

OUT = '/home/claude/surds/out'
os.makedirs(OUT, exist_ok=True)
LET = 'ABCD'
PIN_D = ('none of these', 'not determined', 'not detemined')

TITLES = {
    'L1': ('SURDS \\quad\\textbar\\quad LEVEL 1', 'Surds -- Level 1'),
    'L2': ('SURDS \\quad\\textbar\\quad LEVEL 2', 'Surds -- Level 2'),
    'L3': ('SURDS \\quad\\textbar\\quad LEVEL 3', 'Surds -- Level 3'),
    'L4': ('SURDS \\quad\\textbar\\quad LEVEL 4', 'Surds -- Level 4'),
}
BLURB = {
    'L1': 'Straightforward -- one idea, one step.',
    'L2': 'Lengthy -- correct method, sustained computation.',
    'L3': 'Tricky -- the method has to be found before it can be used.',
    'L4': 'JEE pattern -- mixed difficulty, exam standard.',
}

PRE = r"""\documentclass[11pt,a4paper]{article}
\usepackage[a4paper,left=18mm,right=16mm,top=26mm,bottom=22mm,headsep=7mm,footskip=11mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage{mathpazo}
\usepackage{amsmath,amssymb}
\usepackage{booktabs}
\usepackage{enumitem}
\usepackage{eso-pic}
\usepackage{tikz}
\usetikzlibrary{calc}
\usepackage[most]{tcolorbox}
\usepackage{fancyhdr}
\usepackage{array}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.4pt}
\fancyhead[L]{\small\itshape Sri Chaitanya IIT Academy}
\fancyhead[R]{\small\itshape __RH__}
\fancyfoot[L]{\small PRAGYA G8 -- Achievers}
\fancyfoot[R]{\small Page \thepage}

\AddToShipoutPictureBG{%
  \begin{tikzpicture}[overlay,remember picture]
    \draw[line width=1.1pt]
      ($(current page.north west)+(9mm,-9mm)$) rectangle ($(current page.south east)+(-9mm,9mm)$);
    \draw[line width=0.4pt]
      ($(current page.north west)+(11mm,-11mm)$) rectangle ($(current page.south east)+(-11mm,11mm)$);
  \end{tikzpicture}}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0pt}

\newcounter{qno}
\newcommand{\Q}[1]{\stepcounter{qno}%
  \par\medskip\noindent
  \begin{list}{}{\leftmargin=9mm\itemindent=-9mm\labelwidth=8mm\topsep=0pt\partopsep=0pt\parsep=2pt}
  \item[\textbf{\theqno.}]#1
  \end{list}}

\newcommand{\optTwo}[4]{\par\vspace{3pt}%
  \noindent{\renewcommand{\arraystretch}{1.5}%
  \begin{tabular}{@{\hspace{9mm}}p{0.42\textwidth}@{\hspace{4mm}}p{0.42\textwidth}@{}}
  (A)~#1 & (B)~#2\\[6pt]
  (C)~#3 & (D)~#4
  \end{tabular}}\par\vspace{2pt}}

\newcommand{\optOne}[4]{\par\vspace{2pt}%
  \begin{list}{}{\leftmargin=14mm\itemindent=-5mm\topsep=2pt\parsep=1pt\itemsep=5pt}
  \item[(A)]#1 \item[(B)]#2 \item[(C)]#3 \item[(D)]#4
  \end{list}}

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
\vspace{2mm}
"""
POST = "\n\\end{document}\n"


def optlen(s):
    """rough printed width of an option, ignoring latex control words"""
    n, i = 0, 0
    while i < len(s):
        if s[i] == '\\':
            j = i + 1
            while j < len(s) and s[j].isalpha():
                j += 1
            n += 1
            i = max(j, i + 2)
        elif s[i] in '${}~ ':
            i += 1
        else:
            n += 1
            i += 1
    return n


def emit_opts(o):
    cmd = r'\optOne' if max(optlen(x) for x in o) > 46 else r'\optTwo'
    return cmd + ''.join('{%s}' % x for x in o)


def shuffled(level, seed):
    """Permute options so answer letters come out ~evenly, pinning
    'none of these' style options to (D)."""
    ids = bank.LEVELS[level]
    rnd = random.Random(seed)
    target = [0, 1, 2, 3] * 6 + [0, 1, 2, 3][:1]        # 25 = 7,6,6,6
    rnd.shuffle(target)
    best = None
    for _ in range(4000):
        rnd.shuffle(target)
        out, counts, ok = [], [0, 0, 0, 0], True
        for k, qid in enumerate(ids):
            e = bank.Q[qid]
            opts, ans = list(e['o']), e['ans']
            pin = [i for i, t in enumerate(opts)
                   if any(p in t.lower() for p in PIN_D)]
            want = target[k]
            if pin:
                if pin[0] == ans:          # the pinned option IS the answer
                    want = 3
                elif want == 3:
                    want = (want + 1 + k) % 3
            perm = list(range(4))
            rnd.shuffle(perm)
            # place correct option at `want`, pinned option at 3
            order = [None] * 4
            order[want] = ans
            if pin and pin[0] != ans:
                if order[3] is not None:
                    ok = False; break
                order[3] = pin[0]
            rest = [i for i in range(4) if i not in order]
            rnd.shuffle(rest)
            for slot in range(4):
                if order[slot] is None:
                    order[slot] = rest.pop()
            newopts = [opts[i] for i in order]
            newans = order.index(ans)
            assert newans == want
            counts[newans] += 1
            out.append((qid, newopts, newans, order))
        if not ok:
            continue
        if max(counts) - min(counts) <= 1:
            best = (out, counts)
            break
    assert best, level
    return best


def verify_final(level, rows):
    """Third pass: after shuffling, re-confirm the keyed option is the true one."""
    bad = []
    for qid, newopts, newans, order in rows:
        e = bank.Q[qid]
        if e['optvals'] is None:
            # symbolic item: the option TEXT must be unchanged at the new index
            if newopts[newans] != e['o'][e['ans']]:
                bad.append((qid, 'keyed option text moved'))
            continue
        t = e['truth']()
        f = e['optvals'][order[newans]]
        if f is None:
            hits = [i for i, g in enumerate(e['optvals'])
                    if g is not None and abs(g() - t) < 1e-6 * max(1.0, abs(t))]
            if hits:
                bad.append((qid, 'none-of-these key but %s matches' % hits))
        elif abs(f() - t) > 1e-6 * max(1.0, abs(t)):
            bad.append((qid, 'keyed option no longer equals the true value'))
        if newopts[newans] != e['o'][e['ans']]:
            bad.append((qid, 'text/index mismatch after shuffle'))
    return bad


def build(level, seed):
    rows, counts = shuffled(level, seed)
    bad = verify_final(level, rows)
    if bad:
        print('POST-SHUFFLE FAILURES in %s: %s' % (level, bad))
        sys.exit(1)
    title, rh = TITLES[level]
    body = [PRE.replace('__TITLE__', title).replace('__RH__', rh)]
    body.append(r'\begin{center}\small\itshape %s\end{center}\vspace{1mm}' % BLURB[level])
    for qid, opts, ans, order in rows:
        body.append('\\Q{%s}' % bank.Q[qid]['q'])
        body.append(emit_opts(opts))
    body.append(POST)
    tex = os.path.join(OUT, 'Surds_%s.tex' % level)
    open(tex, 'w').write('\n'.join(body))
    compile_tex(tex)
    return [(i + 1, qid, LET[ans]) for i, (qid, o, ans, od) in enumerate(rows)], counts


def compile_tex(path):
    for _ in range(2):
        r = subprocess.run(['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                            '-output-directory', OUT, path],
                           capture_output=True, text=True)
    if r.returncode:
        print(r.stdout[-3000:])
        sys.exit('LaTeX failed on ' + path)


def build_keys(allkeys):
    body = [PRE.replace('__TITLE__', 'SURDS \\quad\\textbar\\quad ANSWER KEYS (L1--L4)')
                .replace('__RH__', 'Surds -- Answer Keys')]
    for lv in ('L1', 'L2', 'L3', 'L4'):
        keys = allkeys[lv]
        body.append(r'\vspace{3mm}\begin{center}\bfseries\large LEVEL %s\end{center}' % lv[1])
        body.append(r'\begin{center}\small\itshape %s\end{center}\vspace{1mm}' % BLURB[lv])
        cols = 5
        rowsn = (len(keys) + cols - 1) // cols
        body.append(r'\begin{center}\renewcommand{\arraystretch}{1.25}')
        body.append(r'\begin{tabular}{' + 'cc'.join(['|'] * 1) +
                    ('@{\\hspace{5mm}}r@{~--~}c' * cols) + r'@{}}\toprule')
        lines = []
        for r0 in range(rowsn):
            cells = []
            for c in range(cols):
                i = c * rowsn + r0
                cells.append('%d & \\textbf{%s}' % (keys[i][0], keys[i][2]) if i < len(keys) else ' & ')
            lines.append(' & '.join(cells) + r'\\')
        body.append('\n'.join(lines))
        body.append(r'\bottomrule\end{tabular}\end{center}')
    body.append(POST)
    tex = os.path.join(OUT, 'Surds_ANSWER_KEYS.tex')
    open(tex, 'w').write('\n'.join(body))
    compile_tex(tex)


if __name__ == '__main__':
    allkeys = {}
    for lv, seed in (('L1', 11), ('L2', 22), ('L3', 33), ('L4', 44)):
        k, c = build(lv, seed)
        allkeys[lv] = k
        print('%s built  letter spread A/B/C/D = %s' % (lv, c))
    build_keys(allkeys)
    print('keys built')
