t = int(input())
for i in range(t):
    res = ""
    for j in range(8):
        row = input()
        for char in row:
            if char != ".":
                res += char
    print(res)