# 05 — Integrated Papers (JEE Main pattern)

Mixed-chapter papers across Surds, Logarithms, Sequences & Series and Quadratic
Equations for the PRAGYA G8 Achievers batch.

| Paper | File | Zero report |
|---|---|---|
| Integrated Paper – I (Main) | `papers/Paper_I_MAIN.pdf` | `keys/Paper_I_MAIN_Zero_Report.pdf` |
| Integrated Paper – II (Advanced) | `papers/Paper_II_ADVANCED.pdf` | `keys/Paper_II_ADVANCED_Zero_Report.pdf` |

`papers/_superseded_Hell_Paper_*.pdf` are the 27 Sep 2026 versions these replace
("Hell" tag, tagline and marking boxes removed; Q10 wording, Q19 notation, page
breaks and answer-letter clustering fixed in Paper I; Q14 tightened and Q12 page break fixed in
Paper II — see each zero report).

`src/`: `bank.py` (questions + keys), `verify.py` (pass 1: brute force from each
statement), `verify2.py` (pass 2: exact arithmetic along the hand method),
`build.py` (pass 3 key re-check after option swaps; builds paper + zero report).
Pass 4 was a blind re-solve by a separate agent: all 25 agreed.

Rebuild: `cd src && python3 verify.py && python3 verify2.py && python3 build.py "<audit line>"`

Paper II uses `bank_p2.py`, `verify_p2.py`, `verify2_p2.py`, `build_p2.py` (same four passes;
`numsolve.py` holds the shared root scanner).
