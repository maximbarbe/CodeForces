from math import ceil

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    others = sorted(vals[1:])
    for v in others:
        diff = v - vals[0]
        if diff > 0:
            vals[0] += ceil(diff/2)
    print(vals[0])