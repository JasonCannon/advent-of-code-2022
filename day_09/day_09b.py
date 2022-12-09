import sys

sgn = lambda x: (x > 0) - (x < 0)
R = [(0, 0) for _ in range(10)]
D, Seen = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}, {R[-1]}

for args in map(lambda x: x.strip().split(), sys.stdin.readlines()):
    d, v = args[0], int(args[1])
    for _ in range(v):
        R[0] = tuple(sum(x) for x in zip(R[0], D[d]))
        for i in range(1, len(R)):
            dx, dy = R[i-1][0] - R[i][0], R[i-1][1] - R[i][1]
            if abs(dx) > 1 or abs(dy) > 1:
                R[i] = tuple(sum(x) for x in zip(R[i], [sgn(dx), sgn(dy)]))
        Seen.add(R[-1])

print(len(Seen))
