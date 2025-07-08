t = int(input())
for i in range(t):
    stack = []
    s = input()
    for c in s:
        if not stack:
            stack.append(c)
        else:
            if c == "A":
                stack.append("C")
            else:
                stack.pop()
    print(len(stack))