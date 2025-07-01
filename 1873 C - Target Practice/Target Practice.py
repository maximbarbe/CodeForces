t = int(input())

for i in range(t):
    points = 0
    for j in range(10):
        row = input()
        for k in range(len(row)):
            if row[k] == "X":
                if j == 0 or j == 9 or k == 0 or k == 9:
                    points += 1
                elif j == 1 or j == 8 or k == 1 or k == 8:
                    points += 2
                elif j == 2 or j == 7 or k == 2 or k == 7:
                    points += 3
                elif j == 3 or j == 6 or k == 3 or k == 6:
                    points += 4
                else:
                    points += 5
    print(points)