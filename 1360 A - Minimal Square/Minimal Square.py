t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if max(a, b) <= 2*min(a, b):
        print((2*min(a, b))**2)
    else:
        print(max(a, b)**2)