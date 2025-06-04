a = input()
b = input()

int_res = str(int(a) + int(b)).replace("0", "")
str_res = str(int(a.replace("0", "")) + int(b.replace("0", "")))
if int_res ==  str_res:
    print("YES")
else:
    print("NO")