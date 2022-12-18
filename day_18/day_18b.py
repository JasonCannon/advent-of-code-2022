import sys
sys.setrecursionlimit(10000000)

L = [tuple(map(int, line.strip().split(','))) for line in sys.stdin.readlines()]
D = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
Cubes, Outside = set(L), set()

mn = (min(p[0] for p in L) - 4, min(p[1] for p in L) - 4, min(p[2] for p in L) - 4)
mx = (max(p[0] for p in L) + 4, max(p[1] for p in L) + 4, max(p[2] for p in L) + 4)

def flood_fill(p):
    if any(p[i] < mn[i] for i in range(3)) or any(p[i] > mx[i] for i in range(3)): return
    for d in D:
        q = tuple(a + b for a, b in zip(p, d))
        if q not in Outside and q not in Cubes:
            Outside.add(q)
            flood_fill(q)
flood_fill(mn)

print(sum(tuple(a + b for a, b in zip(p, d)) in Outside for d in D for p in L))
