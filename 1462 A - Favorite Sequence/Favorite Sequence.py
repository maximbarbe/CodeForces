t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    res = []
    left = 0
    right = n- 1
    while left <= right:
        if left == right:
            res.append(vals[left])
            left += 1
        else:
            res.append(vals[left])
            res.append(vals[right])
            left += 1
            right -= 1
    print(*res)