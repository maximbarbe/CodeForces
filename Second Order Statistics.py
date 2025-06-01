n = int(input())
vals = set([*map(int, input().split())])
if len(vals) == 1:
    print("NO")
else:
    vals = sorted(vals)
    print(vals[1])