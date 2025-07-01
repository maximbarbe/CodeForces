t = int(input())
for i in range(t):
    n = int(input())
    k = -1
    while 10**(k + 1) <= n:
        k += 1
    print(n - 10**k)