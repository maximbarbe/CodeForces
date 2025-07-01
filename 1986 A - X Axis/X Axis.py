t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    min_dist = 10**9
    for i in range(0, 11):
        d = abs(a - i) + abs(b - i) + abs(c- i )
        if d < min_dist:
            min_dist= d
    print(min_dist)