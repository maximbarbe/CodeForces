n = int(input())
vals = [*map(int, input().split())]
x, y= map(int, input().split())
left = 0
right = sum(vals)
for i in range(len(vals)):
    if x <= left <= y and x <= right <= y:
        print(i + 1)
        exit()
    left += vals[i]
    right -= vals[i]

print(0)