n = int(input())
vals = [*map(int, input().split())]
if vals.index(1) in [0, n-1] or vals.index(n) in [0, n-1]:
    print(n-1)
else:
    min_val = min(vals)
    max_val = max(vals)
    print(max(abs(0 - vals.index(min_val)), abs(0 - vals.index(max_val)), abs(n-1 - vals.index(min_val)), abs(n-1 - vals.index(max_val))))