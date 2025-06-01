n = int(input())
cards = [*map(int, input().split())]
given = [False]*n
target_sum = sum(cards)//(n//2)
for i in range(len(cards) - 1):
    if given[i]:
        continue
    for j in range(i + 1, len(cards)):
        if not given[j] and cards[i] + cards[j] == target_sum:
            given[i] = True
            given[j] = True
            print(i + 1, j+1)
            break
        