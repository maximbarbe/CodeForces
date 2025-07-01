n = int(input())
birds = [*map(int, input().split())]
m = int(input())
for i in range(m):
    x, y = map(lambda el:int(el) - 1, input().split())
    if x == 0 and x == n - 1:
        birds[x] = 0
    elif x == 0:    
        birds[x + 1] += birds[x] - (y + 1)
        birds[x] = 0
    elif x == n-1:
        birds[x - 1] += y
        birds[x] = 0
    else:
        birds[x - 1] += y
        birds[x + 1] += birds[x] - (y + 1)
        birds[x] = 0
for v in birds:
    print(v)