t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a == b:
        print(0)
    elif a < b:
        if a % 2 == b % 2:
            print(2)
        else:
            print(1)
    else:
        if a % 2 != b % 2:
            print(2)
        else:
            print(1)