t = int(input())
for i in range(t):
    n = int(input())
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    for j in range(n):
        if b[j] > a[j]:
            a[j], b[j] = b[j], a[j]
    print(max(a)*max(b))