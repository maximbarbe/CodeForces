input()
vals = sorted([*map(int, input().split())], reverse=True)
cur = 0
res = 0
other = sum(vals)
for i in range(len(vals)):
    cur += vals[i]
    other -= vals[i]
    res += 1
    if cur > other:
        print(res)
        exit()