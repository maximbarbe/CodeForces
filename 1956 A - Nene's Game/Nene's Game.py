from bisect import bisect_right
def res(n, indices):
    while True:
        k = bisect_right(indices, n)
        if k == 0:
            return n
        n -= k
    
        
t = int(input())



for i in range(t):
    k, q =map(int, input().split())
    indices = [*map(int, input().split())]
    remove = dict()
    seq = [*map(int, input().split())]
    for idx in indices:
        remove[idx] = True
    r = []
    for a in seq:
        r.append(res(a, indices))
        
    print(*r)