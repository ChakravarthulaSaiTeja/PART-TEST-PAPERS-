# PART TEST PAPERS — Sri Chaitanya IIT Academy, PRAGYA G8 Achievers

> **New session starting here: read this whole file before touching anything.**
> Section 7 (STATUS) says exactly where the work stopped and what to do next.

---

## 1. Who this is for and what the goal is

**Teja** is Head of Mathematics at Sri Chaitanya IIT Academy, with about 30 years of
teaching experience. He works with the **PRAGYA G8 batch (Achievers cohort)** —
Class 8–10 students on an IIT-JEE Foundation track. He writes their assignments,
verifies answer keys, files objections against bad questions, and produces solution
PDFs for the weekly tests.

He has a folder of **scraped question sets** for four chapters (`source-pdfs/`).
They came out of some earlier bulk extraction and they are messy: image crops, some
clipped, some duplicated, some with genuine typos, many in formats he can't use
(multiple-correct, matrix-matching, subjective).

**The goal: turn each of those four chapters into four clean, printable,
independently-verified assignment papers, one per difficulty level, plus an answer
key and a detailed-solutions PDF for each.**

Sixteen papers in all. Everything in Sri Chaitanya house style, ready to hand to
students.

### The four levels — Teja's own definitions. Do not reinterpret them.

| Level | What it means |
|-------|---------------|
| **L1** | **Easy, straightforward.** One idea, one step. |
| **L2** | **LENGTHY.** He corrected me on this explicitly — it does **not** mean "medium". It means long, grinding computation with an ordinary method. |
| **L3** | **Tricky.** The method has to be found before it can be used. |
| **L4** | **PYQs** — previous-year questions — wherever a real PYQ source exists. Where none exists, a JEE-pattern paper that says on its face that it is JEE-pattern and not genuine PYQs. |

**25 questions per paper.** Four chapters × four levels = 400 questions.

### What he actually values

He has said, in different ways, several times: **check every question before giving
him the final copy, and check it twice.** The papers looking finished matters far
less to him than the keys being right and the discards being reported honestly. When
a source question is broken, he wants to be told it was dropped and why — not to
find a silent substitution later.

He wants **PDFs**. Not .docx. He said "pdf is enough" early on and it has not changed.

---

## 2. Hard constraints

### Syllabus — `syllabus/G8-CPT-01-syllabus.png`, G8 COMMON PART TEST-01

1. **Surds** — no exclusions.
2. **Logarithms** — *graphs and logarithmic inequalities are excluded.*
3. **Sequence and series** — *AGP, sigma notation and properties, Vn method,
   telescopic series, and application of maxima and minima (without calculus) are
   excluded.*
4. **Quadratic Equations** — *location of roots, and solving inequalities based on
   location of roots (modulus, logarithmic, exponential), are excluded.*

### Method level — class 8

Teja's words: *"solving methods has to be like 8th standard not some cauchy
inequality or something."* Ruled out, accumulated across the project:

- Cauchy–Schwarz and other named advanced inequalities; AM–GM as a *required* tool
- calculus of any kind
- Newton's sums / power-sum recurrences (`aₙ = αⁿ − βⁿ`, `pₖ = αᵏ + βᵏ` and friends)
- cube roots of unity
- the greatest-integer function
- trigonometry
- powers of *e* and *π*
- complex numbers
- cubic and biquadratic equations in the Quadratic Equations chapter

A question that is in-syllabus but needs machinery past that line gets **replaced**,
and the replacement is recorded in a `note=` on the bank entry. This has already
happened once (a Cardano cube-root identity in Surds L3).

### Paper conventions — Sri Chaitanya house style

- A4; **`mathpazo`**, never `lmodern`; double-line TikZ page border via `eso-pic`;
  `fancyhdr` header and footer; strict black and white, no colour anywhere.
- Continuous numbering 1–25. No per-section restart.
- Options two per line — `(A) (B)` then `(C) (D)`. Long options and prose options
  fall back to one per line automatically; options containing fractions get a taller
  row so they can't collide.
- **No marks shown anywhere. No instructions box. No marking scheme.** He asked for
  all three to be removed and they must stay out.
- Answer letters balanced across A/B/C/D (7/6/6/6 for a 25-question paper).
  `none of these` / `not determined` is always pinned to **(D)**.

---

## 3. The method — this is the part that matters

**No printed answer key is ever trusted.** Every key is re-derived from scratch.
This is not paranoia; it is where the value is. On this project so far it has caught:

- **8 defective Surds source questions** (dropped) and **3 needing reconstruction**
- **9 defective Quadratic Equations questions** in his earlier hell-difficulty set
- **6 bad distractor options in Surds** and **a duplicate option pair plus a
  formally vacuous premise in Logarithms** — found by the audit pass, invisible to
  the numeric passes because those only check the key

