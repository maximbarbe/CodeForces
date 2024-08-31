from collections import Counter

t = int(input())
for i in range(t):
    input()
    digits = Counter([*map(int, input().split())])
    if digits[0] > 1:
        print(0)
    elif digits[0] == 1:
        prod = 1
        for key, val in digits.items():
            if key == 0 or val == 0:
                continue
            else:
                prod *= pow(key, val)
        print(prod)
    else:
        max_res = 0
        for key in list(digits.keys()):
            if digits[key] != 0:
                digits[key] -= 1
                digits[key + 1] += 1
            else:
                continue
            prod = 1
            for k, v in digits.items():
                if v != 0:
                    prod *= pow(k, v)
                    
            digits[key + 1] -= 1
            digits[key] += 1
            if prod > max_res:
                max_res = prod
        print(max_res)
