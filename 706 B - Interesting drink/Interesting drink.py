from bisect import bisect_right

n = int(input())
prices = [*map(int, input().split())]
q = int(input())
prices.sort()
for i in range(q):
    m = int(input())
    idx = bisect_right(prices, m)
    print(bisect_right(prices, m))