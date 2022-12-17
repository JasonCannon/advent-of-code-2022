import sys, re
from collections import defaultdict

pattern = "Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z]+[, [A-Z]+]*)"
L = [(v, int(f), set(map(lambda x: x.strip(), t.split(',')))) for v, f, t in re.findall(pattern, sys.stdin.read())]

inf, D = 0x3f3f3f3f, defaultdict(lambda: defaultdict(lambda: inf))
Valves, Vertices = {v:int(f) for v, f, _ in L}, []

for v, f, N in L:
    D[v][v] = 0
    for u in N: D[v][u] = 1
    if f > 0: Vertices.append(v)

# Floyd-Warshall
for k in Valves:
    for i in Valves:
        for j in Valves:
            D[i][j] = min(D[i][j], D[i][k] + D[k][j])

Paths, Feasible = [], []
def dfs(curr, t):
    Paths.append(curr)
    ignore = set(curr)
    for v in filter(lambda x: x not in ignore, Vertices):
        rem = t - (1 + D[curr[-1]][v])
        if rem >= 0: dfs((*curr, v), rem)

dfs(('AA',), 26)
for P in Paths:
    v, t, amt = P[0], 26, 0
    for u in P[1::]:
        t -= 1 + D[v][u]
        amt += t*Valves[u]
        v = u
    Feasible.append((amt, set(P[1::])))

Feasible.sort(reverse = True)
best = 0
for i in range(len(Paths)):
    if Feasible[i][0] + Feasible[i + 1][0] < best: break
    mx = next((Feasible[j][0] for j in range(i + 1, len(Paths)) if Feasible[i][1].isdisjoint(Feasible[j][1])), 0)
    best = max(best, Feasible[i][0] + mx)

print(best)
