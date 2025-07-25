t = int(input())
for i in range(t):
    n = int(input())
    s1 = input()
    s2 = input()
    red = 0
    blue = 0
    for r,b in zip(s1, s2):
        if r > b:
            red += 1
        elif b > r:
            blue += 1
    if red > blue:
        print('RED')
    elif blue > red:
        print('BLUE')
    else:
        print('EQUAL')