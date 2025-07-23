t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    prefix_max = [0]*n
    suffix_sum = [0]*n
    for i in range(len(vals)):
        if i == 0:
            prefix_max[i] = vals[i]
            suffix_sum[n - 1 - i] = vals[n - 1 - i]
        else:
            prefix_max[i] = max(vals[i], prefix_max[i - 1])
            suffix_sum[n-1-i] = vals[n - 1 - i] + suffix_sum[n - i]
    
    res = []
    suffix_sum.append(0)
    for i in range(0, n):
        m = prefix_max[n-i-1]
        res.append(suffix_sum[n-i] + m)
    print(*res)