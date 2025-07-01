from collections import defaultdict
r, c = map(int, input().split())
eaten = defaultdict(lambda:False)
grid = []
for i in range(r):
    grid.append(input())
res=  0
for i in range(r):
    indices = set()
    s = False
    for j in range(c):
        if grid[i][j] == "S":
            s = True
            break
        else:
            indices.add((i, j))
    if s:
        continue
    else:
        for v in indices:
            if not eaten[v]:
                res += 1
            eaten[v] = True
for j in range(c):
    indices = set()
    s = False
    for i in range(r):
        if grid[i][j] == "S":
            s = True
            break
        else:
            indices.add((i, j))
    if s:
        continue
    else:
        for v in indices:
            if not eaten[v]:
                res += 1
            eaten[v] = True
print(res)
