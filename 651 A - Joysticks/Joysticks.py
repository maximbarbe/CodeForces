a1, a2 = map(int, input().split())
time = 0
while True:
    if a1 == 0 or a2 == 0:
        print(time)
        break
    if a1 == a2 == 1:
        print(time)
        break
    else:
        if a1 <= a2:
            a1 += 1
            a2 -= 2
        else:
            a2 += 1
            a1 -= 2
    time += 1