t = int(input())
for i in range(t):
    n = int(input())
    digits = []
    while n != 0:
        digits.append(n%10)
        n//=10
        
    f = True
    x = 0
    y = 0
    for j, d in enumerate(digits):
        if d % 2 == 0:
            x += (d//2) * 10**j
            y += (d//2) * 10**j
        else:
            x += (d//2 + int(f)) * 10**j
            y += (d//2 + int(not f)) * 10**j
            f ^= True
    print(x, y)