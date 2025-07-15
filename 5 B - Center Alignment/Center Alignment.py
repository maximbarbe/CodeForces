import sys

lines = []
max_len = 0
for line in sys.stdin.readlines():
    l = line.rstrip("\n")
    max_len = max(max_len, len(l))
    lines.append(l)

print("*"*(max_len + 2))
left = True
for l in lines:
    print("*",end="")
    if (max_len - len(l))%2 == 0:
        side = (max_len - len(l))//2
        print(" "*side + l  + " "*side, end="")
    else:
        side = (max_len - len(l))//2
        if left:
            
            print(" "*side + l  + " "*(side + 1), end="")
        else:
            print(" "*(side + 1) + l  + " "*side, end="")
        left ^= True
    print("*")
print("*"*(max_len + 2))