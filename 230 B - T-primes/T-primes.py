from functools import lru_cache


@lru_cache(None)
def res(v):
    if v == 1:
        return False
    s = v**0.5
    if int(s) != s:
        return False
    v = int(s)
    if v == 2:
        return True
    if v % 2 == 0:
        return False
    for x in range(3, int(v**0.5) + 1):
        if v % x == 0:
            return False
    return True
    

n = int(input())
vals = [*map(int, input().split())]
for v in vals:
    if res(v):
        print('YES')
    else:
        print('NO')