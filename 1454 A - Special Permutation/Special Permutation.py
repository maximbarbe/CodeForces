t =int(input())
for i in range(t):
    n = int(input())
    res = [i for i in range(2, n+1)] + [1]
    print(*res)
        