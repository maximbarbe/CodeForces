t = int(input())
for i in range(t):
    x, y = 0, 0
    n = int(input())
    dirs=  input()
    for char in dirs:
        match char:
            case "U":
                y += 1
            case "D":
                y -= 1
            case "R":
                x += 1
            case _:
                x -= 1
        if x == 1 and y == 1:
            print("YES")
            break
    else:
        print("NO")
