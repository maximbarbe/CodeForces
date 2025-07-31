t = int(input())
for i in range(t):
    n = int(input())
    a = [*map(int, input().split())]
    s = sum(a)
    remainder = s%3
    if remainder == 0:
        print(0)
    elif remainder == 2:
        print(1)
    else:
        for v in a:
            if v % 3 == 1:
                print(1)
                break
        else:
            print(2)