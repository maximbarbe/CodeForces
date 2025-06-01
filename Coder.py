n = int(input())
grid = [["."]*n for i in range(n)]
res = 0
for i in range(n):
    if i%2 == 0:
        for j in range(0, n, 2):
            grid[i][j] = "C"
            res += 1
    else:
        for j in range(1, n, 2):
            grid[i][j] = "C"
            res += 1
            
print(res)
for row in grid:
    print("".join(row))