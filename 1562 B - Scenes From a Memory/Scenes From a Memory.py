
def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
        
    return True

t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    for c in s:
        if c in "14689":
            print(1)
            print(c)
            break
    else:
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if not is_prime(v:=int(s[i] + s[j])):
                    print(2)
                    print(v)
                    break
            else:
                continue
            break
                
        else:
            print(n)
            print(s)