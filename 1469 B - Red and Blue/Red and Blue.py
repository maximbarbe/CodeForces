t = int(input())
for i in range(t):
    n = int(input())
    v1 = [*map(int, input().split())]
    pref1 = [0]*n
    m = int(input())
    v2 = [*map(int, input().split())]
    pref2 = [0]*m
    for i in range(n):
        pref1[i] = v1[i] + pref1[i - 1]
    for i in range(m):
        pref2[i] = v2[i] + pref2[i - 1]
    print(max(0, max(pref1) + max(pref2), max(pref1), max(pref2)))