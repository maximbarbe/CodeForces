t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    s = sorted(vals)
    if vals == s:
        print("NO")
    else:
        print("YES")
        res = []
        for i in range(len(vals)):
            if vals[i] != s[i]:
                res.append(vals[i])
        print(len(res))
        print(*res)