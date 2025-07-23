t = int(input())
for i in range(t):
    s = input()
    pieces = []
    cur = [-1]
    
    for c in s:
        if int(c) >= cur[-1]:
            cur.append(int(c))
        else:
            pieces.append(cur)
            cur = [int(c)]
    else:
        pieces.append(cur)

    zero_and_ones = 0
    
    for p in pieces:
        zero = False
        one = False
        for v in p:
            zero |= v == 0
            one |= v == 1
        if zero and one:
            zero_and_ones += 1
    if zero_and_ones:
        print(len(pieces) + zero_and_ones - 1)
    else:
        print(len(pieces))