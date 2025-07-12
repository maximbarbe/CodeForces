def is_balanced(s):
    stack = []
    for c in s:
        if c == "(":
            stack.append(c)
        else:
            if not stack or stack[-1] != "(":
                return False
            else:
                stack.pop()
    return len(stack) == 0


t = int(input())
assignments = [")))", "))(", ")()", ")((", "())", "()(", "(()", "((("]
for i in range(t):
    s = input()
    for a in assignments:
        b = s.replace("A", a[0])
        b = b.replace("B", a[1])
        b = b.replace("C", a[2])
        if is_balanced(b):
            print("YES")
            break
    else:
        print("NO")
    