t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    cur = 2023
    vals = [*map(int, input().split())]
    for v in vals:
        if cur % v != 0:
            print("NO")
            break
        cur //= v
    else:
        print("YES")
        res = [cur] + [1]*(k - 1)
        print(*res)