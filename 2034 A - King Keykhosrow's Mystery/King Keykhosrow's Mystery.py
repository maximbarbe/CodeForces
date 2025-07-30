from math import lcm


t = int(input())
for i in range(t):
    print(lcm(*map(int, input().split())))