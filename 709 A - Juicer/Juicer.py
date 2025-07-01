n,b,d = map(int, input().split())

oranges = [*map(int, input().split())]
cur = 0
res = 0
for o in oranges:
    if o >b:
        continue
    else:
        if cur + o > d:
            res += 1
            cur = 0
        else:
            cur += o
print(res)