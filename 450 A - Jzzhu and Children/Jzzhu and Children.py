from collections import deque

n, m = map(int, input().split())
vals = [*map(int, input().split())]
q = deque([(i, vals[i]) for i in range(len(vals))])
while len(q) != 1:
    idx, c = q.popleft()
    c -= m
    if c > 0:
        q.append((idx, c))
    
    
else:
    print(q.pop()[0] + 1)