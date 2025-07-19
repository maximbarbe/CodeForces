
def res(a, b):
    for x, y, z in [(a, a, a), (a, a, b), (a, b, b), (b, b, b)]:
        if x + y > z and y + z > x and z + x > y:
            continue
        else:
            return False
    return True

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    for j in range(len(vals) - 1):
        if res(vals[j], vals[j + 1]):
            print("YES")
            break
    else:
        print("NO")