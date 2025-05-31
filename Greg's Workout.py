n = int(input())
vals = [*map(int, input().split())]
res = [0, 0, 0]
for i in range(len(vals)):
    res[i%3] += vals[i]
if max(res) == res[0]:
    print("chest")
elif max(res) == res[1]:
    print("biceps")
else:
    print("back")