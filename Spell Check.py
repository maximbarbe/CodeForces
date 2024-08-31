from collections import Counter

c = Counter("Timur")
t = int(input())
for i in range(t):
    input()
    print('YES' if Counter(input()) == c else 'NO')