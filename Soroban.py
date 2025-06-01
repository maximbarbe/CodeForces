n = input()
for c in n[::-1]:
    c = int(c)
    if c == 0:
        print("O-|-OOOO")
    elif c == 1:
        print("O-|O-OOO")
    elif c == 2:
        print("O-|OO-OO")
    elif c== 3:
        print("O-|OOO-O")
    elif c==4:
        print("O-|OOOO-")
    elif c== 5:
        print("-O|-OOOO")
    elif c== 6:
        print("-O|O-OOO")
    elif c== 7:
        print("-O|OO-OO")
    elif c== 8:
        print("-O|OOO-O")
    else:
        print("-O|OOOO-")