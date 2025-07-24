t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        grid.append(input())
    for i in range(1, n):
        for j in range(1, m):
            left = True
            up = True
            if grid[i][j] == "1":
                for k in range(i-1, -1,-1):
                    if grid[k][j] == "0":
                        up = False
                        break
                for k in range(j - 1, -1, -1):
                    if grid[i][k] == "0":
                        left = False
                        break
            if not left and not up:
                print("NO")
                break
        else:
            continue
        break
    else:
        print("YES")