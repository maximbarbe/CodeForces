from collections import Counter
t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    print(n - Counter(vals).most_common(1)[0][1])