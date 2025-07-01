n = int(input())
res = []
cur = 0
s = input()
for c in s:
    if c == 'B':
        cur += 1
    elif c == "W":
        if cur != 0:
            res.append(cur)
        cur = 0
if cur != 0:
    res.append(cur)
print(len(res))
if len(res) != 0:
    print(*res)