t = int(input())
for i in range(t):
    n, k, x = map(int, input().split())
    if k == x == 1:
        print("NO")
        continue
    if n == 1:
        if x == 1:
            print("NO")
        else:
            print("YES")
            print(1)
            print(1)
        continue
    elif n % 2 == 1:
        if k == 2 and x == 1:
            print("NO")
        else:
            if x != 1:
                print("YES")
                print(n)
                print(*[1]*n)
            else:
                print("YES")
                print(1 + (n-3)//2)
                res = [3] + [2]*((n-3)//2)
                print(*res)
    else:
        if x == 1:
            print("YES")
            print(n//2)
            print(*[2]*(n//2))
        else:
            print("YES")
            print(n)
            print(*[1]*n)
            
                    