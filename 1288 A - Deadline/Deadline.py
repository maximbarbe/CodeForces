from math import ceil


f = lambda d, x:ceil(d/(x + 1))


t = int(input())
for i in range(t):
    n, d = map(int, input().split())
    if d <= n:
        print("YES")
        continue
    left, right = 0, n
    while right - left > 10:
        third = (right - left)//3
        f_left = left + f(d, left)
        f_right = right + f(d, right)
        m1 = left + third
        m2 = right - third
        f1 = m1 + f(d, m1)
        f2 = m2 + f(d, m2)
        if f1 <= n or f2 <= n:
            print("YES")
            break
        else:

            if f1 > f_left:
                right = m1
            elif f2 > f_left:
                right = m2
            elif f2 > f_right:
                left = m2
            elif f1 > f_right:
                left = m1
            else:
                left = m1
                right = m2
                
    else:
        for x in range(left, right + 1):
            if x + f(d, x) <= n:
                print("YES")
                break
        else:
            print("NO")