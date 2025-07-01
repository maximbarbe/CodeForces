t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())

    if (a-1) < abs(c-b) + c-1:
        print(1)
    elif (a-1) > abs(c- b) + c - 1:
        print(2)
    else:
        print(3)