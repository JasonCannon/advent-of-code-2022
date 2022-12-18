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

found_cycle = False
Rows, States = defaultdict(set), dict()
height, j_idx, inc = [0]*3
tot_rocks, i = 1000000000000, -1

while (i := i + 1) < tot_rocks:
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
            Rows[tmp_y].add(tmp_x)
            height = max(height, tmp_y)
    
    Hash = (tuple(tuple(sorted(Rows[height - i])) for i in range(32) if height - i >= 0), i % len(Rocks), j_idx % len(Jets))
    if not found_cycle:
        if Hash in States:
            num_rocks = i - States[Hash][0]
            num_cycles = (tot_rocks - i)//num_rocks
            tot_rocks -= num_rocks*num_cycles
            inc, found_cycle = (height - States[Hash][1])*num_cycles, True
        else: States[Hash] = (i, height)

print(height + inc)
