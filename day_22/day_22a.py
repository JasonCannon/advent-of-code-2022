import sys, re

L = [l.strip('\n') for l in sys.stdin.readlines()]
n = 2 + next(i for i in range(len(L)) if not L[i])
m = 2 + max(len(L[i]) for i in range(n-2))

G, D = [[' ']*m] + [[' ']+list(f"{L[i]: <{m-1}}") for i in range(n-2)] + [[' ']*m], [(0, 1), (1, 0), (0, -1), (-1, 0)]
R = [(next((c for c in range(m) if G[r][c] != ' '), None), next((c for c in range(m-1,-1,-1) if G[r][c] != ' '), None))  for r in range(n)]
C = [(next((r for r in range(n) if G[r][c] != ' '), None), next((r for r in range(n-1,-1,-1) if G[r][c] != ' '), None))  for c in range(m)]
path = [s if s.isalpha() else int(s) for s in re.findall("(\d+|R|L)", L[-1])]

def move(pos, dr):
    r, c = tuple(sum(x) for x in zip(pos, D[dr]))
    if G[r][c] == ' ':
        if dr % 2: r = C[c][0 if dr == 1 else 1]
        else: c = R[r][0 if dr == 0 else 1]
    return (r, c) if G[r][c] == '.' else False

curr, dir = (1, next(c for c in range(m) if G[1][c] == '.')), 0
for p in path:
    if isinstance(p, str): dir = (dir + (1 if p == 'R' else -1)) % len(D)
    else:
        for _ in range(p):
            step = move(curr, dir)
            if not step: break
            curr = step

print(1000*curr[0] + 4*curr[1] + dir)
