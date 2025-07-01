n= int(input())
v = set([*map(int, input().split())])
match len(v):
    case 1:
        print("YES")
    case 2:
        print("YES")
    case 3:
        v = sorted(v)
        v1 = v[0]
        v2 = v[1]
        v3 = v[2]
        if v2 - v1 == v3 - v2:
            print("YES")
        else:
            print("NO")
    case _:
        print("NO")
            