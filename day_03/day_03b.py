import sys, string

Lines = list(map(lambda x: set(x.strip()), sys.stdin.readlines()))
sm, Alphabet = 0, string.ascii_lowercase + string.ascii_uppercase

for i in range(0, len(Lines), 3):
    S = Lines[i].intersection(Lines[i+1]).intersection(Lines[i+2])
    sm += 1 + Alphabet.index(*S)

print(sm)
