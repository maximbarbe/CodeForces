from collections import defaultdict

def dfs(src):
    if marks[src] == 2:
        return
    for dest in edges[src]:
        dfs(dest)
    marks[src] = 2
    order.append(src)    


while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    in_deg = [0]*(n+1)
    edges = defaultdict(lambda:[])
    for i in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        in_deg[b] += 1
    marks = defaultdict(lambda:0)
    order = []
    for i in range(1, n+1):
        if in_deg[i] == 0:
            dfs(i)
    print(*order[::-1])