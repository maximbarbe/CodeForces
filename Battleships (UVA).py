from collections import deque, defaultdict


def bfs(src, n):
    q = deque([src])
    visited[src] = True
    while len(q) != 0:
        i, j = q.popleft()
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i + x < n and 0 <= j + y < n and grid[i + x][y + j] in "@x" and not visited[(i + x, y + j)]:
                q.append((i + x, y+j))
                visited[(i + x, y+j)] = True

t = int(input())
for i in range(t):
    n = int(input())
    grid = []
    res = 0
    visited = defaultdict(lambda:False)
    for j in range(n):
        grid.append(input())
    
    for j in range(n):
        for k in range(n):
            if grid[j][k] == "x" and not visited[(j, k)]:
                res += 1
                bfs((j, k), n)
    
    print("Case "+str(i+1)+": "+str(res))
        