from math import floor

t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    print(k + floor((k-1)/(n-1)))