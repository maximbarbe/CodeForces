s = input()
m = input()
if s == "0":
    if m == "0":
        print("OK")
    else:
        print("WRONG_ANSWER")
    exit()
zeros = []
digits = []
for c in s:
    if c == "0":
        zeros.append("0")
    else:
        digits.append(c)
digits.sort()
res = digits[0] + "".join(zeros) + "".join(digits[1:])
if res == m:
    print("OK")
else:
    print("WRONG_ANSWER")