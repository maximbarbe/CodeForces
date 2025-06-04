res = 0
n = int(input())
vals = [*map(int, input().split())]
zeros = 0
for i in range(len(vals)):
    if vals[i] == 1:
        break
vals = vals[i:]
for v in vals:
    if v == 1:
        if zeros == 1:
            res += 1
        res += 1
        zeros = 0
    else:
        zeros += 1
print(res)