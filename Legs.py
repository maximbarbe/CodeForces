t = int(input())
for i in range(t):
    n = int(input())
    if n % 4 == 0:
        print(n//4)
    else:
        print(n//4 + 1)