import sys
from collections import defaultdict
from functools import lru_cache

Lines = list(map(lambda x: x.strip().split(), sys.stdin.readlines()))
Dirs, path, idx = defaultdict(set), "", 0

while idx < len(Lines):
    if Lines[idx][1] == "cd":
        if Lines[idx][2] == '/': path = '/'
        elif Lines[idx][2] == "..": path = path[:path[:-1].rindex('/')+1]
        else: path += f"{Lines[idx][2]}/"
        idx += 1
    elif Lines[idx][1] == "ls":
        S, idx = set(), idx + 1
        while idx < len(Lines) and Lines[idx][0] != '$':
            S.add((Lines[idx][1], Lines[idx][0]))
            idx += 1
        Dirs[path] = Dirs[path].union(S)

@lru_cache(maxsize=None)
def get_dir_size(s):
    sz = 0
    for k, v in Dirs[s]:
        if v == "dir": sz += get_dir_size(s + f"{k}/")
        else: sz += int(v)
    return sz

print(sum([get_dir_size(k) for k in Dirs if get_dir_size(k) <= 100000]))
