n = int(input())
vals = [*map(int, input().split())]
negatives = []
positives = []
zeros = []
for v in vals:
    if v < 0:
        negatives.append(v)
    elif v > 0:
        positives.append(v)
    else:
        zeros.append(v)
s1 = []
s2 = []
s3 = []
s3.append(0)
if len(negatives) == 1:
    s1.append(negatives[0])
else:
    if len(negatives) % 2 == 0:
        s1.append(negatives[0])
        for i in range(1, len(negatives) - 1):
            s2.append(negatives[i])
        s3.append(negatives[-1])
    else:
        s1.append(negatives[0])
        for i in range(1, len(negatives)):
            s2.append(negatives[i])
for v in positives:
    s2.append(v)
    
print(len(s1), *s1)
print(len(s2), *s2)
print(len(s3), *s3)