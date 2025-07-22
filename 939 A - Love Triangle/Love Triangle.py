n = int(input())
vals = [*map(lambda el:int(el) - 1, input().split())]

if n == 2:
    print("NO")
    exit()
for i in range(len(vals)):
    first = i
    sec = vals[first]
    third = vals[sec]
    if third != first and vals[third] == first:
        print("YES")
        break
else:
    print("NO")