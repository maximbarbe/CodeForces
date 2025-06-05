from math import factorial


while True:
    n, m = map(int, input().lstrip().split())
    if n == m == 0:
        break
    value = (factorial(n)//factorial(m))//factorial(n - m)
    print("{0} things taken {1} at a time is {2} exactly.".format(n, m, value))
    