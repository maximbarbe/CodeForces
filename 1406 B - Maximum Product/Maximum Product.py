from math import prod

for i in range(int(input())):
    n = int(input())
    vals = sorted([*map(int, input().split())])
    print(max(vals[0]*vals[1]*vals[-1]*vals[-2]*vals[-3], vals[0]*vals[1]*vals[2]*vals[3]*vals[-1], vals[-5]*vals[-4]*vals[-1]*vals[-2]*vals[-3]))