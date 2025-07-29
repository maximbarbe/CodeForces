from collections import defaultdict, deque


q = deque()
edges = defaultdict(lambda:[])
visited = defaultdict(lambda:False)
n = int(input())
for i in range(n):
    parent = int(input())
    if parent == -1:
        q.append((i, 1))
        visited[i] = True
    else:
        edges[parent - 1].append(i)

p = 0
while q:
    node, m = q.popleft()
    p = max(m, p)
    for dest in edges[node]:
        if not visited[dest]:
            visited[dest] = True
            q.append((dest, m + 1))
print(p)