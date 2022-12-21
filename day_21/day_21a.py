import sys, re
import operator as op
from functools import cache

pattern = "(.+): (.+)"
D = {k: int(v) if v.isdigit() else v for k, v in re.findall(pattern, sys.stdin.read())}
ops = {'+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv}

@cache
def solve(r):
    if isinstance(D[r], int): return D[r]
    a, s, b = D[r].split()
    return ops[s](solve(a), solve(b))

print(int(solve("root")))
