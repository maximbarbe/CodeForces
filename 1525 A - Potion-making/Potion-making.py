t = int(input())
for i in range(t):
    k = int(input())
    minimum = 100
    for e in range(1, 101):
        w = e*(100-k)/k
        if int(w) == w:
            minimum = min(minimum, e  + int(w))
    print(minimum)