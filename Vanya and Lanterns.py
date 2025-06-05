n, l = map(int, input().split())
vals = [*map(int, input().split())]
vals.sort()
max_radius = 0
for i in range(len(vals) - 1):
    if (vals[i + 1] - vals[i])/2 > max_radius:
        max_radius = (vals[i + 1] - vals[i])/2
print(max(max_radius, vals[0], l - vals[-1]))
