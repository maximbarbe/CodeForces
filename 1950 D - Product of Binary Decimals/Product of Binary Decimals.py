from collections import defaultdict, deque


binary_decimals = [1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010, 1011, 1100, 1101, 1110,1111, 10000, 10001, 10010, 10011, 10100, 10101, 10110, 10111, 11000, 11001, 11010, 11011, 11100, 11101, 11110, 11111, 100000]

seen = defaultdict(lambda:False)
seen[0] = True
for v in binary_decimals:
    seen[v] = True
q = deque(binary_decimals)
lim = 10**5
while q:
    cur = q.popleft()
    for v in binary_decimals:
        prod = cur*v
        if not seen[prod] and prod < lim:
            seen[prod] = True
            q.append(prod)
            
t = int(input())
for i in range(t):
    if seen[int(input())]:
        print("YES")
    else:
        print("NO")