chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

t = int(input())
for i in range(t):
    n = input()
    numbers = []
    
    for j in range(1, len(n) +1):
        for v in chars:
            numbers.append(int(v* j))
    n = int(n)
    for k, val in enumerate(numbers):
        if val > n:
            print(k)
            break
    else:
        print(len(numbers))