t = int(input())
for i in range(t):
    
    string = input()
    substrings = []
    i = 0
    while i != len(string):
        substrings.append(string[i] + string[i + 1])
        i += 2
    res = substrings[0]
    for i in range(1, len(substrings)):
        if substrings[i][0] == res[-1]:
            res += substrings[i][1]
        else:
            res += substrings[i]
    print(res)