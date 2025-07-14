from math import inf

t = int(input())
for i in range(t):
    n = int(input())
    m = -inf
    vals = [*map(int, input().split())]
    vals.sort()
    print(vals[-1] + sum(vals[:-1])/(n-1))
