from collections import defaultdict
from itertools import product

Jets = input()
Rocks = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]],
         [[0, 0, 0, 0], [0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0]],
         [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0]],
         [[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]],
         [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 0, 0], [1, 1, 0, 0]]]
G = defaultdict(int)

def can_move(idx, x, y, dx, dy):
    x, y = x + dx, y + dy
    for r, c in product(range(4), repeat = 2):
        if Rocks[idx][r][c]:
            tmp_x, tmp_y = x + c, y + (3 - r)
            if tmp_y <= 0 or tmp_x <= 0 or tmp_x > 7 or G[tmp_x, tmp_y]: return False
    return (x, y)

height, j_idx = 0, 0
for i in range(2022):
    x, y, ticks = 3, height + 4, 0

    while True:
        if ticks % 2:
            if can_move(i%len(Rocks), x, y, 0, -1): y -= 1
            else: break
        else:
            d = (1, 0) if Jets[j_idx%len(Jets)] == '>' else (-1, 0)
            res = can_move(i%len(Rocks), x, y, *d)
            if res: x, y = res
            j_idx += 1
        ticks += 1
    
    for r, c in product(range(4), repeat = 2):
        if Rocks[i%len(Rocks)][r][c]:
            tmp_x, tmp_y = x + c, y + (3 - r)
            G[tmp_x, tmp_y] = 1
            height = max(height, tmp_y)

print(height)
