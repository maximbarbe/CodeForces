n = int(input())
left = 0
right = n - 1
s = 0
d = 0
vals = [*map(int, input().split())]
sereja = True
while left <= right:
    if sereja:
        if vals[left] > vals[right]:
            s += vals[left]
            left += 1
        else:
            s += vals[right]
            right -= 1
    else:
        if vals[left] > vals[right]:
            d += vals[left]
            left += 1
        else:
            d += vals[right]
            right -= 1
    sereja ^= True
print(s, d)
    