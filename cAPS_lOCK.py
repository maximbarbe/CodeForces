string = input()
rule1 = True
rule2 = True
for idx, char in enumerate(string):
    if char.islower():
        rule1 = False
        if idx != 0:
            rule2 = False
if rule1 or rule2:
    print(string.swapcase())
else:
    print(string)
    