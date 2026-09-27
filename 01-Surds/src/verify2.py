# -*- coding: utf-8 -*-
"""Second, independent verification pass.

Re-executes bank.py after an AST transform that turns EVERY numeric literal
into a 60-significant-digit Decimal, and replaces the float sqrt/cbrt/rt with
Decimal versions (Newton iteration for n-th roots).  Nothing in this pass
shares an arithmetic path with verify.py, so it is a genuine second opinion —
it matters for the nested-radical items where float cancellation eats 12 of
the 16 significant digits.
"""
import ast, decimal, types
from decimal import Decimal as D
decimal.getcontext().prec = 60

def dsqrt(x):
    x = D(x)
    return x.sqrt()

def _nroot(x, n):
    n = int(n)
    x = D(x)
    neg = x < 0
    if neg:
        x = -x
    if x == 0:
        return D(0)
    g = D(repr(float(x) ** (1.0 / n)))
    for _ in range(200):
        gn = ((n - 1) * g + x / g ** (n - 1)) / n
        if gn == g:
            break
        g = gn
    return -g if neg else g

dcbrt = lambda x: _nroot(x, 3)
drt = lambda x, n: _nroot(x, n)

class ToDecimal(ast.NodeTransformer):
    """Wrap every numeric literal in D('...'), except inside range()."""
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id == 'range':
            node.args = [a for a in node.args]      # leave range() ints alone
            return node
        return self.generic_visit(node)

    def visit_Constant(self, node):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            return node
        return ast.Call(func=ast.Name(id='D', ctx=ast.Load()),
                        args=[ast.Constant(value=repr(node.value))], keywords=[])

src = open('/home/claude/surds/bank.py').read()
src = src.replace('from math import sqrt', '')
src = src.replace('def cbrt(x):\n    return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))', '')
src = src.replace('def rt(x, n):\n    return x ** (1.0 / n) if x >= 0 else -((-x) ** (1.0 / n))', '')
src = src.replace('R2, R3, R5, R6, R7 = sqrt(2), sqrt(3), sqrt(5), sqrt(6), sqrt(7)',
                  'R2, R3, R5, R6, R7 = [sqrt(k) for k in (2, 3, 5, 6, 7)]')

tree = ToDecimal().visit(ast.parse(src, 'bank.py[decimal]'))
ast.fix_missing_locations(tree)

mod = types.ModuleType('dbank')
mod.__dict__.update(sqrt=dsqrt, cbrt=dcbrt, rt=drt, D=D)
exec(compile(tree, 'bank.py[decimal]', 'exec'), mod.__dict__)

TOL = D('1e-40')
fails = []
for qid in sorted(mod.Q, key=int):
    e = dict(mod.Q[qid]); e['ans'] = int(e['ans'])
    if e['chk'] is not None:
        try:
            ok = bool(e['chk']())
        except Exception as ex:
            fails.append((qid, 'chk raised %r' % (ex,))); continue
        if not ok:
            fails.append((qid, 'chk returned False under 60-digit arithmetic'))
        continue
    t = D(e['truth']())
    vals = [None if f is None else D(f()) for f in e['optvals']]
    match = [i for i, v in enumerate(vals)
             if v is not None and abs(v - t) < TOL * max(D(1), abs(t))]
    if e['optvals'][e['ans']] is None:
        if match:
            fails.append((qid, 'none-of-these key, but option %s matches' % match))
    elif match != [e['ans']]:
        fails.append((qid, 'true=%s  matching=%s  key=%d' % (str(+t)[:26], match, e['ans'])))

print('60-digit checks run: %d / %d' % (len(mod.Q), len(mod.Q)))
print('FAILURES: %d' % len(fails))
for f in fails:
    print('   Q%-4s %s' % f)
