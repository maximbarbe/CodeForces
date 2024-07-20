n,m = map(int, input().split())
right = True
for i in range(n):
    if i % 2 == 0:
        print("#" * m)
    else:
        if right:
            print("." * (m - 1) + "#")
        else:
            print("#" + "."*(m - 1))
        right ^= True