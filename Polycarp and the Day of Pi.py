from math import pi

val = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"[:30]
t = int(input())
for i in range(t):
    string = input()
    for j in range(len(string)):
        if string[j] != val[j]:
            print(j)
            break
    else:
        print(len(string))