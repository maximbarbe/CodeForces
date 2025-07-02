from math import floor

t = int(input())

def get_k(n, x):
    return floor(n/x)

def f(x, k):
    return x*k*(k + 1)/2

for i in range(t):
    n = int(input())
    maximum = 0
    res = None
    for x in range(2, n+1):
        k = get_k(n, x)
        if k == 0:
            break
        cur = f(x, k)
        if cur > maximum:
            maximum = cur
            res = x
    print(res)