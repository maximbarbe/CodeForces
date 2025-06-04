n = int(input())
vals = [*map(int, input().split())]
left = [0]*n
right = [0]*n
combined = []
for i in range(1, len(vals)):
    if vals[i] >= vals[i - 1]:
        left[i] = left[i - 1] + 1
for i in range(len(vals) - 2, -1, -1):
    if vals[i] >= vals[i + 1]:
        right[i] = right[i + 1] + 1        
for i in range(n):
    combined.append(left[i] + right[i])
print(max(combined) + 1)