for i in range(int(input())):
    input()
    s = input()
    res = []
    for c in s:
        match c:
            case "U":
                res.append("D")
            case "D":
                res.append("U")
            case _:
                res.append(c)
    print("".join(res))