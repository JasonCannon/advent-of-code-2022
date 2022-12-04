import sys, string

sm, Alphabet = 0, string.ascii_lowercase + string.ascii_uppercase

for line in map(lambda x: x.strip(), sys.stdin.readlines()):
    S = set(line[:len(line)//2]).intersection(set(line[len(line)//2:]))
    sm += 1 + Alphabet.index(*S)

print(sm)
