n, k = map(int, input().split())
vals = [*map(int, input().split())]
vals = [(vals[i], i) for i in range(len(vals))]
vals = sorted(vals, key=lambda el:el[0])
cur = 0
inst = []
res = 0
for (v, i) in vals:
    if cur + v <= k:
        res += 1
        cur += v
        inst.append(i+1)
print(res)
if res:
    print(*inst)