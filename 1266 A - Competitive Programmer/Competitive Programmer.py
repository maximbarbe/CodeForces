t = int(input())
for i in range(t):
    s = input()
    if not sum([*map(int, [char for char in s])])%3 == 0:
        print("cyan")
    else:
        zeros = s.count("0")
        if zeros == 0:
            print("cyan")
        elif zeros > 1:
            print("red")
        else:
            for v in "2468":
                if v in s:
                    print("red")
                    break
            else:
                print("cyan")
        