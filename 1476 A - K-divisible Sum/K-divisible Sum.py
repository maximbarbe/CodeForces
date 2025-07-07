from math import ceil

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    if n == k:
        print(1)
    elif k > n:
        print(ceil(k/n))
    else:
        if n%k == 0:
            print(1)
        else:
            print(2)