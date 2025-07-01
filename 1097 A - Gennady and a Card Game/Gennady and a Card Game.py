card = input()
cards = input().split()
for c in cards:
    if card[0] == c[0] or card[1] == c[1]:
        print("YES")
        exit(0)
else:
    print("NO")