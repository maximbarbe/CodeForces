from math import prod

fact = {
    "0": 1,
    "1": 1,
    "2": 2,
    "3": 6,
    "4": 24,
    "5": 120,
    "6": 720,
    "7": 720*7,
    "8": 720*7*8,
    "9": 720*7*8*9
}

def f(x):
    return prod([fact[digit] for digit in x])

n = int(input())
num = input()

val = f(num)
res = []
for factor in [7, 5, 3, 2]:
    while val % factor == 0:
        res.append(str(factor))
        val //= fact[str(factor)]
print("".join(res))