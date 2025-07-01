letters = "abcdefghijklmnopqrstuvwxyz"

n, k = map(int, input().split())

letters = letters[:k]

res = ""
idx = 0
while len(res) != n:
    res += letters[idx]
    idx = (idx + 1)%k
print(res)