year = int(input()) + 1
while True:
    str_rep = str(year)
    if len(set(str_rep)) == len(str_rep):
        print(year)
        exit()
    year += 1 
