t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    vals = [*map(int, input().split())]
    odds = 0
    evens = 0

    for v in vals:
        odds += v%2
        evens += v%2 == 0
    if odds == 0:
        print("NO")
        continue
    if x % 2 == 1:
        cur = 0
        while True:
            if odds >= x-cur:
                print("YES")
                break
            else:
                if cur + 2 <= evens:
                    cur += 2
                else:
                    print("NO")
                    break
    else:
        if evens == 0:
            print("NO")
        else:
            cur = 1
            while True:
                if odds >= x - cur:
                    print("YES")
                    break
                else:
                    if cur + 2 <= evens:
                        cur += 2
                    else:
                        print("NO")
                        break
            