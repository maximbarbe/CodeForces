from collections import deque, defaultdict

t = int(input())
for i in range(t):
    n = int(input())
    n -= 1
    grid = []
    for j in range(2):
        grid.append(input())
        
    visited = defaultdict(lambda:False)
    visited[(0, 0)] = True
    q = deque([(0, 0)])
    while q:
        i, j = q.popleft()
        if (i, j) == (1, n):
            print("YES")
            break
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            if 0 <= i + di <= 1 and 0 <= j + dj <= n:
                end_i = i + di
                end_j = j + dj + 1 if grid[i + di][j + dj] == ">" else - 1
                if not visited[(end_i, end_j)]:
                    visited[(end_i, end_j)] = True
                    q.append((end_i, end_j))
    else:
        print("NO")