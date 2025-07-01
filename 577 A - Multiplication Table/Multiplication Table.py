from math import sqrt
n,x=map(int, input().split())
if x > n**2:
    print(0)
    exit()
res = 0
for i in range(1, int(sqrt(x)) + 1):
    if x % i == 0:
        first = i
        sec = x//i
        if first <= n and sec <= n:
            if first != sec:
                res += 2
            else:
                res += 1
print(res)