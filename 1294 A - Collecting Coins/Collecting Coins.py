t = int(input())
for i in range(t):
    a, b, c, n = map(int, input().split())
    m = max(a, b, c)
    p = 3*m - a - b - c
    if p > n or (n - p)%3 != 0:
        print("NO")
    else:
        print("YES") 