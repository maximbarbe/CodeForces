from collections import Counter

c = Counter()
n = int(input())
s = input()
for i in range(0, len(s)-1):
    c[s[i:i+2]] += 1
print(c.most_common(1)[0][0])