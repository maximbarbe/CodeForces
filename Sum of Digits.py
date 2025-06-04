from sys import set_int_max_str_digits

set_int_max_str_digits(0)

def res(n):
    if len(n) < 2:
        return 0
    cur = 0
    for c in n:
        cur += int(c)
    return 1 + res(str(cur))
print(res(input()))
