n = int(input())
vals = [*map(int, input().split())]
res = []
seen =set()
for i in range(len(vals) - 1, -1, -1):
    if vals[i] not in seen:
        res.append(vals[i])
        seen.add(vals[i])
print(len(res))
print(*res[::-1])