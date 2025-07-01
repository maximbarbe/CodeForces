n = int(input())
if n >= 0:
    print(n)
else:
    str_rep = str(n)
    print(max(int(str_rep[:-1]), int(str_rep[:-2] + str_rep[-1])))