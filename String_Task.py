word = input().lower()
res = []
vowels = "aeiouy"
for char in word:
    if char not in vowels:
        res.append(".")
        res.append(char)
print("".join(res))