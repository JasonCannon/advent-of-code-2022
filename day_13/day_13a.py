import sys

Lines = [line.strip() for line in sys.stdin.readlines()]
Pairs = [tuple(map(eval, Lines[i:i+2])) for i in range(0, len(Lines), 3)]

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

print(sum(i + 1 for i in range(len(Pairs)) if cmp(Pairs[i][0], Pairs[i][1]) < 0))
