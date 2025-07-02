t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    ones = vals.count(1)
    twos = vals.count(2)
    if ones % 2 == 1:
        print("NO")
    else:
        if twos % 2 == 0:
            print("YES")
        else:
            if ones - 2 < 0:
                print("NO")
            else:
                print("YES")