### Four passes

Each chapter's `src/` holds `bank.py`, `verify.py`, `verify2.py`, `build.py`.

**`bank.py`** — every question as a dict: LaTeX question text, four LaTeX options,
the keyed index, and a machine-checkable statement of the truth. Two forms:

- `truth=` (lambda giving the true value) with `optvals=` (one lambda per option).
  The checker confirms **exactly one** option matches and that it is the keyed one.
  Helper `num(...)` builds this shape from `[(latex, value), ...]` pairs.
- `chk=` (lambda returning True/False) for symbolic items: rationalising factors
  (multiply out, assert the product is rational), parametric identities (test at
  3+ parameter values), counting arguments, range arguments.

**Pass 1 — `verify.py`.** Ordinary floating point.

**Pass 2 — `verify2.py`.** *Independent.* An AST transform rewrites `bank.py` so
every numeric literal becomes a 60-significant-digit `Decimal`, and `sqrt`/`log`/
n-th root are swapped for Decimal versions. This is not a re-run of pass 1 — several
nested-radical items lose 12 of 16 significant digits to cancellation in float.

**Pass 3 — inside `build.py`.** The builder shuffles the options for letter balance,
then re-confirms the keyed option still holds the true value, and refuses to compile
if it doesn't. It also fails loudly on overfull lines so nothing runs off the page.

**Pass 4 — a subagent that has not seen the working.** `tools/mkaudit.py` dumps each
built paper back to plain LaTeX blocks in `tools/audit/`. Then dispatch a subagent:

> Read `tools/audit/<Chapter>_L1_audit.txt` and `..._L2_audit.txt`. The printed keys
> are `<paste the line from tools/audit/<Chapter>_keys_flat.txt>`. Solve every
> question from scratch; do not assume the key is right. Use python3 — numpy is
> available, **sympy is not**. Report only: answers that differ from the key;
> questions where zero or two-plus options match; duplicate or identical option
> pairs; printing typos; ill-posed questions. Say explicitly if everything agrees.

Run it in two halves per chapter (L1+L2, then L3+L4) so each agent handles 50
questions. **Do this for every chapter before shipping it.** It is the only pass that
can see a bad *distractor*, and it has already earned its keep twice.

### Environment notes

- **sympy cannot be installed** — PyPI returns 403 through the proxy. Use `numpy`,
  `fractions.Fraction`, and `decimal`. Every existing check is written that way.
- The source PDFs are **image crops**; `pdftotext` returns only the question numbers.
  Read them from `source-pages/` (already rendered, 110 dpi grayscale, ~962 pages) or
  re-render with `pdftoppm -png -r 125 -f N -l M "<pdf>" out/prefix`.
- A cheap way to triage which pages are worth reading: build a contact sheet —
  `pdftoppm -png -r 40 -f A -l B "<pdf>" tri/T` then
  `montage tri/T-0*.png -tile 4x3 -geometry +3+3 sheet.png` — and read that first.
  Layout and question density are legible at 40 dpi even when the maths is not.

---

## 4. Source-material hazards

Expect roughly 8% unusable per chapter, plus a few percent needing reconstruction:

- **Clipped crops** — the top of tall fractions gone, or whole options missing.
  About **16% of the Quadratic Equations crops are permanently truncated** (630 px
  wide, options 3–4 simply absent from the file); pages ~85–100 are the worst.
- **Overlapping crops** — two different option sets printed on top of each other.
- **OCR digit loss** — `32√15` printed as `32√5`.
- **Genuine source typos** — an option matching nothing, a repeated surd, `+3` where
  `+√3` belongs, `√4` where a real surd belongs.
- **Duplicates** — the same question twice under different numbers, and across
  chapters (one item appears in both the Logarithms and the Quadratic Equations
  files; it is used once, in Logarithms L2).
- **Multiple-correct and matrix/matching items** — the Logarithms set is full of
  them. Matching items are gold: each row becomes a good standalone MCQ once solved.
- **Subjective (no-option) items** — also gold: compute the answer, write four
  options round it.

Rule: **discard** anything ambiguous; **reconstruct** only where the correct reading
is provable — e.g. the fixed version makes exactly one printed option exact. Record
which in `note=`, and list discards in a `DROPPED` dict at the end of `bank.py`.

---

## 5. PYQ situation (this decides what L4 is)

- **Quadratic Equations: real PYQs are already in the source file.** Its first ~8
  pages are tagged AIEEE 2009–2011 and JEE (Main) 2013–2021 questions. QE L4 is built
  from these, each carrying its year tag. No external book needed.
- **Sequences & Series: check the same way** — look at the first pages of its source
  file before reaching for the big books.
