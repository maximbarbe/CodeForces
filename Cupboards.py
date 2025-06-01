n = int(input())
a = []
b = []
for i in range(n):
    l, r = map(int, input().split())
    a.append(l)
    b.append(r)
print(n - max(a.count(0), a.count(1)) + n-max(b.count(0), b.count(1)))
