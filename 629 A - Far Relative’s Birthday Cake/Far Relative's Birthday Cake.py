n = int(input())
grid = []
res=0
for i in range(n):
    grid.append(input())
for i in range(n):
    for j in range(n-1):
        for k in range(j + 1, n):
            if grid[i][j] == grid[i][k] == "C":
                res += 1
for j in range(n):
    for i in range(n-1):
        for k in range(i+1, n):
            if grid[i][j] == grid[k][j] == "C":
                res += 1
print(res)