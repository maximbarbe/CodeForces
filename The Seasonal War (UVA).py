from collections import defaultdict, deque

def bfs(src, n):
    q = deque([src])
    visited[src] = True
    while len(q) != 0:
        i, j = q.popleft()
        for x, y in [(0, 1), (0, -1), (1, 0), (1, -1), (-1, 0), (-1, 1), (-1, -1), (1, 1)]:
            if 0 <= i + x < n and 0 <= y + j < n and grid[i + x][y + j] == "1" and not visited[(i + x, y+j)]:
                visited[(i + x, y+j)] = True
                q.append((i + x, y+j))

img = 0
while True:
    img += 1
    try:
        n = int(input())
    except:
        break
    grid = []
    for i in range(n):
        grid.append(input())
    res = 0
    visited = defaultdict(lambda:False)
    for i in range(n):
        for j in range(n):
            if grid[i][j] == "1" and not visited[(i, j)]:
                res += 1
                bfs((i, j), n)
    print("Image number " + str(img) + " contains " + str(res) + " war eagles.")