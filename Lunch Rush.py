from math import inf
n, k = map(int, input().split())
maximum = -inf
for i in range(n):
    f, t = map(int, input().split())
    maximum = max(maximum, f - (t-k) if t > k else f)
print(maximum)