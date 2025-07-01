n = int(input())
h = [*map(int, input().split())]
res = 0
cur = 0
energy = 0
for v in h:
    diff = cur - v
    if energy + diff < 0:
        res += abs(energy + diff)
        energy = 0
    else:
        energy += diff
    cur = v
print(res)