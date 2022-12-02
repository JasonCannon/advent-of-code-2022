import sys

tot = 0
for s1, s2 in map(lambda x: x.split(), sys.stdin.readlines()):
    x, y = ord(s1)-ord('A'), ord(s2)-ord('X')
    tot += int(y == 0)*(1 + (x - 1)%3) + int(y == 1)*(x + 4) + int(y == 2)*(7 + (x + 1)%3)

print(tot)