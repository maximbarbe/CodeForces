t = int(input())
for i in range(t):
    n = int(input())
    if n % 2 == 0:
        print(-1)
    else:
        cur = [i for i in range(1, n+1)][::-1]
        print(*cur)