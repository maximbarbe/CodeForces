t = int(input())
for i in range(t):
    n = int(input())
    if n in [1, 2]:
        print(0)
    else:
        if n % 2 == 1:
            print(n//2)
        else:
            print(n//2 - 1)