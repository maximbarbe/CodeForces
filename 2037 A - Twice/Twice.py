from collections import Counter
 
for i in range(int(input())):
    n = int(input())
    vals = [*map(int, input().split())]
    c = Counter(vals)
    res = 0
    for v in c.keys():
        res += c[v]//2
    print(res)