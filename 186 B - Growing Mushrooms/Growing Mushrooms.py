def find_max_height(t1, t2, ai, bi, k):
    first = t1*ai
    after = t2*bi + first*(1-k)
    return after
    
n, t1, t2, k = map(int, input().split())
v = []
k /= 100
for i in range(1, n+1):
    ai, bi = map(int, input().split())
    v.append((max(find_max_height(t1, t2, ai, bi, k), find_max_height(t1, t2, bi, ai, k)), i))
v.sort(key=lambda el:(-el[0], el[1]))
for res, idx in v:
    print(f"{idx} {res:.2f}")