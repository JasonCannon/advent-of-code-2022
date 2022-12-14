import sys

sgn = lambda x: (x > 0) - (x < 0)
Blocked, Sand = set(), set()

def update(p, floor):
    for q in [(p[0], p[1]+1), (p[0]-1, p[1]+1), (p[0]+1, p[1]+1)]:
        if q not in Blocked and q not in Sand and q[1] < floor: return q
    return None

for line in sys.stdin.readlines():
    P = [tuple(map(int, x.split(','))) for x in line.split('->')]
    for i in range(1, len(P)):
        curr, dx, dy = P[i-1], sgn(P[i][0] - P[i-1][0]), sgn(P[i][1] - P[i-1][1])
        Blocked.add(curr)
        while curr != P[i]:
            curr = (curr[0] + dx, curr[1] + dy)
            Blocked.add(curr)

floor = 2 + max(y for x, y in Blocked)
while True:
    p, q = (500, 0), update((500, 0), floor)
    if not q: break
    while q: p, q = q, update(q, floor)
    Sand.add(p)

print(1 + len(Sand))
