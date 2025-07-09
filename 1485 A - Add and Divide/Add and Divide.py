from collections import deque, defaultdict


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    q = deque([(a, b, 0)])
    seen = defaultdict(lambda:False)
    seen[a] = True
    while True:
        a, b, cur = q.popleft()
        if a == 0:
            break
        first = int(a/b)
        if not seen[first]:
            q.append((int(a/b), b, cur + 1))
        q.append((a, b+1,cur + 1))
    print(cur)