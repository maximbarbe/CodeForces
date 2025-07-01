def f(n):
    return (n*(n+1))//2

n, k = map(int, input().split())


if n == 1:
    print(0)
elif n <= k:
    print(1)
else: 
    n -= 1
    k -= 1
    if n > f(k):
        print(-1)
        exit()
    start = 1
    end = k
    while start != end:
        mid = (start + end)//2
        pipes = f(k) - f(mid - 1)
        if pipes == n:
            print(k - mid + 1)
            exit()
        if pipes > n:
            start = mid + 1
        else:
            end = mid
    print(k - start + 2)