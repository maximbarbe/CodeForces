from collections import Counter

n = int(input())
c = Counter()
for i in range(n):
    c[input()] += 1
    
print(c.most_common(1)[0][0])