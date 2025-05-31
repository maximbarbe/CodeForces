l,r,a = map(int, input().split())
if l == r:
    if a%2 == 1:
        print(l + r + a - 1)
    else:
        print(l + r + a)
elif l < r:
    if l + a <= r:
        print(2*(l+a))
    else:
        num_to_add = r - l
        l = r
        a -= num_to_add
        if a > 0:
            if a%2 == 1:
                print(l + r + a - 1)
            else:
                print(l + r + a)
else:
    if r + a <= l:
        print(2*(r+a))
    else:
        num_to_add = l-r
        r = l
        a -= num_to_add
        if a > 0:
            if a%2 == 1:
                print(l + r + a - 1)
            else:
                print(l + r + a)
        