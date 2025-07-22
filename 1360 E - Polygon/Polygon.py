t = int(input())
for i in range(t):
    n = int(input())
    grid = []
    for j in range(n):
        grid.append(input())
    for i in range(n-2, -1, -1):
        for j in range(n-2, -1, -1):
            if grid[i][j] == "1" and grid[i + 1][j] == "0" and grid[i][j + 1] == "0":
                break
        else:
            continue
        print("NO")
        break
    else:
        print("YES")