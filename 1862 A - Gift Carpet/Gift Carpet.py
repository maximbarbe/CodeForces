t = int(input())
for i in range(t):
    word = "vika"
    idx = 0
    words = []
    n, m = map(int, input().split())
    for i in range(n):
        words.append(input())
    for j in range(m):
        for i in range(n):
            if words[i][j] == word[idx]:
                idx += 1
                break
        if idx == len(word):
            print("YES")
            break
    else:
        print("NO")
            
    