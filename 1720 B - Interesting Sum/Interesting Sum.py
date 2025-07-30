t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    vals.sort()
    print(vals[-1] + vals[-2] - vals[0] - vals[1])