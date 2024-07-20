n= int(input())
vals = [*map(int, input().split())]
max_height = 0
idx_max = 0
min_height = 101
idx_min = 0
for i in range(len(vals)):
    if vals[i] > max_height:
        max_height = vals[i]
        idx_max = i
    if vals[i] <= min_height:
        min_height = vals[i]
        idx_min = i
        
res = (idx_max) + (n - 1 - idx_min)
if idx_max > idx_min:
    res -= 1
print(res)