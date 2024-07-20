n = int(input())
vals = [*map(int, input().split())]
res = [None] * n
for i in range(len(vals)):

    res[vals[i] - 1] = i + 1
print(*res)