cur = 0
s = input()
res = 0
for c in s:
    if ord(c) - ord('a') > cur:
        res += min(ord(c) - ord('a') - cur, cur + 26 - (ord(c) - ord('a')))
    else:
        res += min(cur - (ord(c) - ord('a')), (ord(c) - ord('a')) + 26 - cur)
    cur = ord(c) - ord('a')
print(res)