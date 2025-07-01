t = int(input())
for i in range(t):
    h, m = map(int, input().split())
    if h == 0 and m == 0:
        print(0)
    else:
        print((23 - h) * 60 + (60 - m))