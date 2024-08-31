t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    stack = []
    string = input()
    for char in string:
        if char == "(":
            stack.append(char)
        else:
            if len(stack) == 0:
                res += 1
            else:
                stack.pop()
    print(res)