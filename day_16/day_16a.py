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

def dfs(curr, t):
    mx, ignore = 0, set(curr)
    for v in filter(lambda x: x not in ignore, Vertices):
        rem = t - (1 + D[curr[-1]][v])
        if rem >= 0: mx = max(mx, rem*Valves[v] + dfs((*curr, v), rem))
    return mx

print(dfs(('AA',), 30))
