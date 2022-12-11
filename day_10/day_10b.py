import sys

X, cycle, L = 1, 0, []
G = [['.' for j in range(40)] for i in range(6)]

for args in map(lambda x: x.strip().split(), sys.stdin.readlines()):
    match args:
        case ["addx", val]: L.append((cycle + 2, int(val)))
        case ["noop"]: L.append((cycle + 1, 0))
    while len(L):
        if X - 1 <= cycle % 40 <= X + 1:  G[cycle//40][cycle%40] = '#'
        cycle += 1
        if cycle >= L[0][0]: X += L.pop()[1]

print('\n'.join([''.join(R) for R in G]))