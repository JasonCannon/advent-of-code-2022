import sys

tot = 0

for s1, s2 in map(lambda x: x.split(), sys.stdin.readlines()):
    x, y = ord(s1)-ord('A'), ord(s2)-ord('X')
    tot += (y + 1) + 3*int(x == y) + 6*int((y - 1)%3 == x)

print(tot)