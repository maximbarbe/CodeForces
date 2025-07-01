t = int(input())
for i in range(t):
    string = input().lstrip("0").rstrip("0")
    print(string.count("0"))