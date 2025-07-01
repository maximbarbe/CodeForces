n = int(input())
if n % 7 == 0:
    print(n//7 * 2, n//7 * 2)
else:
    minimum = n//7 * 2
    if n % 7 == 6:
        print(minimum + 1, minimum + 2)
    else:
        print(minimum, minimum + min(n%7, 2))