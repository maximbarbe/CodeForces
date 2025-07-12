t = int(input())
for i in range(t):
    input()
    k,n,m = map(int, input().split())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    res = []
    i = 0
    j = 0
    ok = True
    while i != len(a) and j != len(b):
        if a[i] == 0:
            res.append(0)
            i += 1
            k += 1
            continue
        if b[j] == 0:
            res.append(0)
            j += 1
            k += 1
            continue
        if a[i] >k and b[j] > k:
            ok = False
            break
        if a[i] <= k:
            res.append(a[i])
            i += 1
            continue
        if b[j] <= k:
            res.append(b[j])
            j += 1
            continue
    while ok and i != len(a):
        if a[i] <= k:
            if a[i] == 0:
                k += 1
            res.append(a[i])
            i += 1
        else:
            ok = False
            break
    while ok and j != len(b):
        if b[j] <= k:
            if b[j] == 0:
                k += 1
            res.append(b[j])
            j += 1
        else:
            ok = False
            break
    
    if not ok:
        print(-1)
        continue
    else:
        print(*res)
