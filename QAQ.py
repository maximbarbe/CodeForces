string = input()
res = 0
for i in range(len(string) - 2):
    if string[i] == "Q":
        for j in range(i + 1, len(string) - 1):
            if string[j] == "A":
                for k in range(j + 1, len(string)):
                    if string[k] == "Q":
                        res += 1
print(res)