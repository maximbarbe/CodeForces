t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    n = 2*(max(b, a) - min(b, a))
    if n < max(a, b):
        print(-1)
        continue
    if c > n:
        print(-1)
    else:
        if c > n//2:
            d = c - n//2
        else:
            d = c + n//2
        if d in [a, b]:
            print(-1)
        else:
            print(d)