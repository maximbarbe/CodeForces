n,m = map(int, input().split())
grid = [[0]* n for i in range(n)]
for i in range(n):
    grid[i][i] = m
for row in grid:
    print(*row)