from collections import Counter

guest = Counter(input())
host = Counter(input())
pile = Counter(input())
pile.subtract(host)
pile.subtract(guest)
for val in pile.values():
    if val != 0:
        print("NO")
        exit()
print("YES")