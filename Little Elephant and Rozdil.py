n = int(input())
v = [*map(int, input().split())]
m = min(v)
if v.count(m) > 1:
    print("Still Rozdil")
else:
    print(v.index(m) + 1)