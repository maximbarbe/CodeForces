from collections import deque, defaultdict

def bfs(srcx, srcy, color):
    q = deque([(srcx, srcy)])
    visited[(srcx, srcy)] = True
    while len(q) != 0:
        i, j = q.popleft()
        for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= i + x < n and 0 <= j + y < m and grid[i + x][j + y] == color and not visited[(i+x, j+y)]:
                visited[(i + x, j + y)] = True
                q.append((i+x, j+y))
    


n, m, color = input().split()
n = int(n)
m = int(m)
visited = defaultdict(lambda:False)
grid = []
for i in range(n):
    grid.append(input())
avoid = f"{color}."
res = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == color:
            for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= i + x < n and 0 <= j + y < m and grid[i + x][j + y] not in avoid and not visited[(i+x, j+y)]:
                    res += 1
                    bfs(i+x, j+y, grid[i + x][j + y])
print(res)