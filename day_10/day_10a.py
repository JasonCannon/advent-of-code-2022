import sys

X, cycle, sm, L = 1, 1, 0, []

for args in map(lambda x: x.strip().split(), sys.stdin.readlines()):
    match args:
        case ["addx", val]: L.append((cycle + 2, int(val)))
        case ["noop"]: L.append((cycle + 1, 0))
    while len(L):
        cycle += 1
        if cycle >= L[0][0]: X += L.pop()[1]
        if cycle in {20, 60, 100, 140, 180, 220}: sm += cycle*X

print(sm)