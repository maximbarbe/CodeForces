p, n = map(int, input().split())
buckets = [None]*p
for i in range(n):
    k = int(input())%p
    if buckets[k] != None:
        print(i + 1)
        exit()
    buckets[k] = 1
print(-1)