import sys

n, Elves = 1, [0]
for line in map(lambda x : x.strip(), sys.stdin.readlines()):
    if line: Elves[n - 1] += int(line)
    else: n, Elves = n + 1, Elves + [0]

print(max(Elves))