t = int(input())
for i in range(t):
    n = int(input())
    print(sum(map(lambda el:abs(int(el)), input().split())))
    