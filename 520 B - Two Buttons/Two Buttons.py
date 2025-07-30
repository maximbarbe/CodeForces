from collections import deque, defaultdict


n, m = map(int, input().split())
visited =defaultdict(lambda:False)
q = deque([(n, 0)])
while q:
    cur, count = q.popleft()
    if cur == m:
        print(count)
        exit()
    else:
        if cur - 1 >= 0 and not visited[cur - 1]:
            q.append((cur - 1, count + 1))
            visited[cur - 1] = True
        if cur < m and not visited[2*cur]:
            q.append((2*cur, count + 1))
            visited[2*cur] = True