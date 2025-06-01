grid = []
res = [[0]*3 for i in range(3)]
for i in range(3):
    grid.append([*map(int, input().split())])
for i in range(3):
    for j in range(3):
        cur =0
        for x, y in [(0,1 ), (0, -1), (1, 0), (-1, 0), (0, 0)]:
            if 0 <= i + x < 3 and 0 <= j + y < 3:
                cur += grid[i + x][j + y]
        if cur % 2 == 0:
            res[i][j] = "1"
        else:
            res[i][j] = "0"
for row in res:
    print("".join(row))