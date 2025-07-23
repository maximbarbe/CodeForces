n, t = map(int, input().split())

vals = [*map(int, input().split())] + [1]
cur = 0
while cur < n:
    if cur == t - 1:
        print("YES")
        break
    cur += vals[cur]
else:
    print("NO")