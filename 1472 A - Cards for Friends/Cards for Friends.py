t = int(input())
for i in range(t):
    w, h, n = map(int, input().split())
    cards = 1
    while w % 2 == 0:
        w //= 2
        cards *= 2
    while h % 2 == 0:
        h //= 2
        cards *= 2
    print("YES" if cards >= n else 'NO')
