t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    closest = dict()
    closest[vals[0]] = vals[1] - vals[0]
    for i in range(1, len(vals) - 1):
        closest[vals[i]] = min(vals[i] - vals[i - 1], vals[i+1] - vals[i])
    else:
        closest[vals[-1]] =vals[-1] - vals[-2]
    for i in range(1, max(vals)):
        for key, val in closest.items():
            if abs(i - key) >= val:
                break
        else:
            print("YES")
            break
    else:
        print("NO")