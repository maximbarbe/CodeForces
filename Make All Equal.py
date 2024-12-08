from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    c = Counter([*map(int, input().split())])
    print(n - c.most_common(1)[0][1])