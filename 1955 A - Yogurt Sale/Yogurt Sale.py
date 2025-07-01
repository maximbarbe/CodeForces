t = int(input())
for i in range(t):
    n, a, b = map(int, input().split())
    if n == 1:
        print(a)
    else:
        if b // 2< a:
            if n % 2 == 0:
                print((n//2) * b)
            else:
                print((n//2)*b + a)
        else:
            print(n*a)