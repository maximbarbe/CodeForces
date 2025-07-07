sieve = [True]*30001
sieve[0] = sieve[1] = False
for i in range(2, 30001):
    for j in range(2, 30_000//i + 1):
        sieve[i * j] = False
        
primes = [i for i in range(len(sieve)) if sieve[i]]

t = int(input())
for i in range(t):
    d = int(input())
    first = None
    sec = None
    for v in primes:
        if not first:
            if v - 1 >= d:
                first = v
        else:
            if v - first >= d:
                second = v
                break
    print(first*second)