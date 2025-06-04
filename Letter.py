n, m = map(int, input().split())
left = m + 1
right = 0
up = n + 1
down = 0 
grid = []
for i in range(n):
    row = input()
    for j in range(len(row)):
        if row[j] == "*":
            if i < up:
                up = i
            if i > down:
                down = i
            if j < left:
                left = j
            if j > right:
                right = j
    grid.append(row)
res = []
for i in range(up, down + 1):
    print(grid[i][left:right + 1])
