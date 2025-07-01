# Use triangle inequality
# For a non-degenerate triangle of sides a, b,c
# The three inequalities follow:
# a + b > c, a + c > b, b + c > a
# Since c > b and b > a, the two last are trivial.
# We have to find a,b and c s.t. a + b > c


n = int(input())
v = sorted([*map(int, input().split())])

for i in range(1, n-1):
    a = v[i - 1]
    b = v[i]
    c = v[i + 1]
    if a + b > c:
        print("YES")
        exit()
else:
    print("NO")