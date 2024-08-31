from collections import Counter

t = int(input())
for i in range(t):
    c = Counter(input())
    if c['A'] > c['B']:
        print('A')
    else:
        print('B')