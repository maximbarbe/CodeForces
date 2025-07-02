t = int(input())
for i in range(t):
    n = int(input())
    seen = dict()
    res = 0
    if n % 2 == 0:
        res += 1
    for i in range(1, n if n % 2 == 0 else n + 1):
        if seen.get(i, None) != None:
            res += 2
            
        seen[n - i] = i
    print(res)