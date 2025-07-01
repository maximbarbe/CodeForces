n=  int(input())
s = input()
res = [None]*n
indices = [i for i in range(n)]
for i in range(n):
    if len(indices) % 2 == 1:
        median = indices[len(indices)//2]
        indices.pop(len(indices)//2)
    else:    
        median = indices[len(indices)//2 - 1]
        indices.pop(len(indices)//2 - 1)
    res[median] = s[i]
print("".join(res))