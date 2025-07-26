t = int(input())
MOD = 10**9 + 7
for i in range(t):
    n, k = map(int, input().split())
    vals = [*map(int, input().split())]
    m = max(vals)
    if m <= 0:
        print(sum(vals)%MOD)
    else:
        m = 0
        cur = 0
        for v in vals:
            if cur + v >= 0:
                cur += v
            else:
                cur = 0
            m = max(cur, m)
        s = sum(vals) - m
        
        print((s + (m*pow(2, k, MOD))%MOD)%MOD)