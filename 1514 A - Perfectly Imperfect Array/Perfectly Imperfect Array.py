t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    for v in vals:
        if int(v**0.5)**2 != v:
            print("YES")
            break
    else:
        print("NO")