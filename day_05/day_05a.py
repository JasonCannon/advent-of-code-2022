import sys

Lines = list(map(lambda x: x.strip('\n'), sys.stdin.readlines()))
idx = Lines.index('')

N = int(Lines[idx-1].split()[-1])
Stacks = [[] for _ in range(N)]

for i in range(idx-2, -1, -1):
    for j in range(N):
        val = Lines[i][1 + 4*j]
        if val != ' ':
            Stacks[j].append(val)

for i in range(idx+1, len(Lines)):
    cmd = Lines[i].split()
    amt, fr, to = int(cmd[1]), int(cmd[3]) - 1, int(cmd[5]) - 1
    Stacks[to] +=  Stacks[fr][:-amt-1:-1]
    del Stacks[fr][-amt:]

print(''.join(S[-1] if S else '' for S in Stacks))
