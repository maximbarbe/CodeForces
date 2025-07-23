

n, m = map(int, input().split())

minimum = 10**6
for y in range(n//2 + 1):
    x = n - 2*y
    if (x + y)%m == 0:
        minimum = min(x + y, minimum) 
if minimum == 10**6:
    print(-1)
else:
    print(minimum)