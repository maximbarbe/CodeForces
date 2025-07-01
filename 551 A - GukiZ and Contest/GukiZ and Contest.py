n = int(input())
scores = [*map(int, input().split())]
scores = [(scores[i], i) for i in range(len(scores))]
res = [None]*n
scores.sort(key=lambda el:-el[0])
prev = None
for i in range(len(scores)):
    if i == 0:
        res[scores[i][1]] = 1
    else:
        if scores[i][0] == scores[i - 1][0]:
            res[scores[i][1]] = res[scores[i - 1][1]]
        else:
            res[scores[i][1]] = i + 1
print(*res)