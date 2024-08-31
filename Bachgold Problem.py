n = int(input())
if n % 2 == 0:
    print(n//2)
    print(" ".join(['2'] * (n//2)))
else:
    if n == 3:
        print(1)
        print(3)
        exit()
    print(1 + (n -3)//2)
    print(" ".join(['2'] * ((n-3)//2)), 3)