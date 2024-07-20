first = input()
second = input()
res = []
for i in range(len(first)):
    if first[i] != second[i]:
        res.append("1")
    else:
        res.append('0')
print("".join(res))
