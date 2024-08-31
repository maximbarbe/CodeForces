n, t = map(int, input().split())
for i in range(10**(n-1), 10**n):
    if i % t == 0:
        print(i)
        exit()
else:
    print(-1)