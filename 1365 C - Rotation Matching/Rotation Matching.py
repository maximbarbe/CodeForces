from collections import defaultdict

t = int(input())
indices = dict()
c = defaultdict(lambda:0)
a = [*map(int, input().split())]
for i in range(t):
    indices[a[i]] = i
b = [*map(int, input().split())]
for i in range(len(b)):
    c[(i - indices[b[i]])%t] += 1
print(max(c.values()))