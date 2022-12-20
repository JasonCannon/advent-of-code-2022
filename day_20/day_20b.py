import sys
from collections import deque

L = [(i, 811589153*x) for i, x in enumerate(map(int, sys.stdin.readlines()))]
Q, e = deque(L), next(x for x in L if not x[1])

for _ in range(10):
    for x in L:
        Q.rotate(len(Q)-Q.index(x)-1)
        Q.pop()
        Q.rotate(-x[1]%len(Q))
        Q.append(x)

idx = Q.index(e)
print(sum(Q[(idx + i)%len(Q)][1] for i in [1000, 2000, 3000]))
