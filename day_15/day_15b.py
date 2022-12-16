import sys, re
from collections import defaultdict

pattern = "Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
L = [tuple(map(int, x)) for x in re.findall(pattern, sys.stdin.read())]

def merge(L):
    idx, L = 0, sorted(L)
    for p in L:
        if L[idx][1] >= p[0]: L[idx] = (L[idx][0], max(L[idx][1], p[1]))
        else: idx, L[idx] = idx+1, p
    return L[:idx+1]

mn, mx, Intervals = 0, 4000000, defaultdict(list)
for x1, y1, x2, y2 in L:
    d = abs(x2 - x1) + abs(y2 - y1)
    for row in range(-d, d+1): Intervals[y1+row].append((x1-(d-abs(row)), x1+(d-abs(row))))

for y in Intervals:
    I = merge(Intervals[y])
    I[0], I[-1] = (max(mn, I[0][0]), max(mn, I[0][1])), (min(mx, I[-1][0]), min(mx, I[-1][1]))

    if mn <= y <= mx and sum(1+x2-x1 for x1, x2 in I) <= mx:
        x = next(I[i][0] - 1 for i in range(1, len(I)) if I[i][0] - I[i-1][1] > 1)
        print(4000000*x + y)
        break
