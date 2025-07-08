
f = lambda s:s==s[::-1]

n, m = map(int, input().split())
taken = dict()
moves = []

words = []
palindromes = []
for i in range(n):
    cur = input()
    for j in range(len(words)):
        if words[j] == cur[::-1]:
            moves.append((cur, words[j]))
            taken[i] = True
            taken[j] = True
    words.append(cur)

for i in range(len(words)):
    if not taken.get(i, False) and f(words[i]):
        palindromes.append(words[i])
        
left = []
right = []
for u, v in moves:
    left.append(u)
    right.append(v)
if not palindromes:
    palindromes.append("")
right = right[::-1]
res = "".join(left) + palindromes[0] + "".join(right)
print(len(res))
print(res)