n = int(input())
vals = [*map(int, input().split())]
res = 0
before = 0
after = sum(vals)
for i in range(len(vals)):
    cur = after
    zeros = 0
    ones = 0
    for i in range(i, len(vals)):
        if vals[i] == 1:
            ones += 1
        else:
            zeros += 1
        
        res = max(res, before + cur + zeros - ones)
    before += vals[i]
    after -= vals[i]
print(res)