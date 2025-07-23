n, m = map(int, input().split())
c = dict()
for i in range(m):
    a, b = input().split()
    if len(a) <= len(b):
        c[b] = a
        c[a] = a
    else:
        c[a] = b
        c[b] =b
res = []
for word in input().split():
    res.append(c[word])
print(*res)