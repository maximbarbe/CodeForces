n = int(input())
idx1, idx2 = None, None
minimum = 10**4
vals = [*map(int, input().split())]
for i in range(n):
    cur = abs(vals[i] - vals[(i + 1)%n])
    if cur < minimum:
        minimum = cur
        idx1 = i
        idx2 = (i + 1)%n
print(idx1 + 1, idx2 + 1)