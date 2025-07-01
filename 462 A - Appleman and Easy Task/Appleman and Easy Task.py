n = int(input())
grid = []
for i in range(n):
    grid.append(input())
for i in range(n):
    for j in range(n):
        c = 0
        for x, y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= i + x < n and 0 <= j + y < n and grid[i+x][j+y] == "o":
                c += 1
        if c % 2 != 0:
            print("NO")
            exit()
print("YES")
    