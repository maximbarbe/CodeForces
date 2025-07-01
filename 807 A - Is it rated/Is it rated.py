n = int(input())
rated = False
ratings = []
for i in range(n):
    a, b = map(int, input().split())
    if a != b:
        rated = True
    ratings.append((a, b))
if rated:
    print("rated")
else:
    minimum = 10**9
    maybe = True
    for a, b in ratings:
        if a <= minimum:
            minimum = a
        else:
            maybe = False
            break
    if maybe:
        print("maybe")
    else:
        print("unrated")