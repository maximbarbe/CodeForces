t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    vals.sort()
    diff = 10**12
    for i in range(len(vals) - 1):
        if abs(vals[i] - vals[i + 1]) < diff:
            diff = abs(vals[i] - vals[i + 1])
    print(diff)