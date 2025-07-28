from bisect import bisect_left

n = int(input())
vals = [*map(int, input().split())]
prefix = [0]*n
for j in range(len(vals)):
    prefix[j] = prefix[j - 1] + vals[j]
m = int(input())
labels = [*map(int, input().split())]
for v in labels:
    print(bisect_left(prefix, v) + 1)