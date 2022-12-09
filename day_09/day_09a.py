import sys

sgn = lambda x: (x > 0) - (x < 0)
h, t = (0, 0), (0, 0)
D, Seen = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}, {t}

for args in map(lambda x: x.strip().split(), sys.stdin.readlines()):
    d, v = args[0], int(args[1])
    for _ in range(v):
        h = tuple(sum(x) for x in zip(h, D[d]))
        dx, dy = h[0] - t[0], h[1] - t[1]
        if abs(dx) > 1 or abs(dy) > 1:
            t = tuple(sum(x) for x in zip(t, [sgn(dx), sgn(dy)]))
        Seen.add(t)

print(len(Seen))
