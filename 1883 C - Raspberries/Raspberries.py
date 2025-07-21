for i in range(int(input())):
    n, k = map(int, input().split())
    
    if k == 2:
        for v in [*map(int, input().split())]:
            if v % 2 == 0:
                print(0)
                break
        else:
            print(1)
    elif k == 4:
        c = 0
        three = 0
        for v in [*map(int, input().split())]:
            if v % 4 == 0:
                print(0)
                break
            if v % 2 == 0:
                c += 1
            elif v%4 == 3:
                three += 1
        else:
            if three == 0:
                print(max(0, 2-c))
            else:    
                if c < 2:
                    print(1)
                else:
                    print(0)

    else:
        m = k
        for v in [*map(int, input().split())]:
            if v % k == 0:
                print(0)
                break
            m = min(m, k - v%k)
        else:
            print(m)