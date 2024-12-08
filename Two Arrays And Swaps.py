t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    first = sorted([*map(int, input().split())])
    sec = sorted([*map(int, input().split())], reverse=True)
    cur = 0
    while k != 0 and cur != n:
        if sec[cur] > first[cur]:
            first[cur] = sec[cur]
            cur += 1
            k -= 1
        else:
            break
    print(sum(first))