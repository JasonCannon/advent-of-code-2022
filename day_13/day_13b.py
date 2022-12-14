import sys
from functools import cmp_to_key

A, B = [[2]], [[6]]
Packets = [eval(line) for line in sys.stdin.readlines() if line != '\n'] + [A, B]

def cmp(A, B):
    if isinstance(A, int) != isinstance(B, int):
        A, B = A if isinstance(A, list) else [A], B if isinstance(B, list) else [B]
    if isinstance(A, int) and isinstance(B, int):
        return -1 if A < B else (1 if A > B else 0)
    else:
        for i in range(min(len(A), len(B))):
            res = cmp(A[i], B[i])
            if res: return res
        return -1 if len(A) < len(B) else (1 if len(A) > len(B) else 0)

Packets.sort(key=cmp_to_key(cmp))
print((Packets.index(A) + 1)*(Packets.index(B) + 1))