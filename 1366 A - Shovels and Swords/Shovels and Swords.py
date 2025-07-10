from math import floor


t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    res = 0
    if a > b:
        x = min(a-b, min(b, a//2))
        res += x
        a -= 2*x
        b -= x
    elif a < b:
        x = min(b-a, min(a, b//2))
        res += x
        b -= 2*x
        a -= x

    if a == b:
        c = min(a//3, b//3)
        res += c*2
        a -= c*3
        b -= c*3
        if a >= 2 and b >= 2:
            res += 1
            a -= 2
            b -= 1
        if a == 1 and b >= 2:
            res += 1
            
        
    print(res)