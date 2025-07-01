t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(input())
    for i in range(0, n, k):
        for j in range(0, n, k):
            print(grid[i][j], end="")
        print()