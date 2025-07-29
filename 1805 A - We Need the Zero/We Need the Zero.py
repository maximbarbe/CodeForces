t = int(input())
for i in range(t):
    n = int(input())
    arr = [*map(int, input().split())]
    cur = arr[0]
    for i in range(1, len(arr)):
        cur ^= arr[i]
    if n % 2 == 0:
        if cur == 0:
            print(0)
        else:
            print(-1)
    else:
        print(cur)