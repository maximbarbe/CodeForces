order = "qwertyuiopasdfghjkl;zxcvbnm,./"
idx = {order[i]:i for i in range(len(order))}
c = input()
s = input()
if c == "R":
    res = ""
    for char in s:
        res += order[idx[char] - 1]
    print(res)
else:
    res = ""
    for char in s:
        res += order[idx[char] + 1]
    print(res)