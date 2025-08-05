t = int(input())
for i in range(t):
    s = input()
    stack = []
    for idx, c in enumerate(s):
        if idx == len(s) - 1:
            if stack[0][1] == 0:
                print("NO")
                break
            else:
                print("YES")
                break
        if c == "(":
            stack.append((c, idx))
        else:
            stack.pop()