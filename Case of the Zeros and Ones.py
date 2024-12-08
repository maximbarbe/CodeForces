n = int(input())
string = input()
stack = []
for char in string:
    if stack == [] or char == stack[-1]:
        stack.append(char)
    else:
        stack.pop()
print(len(stack))