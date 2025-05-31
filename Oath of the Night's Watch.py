n = int(input())
vals = [*map(int, input().split())]
vals.sort()
smaller = [False]*n
bigger = [False]*n
for i in range(len(vals)):
    if i == 0:
        smaller[i] = False
    else:
        if vals[i] > vals[i - 1]:
            smaller[i] = True
        elif vals[i] == vals[i - 1] and smaller[i-1] == True:
            smaller[i] = True
        else:
            smaller[i] = False
            
for i in range(len(vals) -2, -1, -1):
    if vals[i] < vals[i + 1]:
        bigger[i] = True
    elif vals[i] == vals[i + 1] and bigger[i + 1] == True:
        bigger[i] = True
res = 0
for i in range(n):
    if bigger[i] and smaller[i]:
        res += 1
print(res)