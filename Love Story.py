word = "codeforces"
t = int(input())
for i in range(t):
    string = input()
    res = 0
    for j in range(len(string)):
        if string[j] != word[j]:
            res += 1
    print(res)