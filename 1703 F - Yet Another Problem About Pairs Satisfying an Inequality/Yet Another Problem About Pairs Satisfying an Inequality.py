from bisect import bisect_right

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    res = 0
    indices = []
    for j in range(1, len(vals) + 1):
        if vals[j - 1] < j:
            indices.append(j)
    for idx in indices:
        val =  vals[idx - 1]
        res += bisect_right(indices, val - 1)
    print(res)