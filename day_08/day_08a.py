import sys
from itertools import accumulate, product

Lines = list(map(lambda x: x.strip(), sys.stdin.readlines()))
n = len(Lines[0])

G = [[-1]*(n+2)] + [[-1]+list(map(int, Lines[i][::]))+[-1] for i in range(n)] + [[-1]*(n+2)]
Gt = [*zip(*G)]


L = [list(accumulate(G[i], max)) for i in range(n+2)]
R = [list(accumulate(G[i][::-1], max))[::-1] for i in range(n+2)]
U = [list(accumulate(Gt[i], max)) for i in range(n+2)]
D = [list(accumulate(Gt[i][::-1], max))[::-1] for i in range(n+2)]

cnt = 0
for r, c in product(range(1, n + 1), repeat = 2):
    cnt += G[r][c] > min(L[r][c - 1], R[r][c + 1], U[c][r - 1], D[c][r + 1])

print(cnt)