from math import inf
import heapq
from collections import defaultdict

n, m = map(int, input().split())
edges = defaultdict(lambda:[])
MOD = 10**12
distances = [MOD]*n
visited = [False]*n
parent = [None]*n
distances[0] = 0
heap = [(inf, i) for i in range(n)]
heap[0] = (0, 0)
for i in range(m):
    u,v,c = map(int, input().split())
    u -= 1
    v -= 1
    edges[u].append((v, c))
    edges[v].append((u, c))
while heap:
    cost, vtx = heapq.heappop(heap)
    if vtx == n-1:
        break
    if visited[vtx]:
        continue
    visited[vtx] = True
    for dest, c in edges[vtx]:
        if cost + c < distances[dest]:
            distances[dest] = cost + c
            heapq.heappush(heap, (cost + c, dest))
            parent[dest] = vtx
    
    
if parent[n - 1] == None:
    print(-1)
else:
    path = []
    idx = n - 1
    while parent[idx] != None:
        path.append(idx + 1)
        idx = parent[idx]
    path.append(1)
    print(*path[::-1])