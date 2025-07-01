t = int(input())
for i in range(t):
    n, m, k = map(int, input().split())
    res = 0
    left = [*map(int, input().split())]
    right = [*map(int, input().split())]
    for v1 in left:
        for v2 in right:
            if v1 + v2 <= k:
                res += 1
    print(res)