n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(input())
best = set()
for j in range(m):
    cur = set()
    maximum = 0
    for i in range(n):
        if int(grid[i][j]) > maximum:
            maximum = int(grid[i][j])
            cur = set([i])
        elif int(grid[i][j]) == maximum:
            cur.add(int(i))
    best = best.union(cur)
print(len(best))