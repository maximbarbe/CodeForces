t = int(input())
for i in range(t):
    n = int(input())
    vals = set([*map(lambda el:int(el) % 2, input().split())])
    if len(vals) == 1:
        print("YES")
    else:
        print('NO')