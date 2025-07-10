t = int(input())
for i in range(t):
    n= int(input())
    vals = [*map(int, input().split())]
    s = input()
    liked = []
    disliked = []
    ones = 0
    zeros = 0
    for i in range(len(vals)):
        if s[i] == "1":
            ones += 1
            liked.append((vals[i], i))
        else:
            zeros += 1
            disliked.append((vals[i], i))
    liked.sort()
    disliked.sort()
    res = [None]*n
    for i in range(1, zeros + 1):
        res[disliked[i - 1][1]] = i
    for idx, j in zip(range(ones), range(zeros + 1, n+1)):
        res[liked[idx][1]] = j
    print(*res)
            