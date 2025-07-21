import heapq
 
for i in range(int(input())):
    n, m, L = map(int, input().split())
    events = []
    for i in range(n):
        l, r = map(int, input().split())
        events.append((l, r, 1))
    for i in range(m):
        x, v = map(int, input().split())
        events.append((x, v, 2))
    events.sort(key=lambda el:el[0])
    cur = 1
    res = 0
    jump = 1
    heap = []
    for event in events:
        if cur >= L:
            print(res)
            break
        else:
            if event[2] == 2:
                x, v, _ = event
                cur = x
                heapq.heappush(heap, -v)
            else:
                l, r, _ = event
                cur = l - 1
                while heap and l <= cur + jump <= r:
                    jump += -heapq.heappop(heap)
                    res += 1
                if l <= cur + jump <= r:
                    print(-1)
                    break
    else:
        print(res)