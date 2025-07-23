from collections import Counter


n = int(input())
l = [*map(int, input().split())]
c = Counter(l)
print(max(c.values()), len(c))