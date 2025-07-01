n,s = map(int, input().split())
floors = []
for i in range(n):
    f, t = map(int, input().split())
    floors.append((f, t))
floors.sort(key=lambda el:-el[0])
res = 0
cur = s
for f, t in floors:
    res += cur - f
    cur = f
    if t > res:
        res = t
print(res + cur)