from math import floor

t = int(input())
for i in range(t):
    n = int(input())
    cur = 0
    for x in range(floor(n/2020) + 1):
        
        if (n - cur)%2021 == 0:
            print("YES")
            break
        cur += 2020
    else:
        print("NO")