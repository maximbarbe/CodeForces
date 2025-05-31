from collections import defaultdict

keys = defaultdict(lambda:0)
input()
string = input()
res = 0
for c in string:
    if c.isupper():
        if keys[c.lower()] == 0:
            res += 1
        else:
            keys[c.lower()] -= 1
    else:
        keys[c] += 1
print(res)