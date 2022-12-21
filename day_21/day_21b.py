import sys, re
import operator as op
from functools import cache

pattern = "(.+): (.+)"
D = {k: int(v) if v.isdigit() else v for k, v in re.findall(pattern, sys.stdin.read())}
ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

@cache
def solve(r, val):
    if r == "humn": return val
    if isinstance(D[r], int): return D[r]
    a, s, b = D[r].split()
    return ops[s](solve(a, val), solve(b, val))

lhs, _, rhs = D["root"].split()
if abs(solve(rhs, 1) != solve(rhs, 0)): lhs, rhs = rhs, lhs

lo, hi = 0, int(1e32)
while lo < hi:
    mi = (lo + hi) // 2
    diff = solve(lhs, mi) - solve(rhs, 0)
    if diff < 0: hi = mi
    elif diff > 0: lo = mi
    else: break

print(mi)