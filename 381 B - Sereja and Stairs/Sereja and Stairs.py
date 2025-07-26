from collections import Counter

n = int(input())
vals = [*map(int, input().split())]
c = Counter(vals)

m = max(vals)

left = []
right = []

for k in sorted(c.keys(), reverse=True)[1:]:
    if c[k] >= 2:
        left.append(k)
        right.append(k)
    else:
        left.append(k)

res = left[::-1] + [m] + right

print(len(res))
print(*res)