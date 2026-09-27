# -*- coding: utf-8 -*-
"""Independent check of every keyed answer in the surds bank."""
import sys
sys.path.insert(0, '/home/claude/logs')
import bank

fails, checked = [], 0
for qid in sorted(bank.Q):
    e = bank.Q[qid]
    if e['chk'] is not None:
        try:
            ok = bool(e['chk']())
        except Exception as ex:
            ok = False
            e = dict(e); e['err'] = repr(ex)
        checked += 1
        if not ok:
            fails.append((qid, 'chk returned False', e.get('err', '')))
        continue
    if e['truth'] is None:
        fails.append((qid, 'NO CHECK ATTACHED', ''))
        continue
    t = e['truth']()
    vals = []
    for f in e['optvals']:
        vals.append(None if f is None else f())
    # which options match the true value?
    match = [i for i, v in enumerate(vals)
             if v is not None and abs(v - t) < 1e-6 * max(1.0, abs(t))]
    checked += 1
    if e['optvals'][e['ans']] is None:      # "none of these" style key
        if match:
            fails.append((qid, 'key says none-of-these but option %s matches' % match, t))
    elif match != [e['ans']]:
        fails.append((qid, 'true=%.10g  matching options=%s  key=%d' % (t, match, e['ans']), vals))

print('questions with a check run:', checked, '/', len(bank.Q))
if fails:
    print('\nFAILURES (%d):' % len(fails))
    for f in fails:
        print('  Q%-4s %s   %s' % (f[0], f[1], f[2]))
else:
    print('\nALL KEYS VERIFIED — 0 failures')
