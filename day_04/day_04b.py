import sys

cnt = 0

for p1, p2 in map(lambda x: x.strip().split(','), sys.stdin.readlines()):
    a1, b1 = map(int, p1.split('-'))
    a2, b2 = map(int, p2.split('-'))
    cnt += (a2 <= a1 <= b2) or (a2 <= b1 <= b2) or (a1 <= a2 <= b1) or (a1 <= b2 <= b1)

print(cnt)
