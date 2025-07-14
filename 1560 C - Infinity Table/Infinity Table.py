from math import ceil, floor

t = int(input())
for i in range(t):
    n = int(input())
    if int(n**0.5)**2 == n:
        lower = floor(n**0.5) - 1
        higher = ceil(n**0.5)
    else:
        lower = floor(n**0.5)
        higher = ceil(n**0.5)
    mid = (lower**2 + higher**2)//2
    if n <= mid:
        col = higher
        row = n - lower**2
        print(row, col)
    else:
        row = higher
        col = higher**2 - n + 1
        print(row, col)