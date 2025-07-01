word = input()
lower = 0
upper = 0
for char in word:
    if char == char.lower():
        lower += 1
    else:
        upper += 1
if lower >= upper:
    print(word.lower())
else:
    print(word.upper())