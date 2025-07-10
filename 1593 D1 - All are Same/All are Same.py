from math import inf, sqrt

def get_factors(n):

    factors = set()
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n//i)
    return factors

t = int(input())
for i in range(t):
    n = int(input())
    vals = [*map(int, input().split())]
    if len(set(vals)) == 1:
        print(-1)
        continue
    vals = sorted(set(vals))
    possible = None
    for i in range(len(vals) - 1):
        for j in range(i + 1, len(vals)):
            f = get_factors(vals[j] - vals[i])
            if possible == None:
                possible = f
            else:
                possible = possible.intersection(f)
    print(max(possible))