n = int(input())
chars = [c for c in input()]
sat =chars.count("x")
stood = chars.count("X")
if sat == stood:
    print(0)
    print("".join(chars))
elif sat > stood:
    moves = sat - n//2
    res = moves
    for i in range(n):
        if moves != 0 and chars[i] == "x":
            chars[i] = "X"
            moves -= 1
    print(res)
    print("".join(chars))
else:
    moves = stood - n//2
    res = moves
    for i in range(n):
        if moves != 0 and chars[i] == "X":
            chars[i] = "x"
            moves -= 1
    print(res)
    print("".join(chars))