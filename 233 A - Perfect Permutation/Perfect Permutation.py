n = int(input())
if n % 2 == 1:
    print(-1)
else:
    vals = [i for i in range(1, n+1)]
    for i in range(0, n, 2):
        vals[i], vals[i + 1] =vals[i + 1], vals[i]
    print(*vals)