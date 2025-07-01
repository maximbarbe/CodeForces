import heapq


n, f = map(int, input().split())
res = 0
v = []
for i in range(n):
    
    ki, li = map(int, input().split())
    v.append((min(2*ki, li) - min(ki, li), ki, li))
v.sort(key=lambda el:-el[0])
for i in range(len(v)):
    a, b,c = v[i]
    if i < f:
        res += min(2*b, c)
    else:
        res += min(b, c)
print(res)