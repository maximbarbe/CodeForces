t = int(input())
for i in range(t):
    a, b = input().split()
    print(b[0] + a[1:], a[0] + b[1:])