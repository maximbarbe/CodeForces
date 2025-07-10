t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    more = 0
    for j in range(len(vals)):
        if vals[j] > j:
            more += vals[j] - j
            vals[j] = j
        else:
            if j - vals[j] > more:
                print("NO")
                break
            else:
                more = more - (j - vals[j])
                vals[j] = j
                
    else:
        print("YES")