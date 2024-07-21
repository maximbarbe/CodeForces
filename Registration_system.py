n = int(input())
register = dict()
for i in range(n):
    name = input()
    if name not in register:
        print("OK")
        register[name] = 1
    else:
        print(f"{name}{register[name]}")
        register[name] += 1