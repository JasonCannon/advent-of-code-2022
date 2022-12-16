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

row, Intervals = 2000000, defaultdict(list)

for x1, y1, x2, y2 in L:
    rem = abs(x2 - x1) + abs(y2 - y1) - abs(y1 - row)
    if rem >= 0: Intervals[row].append((x1 - rem, x1 + rem))

print(sum(x2-x1 for x1, x2 in merge(Intervals[row])))
