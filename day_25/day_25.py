import sys

L, sym = list(map(lambda x: x.strip(), sys.stdin.readlines())), "=-012"

def to_SNAFU(x):
    out = ''
    while x:
        x, idx = divmod(x + 2, 5)
        out += sym[idx]
    return out[::-1]

def from_SANFU(s):
    return sum(5**i * (sym.index(c) - 2) for i, c in enumerate(s[::-1]))

print(to_SNAFU(sum(from_SANFU(l) for l in L)))
