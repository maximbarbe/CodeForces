string = input()
conv = {input():str(i) for i in range(10)}
res = ""
for i in range(0, len(string), 10):
    res += conv[string[i:i+10]]
print(res)