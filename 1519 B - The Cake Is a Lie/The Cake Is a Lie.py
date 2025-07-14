from collections import defaultdict, deque

t = int(input())
for i in range(t):
    n,m,k = map(int, input().split())
    visited = defaultdict(lambda:False)
    q = deque([(1, 1, 0)])
    while q:
        x, y, cost = q.popleft()
        if (x, y) == (n,m) and cost == k:
            print("YES")
            break
        first = (x + 1, y, cost + y)
        second = (x, y+1, cost + x)
        if not visited[first] and first[0] <= n and first[2] <= k:
            q.append(first)
            visited[first] = True
        if not visited[second] and second[1] <= m and second[2] <= k:
            q.append(second)
            visited[second] = True
    else:
        print("NO")