t = int(input())
for i in range(t):
    n, m, x, y = map(int, input().split())
    grid = []
    res = 0
    for i in range(n):
        grid.append(input())
    p = y >= 2*x
    i = 0
    j = 0
    while i != n:
        if grid[i][j] == ".":
            if p:
                res += x
                j += 1
            else:
                if j != m - 1 and grid[i][j + 1] == ".":
                    res += y
                    j += 2
                else:
                    res += x
                    j += 1
        else:
            j += 1
        if j == m:
            i += 1
            j = 0
    print(res)
                    