t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    if a % 2 == b%2 == c%2:
        print(1, 1, 1)
    elif a%2 == b%2:
        print(0, 0, 1)
    elif a % 2 == c%2:
        print(0, 1, 0)
    elif b%2 == c%2:
        print(1, 0, 0)
    else:
        print(0, 0, 0)