n, m = map(int, input().split())
count = [0]*(n+1)
vals = [*map(int, input().split())]
seen = set()
for i in range(len(vals) - 1, -1, -1):
    if vals[i] in seen:
        count[i] = count[i + 1]
    else:
        seen.add(vals[i])
        count[i] = 1 + count[i + 1]
    
for j in range(m):
    li = int(input())
    print(count[li - 1])