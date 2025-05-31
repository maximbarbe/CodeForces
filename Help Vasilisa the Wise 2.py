r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())
if r2 - c1 + r1 -c2 != 0 or d2 - c1 -c2 + d1 != 0:
    print(-1)
else:
    d = (d1-r1+c2)/2
    a = (r1-c2)+ d
    b =c2 - d
    c = c1-r1+c2-d
    for n in [a, b, c, d]:
        if n not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print(-1)
            exit()
    digits = set([a, b, c, d])
    if len(digits) != 4:
        print(-1)
        exit()
    print(int(a), int(b))
    print(int(c), int(d))