n, k = map(int, input().split())
s = input()
a = 0
b = 0
l = r = 0
m = 0
for c in s:
    if c == "a":
        a += 1
    else:
        b += 1
    r += 1
    if min(a, b) <= k:
        m = max(a + b, m)
    else:
        while min(a, b) > k:
            if s[l] == "a":
                a -= 1
            else:
                b -= 1
            l += 1
print(m)