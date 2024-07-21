t = int(input())
vals = [*map(int, input().split())]
vals.sort()
res = 0
left = 0
right = len(vals) - 1
cur =0
while left <= right:
    if cur + vals[right] <= 4:
        cur += vals[right]
        right -= 1
    elif cur + vals[left] <= 4:
        cur += vals[left]
        left += 1
    else:
        res += 1
        cur = 0
if cur != 0:
    res += 1
print(res)