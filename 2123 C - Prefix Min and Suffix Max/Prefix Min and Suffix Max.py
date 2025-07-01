from math import inf
 
t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    minimums = [None]*n
    maximums = [None]*n
    for j in range(len(vals)):
        if j == 0:
            minimums[j] = vals[j]
        else:
            minimums[j] = min(minimums[j - 1], vals[j])
        
    for j in range(len(vals) - 1, -1, -1):
        if j == len(vals) - 1:
            maximums[j] = vals[j]
        else:
            maximums[j] = max(maximums[j + 1], vals[j])
    res = []
    minimums = [-inf] + minimums
    maximums = maximums + [inf]
    for i in range(1, n+1):
        if (vals[i - 1] >= minimums[i] and vals[i - 1] == maximums[i -1]) or (vals[i - 1] <= maximums[i] and vals[i - 1] == minimums[i]):
            res.append("1")
        else:
            res.append("0")
    print("".join(res))