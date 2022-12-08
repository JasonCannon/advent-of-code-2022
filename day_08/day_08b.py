import sys
from itertools import accumulate, product

Lines = list(map(lambda x: x.strip(), sys.stdin.readlines()))
n = len(Lines[0])

G = [list(map(int, Lines[i][::])) for i in range(n)]
Gt = [*zip(*G)]

mx = 0

for r, c in product(range(1, n), repeat = 2):
    res = 1
    for A in [G[r][c-1::-1], G[r][c+1::], Gt[c][r-1::-1], Gt[c][r+1::]]:
        res *= len(A[:1+next((i for i, x in enumerate(A) if x >= G[r][c]), n)])
    mx = max(mx, res)

print(mx)