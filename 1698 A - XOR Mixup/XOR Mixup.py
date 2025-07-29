t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    vals.sort()
    prefix = [0]*n
    suffix = [0]*n
    for i in range(len(vals)):
        if i == 0:
            prefix[i] = vals[i]
            suffix[n  - 1] = vals[n  - 1]
        else:
            prefix[i] = vals[i] ^ prefix[i - 1]
            suffix[n - i - 1] = vals[n - i - 1] ^suffix[n - i]
    for i in range(len(vals)):
        if i == 0:
            before = 0
            after = suffix[i + 1]
        elif i == n-1:
            before = prefix[i - 1]
            after = 0
        else:
            before = prefix[i - 1]
            after = suffix[i + 1]
        if before ^after == vals[i]:
            print(vals[i])
            break
            