t = int(input())
for i in range(t):
    n = int(input())
    string = input().lower()
    stack = []
    for char in string:
        if stack == [] or char != stack[-1]:
            stack.append(char)
    print("YES" if "".join(stack) == "meow" else "NO")