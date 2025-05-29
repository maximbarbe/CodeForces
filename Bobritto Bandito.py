t = int(input())
for i in range(t):
    n, m, l, r = map(int, input().split())
    for i in range(n-m):
        if l < 0:
            l += 1
        elif r > 0:
            r -= 1
    print(l, r)