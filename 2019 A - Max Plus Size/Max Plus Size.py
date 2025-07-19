from math import inf

t = int(input())
for i in range(t):
    n = int(input())
    a = [*map(int, input().split())]
    res = 0
    for i in range(len(a)):
        res = max(res, a[i] + i//2+ (n-1-i)//2 + 1)
    print(res)