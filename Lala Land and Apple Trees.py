n = int(input())
negatives = []
positives = []
for i in range(n):
    xi, ai = map(int, input().split())
    if xi < 0:
        negatives.append((xi, ai))
    else:
        positives.append((xi, ai))
negatives.sort(key=lambda el:(-el[0], -el[1]))
positives.sort(key=lambda el:(el[0], -el[1]))
startsleft = 0
startsright = 0

i1 = 0
i2 = 0
left = True
while True:
    
    if left:
        if i1 == len(negatives):
            break
        startsleft += negatives[i1][1]
        i1 += 1
    else:
        if i2 == len(positives):
            break
        startsleft += positives[i2][1]
        i2 += 1
    left ^= True
left = False
i1 = 0
i2 = 0
while True:
    
    if left:
        if i1 == len(negatives):
            break
        startsright += negatives[i1][1]
        i1 += 1
    else:
        if i2 == len(positives):
            break
        startsright += positives[i2][1]
        i2 += 1
    left ^= True
print(max(startsleft, startsright))