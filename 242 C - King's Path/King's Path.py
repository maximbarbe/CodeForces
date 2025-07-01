from collections import defaultdict, deque
x0, y0, x1, y1 = map(int, input().split())
r_max = 10**9
can_visit = defaultdict(lambda:False)
visited = defaultdict(lambda:False)
for i in range(int(input())):
    r, a, b = map(int, input().split())
    for j in range(a, b + 1):
        can_visit[(r, j)] = True
        
q = deque([(x0, y0, 0)])
visited[(x0, y0)] = True
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
while len(q) != 0:
    i, j, cost = q.popleft()
    if i == x1 and j == y1:
        print(cost)
        exit()
    for x, y in dirs:
        if 1 <= i + x <= r_max and 1 <= y+j <= r_max and can_visit[(i + x, y+j)] and not visited[(i + x, y+j)]:
            q.append((i + x, y+j, cost  + 1))
            visited[(i + x, y+j)] = True
else:
    print(-1)