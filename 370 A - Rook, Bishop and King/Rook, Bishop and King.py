from collections import deque, defaultdict

r1,c1,r2,c2 = map(int, input().split())

bishop = 0 if (r1 + c1)%2 != (r2 + c2)%2 else 1 if abs(r1-r2) == abs(c1-c2) else 2
rook = 1 if r1 == r2 or c1 == c2 else 2


visited = defaultdict(lambda:False)
visited[(r1, c1)] = True
q = deque([(r1, c1, 0)])
while q:
    i, j, c = q.popleft()
    if (i, j) == (r2, c2):
        print(rook, bishop, c)
        exit()
    for di, dj in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]:
        if 1 <= i + di <= 8 and 1 <= j + dj <= 8 and not visited[(i + di, j + dj)]:
            q.append((i + di, j + dj, c + 1))
            visited[(i + di, j + dj)] = True

