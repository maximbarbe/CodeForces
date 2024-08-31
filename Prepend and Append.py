t = int(input())
for i in range(t):
    n = int(input())
    string = input()
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] == string[right]:
            print(right - left + 1)
            break
        left += 1
        right -= 1
    else:
        if len(string) % 2 == 1:
            print(1)
        else:
            print(0)