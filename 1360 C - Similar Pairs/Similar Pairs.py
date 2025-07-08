t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    vals.sort()
    evens = 0
    odds = 0
    for v in vals:
        evens += int(v%2 == 0)
        odds += int(v%2 == 1)
    if evens%2 == 0 and odds%2 == 0:
        print("YES")
    else:
        for i in range(len(vals) - 1):
            if vals[i] + 1 == vals[i + 1]:
                print("YES")
                break
        else:
            print("NO")