t = int(input())
for i in range(t):
    string = input()
    if len(set(string)) == 1:
        print("NO")
    else:
        left, right = 0, len(string) - 1
        string = [char for char in string]
        while string[left] == string[right]:
            left += 1
        string[left], string[right] = string[right], string[left]
        print("YES")
        print("".join(string))
        