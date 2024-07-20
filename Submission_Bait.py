t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    mx = 0
    vals.sort(reverse= True)
    alice = True
    for i in range(len(vals)):
        if vals[i] >= mx:
            alice ^= True
            mx = vals[i]
            
        else:
            break
    if not alice:
        print("YES")
    else:
        print("NO")