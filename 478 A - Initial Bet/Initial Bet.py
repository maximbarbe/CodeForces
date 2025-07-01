vals = [*map(int, input().split())]
s = sum(vals)
if s % 5 != 0 or s == 0:
    print(-1)
else:
    print(s//5)