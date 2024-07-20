from collections import Counter
n = int(input())
res = set([*map(int, input().split())])
if 1 in res:
    print("HARD")
else:
    print("EASY")