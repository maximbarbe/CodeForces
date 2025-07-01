vals = []
n = int(input())
for i in range(n):
    if i == n - 1:
        if i % 2 == 0:
            vals.append("I hate it")
        else:
            vals.append("I love it")
    else:    
        if i % 2 == 0:
            vals.append("I hate that")
        else:
            vals.append("I love that")
print(" ".join(vals))