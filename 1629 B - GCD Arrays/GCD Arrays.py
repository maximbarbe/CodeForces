t = int(input())
for i in range(t):
    l, r, k = map(int, input().split())
    if r == l:
        if l == 1:
            print("NO")
        else:
            print("YES")
    else:
        odds = 0
        if l % 2 == 1:
            l += 1
            odds += 1
        if r % 2 == 1:
            r -= 1
            odds += 1
        odds += (r -l)//2
        if odds > k:
            print("NO")
        else:
            print("YES")