from math import gcd

l, r = map(int, input().split())
for i in range(l, r-1):
    for j in range(i + 1, r):
        for k in range(j + 1, r + 1):
            if gcd(i, j) == 1 and gcd(j, k) == 1 and gcd(i, k) != 1:
                print(i, j, k)
                exit()
else:
    print(-1)