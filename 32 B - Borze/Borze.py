string = input()
digits = {
    ".": "0",
    "-.": "1",
    "--": "2"
}
res = ""
i = 0
while i != len(string):
    if i == len(string) - 1:
        res += "0"
        break
    else:
        if string[i] + string[i + 1] in digits.keys():
            res += digits[string[i] + string[i + 1]]
            i += 2
        else:
            res += "0"
            i += 1
print(res)