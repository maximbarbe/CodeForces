n = int(input())
vals = [*map(int, input().split())]
for i in range(len(vals) - 2, -1, -1):
    for j in range(i, len(vals) - 1):
        if vals[j] > vals[j + 1]:
            diff = vals[j] -vals[j + 1]
            vals[j + 1] += diff
            vals[j] -= diff
            
print(*vals)