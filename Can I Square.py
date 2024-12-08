from math import sqrt, floor

t = int(input())
for _ in range(t):
    n = int(input())
    res = sum([*map(int, input().split())])
    if floor(sqrt(res))**2 == res:
        print('YES')
    else:
        print('NO')