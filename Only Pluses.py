from math import prod
import heapq

t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    heap = [a, b, c]
    heapq.heapify(heap)
    for i in range(5):
        cur = heapq.heappop(heap) + 1
        heapq.heappush(heap, cur)
    print(prod(heap))