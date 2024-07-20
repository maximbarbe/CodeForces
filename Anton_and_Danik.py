from collections import Counter

n = input()
wins = Counter(input())
if wins['A'] > wins['D']:
    print("Anton")
elif wins['D'] > wins['A']:
    print("Danik")
else:
    print("Friendship")