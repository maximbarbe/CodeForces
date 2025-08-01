from math import ceil

t = int(input())
for i in range(t):
    res = 0
    l, r = map(int, input().split())
    while True:
        if l % 2 == 0:
            l += 1
        if l + 2 <= r:
            res += 1
            l += 4
        else:
            break
    print(res)    