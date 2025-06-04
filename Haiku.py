syllables = [5, 7, 5]
lines = [input() for i in range(3)]
for i, l in enumerate(lines):
    vowels = l.count("a") + l.count("e") + l.count("i") + l.count("o") + l.count("u")
    if vowels != syllables[i]:
        print("NO")
        exit()
print("YES")