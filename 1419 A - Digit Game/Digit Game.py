t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    # Le dernier nombre aura un index pair.
    if n % 2 == 0:
        for i in range(n):
            if (i+1)%2 == 0 and s[i] in "02468":
                print(2)
                break
        else:
            print(1)
    else:
        for i in range(n):
            if (i+1)%2 == 1 and s[i] in "13579":
                print(1)
                break
        else:
            print(2)