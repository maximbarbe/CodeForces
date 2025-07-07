t = int(input())
for i in range(t):
    x = int(input())
    for j in range(1, int(x**(1/3)) + 1):
        a = (x-j**3)**(1/3)
        if abs(a - round(a)) <= 0.0000000001 and a != 0:
            print("YES")
            break
    else:
        print("NO")
        