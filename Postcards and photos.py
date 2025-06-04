string = input()
prev = None
res = 0
cur = 0
for c in string:
    if c != prev:
        if prev == None:
            prev = c
            cur = 1
        else:
            res += 1
            prev = c
            cur = 1
    else:
        cur += 1
    if cur == 6:
        cur = 1
        res += 1
if cur != 0:
    res += 1
print(res)