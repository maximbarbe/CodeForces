t = int(input())
for i in range(t):
    l = [*map(int, input().split())]
    l.sort()
    if l[0] != l[1] and l[1] != l[2]:
        if l[0] + l[1] == l[2]:
            print("YES")
        else:
            print('NO')
    else:
        if len(set(l)) == 2:
            if l[0] == l[1]:
                if l[2] % 2 != 0:
                    print("NO")
                else:
                    print("YES")
            elif l[0] == l[2]:
                if l[1] % 2 != 0:
                    print("NO")
                else:
                    print("YES")
            else:
                if l[0] % 2 != 0:
                    print("NO")
                else:
                    print("YES")
        elif len(set(l)) == 1:
            if l[0] % 2 == 0:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")