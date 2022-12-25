import sys
from collections import defaultdict

L = list(map(lambda x: x.strip(), sys.stdin.readlines()))
Elves = {(i, j) for i in range(len(L)) for j in range(len(L[i])) if L[i][j] == '#'}
Dirs = ((-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1))
Order = (((0, 1, 7), 0), ((4, 3, 5), 4), ((6, 7, 5), 6), ((2, 1, 3), 2))
cw_add = lambda a, b: tuple(sum(x) for x in zip(a, b))

t = 0
while t := t + 1:
    Proposed, Count = [], defaultdict(int)
    for e in Elves:
        flag = True
        if any(cw_add(e, x) in Elves for x in Dirs):
            for i in range(len(Order)):
                checks, d = Order[(t + i - 1)%len(Order)]
                if all(cw_add(e, Dirs[x]) not in Elves for x in checks):
                    p = cw_add(e, Dirs[d])
                    Proposed.append((e, p))
                    Count[p] += 1
                    flag = False
                    break
        if flag: Proposed.append((e, None))
    tmp = {e if Count.get(p, 0) != 1 else p for e, p in Proposed}
    if Elves == tmp: break
    Elves = tmp

print(t)
