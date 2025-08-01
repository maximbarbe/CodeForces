from string import ascii_lowercase
from itertools import product



indices = dict()
cur = 1
for el in product(ascii_lowercase, ascii_lowercase):
    if el[0] != el[1]:
        indices["".join(el)] = cur
        cur += 1

for i in range(int(input())):
    print(indices[input()])