from collections import defaultdict

k = int(input())
freq = defaultdict(lambda:0)
for i in range(4):
    row = input()
    for c in row:
        if c != ".":
            freq[int(c)] += 1
for i in range(1, 10):
    if freq[i] > 2*k:
        print("NO")
        exit()
print("YES")