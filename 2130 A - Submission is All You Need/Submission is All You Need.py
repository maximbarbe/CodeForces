from collections import Counter
 
for _ in range(int(input())):
    n = int(input())
    
    s = [*map(int, input().split())]
    c = Counter(s)
    count = min(c[0], c[1])
    res = 2 * count
    c[0] -= count
    c[1] -= count
    zero_count = c[0]
    res += zero_count
    c[0] -= zero_count
    for key in c.keys():
        res += key*c[key]
    print(res)