import sys

sys.set_int_max_str_digits(0)
n = int(input())
print((1 + pow(2, n, 5) + pow(3, n, 5) + pow(4, n, 5))%5)