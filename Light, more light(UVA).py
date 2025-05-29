while True:
    n = int(input())
    if n == 0:
        break
    if int(n**0.5)==n**0.5:
        print("yes")
    else:
        print("no")