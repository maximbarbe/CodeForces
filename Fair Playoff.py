t = int(input())
for i in range(t):
    vals = [*map(int, input().split())]
    s = sorted(vals)
    if set([vals[0], vals[1]]) == set(s[2:]) or set([vals[2], vals[3]]) == set(s[2:]):
        print("NO")
    else:
        print("YES")
    