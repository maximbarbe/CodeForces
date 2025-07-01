from math import factorial

s1 = input()
s2 = input()

plus_1 = s1.count("+")
minus_1 = s1.count("-")
plus_2 = s2.count("+")
minus_2 = s2.count("-")
diff_plus = plus_1 - plus_2
diff_minus = minus_1 - minus_2
if diff_plus < 0 or diff_minus < 0:
    print(0)
else:
    res = 0.5**(diff_plus + diff_minus) * factorial(diff_minus + diff_plus)/(factorial(diff_minus)*factorial(diff_plus))
    print(res)