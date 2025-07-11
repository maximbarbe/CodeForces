n = int(input())
vals =[*map(int, input().split())]
vals.sort()
day = 1
for v in vals:
    if v >= day:
        day += 1
print(day-1)