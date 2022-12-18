import sys

L = [tuple(map(int, line.strip().split(','))) for line in sys.stdin.readlines()]
D = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
Cubes = set(L)

print(sum(tuple(a + b for a, b in zip(p, d)) not in Cubes for d in D for p in L))
