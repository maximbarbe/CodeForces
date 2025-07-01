s = input()
n = int(input())
words = [input() for i in range(n)]
words = [word for word in words if word.startswith(s)]
if not words:
    print(s)
else:
    words.sort()
    print(words[0])