t = int(input())
for i in range(t):
    n = int(input())
    seen = dict()
    vals = [*map(int, input().split())]
    for i in range(len(vals)):
        if seen.get(vals[i], None) != None:
            print("YES")
            break
        seen[vals[i]] = True
    else:
        print("NO")