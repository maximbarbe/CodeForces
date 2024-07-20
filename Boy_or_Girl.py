from collections import Counter

line = Counter(input())
if len(line.keys()) % 2 == 1:
    print("IGNORE HIM!")
else:
    print("CHAT WITH HER!")