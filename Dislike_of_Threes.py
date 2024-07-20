sequence = []
cur = 1
while len(sequence) != 1000:
    if cur % 3 != 0 and cur % 10 != 3:
        sequence.append(cur)
    cur += 1
t = int(input())
for i in range(t):
    print(sequence[int(input()) - 1])