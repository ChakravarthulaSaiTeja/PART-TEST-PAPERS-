import os, re

def groups(s, i, n):
    """read n brace groups starting at s[i]=='{'"""
    out = []
    for _ in range(n):
        while s[i] != '{':
            i += 1
        d, j = 0, i
        while True:
            if s[j] == '{': d += 1
            elif s[j] == '}':
                d -= 1
                if d == 0: break
            j += 1
        out.append(s[i + 1:j]); i = j + 1
    return out, i

def audit(texdir, name):
    for lv in ('L1', 'L2', 'L3', 'L4'):
        s = open(os.path.join(texdir, '%s_%s.tex' % (name, lv))).read()
        s = s.split(r'\vspace{1mm}')[-1]
        items, i = [], 0
        while True:
            k = s.find('\\Q{', i)
            if k < 0: break
            (q,), j = groups(s, k + 2, 1)
            m = re.search(r'\\opt(Two|TwoTall|One)', s[j:j + 40])
            o, i = groups(s, j + m.end(), 4)
            items.append((q, o))
        assert len(items) == 25, (name, lv, len(items))
        open('/home/claude/check/%s_%s_audit.txt' % (name, lv), 'w').write(
            '\n\n'.join('Q%d. %s\n   (A) %s\n   (B) %s\n   (C) %s\n   (D) %s'
                        % (n, q, *o) for n, (q, o) in enumerate(items, 1)))
        print(name, lv, len(items))

audit('/home/claude/surds/out', 'Surds')
audit('/home/claude/logs/out', 'Logarithms')
