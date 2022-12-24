import sys, re

L = [l.strip('\n') for l in sys.stdin.readlines()]
rows = next(i for i in range(len(L)) if not L[i])
cols = max(len(L[i]) for i in range(rows))

n, G, D = 50, [list(f"{L[i]: <{cols}}") for i in range(rows)], [(0, 1), (1, 0), (0, -1), (-1, 0)]
path = [s if s.isalpha() else int(s) for s in re.findall("(\d+|R|L)", L[-1])]

face_coords = [(1, 2), (1, 3), (2, 2), (3, 1), (3, 2), (4, 1)]
Faces = [[[' ']*(n+2)] + [[' '] + g[n*(c-1):n*c] + [' '] for g in G[n*(r-1):n*r]] + [[' ']*(n+2)] for r, c in face_coords]

EAST, SOUTH, WEST, NORTH = range(4)
Transitions = { # ((r, c), f_idx, dir)
    (0, EAST): lambda p: ((p[0], 1), 1, EAST), (0, SOUTH): lambda p: ((1, p[1]), 2, SOUTH),  (0, WEST): lambda p: ((n+1-p[0], 1), 3, EAST),  (0, NORTH): lambda p: ((p[1], 1), 5, EAST), # Face 0
    (1, EAST): lambda p: ((n+1-p[0], n), 4, WEST), (1, SOUTH): lambda p: ((p[1], n), 2, WEST), (1, WEST): lambda p: ((p[0], n), 0, WEST), (1, NORTH): lambda p: ((n, p[1]), 5, NORTH), # Face 1
    (2, EAST): lambda p: ((n, p[0]), 1, NORTH), (2, SOUTH): lambda p: ((1, p[1]), 4, SOUTH), (2, WEST): lambda p: ((1, p[0]), 3, SOUTH), (2, NORTH): lambda p: ((n, p[1]), 0, NORTH), # Face 2
    (3, EAST): lambda p: ((p[0], 1), 4, EAST), (3, SOUTH): lambda p: ((1, p[1]), 5, SOUTH), (3, WEST): lambda p: ((n+1-p[0], 1), 0, EAST), (3, NORTH): lambda p: ((p[1], 1), 2, EAST), # Face 3
    (4, EAST): lambda p: ((n+1-p[0], n), 1, WEST), (4, SOUTH): lambda p: ((p[1], n), 5, WEST), (4, WEST): lambda p: ((p[0], n), 3, WEST), (4, NORTH): lambda p: ((n, p[1]), 2, NORTH), # Face 4
    (5, EAST): lambda p: ((n, p[0]), 4, NORTH), (5, SOUTH): lambda p: ((1, p[1]), 1, SOUTH), (5, WEST): lambda p: ((1, p[0]), 0, SOUTH), (5, NORTH): lambda p: ((n, p[1]), 3, NORTH) # Face 5
}

def move(coords, f_idx, dr):
    p = tuple(sum(x) for x in zip(coords, D[dr]))
    if Faces[f_idx][p[0]][p[1]] == ' ':
        p, f_idx, dr = Transitions[f_idx, dr](coords)
    return (p, f_idx, dr) if Faces[f_idx][p[0]][p[1]] == '.' else False

curr, f_idx, dir = (1, next(c for c in range(n+2) if Faces[0][1][c] == '.')), 0, 0

for p in path:
    if isinstance(p, str): dir = (dir + (1 if p == 'R' else -1)) % len(D)
    else:
        for _ in range(p):
            step = move(curr, f_idx, dir)
            if not step: break
            curr, f_idx, dir = step

print(1000*(50*(face_coords[f_idx][0]-1) + curr[0]) + 4*(50*(face_coords[f_idx][1]-1) + curr[1]) + dir)
