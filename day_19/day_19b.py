import sys, re
from math import prod

pattern = "Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian."
L = [tuple(map(int, x)) for x in re.findall(pattern, sys.stdin.read())][:3]
Blueprints = {x[0]: (
    ((x[1], 0, 0, 0), (1, 0, 0, 0)), 
    ((x[2], 0, 0, 0), (0, 1, 0, 0)), 
    ((x[3], x[4], 0, 0), (0, 0, 1, 0)), 
    ((x[5], 0, x[6], 0), (0, 0, 0, 1)),
    ((0, 0, 0, 0), (0, 0, 0, 0))
    ) for x in L}

def solve(B):
    Q = [[[0, 0, 0, 0], [1, 0, 0, 0]]]
    for t in range(32):
        Q_tmp = []
        for quan, prod in Q:
            for cost, inc in B:
                quan_cost = [x - y for x, y in zip(quan, cost)]
                if all(x >= 0 for x in quan_cost):
                    prod_inc = [sum(x) for x in zip(prod, inc)]
                    Q_tmp.append([[sum(x) for x in zip(quan_cost, prod)], prod_inc])
        Q_tmp.sort(key = lambda x: tuple((b, a) for a, b in zip(*map(reversed, x))), reverse = True)
        Q = Q_tmp[:5000]
    return max(quan[3] for quan, prod in Q)

print(prod(solve(Blueprints[ID]) for ID in Blueprints))