cur = 0
string = input()
danger = False
past = None
for char in string:
    if char != past:
        past = char
        cur =1 
    else:
        cur += 1
    if cur == 7:
        print("YES")
        exit()
else:
    print("NO")