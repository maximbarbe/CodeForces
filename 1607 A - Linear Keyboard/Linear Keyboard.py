t = int(input())
for i in range(t):
    keys = input()
    keyboard = {keys[i]:i for i in range(len(keys))}
    word = input()
    res = 0
    for i in range(len(word) - 1):
        res += abs(keyboard[word[i]] - keyboard[word[i + 1]])
        
    print(res)