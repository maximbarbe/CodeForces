from math import inf
from collections import deque
n = int(input())
a = [*map(int, input().split())]
m = int(input())
b = [*map(int, input().split())]
res = 0
a.sort()
b.sort()
for i in range(n):
    for j in range(m):
        if abs(a[i] - b[j]) <= 1:
            res += 1
            b[j] = inf
            break
print(res)