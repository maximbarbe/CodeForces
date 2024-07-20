t = int(input())
for i in range(t):
    n = int(input())
    values = [*map(int, input().split())]
    values.sort(reverse=True)
    while len(values) != 1:
        if abs(values[-1] - values[-2]) > 1:
            print("NO")
            break
        else:
            values.pop(-1)
        
    else:
        print("YES")