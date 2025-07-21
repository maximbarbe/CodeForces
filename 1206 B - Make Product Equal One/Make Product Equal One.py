n = int(input())
vals = [*map(int, input().split())]
negatives = 0
zeros = 0


res = 0
for v in vals:
    if v < 0:
        res += abs(v) - 1
        negatives += 1
    elif v > 0:
        res += v - 1
    else:
        res += 1
        zeros += 1
if negatives % 2 == 1:
    if zeros == 0:
        res += 2
print(res)