from collections import defaultdict, deque


t = int(input())
for i in range(t):
    n=int(input())
    grid = []
    for i in range(2):
        grid.append(input())
    q = deque([(0, 0)])
    visited = defaultdict(lambda:False)
    visited[(0, 0)] = True
    while q:
        i, j = q.popleft()
        if i == 1 and j == n - 1:
            print("YES")
            break
        for di, dj in [(0, 1), (1, 0), (-1, 0), (1, 1), (-1, 1)]:
            if 0 <= i + di <= 1 and 0 <= j + dj < n and not visited[(i + di, j + dj)] and grid[i + di][j + dj] == "0":
                q.append((i + di, j + dj))
                visited[(i + di, j + dj)] = True
    else:
        print("NO")    