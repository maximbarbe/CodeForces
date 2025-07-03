n = int(input())
for i in range(n):
    res = []
    s = input()
    for c in s:
        if c == "w":
            res.append(c)
        elif c == "q":
            res.append("p")
        else:
            res.append("q")
    print("".join(res[::-1]))