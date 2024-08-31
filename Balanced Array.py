t = int(input())
for i in range(t):
    n = int(input())
    if (n//2)%2 == 1:
        print("NO") 
    else:
        print("YES")
        n//=2
        arr = [i*2 for i in range(1, n + 1)]
        cur = 1
        added = 0
        sumn = sum(arr)
        while added != n - 1:
            sumn -= cur
            arr.append(cur)
            cur += 2
            added += 1
        else:
            arr.append(sumn)
        print(*arr)