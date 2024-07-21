values = "HQ9"
string = input()
for char in string:
    if char in values:
        print("YES")
        exit()
else:
    print("NO")