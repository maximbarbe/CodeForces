a, b, c= map(int, input().split())
if (a*c)%b != 0:
    data_needed = a*c + b - (a*c)%b
else:
    data_needed = a*c
print(data_needed//b - c)
