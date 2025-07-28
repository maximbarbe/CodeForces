from collections import deque

t = int(input())
for i in range(t):
    n, s = map(int, input().split())
    q = deque()
    a = [*map(int, input().split())]
    c = 0
    for i, v in enumerate(a):
        if v == 1:
            c += 1
            q.append(i)
    if c < s:
        print(-1)
    elif c == s:
        print(0)
    else:
        left = right = 0
        m = 0
        cur = 0
        while right != n:
            if cur == s and a[right] == 1:
                while left < right and cur == s:
                    cur -= a[left]
                    left += 1
                    
                
            else:
                cur += a[right]
                right += 1
            m = max(m, right - left)
        print(n - m)