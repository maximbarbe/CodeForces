t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    s = sum(vals)
    if s == len(vals):
        print(0)
    elif s > len(vals):
        print(s - len(vals))
    else:
        print(1)