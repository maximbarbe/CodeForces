from itertools import combinations

n = int(input())
vals = []
for i in range(n):
    home, guest = map(int, input().split())
    vals.append((home, guest))
res = 0
for cmb in combinations(vals, 2):
    if cmb[0][0] == cmb[1][1]:
        res += 1
    if cmb[0][1] == cmb[1][0]:
        res += 1
print(res)