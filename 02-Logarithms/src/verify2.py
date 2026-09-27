# -*- coding: utf-8 -*-
"""Second verification pass for the logarithms bank: every numeric literal is
re-read as a 60-digit Decimal and every logarithm/root recomputed with
Decimal.ln()/sqrt().  Items whose check is a structural lambda (no Decimal
path) are reported separately so they can be re-derived by hand."""
import ast, decimal, types, math
from decimal import Decimal as D
decimal.getcontext().prec = 60

def dlog(x, b=None):
    v = D(x).ln()
    return v if b is None else v / D(b).ln()

def dsqrt(x):
    return D(x).sqrt()

def dfloor(x):
    return int(math.floor(float(x))) if not isinstance(x, D) else int(x.to_integral_value(rounding=decimal.ROUND_FLOOR))

class ToDecimal(ast.NodeTransformer):
    def visit_Call(self, node):
        if isinstance(node.func, ast.Name) and node.func.id in ('range', 'str', 'int', 'round', 'len'):
            for a in node.args:
                if not isinstance(a, ast.Constant):
                    self.visit(a)
            return node
        return self.generic_visit(node)
    def visit_Subscript(self, node):
        self.visit(node.value)          # leave index literals alone
        return node
    def visit_Constant(self, node):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            return node
        return ast.Call(func=ast.Name(id='D', ctx=ast.Load()),
                        args=[ast.Constant(value=repr(node.value))], keywords=[])

src = open('bank.py').read().replace('from math import log, sqrt, floor', '')
tree = ToDecimal().visit(ast.parse(src, 'bank.py[dec]'))
ast.fix_missing_locations(tree)
mod = types.ModuleType('dbank')
mod.__dict__.update(log=dlog, sqrt=dsqrt, floor=dfloor, D=D)
exec(compile(tree, 'bank.py[dec]', 'exec'), mod.__dict__)

TOL = D('1e-25')
fails, skipped, done = [], [], 0
for qid in sorted(mod.Q, key=int):
    e = dict(mod.Q[qid]); e['ans'] = int(e['ans'])
    if e['truth'] is None:
        try:
            ok = bool(e['chk']())
        except Exception as ex:
            skipped.append((qid, type(ex).__name__)); continue
        done += 1
        if not ok:
            fails.append((qid, 'structural check false under decimal'))
        continue
    try:
        t = D(e['truth']())
        vals = [D(f()) for f in e['optvals']]
    except Exception as ex:
        skipped.append((qid, type(ex).__name__)); continue
    done += 1
    match = [i for i, v in enumerate(vals) if abs(v - t) < TOL * max(D(1), abs(t))]
    if match != [e['ans']]:
        fails.append((qid, 'true=%s matching=%s key=%d' % (str(+t)[:26], match, e['ans'])))

print('re-checked in 60-digit decimal: %d / %d' % (done, len(mod.Q)))
print('FAILURES: %d' % len(fails))
for f in fails:
    print('   Q%-5s %s' % f)
print('not expressible in the decimal path (need hand re-derivation): %s'
      % sorted(q for q, _ in skipped))
