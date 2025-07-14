from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    vals.sort()
    c = Counter(vals)
    print(n-c[min(vals)])