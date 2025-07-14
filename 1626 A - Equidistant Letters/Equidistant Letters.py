from collections import Counter

t = int(input())
for i in range(t):
    s = input()
    res = ""
    c = Counter(s)
    for k,v in c.items():
        res += k*v
    print(res)