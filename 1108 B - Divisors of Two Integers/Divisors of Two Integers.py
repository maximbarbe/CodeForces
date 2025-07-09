n = int(input())
vals =[*map(int, input().split())]
vals.sort()
v = vals[-1]
factors = [i for i in range(1, v + 1) if v%i == 0]
other = []
i = 0
j = 0
while i != len(vals) and j != len(factors):
    if vals[i] == factors[j]:
        i += 1
        j += 1
    else:
        other.append(vals[i])
        i += 1

while i != len(vals):
    other.append(vals[i])
    i += 1
print(v, other[-1])