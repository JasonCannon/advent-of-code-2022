import sys
from collections import deque

L = [line.strip() for line in sys.stdin.readlines()]
G = [[44]*(len(L[0]) + 2)] + [[44] + [ord(c) - ord('a') if c.islower() else c for c in line] + [44] for line in L] + [[44]*(len(L[0]) + 2)]

seen, Q = set(), deque()
for i in range(len(G)):
    for j in range(len(G[0])):
        if G[i][j] == 'S': start, G[i][j] = (i, j), 0
        if G[i][j] == 'E': end, G[i][j] = (i, j), 25
        if G[i][j] == 0: Q.append((0, (i, j)))

while len(Q):
    dist, curr = Q.popleft()
    if curr in seen: continue
    seen.add(curr)
    if curr == end:
        print(dist)
        break
    for dr in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        next = tuple(sum(x) for x in zip(curr, dr))
        if G[curr[0]][curr[1]] + 1 >= G[next[0]][next[1]]: Q.append((dist + 1, next))
