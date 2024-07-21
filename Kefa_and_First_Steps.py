n = int(input())
cur_max = 0
cur = 0
prev = 10**9 + 1
vals = [*map(int, input().split())]
for val in vals:
    if val < prev:
        prev = val
        cur = 1
    else:
        prev = val
        cur += 1
    if cur  > cur_max:
        cur_max = cur
print(cur_max)