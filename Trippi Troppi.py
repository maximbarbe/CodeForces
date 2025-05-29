n = int(input())
for i in range(n):
    words = input().split()
    print("".join([words[i][0] for i in range(len(words))]))