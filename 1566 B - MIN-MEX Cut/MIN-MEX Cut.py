t = int(input())
for i in range(t):
    s=  input()
    res = 0
    one = False
    zero = False
    for c in s:
        match c:
            case "0":
                if not zero:
                    zero = True
                    res += 1
                if one:
                    one = False
            case "1":
                if not one:
                    one = True
                if not zero:
                    one = True
                else:
                    zero = False
                    one = True
    print(min(res, 2))