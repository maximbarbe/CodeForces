string = input().split("WUB")
words = []
for t in string:
    if t != "":
        words.append(t)
print(" ".join(words))