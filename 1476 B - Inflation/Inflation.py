from math import ceil

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    res = 0
    p = [*map(int, input().split())]
    prev = p[0]
    for i in range(1, len(p)):
        z = max(ceil((100*p[i])/k - prev), 0)
        res += z
        prev += z + p[i]
    print(res)