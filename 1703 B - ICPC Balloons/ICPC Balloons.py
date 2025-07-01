t = int(input())
for i in range(t):
    n = int(input())
    seen = dict()
    res = 0
    string = input()
    for char in string:
        if seen.get(char, False) == False:
            seen[char] = True
            res += 2
        else:
            res += 1
    print(res)