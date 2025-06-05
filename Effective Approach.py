n = int(input())
vals = [*map(int, input().split())]
indices = {vals[i]:i for i in range(len(vals))}
m = int(input())
b = [*map(int, input().split())]
r1 = r2 = 0
for v in b:
    if indices.get(v) == None:
        r1 += n
        r2 += n
    else:
        r1 += indices[v] + 1
        r2 += n - indices[v]
print(r1, r2)