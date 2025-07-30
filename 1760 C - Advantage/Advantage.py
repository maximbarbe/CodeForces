t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    temp = [(vals[i], i) for i in range(len(vals))]
    temp.sort(key=lambda el:el[0])
    res = [None]*n
    for j in range(len(temp)):
        if j != n-1:
            res[temp[j][1]] = temp[j][0] - temp[-1][0]
        else:
             res[temp[j][1]] = temp[j][0] - temp[j-1][0]
    
    print(*res)