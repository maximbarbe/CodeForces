t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    res = 0
    left = 0
    right = n - 1
    a = b= 0
    while left <= right:
        if a <= b:
            a += vals[left]
            left += 1
        else:
            b += vals[right]
            right -= 1
        if a == b:
            res = left + (n-1-right)
    print(res)