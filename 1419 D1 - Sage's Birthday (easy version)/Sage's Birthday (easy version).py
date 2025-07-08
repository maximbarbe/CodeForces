from collections import deque

n = int(input())

vals = deque(sorted([*map(int, input().split())]))
v = n//2 if n%2 == 1 else n//2 - 1

res = []
while len(vals) >= 2:
   res.append(vals.pop())
   res.append(vals.popleft())
   
if vals:
    res.append(vals.pop())

    
print(v)
print(*res)    
    

