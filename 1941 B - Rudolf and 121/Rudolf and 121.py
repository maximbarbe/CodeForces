from collections import deque

for i in range(int(input())):
    n = int(input())
    q = deque([*map(int, input().split())])
    while q and q[0] == 0:
        q.popleft()
    while q and q[-1] == 0:
        q.pop()
    while len(q) >= 3:
        a, b, c = q.popleft(), q.popleft(), q.popleft()
        
        if b < 2*a or c < a:
            break
        b -= 2*a
        c -= a
        if b:
            q.appendleft(c)
            q.appendleft(b)
        elif c:
            q.appendleft(c)
        
    else:
        if len(q) == 0:
            print('YES')
        else:
            print("NO")
        continue
    print("NO")