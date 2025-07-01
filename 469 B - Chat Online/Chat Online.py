from collections import defaultdict

p,q,l,r = map(int,input().split())
z_available = [False]*(1001)
for i in range(p):
    ai, bi = map(int, input().split())
    for j in range(ai, bi + 1):
        z_available[j] = True
times = []
for i in range(q):
    ci, di = map(int, input().split())
    times.append((ci, di))
res = 0
t = set()
for i in range(l, r + 1):
    for ci, di in times:
        if ci + i <= 1000:
            for k in range(ci + i, min(1001, di + i + 1)):
                if z_available[k]:
                    t.add(i)
                    res += 1
                    break
            else:
                continue
            break

print(len(t))