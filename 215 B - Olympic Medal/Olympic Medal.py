n, *x = map(int, input().split())
m, *y = map(int, input().split())
k, *z = map(int, input().split())
A, B = map(int, input().split())
res = 0
r1 = max(x)
p2 = min(z)
for p1 in y:
    r2 = ((p1*r1**2*B)/(B*p1 + A*p2))**0.5
    res = max(res, r2)
print(res)