- **Surds: no PYQ chapter exists** in any of the three PYQ books on Teja's Desktop.
  Verified against Arihant's 26-chapter contents, MTG's Class-XI contents, and a
  full-text sweep of Arihant. Surds L4 is therefore 18 of the hardest remaining
  source items plus 7 JEE-pattern questions written for the purpose, and the paper
  says so.
- **Logarithms: same gap**, same treatment. (Arihant's text layer is useless for
  maths anyway — 102 `√` glyphs across 658 pages — so content search won't find them.)

The three PYQ books (`PYQ's/` on his Desktop: Arihant 658 pp, MTG 1112 pp, PW 1002 pp)
are **not in this repo** — 651 MB and 260 MB are too large.

---

## 6. What is in this repo

```
CLAUDE.md                  this file
README.md
syllabus/                  G8 CPT-01 syllabus image
source-pdfs/               the four scraped question sets, as supplied
source-pages/              every page of all four, rendered to PNG (110 dpi, 962 pages)
01-Surds/                  papers/  keys/  solutions/  src/
02-Logarithms/             papers/  keys/  solutions/  src/
03-Quadratic-Equations/    papers/  keys/  solutions/  src/
04-Sequences-and-Series/   papers/  keys/  solutions/  src/
tools/mkaudit.py           dumps built papers back to LaTeX blocks for the audit pass
tools/audit/               those dumps, plus the flat keys to paste into the prompt
```

---

## 7. STATUS

| Chapter | L1 | L2 | L3 | L4 | Keys | Solutions | Audited |
|---|---|---|---|---|---|---|---|
| 01 Surds | 25 ✅ | 25 ✅ | 25 ✅ | 25 ✅ *(JEE-pattern — no PYQ source)* | ✅ | **TODO** | ✅ clean |
| 02 Logarithms | 25 ✅ | 25 ✅ | 25 ✅ | 25 ✅ *(JEE-pattern — no PYQ source)* | ✅ | **TODO** | ✅ clean |
| 03 Quadratic Equations | 15 ⚠️ | 15 ⚠️ | 15 ⚠️ | 25 ✅ *(real AIEEE/JEE-Main PYQs)* | ✅ | **TODO** | **TODO** |
| 04 Sequences & Series | **TODO** | **TODO** | **TODO** | **TODO** | **TODO** | **TODO** | **TODO** |

⚠️ = first draft, short of the 25 target. All keys in it are verified; there are just
not enough questions yet.

### Next actions, in order

1. **Finish Quadratic Equations L1–L3.** They currently hold 15 each; the target is
   25. ~30 more items are needed. The harvested pages so far are **14–19** (clean
   four-option questions, ~24 per page, the best ground in the file). Pages 20–29 and
   32–60 are the obvious next sweep. Apply the §2 exclusions — this chapter has the
   most cuts, especially location-of-roots, which is everywhere in the later pages.
   **Also check against the 75 questions already issued to this batch** in Teja's
   earlier three hell-difficulty QE assignments; those came from a different set of
   nine PDFs, so overlap is possible.
2. **Sequences & Series, all four levels, from scratch** (419 pp, 999 questions in
   `source-pages/04-Sequences-and-Series/`). Nothing has been read yet. Check its
   opening pages for tagged PYQs first — QE had them, so this one may too. Exclusions
   for this chapter are the heaviest: AGP, sigma notation, Vn method, telescopic
   series, and maxima/minima without calculus all come out.
3. **Run the pass-4 subagent audit** on Quadratic Equations and on Sequences & Series
   before shipping either.
4. **Detailed-solutions PDFs for all four chapters.** Not started for any of them.
   Teja's earlier QE project produced these as `sol*.py` files holding
   `SOL = [(qno, "ANS", r"latex body"), ...]`, built by a `buildsol.py` that refuses
   to compile if any stated answer disagrees with the key. Reuse that shape — the
   cross-check at build time is the point.

### Housekeeping owed

A `_preview/` folder of rendered page images was left inside
`~/Desktop/QUESTIONS 1ST DRAFT/`. Deleting inside a connected folder needs
`device_request_delete_permission`; if that is declined, move it to `_to_delete/`
and tell him.

---

## 8. Delivery

Deliver PDFs with `SendUserFile` **and** write them into
`~/Desktop/QUESTIONS 1ST DRAFT/Redesigned/<Chapter>/` on his Mac when the desktop app
is linked, as well as into this repo.

Tell him plainly about every question discarded and every one reconstructed. He cares
about that more than about the papers looking finished.

**Pushing:** this repo could not be pushed from the container — the agent proxy
refuses to inject a credential for a repository that is not in the session's
authorized set. The workaround is `push-to-github.sh` at the repo root, which Teja
runs on his own machine. If a future session *can* push, just push.
