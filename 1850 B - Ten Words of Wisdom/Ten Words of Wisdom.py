t = int(input())
for i in range(t):
    n = int(input())
    max_qual = 0
    res = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a <= 10 and b > max_qual:
            max_qual = b
            res = i + 1
            
    print(res)